"""So out/model.json (bên dựng) với model/independent/recompute.json (agent độc lập) theo dung sai gates/V0-defs.md."""
import json, os
EP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
a = json.load(open(os.path.join(EP, 'out/model.json')))
b = json.load(open(os.path.join(EP, 'model/independent/recompute.json')))
nd = lambda v: v + '-01' if isinstance(v, str) and len(v) == 7 else v
def tol(k):
    if 'share' in k: return 0.1
    if 'payment' in k: return 0.01
    if 'rate' in k or k in ('index_today', 'margin'): return 0.01
    if k.startswith('n_'): return 0
    return 1
rows, bad, fmt = [], 0, 0
def cmp(path, x, y, k):
    global bad, fmt
    if isinstance(x, str) or isinstance(y, str):
        ok = nd(x) == nd(y); f = ok and x != y
        fmt += f
    else:
        ok = abs(x - y) <= tol(k) + 1e-9
    bad += not ok
    rows.append((path, x, y, 'OK' + (' (chỉ khác cách viết)' if isinstance(x, str) and x != y and ok else '') if ok else 'LỆCH'))
for k, v in a['base'].items():
    if k == 'index_date': continue
    cmp('base.' + k, v, b['core'][k], k)
skipped = []
for k, v in a['payments'].items():
    if k not in b['payments']: skipped.append('payments.' + k); continue
    cmp('payments.' + k, v, b['payments'][k], k)
for grid in ('gaps', 'caps'):
    for g, d in a[grid].items():
        for k, v in d.items():
            cmp(f'{grid}.{g}.{k}', v, b[grid][g][k], k)
bw = {nd(w['start']): w for w in b['windows']}
wbad = sign = 0
for w in a['windows']:
    o = bw[w['start']]
    wbad += abs(w['diff'] - o['diff']) > 0.05 or abs(w['maxRate'] - o['maxRate']) > 0.0001 or abs(w['maxPay'] - o['maxPay']) > 0.01
    sign += (w['diff'] > 0) != (o['diff'] > 0)
print(f"đại lượng: {len(rows)} so, {bad} lệch, {fmt} chỉ khác cách viết ngày")
print('không có trong định nghĩa V0 (không kiểm, không dùng làm claim):', skipped)
print(f"cửa sổ: {len(a['windows'])} vs {len(b['windows'])}; lệch {wbad}; khác dấu {sign}")
for r in rows:
    if r[3] != 'OK': print(r)
json.dump({'n': len(rows), 'mismatch': bad, 'formatOnly': fmt, 'windows': len(a['windows']), 'windowMismatch': wbad, 'signMismatch': sign,
           'rows': rows}, open(os.path.join(EP, 'model/independent/compare.json'), 'w'), indent=1)
