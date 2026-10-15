"""Tập 9 · dữ liệu hình cho các đoạn thế giới (một hàng mỗi tháng bắt đầu), dẫn xuất từ model/model.py (cùng định nghĩa với out/model.json).
    python3 episodes/ep009/world/data.py → episodes/ep009/world/data.json
starts10 (307 tháng, Jan 1991 → Jul 2016): ahead10[mode] (người mua hơn sau 10 năm; mode = cash · stocks · lump · fee), ahead10y[y] (quỹ cổ phiếu,
thẻ thuê y % — S22), adv10 / low10 (quỹ cổ phiếu thấp nhất trong cửa sổ), gS / gH (tăng trưởng 10 năm của $1 cổ phiếu / chỉ số giá nhà — B01);
starts5 / ahead5s; starts15 / ahead15s / ahead15c; traj[s] = chuỗi tháng (121 điểm) quỹ cổ phiếu, quỹ tiền mặt, vốn người mua (sau phí bán) cho
các tháng dùng trên hình. Kiểm chéo với out/model.json (số đếm, tỉ lệ) — lệch → dừng."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); EP = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(EP, 'model')); sys.dont_write_bytecode = True
import model as M  # noqa: E402
Q = json.load(open(os.path.join(EP, 'out', 'model.json')))['quantities']
D = M.load(); hpi, cpi, rate, stk = D
s10, s5, s15 = M.starts(10, D), M.starts(5, D), M.starts(15, D)
run = lambda s, H, md='cash', y0=M.Y0: M.run(s, H, D, md, y0)
r10 = {md: [run(s, 10, md) for s in s10] for md in ('cash', 'stocks', 'lump', 'stocks_fee')}


def traj(s, H=10, y0=M.Y0):
    """Chuỗi tháng của run() (cùng công thức): quỹ cổ phiếu, quỹ tiền mặt, vốn người mua sau phí bán — kiểm điểm cuối = run()."""
    r = rate[s] / 1200; loan = M.P * (1 - M.DOWN); pay = loan * r / (1 - (1 + r) ** -M.N)
    y = y0 * (cpi[s] / hpi[s]) / (cpi[M.ANCHOR] / hpi[M.ANCHOR]); rent0 = y * M.P / 12
    ps = pc = M.P * (M.DOWN + M.CLOSE); bal = loan; o = {'stocks': [round(ps)], 'cash': [round(pc)], 'eq': [round((1 - M.SELL) * M.P - bal)]}
    for k in range(12 * H):
        m = M.mo(s, k)
        diff = pay + M.OWN / 12 * M.P * hpi[m] / hpi[s] - rent0 * cpi[m] / cpi[s]
        ps = (ps + diff) * (1 + stk[m]); pc += diff; bal = bal * (1 + r) - pay
        e = M.mo(s, k + 1)
        o['stocks'].append(round(ps)); o['cash'].append(round(pc)); o['eq'].append(round((1 - M.SELL) * M.P * hpi[e] / hpi[s] - bal))
    a, b = run(s, H, 'stocks'), run(s, H, 'cash')
    assert abs(o['stocks'][-1] - a['pot']) < 2 and abs(o['cash'][-1] - b['pot']) < 2 and abs(o['eq'][-1] - a['eq']) < 2, s
    return o


low = [x['low'] for x in r10['stocks']]
iLow = min(range(len(s10)), key=lambda i: low[i])
YS = [4.0, 4.5, 4.83, 5.0, 5.06, 5.5, 5.59, 6.0]
out = {'starts10': s10, 'starts5': s5, 'starts15': s15,
       'ahead10': {k: [x['adv'] > 0 for x in r10[md]] for k, md in (('cash', 'cash'), ('stocks', 'stocks'), ('lump', 'lump'), ('fee', 'stocks_fee'))},
       'ahead10y': {str(y): [run(s, 10, 'stocks', y / 100)['adv'] > 0 for s in s10] for y in YS},
       'adv10': [round(x['adv']) for x in r10['stocks']], 'adv10c': [round(x['adv']) for x in r10['cash']],
       'low10': [round(v) for v in low], 'below10': [v < M.P * (M.DOWN + M.CLOSE) for v in low],
       'gS': [round(M.growth(s, 10, stk), 3) for s in s10], 'gH': [round(hpi[M.mo(s, 120)] / hpi[s], 3) for s in s10],
       'ahead5s': [run(s, 5, 'stocks')['adv'] > 0 for s in s5],
       'ahead15s': [run(s, 15, 'stocks')['adv'] > 0 for s in s15], 'ahead15c': [run(s, 15, 'cash')['adv'] > 0 for s in s15],
       'lowStart': s10[iLow], 'traj': {s: traj(s) for s in ('1991-01', '2006-06', '2012-04', s10[iLow], '1999-03')}}
g = [1.0]
for k in range(120):
    g.append(g[-1] * (1 + stk[M.mo('1991-01', k)]))
out['g1991'] = [round(v, 4) for v in g]   # $1 trong cổ phiếu từ 1991-01, theo tháng (S05.1, S06.1)
out['traj'][s10[iLow]]['lowIdx'] = min(range(121), key=lambda k: out['traj'][s10[iLow]]['stocks'][k])
pct = lambda a: round(100 * sum(a) / len(a), 1)
chk = [(len(s10), Q['n_10y']['value']), (len(s15), Q['n_15y']['value']), (len(s5), Q['n_5y']['value']),
       (pct(out['ahead10']['cash']), Q['share_buyer_ahead_cash_10y']['value']), (pct(out['ahead10']['stocks']), Q['share_buyer_ahead_stocks_10y']['value']),
       (pct(out['ahead10']['lump']), Q['share_buyer_ahead_lump_10y']['value']), (pct(out['ahead10']['fee']), Q['share_buyer_ahead_stocks_fee_10y']['value']),
       (pct(out['ahead5s']), Q['share_buyer_ahead_stocks_5y']['value']), (pct(out['ahead15s']), Q['share_buyer_ahead_stocks_15y']['value']),
       (pct(out['ahead15c']), Q['share_buyer_ahead_cash_15y']['value']), (sum(out['below10']), Q['n_pot_below_start_stocks_10y']['value']),
       (round(low[iLow]), Q['min_pot_stocks_10y']['value']), (pct([a > b for a, b in zip(out['gS'], out['gH'])]), Q['share_stocks_beat_house_10y']['value']),
       (pct(out['ahead10y']['4.83']), Q['share_hvs_2025Q4_stocks_10y']['value']), (pct(out['ahead10y']['5.59']), Q['share_hvs_2026Q1_stocks_10y']['value'])]
for a, b in chk:
    assert abs(a - b) < 0.11, chk
json.dump(out, open(os.path.join(HERE, 'data.json'), 'w'))
print('starts', len(s10), len(s5), len(s15), 'lit', {k: sum(v) for k, v in out['ahead10'].items()}, 'low', out['lowStart'], low[iLow],
      'tag', {k: sum(v) for k, v in out['ahead10y'].items()})
