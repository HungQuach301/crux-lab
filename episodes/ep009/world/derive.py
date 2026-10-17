"""Tập 9 · chuỗi số trên hình của các đoạn thế giới, dẫn xuất từ out/model.json + numbers.md (không sửa mô hình). Mẫu: episodes/ep008/world/derive.py.
    python3 episodes/ep009/world/derive.py → episodes/ep009/world/claims.json
display = đoạn NGUYÊN VẸN của cột "Hiển thị" (display_full) trong numbers.md — kiểm ở đây (không khớp → dừng). _geom = hằng hình học."""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); EP = os.path.dirname(HERE)
Q = json.load(open(os.path.join(EP, 'out/model.json')))['quantities']
rows = {}
for ln in open(os.path.join(EP, 'numbers.md'), encoding='utf-8'):
    m = re.match(r'^\| `([\w-]+)` \| ([^|]+) \| ([^|]+) \|', ln)
    if m: rows[m.group(1)] = (m.group(2).strip(), m.group(3).strip())
short = {'share_buyer_ahead_cash_10y': 'about 3 out of 4', 'share_buyer_ahead_stocks_10y': 'about half', 'share_buyer_ahead_lump_10y': 'about 2 in 3',
         'share_buyer_ahead_cash_15y': 'every one', 'share_buyer_ahead_stocks_15y': 'about 1 in 5', 'era_2002-2007_share_stocks': 'none of 72',
         'era_2002-2007_share_cash': '6 of 72', 'era_1990s_share_stocks': 'about 2 in 3', 'era_2009-2016_share_stocks': 'nearly 4 in 5',
         'stocks_growth_1991-01_10y': 'almost 5 times', 'n_pot_below_start_stocks_10y': '183 of 307', 'share_stocks_beat_house_10y': 'about 9 in 10',
         'flip_yield_stocks_10y': 'about 5.1%', 'yield_anchor_pct': '5 percent', 'stocks_growth_worst_10y': '0.77x', 'n_stocks_lost_buyer_ahead_10y': 'all 16 stay lit',
         'median_adv_stocks_10y': '$5,827 behind', 'owner_cost_pct': '2.5 percent a year'}
cl = {}
for k, (v, full) in rows.items():
    if k not in Q: continue
    d = short.get(k, re.sub(r'\s*\(.*\)$', '', full).strip())
    assert d in full, f'{k}: "{d}" không nằm trong "{full}"'
    cl[k] = {'value': Q[k]['value'], 'display': d, 'display_full': full}


def sub(k, of, d):
    assert d in rows[of][1], (k, d, rows[of][1]); cl[k] = {'value': Q[of]['value'], 'display': d, 'display_full': rows[of][1], 'of': of}


sub('share_buyer_ahead_stocks_10y_n', 'share_buyer_ahead_stocks_10y', '152 of 307')
sub('share_buyer_ahead_stocks_10y_pct', 'share_buyer_ahead_stocks_10y', '49.5%')
sub('share_buyer_ahead_cash_10y_pct', 'share_buyer_ahead_cash_10y', '75.6%')
sub('share_buyer_ahead_stocks_15y_pct', 'share_buyer_ahead_stocks_15y', '21.9%')
sub('share_buyer_ahead_lump_10y_pct', 'share_buyer_ahead_lump_10y', '63.8%')
sub('share_stocks_beat_house_10y_pct', 'share_stocks_beat_house_10y', '88.9%')
sub('era_1990s_share_stocks_pct', 'era_1990s_share_stocks', '67.6%')
sub('era_2009-2016_share_stocks_pct', 'era_2009-2016_share_stocks', '78.0%')
sub('stocks_growth_1991-01_10y_x', 'stocks_growth_1991-01_10y', '4.92x')
sub('yield_anchor_tag', 'yield_anchor_pct', '5')
# tham số / nhãn hình không có dòng numbers.md riêng
cl['yield5_tag'] = {'value': 5, 'display': '5%', 'display_full': 'rent tag 5% of the price a year (assumption, numbers.md yield_anchor_pct)', 'param': True}
cl['era_1990s_span'] = {'value': '1991-1999', 'display': '1990s', 'display_full': 'start months 1991 through 1999', 'param': True}
cl['era_2002-2007_span'] = {'value': '2002-2007', 'display': '2002 to 2007', 'display_full': 'start months 2002 through 2007', 'param': True}
cl['era_2009-2016_span'] = {'value': '2009-2016', 'display': '2009 to mid-2016', 'display_full': 'start months 2009 through July 2016', 'param': True}
cl['hold_15y'] = {'value': 15, 'display': '15 years', 'display_full': 'held fifteen years', 'param': True}
cl['hold_10y'] = {'value': 10, 'display': '10 years', 'display_full': 'held ten years', 'param': True}
cl['first_10y'] = {'value': '1991-01', 'display': 'January 1991', 'display_full': 'first start month January 1991', 'param': True}
cl['low_start'] = {'value': '2007-11', 'display': 'November 2007 start', 'display_full': 'start month of the lowest stock pot (world/data.json lowStart)', 'param': True}
for k, v in cl.items():
    if isinstance(v, dict) and '$' in str(v.get('display', '')) + str(v.get('display_full', '')):
        v['basis'] = 'nominal'
cl['_geom'] = {'n10': Q['n_10y']['value'], 'n15': Q['n_15y']['value'], 'n5': Q['n_5y']['value'], 'lit10': round(Q['share_buyer_ahead_stocks_10y']['value'] * Q['n_10y']['value'] / 100)}
json.dump(cl, open(os.path.join(HERE, 'claims.json'), 'w'), indent=1, ensure_ascii=False)
print(len(cl) - 1, 'claims')
