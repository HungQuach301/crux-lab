"""Sinh numbers.md (claim ID = khoá `quantities` của out/model.json) — Tập 7.
    python3 episodes/ep007/model/numbers_md.py"""
import json, os
EP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Q = json.load(open(os.path.join(EP, 'out', 'model.json')))['quantities']
SRC = 'data/normalized/pmms_weekly.csv'
DISP = {  # hiển thị an toàn (kiểm độc lập: hiệu/tích tính từ số chưa làm tròn → hiển thị đô la nguyên)
 'n_weeks': ('1,833 weeks', 'history'), 'first_week': ('August 1991', 'history'), 'last_week': ('the week of October 8, 2026', 'present fact'),
 'r30_now': ('7.40%', 'present fact'), 'r15_now': ('6.73%', 'present fact'), 'spread_now': ('0.67 point', 'present fact'),
 'pay15_now': ('$2,828 a month', 'present fact; ILLUSTRATIVE loan'), 'pay30_now': ('$2,216 a month', 'present fact; ILLUSTRATIVE loan'),
 'pay30on15_now': ('$2,948 a month', 'present fact; ILLUSTRATIVE loan'), 'extra_vs15_month_now': ('$120 a month', 'present fact'),
 'extra_vs15_total_now': ('$21,622 (about $21,600)', 'present fact'), 'fallback_gap_now': ('about $613 a month', 'present fact'),
 'extra_principal_needed_now': ('$733 a month', 'present fact'), 'months_at_pay15_now': ('about 195 months (16 years and 3 months)', 'present fact'),
 'months_late_at_pay15_now': ('about 15 months late', 'present fact'), 'interest_15_now': ('$189,069 (about $189,000)', 'present fact'),
 'interest_30on15_now': ('$210,691 (about $211,000)', 'present fact'), 'interest_30full_now': ('$477,622 (about $478,000)', 'present fact'),
 'spread_mean': ('0.57 point', 'history'), 'spread_min': ('0.2 point', 'history'), 'spread_max': ('1.0 point', 'history'),
 'share_spread_ge_050': ('63% (about 2 in 3 weeks)', 'history'), 'extra_total_median': ('$16,631 (about $16,600)', 'history'),
 'extra_total_min': ('$6,097 (about $6,100)', 'history'), 'extra_total_min_week': ('December 2008', 'history'),
 'extra_total_max': ('$29,502 (about $29,500)', 'history'), 'extra_total_max_week': ('January 2023', 'history'),
 'share_extra_ge_now': ('18.7% (fewer than 1 in 5 weeks)', 'history'), 'bar_now': ('7.40% a year, before taxes', 'present fact; rule'),
 'r30_min': ('2.65%', 'history'), 'r30_min_week': ('January 2021', 'history'), 'r30_max': ('9.25%', 'history'), 'r30_max_week': ('November 1994', 'history'),
 'share_r30_ge_now': ('19% (about 1 week in 5)', 'history'), 'leo_r30': ('2.65%', 'history; ILLUSTRATIVE (Leo)'), 'leo_r15': ('2.16%', 'history; ILLUSTRATIVE (Leo)'),
 'leo_extra_vs15_total': ('$13,231 (about $13,200)', 'history; ILLUSTRATIVE (Leo)'), 'leo_extra_vs15_month': ('$74 a month', 'history; ILLUSTRATIVE (Leo)'),
 'leo_fallback_gap': ('about $793 a month', 'history; ILLUSTRATIVE (Leo)'),
 'era1991_median_extra_total': ('$15,118 (about $15,100)', 'history'), 'era1991_median_r30': ('7.73%', 'history'), 'era1991_median_spread': ('0.46 point', 'history'),
 'era2000_median_extra_total': ('$14,210 (about $14,200)', 'history'), 'era2000_median_r30': ('6.18%', 'history'), 'era2000_median_spread': ('0.45 point', 'history'),
 'era2010_median_extra_total': ('$20,374 (about $20,400)', 'history'), 'era2010_median_r30': ('4.03%', 'history'), 'era2010_median_spread': ('0.72 point', 'history'),
 'era2020_median_extra_total': ('$21,345 (about $21,300)', 'history'), 'era2020_median_r30': ('about 6.3%', 'history (median 6.275: show one decimal)'), 'era2020_median_spread': ('0.70 point', 'history'),
 'monthly_extra_months': ('180 months (15 years)', 'present fact; rule'), 'monthly_extra_interest': ('$210,691', 'present fact'),
 'yearly_lump': ('$8,792 once a year', 'present fact'), 'yearly_lump_months': ('184 months (4 months later)', 'present fact'),
 'yearly_lump_interest': ('$218,857 (about $218,900)', 'present fact'), 'yearly_vs_monthly_interest': ('$8,166 (about $8,200)', 'present fact'),
}
print('| Claim ID | Giá trị | Hiển thị | Định nghĩa | Nguồn | Ghi chú |\n|---|---|---|---|---|---|')
for k, v in Q.items():
    d, note = DISP[k]
    print(f"| `{k}` | {v['value']} | {d} | {v['definition'].split('principal and interest only. ')[-1]} | {SRC} | {note} |")
