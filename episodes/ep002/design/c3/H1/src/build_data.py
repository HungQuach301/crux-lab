#!/usr/bin/env python3
"""H1 (C3 Tập 2) — dữ liệu cho cảnh. Đọc episodes/ep002/data/raw/TB3MS.csv (FRED, KHÔNG commit), chạy lại đúng lõi
model/model.py, assert khớp out/model.json + out/claims.json, rồi ghi src/data.js (trong .gitignore của thư mục này).
   python3 src/build_data.py"""
import csv, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.abspath(os.path.join(HERE, '../../../..'))
P, N, FIXED, VAR0 = 50000.0, 120, 9.00, 7.50
rows = [(r[0][:7], float(r[1])) for r in list(csv.reader(open(os.path.join(EP, 'data/raw/TB3MS.csv'))))[1:] if r[1] not in ('', '.')]
dates = [d for d, _ in rows]; tb = [v for _, v in rows]; IDX = tb[-1]


def run(path):
    bal, tot, cur, pay, ints, bals = P, 0.0, None, 0.0, [], []
    for k, r in enumerate(path):
        if r != cur:
            x = r / 1200; pay = bal * x / (1 - (1 + x) ** -(N - k)); cur = r
        i = bal * r / 1200; tot += i; ints.append(i); bals.append(bal); bal -= pay - i
    return tot, ints, bals


FIX_INT, FIX_I, FIX_B = run([FIXED] * N)
s0 = dates.index('1954-01')
starts = [s for s in range(s0, len(tb)) if s + N <= len(tb)]


def path_for(s, var0):
    m = var0 - IDX
    return [round(m + max(0.0, IDX + tb[s + k] - tb[s]), 6) for k in range(N)]


GAPS = [round(-1 + 0.25 * i, 2) for i in range(17)]  # -1 .. 3
win = []
costlier = {g: [] for g in GAPS}
worst = {}
for s in starts:
    p = path_for(s, VAR0)
    vi, ints, _ = run(p)
    win.append({'start': dates[s], 'diff': vi - FIX_INT, 'above': max(p) > FIXED, 'max': max(p)})
for g in GAPS:
    best = None
    for s in starts:
        vi, _, _ = run(path_for(s, FIXED - g))
        d = vi - FIX_INT
        costlier[g].append(1 if d > 0 else 0)
        if best is None or d > best[0]: best = (d, dates[s])
    worst[g] = best

# ---- assert against the episode's model + claims
M = json.load(open(os.path.join(EP, 'out/model.json')))
assert len(win) == M['nWindows'] == 753
for a, b in zip(win, M['windows']):
    assert a['start'] == b['start'] and abs(a['diff'] - b['difference']) < 1e-6
share = lambda xs: 100 * sum(xs) / len(xs)
assert abs(share(costlier[1.5]) - M['shareCostlier']) < 1e-9
for k, v in M['sensitivity'].items():
    assert abs(share(costlier[float(k)]) - v) < 1e-9, k
CL = {c['claimId']: c for c in json.load(open(os.path.join(EP, 'out/claims.json')))['claims']}
assert abs(share([w['above'] for w in win]) - CL['share_rate_above_fixed']['value']) < 0.06
early = [i for i, w in enumerate(win) if w['start'] < '1981-01']
assert len(early) == 324
assert abs(share([costlier[2.0][i] for i in early]) - CL['gap20_early']['value']) < 0.06
assert abs(share([costlier[3.0][i] for i in early]) - CL['gap30_early']['value']) < 0.06
assert sum(costlier[2.0][i] for i in range(324, 753)) == 0
iw = max(range(753), key=lambda i: win[i]['diff']); assert win[iw]['start'] == '1977-04'
assert all(worst[g][1] == '1977-04' for g in GAPS)


def cushion(start):
    s = dates.index(start); p = path_for(s, VAR0); vi, ints, bals = run(p)
    c, cs = 0.0, []
    for k in range(N): c += FIX_I[k] - ints[k]; cs.append(c)
    return {'start': start, 'rates': p, 'cushion': cs, 'balance': bals, 'varInt': ints, 'diff': vi - FIX_INT}


# candidates for KEY-4 (printed for the designer)
if os.environ.get('SCAN'):
    for i, s in enumerate(starts):
        p = path_for(s, VAR0); n = sum(r > FIXED for r in p)
        if 1 <= n <= 8 and win[i]['diff'] < -2500:
            fa = next(k for k, r in enumerate(p) if r > FIXED)
            print(dates[s], 'months>9:', n, 'first above at', fa, 'diff', round(win[i]['diff']))
    raise SystemExit

ridge = [[d, v] for d, v in zip(dates, tb) if d >= '1954-01']
data = {
    'ridge': ridge, 'starts': [w['start'] for w in win], 'above': [1 if w['above'] else 0 for w in win],
    'costlier': {f'{g:g}': costlier[g] for g in GAPS}, 'worstAt': {f'{g:g}': round(worst[g][0]) for g in GAPS},
    'fixedInt': FIX_INT, 'fixedIntM': FIX_I, 'fixedBal': FIX_B, 'worstIdx': iw,
    'runs': {k: cushion(k) for k in ['2002-01', '1954-01', '1956-05', '1976-06', '1977-04', '1989-03']},
    'claims': {k: {'display': v['display']} for k, v in CL.items()},
}
open(os.path.join(HERE, 'data.js'), 'w').write('window.DATA=' + json.dumps(data, separators=(',', ':')) + ';\n')
print('ok: 753 windows, asserts passed; data.js', os.path.getsize(os.path.join(HERE, 'data.js')), 'bytes')
