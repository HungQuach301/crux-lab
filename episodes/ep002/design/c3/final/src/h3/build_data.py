#!/usr/bin/env python3
"""H3 data: re-runs the ep002 model arithmetic (same formula as model/model.py) on data/normalized/tb3ms_monthly.csv,
asserts every window against out/model.json, and writes final/work/h3data.js (FRED-derived, not committed) (window.DATA) for the renderer.
   python3 episodes/ep002/design/c3/H3/src/build_data.py"""
import csv, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.abspath(os.path.join(HERE, '../../../../..'))
P, N, FIXED, VAR0 = 50000.0, 120, 9.0, 7.5
rows = [(r[0][:7], float(r[1])) for r in list(csv.reader(open(os.path.join(EP, 'data/normalized/tb3ms_monthly.csv'))))[1:]]
dates = [d for d, _ in rows]; tb = [v for _, v in rows]; IDX = tb[-1]
model = json.load(open(os.path.join(EP, 'out/model.json')))
claims = {c['claimId']: c for c in json.load(open(os.path.join(EP, 'out/claims.json')))['claims']}

def run(path):
    bal, tot, cur, pay, ints, bals = P, 0.0, None, 0.0, [], []
    for k, r in enumerate(path):
        if r != cur:
            x = r / 1200; pay = bal * x / (1 - (1 + x) ** -(N - k)); cur = r
        i = bal * r / 1200; tot += i; bals.append(bal); bal -= pay - i; ints.append(i)
    return tot, ints, bals

FIX_INT, FIX_INTS, FIX_BALS = run([FIXED] * N)
starts = [s for s in range(len(tb)) if dates[s] >= '1954-01' and s + N <= len(tb)]
def path(s, var0): m = var0 - IDX; return [round(m + max(0.0, IDX + tb[s + k] - tb[s]), 6) for k in range(N)]

wins = []
for s, mw in zip(starts, model['windows']):
    p = path(s, VAR0); vi, ints, bals = run(p)
    assert dates[s] == mw['start'] and abs((vi - FIX_INT) - mw['difference']) < 1e-6, dates[s]
    wins.append({'s': s, 'start': dates[s], 'diff': vi - FIX_INT, 'maxRate': max(p), 'path': p, 'ints': ints, 'bals': bals})
assert len(wins) == 753
share = lambda ws: 100 * sum(w['diff'] > 0 for w in ws) / len(ws)
early = [w for w in wins if w['start'] < '1981-01']; late = [w for w in wins if w['start'] >= '1981-01']
assert claims['share_all']['display'] == f"{share(wins):.1f}%" and claims['share_early']['display'] == f"{share(early):.1f}%"
assert claims['share_late']['display'] == f"{share(late):.1f}%"
assert claims['share_rate_above_fixed']['display'] == f"{100*sum(w['maxRate']>FIXED for w in wins)/753:.1f}%"
worst = max(wins, key=lambda w: w['diff']); assert worst['start'] == '1977-04'

# head-start sweep (fixed stays 9%; variable starts at 9 - g), g = -1.00 .. 3.00 step 0.05
G = [round(-1 + 0.05 * i, 2) for i in range(81)]
sweep = []
for g in G:
    d = [run(path(w['s'], FIXED - g))[0] - FIX_INT for w in wins]
    sweep.append({'g': g, 'bits': ''.join('1' if x > 0 else '0' for x in d), 'worst': max(d), 'worstIdx': d.index(max(d))})
for g, ce, cl in [(2.0, 'gap20_early', 'gap20_late'), (3.0, 'gap30_early', 'gap30_late'), (1.0, 'gap10_early', 'gap10_late')]:
    b = next(x for x in sweep if abs(x['g'] - g) < 1e-9)['bits']
    e = 100 * b[:324].count('1') / 324; l = 100 * b[324:].count('1') / 429
    assert claims[ce]['display'] == f"{e:.1f}%".replace('.0%', '%'), (ce, e)
    assert claims[cl]['display'] in (f"{l:.1f}%", f"{l:.0f}%"), (cl, l)
assert all(x['worstIdx'] == wins.index(worst) for x in sweep)

def cushion(w):  # cumulative interest saved vs fixed, month by month (end value = -diff)
    c, out = 0.0, []
    for a, b in zip(FIX_INTS, w['ints']): c += a - b; out.append(c)
    assert abs(out[-1] + w['diff']) < 1e-6
    return [round(x, 2) for x in out]

# KEY-4 example windows: a short blip (exceeds 9% for few months, ends far cheaper), a long early climb (costlier, not the worst), a falling stretch (best)
def months_above(w): return sum(r > FIXED for r in w['path'])
def first_above(w): return next((k for k, r in enumerate(w['path']) if r > FIXED), None)
def peak_cushion(w):
    c, m = 0.0, 0.0
    for a, b in zip(FIX_INTS, w['ints']): c += a - b; m = max(m, c)
    return m
# blip: rate first exceeds 9% after month 24, for at most 8 months, loan ends cheaper; take the highest such peak
blip = max([w for w in wins if (first_above(w) or 0) >= 24 and 1 <= months_above(w) <= 8 and w['diff'] < 0], key=lambda w: w['maxRate'])
# climb: a 1954-1980 costlier loan whose cushion first reached at least $3,000 (so the jar visibly fills, then drains dry); largest cost
climb = max([w for w in early if w['diff'] > 0 and peak_cushion(w) >= 3000 and w is not worst], key=lambda w: w['diff'])
best = min(wins, key=lambda w: w['diff']); assert best['start'] == '1981-08'
ex = {}
for k, w in [('blip', blip), ('climb', climb), ('fall', best), ('worst', worst)]:
    ex[k] = {'i': wins.index(w), 'start': w['start'], 'diff': round(w['diff'], 2), 'path': w['path'], 'cushion': cushion(w),
             'bals': [round(b, 2) for b in w['bals']], 'monthsAbove': months_above(w)}
    print(k, w['start'], round(w['diff']), 'months above 9%:', months_above(w), 'max cushion', max(ex[k]['cushion']))

data = {
    'series': [[d, v] for d, v in zip(dates, tb) if d >= '1954-01'],
    'windows': [{'start': w['start'], 'diff': round(w['diff'], 2), 'above': w['maxRate'] > FIXED, 'tb0': tb[w['s']]} for w in wins],
    'sweep': sweep, 'ex': ex, 'fixInt': FIX_INT, 'worstIdx': wins.index(worst),
    'claims': {k: {'display': v['display'], 'illustrative': v.get('illustrative', False)} for k, v in claims.items()},
}
os.makedirs(os.path.join(HERE, '../../work'), exist_ok=True)
open(os.path.join(HERE, '../../work/h3data.js'), 'w').write('window.DATA=' + json.dumps(data, separators=(',', ':')) + ';\n')
print('ok: 753/753 windows match out/model.json; sweep', len(sweep), 'steps')
