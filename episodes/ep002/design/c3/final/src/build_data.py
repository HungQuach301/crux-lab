#!/usr/bin/env python3
"""Final (D2) data: recompute the replay exactly as episodes/ep002/model/model.py (same formula as H2/H3 build_data),
assert every value shown against out/claims.json, write ../work/data.js (NOT committed: FRED-derived series).
python3 src/build_data.py"""
import csv, json, os
HERE = os.path.dirname(os.path.abspath(__file__)); FIN = os.path.dirname(HERE)
EP = os.path.abspath(os.path.join(FIN, '../../../'))
P, N, FIXED, VAR0, FIRST, SPLIT = 50000.0, 120, 9.0, 7.5, '1954-01-01', '1981-01-01'
GAPS = [-1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
rows = [(r[0], float(r[1])) for r in list(csv.reader(open(os.path.join(EP, 'data/raw/TB3MS.csv'))))[1:] if r[1] not in ('', '.')]
dates = [d for d, _ in rows]; tb = [v for _, v in rows]; IDX = tb[-1]

def run(path):
    bal, cur, pay, tot = P, None, 0.0, 0.0
    for k, r in enumerate(path):
        if r != cur:
            x = r / 1200; pay = bal * x / (1 - (1 + x) ** -(N - k)); cur = r
        i = bal * r / 1200; tot += i; bal -= pay - i
    return tot
FIX_INT = run([FIXED] * N)
starts = [s for s in range(len(tb)) if dates[s] >= FIRST and s + N <= len(tb)]
def path_of(s, var0): m = var0 - IDX; return [round(m + max(0.0, IDX + tb[s + k] - tb[s]), 6) for k in range(N)]
early = [i for i, s in enumerate(starts) if dates[s] < SPLIT]; late = [i for i, s in enumerate(starts) if dates[s] >= SPLIT]
sh = lambda ix, d: round(100 * sum(d[i] > 0 for i in ix) / len(ix), 1)
cl = {c['claimId']: c for c in json.load(open(os.path.join(EP, 'out/claims.json')))['claims']}
def chk(cid, v): assert abs(cl[cid]['value'] - v) < (0.51 if abs(v) > 1000 else 0.051), (cid, cl[cid]['value'], v)
chk('n_starts', len(starts)); chk('n_early', len(early)); chk('n_late', len(late))
gap = {}
for g in GAPS:
    d = [run(path_of(s, FIXED - g)) - FIX_INT for s in starts]
    gap[f'{g:g}'] = {'costlier': ''.join('1' if x > 0 else '0' for x in d), 'early': sh(early, d), 'late': sh(late, d),
                     'all': sh(range(len(starts)), d), 'worst': round(max(d))}
for g, k in [(-1, 'gapm10'), (-0.5, 'gapm05'), (0, 'gap00'), (0.5, 'gap05'), (1, 'gap10'), (1.5, 'gap15'), (2, 'gap20'), (2.5, 'gap25'), (3, 'gap30')]:
    for h in ('early', 'late', 'worst'): chk(f'{k}_{h}', gap[f'{g:g}'][h])
assert gap['1.5']['early'] == 28.4 and gap['1.5']['late'] == 3.5
# KEY-1: one real replay of Leah's loan (7.5% start) that goes above and below 9% several times (chosen by eye from
# the windows with >= 6 crossings of 9% and max <= 12.5%): start December 1962. Not labelled on screen (no claim).
K1_START = '1962-12'
s1 = dates.index(K1_START + '-01'); k1p = path_of(s1, VAR0)
assert sum((k1p[k] - FIXED) * (k1p[k + 1] - FIXED) < 0 for k in range(N - 1)) >= 6 and max(k1p) <= 12.6 and k1p[0] == VAR0
k1 = (None, K1_START, k1p)
ridge = [{'m': dates[i][:7], 'r': tb[i]} for i in range(len(tb)) if dates[i] >= '1953-01-01']
out = {'ridge': ridge, 'starts': [dates[s][:7] for s in starts], 'gap': gap, 'k1': {'start': k1[1], 'path': k1[2]},
       'claims': {k: v['display'] for k, v in cl.items()}}
os.makedirs(os.path.join(FIN, 'work'), exist_ok=True)
open(os.path.join(FIN, 'work/data.js'), 'w').write('window.DATA = ' + json.dumps(out) + ';\n')
print('ok; gaps', {k: (v['early'], v['late']) for k, v in gap.items()}, 'K1 start', k1[1])
