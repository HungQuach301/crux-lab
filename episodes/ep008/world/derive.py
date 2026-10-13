"""Tập 8 · chuỗi số trên hình của các đoạn thế giới, dẫn xuất từ out/model.json + numbers.md (không sửa mô hình).
    python3 episodes/ep008/world/derive.py → episodes/ep008/world/claims.json
display = đoạn NGUYÊN VẸN của cột "Hiển thị" (display_full) trong numbers.md — kiểm ở đây (không khớp → dừng). _geom = hằng hình học."""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); EP = os.path.dirname(HERE)
Q = json.load(open(os.path.join(EP, 'out/model.json')))['quantities']
rows = {}
for ln in open(os.path.join(EP, 'numbers.md'), encoding='utf-8'):
    m = re.match(r'^\| `([\w-]+)` \| ([^|]+) \| ([^|]+) \|', ln)
    if m: rows[m.group(1)] = (m.group(2).strip(), m.group(3).strip())
short = {'share_buyer_ahead_10y': 'about 3 in 4', 'median_adv_10y': 'about $157,000', 'best_adv_10y': 'about $484,000', 'worst_adv_10y': '$82,385 behind',
         'share_tbills_10y': 'about 2 in 3', 'best_price_change_10y': 'more than doubled', 'rate_latest': '6.86%', 'yield_anchor_pct': '5% a year',
         'owner_cost_pct': '2.5 percent', 'era_2002-2007_share': '6 of 72', 'share_buyer_ahead_15y': 'every one'}
cl = {}
for k, (v, full) in rows.items():
    if k not in Q: continue
    d = short.get(k, re.sub(r'\s*\(.*\)$', '', full).strip())
    assert d in full, f'{k}: "{d}" không nằm trong "{full}"'
    cl[k] = {'value': Q[k]['value'], 'display': d, 'display_full': full}
# claim phụ: dạng khác của cùng một số (đoạn nguyên vẹn của Hiển thị)
def sub(k, of, d):
    assert d in rows[of][1], (k, d, rows[of][1]); cl[k] = {'value': Q[of]['value'], 'display': d, 'display_full': rows[of][1], 'of': of}
sub('share_buyer_ahead_10y_pct', 'share_buyer_ahead_10y', '75.6%')
sub('era_2002-2007_pct', 'era_2002-2007_share', '8.3%')
sub('share_tbills_10y_pct', 'share_tbills_10y', '66.4%')
sub('share_15y_pct', 'share_buyer_ahead_15y', '100%')
sub('worst_adv_10y_short', 'worst_adv_10y', 'about $82,000')
for k in ('sell_pct', 'down_pct', 'closing_pct', 'owner_cost_pct'):
    if k in rows and k not in cl:
        cl[k] = {'value': float(rows[k][0]), 'display': rows[k][1].split(' of')[0], 'display_full': rows[k][1], 'param': True}
cl['_geom'] = {'n10': Q['n_10y']['value'], 'n15': Q['n_15y']['value'], 'renter10': Q['n_renter_ahead_10y']['value']}
json.dump(cl, open(os.path.join(HERE, 'claims.json'), 'w'), indent=1, ensure_ascii=False)
print(len(cl) - 1, 'claims')
