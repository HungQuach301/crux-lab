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


# ---- kind "float-vs-fixed-replay" (Episode 2: a variable-rate loan against a fixed one, replayed over every window of a short-rate index) -----
# Written by the checking session (K3.5) from the topic spec (topics-r1/machine/debt-2/result.json: numbers[].definition and assumptions),
# never from the builder's code. Conventions the spec leaves open are parameters of the contract (model.params), each named below.
#   Index path for start month s, month k = 0..n−1:  idx_k = max(indexFloor, today + X[s+k] − X[s])   (today = last value of the index file)
#   Variable rate: rate_k = (floatStartRate − today) + idx_k, capped at rateCap when one is given   (so rate_0 = floatStartRate)
#   Each month: interest = balance × rate_k / 1200; payment = level payment of the balance over the n − k months left at rate_k (re-amortised
#   whenever the rate changes; at an unchanged rate the recomputed payment is the same); balance −= payment − interest.
#   Fixed loan: fixedRate all n months; total interest = n × level payment − principal.  Difference = variable interest − fixed interest.
#   Windows: every start month from firstStart through the last month with n months of data. "Costlier" = Difference > 0 (strictly).
def ym(s):
    """'YYYY-MM' ≡ 'YYYY-MM-01' (topics-r2 V3: dates are compared after normalisation, never as strings). Any other day is not a month: None."""
    s = str(s).strip()
    if len(s) == 7 and s[4] == '-' and s[:4].isdigit() and s[5:].isdigit():
        y, m = int(s[:4]), int(s[5:])
    elif len(s) == 10 and s[4] == '-' and s[7] == '-' and s[8:] == '01' and s[:4].isdigit() and s[5:7].isdigit():
        y, m = int(s[:4]), int(s[5:7])
    else:
        return None
    return y * 12 + m - 1 if 1 <= m <= 12 else None


def ym_str(i):
    return f'{i // 12:04d}-{i % 12 + 1:02d}'


def _ym_need(s, field):
    i = ym(s)
    if i is None:
        raise Missing(f'contract.json: model.params.{field} must be a month "YYYY-MM" or "YYYY-MM-01" (got {s!r})')
    return i


def index_series(ctx, spec):
    """{file, dateColumn, valueColumn}: a monthly series, one row per month, no gaps. Returns (first month index, [values])."""
    for k in ('file', 'dateColumn', 'valueColumn'):
        if not spec.get(k):
            raise Missing('contract.json: model.params.index.' + k)
    by = {}
    for r in csv.DictReader(open(ctx.need(spec['file']))):
        v = (r.get(spec['valueColumn']) or '').strip()
        if v in ('', '.'):
            continue
        i = ym(r[spec['dateColumn']])
        if i is None or i in by:
            raise Missing(f'{spec["file"]}: a monthly series (one row per month, dates YYYY-MM or YYYY-MM-01); bad row {r[spec["dateColumn"]]!r}')
        by[i] = float(v)
    if not by:
        raise Missing(f'{spec["file"]}: column {spec["valueColumn"]}')
    a, b = min(by), max(by)
    gaps = [ym_str(i) for i in range(a, b + 1) if i not in by]
    if gaps:
        raise Missing(f'{spec["file"]}: months without a value {gaps[:5]}')
    return a, [by[i] for i in range(a, b + 1)]


def _fvf_params(params):
    idx, P, n, fx, fl, first = _need(params, 'index', 'principal', 'termMonths', 'fixedRate', 'floatStartRate', 'firstStart')
    floor = _need(params, 'indexFloor')[0]
    cap = params.get('rateCap')
    breaks = [_ym_need(b, 'periodBreaks[]') for b in params.get('periodBreaks', [])]
    return {'index': idx, 'P': float(P), 'n': int(n), 'fixed': float(fx), 'float': float(fl), 'first': _ym_need(first, 'firstStart'),
            'floor': float(floor), 'cap': None if cap is None else float(cap), 'breaks': sorted(breaks)}


def float_window(P, n, rates):
    """Level-payment loan re-amortised every month at rates[k]: (total interest, highest payment, payments)."""
    B, tot, pays = P, 0.0, []
    for k, r in enumerate(rates):
        i = B * r / 1200.0
        p = payment(B, r, n - k)
        tot += i
        B -= p - i
        pays.append(p)
    return tot, max(pays), pays


def fvf_run(ctx, params, float_start=None):
    """Every window: [{start, totalInterest, difference, maxRate, maxPayment, rates, minIndex}] and the shared quantities."""
    c = _fvf_params(params)
    a, xs = index_series(ctx, c['index'])
    n, P = c['n'], c['P']
    fl = c['float'] if float_start is None else float_start
    today = xs[-1]
    margin = fl - today
    last = a + len(xs) - n
    if c['first'] < a or c['first'] > last:
        raise Missing(f'contract.json: model.params.firstStart {ym_str(c["first"])} outside {ym_str(a)}..{ym_str(last)} (the index file)')
    fpay = payment(P, c['fixed'], n)
    fint = n * fpay - P
    wins = []
    for s in range(c['first'], last + 1):
        x0 = xs[s - a]
        ids = [max(c['floor'], today + xs[s - a + k] - x0) for k in range(n)]
        rates = [margin + v if c['cap'] is None else min(c['cap'], margin + v) for v in ids]
        tot, mp, _ = float_window(P, n, rates)
        wins.append({'start': s, 'totalInterest': tot, 'difference': tot - fint, 'maxRate': max(rates), 'maxPayment': mp, 'rate0': rates[0], 'minIndex': min(ids)})
    return {'c': c, 'today': today, 'margin': margin, 'fixedPayment': fpay, 'fixedTotalInterest': fint, 'windows': wins, 'last': last}


def _share(ws):
    return 100.0 * sum(1 for w in ws if w['difference'] > 0) / len(ws) if ws else None


def fvf_periods(run):
    """Periods split at periodBreaks: [firstStart, b1 − 1], [b1, b2 − 1], …, [bk, last start]."""
    c, ws = run['c'], run['windows']
    edges = [c['first']] + [b for b in c['breaks'] if c['first'] < b <= run['last']] + [run['last'] + 1]
    out = []
    for lo, hi in zip(edges, edges[1:]):
        sub = [w for w in ws if lo <= w['start'] < hi]
        out.append({'from': lo, 'to': hi - 1, 'nWindows': len(sub), 'shareCostlier': _share(sub)})
    return out


def fvf_summary(run):
    ws = run['windows']
    d = [w['difference'] for w in ws]
    worst = max(ws, key=lambda w: (w['difference'], -w['start']))   # ties: the earliest start
    best = min(ws, key=lambda w: (w['difference'], w['start']))
    return {'nWindows': len(ws), 'firstStart': ws[0]['start'], 'lastStart': ws[-1]['start'], 'indexToday': run['today'], 'margin': run['margin'],
            'fixedPayment': run['fixedPayment'], 'fixedTotalInterest': run['fixedTotalInterest'], 'shareCostlier': _share(ws),
            'medianDifference': float(np.median(d)), 'bestDifference': best['difference'], 'bestStart': best['start'],
            'worstDifference': worst['difference'], 'worstStart': worst['start'], 'maxRate': max(w['maxRate'] for w in ws),
            'maxPayment': max(w['maxPayment'] for w in ws)}


def share_at_spread(ctx, params, spread):
    """Sensitivity: share of costlier windows when the variable loan starts `spread` points under the fixed rate (floatStartRate = fixedRate − spread)."""
    c = _fvf_params(params)
    return _share(fvf_run(ctx, params, c['fixed'] - float(spread))['windows'])


MONEY, RATE, COUNT, DATE = 'money', 'rate', 'count', 'date'
FVF_FIELDS = {'nWindows': COUNT, 'firstStart': DATE, 'lastStart': DATE, 'indexToday': RATE, 'margin': RATE, 'fixedPayment': RATE,
              'fixedTotalInterest': MONEY, 'shareCostlier': RATE, 'medianDifference': MONEY, 'bestDifference': MONEY, 'bestStart': DATE,
              'worstDifference': MONEY, 'worstStart': DATE, 'maxRate': RATE, 'maxPayment': RATE}
WINDOW_FIELDS = {'totalInterest': MONEY, 'difference': MONEY, 'maxRate': RATE, 'maxPayment': RATE}


def _fvf_cmp(bad, where, theirs, mine, how):
    """money: max($0.50, 1e-6 relative); rates, shares (%) and payments: 0.005; counts exactly; months after normalisation (YYYY-MM ≡ YYYY-MM-01)."""
    if how == DATE:
        ok = theirs is not None and ym(theirs) == mine
        shown = ym_str(mine)
    elif mine is None or theirs is None or isinstance(theirs, (bool, str)):
        ok, shown = theirs is None and mine is None, mine
    elif how == COUNT:
        ok, shown = theirs == mine, mine
    else:
        ok = abs(float(theirs) - mine) <= (max(0.5, 1e-6 * abs(mine)) if how == MONEY else 0.005)
        shown = round(mine, 4)
    if not ok:
        bad.append((where, theirs, shown))
    return 1


def fvf_compare(ctx, params, out):
    """The model file: echo of the inputs (principal, termMonths, fixedRate, floatStartRate, firstStart, indexFloor, rateCap, periodBreaks), the summary
    quantities (FVF_FIELDS), windows [{start, totalInterest, difference, maxRate, maxPayment}] (every window), periods [{from, to, nWindows,
    shareCostlier}], sensitivity {<spread>: shareCostlier} (every spread of params.spreads; others given are re-computed too)."""
    run = fvf_run(ctx, params)
    c = run['c']
    bad, checked = [], 0
    for k, want, how in (('principal', c['P'], MONEY), ('termMonths', c['n'], COUNT), ('fixedRate', c['fixed'], RATE), ('floatStartRate', c['float'], RATE),
                         ('firstStart', c['first'], DATE), ('indexFloor', c['floor'], RATE), ('rateCap', c['cap'], RATE)):
        checked += _fvf_cmp(bad, k, out.get(k), want, how)
    theirs_b = out.get('periodBreaks')
    checked += 1
    if not isinstance(theirs_b, list) or sorted(ym(b) for b in theirs_b) != c['breaks']:
        bad.append(('periodBreaks', theirs_b, [ym_str(b) for b in c['breaks']]))
    summ = fvf_summary(run)
    for k, how in FVF_FIELDS.items():
        checked += _fvf_cmp(bad, k, out.get(k), summ[k], how)
    theirs = {}
    for w in out.get('windows') or []:
        theirs[ym(w.get('start'))] = w
    checked += _fvf_cmp(bad, 'windows (count)', len(out.get('windows') or []), len(run['windows']), COUNT)
    for w in run['windows']:
        t = theirs.get(w['start'])
        if t is None:
            bad.append((f'windows.{ym_str(w["start"])}', 'missing', None))
            continue
        for k, how in WINDOW_FIELDS.items():
            checked += _fvf_cmp(bad, f'windows.{ym_str(w["start"])}.{k}', t.get(k), w[k], how)
    extra = sorted(ym_str(i) if i is not None else 'bad date' for i in set(theirs) - {w['start'] for w in run['windows']})
    if extra:
        bad.append(('windows not in the replay', extra[:10], None))
    per = fvf_periods(run)
    tp = out.get('periods') or []
    checked += _fvf_cmp(bad, 'periods (count)', len(tp), len(per), COUNT)
    for i, (p, t) in enumerate(zip(per, tp)):
        for k, how in (('from', DATE), ('to', DATE), ('nWindows', COUNT), ('shareCostlier', RATE)):
            checked += _fvf_cmp(bad, f'periods[{i}].{k}', t.get(k), p[k], how)
    sens = out.get('sensitivity') or {}
    want = [float(x) for x in params.get('spreads', [])]
    got = {float(k): v for k, v in sens.items()}
    for sp in sorted(set(want) | set(got)):
        checked += _fvf_cmp(bad, f'sensitivity.{sp:g}', got.get(sp), share_at_spread(ctx, params, sp), RATE)
    conv = params.get('conventions') or {}
    for k, v in conv.items():
        checked += 1
        if out.get(k) != v:
            bad.append((k, out.get(k), v))
    covered = ({'principal', 'termMonths', 'fixedRate', 'floatStartRate', 'firstStart', 'indexFloor', 'rateCap', 'periodBreaks', 'windows', 'periods',
                'sensitivity'} | set(FVF_FIELDS) | set(conv))
    return checked, bad, sorted(set(out) - covered - set(params.get('notModel', [])))


def fvf_value(ctx, params, key):
    """Summary fields (FVF_FIELDS; a month field as "<field>Year" / "<field>Month", e.g. worstStartYear = 1977, worstStartMonth = 4: S05 compares
    numbers), "nWindows:<period start>", "shareCostlier:<period start>" (period start = firstStart or a periodBreak, YYYY-MM),
    "shareCostlierAtSpread:<points>". Tolerances: $0.50 money; 0.005 rates, shares (%) and payments; counts and months exactly."""
    run = fvf_run(ctx, params)
    summ = fvf_summary(run)
    name, _, arg = key.partition(':')
    tol = {MONEY: 0.5, RATE: 0.005, COUNT: 0}
    if not arg:
        for f_, how in FVF_FIELDS.items():
            if how == DATE and key in (f_ + 'Year', f_ + 'Month'):
                i = summ[f_]
                return float(i // 12 if key.endswith('Year') else i % 12 + 1), 0
            if key == f_ and how != DATE:
                return float(summ[f_]), tol[how]
    elif name == 'shareCostlierAtSpread':
        return share_at_spread(ctx, params, float(arg)), 0.005
    elif name in ('nWindows', 'shareCostlier') and ym(arg) is not None:
        for p in fvf_periods(run):
            if p['from'] == ym(arg):
                return float(p[name]), 0 if name == 'nWindows' else 0.005
    raise Missing(f'contract.json: model.claims key "{key}" is not a quantity of kind float-vs-fixed-replay')


def fvf_invariants(ctx, params):
    """(1) the variable loan's first-month rate equals floatStartRate in every window; (2) the index path is never negative; (3) the fixed loan's total
    interest from the month-by-month amortisation equals the level-payment formula n × P·r/(1 − (1 + r)^−n) − P."""
    run = fvf_run(ctx, params)
    c, ws = run['c'], run['windows']
    tot, _, _ = float_window(c['P'], c['n'], [c['fixed']] * c['n'])
    return [metric('max |first-month variable rate − floatStartRate| pp', max(abs(w['rate0'] - c['float']) for w in ws), '<=', 1e-9, 'pp'),
            metric('lowest index value on any window path', min(w['minIndex'] for w in ws), '>=', 0, 'pp'),
            metric('|fixed interest amortised − level-payment formula| $', abs(tot - run['fixedTotalInterest']), '<=', 0.5, '$')]


KINDS = {'retirement-6040': (ret_compare, ret_value, ret_invariants),
         'refinance-breakeven': (refi_compare, refi_value, lambda ctx, p: []),
         'float-vs-fixed-replay': (fvf_compare, fvf_value, fvf_invariants)}


def kind(ctx):
    k = ctx.cfield('model', 'kind', kind=str)
    if k not in KINDS:
        raise Missing(f'an independent re-computation for model kind "{k}" (checks/py/r_model.py KINDS: {sorted(KINDS)}); the checking session writes it')
    return KINDS[k]
