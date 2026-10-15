"""Tập 9: so result.json (kiểm độc lập headless Sonnet, chỉ đọc data/raw + định nghĩa) với out/model.json; và đối chiếu chuỗi tổng lợi nhuận
French (CRSP, mọi cổ phiếu Mỹ) với Shiller (S&P Composite giá + cổ tức/12) trên 1991-01..2023-08.  python3 episodes/ep009/model/independent/compare.py"""
import json, os, statistics as st, sys, xlrd
EP = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(EP, 'model')); import model as M
r = json.load(open(os.path.join(EP, 'model/independent/result.json')))
q = {k: v['value'] for k, v in json.load(open(os.path.join(EP, 'out/model.json')))['quantities'].items()}
pairs = [('n_windows_10y', 'n_10y'), ('last_start', 'last_10y')]
for md in ('cash', 'stocks', 'lump'):
    pairs += [('share_buyer_ahead_' + md, 'share_buyer_ahead_%s_10y' % md), ('renter_ahead_count_' + md, 'n_renter_ahead_%s_10y' % md),
              ('median_advantage_' + md, 'median_adv_%s_10y' % md)]
pairs += [('cash_ahead_stocks_not', 'n_flip_to_renter_10y'), ('windows_stocks_dollar_below_1', 'n_stocks_lost_10y'),
          ('share_stocks_y0_0.04', None), ('share_stocks_y0_0.06', None)]
rows, ok = [], 0
def cmp(a, b, name):
    global ok
    same = a == b; ok += same; rows.append('| %s | %s | %s | %s |' % (name, a, b, 'trùng' if same else '**LỆCH**'))
for a, b in pairs:
    if b: cmp(r[a], q[b], a)
cmp(r['stocks_min']['start'], q['worst_start_stocks_10y'], 'stocks_min.start'); cmp(r['stocks_min']['value'], q['worst_adv_stocks_10y'], 'stocks_min.value')
cmp(r['stocks_max']['start'], q['best_start_stocks_10y'], 'stocks_max.start'); cmp(r['stocks_max']['value'], q['best_adv_stocks_10y'], 'stocks_max.value')
cmp(r['h15']['n'], q['n_15y'], 'h15.n'); cmp(r['h15']['share_cash'], q['share_buyer_ahead_cash_15y'], 'h15.cash'); cmp(r['h15']['share_stocks'], q['share_buyer_ahead_stocks_15y'], 'h15.stocks')
for e, k in (('1991-01..1999-12', '1990s'), ('2002-01..2007-12', '2002-2007'), ('2009-01..2016-07', '2009-2016')):
    for md in ('cash', 'stocks'):
        cmp(r['eras'][e]['share_' + md], q['era_%s_share_%s' % (k, md)], 'era %s %s' % (k, md))
for s in ('2006-06', '2012-04', '1991-01'):
    for md in ('cash', 'stocks'):
        cmp(r['point_advantages'][s][md], q['adv_%s_%s_10y' % (s, md)], 'adv %s %s' % (s, md))
sw = {x['anchorYieldPct']: x['stocks'] for x in json.load(open(os.path.join(EP, 'out/model.json')))['sweep']}
cmp(r['share_stocks_y0_0.04'], sw[4.0], 'sweep 4% stocks'); cmp(r['share_stocks_y0_0.06'], sw[6.0], 'sweep 6% stocks')
# French vs Shiller
fr = M.french(); s = xlrd.open_workbook(os.path.join(EP, 'data/raw/ie_data.xls')).sheet_by_name('Data')
px, dv = {}, {}
for i in range(8, s.nrows):
    d = str(s.cell_value(i, 0))
    try: y, m = d.split('.'); key = '%s-%02d' % (y, int((m + '0')[:2]))
    except Exception: continue
    if isinstance(s.cell_value(i, 1), float): px[key] = s.cell_value(i, 1)
    if isinstance(s.cell_value(i, 2), float): dv[key] = s.cell_value(i, 2)
ms = sorted(k for k in fr if '1991-01' <= k <= '2023-05' and k in px and M.mo(k, 1) in px and k in dv)
sh = {k: (px[M.mo(k, 1)] + dv[k] / 12) / px[k] - 1 for k in ms}
gf = gs = 1.0
for k in ms: gf *= 1 + fr[k]; gs *= 1 + sh[k]
a, b = [fr[k] for k in ms], [sh[k] for k in ms]
ma, mb = st.mean(a), st.mean(b)
corr = sum((x - ma) * (y - mb) for x, y in zip(a, b)) / (sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b)) ** 0.5
cagr = lambda g: 100 * (g ** (12 / len(ms)) - 1)
txt = ['# Kiểm độc lập Tập 9 (Việc 0)', '',
       'Người kiểm: Claude Code headless **Sonnet** khoá Console (`briefs/independent.md`, log `logs/independent.jsonl`, $0,20), chỉ đọc `data/raw/*` + định nghĩa, viết `check.py` (thư viện chuẩn). Bash bị chặn trong lượt nên điều phối chạy `check.py` (không sửa).', '',
       '**%d/%d dòng trùng.**' % (ok, len(rows)), '', '| đại lượng | kiểm độc lập | model.json | |', '|---|---|---|---|'] + rows + ['',
       '## Đối chiếu nguồn cổ phiếu (B7: nguồn độc lập)', '',
       'French (CRSP, mọi cổ phiếu Mỹ, giá trị-trọng) vs Shiller (S&P Composite, giá trung bình tháng + cổ tức/12), %s..%s, %d tháng:' % (ms[0], ms[-1], len(ms)), '',
       '- tương quan lợi nhuận tháng **%.3f** (Shiller dùng giá trung bình tháng nên làm trơn — tương quan < 1 là đúng dạng);' % corr,
       '- $1 → **%.2f** (French) vs **%.2f** (Shiller); lãi kép năm %.2f %% vs %.2f %%.' % (gf, gs, cagr(gf), cagr(gs)),
       '- Kết luận: hai nguồn cùng bậc; lời chỉ dùng French (Shiller ở URL Yale dừng 2023-09).']
open(os.path.join(EP, 'model/independent/report.md'), 'w').write('\n'.join(txt) + '\n'); print('\n'.join(txt[-6:])); print(ok, len(rows))
