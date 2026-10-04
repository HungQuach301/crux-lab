#!/usr/bin/env python3
"""H2 data: recompute the replay exactly as episodes/ep002/model/model.py (same formula, same TB3MS file), add the
month-by-month cushion (cumulative fixed interest - variable interest) for the windows shown, assert every headline
against out/claims.json, write ../work/data.js (NOT committed: contains a FRED-derived series; see ../.gitignore).
python3 src/build_data.py"""
import csv, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
H2 = os.path.dirname(HERE)
EP = os.path.abspath(os.path.join(H2, '../../../'))
P, N, FIXED, VAR0, FIRST, SPLIT = 50000.0, 120, 9.0, 7.5, '1954-01-01', '1981-01-01'
GAPS = [-1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
rows = [(r[0], float(r[1])) for r in list(csv.reader(open(os.path.join(EP, 'data/raw/TB3MS.csv'))))[1:] if r[1] not in ('', '.')]
dates = [d for d, _ in rows]; tb = [v for _, v in rows]; IDX = tb[-1]

def run(path):
    bal, cur, pay, ints, bals = P, None, 0.0, [], []
    for k, r in enumerate(path):
        if r != cur:
            x = r / 1200; pay = bal * x / (1 - (1 + x) ** -(N - k)); cur = r
        i = bal * r / 1200; ints.append(i); bals.append(bal); bal -= pay - i
    return ints, bals

FIX_INTS, FIX_BALS = run([FIXED] * N); FIX_INT = sum(FIX_INTS)
starts = [s for s in range(len(tb)) if dates[s] >= FIRST and s + N <= len(tb)]
def path_of(s, var0): m = var0 - IDX; return [round(m + max(0.0, IDX + tb[s + k] - tb[s]), 6) for k in range(N)]
def diffs(var0): return [sum(run(path_of(s, var0))[0]) - FIX_INT for s in starts]

base = diffs(VAR0)
above = [max(path_of(s, VAR0)) > FIXED for s in starts]
early = [i for i, s in enumerate(starts) if dates[s] < SPLIT]; late = [i for i, s in enumerate(starts) if dates[s] >= SPLIT]
sh = lambda ix, d: round(100 * sum(d[i] > 0 for i in ix) / len(ix), 1)
cl = {c['claimId']: c for c in json.load(open(os.path.join(EP, 'out/claims.json')))['claims']}
def chk(cid, v):
    assert abs(cl[cid]['value'] - v) < 0.051 or str(cl[cid]['value']) == str(v), (cid, cl[cid]['value'], v)
chk('n_starts', len(starts)); chk('share_all', sh(range(len(starts)), base)); chk('share_early', sh(early, base))
chk('share_late', sh(late, base)); chk('worst_diff', round(max(base))); chk('share_rate_above_fixed', round(100 * sum(above) / len(above), 1))
chk('fixed_int', round(FIX_INT))
wi = max(range(len(base)), key=lambda i: base[i]); assert dates[starts[wi]][:7] == '1977-04'
assert round(max(path_of(starts[wi], VAR0)), 1) == 19.3
gap = {}
for g in GAPS:
    d = diffs(FIXED - g)
    gap[f'{g:g}'] = {'costlier': ''.join('1' if x > 0 else '0' for x in d), 'worst': round(max(d)),
                     'early': sh(early, d), 'late': sh(late, d), 'all': sh(range(len(starts)), d)}
for g, k in [(2, 'gap20'), (3, 'gap30'), (1, 'gap10'), (0, 'gap00'), (-1, 'gapm10')]:
    chk(k + '_early', gap[f'{g:g}']['early']); chk(k + '_late', gap[f'{g:g}']['late']); chk(k + '_worst', gap[f'{g:g}']['worst'])
for g, k in [(2, 'spread2_share'), (3, 'spread3_share'), (1, 'spread1_share'), (0, 'spread0_share'), (-1, 'spreadm1_share')]:
    chk(k, gap[f'{g:g}']['all'])

def detail(start, var0=VAR0):
    s = dates.index(start + '-01'); p = path_of(s, var0); vi, vb = run(p); cum, c = [], 0.0
    for k in range(N): c += FIX_INTS[k] - vi[k]; cum.append(round(c, 2))
    return {'start': start, 'path': p, 'bal': [round(b, 2) for b in vb], 'cushion': cum, 'diff': round(-cum[-1], 2),
            'tb': tb[s:s + N]}
SHOW = ['1981-08', '1988-07', '1958-06', '1976-04', '1986-03', '1998-11', '1977-04', '1954-01', '1962-03', '1985-02', '1999-05', '2004-06', '1968-09']
det = {k: detail(k) for k in SHOW}
assert round(det['1977-04']['diff']) == 11219 and round(det['1981-08']['diff']) == -15295
ridge = [{'m': dates[i][:7], 'r': tb[i]} for i in range(len(tb)) if dates[i] >= '1953-01-01']
out = {'ridge': ridge, 'starts': [dates[s][:7] for s in starts], 'base': [round(x, 2) for x in base],
       'above': ''.join('1' if a else '0' for a in above), 'gap': gap, 'detail': det,
       'fixInts': [round(x, 4) for x in FIX_INTS], 'fixBals': [round(x, 2) for x in FIX_BALS], 'fixInt': FIX_INT,
       'claims': {k: v['display'] for k, v in cl.items()}}
os.makedirs(os.path.join(H2, 'work'), exist_ok=True)
open(os.path.join(H2, 'work/data.js'), 'w').write('window.DATA = ' + json.dumps(out) + ';\n')
print('ok; worst', round(max(base)), 'gaps', {k: (v['early'], v['late'], v['worst']) for k, v in gap.items()})
