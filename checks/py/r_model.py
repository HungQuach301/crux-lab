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
    # declared conventions (e.g. "rebalance": "annual"): text fields of the model file that name how it was computed; they must say exactly
    # what the contract says the model is (the re-computation above follows the contract), so they are covered, not trusted
    conv = params.get('conventions') or {}
    for k, v in conv.items():
        checked += 1
        if out.get(k) != v:
            bad.append((k, out.get(k), v))
    covered = {'initial', 'rate', 'years', 'weights', 'tax', 'fees', 'paths', 'starts'} | set(conv)
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


# ---- kind "refinance-breakeven" (Episode 1, M1b: break-even counting what is still owed) ---------------------------
# Written by the checking session from the episode contract's recompute text (contract.json model.recompute), never from model/refi.py.
# Conventions the text leaves open are parameters of the contract (model.params), each named below; the checker does not guess them.
def payment(balance, annual_pct, months):
    r = annual_pct / 1200.0
    return balance * r / (1 - (1 + r) ** -months) if r else balance / months


def balance_after(principal, annual_pct, months, k):
    """Balance of a level-payment loan after k payments."""
    r = annual_pct / 1200.0
    if not r:
        return principal * (1 - k / months)
    return principal * ((1 + r) ** months - (1 + r) ** k) / ((1 + r) ** months - 1)


def net_after(p0, r_old, k, bal, r_new, cost, m, n):
    """What the refinance has earned after m months: payments saved + (balance still owed on the old loan − balance owed on the new one) − cost."""
    sav = payment(p0, r_old, n) - payment(bal, r_new, n)
    return sav * m + balance_after(p0, r_old, n, k + m) - balance_after(bal, r_new, n, m) - cost


def be_balance(p0, r_old, k, bal, r_new, cost, n, horizon=None):
    """MAIN break-even: first month m ≥ 1 with net_after ≥ 0 (None if never within the horizon, default the new term)."""
    for m in range(1, (horizon or n) + 1):
        if net_after(p0, r_old, k, bal, r_new, cost, m, n) >= 0:
            return m
    return None


def be_simple(p0, r_old, bal, r_new, cost, n):
    sav = payment(p0, r_old, n) - payment(bal, r_new, n)
    return math.ceil(cost / sav) if sav > 0 else None


def cut_for(p0, r_old, k, cost, n, months):
    """Smallest rate cut (points below the old rate) whose MAIN break-even is ≤ `months` (bisection on the cut)."""
    bal = balance_after(p0, r_old, n, k)
    lo, hi = 0.0, r_old
    for _ in range(100):
        mid = (lo + hi) / 2
        be = be_balance(p0, r_old, k, bal, r_old - mid, cost, n, months)
        if be is not None:
            hi = mid
        else:
            lo = mid
    return hi


def _months(a, b):
    return (int(b[:4]) - int(a[:4])) * 12 + int(b[5:7]) - int(a[5:7])


def _add(m, k):
    y, mo = int(m[:4]), int(m[5:7]) - 1 + k
    return f'{y + mo // 12:04d}-{mo % 12 + 1:02d}'


def monthly_means(ctx, spec):
    """{file, dateColumn, rateColumn}: calendar-month mean of a weekly series (unrounded; rates are reported rounded to 2 decimals)."""
    rows = list(csv.DictReader(open(ctx.need(spec['file']))))
    by = {}
    for r in rows:
        by.setdefault(r[spec['dateColumn']][:7], []).append(float(r[spec['rateColumn']]))
    return {m: sum(v) / len(v) for m, v in sorted(by.items())}


def zigzag_drops(rate, swing):
    """Alternating peaks and troughs of the monthly series where each reversal is ≥ `swing` points; ties go to the later month.
    Drop episodes = (peak, trough) pairs; a drop still running at the end of the data (≥ swing below its peak) is an episode too."""
    ms = list(rate)
    hi = lo = ms[0]
    trend, cand, piv = None, None, []
    for m in ms[1:]:
        if trend is None:
            if rate[m] >= rate[hi]:
                hi = m
            if rate[m] <= rate[lo]:
                lo = m
            if rate[hi] - rate[m] >= swing - 1e-9:
                trend, cand = 'down', m
                piv.append(('peak', hi))
            elif rate[m] - rate[lo] >= swing - 1e-9:
                trend, cand = 'up', m
                piv.append(('trough', lo))
            continue
        if trend == 'down':
            if rate[m] <= rate[cand]:
                cand = m
            elif rate[m] - rate[cand] >= swing - 1e-9:
                piv.append(('trough', cand))
                trend, cand = 'up', m
        else:
            if rate[m] >= rate[cand]:
                cand = m
            elif rate[cand] - rate[m] >= swing - 1e-9:
                piv.append(('peak', cand))
                trend, cand = 'down', m
    if trend == 'down' and piv and piv[-1][0] == 'peak' and rate[piv[-1][1]] - rate[cand] >= swing - 1e-9:
        piv.append(('trough', cand))
    return [(a[1], b[1]) for a, b in zip(piv, piv[1:]) if a[0] == 'peak' and b[0] == 'trough']


def cost_shares(ctx, spec):
    """{file, filter: {column: value}, yearColumn, shareColumn}: the HMDA median cost share (% of the loan) by year."""
    out = {}
    for r in csv.DictReader(open(ctx.need(spec['file']))):
        if all(r.get(k) == v for k, v in spec['filter'].items()):
            out[int(r[spec['yearColumn']])] = float(r[spec['shareColumn']])
    return out


def history(ctx, h):
    """The history simulation (contract text: "monthly means of MORTGAGE30US; drop episodes = zig-zag swings >= 1.00 point; refinance in the
    first month >= spread under the peak; cost = HMDA median share of that year (fixed median share before 2018, ILLUSTRATIVE)").
    Old loan: h.loan at the peak month's rate over h.termMonths, first payment the month after the peak. Refinance month: first month after the
    peak, up to the trough, whose mean is ≤ peak − spread; payments made on the old loan = months since the peak; the new loan = the balance then,
    at that month's rate; cost = share of that year (years before the first HMDA year: the median of the HMDA years' shares) × new loan.
    Another drop before break-even: first month in (refinance, refinance + break-even] whose mean is strictly more than `spread` below the new rate. Censored: the data end
    before refinance + break-even."""
    rate = monthly_means(ctx, h['series'])
    sh = cost_shares(ctx, h['costShares'])
    fixed = float(np.median(list(sh.values())))
    n, p0 = int(h['termMonths']), float(h['loan'])
    last = list(rate)[-1]
    out = []
    for pk, tr in zigzag_drops(rate, float(h['swingPoints'])):
        cases = []
        for sp in h['spreads']:
            ms = [m for m in rate if pk < m <= tr and rate[m] <= rate[pk] - sp + 1e-9]
            if not ms:
                cases.append({'spread': sp, 'reached': False})
                continue
            m = ms[0]
            k = _months(pk, m)
            bal = balance_after(p0, rate[pk], n, k)
            y = int(m[:4])
            share = sh.get(y, fixed) if y >= min(sh) else fixed
            cost = share / 100 * bal
            be = be_balance(p0, rate[pk], k, bal, rate[m], cost, n)
            nxt = next((x for x in rate if m < x <= _add(m, be or n) and rate[x] < rate[m] - sp), None)
            cases.append({'spread': sp, 'reached': True, 'refiMonth': m, 'newRate': round(rate[m], 2), 'monthsOnOldLoan': k, 'balance': bal, 'costSharePct': share,
                          'costIllustrative': y < min(sh), 'closingCost': cost, 'monthlySavings': payment(p0, rate[pk], n) - payment(bal, rate[m], n),
                          'breakEvenMonths': be, 'breakEvenSimple': be_simple(p0, rate[pk], bal, rate[m], cost, n), 'beforeBreakEvenAnotherDrop': nxt,
                          'censored': _add(m, be or n) > last})
        out.append({'peak': pk, 'peakRate': round(rate[pk], 2), 'trough': tr, 'troughRate': round(rate[tr], 2), 'drop': round(rate[pk] - rate[tr], 2), 'cases': cases})
    return out, sh, fixed


def _cmp(bad, where, theirs, mine, tol):
    if isinstance(mine, bool) or mine is None or isinstance(mine, str):
        ok = theirs == mine
    else:
        ok = theirs is not None and abs(float(theirs) - float(mine)) <= tol
    if not ok:
        bad.append((where, theirs, round(mine, 4) if isinstance(mine, float) else mine))
    return 1


def refi_compare(ctx, params, out):
    sc, chars, h = _need(params, 'scenario', 'characters', 'history')
    n, k, r0, rt = int(sc['termMonths']), int(sc['paymentsMade']), float(sc['oldRate']), float(sc['todayRate'])
    bad, checked = [], 0
    for key, want in (('oldRate', r0), ('paymentsMade', k), ('todayRate', rt)):
        checked += _cmp(bad, f'scenario.{key}', (out.get('scenario') or {}).get(key), want, 1e-9)
    for name, c in chars.items():
        o = (out.get('characters') or {}).get(name) or {}
        L, C = float(c['loan']), float(c['cost'])
        bal = balance_after(L, r0, n, k)
        mine = {'loan': L, 'cost': C, 'balance': bal, 'monthlySavings': payment(L, r0, n) - payment(bal, rt, n), 'simple': be_simple(L, r0, bal, rt, C, n),
                'withBalance': be_balance(L, r0, k, bal, rt, C, n)}
        for hz in sc.get('netHorizons', []):
            mine[f'net{hz}'] = net_after(L, r0, k, bal, rt, C, hz, n)
            mine[f'cut{hz}'] = cut_for(L, r0, k, C, n, hz)
        for f_, v in mine.items():
            checked += _cmp(bad, f'characters.{name}.{f_}', o.get(f_), v, 0.0005 if f_.startswith('cut') else 0.01)
    ref = sc.get('byCutOf')
    if ref:
        L, C = float(chars[ref]['loan']), float(chars[ref]['cost'])
        bal = balance_after(L, r0, n, k)
        for cut, o in (out.get(f'{ref}ByCut') or {}).items():
            rn = r0 - float(cut)
            for f_, v in (('balance', bal), ('monthlySavings', payment(L, r0, n) - payment(bal, rn, n)), ('simple', be_simple(L, r0, bal, rn, C, n)),
                          ('withBalance', be_balance(L, r0, k, bal, rn, C, n))):
                checked += _cmp(bad, f'{ref}ByCut.{cut}.{f_}', o.get(f_), v, 0.01)
        s_ = be_simple(L, r0, bal, rt, C, n)
        # still owed more on the new loan than on the old one at the simple break-even month (the thesis: "counting what is still owed")
        checked += _cmp(bad, 'gapAtSimpleBreakEven', out.get('gapAtSimpleBreakEven'), balance_after(bal, rt, n, s_) - balance_after(L, r0, n, k + s_), 0.01)
    hist, sh, fixed = history(ctx, h)
    for y, v in sh.items():
        checked += _cmp(bad, f'costSharesByYear.{y}', (out.get('costSharesByYear') or {}).get(str(y)), v, 1e-9)
    checked += _cmp(bad, 'fixedSharePre2018', out.get('fixedSharePre2018'), fixed, 1e-9)
    theirs = out.get('history') or []
    checked += _cmp(bad, 'history episodes', len(theirs), len(hist), 0)
    for i, (e, t) in enumerate(zip(hist, theirs)):
        for f_ in ('peak', 'peakRate', 'trough', 'troughRate', 'drop'):
            checked += _cmp(bad, f'history[{i}].{f_}', t.get(f_), e[f_], 1e-9)
        for j, (c, tc) in enumerate(zip(e['cases'], t.get('cases', []))):
            for f_, v in c.items():
                tol = 0.01 if f_ in ('balance', 'closingCost', 'monthlySavings') else 1e-9
                checked += _cmp(bad, f'history[{i}].cases[{j}].{f_}', tc.get(f_), v, tol)
    covered = {'scenario', 'characters', 'costSharesByYear', 'fixedSharePre2018', 'history'} | ({f'{ref}ByCut', 'gapAtSimpleBreakEven'} if ref else set())
    return checked, bad, sorted(set(out) - covered - set(params.get('notModel', [])))


def refi_value(ctx, params, key):
    """"<character>.<field>" (a recomputed character field, e.g. maya.withBalance, maya.cut36), "history.<i>.<spread>.<field>"."""
    sc, chars = _need(params, 'scenario', 'characters')
    n, k, r0, rt = int(sc['termMonths']), int(sc['paymentsMade']), float(sc['oldRate']), float(sc['todayRate'])
    who, _, f_ = key.partition('.')
    if who in chars:
        L, C = float(chars[who]['loan']), float(chars[who]['cost'])
        bal = balance_after(L, r0, n, k)
        vals = {'loan': (L, 0.5), 'cost': (C, 0.5), 'balance': (bal, 0.5), 'monthlySavings': (payment(L, r0, n) - payment(bal, rt, n), 0.5),
                'simple': (be_simple(L, r0, bal, rt, C, n), 0), 'withBalance': (be_balance(L, r0, k, bal, rt, C, n), 0)}
        if f_.startswith('cut'):
            return cut_for(L, r0, k, C, n, int(f_[3:])), 0.005
        if f_.startswith('net'):
            return net_after(L, r0, k, bal, rt, C, int(f_[3:]), n), 0.5
        if f_ in vals:
            v, t = vals[f_]
            return float(v), t
    raise Missing(f'contract.json: model.claims key "{key}" is not a quantity of kind refinance-breakeven')


KINDS = {'retirement-6040': (ret_compare, ret_value, ret_invariants),
         'refinance-breakeven': (refi_compare, refi_value, lambda ctx, p: [])}


def kind(ctx):
    k = ctx.cfield('model', 'kind', kind=str)
    if k not in KINDS:
        raise Missing(f'an independent re-computation for model kind "{k}" (checks/py/r_model.py KINDS: {sorted(KINDS)}); the checking session writes it')
    return KINDS[k]
