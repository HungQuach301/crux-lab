"""Tập 7 · dữ liệu hình cho các đoạn thế giới 3D (C3), dẫn xuất từ out/model.json + numbers.md của tập (không sửa mô hình).
  python3 episodes/ep007/world/derive.py → episodes/ep007/world/claims.json
claims.json = claim hiển thị {value, display, display_full}: value chép từ out/model.json; display = chuỗi đúng như trên hình, luôn là một
đoạn NGUYÊN VẸN của cột "Hiển thị" (display_full) trong numbers.md — kiểm ở đây (thiếu/không khớp → dừng).
Ngoại lệ có ghi: `principal` = params.principal của model.json ($320,000, khoản vay minh hoạ; không có dòng claim riêng trong numbers.md).
Kiểm chéo số học: tổng chồng = 15 bó năm (bundle = extra_vs15_total_now / 15 ≈ 12 × $120), tháng trễ = 195 − 180, 184 − 180 = 4."""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); EP = os.path.dirname(HERE)
model = json.load(open(os.path.join(EP, 'out/model.json'))); Q = model['quantities']
rows = {}
for ln in open(os.path.join(EP, 'numbers.md'), encoding='utf-8'):
    m = re.match(r'^\| `(\w+)` \| ([^|]+) \| ([^|]+) \|', ln)
    if m: rows[m.group(1)] = m.group(3).strip()

# chuỗi hiển thị trên hình (mỗi chuỗi là đoạn nguyên vẹn của cột Hiển thị); mọi số trên hình đi qua đây
disp = {'extra_vs15_month_now': '$120 a month', 'extra_vs15_total_now': '$21,622', 'pay30on15_now': '$2,948 a month', 'pay15_now': '$2,828',
        'last_week': 'October 8, 2026', 'months_at_pay15_now': 'about 195 months', 'months_late_at_pay15_now': 'about 15 months late',
        'extra_principal_needed_now': '$733 a month', 'monthly_extra_months': '180 months', 'yearly_lump': '$8,792 once a year',
        'yearly_lump_months': '184 months', 'bar_now': '7.40% a year, before taxes', 'r30_now': '7.40%', 'pay30_now': '$2,216 a month',
        # C4 (đoạn a, b): nhãn B03–B09
        'r15_now': '6.73%', 'spread_now': '0.67 point', 'fallback_gap_now': 'about $613 a month', 'interest_30full_now': '$477,622',
        'interest_30on15_now': '$210,691', 'interest_15_now': '$189,069', 'n_weeks': '1,833 weeks'}
cl = {}
for k, d in disp.items():
    full = rows[k]
    assert d in full, f'{k}: "{d}" không nằm trong cột Hiển thị "{full}"'
    cl[k] = {'value': Q[k]['value'], 'display': d, 'display_full': full}
# hiển thị rút gọn của ngày (nhãn ≤ ~8 từ): "Oct 8, 2026" — cùng ngày last_week; ghi riêng để trang kiểm khớp chuỗi trên hình
assert Q['last_week']['value'] == '2026-10-08'
cl['last_week_short'] = {'value': '2026-10-08', 'display': 'Oct 8, 2026', 'display_full': rows['last_week'], 'of': 'last_week'}
cl['yearly_lump_late'] = {'value': Q['yearly_lump_months']['value'] - 180, 'display': '4 months later', 'display_full': rows['yearly_lump_months'], 'of': 'yearly_lump_months'}
assert '4 months later' in rows['yearly_lump_months'] and Q['yearly_lump_months']['value'] - 180 == 4
# s06 (vòng 2): khoản 15 năm ghi kèm "a month" cạnh vạch mức 15 năm — cùng claim pay15_now, chuỗi = cả cột Hiển thị
cl['pay15_month'] = {'value': Q['pay15_now']['value'], 'display': '$2,828 a month', 'display_full': rows['pay15_now'], 'of': 'pay15_now'}
assert cl['pay15_month']['display'] in rows['pay15_now']
# s21 (vòng 3): "to finish in 180 months: $2,216 required + $733 a month" — khoản bắt buộc không kèm "a month" (đoạn nguyên vẹn của Hiển thị)
cl['pay30_amt'] = {'value': Q['pay30_now']['value'], 'display': '$2,216', 'display_full': rows['pay30_now'], 'of': 'pay30_now'}
assert cl['pay30_amt']['display'] in rows['pay30_now']
cl['principal'] = {'value': model['params']['principal'], 'display': '$320,000', 'display_full': '$320,000 (params.principal; ILLUSTRATIVE loan)'}
assert model['params']['principal'] == 320000
# C4 (B02): "every week since Aug 1991" — cùng tuần first_week, dạng tháng rút gọn như last_week_short
assert Q['first_week']['value'] == '1991-08-30'
cl['first_week_short'] = {'value': '1991-08-30', 'display': 'Aug 1991', 'display_full': rows['first_week'], 'of': 'first_week'}
# C4: kỳ hạn hai khoản vay trên hình (thẻ hai khoản B02, nhãn thanh B04–B09) = params.termShort / termLong (tháng) ÷ 12 — chữ số trên hình nào
# cũng qua claim; "in 15" = trả xong trong 15 năm (monthly_extra_months = 180 tháng)
P = model['params']
assert P['termShort'] == 180 and P['termLong'] == 360 and Q['monthly_extra_months']['value'] == 180
cl['term_short'] = {'value': P['termShort'] / 12, 'display': '15-year', 'display_full': '15-year (params.termShort = 180 months)', 'of': 'params.termShort'}
cl['term_long'] = {'value': P['termLong'] / 12, 'display': '30-year', 'display_full': '30-year (params.termLong = 360 months)', 'of': 'params.termLong'}
cl['term_short_years'] = {'value': P['termShort'] / 12, 'display': '15 years', 'display_full': rows['monthly_extra_months'], 'of': 'monthly_extra_months'}
cl['paid_in_short'] = {'value': P['termShort'] / 12, 'display': 'in 15', 'display_full': '30-year paid in 15 (monthly_extra_months = 180 months)', 'of': 'monthly_extra_months'}
assert '15 years' in rows['monthly_extra_months']

# kiểm chéo dùng cho hình
v = lambda k: Q[k]['value']
assert abs(v('months_at_pay15_now') - 180 - v('months_late_at_pay15_now')) < 0.05
assert v('monthly_extra_months') == 180 and round(v('extra_vs15_month_now')) == 120
assert abs(v('extra_vs15_month_now') * 180 - v('extra_vs15_total_now')) < 1
geom = {'bundle_usd': round(v('extra_vs15_total_now') / 15, 2), 'late_months': round(v('months_late_at_pay15_now'), 1),
        'lump_late_months': v('yearly_lump_months') - 180, 'pay15': v('pay15_now'), 'pay30': v('pay30_now'), 'pay30on15': v('pay30on15_now'),
        'stack_total': v('extra_vs15_total_now'), 'bar': v('bar_now')}
cl['_geom'] = geom
json.dump(cl, open(os.path.join(HERE, 'claims.json'), 'w'), indent=1, ensure_ascii=False)
print('claims', len(cl) - 1, 'geom', geom)
