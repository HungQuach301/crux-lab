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


class Month(int):
    """A month (index y × 12 + m − 1) returned by value(): S05 compares it with a claim written "YYYY-MM" or "YYYY-MM-01" after normalisation (K3.6)."""


def _run_cached(ctx, params, float_start=None):
    """fvf_run memoised per check context (S05 asks for many keys of the same replay; K3.6 keys replay once per spread)."""
    return ctx.memo(('fvf-run', id(params), float_start), lambda: (params, fvf_run(ctx, params, float_start)))[1]   # params kept: the id stays its own


def _spread_run(ctx, params, arg):
    """The replay with the variable loan starting `arg` points under the fixed rate (floatStartRate = fixedRate − spread; 0 and negative spreads too)."""
    try:
        sp = float(arg)
    except ValueError:
        raise Missing(f'contract.json: model.claims spread "{arg}" is not a number of points')
    c = _fvf_params(params)
    return _run_cached(ctx, params, c['fixed'] - sp)


def _period(run, arg, key):
    i = ym(arg)
    for p in fvf_periods(run):
        if i is not None and p['from'] == i:
            return p
    raise Missing(f'contract.json: model.claims key "{key}": "{arg}" is not the first month of a period (firstStart or a periodBreak)')


def _worst(run):
    return max(run['windows'], key=lambda w: (w['difference'], -w['start']))   # ties: the earliest start (as fvf_summary)


def fvf_value(ctx, params, key):
    """Summary fields (FVF_FIELDS; a month field as "<field>Year" / "<field>Month", e.g. worstStartYear = 1977, worstStartMonth = 4: S05 compares
    numbers; K3.6: the month field itself, e.g. "worstStart", compared with a claim "YYYY-MM" / "YYYY-MM-01" after normalisation),
    "nWindows:<period start>", "shareCostlier:<period start>" (period start = firstStart or a periodBreak, YYYY-MM),
    "shareCostlierAtSpread:<points>". Tolerances: $0.50 money; 0.005 rates, shares (%) and payments; counts and months exactly.
    K3.6 (spec: episodes/ep002/checks-notes.md "K3.6"; topics-r1/machine/debt-2/result.json definitions), every key explicit, none derived by S05:
      "shareCostlierAtSpread:<points>:<period start>"  share (%) of the period's windows costlier when the variable loan starts <points> under fixedRate
      "worstDifferenceAtSpread:<points>"                the largest Difference ($) of that replay
      "worstStartAtSpread:<points>"                     its start month (ties: earliest); also "worstStartAtSpreadYear:<points>" / "worstStartAtSpreadMonth:<points>"
      "minShareCostlierOverSpreads:<period start>"      the smallest period share (%) over every spread of params.spreads
      "floatFirstPayment"                               month-0 payment of the variable loan: level payment of principal over termMonths at floatStartRate
      "firstPaymentGap"                                 fixedPayment − floatFirstPayment
      "worstWindowMaxRate"                              highest monthly variable rate in the worst window (worstStart)
      "shareRateAboveFixed"                             % of windows with at least one month whose variable rate > fixedRate (strictly)
      "worstShareOfFixed"                               100 × worstDifference / fixedTotalInterest (%)
    A spread may be 0 or negative (the variable loan then starts at or above the fixed rate)."""
    run = _run_cached(ctx, params)
    summ = fvf_summary(run)
    c = run['c']
    name, _, arg = key.partition(':')
    tol = {MONEY: 0.5, RATE: 0.005, COUNT: 0}
    if not arg:
        for f_, how in FVF_FIELDS.items():
            if how == DATE and key in (f_ + 'Year', f_ + 'Month'):
                i = summ[f_]
                return float(i // 12 if key.endswith('Year') else i % 12 + 1), 0
            if key == f_:
                return (Month(summ[f_]), 0) if how == DATE else (float(summ[f_]), tol[how])
        ffp = payment(c['P'], c['float'], c['n'])
        if key == 'floatFirstPayment':
            return ffp, 0.005
        if key == 'firstPaymentGap':
            return run['fixedPayment'] - ffp, 0.005
        if key == 'worstWindowMaxRate':
            return float(_worst(run)['maxRate']), 0.005
        if key == 'shareRateAboveFixed':
            ws = run['windows']
            return 100.0 * sum(1 for w in ws if w['maxRate'] > c['fixed']) / len(ws), 0.005
        if key == 'worstShareOfFixed':
            return 100.0 * summ['worstDifference'] / run['fixedTotalInterest'], 0.005
    elif name == 'shareCostlierAtSpread':
        sp, _, per = arg.partition(':')
        if not per:
            return share_at_spread(ctx, params, float(sp)), 0.005
        p = _period(_spread_run(ctx, params, sp), per, key)
        return float(p['shareCostlier']), 0.005
    elif name == 'worstDifferenceAtSpread':
        return float(_worst(_spread_run(ctx, params, arg))['difference']), 0.5
    elif name in ('worstStartAtSpread', 'worstStartAtSpreadYear', 'worstStartAtSpreadMonth'):
        i = _worst(_spread_run(ctx, params, arg))['start']
        if name == 'worstStartAtSpread':
            return Month(i), 0
        return float(i // 12 if name.endswith('Year') else i % 12 + 1), 0
    elif name == 'minShareCostlierOverSpreads':
        sps = params.get('spreads') or []
        if not sps:
            raise Missing('contract.json: model.params.spreads (minShareCostlierOverSpreads needs the spreads it takes the minimum over)')
        return min(float(_period(_spread_run(ctx, params, sp), arg, key)['shareCostlier']) for sp in sps), 0.005
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


# ---- kind "lock-vs-roll-replay" (Episode 3, K3.7: lock a known multiple, or a locked rate, for H months against rolling a short rate every p months) -----
# Written by the checking session (K3.7) from the topic spec (topics-r1/machine/retire-4/model.json newKindNeeds, quantities[].meaning; episodes/ep003/
# numbers.md, checks-notes.md), never from the builder's code. One kind for retire-4 (savings bond doubling vs rolled 3-month T-bills: p = 1, constant
# multiple m = 2, H = 240) and retire-3 (5-year yield locked vs 1-year yield rolled: p = 12, locked series q = 12, H = 60, startFilter).
#   Window from start month s: Roll(s) = Π_{k=0}^{H/p−1} (1 + R(s + k·p)·p/1200);  Lock(s) = m (constant) or (1 + L(s)·q/1200)^(H/q) (locked series).
#   Windows: every s from firstStart (default: the first month with inputs) to lastStart (default: the last s with s + H − 1 ≤ the last roll month) whose
#   inputs all exist (R at every s + k·p; L(s) for a locked series). Roll ahead = Roll > Lock, lock ahead = Lock > Roll (strict; ties in neither).
#   Deflator P: real factor = P(s)/P(s + H); a window without P at either end is skipped from the real quantities (counted). Real lock = Lock × factor.
#   Sets: all windows; each subset {name: [from, to | null]} (start months, inclusive, null = lastStart; subsets may overlap); "filtered" = the starts kept
#   by startFilter (rollRateAboveLockRate: R(s) > L(s)). Runs: maximal sequences of consecutive calendar months inside the filtered starts; a run is
#   lock-majority when more than half of its starts are lock ahead.
#   Constant lock only: equivalentLockRate = 100(m^(12/H) − 1) (% a year, compounded yearly); steadyBreakevenRate = 1200/p · (m^(p/H) − 1) (the roll rate
#   that, held for H months, gives exactly m); mean rule = "mean of the window's roll rates > steadyBreakevenRate".
def monthly_values(ctx, spec, field):
    """{file, dateColumn, valueColumn}: {month index: value}. A blank or "." value is a gap (a missing input, never a zero); dates YYYY-MM or YYYY-MM-01."""
    if not isinstance(spec, dict):
        raise Missing(f'contract.json: model.params.{field}')
    for k in ('file', 'dateColumn', 'valueColumn'):
        if not spec.get(k):
            raise Missing(f'contract.json: model.params.{field}.{k}')
    by = {}
    for r in csv.DictReader(open(ctx.need(spec['file']))):
        i = ym(r.get(spec['dateColumn'], ''))
        if i is None or i in by:
            raise Missing(f'{spec["file"]}: a monthly series (one row per month, dates YYYY-MM or YYYY-MM-01); bad row {r.get(spec["dateColumn"])!r}')
        v = (r.get(spec['valueColumn']) or '').strip()
        if v not in ('', '.'):
            by[i] = float(v)
    if not by:
        raise Missing(f'{spec["file"]}: column {spec["valueColumn"]}')
    return by


def _lvr_params(params):
    roll, lock, H = _need(params, 'roll', 'lock', 'horizonMonths')
    H = int(H)
    p = int((roll or {}).get('periodMonths') or 0)
    if p < 1 or H % p:
        raise Missing('contract.json: model.params.roll.periodMonths (≥ 1, horizonMonths a multiple of it)')
    if not isinstance(lock, dict):
        raise Missing('contract.json: model.params.lock')
    if lock.get('multiple') is not None:
        m, q = float(lock['multiple']), None
    else:
        q = int(lock.get('periodMonths') or 0)
        if q < 1 or H % q:
            raise Missing('contract.json: model.params.lock.multiple, or lock.{file, dateColumn, valueColumn, periodMonths} (horizonMonths a multiple of it)')
        m = None
    subsets = {}
    for name, ab in (params.get('subsets') or {}).items():
        if name in ('all', 'filtered') or not isinstance(ab, (list, tuple)) or len(ab) != 2:
            raise Missing(f'contract.json: model.params.subsets.{name} = [from, to | null] (names "all" and "filtered" are taken)')
        subsets[name] = (_ym_need(ab[0], f'subsets.{name}[0]'), None if ab[1] is None else _ym_need(ab[1], f'subsets.{name}[1]'))
    flt = params.get('startFilter')
    if flt is not None and (not isinstance(flt, dict) or flt.get('type') != 'rollRateAboveLockRate' or m is not None):
        raise Missing('contract.json: model.params.startFilter = {"type": "rollRateAboveLockRate"} (needs a locked series)')
    term = roll.get('termMonths')
    band = params.get('nearBandPct')
    return {'roll': roll, 'lock': lock, 'H': H, 'p': p, 'm': m, 'q': q, 'subsets': subsets, 'filter': flt is not None,
            'first': None if params.get('firstStart') is None else _ym_need(params['firstStart'], 'firstStart'),
            'last': None if params.get('lastStart') is None else _ym_need(params['lastStart'], 'lastStart'),
            'deflator': params.get('deflator'), 'term': None if term is None else int(term), 'band': None if band is None else float(band)}


def lvr_run(ctx, params, bump=0.0, const_roll=None):
    """Every window [{start, end, roll, lock, nObs, meanRate, rate0, lockRate0?, real?}]. bump / const_roll: every roll rate raised by `bump` points, or
    replaced by a constant (the invariants' replays)."""
    c = _lvr_params(params)
    R0 = monthly_values(ctx, c['roll'], 'roll')
    R = R0 if not bump and const_roll is None else {i: (const_roll if const_roll is not None else v + bump) for i, v in R0.items()}
    L = None if c['m'] is not None else monthly_values(ctx, c['lock'], 'lock')
    P = monthly_values(ctx, c['deflator'], 'deflator') if c['deflator'] else None
    H, p = c['H'], c['p']
    z = max(R)
    first = c['first'] if c['first'] is not None else (min(R) if L is None else max(min(R), min(L)))
    last = c['last'] if c['last'] is not None else z - H + 1
    if last > z - H + 1:
        raise Missing(f'contract.json: model.params.lastStart {ym_str(last)} after {ym_str(z - H + 1)} (its {H} months run past the roll file)')
    wins = []
    for s in range(first, last + 1):
        obs = range(s, s + H, p)
        if any(o not in R for o in obs) or (L is not None and s not in L):
            continue
        roll = 1.0
        for o in obs:
            roll *= 1 + R[o] * p / 1200.0
        lock = c['m'] if L is None else (1 + L[s] * c['q'] / 1200.0) ** (H // c['q'])
        w = {'start': s, 'end': s + H - 1, 'roll': roll, 'lock': lock, 'nObs': len(obs), 'meanRate': sum(R[o] for o in obs) / len(obs), 'rate0': R[s]}
        if L is not None:
            w['lockRate0'] = L[s]
        if P is not None and s in P and s + H in P:
            w['real'] = P[s] / P[s + H]
        wins.append(w)
    if not wins:
        raise Missing(f'no window: firstStart {ym_str(first)} .. lastStart {ym_str(last)} has no start month with every input')
    return {'c': c, 'R': R, 'R0': R0, 'P': P, 'windows': wins, 'dataLast': z}


def lvr_sets(run):
    """{"all": windows, <subset>: its windows, "filtered": the filtered starts (with a startFilter)}."""
    ws, c = run['windows'], run['c']
    last = ws[-1]['start']
    sets = {'all': ws}
    for name, (a, b) in c['subsets'].items():
        hi = last if b is None else min(b, last)
        sets[name] = [w for w in ws if a <= w['start'] <= hi]
    if c['filter']:
        sets['filtered'] = [w for w in ws if w['rate0'] > w['lockRate0']]
    return sets


def _pick(ws, f, top):
    """Smallest (top=False) or largest (top=True) f(w); ties: the earliest start."""
    return (max if top else min)(ws, key=lambda w: (f(w), -w['start'] if top else w['start']))


def _pct(k, n):
    return 100.0 * k / n if n else None


def lvr_runs(ws):
    """Maximal sequences of consecutive calendar months: [{from, to, nWindows, nLockAhead}]."""
    out = []
    for w in ws:
        if out and out[-1]['to'] == w['start'] - 1:
            out[-1]['to'] = w['start']
        else:
            out.append({'from': w['start'], 'to': w['start'], 'nWindows': 0, 'nLockAhead': 0})
        out[-1]['nWindows'] += 1
        out[-1]['nLockAhead'] += w['lock'] > w['roll']
    return out


def lvr_stats(run, ws):
    """Quantities of one set of windows (None where the set is empty or the input absent)."""
    c, n = run['c'], len(ws)
    st = {'nWindows': n}
    if not n:
        return st
    gap = lambda w: 100.0 * (w['lock'] / w['roll'] - 1)
    mn, mx = _pick(ws, lambda w: w['roll'], False), _pick(ws, lambda w: w['roll'], True)
    gmn, gmx = _pick(ws, gap, False), _pick(ws, gap, True)
    ra, la = sum(w['roll'] > w['lock'] for w in ws), sum(w['lock'] > w['roll'] for w in ws)
    st.update({'firstStart': ws[0]['start'], 'lastStart': ws[-1]['start'], 'shareRollAhead': _pct(ra, n), 'shareLockAhead': _pct(la, n),
               'shareTie': _pct(n - ra - la, n), 'medianRoll': float(np.median([w['roll'] for w in ws])), 'minRoll': mn['roll'], 'minRollStart': mn['start'],
               'maxRoll': mx['roll'], 'maxRollStart': mx['start'], 'medianLockVsRollPct': float(np.median([gap(w) for w in ws])),
               'minLockVsRollPct': gap(gmn), 'minLockVsRollStart': gmn['start'], 'maxLockVsRollPct': gap(gmx), 'maxLockVsRollStart': gmx['start'],
               'shareMeanRateBelowStart': _pct(sum(w['meanRate'] < w['rate0'] for w in ws), n)})
    if c['m'] is not None:
        r_star = 1200.0 / c['p'] * (c['m'] ** (c['p'] / c['H']) - 1)
        st['shareMeanRuleAgrees'] = _pct(sum((w['meanRate'] > r_star) == (w['roll'] > w['lock']) for w in ws), n)
    if c['band'] is not None:
        st['nearCount'] = sum(abs(w['roll'] / w['lock'] - 1) < c['band'] / 100.0 for w in ws)
    if run['P'] is not None:
        real = [w for w in ws if 'real' in w]
        lr = [w['lock'] * w['real'] for w in real]
        st.update({'nRealWindows': len(real), 'skippedRealStarts': n - len(real)})
        if real:
            lo = _pick(real, lambda w: w['lock'] * w['real'], False)
            below = [w['start'] for w in real if w['lock'] * w['real'] < 1]
            st.update({'shareLockRealAtLeastOne': _pct(sum(x >= 1 for x in lr), len(real)), 'shareLockRealBelowOne': _pct(sum(x < 1 for x in lr), len(real)),
                       'medianLockRealPct': 100.0 * float(np.median(lr)), 'minLockRealPct': 100.0 * lo['lock'] * lo['real'], 'minLockRealStart': lo['start'],
                       'lastStartLockRealBelowOne': max(below) if below else None,
                       'shareRollRealAtLeastOne': _pct(sum(w['roll'] * w['real'] >= 1 for w in real), len(real)),
                       'medianRollRealPct': 100.0 * float(np.median([w['roll'] * w['real'] for w in real]))})
    if run['c']['filter']:
        runs = lvr_runs(ws)
        st.update({'runs': len(runs), 'lockMajorityRuns': sum(2 * r['nLockAhead'] > r['nWindows'] for r in runs)})
    return st


def lvr_summary(run):
    """The quantities of the whole replay: the "all" set and the run-wide numbers."""
    c, ws, R0 = run['c'], run['windows'], run['R0']
    st = lvr_stats(run, ws)
    z, f0 = max(R0), ws[0]['start']
    st.update({'horizonMonths': c['H'], 'horizonYears': c['H'] / 12.0, 'rollPeriodMonths': c['p'], 'latestStart': ws[-1]['start'], 'latestEnd': ws[-1]['end'],
               'latestRoll': ws[-1]['roll'], 'latestLock': ws[-1]['lock'], 'rollRateLatest': R0[z], 'rollRateLatestMonth': z,
               'meanRollRateAll': float(np.mean([R0[i] for i in range(f0, z + 1) if i in R0])), 'nonOverlapPeriods': (z - f0 + 1) // c['H']})
    if c['m'] is not None:
        st['equivalentLockRate'] = 100.0 * (c['m'] ** (12.0 / c['H']) - 1)
        st['steadyBreakevenRate'] = 1200.0 / c['p'] * (c['m'] ** (c['p'] / c['H']) - 1)
    if c['term']:
        st.update({'rollTermMonths': c['term'], 'rollsPerHorizon': c['H'] / c['term']})
    if c['band'] is not None:
        st['nearBandPct'] = c['band']
    return st


MULT, PCT, CNT, MON = 'multiple', 'pct', 'count', 'month'
LVR_FIELDS = {'nWindows': CNT, 'firstStart': MON, 'lastStart': MON, 'shareRollAhead': PCT, 'shareLockAhead': PCT, 'shareTie': PCT, 'medianRoll': MULT,
              'minRoll': MULT, 'minRollStart': MON, 'maxRoll': MULT, 'maxRollStart': MON, 'medianLockVsRollPct': PCT, 'minLockVsRollPct': PCT,
              'minLockVsRollStart': MON, 'maxLockVsRollPct': PCT, 'maxLockVsRollStart': MON, 'shareMeanRateBelowStart': PCT, 'shareMeanRuleAgrees': PCT,
              'nearCount': CNT, 'nRealWindows': CNT, 'skippedRealStarts': CNT, 'shareLockRealAtLeastOne': PCT, 'shareLockRealBelowOne': PCT,
              'medianLockRealPct': PCT, 'minLockRealPct': PCT, 'minLockRealStart': MON, 'lastStartLockRealBelowOne': MON, 'shareRollRealAtLeastOne': PCT,
              'medianRollRealPct': PCT, 'runs': CNT, 'lockMajorityRuns': CNT,
              # run-wide (no set)
              'horizonMonths': CNT, 'horizonYears': PCT, 'rollPeriodMonths': CNT, 'latestStart': MON, 'latestEnd': MON, 'latestRoll': MULT, 'latestLock': MULT,
              'rollRateLatest': PCT, 'rollRateLatestMonth': MON, 'meanRollRateAll': PCT, 'nonOverlapPeriods': CNT, 'equivalentLockRate': PCT,
              'steadyBreakevenRate': PCT, 'rollTermMonths': CNT, 'rollsPerHorizon': PCT, 'nearBandPct': PCT}
LVR_SET_ONLY = {'runs', 'lockMajorityRuns'}   # the filtered set's runs; on any other set they are the runs of that set's start months
LVR_TOL = {MULT: 0.0005, PCT: 0.005, CNT: 0}  # S05: multiples 0.0005, rates / shares / % 0.005, counts and months exactly


def _lvr_cached(ctx, params, bump=0.0, const_roll=None):
    return ctx.memo(('lvr-run', id(params), bump, const_roll), lambda: (params, lvr_run(ctx, params, bump, const_roll)))[1]


def _lvr_out(name, v, how):
    if v is None:
        raise Missing(f'model.claims key "{name}": no value (empty set, or the input it needs is not in model.params)')
    return (Month(v), 0) if how == MON else (float(v), LVR_TOL[how])


def lvr_value(ctx, params, key):
    """Keys (S05). "<quantity>" = the whole replay; "<quantity>:<set>" = one set (a subset name of params.subsets, or "filtered"). Quantities: LVR_FIELDS
    (a month quantity also as "<field>Year" / "<field>Month", numbers). Set bounds: "subsetFrom:<name>", "subsetTo:<name>" (to = lastStart when null or
    later). Starts before a subset: "nWindowsBefore:<name>" (windows with start < its from), "shareWindowsBefore:<name>" (% of all windows).
    Tolerances: multiples 0.0005; rates, shares and % 0.005; counts and months exactly."""
    run = _lvr_cached(ctx, params)
    name, _, arg = key.partition(':')
    sets = lvr_sets(run)
    if name in ('subsetFrom', 'subsetTo', 'nWindowsBefore', 'shareWindowsBefore'):
        if arg not in run['c']['subsets']:
            raise Missing(f'contract.json: model.claims key "{key}": "{arg}" is not a subset of model.params.subsets')
        a, b = run['c']['subsets'][arg]
        last = run['windows'][-1]['start']
        if name == 'subsetFrom':
            return Month(a), 0
        if name == 'subsetTo':
            return Month(last if b is None else min(b, last)), 0
        k = sum(1 for w in run['windows'] if w['start'] < a)
        return (float(k), 0) if name == 'nWindowsBefore' else (_pct(k, len(run['windows'])), 0.005)
    if arg and arg not in sets:
        raise Missing(f'contract.json: model.claims key "{key}": "{arg}" is not a set (subsets: {sorted(run["c"]["subsets"])}, or "filtered" with a startFilter)')
    st = lvr_summary(run) if not arg else lvr_stats(run, sets[arg])
    for f_, how in LVR_FIELDS.items():
        if how == MON and name in (f_ + 'Year', f_ + 'Month') and f_ in st:
            v = st[f_]
            if v is None:
                break
            return float(v // 12 if name.endswith('Year') else v % 12 + 1), 0
        if name == f_ and f_ in st:
            return _lvr_out(key, st[f_], how)
    raise Missing(f'contract.json: model.claims key "{key}" is not a quantity of kind lock-vs-roll-replay')


def _lvr_cmp(bad, where, theirs, mine, how):
    """S01: multiples 1e-6 relative (the model file is unrounded); rates, shares, % 0.005; counts exactly; months after normalisation."""
    if mine is None or theirs is None:
        ok, shown = theirs is None and mine is None, ym_str(mine) if how == MON and mine is not None else mine
    elif how == MON:
        ok, shown = ym(theirs) == mine, ym_str(mine)
    elif isinstance(theirs, bool) or not isinstance(theirs, (int, float)):
        ok, shown = False, mine                     # a string, list or object where a number is due
    elif how == CNT:
        ok, shown = theirs == mine, mine
    else:
        ok = abs(float(theirs) - mine) <= (1e-6 * max(1.0, abs(mine)) if how == MULT else 0.005)
        shown = round(mine, 6)
    if not ok:
        bad.append((where, theirs, shown))
    return 1


LVR_TOP = ('nWindows', 'firstStart', 'lastStart', 'shareRollAhead', 'shareLockAhead', 'shareTie', 'medianRoll', 'minRoll', 'minRollStart', 'maxRoll',
           'maxRollStart', 'medianLockVsRollPct', 'minLockVsRollPct', 'minLockVsRollStart', 'maxLockVsRollPct', 'maxLockVsRollStart', 'rollRateLatest',
           'rollRateLatestMonth', 'meanRollRateAll', 'nonOverlapPeriods')
LVR_SUBSET = ('from', 'to', 'nWindows', 'shareRollAhead', 'shareLockAhead', 'minRoll', 'maxRoll')
LVR_FILTERED = ('nWindows', 'shareLockAhead', 'medianLockVsRollPct', 'minLockVsRollPct', 'maxLockVsRollPct', 'lockMajorityRuns')
LVR_DEFLATOR = {'nRealWindows': CNT, 'skippedStarts': CNT, 'shareLockRealAtLeastOne': PCT, 'medianLockReal': MULT, 'minLockReal': MULT,
                'minLockRealStart': MON, 'lastStartLockRealBelowOne': MON}


def lvr_compare(ctx, params, out):
    """The model file (unrounded): echo of the inputs (horizonMonths, rollPeriodMonths, lockMultiple, lockPeriodMonths, nearBandPct); LVR_TOP;
    equivalentLockRate and steadyBreakevenRate (constant lock), nearCount (with nearBandPct); latest {start, end, roll, lock};
    subsets {<name>: {from, to, nWindows, shareRollAhead, shareLockAhead, minRoll, maxRoll}} (every subset); filtered {LVR_FILTERED, runs: [{from, to,
    nWindows, nLockAhead}]} (with a startFilter); deflator {nRealWindows, skippedStarts, shareLockRealAtLeastOne, medianLockReal, minLockReal,
    minLockRealStart, lastStartLockRealBelowOne} (with a deflator; ratios, not %); windows [{start, end, roll, lock, lockReal?}] (every window)."""
    run = _lvr_cached(ctx, params)
    c = run['c']
    summ = lvr_summary(run)
    bad, checked = [], 0
    for k, want, how in (('horizonMonths', c['H'], CNT), ('rollPeriodMonths', c['p'], CNT), ('lockMultiple', c['m'], MULT),
                         ('lockPeriodMonths', c['q'], CNT), ('nearBandPct', c['band'], PCT)):
        checked += _lvr_cmp(bad, k, out.get(k), want, how)
    for k in LVR_TOP:
        checked += _lvr_cmp(bad, k, out.get(k), summ[k], LVR_FIELDS[k])
    extra = set()
    if c['m'] is not None:
        extra |= {'equivalentLockRate', 'steadyBreakevenRate'}
    if c['band'] is not None:
        extra.add('nearCount')
    for k in sorted(extra):
        checked += _lvr_cmp(bad, k, out.get(k), summ[k], LVR_FIELDS[k])
    lt = out.get('latest') or {}
    for k, mine, how in (('start', summ['latestStart'], MON), ('end', summ['latestEnd'], MON), ('roll', summ['latestRoll'], MULT), ('lock', summ['latestLock'], MULT)):
        checked += _lvr_cmp(bad, f'latest.{k}', lt.get(k), mine, how)
    sets = lvr_sets(run)
    tsub = out.get('subsets') or {}
    for name in c['subsets']:
        st, t = lvr_stats(run, sets[name]), tsub.get(name) or {}
        if not sets[name]:
            checked += _lvr_cmp(bad, f'subsets.{name}.nWindows', t.get('nWindows'), 0, CNT)
            continue
        st['from'], st['to'] = st['firstStart'], st['lastStart']
        for k in LVR_SUBSET:
            checked += _lvr_cmp(bad, f'subsets.{name}.{k}', t.get(k), st[k], MON if k in ('from', 'to') else LVR_FIELDS[k])
    for name in sorted(set(tsub) - set(c['subsets'])):
        bad.append((f'subsets.{name}', 'not in model.params.subsets', None))
    if c['filter']:
        st, t = lvr_stats(run, sets['filtered']), out.get('filtered') or {}
        for k in LVR_FILTERED:
            checked += _lvr_cmp(bad, f'filtered.{k}', t.get(k), st.get(k), LVR_FIELDS[k])
        mine, theirs = lvr_runs(sets['filtered']), t.get('runs') or []
        checked += _lvr_cmp(bad, 'filtered.runs (count)', len(theirs), len(mine), CNT)
        for i, (r, tr) in enumerate(zip(mine, theirs)):
            for k in ('from', 'to', 'nWindows', 'nLockAhead'):
                checked += _lvr_cmp(bad, f'filtered.runs[{i}].{k}', tr.get(k), r[k], MON if k in ('from', 'to') else CNT)
    if run['P'] is not None:
        t = out.get('deflator') or {}
        mine = {'nRealWindows': summ['nRealWindows'], 'skippedStarts': summ['skippedRealStarts']}
        if summ['nRealWindows']:
            mine.update({'shareLockRealAtLeastOne': summ['shareLockRealAtLeastOne'], 'medianLockReal': summ['medianLockRealPct'] / 100,
                         'minLockReal': summ['minLockRealPct'] / 100, 'minLockRealStart': summ['minLockRealStart'],
                         'lastStartLockRealBelowOne': summ['lastStartLockRealBelowOne']})
        for k, v in mine.items():
            checked += _lvr_cmp(bad, f'deflator.{k}', t.get(k), v, LVR_DEFLATOR[k])
    theirs = {}
    for w in out.get('windows') or []:
        theirs[ym(w.get('start'))] = w
    checked += _lvr_cmp(bad, 'windows (count)', len(out.get('windows') or []), len(run['windows']), CNT)
    for w in run['windows']:
        t = theirs.get(w['start'])
        if t is None:
            bad.append((f'windows.{ym_str(w["start"])}', 'missing', None))
            continue
        fields = [('end', w['end'], MON), ('roll', w['roll'], MULT), ('lock', w['lock'], MULT)]
        if run['P'] is not None:
            fields.append(('lockReal', w['lock'] * w['real'] if 'real' in w else None, MULT))
        for k, mine, how in fields:
            checked += _lvr_cmp(bad, f'windows.{ym_str(w["start"])}.{k}', t.get(k), mine, how)
    stray = sorted(ym_str(i) if i is not None else 'bad date' for i in set(theirs) - {w['start'] for w in run['windows']})
    if stray:
        bad.append(('windows not in the replay', stray[:10], None))
    conv = params.get('conventions') or {}
    for k, v in conv.items():
        checked += 1
        if out.get(k) != v:
            bad.append((k, out.get(k), v))
    covered = ({'horizonMonths', 'rollPeriodMonths', 'lockMultiple', 'lockPeriodMonths', 'nearBandPct', 'latest', 'subsets', 'windows'} | set(LVR_TOP) | extra
               | ({'filtered'} if c['filter'] else set()) | ({'deflator'} if run['P'] is not None else set()) | set(conv))
    return checked, bad, sorted(set(out) - covered - set(params.get('notModel', [])))


def lvr_invariants(ctx, params):
    """The spec's invariants (newKindNeeds.invariants), on the contract's own inputs:
    (1) constant roll rate r (5% a year) → Roll = (1 + r·p/1200)^(H/p) in every window (1e-12 relative);
    (2) Roll(s) = G(s + H)/G(s) for the running index G along each p-month chain (G(i + p) = G(i)·(1 + R(i)·p/1200)): product and index agree (1e-9 relative);
    (3) shareRollAhead + shareLockAhead + shareTie = 100 for every set; every window uses exactly H/p roll rates and ends ≤ the last roll month;
    (4) every roll rate raised by 0.25 point never lowers shareRollAhead;
    (5) constant lock: (1 + equivalentLockRate/100)^(H/12) = m, and the steady roll rate gives Roll = m in every window."""
    run = _lvr_cached(ctx, params)
    c, ws, R = run['c'], run['windows'], run['R0']
    H, p = c['H'], c['p']
    r = 5.0
    want = (1 + r * p / 1200.0) ** (H // p)
    cst = _lvr_cached(ctx, params, const_roll=r)['windows']
    G = {}
    for i in sorted(R):
        G[i] = G[i - p] * (1 + R[i - p] * p / 1200.0) if i - p in R else 1.0
    for i in sorted(R):            # one step past each chain's last rate, for windows that end on the last roll month
        if i + p not in G:
            G[i + p] = G[i] * (1 + R[i] * p / 1200.0)
    idx_err = max(abs(G[w['start'] + H] / G[w['start']] - w['roll']) / w['roll'] for w in ws)
    sums = max(abs(sum(lvr_stats(run, s_)[k] for k in ('shareRollAhead', 'shareLockAhead', 'shareTie')) - 100) for s_ in lvr_sets(run).values() if s_)
    shape = sum(1 for w in ws if w['nObs'] != H // p or w['end'] > run['dataLast'])
    base = lvr_stats(run, ws)['shareRollAhead']
    up = lvr_stats(_lvr_cached(ctx, params, bump=0.25), _lvr_cached(ctx, params, bump=0.25)['windows'])['shareRollAhead']
    ms = [metric('max relative |Roll − closed form| at a constant 5% roll rate', max(abs(w['roll'] - want) / want for w in cst), '<=', 1e-12, ''),
          metric('max relative |Roll − G(s+H)/G(s)| (product vs running index)', idx_err, '<=', 1e-9, ''),
          metric('max |shareRollAhead + shareLockAhead + shareTie − 100| over the sets', sums, '<=', 1e-9, 'pp'),
          metric('windows not using exactly H/p roll rates or ending after the last roll month', shape, '<=', 0),
          metric('shareRollAhead change when every roll rate rises 0.25 point', up - base, '>=', 0, 'pp')]
    if c['m'] is not None:
        eq = 100.0 * (c['m'] ** (12.0 / H) - 1)
        rs = 1200.0 / p * (c['m'] ** (p / H) - 1)
        st = _lvr_cached(ctx, params, const_roll=rs)['windows']
        ms += [metric('|(1 + equivalentLockRate/100)^(H/12) − m|', abs((1 + eq / 100) ** (H / 12.0) - c['m']), '<=', 1e-12, ''),
               metric('max |Roll − m| at the steady break-even roll rate', max(abs(w['roll'] - c['m']) for w in st), '<=', 1e-9, '')]
    return ms


# ---- kind "fixed-cap-vs-index-growth" (Episode 4, K3.8: a fixed nominal limit against regional price-index growth) ------------------------
# Spec: topics-r1/machine/tax-2/model.json → newKindNeeds, extended by episodes/ep004/gates/V0-defs.md §4 (purchase prices). Written from the spec text,
# never from the builder's code. Parameterised for reuse: any set of quarterly price indexes (FRED CSV), any number of fixed nominal caps, each over all
# series or a named few; purchase prices and count cutoffs are lists.
#   base_s = mean of the four quarterly values of buyYear (exactly four); g_s = value(saleQuarter) / base_s (saleQuarter = last row of every index file).
#   threshold_<cap>_<s> = cap / (g_s − 1) (g_s > 1, else no threshold). Metros = every series except `national`.
#   min / max (+ _metro key) over the metros, for every cap that covers all of them; metros_threshold_under_<label> = metros with the unrounded threshold of
#   `primaryCap` strictly below the cutoff.
#   For a purchase price P (label: P/1000 + "k"): gain_at_<label>_<s> = P(g_s − 1);
#   cross_quarter_at_<label>_<s> = first quarter d ≥ crossFrom (default buyYear + 1, Q1) with P(value_d/base_s − 1) > primary cap (strict), else null;
#   stay_quarter_at_<label>_<s> = first quarter d ≥ crossFrom from which the strict inequality holds at d and every later quarter through saleQuarter;
#   metros_crossed_at_<label> = metros whose cross quarter is not null.
#   Deflator (optional): cpi_base = CPI(baseMonth), cpi_now = CPI(nowMonth) (= last CPI row); excl_<primaryCap>_<base year>_in_now = cap × cpi_now / cpi_base.
FCI_MONEY, FCI_RATIO, FCI_CNT, FCI_DATE, FCI_EXACT = 'money', 'ratio', 'count', 'date', 'exact'


class Exact:
    """A value returned by value() that S05 compares by equality: a name, a list of names (order ignored) or null (e.g. a quarter that never came)."""
    def __init__(self, v):
        self.v = sorted(v) if isinstance(v, list) else v

    def same(self, theirs):
        return (sorted(theirs) if isinstance(theirs, list) else theirs) == self.v


def _fci_label(P):
    P = float(P)
    if P <= 0 or P % 1000:
        raise Missing(f'contract.json: model.params prices / countCutoffs must be positive multiples of 1000 USD (got {P})')
    return f'{int(P // 1000)}k'


def quarterly_values(ctx, spec, field):
    """{file, dateColumn, valueColumn}: a quarterly series, quarter-start dates (YYYY-01/04/07/10, -01), consecutive, no gaps. Returns {month index: value}."""
    by = monthly_values(ctx, spec, field)
    ks = sorted(by)
    if any(i % 3 for i in ks):
        raise Missing(f'{spec["file"]}: quarter-start dates only (months 01, 04, 07, 10); got {[ym_str(i) for i in ks if i % 3][:3]}')
    gaps = [ym_str(i) for i in range(ks[0], ks[-1] + 1, 3) if i not in by]
    if gaps:
        raise Missing(f'{spec["file"]}: quarters without a value {gaps[:5]}')
    return by


def _fci_params(params):
    series, buy, sale, caps, primary = _need(params, 'series', 'buyYear', 'saleQuarter', 'caps', 'primaryCap')
    if not isinstance(series, dict) or not series:
        raise Missing('contract.json: model.params.series = {<key>: {file, dateColumn, valueColumn}}')
    nat = params.get('national')
    if nat is not None and nat not in series:
        raise Missing(f'contract.json: model.params.national "{nat}" is not a key of model.params.series')
    if not isinstance(caps, dict) or primary not in caps:
        raise Missing('contract.json: model.params.caps = {<name>: {value, series: "all" | [keys]}} with model.params.primaryCap one of them')
    cv = {}
    for name, c in caps.items():
        if not isinstance(c, dict) or c.get('value') is None:
            raise Missing(f'contract.json: model.params.caps.{name}.value')
        cov = c.get('series', 'all')
        keys = list(series) if cov == 'all' else list(cov or [])
        if not keys or any(k not in series for k in keys):
            raise Missing(f'contract.json: model.params.caps.{name}.series ("all" or keys of model.params.series)')
        cv[name] = (float(c['value']), keys)
    if cv[primary][1] != list(series):
        raise Missing(f'contract.json: model.params.caps.{primary} (the primary cap) must cover every series')
    sale_i = _ym_need(sale, 'saleQuarter')
    cf = params.get('crossFrom')
    defl = params.get('deflator')
    if defl is not None:
        for k in ('file', 'dateColumn', 'valueColumn', 'baseMonth', 'nowMonth'):
            if not defl.get(k):
                raise Missing('contract.json: model.params.deflator.' + k)
    return {'series': series, 'national': nat, 'metros': [k for k in series if k != nat], 'buy': int(buy), 'sale': sale_i, 'caps': cv, 'primary': primary,
            'prices': [float(x) for x in params.get('prices') or []], 'cutoffs': [float(x) for x in params.get('countCutoffs') or []],
            'crossFrom': (int(buy) + 1) * 12 if cf is None else _ym_need(cf, 'crossFrom'), 'deflator': defl}


def fci_run(ctx, params, scale=None):
    """Every quantity of the kind (unrounded), as the flat key → value map of the model file. scale: {series key: factor} multiplies that index (the
    invariants' replays: a scaled index leaves every ratio, threshold and quarter unchanged)."""
    c = _fci_params(params)
    out, ser = {}, {}
    for k, spec in c['series'].items():
        by = quarterly_values(ctx, spec, f'series.{k}')
        if scale and k in scale:
            by = {i: v * scale[k] for i, v in by.items()}
        if max(by) != c['sale']:
            raise Missing(f'{spec["file"]}: saleQuarter {ym_str(c["sale"])} must be the last observation (last is {ym_str(max(by))})')
        q = [c['buy'] * 12 + m for m in (0, 3, 6, 9)]
        if any(i not in by for i in q):
            raise Missing(f'{spec["file"]}: the four quarters of buyYear {c["buy"]}')
        base = sum(by[i] for i in q) / 4.0
        g = by[c['sale']] / base
        ser[k] = (by, base, g)
        out[f'growth_{k}'] = g
    cap0 = c['caps'][c['primary']][0]
    for name, (v, keys) in c['caps'].items():
        for k in keys:
            g = ser[k][2]
            out[f'threshold_{name}_{k}'] = v / (g - 1) if g > 1 else None
        if all(m in keys for m in c['metros']) and c['metros']:
            vals = [(out[f'threshold_{name}_{m}'], m) for m in c['metros'] if out[f'threshold_{name}_{m}'] is not None]
            if vals:
                lo, hi = min(vals), max(vals)
                out.update({f'threshold_{name}_min': lo[0], f'threshold_{name}_min_metro': lo[1], f'threshold_{name}_max': hi[0], f'threshold_{name}_max_metro': hi[1]})
    for cut in c['cutoffs']:
        lab = _fci_label(cut)
        under = sorted(m for m in c['metros'] if out[f'threshold_{c["primary"]}_{m}'] is not None and out[f'threshold_{c["primary"]}_{m}'] < cut)
        out[f'metros_threshold_under_{lab}'] = len(under)
        out[f'metros_threshold_under_{lab}_names'] = under
    for P in c['prices']:
        lab = _fci_label(P)
        for k, (by, base, g) in ser.items():
            out[f'gain_at_{lab}_{k}'] = P * (g - 1)
            qs = [i for i in sorted(by) if c['crossFrom'] <= i <= c['sale']]
            above = [P * (by[i] / base - 1) > cap0 for i in qs]
            out[f'cross_quarter_at_{lab}_{k}'] = next((Month(i) for i, a in zip(qs, above) if a), None)
            stay = None
            for i, a in zip(reversed(qs), reversed(above)):
                if not a:
                    break
                stay = Month(i)
            out[f'stay_quarter_at_{lab}_{k}'] = stay
        out[f'metros_crossed_at_{lab}'] = sum(1 for m in c['metros'] if out[f'cross_quarter_at_{lab}_{m}'] is not None)
    d = c['deflator']
    if d is not None:
        cpi = monthly_values(ctx, d, 'deflator')
        b, n = _ym_need(d['baseMonth'], 'deflator.baseMonth'), _ym_need(d['nowMonth'], 'deflator.nowMonth')
        if n != max(cpi):
            raise Missing(f'{d["file"]}: deflator.nowMonth {ym_str(n)} must be the last observation (last is {ym_str(max(cpi))})')
        if b not in cpi:
            raise Missing(f'{d["file"]}: deflator.baseMonth {ym_str(b)}')
        out['cpi_base'], out['cpi_now'] = cpi[b], cpi[n]
        out[f'excl_{c["primary"]}_{b // 12}_in_now'] = cap0 * cpi[n] / cpi[b]
    return c, ser, out


def _fci_how(key):
    if key.startswith(('cross_quarter_', 'stay_quarter_')):
        return FCI_DATE
    if key.startswith(('metros_threshold_under_', 'metros_crossed_')):
        return FCI_EXACT if key.endswith('_names') else FCI_CNT
    if key.endswith('_metro'):
        return FCI_EXACT
    if key.startswith('growth_') or key.startswith('cpi_'):
        return FCI_RATIO
    return FCI_MONEY


FCI_TOL = {FCI_MONEY: 0.5, FCI_RATIO: 0.0005, FCI_CNT: 0}


def _fci_cached(ctx, params, scale=None):
    key = None if scale is None else tuple(sorted(scale.items()))
    return ctx.memo(('fci-run', id(params), key), lambda: (params, fci_run(ctx, params, scale)))[1]


def fci_value(ctx, params, key):
    """Keys (S05): every key of the model file (FCI quantities above, e.g. "threshold_joint_miami", "cross_quarter_at_300k_us", "metros_crossed_at_200k",
    "excl_joint_1997_in_now"), plus the inputs a claim may quote: "cap:<name>" (USD), "price:<label>" (USD), "metroCount", "buyYear", "saleQuarter" (month), "cpiBaseMonth" (month, with a deflator).
    Tolerances: money $0.50, ratios and CPI 0.0005, counts exactly, quarters exactly (YYYY-MM ≡ YYYY-MM-01), names and null by equality."""
    c, _, out = _fci_cached(ctx, params)
    name, _, arg = key.partition(':')
    if name == 'cap' and arg in c['caps']:
        return c['caps'][arg][0], 0.5
    if name == 'price' and arg in {_fci_label(P): P for P in c['prices']}:
        return {_fci_label(P): P for P in c['prices']}[arg], 0.5
    if key == 'metroCount':
        return float(len(c['metros'])), 0
    if key == 'buyYear':
        return float(c['buy']), 0
    if key == 'saleQuarter':
        return Month(c['sale']), 0
    if key == 'cpiBaseMonth' and c['deflator'] is not None:
        return Month(_ym_need(c['deflator']['baseMonth'], 'deflator.baseMonth')), 0
    if key not in out:
        raise Missing(f'contract.json: model.claims key "{key}" is not a quantity of kind fixed-cap-vs-index-growth')
    v, how = out[key], _fci_how(key)
    if v is None or how == FCI_EXACT:
        return Exact(v), 0
    if how == FCI_DATE:
        return v, 0
    return float(v), FCI_TOL[how]


def fci_compare(ctx, params, out):
    """The model file: {params (echo, not compared), raw: {every FCI key: unrounded value}, rounded?: {...} (display values, not compared)}; a flat file
    without "raw" is read as raw. S01: money max($0.50, 1e-6 relative), ratios and CPI 1e-9 relative, counts exactly, quarters exactly after normalisation,
    names (and null) by equality; every key the kind computes must be present; a raw key the kind does not compute is listed."""
    _, _, mine = _fci_cached(ctx, params)
    raw = out.get('raw') if isinstance(out.get('raw'), dict) else out
    bad, checked = [], 0
    for k, v in mine.items():
        checked += 1
        t, how = raw.get(k, '<absent>'), _fci_how(k)
        if t == '<absent>':
            bad.append((k, 'absent', v if how != FCI_DATE or v is None else ym_str(v)))
            continue
        if v is None or how == FCI_EXACT:
            ok = Exact(v).same(t)
        elif how == FCI_DATE:
            ok = isinstance(t, str) and ym(t) == int(v)
        elif isinstance(t, bool) or not isinstance(t, (int, float)):
            ok = False
        elif how == FCI_CNT:
            ok = t == v
        elif how == FCI_RATIO:
            ok = abs(t - v) <= 1e-9 * max(1.0, abs(v))
        else:
            ok = close(t, v)
        if not ok:
            bad.append((k, t, ym_str(v) if how == FCI_DATE and v is not None else v))
    for k, v in (params.get('conventions') or {}).items():
        checked += 1
        if raw.get(k) != v:
            bad.append((k, raw.get(k), v))
    covered = set(mine) | set(params.get('conventions') or {}) | set(params.get('notModel', []))
    unrec = sorted(set(raw) - covered)
    if raw is not out:
        unrec += sorted(set(out) - {'params', 'raw', 'rounded'} - covered)
    return checked, bad, unrec


def fci_invariants(ctx, params):
    """The spec's invariants (newKindNeeds.invariants + V0-defs §4), on the contract's own inputs:
    (1) threshold × (g − 1) = cap for every series and cap (|error| < 1e-6); (2) two caps on one series: thresholds in the ratio of the caps (1e-9);
    (3) g > 1 for every series; (4) min / max equal one metro threshold and bound every metro threshold; (5) metro counts non-decreasing in the cutoff and
    ≤ the number of metros; (6) restated cap > cap iff CPI now > CPI base; (7) price P: stay quarter not null iff P > the primary threshold, and
    the cross quarter ≤ the stay quarter; (8) scaling an index by 2 leaves growth, thresholds and quarters unchanged (1e-12)."""
    c, ser, out = _fci_cached(ctx, params)
    err1 = 0.0
    for name, (v, keys) in c['caps'].items():
        for k in keys:
            t = out[f'threshold_{name}_{k}']
            if t is not None:
                err1 = max(err1, abs(t * (ser[k][2] - 1) - v))
    err2 = 0.0
    names = list(c['caps'])
    for a in names:
        for b in names:
            if a < b:
                for k in set(c['caps'][a][1]) & set(c['caps'][b][1]):
                    ta, tb = out[f'threshold_{a}_{k}'], out[f'threshold_{b}_{k}']
                    if ta is not None and tb is not None:
                        err2 = max(err2, abs(ta / tb - c['caps'][a][0] / c['caps'][b][0]))
    notup = sum(1 for k in ser if ser[k][2] <= 1)
    mm = 0
    for name, (v, keys) in c['caps'].items():
        if f'threshold_{name}_min' in out:
            ts = [out[f'threshold_{name}_{m}'] for m in c['metros'] if out[f'threshold_{name}_{m}'] is not None]
            lo, hi = out[f'threshold_{name}_min'], out[f'threshold_{name}_max']
            mm += (lo not in ts) + (hi not in ts) + sum(1 for t in ts if not lo <= t <= hi)
    counts = [out[f'metros_threshold_under_{_fci_label(x)}'] for x in sorted(c['cutoffs'])]
    mono = sum(1 for a, b in zip(counts, counts[1:]) if b < a) + sum(1 for n in counts if n > len(c['metros']))
    ms = [metric('max |threshold × (g − 1) − cap| over series and caps', err1, '<=', 1e-6, 'USD'),
          metric('max |thresholdA / thresholdB − capA / capB| (two caps, one series)', err2, '<=', 1e-9, ''),
          metric('series with growth ≤ 1 (no threshold)', notup, '<=', 0),
          metric('min / max not a metro threshold, or a metro threshold outside [min, max]', mm, '<=', 0),
          metric('metro counts decreasing in the cutoff, or above the number of metros', mono, '<=', 0)]
    if c['deflator'] is not None:
        r = out[f'excl_{c["primary"]}_{_ym_need(c["deflator"]["baseMonth"], "deflator.baseMonth") // 12}_in_now']
        ms.append(metric('restated cap > cap iff CPI now > CPI base (violations)', int((r > c['caps'][c['primary']][0]) != (out['cpi_now'] > out['cpi_base'])), '<=', 0))
    if c['prices']:
        badq = 0
        for P in c['prices']:
            lab = _fci_label(P)
            for k in ser:
                t, st, cr = out[f'threshold_{c["primary"]}_{k}'], out[f'stay_quarter_at_{lab}_{k}'], out[f'cross_quarter_at_{lab}_{k}']
                badq += int((st is not None) != (t is not None and P > t)) + int(st is not None and (cr is None or cr > st))
        ms.append(metric('price claims inconsistent (stay quarter ⇔ P > threshold; cross ≤ stay)', badq, '<=', 0))
    k0 = next(iter(ser))
    _, _, o2 = _fci_cached(ctx, params, scale={k0: 2.0})
    drift = sum(1 for k, v in out.items() if k0 in k and (isinstance(v, float) and abs(o2[k] - v) > 1e-12 * max(1.0, abs(v)) or not isinstance(v, float) and o2[k] != v))
    ms.append(metric(f'quantities of "{k0}" changed when its index is doubled', drift, '<=', 0))
    return ms


# ---- kind "ltv-first-passage" (Episode 5, K3.9) -------------------------------------------------------------------------------------------
#   Written from the spec topics-r2/machine/debt-2/model.json → newKindNeeds (+ quantities[].meaning) and episodes/ep005/numbers.md (rules for the
#   latest rate month, the illustrative buyers, the slump); never from calc.py or the builder's model code.
#   Monthly rate R(m) = mean of the rate observations dated in calendar month m (weekly series: a month is complete when the next weekly date, last
#   observation + 7 days, falls in a later month; the latest rate month is the latest complete one). For rate R: x = R/1200, loan L0 = 1 − downShare
#   (share of the price), level payment p = L0·x/(1 − (1 + x)^−n), scheduled balance B_k = L0(1 + x)^k − p((1 + x)^k − 1)/x (share of the price).
#   sched(R, t) = first k in 0..n with B_k ≤ t. Index loan-to-value LTV(s, k) = B_k / (H[s + k]/H[s]). Purchase months: index months with a monthly
#   rate. Set A: s + lookMonthsA ≤ last index month; set B: last index month − s ≥ minFollowB (the spec's "more than 120" read as numbers.md does:
#   2016-07, exactly 120 later months, is in B). T(s) = first k in 0..min(n, months left) with LTV(s, k) ≤ requestLtv. Every comparison ≤ with 1e-12 slack.
#   Key labels come from the parameters: 100 × LTV ("80", "77p5"), months ("24", "60").
LFP_MONTH, LFP_DAY, LFP_CNT, LFP_RATE, LFP_RATIO, LFP_MONEY, LFP_EXACT = 'month', 'day', 'count', 'rate', 'ratio', 'money', 'exact'
LFP_TOL = {LFP_RATE: 0.005, LFP_RATIO: 0.0005, LFP_MONEY: 0.5, LFP_CNT: 0}   # S05: rates and % 0.005, shares / LTV / years / index levels 0.0005, money $0.50
LFP_EPS = 1e-12


def _lfp_lab(x):
    return f'{100 * float(x):g}'.replace('.', 'p')


def _lfp_day(s):
    import datetime
    try:
        return datetime.date.fromisoformat(str(s).strip()[:10])
    except ValueError:
        return None


def _lfp_series(ctx, spec, field):
    """{file, dateColumn, valueColumn}: a monthly series, one row per month, no gaps (blank / "." = no value). Returns (first month, [values])."""
    by = monthly_values(ctx, spec, field)
    a, b = min(by), max(by)
    gaps = [ym_str(i) for i in range(a, b + 1) if i not in by]
    if gaps:
        raise Missing(f'{spec["file"]}: months without a value {gaps[:5]}')
    return a, [by[i] for i in range(a, b + 1)]


def _lfp_rates(ctx, spec):
    """{file, dateColumn, valueColumn, frequency: "weekly" | "monthly"} → dict with monthly means, latest complete month and the partial month."""
    if not isinstance(spec, dict):
        raise Missing('contract.json: model.params.rate')
    for k in ('file', 'dateColumn', 'valueColumn'):
        if not spec.get(k):
            raise Missing('contract.json: model.params.rate.' + k)
    freq = spec.get('frequency', 'weekly')
    if freq not in ('weekly', 'monthly'):
        raise Missing('contract.json: model.params.rate.frequency ("weekly" or "monthly")')
    obs = []
    for r in csv.DictReader(open(ctx.need(spec['file']))):
        v = (r.get(spec['valueColumn']) or '').strip()
        if v in ('', '.'):
            continue
        d = _lfp_day(r.get(spec['dateColumn'], ''))
        if d is None:
            raise Missing(f'{spec["file"]}: dates YYYY-MM-DD; bad row {r.get(spec["dateColumn"])!r}')
        obs.append((d, float(v)))
    if not obs:
        raise Missing(f'{spec["file"]}: column {spec["valueColumn"]}')
    obs.sort()
    by = {}
    for d, v in obs:
        by.setdefault(d.year * 12 + d.month - 1, []).append((d, v))
    last_d, last_v = obs[-1]
    last_m = last_d.year * 12 + last_d.month - 1
    if freq == 'weekly':
        import datetime
        nxt = last_d + datetime.timedelta(days=7)
        latest = last_m if nxt.year * 12 + nxt.month - 1 > last_m else last_m - 1
    else:
        latest = last_m
    while latest not in by:
        latest -= 1
        if latest < min(by):
            raise Missing(f'{spec["file"]}: no complete month')
    monthly = {m: sum(v for _, v in ws) / len(ws) for m, ws in by.items() if m <= latest}

    def expected(m):   # weekly dates of month m on the series' weekday grid
        if freq != 'weekly':
            return 1
        import datetime
        d0 = datetime.date(m // 12, m % 12 + 1, 1)
        return sum(1 for k in range(31) if (d0 + datetime.timedelta(days=k)).month == d0.month and ((d0 + datetime.timedelta(days=k)) - last_d).days % 7 == 0)
    part = last_m if latest < last_m else None
    return {'freq': freq, 'monthly': monthly, 'latest': latest, 'weeks': len(by[latest]), 'expected': expected(latest), 'last_d': last_d, 'last_v': last_v,
            'partial': part, 'partial_mean': None if part is None else sum(v for _, v in by[part]) / len(by[part]), 'partial_weeks': 0 if part is None else len(by[part])}


class _Sched:
    """Scheduled balance B_k (share of the price) of a level-payment loan, cached by rate."""
    def __init__(self, L0, n):
        self.L0, self.n, self._c = L0, n, {}

    def balances(self, R):
        if R not in self._c:
            k = np.arange(self.n + 1, dtype=float)
            if R == 0:
                b = self.L0 * (1 - k / self.n)
            else:
                x = R / 1200.0
                g = (1 + x) ** k
                p = self.L0 * x / (1 - (1 + x) ** -self.n)
                b = self.L0 * g - p * (g - 1) / x
            self._c[R] = b
        return self._c[R]

    def payment(self, R):
        x = R / 1200.0
        return self.L0 / self.n if R == 0 else self.L0 * x / (1 - (1 + x) ** -self.n)

    def months(self, R, t):
        b = self.balances(R)
        hit = np.nonzero(b <= t + LFP_EPS)[0]
        return int(hit[0]) if len(hit) else None


def _lfp_params(params):
    idx, rate, down, n, rq, au, early, look, follow, cut = _need(params, 'index', 'rate', 'downShare', 'termMonths', 'requestLtv', 'autoLtv', 'lenderLtvEarly',
                                                                  'lookMonthsA', 'minFollowB', 'slowCutMonths')
    down, rq, au, early = float(down), float(rq), float(au), float(early)
    n, look, follow, cut = int(n), int(look), int(follow), int(cut)
    if not 0 < down < 1 or not (0 < au < rq < 1 - down) or not 0 < early <= rq:
        raise Missing('contract.json: model.params: 0 < downShare < 1 and 0 < autoLtv < requestLtv < 1 − downShare, 0 < lenderLtvEarly ≤ requestLtv')
    if n < 2 or n % 2 or look < 1 or follow < 1 or cut < 0:
        raise Missing('contract.json: model.params: termMonths even ≥ 2, lookMonthsA ≥ 1, minFollowB ≥ 1, slowCutMonths ≥ 0')
    buyers = params.get('buyers') or {}
    for name, b in buyers.items():
        if not isinstance(b, dict) or ym(b.get('month', '')) is None or b.get('is') not in ('min', 'median', 'max') \
                or b.get('tie', 'earliest') not in ('earliest', 'latest', 'latestYearEarliestMonth'):
            raise Missing(f'contract.json: model.params.buyers.{name} = {{month, is: "min"|"median"|"max", tie?: "earliest"|"latest"|"latestYearEarliestMonth"}}')
    slump = params.get('slump')
    if slump is not None and (ym(slump.get('peakBefore', '')) is None or ym(slump.get('troughBefore', '')) is None):
        raise Missing('contract.json: model.params.slump = {peakBefore, troughBefore} (months)')
    ref = params.get('priceRef')
    if ref is not None and not ref.get('name'):
        raise Missing('contract.json: model.params.priceRef.name')
    return {'index': idx, 'rate': rate, 'down': down, 'L0': 1 - down, 'n': n, 'rq': rq, 'au': au, 'early': early, 'look': look, 'follow': follow, 'cut': cut,
            'price': None if params.get('illustrativePrice') is None else float(params['illustrativePrice']), 'buyers': buyers, 'slump': slump,
            'priceRef': ref, 'robust': params.get('robust') or {}}


def _lfp_replay(c, sch, R, i0, H, scale=1.0):
    """Sets A and B for index H (first month i0) and monthly rates R. Returns per-purchase-month rows and the set quantities."""
    H = np.asarray(H, float) * scale
    last = i0 + len(H) - 1
    rows = {}
    for s in range(i0, last + 1):
        if s not in R:
            continue
        b = sch.balances(R[s])
        left = last - s
        kk = min(c['n'], left)
        ltv = b[:kk + 1] / (H[s - i0:s - i0 + kk + 1] / H[s - i0])
        hit = np.nonzero(ltv <= c['rq'] + LFP_EPS)[0]
        rows[s] = {'left': left, 'T': int(hit[0]) if len(hit) else None,
                   'ltvA': float(b[c['look']] / (H[s - i0 + c['look']] / H[s - i0])) if left >= c['look'] else None}
    A = sorted(s for s, r in rows.items() if r['left'] >= c['look'])
    B = sorted(s for s, r in rows.items() if r['left'] >= c['follow'])
    rq, la, le, cut = _lfp_lab(c['rq']), str(c['look']), _lfp_lab(c['early']), str(c['cut'])
    o = {'nA': (len(A), LFP_CNT), 'nB': (len(B), LFP_CNT)}
    if A:
        o.update({'firstA': (Month(A[0]), LFP_MONTH), 'lastA': (Month(A[-1]), LFP_MONTH),
                  f'shareA_ltv{la}_le{rq}': (sum(rows[s]['ltvA'] <= c['rq'] + LFP_EPS for s in A) / len(A), LFP_RATIO),
                  f'shareA_ltv{la}_le{le}': (sum(rows[s]['ltvA'] <= c['early'] + LFP_EPS for s in A) / len(A), LFP_RATIO)})
    Ts = [rows[s]['T'] for s in B if rows[s]['T'] is not None]
    if B and len(Ts) == len(B):
        mx = max(Ts)
        o.update({'firstB': (Month(B[0]), LFP_MONTH), 'lastB': (Month(B[-1]), LFP_MONTH),
                  f'medianB_months_to{rq}': (float(np.median(Ts)), LFP_CNT), f'minB_months_to{rq}': (min(Ts), LFP_CNT),
                  f'maxB_months_to{rq}': (mx, LFP_CNT), 'maxB_start': (Month(next(s for s in B if rows[s]['T'] == mx)), LFP_MONTH),
                  f'shareB_over{cut}': (sum(t > c['cut'] for t in Ts) / len(B), LFP_RATIO),
                  f'shareB_le_sched{rq}': (sum(rows[s]['T'] <= sch.months(R[s], c['rq']) for s in B) / len(B), LFP_RATIO)})
    return rows, A, B, o


def lfp_run(ctx, params, scale=1.0):
    """Every quantity of the kind (unrounded) as {key: (value, type)}, plus the working tables. scale multiplies the index (invariant replay)."""
    c = _lfp_params(params)
    i0, H = _lfp_series(ctx, c['index'], 'index')
    rt = _lfp_rates(ctx, c['rate'])
    R = rt['monthly']
    sch = _Sched(c['L0'], c['n'])
    rq, au, la = _lfp_lab(c['rq']), _lfp_lab(c['au']), str(c['look'])
    last = i0 + len(H) - 1
    Rl = R[rt['latest']]
    o = {'hpi_first': (Month(i0), LFP_MONTH), 'hpi_last': (Month(last), LFP_MONTH),
         'rate_month_latest': (Month(rt['latest']), LFP_MONTH), 'rate_latest': (Rl, LFP_RATE),
         f'sched{rq}_months_latest': (sch.months(Rl, c['rq']), LFP_CNT), f'sched{au}_months_latest': (sch.months(Rl, c['au']), LFP_CNT)}
    if rt['freq'] == 'weekly':
        o.update({'rate_last_week': (rt['last_d'].isoformat(), LFP_DAY), 'rate_last_week_value': (rt['last_v'], LFP_RATE),
                  'rate_weeks_latest': (rt['weeks'], LFP_CNT),
                  'rate_month_partial': (None if rt['partial'] is None else Month(rt['partial']), LFP_MONTH),
                  'rate_partial': (rt['partial_mean'], LFP_RATE), 'rate_weeks_partial': (rt['partial_weeks'], LFP_CNT)})
    mid = c['n'] // 2
    o.update({'midpoint_months': (mid, LFP_CNT), 'midpoint_end_month': (mid + 1, LFP_CNT),
              f'sched{au}_before_midpoint': (sch.months(Rl, c['au']) <= mid, LFP_EXACT)})
    late = sorted(m for m in R if sch.months(R[m], c['au']) > mid)
    o.update({f'n_months_sched{au}_after_midpoint': (len(late), LFP_CNT),
              'midpoint_binding_rate_min': (min(R[m] for m in late) if late else None, LFP_RATE),
              'midpoint_binding_last_month': (Month(late[-1]) if late else None, LFP_MONTH)})
    rows, A, B, so = _lfp_replay(c, sch, R, i0, H, scale)
    o.update(so)
    if A:
        sA = [sch.months(R[s], c['rq']) for s in A]
        o.update({f'sched{rq}_min_A': (min(sA), LFP_CNT), f'sched{rq}_max_A': (max(sA), LFP_CNT),
                  'rate_min_A': (min(R[s] for s in A), LFP_RATE), 'rate_max_A': (max(R[s] for s in A), LFP_RATE)})
    slow = [s for s in B if rows[s]['T'] is not None and rows[s]['T'] > c['cut']]
    o.update({'slowB_n': (len(slow), LFP_CNT), 'slowB_first': (Month(slow[0]) if slow else None, LFP_MONTH),
              'slowB_last': (Month(slow[-1]) if slow else None, LFP_MONTH), 'slowB_years': (sorted({s // 12 for s in slow}), LFP_EXACT)})
    Hs = [h * scale for h in H]
    if c['slump']:
        pb, tb = ym(c['slump']['peakBefore']), ym(c['slump']['troughBefore'])
        pk = [(Hs[i - i0], i) for i in range(i0, min(pb, last + 1))]
        if pk:
            pv, pm = max(pk, key=lambda t: (t[0], -t[1]))
            tr = [(Hs[i - i0], i) for i in range(pm + 1, min(tb, last + 1))]
            o.update({'hpi_peak_month': (Month(pm), LFP_MONTH), 'hpi_peak': (pv, LFP_RATIO)})
            if tr:
                tv, tm = min(tr)
                o.update({'hpi_trough_month': (Month(tm), LFP_MONTH), 'hpi_trough': (tv, LFP_RATIO), 'hpi_peak_to_trough_pct': (100 * (tv / pv - 1), LFP_RATE)})
    for name, b in c['buyers'].items():
        s = ym(b['month'])
        if s not in rows or rows[s]['T'] is None:
            raise Missing(f'contract.json: model.params.buyers.{name}.month {ym_str(s)}: a purchase month with a rate and an observed first passage')
        T, Rs, bal = rows[s]['T'], R[s], sch.balances(R[s])
        ch = [Hs[s + k - i0] / Hs[s - i0] - 1 for k in range(1, T + 1)]
        p = f'buyer_{name}_'
        o.update({p + 'purchaseMonth': (Month(s), LFP_MONTH), p + 'rate': (Rs, LFP_RATE), p + f'monthsTo{rq}Index': (T, LFP_CNT),
                  p + f'sched{rq}Months': (sch.months(Rs, c['rq']), LFP_CNT), p + f'sched{au}Months': (sch.months(Rs, c['au']), LFP_CNT),
                  p + f'ltvIndexAt{la}': (rows[s]['ltvA'], LFP_RATIO), p + f'hpiChangeTo{rq}Pct': (100 * (Hs[s + T - i0] / Hs[s - i0] - 1), LFP_RATE),
                  p + f'balanceAt{rq}Share': (float(bal[T]), LFP_RATIO)})
        if ch:
            kp = max(range(len(ch)), key=lambda k: (ch[k], -k))
            kt = min(range(len(ch)), key=lambda k: (ch[k], k))
            o.update({p + 'indexPeakPct': (100 * ch[kp], LFP_RATE), p + 'indexPeakMonth': (kp + 1, LFP_CNT),
                      p + 'indexTroughPct': (100 * ch[kt], LFP_RATE), p + 'indexTroughMonth': (kt + 1, LFP_CNT)})
    if c['price'] is not None:
        P, s80, s78 = c['price'], sch.months(Rl, c['rq']), sch.months(Rl, c['au'])
        o.update({'ex_price': (P, LFP_MONEY), 'ex_down': (P * c['down'], LFP_MONEY), 'ex_loan': (P * c['L0'], LFP_MONEY),
                  'ex_payment_pi': (P * sch.payment(Rl), LFP_MONEY), f'ex_balance_at_sched{rq}': (P * float(sch.balances(Rl)[s80]), LFP_MONEY),
                  f'ex_target{rq}': (P * c['rq'], LFP_MONEY), f'ex_target{au}': (P * c['au'], LFP_MONEY),
                  f'ex_extra_down_for_{_lfp_lab(1 - c["rq"])}': (P * (1 - c['rq'] - c['down']), LFP_MONEY),
                  f'ex_sched{rq}_years': (s80 / 12, LFP_RATIO), f'ex_sched{au}_years': (s78 / 12, LFP_RATIO)})
    if c['priceRef']:
        ref = c['priceRef']
        by = monthly_values(ctx, ref, 'priceRef')
        m = max(by)
        per = 'quarter' if all(i % 3 == 0 for i in by) else 'month'
        o.update({f'{ref["name"]}_{per}': (Month(m), LFP_MONTH), f'{ref["name"]}_latest': (by[m], LFP_MONEY)})
    for key, spec in c['robust'].items():
        j0, G = _lfp_series(ctx, spec, f'robust.{key}')
        lo, hi = max(i0, j0), min(last, j0 + len(G) - 1)
        _, _, _, ro = _lfp_replay(c, sch, R, lo, G[lo - j0:hi - j0 + 1], scale)
        for k in ('nA', 'nB', f'shareA_ltv{la}_le{rq}', f'shareA_ltv{la}_le{_lfp_lab(c["early"])}', f'medianB_months_to{rq}', f'shareB_over{c["cut"]}',
                  f'maxB_months_to{rq}', 'maxB_start'):
            if k in ro:
                o[f'robust_{key}_{k}'] = ro[k]
    return {'c': c, 'i0': i0, 'H': H, 'R': R, 'rt': rt, 'sch': sch, 'rows': rows, 'A': A, 'B': B, 'out': o}


def _lfp_cached(ctx, params, scale=1.0):
    return ctx.memo(('lfp-run', id(params), scale), lambda: (params, lfp_run(ctx, params, scale)))[1]


LFP_INPUTS = {'downShare': ('down', LFP_RATIO), 'termMonths': ('n', LFP_CNT), 'requestLtv': ('rq', LFP_RATIO), 'autoLtv': ('au', LFP_RATIO),
              'lenderLtvEarly': ('early', LFP_RATIO), 'lookMonthsA': ('look', LFP_CNT), 'minFollowB': ('follow', LFP_CNT), 'slowCutMonths': ('cut', LFP_CNT),
              'illustrativePrice': ('price', LFP_MONEY)}


def lfp_value(ctx, params, key):
    """Keys (S05): every key of the model file the kind computes (e.g. "sched80_months_latest", "shareA_ltv24_le75", "medianB_months_to80", "maxB_start",
    "buyer_slow_monthsTo80Index", "ex_payment_pi", "robust_cs_maxB_months_to80"); the inputs "downShare", "termMonths", "requestLtv", "autoLtv",
    "lenderLtvEarly", "lookMonthsA", "minFollowB", "slowCutMonths", "illustrativePrice"; and "fraction:<key>" = a % key / 100 (a claim written as a share).
    Tolerances: rates and % 0.005; shares, LTV, years, index levels 0.0005; money $0.50; counts and months exactly (YYYY-MM ≡ YYYY-MM-01); names, lists,
    booleans and null by equality."""
    run = _lfp_cached(ctx, params)
    o = run['out']
    if key in LFP_INPUTS and run['c'][LFP_INPUTS[key][0]] is not None:
        f, how = LFP_INPUTS[key]
        return float(run['c'][f]), LFP_TOL[how]
    frac = key.startswith('fraction:')
    k = key.partition(':')[2] if frac else key
    if k not in o or frac and o[k][1] != LFP_RATE:
        raise Missing(f'contract.json: model.claims key "{key}" is not a quantity of kind ltv-first-passage')
    v, how = o[k]
    if v is None or how in (LFP_EXACT, LFP_DAY):
        return Exact(v), 0
    if how == LFP_MONTH:
        return v, 0
    return (float(v) / 100, LFP_TOL[how] / 100) if frac else (float(v), LFP_TOL[how])


def lfp_compare(ctx, params, out):
    """The model file: {params (echo, not compared), raw: {key: unrounded value}, rounded?: {...} (display, not compared)}; a flat file without "raw" is
    read as raw. S01: money max($0.50, 1e-6 relative); rates, shares, LTV, index levels 1e-9 relative; counts exactly; months exactly after
    normalisation; the last weekly date, booleans, lists and null by equality. Every key the kind computes must be present; a raw key it does not compute
    (and not in conventions / notModel) is listed."""
    o = _lfp_cached(ctx, params)['out']
    raw = out.get('raw') if isinstance(out.get('raw'), dict) else out
    bad, checked = [], 0
    for k, (v, how) in o.items():
        checked += 1
        t = raw.get(k, '<absent>')
        shown = ym_str(v) if how == LFP_MONTH and v is not None else v
        if t == '<absent>':
            bad.append((k, 'absent', shown))
            continue
        if v is None or how in (LFP_EXACT, LFP_DAY):
            ok = Exact(v).same(t) and (type(t) is bool) == (type(v) is bool)
        elif how == LFP_MONTH:
            ok = isinstance(t, str) and ym(t) == int(v)
        elif isinstance(t, bool) or not isinstance(t, (int, float)):
            ok = False
        elif how == LFP_CNT:
            ok = t == v
        elif how == LFP_MONEY:
            ok = close(t, v)
        else:
            ok = abs(t - v) <= 1e-9 * max(1.0, abs(v))
        if not ok:
            bad.append((k, t, shown))
    for k, v in (params.get('conventions') or {}).items():
        checked += 1
        if raw.get(k) != v:
            bad.append((k, raw.get(k), v))
    covered = set(o) | set(params.get('conventions') or {}) | set(params.get('notModel', []))
    unrec = sorted(set(raw) - covered)
    if raw is not out:
        unrec += sorted(set(out) - {'params', 'raw', 'rounded'} - covered)
    return checked, bad, unrec


def lfp_invariants(ctx, params):
    """The spec's invariants (newKindNeeds.invariants) and numbers.md's rules, on the contract's own inputs:
    (1) B_0 = L0 and B_n = 0 (±1e-9), B_k strictly decreasing, at every monthly rate; (2) sched(R, requestLtv) < sched(R, autoLtv) ≤ n and both
    non-decreasing in R; (3) T(s) ≥ 1 in set B (LTV(s, 0) = L0 > requestLtv); (4) T(s) ≤ sched(R(s), requestLtv) whenever the index never fell below
    the purchase month's level up to that schedule month; (5) share at ≤ lenderLtvEarly ≤ share at ≤ requestLtv; (6) every T(s) in set B observed (not
    censored); (7) shares in [0, 1], nA ≥ nB, lastB < lastA; (8) the latest rate month is complete (every weekly date of the month) and any partial
    month is later; (9) each buyer's month is in set B, its T is the set's min / median / max, and its tie rule picks that month; (10) multiplying the
    index by 2.5 changes no quantity but the index levels."""
    run = _lfp_cached(ctx, params)
    c, sch, R, rows, A, B, o, rt = run['c'], run['sch'], run['R'], run['rows'], run['A'], run['B'], run['out'], run['rt']
    H, i0 = run['H'], run['i0']
    rates = sorted(set(R.values()))
    e1 = 0
    for r in rates:
        b = sch.balances(r)
        e1 += int(abs(b[0] - c['L0']) > 1e-9 or abs(b[-1]) > 1e-9 or not np.all(np.diff(b) < 0))
    s_rq = [sch.months(r, c['rq']) for r in rates]
    s_au = [sch.months(r, c['au']) for r in rates]
    e2 = sum(1 for a, b in zip(s_rq, s_au) if a is None or b is None or not a < b <= c['n'])
    e2 += sum(1 for x, y in zip(s_rq, s_rq[1:]) if y < x) + sum(1 for x, y in zip(s_au, s_au[1:]) if y < x)
    Ts = {s: rows[s]['T'] for s in B}
    e3 = sum(1 for t in Ts.values() if t is not None and t < 1)
    e4 = 0
    for s in B:
        k80 = sch.months(R[s], c['rq'])
        if Ts[s] is not None and s + k80 - i0 < len(H) and min(H[s - i0:s - i0 + k80 + 1]) >= H[s - i0] and Ts[s] > k80:
            e4 += 1
    rq, la, le = _lfp_lab(c['rq']), str(c['look']), _lfp_lab(c['early'])
    sh_rq, sh_le = o.get(f'shareA_ltv{la}_le{rq}', (0, 0))[0], o.get(f'shareA_ltv{la}_le{le}', (0, 0))[0]
    cens = sum(1 for t in Ts.values() if t is None)
    shares = [v for k, (v, how) in o.items() if k.startswith(('shareA_', 'shareB_')) or '_share' in k]
    e7 = sum(1 for v in shares if not 0 <= v <= 1) + int(len(A) < len(B)) + int(bool(A and B) and B[-1] >= A[-1])
    e8 = int(rt['weeks'] != rt['expected']) + int(rt['partial'] is not None and rt['partial'] <= rt['latest'])
    e9 = 0
    vals = sorted(t for t in Ts.values() if t is not None)
    for name, b in c['buyers'].items():
        s = ym(b['month'])
        if s not in Ts or Ts[s] is None:
            e9 += 1
            continue
        want = {'min': vals[0], 'max': vals[-1], 'median': float(np.median(vals))}[b['is']]
        if Ts[s] != want:
            e9 += 1
            continue
        same = [m for m in B if Ts[m] == want]
        tie = b.get('tie', 'earliest')
        pick = same[0] if tie == 'earliest' else same[-1] if tie == 'latest' else min(m for m in same if m // 12 == max(x // 12 for x in same))
        e9 += int(pick != s)
    o2 = _lfp_cached(ctx, params, 2.5)['out']
    levels = {'hpi_peak', 'hpi_trough'}
    drift = sum(1 for k, (v, how) in o.items() if k not in levels and not (
        o2[k][0] == v if not isinstance(v, float) or isinstance(v, bool) else abs(o2[k][0] - v) <= 1e-9 * max(1.0, abs(v))))
    return [metric('schedules with B_0 ≠ L0, B_n ≠ 0 or a balance not strictly decreasing (every monthly rate)', e1, '<=', 0),
            metric('rates where sched(requestLtv) < sched(autoLtv) ≤ n fails, or a schedule decreasing in the rate', e2, '<=', 0),
            metric('set-B months with T < 1', e3, '<=', 0),
            metric('set-B months with the index never below purchase yet T later than the schedule', e4, '<=', 0),
            metric(f'share at ≤ {le} minus share at ≤ {rq} (set A)', sh_le - sh_rq, '<=', 0),
            metric('set-B months whose first passage is not observed (censored)', cens, '<=', 0),
            metric('shares outside [0, 1], nA < nB, or lastB ≥ lastA', e7, '<=', 0),
            metric('latest rate month incomplete, or a partial month not after it', e8, '<=', 0),
            metric('buyers not in set B, not at their min / median / max, or not picked by their tie rule', e9, '<=', 0),
            metric('quantities changed when the index is multiplied by 2.5 (index levels aside)', drift, '<=', 0)]


KINDS = {'retirement-6040': (ret_compare, ret_value, ret_invariants),
         'refinance-breakeven': (refi_compare, refi_value, lambda ctx, p: []),
         'float-vs-fixed-replay': (fvf_compare, fvf_value, fvf_invariants),
         'lock-vs-roll-replay': (lvr_compare, lvr_value, lvr_invariants),
         'fixed-cap-vs-index-growth': (fci_compare, fci_value, fci_invariants),
         'ltv-first-passage': (lfp_compare, lfp_value, lfp_invariants)}


def kind(ctx):
    k = ctx.cfield('model', 'kind', kind=str)
    if k not in KINDS:
        raise Missing(f'an independent re-computation for model kind "{k}" (checks/py/r_model.py KINDS: {sorted(KINDS)}); the checking session writes it')
    return KINDS[k]
