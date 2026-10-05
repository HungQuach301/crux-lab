# Claim — Tập 3 (claim ID = tên đại lượng của `topics-r1/machine/retire-4/model.json`)

Dữ liệu ghim: TB3MS, CPIAUCNS (FRED, coed=2026-08-01, SHA khớp hồ sơ). "Hôm nay" = **August 2026**. Tính: `episodes/ep003/model/model.py` (đặc tả `newKindNeeds`; tên kind do phiên K). Kiểm độc lập: 873/873 cửa sổ trùng tuyệt đối, 36/36 đại lượng (`model/independent/`). Mọi kết quả trước 5/2005 là **giả định** (bảo đảm áp như thể đã có) — claim `ctx_hypothetical` phải đi kèm câu NÊU kết quả.

## A. Đại lượng mô hình

| Claim ID | Giá trị | Đơn vị | Nghĩa |
|---|---|---|---|
| `starts` | 873 | start months | number of 20-year start months (T-bill roll windows) |
| `first_start` | 1934-01-01 | month | first start month |
| `last_start` | 2006-09-01 | month | last start month (its 240 months end with the latest data month) |
| `share_tbills_above_double_pct` | 52.3 | % of start months | share of start months where the 20-year T-bill roll ended above 2.0 times the money (strict) |
| `median_tbill_multiple_20y` | 2.097 | multiple | median 20-year T-bill roll multiple over all start months |
| `min_tbill_multiple_20y` | 1.129 | multiple | smallest 20-year roll multiple (start month = min_start) |
| `max_tbill_multiple_20y` | 4.612 | multiple | largest 20-year roll multiple (start month = max_start) |
| `share_tbills_above_double_starts_since_1990_pct` | 5.0 | % of start months | share of start months from 1990-01 on with roll above double |
| `latest_tbill_multiple_20y` | 1.378 | multiple | roll multiple of the last start month (window last_start .. latest_window_end) |
| `doubling_rate_pct_per_year` | 3.53 | % a year | annual rate that turns 1 into 2 in 20 years: 100(2^(1/20) − 1) |
| `real_windows` | 871 | start months | start months with CPI at both ends of the 20 years |
| `share_double_beat_prices_pct` | 58.7 | % of start months | share of real windows where 2.0 × CPI(s)/CPI(s+240) ≥ 1 (double kept its buying power) |
| `median_real_value_double_pct` | 107.3 | % | median buying power of the doubled amount, % of the original money |
| `tb3ms_latest_pct` | 3.72 | % a year | TB3MS in the latest data month (August 2026) |
| `viewer_age_decade` | 40 | years | card audience (savers in their 40s): audience definition, not a data claim |
| `horizon_years` | 20 | years | holding period of the comparison |
| `horizon_months` | 240 | months | holding period of the comparison |
| `bill_term_months` | 3 | months | maturity of the rolled bill |
| `bills_per_horizon` | 80 | bills | number of 3-month bills rolled in 20 years = 240/3 |
| `latest_window_end` | 2026-08-01 | month | last month of the latest full window = latest data month |
| `tb3ms_latest_month` | 2026-08-01 | month | month of tb3ms_latest_pct |
| `since_1990_from` | 1990-01-01 | month | first start month of the "from 1990 on" group |
| `min_start` | 1934-01-01 | month | start month of min_tbill_multiple_20y |
| `max_start` | 1972-05-01 | month | start month of max_tbill_multiple_20y |
| `guarantee_from` | 2005-05-01 | month | first issue month of bonds with today's 20-year doubling terms (31 CFR 351.34(a), 351.35(f)(2)) |
| `starts_with_guarantee` | 17 | start months | start months on or after guarantee_from (guarantee real, not hypothetical) |
| `starts_hypothetical` | 856 | start months | start months before guarantee_from (guarantee applied as if it had existed) |
| `share_hypothetical_pct` | 98.1 | % of start months | starts_hypothetical as a share of all start months |
| `share_above_double_guarantee_starts_pct` | 0.0 | % of start months | share of the starts_with_guarantee months with roll above double |
| `min_multiple_guarantee_starts` | 1.378 | multiple | smallest roll multiple among starts_with_guarantee |
| `max_multiple_guarantee_starts` | 1.388 | multiple | largest roll multiple among starts_with_guarantee |
| `starts_1934_1949` | 192 | start months | start months 1934-01 .. 1949-12 |
| `share_above_double_1934_1949_pct` | 0.0 | % of start months | share of 1934-01 .. 1949-12 starts with roll above double |
| `early_from` | 1934-01-01 | month | first month of the 1934–1949 group |
| `early_to` | 1949-12-01 | month | last month of the 1934–1949 group |
| `starts_1950_1989` | 480 | start months | start months 1950-01 .. 1989-12 |
| `share_above_double_1950_1989_pct` | 93.1 | % of start months | share of 1950-01 .. 1989-12 starts with roll above double |
| `mid_from` | 1950-01-01 | month | first month of the 1950–1989 group |
| `mid_to` | 1989-12-01 | month | last month of the 1950–1989 group |
| `starts_since_1990` | 201 | start months | start months 1990-01 .. last_start |
| `share_double_lost_buying_power_pct` | 41.3 | % of start months | share of real windows where the doubled amount bought less than the original (2.0 × CPI(s)/CPI(s+240) < 1) |
| `last_lost_start` | 1981-01-01 | month | latest start month in which double lost buying power |
| `worst_real_value_double_pct` | 58.0 | % | lowest buying power of the doubled amount, % of the original (start = worst_real_start) |
| `worst_real_start` | 1966-01-01 | month | start month of worst_real_value_double_pct |
| `share_since_1990_avg_below_start_pct` | 87.6 | % of start months | share of starts from 1990 on whose average TB3MS over the 240 months is below TB3MS in the start month |
| `mean_tb3ms_all_pct` | 3.42 | % a year | mean of every TB3MS month 1934-01 .. 2026-08 |
| `nonoverlap_periods` | 4 | periods | whole non-overlapping 20-year periods in the data = floor(1112/240) |
| `near_double_band_pct` | 0.5 | % | band used for near_double_starts |
| `near_double_starts` | 6 | start months | start months with |roll/2 − 1| < 0.5% |

## B. Bối cảnh (không phải số mô hình)

| Claim ID | Nội dung | Nguồn | Mức kiểm |
|---|---|---|---|
| `ctx_guarantee` | Series EE bonds issued May 1, 2005 or later reach original maturity at 20 years; at original maturity a book-entry bond is worth not less than double its purchase price | 31 CFR 351.34(a), 351.35(f)(2) (70 FR 17288–17289) | V1 — nguyên văn đọc trực tiếp law.cornell.edu 2026-10-04 |
| `ctx_hypothetical` | For start months before May 2005 the episode applies today's guarantee **as if it had existed**; earlier EE bonds had other terms | `model.json` `starts_hypothetical` = 856 (98.1%) | V1 (đếm) |
| `ctx_penalty` | Cashed before 5 years: lose 3 months of interest | 31 CFR 351.35(e) | V1 |
| `ctx_ee_rate` | EE bonds issued May–October 2026 earn a fixed 2.40% a year; the 20-year doubling tops this up. Lời và hình: "for bonds issued May–October 2026" | TreasuryDirect release 2026-05-01 + trang EE bonds | **V1** — chủ dự án (chat chiến lược) đọc trực tiếp, 2026-10-04. Lãi đặt lại mỗi 1/5 và 1/11 → **P3/C6 cập nhật lãi công bố 1/11/2026** (một claim; kết quả lịch sử không đổi) |
| `ctx_tb_sep` | TB3MS September 2026 = 3.94% (công bố 2026-10-01; ngoài bản ghim) | FRED TB3MS (không ghim) | dữ liệu; thêm vào không đổi tỉ lệ 52.3% / 5.0% (median 2.093, 18 tháng có bảo đảm, latest 1.377) |
| `ctx_cpi_rights` | TB3MS và CPIAUCNS: FRED gắn thẻ "Public Domain: Citation Requested" | trang series FRED, 2026-10-04 (bls.gov: proxy 403, chưa đọc trang BLS) | V1 theo thẻ FRED; dòng nguồn "U.S. Bureau of Labor Statistics via FRED" |

## C. Thêm ở C2 (needs-claims WRITER; `model/model.py` → `extra4`, kiểm độc lập)

| Claim ID | Giá trị | Đơn vị | Nghĩa |
|---|---|---|---|
| `steady_breakeven_tb3ms_pct` | 3.47 | % a year | lãi T-bill (cùng quy ước TB3MS/12, kép tháng) giữ nguyên 240 tháng thì vừa đúng gấp đôi: 1200(2^(1/240) − 1) = 3.4707 |
| `share_avg_rule_agrees_pct` | 100.0 | % of start months | tỉ lệ tháng bắt đầu mà "trung bình cộng TB3MS 240 tháng > 3.47" cho cùng kết luận với "lăn T-bill vượt gấp đôi" (873/873) |

