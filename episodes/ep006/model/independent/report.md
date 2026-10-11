43/43 khớp

Tính lại độc lập bằng `check.py` (chỉ đọc data/raw + định nghĩa; không đọc model.py/statements.py/calc.py/model.json). Câu trong statements.json: 9/9 True.

| Claim | numbers.md | Tính lại | Kết quả | Ghi chú |
|---|---|---|---|---|
| `cpi_yoy_latest_pct` | 3.4 | 3.4 | khớp |  |
| `index_last_month` | 2026-08-01 | 2026-08-01 | khớp |  |
| `windows_20y` | 715 | 715 | khớp | 1947-01..2006-08 |
| `windows_2pct_kept_up_20y` | 17 | 17 | khớp |  |
| `share_2pct_kept_up_20y_pct` | 2.4 | 2.4 | khớp |  |
| `kept_up_first_start_20y` | 1947-09-01 | 1947-09-01 | khớp |  |
| `kept_up_last_start_20y` | 1949-01-01 | 1949-01-01 | khớp |  |
| `windows_25y` | 655 | 655 | khớp | 1947-01..2001-08 |
| `windows_2pct_kept_up_25y` | 0 | 0 | khớp |  |
| `median_inflation_20y_pct_per_year` | 3.1 | 3.1 | khớp |  |
| `median_real_value_2pct_payment_after_20y_pct` | 80.7 | 80.7 | khớp |  |
| `median_real_value_level_payment_after_20y_pct` | 54.3 | 54.3 | khớp |  |
| `worst_real_value_2pct_payment_after_20y_pct` | 43.1 | 43.1 | khớp | start 1966-01 |
| `worst_real_value_level_payment_after_20y_pct` | 29.0 | 29.0 | khớp |  |
| `worst_window_start_year_20y` | 1966 | 1966 | khớp |  |
| `share_2pct_at_least_90_after_20y_pct` | 32.6 | 32.6 | khớp |  |
| `share_2pct_at_least_75_after_20y_pct` | 56.2 | 56.2 | khớp |  |
| `two_pct_growth_20y_pct` | 48.6 | 48.6 | khớp |  |
| `latest_start / latest_end` | 2006-08-01 / 2026-08-01 | 2006-08-01 / 2026-08-01 | khớp |  |
| `latest_window_real_value_2pct_payment_pct` | 90.4 | 90.4 | khớp |  |
| `latest_window_real_value_level_payment_pct` | 60.9 | 60.9 | khớp |  |
| `latest_window_price_rise_pct` | 64.3 | 64.3 | khớp |  |
| `latest_window_inflation_pct_per_year` | 2.51 | 2.51 | khớp |  |
| `guide_start` | 2006-08-01 | 2006-08-01 | khớp |  |
| `guide_last_year_2pct_at_or_above_100` | 15 | 15 | khớp | k=15: 100.31% |
| `guide_years_2pct_at_or_above_100` | 12 | 12 | khớp |  |
| `guide_real_2pct_2022_pct` | 94.5 | 94.5 | khớp |  |
| `guide_real_level_2021_pct` | 74.5 | 74.5 | khớp |  |
| `guide_real_2pct_end_pct` | 90.4 | 90.4 | khớp |  |
| `guide_real_level_end_pct` | 60.9 | 60.9 | khớp |  |
| `guide_year_level_reaches_2pct_end` | 5 | 5 | khớp | k=5: 90.00% |
| `median_year_level_reaches_2pct_end_median` | 8 | 8 | khớp |  |
| `by_decade_1990_median_real_2pct` | 94.8 | 94.8 | khớp |  |
| `by_decade_2000_kept` | 0 | 0 | khớp | n=79 (bỏ 2005-10) |
| `by_decade_2000_max_real_2pct` | 99.5 | 99.5 | khớp |  |
| `by_decade_1960_median_real_2pct` | 44.3 | 44.3 | khớp |  |
| `raise_needed_half_20y_pct` | 3.1 | 3.1 | khớp |  |
| `raise_needed_all_20y_pct` | 6.38 | 6.38 | khớp | max ở 1966-01 |
| `raise_grid_3pct` | 42.4 | 42.4 | khớp |  |
| `robust_cpiw_share_kept_up_20y_pct` | 2.9 | 2.9 | khớp | 21/715 |
| `robust_pce_share_kept_up_20y_pct` | 19.2 | 19.2 | khớp | 110/572 |
| `cpiu_from_pce_start_kept_up_20y` | 0 | 0 | khớp | n=571 |
| `robust_pce_median_real_2pct_pct` | 88.0 | 88.0 | khớp |  |

## Định nghĩa mơ hồ (không ảnh hưởng kết quả hiện tại)
- `median_year_level_reaches_2pct_end_median`: ngưỡng 80.7 (đã làm tròn) hay trung vị chính xác (80.70…)? Cả hai cho 8. Mọi cửa sổ đều chạm ngưỡng trong k≤20 (không có cửa sổ "không bao giờ" cần quy ước).
- `guide_year_level_reaches_2pct_end`: so với 90.4 làm tròn hay 90.40… chính xác — đều cho k=5 (90.004%, sát ngưỡng 90.0 nếu ai so với 90.0).
- `guide_years_2pct_at_or_above_100`: "k=1..20" nhưng hiển thị "of the first 15" — số 12 đúng cho cả hai (không có k>15 ≥100).
- Decades / `by_decade_2000_*`: "2000s" = start 2000-01..2006-08 (79 cửa sổ), không phải thập kỷ đầy đủ.
- Câu 7 nói "including the low-inflation … 2010s": không có cửa sổ 20 năm nào *bắt đầu* trong 2010s; chỉ đúng nếu hiểu là các cửa sổ *bao trùm* 2010s (khởi đầu 1990s/2000s). Nên sửa chữ hoặc ghi rõ.
- Biên "kept up" (≥): cửa sổ gần 100% nhất cách 0.18 điểm → không có tie, ≥ vs > không đổi kết quả.
- `cpi_yoy_latest_pct`: lấy Aug 2026/Aug 2025 (tháng cuối có dữ liệu) — đúng theo định nghĩa.
