# Claim — Tập 6 (Việc 0; claim ID = khoá của `out/model.json` → `rounded`, hoặc khoá suy ra ghi rõ định nghĩa)

Dữ liệu (FRED, tải 2026-10-08, `data/fetch.py`; không commit): CPIAUCNS (CPI-U, NSA) 1913-01 → **2026-08** (ô 2025-10 trống trong nguồn); đối chiếu CPIAUCSL (SA): % đổi 12 tháng **943/943 tháng trong 0,5 điểm** (lệch lớn nhất 0,468); độ vững CWUR0000SA0 (CPI-W), PCEPI (PCE, từ 1959).
Bản ghim hồ sơ `topics-r1/machine/retire-1/sources.json` (coed=2026-08-01): **SHA khớp** (f79e3a78…); file mới = bản ghim (FRED chưa có CPI tháng 9/2026 ngày 08/10). bls.gov bị proxy chặn (403): không dùng R-CPI-E.
Tính: `model/model.py` (viết lại từ định nghĩa `result.json`, không gọi calc.py). calc.py hồ sơ chạy lại trên dữ liệu tải lại: **12/12 trùng `result.json`**. Câu diễn giải: `model/statements.py --all` → **9/9 True**. Kiểm độc lập (agent mới, chỉ từ định nghĩa): **43/43 khớp**, 9/9 câu đúng — `model/independent/report.md`.

**Luật nói (claim-risk, `topics-r1/machine/retire-1/claim-risk.md` + lệnh phiên 08/10):** không khuyên chọn sản phẩm/khoản trả/công ty, không nói gói CPI "tốt hơn"; **không dự báo lạm phát** (không "with inflation at X% today, you will…"); "history, not a forecast" cho mọi dòng `history`; **CPI-U ≠ giỏ hàng người về hưu** (y tế, nhà ở có thể khác — nói là giới hạn, không có số R-CPI-E); 715 cửa sổ chồng nhau ≠ 715 phép thử độc lập; giá niên kim (khoản 2 % khởi đầu thấp hơn bao nhiêu) **không mô hình hoá** → không nói khoản nào "nhận nhiều tiền hơn"; **không có cửa sổ 20 năm nào bắt đầu sau 2006-08**: nói "stretches that ran through the 2000s and 2010s", không "stretches starting in the 2010s" (kiểm độc lập, câu 7 hồ sơ); người về hưu dẫn đường và mọi ví dụ $ là ILLUSTRATIVE; "3.1%" là trung vị lịch sử, không phải kỳ vọng.

| Claim ID | Giá trị | Hiển thị | Định nghĩa | Nguồn | Ghi chú |
|---|---|---|---|---|---|
| `cpi_yoy_latest_pct` | 3.4 | 3.4% | CPI-U Aug 2026 / Aug 2025 − 1 (latest 12 months) | data/raw/CPIAUCNS.csv | present fact |
| `index_last_month` | 2026-08-01 | August 2026 | last CPIAUCNS observation (Sept 2026 CPI not released on 2026-10-08) | data/raw/CPIAUCNS.csv |  |
| `windows_20y` | 715 | 715 stretches | 20-year window = start month s ≥ 1947-01, end e = s + 240 months, both CPIAUCNS values present (2025-10 blank → start 2005-10 skipped); P = CPI(e)/CPI(s); starts 1947-01..2006-08 | data/raw/CPIAUCNS.csv | history |
| `windows_2pct_kept_up_20y` | 17 | 17 | count of 20-year windows with 1.02^20 ≥ P; all start 1947-09..1949-01 | data/raw/CPIAUCNS.csv | history |
| `share_2pct_kept_up_20y_pct` | 2.4 | 2.4% | 100 × kept / 715 (17 in 715 ≈ 1 in 42) | data/raw/CPIAUCNS.csv | history |
| `kept_up_first_start_20y` | 1947-09-01 | September 1947 | first start month of a kept-up window | data/raw/CPIAUCNS.csv | history |
| `kept_up_last_start_20y` | 1949-01-01 | January 1949 | last start month of a kept-up window (none since) | data/raw/CPIAUCNS.csv | history |
| `windows_25y` | 655 | 655 | 25-year windows (end s + 300), starts 1947-01..2001-08 | data/raw/CPIAUCNS.csv | history |
| `windows_2pct_kept_up_25y` | 0 | 0 of 655 | count with 1.02^25 ≥ P (25-year) | data/raw/CPIAUCNS.csv | history |
| `median_inflation_20y_pct_per_year` | 3.1 | 3.1% a year | median over 20-year windows of 100(P^(1/20) − 1) | data/raw/CPIAUCNS.csv | history; not an expectation |
| `median_real_value_2pct_payment_after_20y_pct` | 80.7 | 80.7% (about 4/5) | median of 100 × 1.02^20 / P | data/raw/CPIAUCNS.csv | history |
| `median_real_value_level_payment_after_20y_pct` | 54.3 | 54.3% (about half) | median of 100 / P | data/raw/CPIAUCNS.csv | history |
| `worst_real_value_2pct_payment_after_20y_pct` | 43.1 | 43.1% | min of 100 × 1.02^20 / P (window starting 1966-01) | data/raw/CPIAUCNS.csv | history |
| `worst_real_value_level_payment_after_20y_pct` | 29.0 | 29.0% | level check in the same worst window (1966-01 → 1986-01) | data/raw/CPIAUCNS.csv | history |
| `worst_window_start_year_20y` | 1966 | 1966 (January) | start of the worst window for the 2% check | data/raw/CPIAUCNS.csv | history |
| `share_2pct_at_least_90_after_20y_pct` | 32.6 | 32.6% (about 1 in 3) | % of 20-year windows with 2% check ≥ 90% of start | data/raw/CPIAUCNS.csv | history |
| `share_2pct_at_least_75_after_20y_pct` | 56.2 | 56.2% | % of windows with 2% check ≥ 75% | data/raw/CPIAUCNS.csv | history |
| `two_pct_growth_20y_pct` | 48.6 | 48.6% (about half) | 100(1.02^20 − 1): how much 20 raises of 2% grow a check | arithmetic | rule |
| `latest_start / latest_end` | 2006-08-01 / 2026-08-01 | Aug 2006 → Aug 2026 | most recent complete 20-year window | data/raw/CPIAUCNS.csv | history |
| `latest_window_real_value_2pct_payment_pct` | 90.4 | 90.4% (about 9 in 10) | 100 × 1.02^20 / P(2006-08 → 2026-08) | data/raw/CPIAUCNS.csv | history |
| `latest_window_real_value_level_payment_pct` | 60.9 | 60.9% (about 6 in 10) | 100 / P, same window | data/raw/CPIAUCNS.csv | history |
| `latest_window_price_rise_pct` | 64.3 | 64.3% | 100(P − 1), Aug 2006 → Aug 2026 | data/raw/CPIAUCNS.csv | history |
| `latest_window_inflation_pct_per_year` | 2.51 | 2.51% a year | 100(P^(1/20) − 1), Aug 2006 → Aug 2026 | data/raw/CPIAUCNS.csv | history |
| `guide_start` | 2006-08-01 | August 2006, age 65 | ILLUSTRATIVE guide character: first check Aug 2006 at 65 (= latest window) | data/raw/CPIAUCNS.csv | ILLUSTRATIVE |
| `guide_last_year_2pct_at_or_above_100` | 15 | 15 years (Aug 2021, age 80) | last anniversary k with 100 × 1.02^k / (CPI(s+12k)/CPI(s)) ≥ 100; values at k=15: 100.3% | data/raw/CPIAUCNS.csv | ILLUSTRATIVE; history |
| `guide_years_2pct_at_or_above_100` | 12 | 12 of the first 15 anniversaries | anniversaries k=1..20 with 2% check ≥ 100% (k=1,3,4,7,8,9,10..15; below at 2,5,6) | data/raw/CPIAUCNS.csv | ILLUSTRATIVE; history |
| `guide_real_2pct_2022_pct` | 94.5 | 94.5% (Aug 2022, age 81) | 2% check at k=16 (one year after 100.3%) | data/raw/CPIAUCNS.csv | ILLUSTRATIVE; history |
| `guide_real_level_2021_pct` | 74.5 | 74.5% (Aug 2021) | level check at k=15 | data/raw/CPIAUCNS.csv | ILLUSTRATIVE; history |
| `guide_real_2pct_end_pct` | 90.4 | 90.4% (Aug 2026, age 85) | = latest_window_real_value_2pct_payment_pct | data/raw/CPIAUCNS.csv | ILLUSTRATIVE; history |
| `guide_real_level_end_pct` | 60.9 | 60.9% | = latest_window_real_value_level_payment_pct | data/raw/CPIAUCNS.csv | ILLUSTRATIVE; history |
| `guide_year_level_reaches_2pct_end` | 5 | year 5 (Aug 2011, 90.0%) | first anniversary where her level check ≤ her 2% check's 20-year end value (90.4%) | data/raw/CPIAUCNS.csv | ILLUSTRATIVE; history |
| `median_year_level_reaches_2pct_end_median` | 8 | about year 8 | median over windows of first anniversary k where 100/(CPI(s+12k)/CPI(s)) ≤ 80.7 | data/raw/CPIAUCNS.csv | history |
| `by_decade_1990_median_real_2pct` | 94.8 | 94.8% | median 2% check after 20 years, starts 1990-01..1999-12 (0 of 120 kept up) | data/raw/CPIAUCNS.csv | history |
| `by_decade_2000_kept` | 0 | 0 of 79 | starts 2000-01..2006-08 that kept up (best 99.5%) | data/raw/CPIAUCNS.csv | history |
| `by_decade_2000_max_real_2pct` | 99.5 | 99.5% | best 2% check after 20 years among 2000s starts | data/raw/CPIAUCNS.csv | history |
| `by_decade_1960_median_real_2pct` | 44.3 | 44.3% | median, starts in the 1960s | data/raw/CPIAUCNS.csv | history |
| `raise_needed_half_20y_pct` | 3.1 | 3.1% a year | fixed yearly raise that kept up in half the 20-year windows (= median inflation) | data/raw/CPIAUCNS.csv | history; not advice |
| `raise_needed_all_20y_pct` | 6.38 | 6.38% a year | raise that kept up in every 20-year window (= max annualized inflation, window starting 1966-01) | data/raw/CPIAUCNS.csv | history; not advice |
| `raise_grid_3pct` | 42.4 | 42.4% | % of 20-year windows a 3% yearly raise kept up with | data/raw/CPIAUCNS.csv | history; not advice |
| `robust_cpiw_share_kept_up_20y_pct` | 2.9 | 2.9% (21 of 715) | same test on CPI-W (CWUR0000SA0, index for Social Security COLAs) | data/raw/CWUR0000SA0.csv | history; robustness |
| `robust_pce_share_kept_up_20y_pct` | 19.2 | 19.2% (110 of 572) | same test on the PCE price index (from 1959; starts 1959-01..2006-08) | data/raw/PCEPI.csv | history; robustness |
| `cpiu_from_pce_start_kept_up_20y` | 0 | 0 of 571 | CPI-U windows starting 1959-01 or later that kept up | data/raw/CPIAUCNS.csv | history; robustness |
| `robust_pce_median_real_2pct_pct` | 88.0 | 88.0% | median 2% check after 20 years on PCE | data/raw/PCEPI.csv | history; robustness |
