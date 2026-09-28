"""Independent re-computation of an episode's model, by model kind (K2). The episode contract (contract.json `model`) names the kind, its
parameters and its output file; the checker owns one re-implementation per kind, written from the brief, never from the builder's code.
A kind the checker has no re-implementation for is MISSING (S01, S05): the checker does not guess a model.

Each kind gives:
  compare(ctx, params, out)  -> (checked, mismatches, notRecomputed)   value-by-value comparison with the model output (S01)
  value(ctx, params, key)    -> float                                   a recomputed quantity a claim can be mapped to (S05)
  invariants(ctx, params)    -> [metric]                                 statements the episode's thesis rests on (S05)
"""
import csv
import math

import numpy as np

from common import Missing, metric


def _need(params, *keys):
    for k in keys:
        if k not in params or params[k] is None:
            raise Missing('contract.json: model.params.' + k)
    return [params[k] for k in keys]


def close(a, b, abs_tol=0.5, rel=1e-6):
    return abs(a - b) <= max(abs_tol, rel * abs(b))


# ---- kind "retirement-6040" (test D: same average, different fate) ----------------------------------------
def _annual(ctx, params):
    (rel,) = _need(params, 'annual')
    rows = list(csv.DictReader(open(ctx.need(rel))))
    return {int(r['year']): (float(r['stocks']), float(r['bonds']), float(r['inflation'])) for r in rows}


def _simulate(seq, initial, rate, ws_, wb_):
    """Withdraw at the start of each year: year 1 = rate × initial, later years = previous withdrawal × (1 + previous year's inflation).
    The rest earns the stock/bond return (rebalanced yearly). Returns withdrawals, end nominal, end real (start-year dollars), depleted year or None."""
    B, W = float(initial), rate * initial
    ws, en, er, dep = [], [], [], None
    price = 1.0
    for k, (s, b, inf) in enumerate(seq):
        if k > 0:
            W *= 1 + seq[k - 1][2]
        take = min(W, B)
        if dep is None and B < W:
            dep = k + 1
        B = (B - take) * (1 + ws_ * s + wb_ * b)
        price *= 1 + inf
        ws.append(take)
        en.append(B)
        er.append(B / price)
    return ws, en, er, dep


def _path_seq(data, spec, years):
    """A named path: `from` = first year; `reverse` ⊇ {"returns"} plays the returns backwards (and the inflation too if listed)."""
    y0 = int(spec['from'])
    base = [data[y] for y in range(y0, y0 + years)]
    rev = set(spec.get('reverse', []))
    if not rev:
        return base
    if 'returns' not in rev:
        raise Missing('contract.json: model.params.paths.*.reverse must include "returns"')
    rr = base[::-1]
    return [(rr[k][0], rr[k][1], (rr[k] if 'inflation' in rev else base[k])[2]) for k in range(years)]


def _ret_params(params):
    rate, years, w, starts, paths = _need(params, 'rate', 'years', 'weights', 'startRange', 'paths')
    return float(rate), int(years), (float(w['stocks']), float(w['bonds'])), (int(starts[0]), int(starts[1])), paths


def ret_compare(ctx, params, out):
    data = _annual(ctx, params)
    rate, years, (ws_, wb_), (s0, s1), paths = _ret_params(params)
    init = float(out['initial'])
    bad, checked = [], 0
    for k, want in (('rate', rate), ('years', years), ('tax', 0), ('fees', 0)):
        if out.get(k, 0 if k in ('tax', 'fees') else None) != want:
            bad.append((k, out.get(k), want))
    if [out.get('weights', {}).get('stocks'), out.get('weights', {}).get('bonds')] != [ws_, wb_]:
        bad.append(('weights', out.get('weights'), [ws_, wb_]))

    def cmp(key, seq, p):
        nonlocal checked
        w, en, er, dep = _simulate(seq, init, rate, ws_, wb_)
        for name, mine in (('withdrawals', w), ('endNominal', en), ('endReal', er)):
            theirs = p.get(name)
            if theirs is None:
                bad.append((key, name, 'missing'))
                continue
            for k, (a, b) in enumerate(zip(theirs, mine)):
                checked += 1
                if not close(a, b):
                    bad.append((key, name, k + 1, round(a, 2), round(b, 2)))
                    break
            if len(theirs) != len(mine):
                bad.append((key, name, 'length', len(theirs)))
        if p.get('depletedYear', None) != dep:
            bad.append((key, 'depletedYear', p.get('depletedYear'), dep))

    for key, spec in paths.items():
        p = out.get('paths', {}).get(key)
        if p is None:
            bad.append((key, 'path missing'))
            continue
        cmp(key, _path_seq(data, spec, years), p)
    for y in range(s0, s1 + 1):
        p = out.get('starts', {}).get(str(y))
        if p is None:
            bad.append((y, 'start year missing'))
            continue
        cmp(str(y), [data[k] for k in range(y, y + years)], p)
    covered = {'initial', 'rate', 'years', 'weights', 'tax', 'fees', 'paths', 'starts'}
    return checked, bad, sorted(set(out) - covered)


def _geo(seq, ws_, wb_):
    return float(np.prod([1 + ws_ * s + wb_ * b for s, b, _ in seq]) ** (1 / len(seq)) - 1)


def ret_value(ctx, params, key):
    """"geomean:<path>" = geometric mean of the path's yearly portfolio return, in %."""
    data = _annual(ctx, params)
    rate, years, (ws_, wb_), _, paths = _ret_params(params)
    kind, _, arg = key.partition(':')
    if kind == 'geomean' and arg in paths:
        return 100 * _geo(_path_seq(data, paths[arg], years), ws_, wb_), 0.005
    raise Missing(f'contract.json: model.claims key "{key}" is not a quantity of kind retirement-6040')


def ret_invariants(ctx, params):
    """`sameGeomean: [a, b]`: the two paths have the same geometric mean within 0.01 pp (the thesis of test D)."""
    out = []
    pair = params.get('sameGeomean')
    if pair:
        a, b = (ret_value(ctx, params, f'geomean:{k}')[0] for k in pair)
        out.append(metric(f'|G({pair[0]}) − G({pair[1]})| pp', abs(a - b), '<=', 0.01, 'pp'))
    return out


# ---- kind "refinance-breakeven" (Episode 1) ----------------------------------------------------------------
def payment(balance, annual_pct, months):
    r = annual_pct / 1200.0
    return balance * r / (1 - (1 + r) ** -months) if r else balance / months


def _refi(params):
    loan, cost, old, n = _need(params, 'loan', 'cost', 'oldRate', 'termMonths')
    return float(loan), float(cost), float(old), int(n)


def breakeven(loan, cost, old, spread, n):
    s = payment(loan, old, n) - payment(loan, old - spread, n)
    return math.ceil(cost / s) if s > 0 else None, s


def spread_for(loan, cost, old, n, months):
    """Smallest rate cut (points) whose break-even is ≤ `months`: savings(spread) ≥ cost / months, solved by bisection on the continuous
    savings (the break-even itself is a whole number of months)."""
    need = cost / months
    lo, hi = 0.0, old
    for _ in range(200):
        mid = (lo + hi) / 2
        if payment(loan, old, n) - payment(loan, old - mid, n) >= need:
            hi = mid
        else:
            lo = mid
    return hi


def refi_compare(ctx, params, out):
    loan, cost, old, n = _refi(params)
    bad, checked = [], 0
    for k, want in (('loan', loan), ('cost', cost), ('oldRate', old)):
        checked += 1
        if out.get(k) is None or not close(float(out[k]), want, 0.005):
            bad.append((k, out.get(k), want))
    for sp, c in (out.get('cases') or {}).items():
        be, s = breakeven(loan, cost, old, float(sp), n)
        for name, mine, tol in (('oldPayment', payment(loan, old, n), 0.005), ('newPayment', payment(loan, old - float(sp), n), 0.005),
                                ('monthlySavings', s, 0.005), ('breakEvenMonths', be, 0)):
            checked += 1
            if c.get(name) is None or (not close(float(c[name]), mine, tol) if tol else c[name] != mine):
                bad.append((f'cases.{sp}', name, c.get(name), round(mine, 4) if isinstance(mine, float) else mine))
    if not out.get('cases'):
        bad.append(('cases', 'missing'))
    targets = params.get('breakEvenTargets') or {}
    classes = params.get('classes') or {}
    covered = {'loan', 'cost', 'oldRate', 'cases'}
    unrec = []
    for key, months in targets.items():
        got = out.get(key)
        if got is None:
            bad.append((key, 'missing'))
            continue
        covered.add(key)
        for cls, v in (got.items() if isinstance(got, dict) else [('mid', got)]):
            if cls == 'mid':
                L, C = loan, cost
            elif cls in classes:
                L, C = float(classes[cls]['loan']), float(classes[cls]['cost'])
            else:
                unrec.append(f'{key}.{cls}')
                continue
            checked += 1
            mine = spread_for(L, C, old, n, int(months))
            if not close(float(v), mine, 0.0005):
                bad.append((f'{key}.{cls}', round(float(v), 5), round(mine, 5)))
    unrec += sorted(set(out) - covered - set(params.get('notModel', [])))
    return checked, bad, unrec


def refi_value(ctx, params, key):
    """"breakEven:<spread>" (months), "savings:<spread>" ($/month), "spreadFor:<months>[:<class>]" (points), "payment" ($/month at the old rate)."""
    loan, cost, old, n = _refi(params)
    kind, _, arg = key.partition(':')
    if kind == 'breakEven':
        return float(breakeven(loan, cost, old, float(arg), n)[0]), 0
    if kind == 'savings':
        return breakeven(loan, cost, old, float(arg), n)[1], 0.5
    if kind == 'payment':
        return payment(loan, old, n), 0.5
    if kind == 'spreadFor':
        months, _, cls = arg.partition(':')
        L, C = loan, cost
        if cls and cls != 'mid':
            c = (params.get('classes') or {}).get(cls)
            if not c:
                raise Missing(f'contract.json: model.params.classes.{cls}')
            L, C = float(c['loan']), float(c['cost'])
        return spread_for(L, C, old, n, int(months)), 0.005
    raise Missing(f'contract.json: model.claims key "{key}" is not a quantity of kind refinance-breakeven')


KINDS = {'retirement-6040': (ret_compare, ret_value, ret_invariants),
         'refinance-breakeven': (refi_compare, refi_value, lambda ctx, p: [])}


def kind(ctx):
    k = ctx.cfield('model', 'kind', kind=str)
    if k not in KINDS:
        raise Missing(f'an independent re-computation for model kind "{k}" (checks/py/r_model.py KINDS: {sorted(KINDS)}); the checking session writes it')
    return KINDS[k]
