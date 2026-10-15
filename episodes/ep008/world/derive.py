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
short = {'share_buyer_ahead_10y': 'about 3 out of 4', 'median_adv_10y': 'about $157,000', 'best_adv_10y': 'about $484,000', 'worst_adv_10y': '$82,385 behind',
         'share_tbills_10y': 'about 2 out of 3', 'best_price_change_10y': 'more than doubled', 'rate_latest': '6.86%', 'yield_anchor_pct': '5% a year',
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
# M6 checks S07 (14/10): nhãn trên hình cần một khoảng claim nguyên vẹn
sub('today_buyer_month1_usd', 'today_buyer_month1', '$2,933')
sub('today_rent_month1_usd', 'today_rent_month1', '$1,667')
sub('share_tbills_10y_pct', 'share_tbills_10y', '66.4%')
sub('share_15y_pct', 'share_buyer_ahead_15y', '100%')
sub('worst_adv_10y_short', 'worst_adv_10y', 'about $82,000')
for k in ('sell_pct', 'down_pct', 'closing_pct', 'owner_cost_pct'):
    if k in rows and k not in cl:
        cl[k] = {'value': float(rows[k][0]), 'display': rows[k][1].split(' of')[0], 'display_full': rows[k][1], 'param': True}
for y in (4, 5, 6):   # chữ trên thẻ / nhãn thẻ tiền thuê ở đồ thị (giả định, numbers.md: định nghĩa của share_yield4pct_10y / yield_anchor_pct / share_yield6pct_10y)
    cl[f'yield{y}_tag'] = {'value': y, 'display': f'{y}%', 'display_full': f'anchor yield {y}% (assumption)', 'param': True}
# M5 checks S07 (14/10): số nói ra là tham số/khoảng của mô hình, chưa có claim
cl['term_30y'] = {'value': 30, 'display': '30-year', 'display_full': '30-year fixed mortgage (assumption, numbers.md)', 'param': True}
cl['era_2002-2007_span'] = {'value': '2002-2007', 'display': '2002 to 2007', 'display_full': 'start months 2002 through 2007', 'param': True}
cl['hold_15y'] = {'value': 15, 'display': '15 years', 'display_full': 'held fifteen years', 'param': True}
# G2 câu 6 (S09): mọi số $ là đô la danh nghĩa (mô hình không hiệu chỉnh lạm phát)
for k, v in cl.items():
    if isinstance(v, dict) and '$' in str(v.get('display', '')) + str(v.get('display_full', '')):
        v['basis'] = 'nominal'
cl['_geom'] = {'n10': Q['n_10y']['value'], 'n15': Q['n_15y']['value'], 'renter10': Q['n_renter_ahead_10y']['value']}
json.dump(cl, open(os.path.join(HERE, 'claims.json'), 'w'), indent=1, ensure_ascii=False)
print(len(cl) - 1, 'claims')
