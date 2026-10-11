"""Sinh bảng claim của numbers.md từ out/model.json (claim ID = khoá `rounded`, hoặc khoá suy ra ghi rõ định nghĩa).
    python3 episodes/ep006/model/numbers_md.py > /tmp/rows.md"""
import json, os
EP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M = json.load(open(os.path.join(EP, 'out', 'model.json')))
R, raw = M['rounded'], M['raw']
SRC = 'data/raw/CPIAUCNS.csv'
W20 = '20-year window = start month s ≥ 1947-01, end e = s + 240 months, both CPIAUCNS values present (2025-10 blank → start 2005-10 skipped); P = CPI(e)/CPI(s)'
rows = [
 ('cpi_yoy_latest_pct', R['cpi_yoy_latest_pct'], '3.4%', 'CPI-U Aug 2026 / Aug 2025 − 1 (latest 12 months)', SRC, 'present fact'),
 ('index_last_month', R['index_last_month'], 'August 2026', 'last CPIAUCNS observation (Sept 2026 CPI not released on 2026-10-08)', SRC, ''),
 ('windows_20y', R['windows_20y'], '715 stretches', W20 + '; starts 1947-01..2006-08', SRC, 'history'),
 ('windows_2pct_kept_up_20y', R['windows_2pct_kept_up_20y'], '17', 'count of 20-year windows with 1.02^20 ≥ P; all start 1947-09..1949-01', SRC, 'history'),
 ('share_2pct_kept_up_20y_pct', R['share_2pct_kept_up_20y_pct'], '2.4%', '100 × kept / 715 (17 in 715 ≈ 1 in 42)', SRC, 'history'),
 ('kept_up_first_start_20y', R['kept_up_first_start_20y'], 'September 1947', 'first start month of a kept-up window', SRC, 'history'),
 ('kept_up_last_start_20y', R['kept_up_last_start_20y'], 'January 1949', 'last start month of a kept-up window (none since)', SRC, 'history'),
 ('windows_25y', R['windows_25y'], '655', '25-year windows (end s + 300), starts 1947-01..2001-08', SRC, 'history'),
 ('windows_2pct_kept_up_25y', R['windows_2pct_kept_up_25y'], '0 of 655', 'count with 1.02^25 ≥ P (25-year)', SRC, 'history'),
 ('median_inflation_20y_pct_per_year', R['median_inflation_20y_pct_per_year'], '3.1% a year', 'median over 20-year windows of 100(P^(1/20) − 1)', SRC, 'history; not an expectation'),
 ('median_real_value_2pct_payment_after_20y_pct', R['median_real_value_2pct_payment_after_20y_pct'], '80.7% (about 4/5; about 8 of 10 crates)', 'median of 100 × 1.02^20 / P', SRC, 'history'),
 ('median_real_value_level_payment_after_20y_pct', R['median_real_value_level_payment_after_20y_pct'], '54.3% (about half)', 'median of 100 / P', SRC, 'history'),
 ('worst_real_value_2pct_payment_after_20y_pct', R['worst_real_value_2pct_payment_after_20y_pct'], '43.1%', 'min of 100 × 1.02^20 / P (window starting 1966-01)', SRC, 'history'),
 ('worst_real_value_level_payment_after_20y_pct', R['worst_real_value_level_payment_after_20y_pct'], '29.0%', 'level check in the same worst window (1966-01 → 1986-01)', SRC, 'history'),
 ('worst_window_start_year_20y', R['worst_window_start_year_20y'], '1966 (January)', 'start of the worst window for the 2% check', SRC, 'history'),
 ('worst_window_years_2pct_fell_20y', R['worst_window_years_2pct_fell_20y'], 'every one of 20 anniversaries (crates: 10 → about 4)', "Carl's window (Jan 1966 → Jan 1986): count of anniversaries k=1..20 where 100 × 1.02^k / (CPI(s+12k)/CPI(s)) is below its value at k−1; crate row = round(10 × value / 100): 10 at the start, about 4 at year 20 (43.1%)", SRC, 'ILLUSTRATIVE (Carl); history'),
 ('share_2pct_at_least_90_after_20y_pct', R['share_2pct_at_least_90_after_20y_pct'], '32.6% (about 1 in 3)', '% of 20-year windows with 2% check ≥ 90% of start', SRC, 'history'),
 ('share_2pct_at_least_75_after_20y_pct', R['share_2pct_at_least_75_after_20y_pct'], '56.2%', '% of windows with 2% check ≥ 75%', SRC, 'history'),
 ('two_pct_growth_20y_pct', R['two_pct_growth_20y_pct'], '48.6% (about half)', '100(1.02^20 − 1): how much 20 raises of 2% grow a check', 'arithmetic', 'rule'),
 ('latest_start / latest_end', f"{R['latest_start']} / {R['latest_end']}", 'Aug 2006 → Aug 2026', 'most recent complete 20-year window', SRC, 'history'),
 ('latest_window_real_value_2pct_payment_pct', R['latest_window_real_value_2pct_payment_pct'], '90.4% (about 9 in 10)', '100 × 1.02^20 / P(2006-08 → 2026-08)', SRC, 'history'),
 ('latest_window_real_value_level_payment_pct', R['latest_window_real_value_level_payment_pct'], '60.9% (about 6 in 10)', '100 / P, same window', SRC, 'history'),
 ('latest_window_price_rise_pct', R['latest_window_price_rise_pct'], '64.3%', '100(P − 1), Aug 2006 → Aug 2026', SRC, 'history'),
 ('latest_window_inflation_pct_per_year', R['latest_window_inflation_pct_per_year'], '2.51% a year', '100(P^(1/20) − 1), Aug 2006 → Aug 2026', SRC, 'history'),
 ('guide_start', R['guide_start'], 'August 2006, age 65', 'ILLUSTRATIVE guide character: first check Aug 2006 at 65 (= latest window)', SRC, 'ILLUSTRATIVE'),
 ('guide_last_year_2pct_at_or_above_100', R['guide_last_year_2pct_at_or_above_100'], '15 years (Aug 2021, age 80)', 'last anniversary k with 100 × 1.02^k / (CPI(s+12k)/CPI(s)) ≥ 100; values at k=15: ' + f"{raw['guide_path'][15]['real_2pct_pct']:.1f}%", SRC, 'ILLUSTRATIVE; history'),
 ('guide_years_2pct_at_or_above_100', R['guide_years_2pct_at_or_above_100'], '12 of the first 15 anniversaries', 'anniversaries k=1..20 with 2% check ≥ 100% (k=1,3,4,7,8,9,10..15; below at 2,5,6)', SRC, 'ILLUSTRATIVE; history'),
 ('guide_real_2pct_2022_pct', round(raw['guide_path'][16]['real_2pct_pct'], 1), '94.5% (Aug 2022, age 81)', '2% check at k=16 (one year after 100.3%)', SRC, 'ILLUSTRATIVE; history'),
 ('guide_real_level_2021_pct', round(raw['guide_path'][15]['real_level_pct'], 1), '74.5% (Aug 2021)', 'level check at k=15', SRC, 'ILLUSTRATIVE; history'),
 ('guide_real_2pct_end_pct', R['guide_real_2pct_end_pct'], '90.4% (Aug 2026, age 85)', '= latest_window_real_value_2pct_payment_pct', SRC, 'ILLUSTRATIVE; history'),
 ('guide_real_level_end_pct', R['guide_real_level_end_pct'], '60.9%', '= latest_window_real_value_level_payment_pct', SRC, 'ILLUSTRATIVE; history'),
 ('guide_year_level_reaches_2pct_end', R['guide_year_level_reaches_2pct_end'], 'year 5 (Aug 2011, 90.0%)', 'first anniversary where her level check ≤ her 2% check\'s 20-year end value (90.4%)', SRC, 'ILLUSTRATIVE; history'),
 ('median_year_level_reaches_2pct_end_median', R['median_year_level_reaches_2pct_end_median'], 'about year 8', 'median over windows of first anniversary k where 100/(CPI(s+12k)/CPI(s)) ≤ 80.7', SRC, 'history'),
 ('by_decade_1990_median_real_2pct', round(raw['by_decade']['1990']['median_real_2pct_pct'], 1), '94.8%', 'median 2% check after 20 years, starts 1990-01..1999-12 (0 of 120 kept up)', SRC, 'history'),
 ('by_decade_2000_kept', raw['by_decade']['2000']['kept'], '0 of 79', 'starts 2000-01..2006-08 that kept up (best 99.5%)', SRC, 'history'),
 ('by_decade_2000_max_real_2pct', round(raw['by_decade']['2000']['max_real_2pct_pct'], 1), '99.5%', 'best 2% check after 20 years among 2000s starts', SRC, 'history'),
 ('by_decade_1960_median_real_2pct', round(raw['by_decade']['1960']['median_real_2pct_pct'], 1), '44.3%', 'median, starts in the 1960s', SRC, 'history'),
 ('raise_needed_half_20y_pct', R['raise_needed_half_20y_pct'], '3.1% a year', 'fixed yearly raise that kept up in half the 20-year windows (= median inflation)', SRC, 'history; not advice'),
 ('raise_needed_all_20y_pct', R['raise_needed_all_20y_pct'], '6.38% a year', 'raise that kept up in every 20-year window (= max annualized inflation, window starting 1966-01)', SRC, 'history; not advice'),
 ('raise_grid_3pct', round(raw['raise_grid']['0.030'], 1), '42.4%', '% of 20-year windows a 3% yearly raise kept up with', SRC, 'history; not advice'),
 ('robust_cpiw_share_kept_up_20y_pct', R['robust_cpiw_share_kept_up_20y_pct'], '2.9% (21 of 715)', 'same test on CPI-W (CWUR0000SA0, index for Social Security COLAs)', 'data/raw/CWUR0000SA0.csv', 'history; robustness'),
 ('robust_pce_share_kept_up_20y_pct', R['robust_pce_share_kept_up_20y_pct'], '19.2% (110 of 572)', 'same test on the PCE price index (from 1959; starts 1959-01..2006-08)', 'data/raw/PCEPI.csv', 'history; robustness'),
 ('cpiu_from_pce_start_kept_up_20y', R['cpiu_from_pce_start_kept_up_20y'], '0 of 571', 'CPI-U windows starting 1959-01 or later that kept up', SRC, 'history; robustness'),
 ('robust_pce_median_real_2pct_pct', R['robust_pce_median_real_2pct_pct'], '88.0%', 'median 2% check after 20 years on PCE', 'data/raw/PCEPI.csv', 'history; robustness'),
]
print('| Claim ID | Giá trị | Hiển thị | Định nghĩa | Nguồn | Ghi chú |\n|---|---|---|---|---|---|')
for r in rows:
    print('| `%s` | %s | %s | %s | %s | %s |' % r)
