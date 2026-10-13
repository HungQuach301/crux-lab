"""Tập 8 · dữ liệu hình cho các đoạn thế giới (một hàng mỗi tháng bắt đầu), dẫn xuất từ model/model.py (cùng định nghĩa với out/model.json).
    python3 episodes/ep008/world/data.py → episodes/ep008/world/data.json
starts10 (307 tháng, Jan 1991 → Jul 2016): ahead10[y] (người mua hơn sau 10 năm, giả định tiền thuê y = 4/5/6 % và hai mốc Census, tbills),
adv10 (chênh $, neo 5 %), ratio1 (tiền thuê tháng đầu / chi người mua tháng đầu); starts5 / ahead5; starts15 / ahead15. Kiểm chéo với
out/model.json (số đếm, tỉ lệ) — lệch → dừng."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); EP = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(EP, 'model')); sys.dont_write_bytecode = True
import model as M  # noqa: E402
Q = json.load(open(os.path.join(EP, 'out', 'model.json')))['quantities']
hpi, cpi, tb, rate, rml, lw = M.load(); D = (hpi, cpi, tb, rate)
s10, s5, s15 = M.starts(10, D), M.starts(5, D), M.starts(15, D)
run = lambda s, H, **k: M.run(s, H, D, **k)
r10 = [run(s, 10) for s in s10]
out = {'starts10': s10, 'starts5': s5, 'starts15': s15,
       'ahead10': {'5': [r['adv'] > 0 for r in r10]},
       'adv10': [round(r['adv']) for r in r10], 'ratio1': [round(r['m1rent'] / r['m1buy'], 4) for r in r10],
       'ahead5': [run(s, 5)['adv'] > 0 for s in s5], 'ahead15': [run(s, 15)['adv'] > 0 for s in s15]}
for y in (4, 6):
    out['ahead10'][str(y)] = [run(s, 10, y0=y / 100)['adv'] > 0 for s in s10]
for k in ('hvs_yield_2025Q4', 'hvs_yield_2026Q1'):
    out['ahead10'][k] = [run(s, 10, y0=Q[k]['value'] / 100 if Q[k]['value'] > 1 else Q[k]['value'])['adv'] > 0 for s in s10]
st = M.starts(10, D, tbills=True)
out['ahead10']['tbills'] = [run(s, 10, tbills=True)['adv'] > 0 for s in s10] if st == s10 else None
# chuỗi tháng cho nhịp S06 (bản ghi thật): giá nhà (FHFA), tiền thuê (CPI rent), lãi 30 năm (trung bình tháng) — chuẩn hoá 1991-01 = 1
ms = sorted(m for m in hpi if m >= '1991-01' and m in cpi)
out['months'] = ms
out['hpi'] = [round(hpi[m] / hpi[ms[0]], 4) for m in ms]
out['rent'] = [round(cpi[m] / cpi[ms[0]], 4) for m in ms]
out['rate'] = [round(rate[m], 3) if m in rate else None for m in ms]
chk = [(len(s10), Q['n_10y']['value']), (len(s15), Q['n_15y']['value']), (sum(not a for a in out['ahead10']['5']), Q['n_renter_ahead_10y']['value'])]
for a, b in chk: assert a == b, chk
for y, k in (('4', 'share_yield4pct_10y'), ('6', 'share_yield6pct_10y'), ('5', 'share_buyer_ahead_10y')):
    sh = 100 * sum(out['ahead10'][y]) / len(s10); v = Q[k]['value']; v = v * 100 if v <= 1 else v
    assert abs(sh - v) < 0.06, (y, sh, v)
json.dump(out, open(os.path.join(HERE, 'data.json'), 'w'))
print('starts', len(s10), len(s5), len(s15), {k: sum(v) for k, v in out['ahead10'].items() if v}, 'ahead5', sum(out['ahead5']), 'ahead15', sum(out['ahead15']))
