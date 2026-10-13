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
        'interest_30on15_now': '$210,691', 'interest_15_now': '$189,069', 'n_weeks': '1,833 weeks',
        # C4 lượt 2 (đoạn c–g): nhãn B11–B31; chữ thay cho phần trăm khi lời nói bằng chữ ("about 2 in 3 weeks", "fewer than 1 in 5 weeks",
        # "about 1 week in 5"), "about $8,200" = dạng làm tròn của chính cột Hiển thị
        'spread_min': '0.2 point', 'spread_max': '1.0 point', 'spread_mean': '0.57 point', 'share_spread_ge_050': 'about 2 in 3 weeks',
        'extra_total_min': '$6,097', 'extra_total_max': '$29,502', 'extra_total_median': '$16,631', 'share_extra_ge_now': 'fewer than 1 in 5 weeks',
        'era1991_median_extra_total': '$15,118', 'era1991_median_r30': '7.73%', 'era1991_median_spread': '0.46 point',
        'era2000_median_extra_total': '$14,210', 'era2000_median_r30': '6.18%', 'era2000_median_spread': '0.45 point',
        'era2010_median_extra_total': '$20,374', 'era2010_median_r30': '4.03%', 'era2010_median_spread': '0.72 point',
        'era2020_median_extra_total': '$21,345', 'era2020_median_spread': '0.70 point',
        'yearly_vs_monthly_interest': 'about $8,200', 'r30_max': '9.25%', 'r30_min': '2.65%', 'share_r30_ge_now': 'about 1 week in 5',
        'leo_r30': '2.65%', 'leo_extra_vs15_total': '$13,231', 'leo_extra_vs15_month': '$74 a month', 'leo_fallback_gap': 'about $793 a month'}
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
# C4 lượt 2: tháng/năm rút gọn trên hình (như first_week_short) — cùng tuần của claim gốc
SHORT = {'last_week_month': ('last_week', 'Oct 2026'), 'extra_total_min_week_short': ('extra_total_min_week', 'Dec 2008'),
         'extra_total_max_week_short': ('extra_total_max_week', 'Jan 2023'), 'r30_max_week_short': ('r30_max_week', 'Nov 1994'),
         'r30_min_week_short': ('r30_min_week', 'Jan 2021')}
MON = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()
for k, (of, d) in SHORT.items():
    y, m = Q[of]['value'][:4], int(Q[of]['value'][5:7])
    assert d == f'{MON[m - 1]} {y}', (k, d, Q[of]['value'])
    cl[k] = {'value': Q[of]['value'], 'display': d, 'display_full': rows[of], 'of': of}
# B16–B20: tên thập kỷ trên hình = khoảng tuần của từng era (out/model.json eras[].from/to; "1991 to 1999" vì thập kỷ đầu bắt đầu từ Aug 1991)
ER = model['eras']
for k, of, d, i in (('era1991_span', 'era1991_median_extra_total', '1991 to 1999', 0), ('era2000_name', 'era2000_median_extra_total', '2000s', 1),
                    ('era2010_name', 'era2010_median_extra_total', '2010s', 2), ('era2020_name', 'era2020_median_extra_total', '2020s', 3)):
    y0, y1 = int(ER[i]['from'][:4]), int(ER[i]['to'][:4])
    assert d == (f'{y0} to {y1}' if i == 0 else f'{y0}s') and (i == 0 or y0 % 10 == 0), (k, d, ER[i])
    cl[k] = {'value': y0, 'display': d, 'display_full': rows[of], 'of': of}
# B21 (C3 §3 #4, lệch làm tròn $2,216 + $733 = $2,949 ≠ $2,948): khoản trả thêm ghi "about $733" (làm tròn của 732,67) và KHÔNG viết thành phép
# cộng (không "+", không "="): "about $733 extra on top of the $2,216 required"
cl['extra_month_about'] = {'value': Q['extra_principal_needed_now']['value'], 'display': 'about $733', 'display_full': rows['extra_principal_needed_now'],
                           'of': 'extra_principal_needed_now'}
assert round(Q['extra_principal_needed_now']['value']) == 733
# B23 (C3 §3 #5, lệch 12 × $733 = $8,796 ≠ $8,792): khoản năm ghi kèm phép nhân CHƯA làm tròn "(12 × $732.67)" — giữ đúng claim yearly_lump
# ($8,792, numbers.md) thay vì "about $8,800" (một mức làm tròn mới không có trong numbers.md)
cl['yearly_lump_formula'] = {'value': Q['yearly_lump']['value'], 'display': '12 × $732.67', 'display_full': rows['yearly_lump'], 'of': 'yearly_lump'}
assert abs(12 * 732.67 - Q['yearly_lump']['value']) < 0.05 and abs(Q['extra_principal_needed_now']['value'] - 732.67) < 0.005

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
