# Claim — Tập 4 (claim ID = khoá của `out/model.json` → `rounded`)

Dữ liệu ghim: 12 chỉ số FHFA all-transactions metro + USSTHPI (quý, tới **2026 Q2**) + CPIAUCNS (tới **August 2026**), FRED; SHA 14/14 khớp hồ sơ `topics-r1/machine/tax-2/sources.json` (`data/fetch.py`, 2026-10-05). Tính: `model/model.py` (đặc tả `newKindNeeds` của hồ sơ; tên kind do phiên K). Khớp `calc.py` hồ sơ 34/34; kiểm độc lập (agent mới, chỉ đọc `gates/V0-defs.md`) **116/116** đại lượng trùng tuyệt đối (`model/independent/`). Câu diễn giải hồ sơ 24/24 True trên dữ liệu tải lại.

**Luật nói (claim-risk hồ sơ):** mọi ngưỡng là của "a home that rose like the metro average", không phải căn nhà cụ thể; không đổi ngưỡng thành hoá đơn thuế; không khuyên bán/giữ; không dự báo giá nhà hay Quốc hội; FHFA sửa số hằng quý; "history, not a forecast"; "US only"; giá mua $200,000 / $300,000 là ILLUSTRATIVE.

| Claim ID | Giá trị | Nghĩa |
|---|---|---|
| `growth_los_angeles` | 4.3004 | index growth 2000 avg → 2026 Q2 (ratio) — Los Angeles |
| `threshold_joint_los_angeles` | 151500.0 | 2000 purchase price above which an index-typical gain exceeds $500,000 (USD, to $100) — Los Angeles |
| `gain_at_200k_los_angeles` | 660100.0 | gain at 2026 Q2 of a $200,000 2000 purchase that rose like the index (USD, ILLUSTRATIVE) — Los Angeles |
| `cross_quarter_at_200k_los_angeles` | 2021-10-01 | first quarter the $200,000 purchase's gain exceeded $500,000 (null = not by 2026 Q2) — Los Angeles |
| `stay_quarter_at_200k_los_angeles` | 2021-10-01 | first quarter from which the $200,000 gain stayed above $500,000 through 2026 Q2 — Los Angeles |
| `gain_at_300k_los_angeles` | 990100.0 | same, $300,000 purchase — Los Angeles |
| `cross_quarter_at_300k_los_angeles` | 2018-01-01 | same, $300,000 — Los Angeles |
| `stay_quarter_at_300k_los_angeles` | 2018-01-01 | same, $300,000 — Los Angeles |
| `growth_san_diego` | 4.0404 | index growth 2000 avg → 2026 Q2 (ratio) — San Diego |
| `threshold_joint_san_diego` | 164500.0 | 2000 purchase price above which an index-typical gain exceeds $500,000 (USD, to $100) — San Diego |
| `gain_at_200k_san_diego` | 608100.0 | gain at 2026 Q2 of a $200,000 2000 purchase that rose like the index (USD, ILLUSTRATIVE) — San Diego |
| `cross_quarter_at_200k_san_diego` | 2022-04-01 | first quarter the $200,000 purchase's gain exceeded $500,000 (null = not by 2026 Q2) — San Diego |
| `stay_quarter_at_200k_san_diego` | 2023-04-01 | first quarter from which the $200,000 gain stayed above $500,000 through 2026 Q2 — San Diego |
| `gain_at_300k_san_diego` | 912100.0 | same, $300,000 purchase — San Diego |
| `cross_quarter_at_300k_san_diego` | 2021-01-01 | same, $300,000 — San Diego |
| `stay_quarter_at_300k_san_diego` | 2021-01-01 | same, $300,000 — San Diego |
| `growth_san_francisco` | 2.9305 | index growth 2000 avg → 2026 Q2 (ratio) — San Francisco |
| `threshold_joint_san_francisco` | 259000.0 | 2000 purchase price above which an index-typical gain exceeds $500,000 (USD, to $100) — San Francisco |
| `gain_at_200k_san_francisco` | 386100.0 | gain at 2026 Q2 of a $200,000 2000 purchase that rose like the index (USD, ILLUSTRATIVE) — San Francisco |
| `cross_quarter_at_200k_san_francisco` | None | first quarter the $200,000 purchase's gain exceeded $500,000 (null = not by 2026 Q2) — San Francisco |
| `stay_quarter_at_200k_san_francisco` | None | first quarter from which the $200,000 gain stayed above $500,000 through 2026 Q2 — San Francisco |
| `gain_at_300k_san_francisco` | 579200.0 | same, $300,000 purchase — San Francisco |
| `cross_quarter_at_300k_san_francisco` | 2022-01-01 | same, $300,000 — San Francisco |
| `stay_quarter_at_300k_san_francisco` | 2022-01-01 | same, $300,000 — San Francisco |
| `growth_san_jose` | 2.9652 | index growth 2000 avg → 2026 Q2 (ratio) — San Jose |
| `threshold_joint_san_jose` | 254400.0 | 2000 purchase price above which an index-typical gain exceeds $500,000 (USD, to $100) — San Jose |
| `gain_at_200k_san_jose` | 393000.0 | gain at 2026 Q2 of a $200,000 2000 purchase that rose like the index (USD, ILLUSTRATIVE) — San Jose |
| `cross_quarter_at_200k_san_jose` | None | first quarter the $200,000 purchase's gain exceeded $500,000 (null = not by 2026 Q2) — San Jose |
| `stay_quarter_at_200k_san_jose` | None | first quarter from which the $200,000 gain stayed above $500,000 through 2026 Q2 — San Jose |
| `gain_at_300k_san_jose` | 589600.0 | same, $300,000 purchase — San Jose |
| `cross_quarter_at_300k_san_jose` | 2022-04-01 | same, $300,000 — San Jose |
| `stay_quarter_at_300k_san_jose` | 2022-04-01 | same, $300,000 — San Jose |
| `growth_seattle` | 3.7779 | index growth 2000 avg → 2026 Q2 (ratio) — Seattle |
| `threshold_joint_seattle` | 180000.0 | 2000 purchase price above which an index-typical gain exceeds $500,000 (USD, to $100) — Seattle |
| `gain_at_200k_seattle` | 555600.0 | gain at 2026 Q2 of a $200,000 2000 purchase that rose like the index (USD, ILLUSTRATIVE) — Seattle |
| `cross_quarter_at_200k_seattle` | 2022-04-01 | first quarter the $200,000 purchase's gain exceeded $500,000 (null = not by 2026 Q2) — Seattle |
| `stay_quarter_at_200k_seattle` | 2023-04-01 | first quarter from which the $200,000 gain stayed above $500,000 through 2026 Q2 — Seattle |
| `gain_at_300k_seattle` | 833400.0 | same, $300,000 purchase — Seattle |
| `cross_quarter_at_300k_seattle` | 2020-04-01 | same, $300,000 — Seattle |
| `stay_quarter_at_300k_seattle` | 2020-04-01 | same, $300,000 — Seattle |
| `growth_boston` | 3.2089 | index growth 2000 avg → 2026 Q2 (ratio) — Boston |
| `threshold_joint_boston` | 226400.0 | 2000 purchase price above which an index-typical gain exceeds $500,000 (USD, to $100) — Boston |
| `gain_at_200k_boston` | 441800.0 | gain at 2026 Q2 of a $200,000 2000 purchase that rose like the index (USD, ILLUSTRATIVE) — Boston |
| `cross_quarter_at_200k_boston` | None | first quarter the $200,000 purchase's gain exceeded $500,000 (null = not by 2026 Q2) — Boston |
| `stay_quarter_at_200k_boston` | None | first quarter from which the $200,000 gain stayed above $500,000 through 2026 Q2 — Boston |
| `gain_at_300k_boston` | 662700.0 | same, $300,000 purchase — Boston |
| `cross_quarter_at_300k_boston` | 2022-04-01 | same, $300,000 — Boston |
| `stay_quarter_at_300k_boston` | 2023-01-01 | same, $300,000 — Boston |
| `growth_new_york` | 3.3558 | index growth 2000 avg → 2026 Q2 (ratio) — New York |
| `threshold_joint_new_york` | 212200.0 | 2000 purchase price above which an index-typical gain exceeds $500,000 (USD, to $100) — New York |
| `gain_at_200k_new_york` | 471200.0 | gain at 2026 Q2 of a $200,000 2000 purchase that rose like the index (USD, ILLUSTRATIVE) — New York |
| `cross_quarter_at_200k_new_york` | None | first quarter the $200,000 purchase's gain exceeded $500,000 (null = not by 2026 Q2) — New York |
| `stay_quarter_at_200k_new_york` | None | first quarter from which the $200,000 gain stayed above $500,000 through 2026 Q2 — New York |
| `gain_at_300k_new_york` | 706700.0 | same, $300,000 purchase — New York |
| `cross_quarter_at_300k_new_york` | 2023-04-01 | same, $300,000 — New York |
| `stay_quarter_at_300k_new_york` | 2023-04-01 | same, $300,000 — New York |
| `growth_miami` | 5.3601 | index growth 2000 avg → 2026 Q2 (ratio) — Miami |
| `threshold_joint_miami` | 114700.0 | 2000 purchase price above which an index-typical gain exceeds $500,000 (USD, to $100) — Miami |
| `gain_at_200k_miami` | 872000.0 | gain at 2026 Q2 of a $200,000 2000 purchase that rose like the index (USD, ILLUSTRATIVE) — Miami |
| `cross_quarter_at_200k_miami` | 2021-10-01 | first quarter the $200,000 purchase's gain exceeded $500,000 (null = not by 2026 Q2) — Miami |
| `stay_quarter_at_200k_miami` | 2021-10-01 | first quarter from which the $200,000 gain stayed above $500,000 through 2026 Q2 — Miami |
| `gain_at_300k_miami` | 1308000.0 | same, $300,000 purchase — Miami |
| `cross_quarter_at_300k_miami` | 2006-10-01 | same, $300,000 — Miami |
| `stay_quarter_at_300k_miami` | 2019-04-01 | same, $300,000 — Miami |
| `growth_denver` | 3.1961 | index growth 2000 avg → 2026 Q2 (ratio) — Denver |
| `threshold_joint_denver` | 227700.0 | 2000 purchase price above which an index-typical gain exceeds $500,000 (USD, to $100) — Denver |
| `gain_at_200k_denver` | 439200.0 | gain at 2026 Q2 of a $200,000 2000 purchase that rose like the index (USD, ILLUSTRATIVE) — Denver |
| `cross_quarter_at_200k_denver` | None | first quarter the $200,000 purchase's gain exceeded $500,000 (null = not by 2026 Q2) — Denver |
| `stay_quarter_at_200k_denver` | None | first quarter from which the $200,000 gain stayed above $500,000 through 2026 Q2 — Denver |
| `gain_at_300k_denver` | 658800.0 | same, $300,000 purchase — Denver |
| `cross_quarter_at_300k_denver` | 2021-07-01 | same, $300,000 — Denver |
| `stay_quarter_at_300k_denver` | 2021-07-01 | same, $300,000 — Denver |
| `growth_phoenix` | 3.7903 | index growth 2000 avg → 2026 Q2 (ratio) — Phoenix |
| `threshold_joint_phoenix` | 179200.0 | 2000 purchase price above which an index-typical gain exceeds $500,000 (USD, to $100) — Phoenix |
| `gain_at_200k_phoenix` | 558100.0 | gain at 2026 Q2 of a $200,000 2000 purchase that rose like the index (USD, ILLUSTRATIVE) — Phoenix |
| `cross_quarter_at_200k_phoenix` | 2022-04-01 | first quarter the $200,000 purchase's gain exceeded $500,000 (null = not by 2026 Q2) — Phoenix |
| `stay_quarter_at_200k_phoenix` | 2023-04-01 | first quarter from which the $200,000 gain stayed above $500,000 through 2026 Q2 — Phoenix |
| `gain_at_300k_phoenix` | 837100.0 | same, $300,000 purchase — Phoenix |
| `cross_quarter_at_300k_phoenix` | 2021-04-01 | same, $300,000 — Phoenix |
| `stay_quarter_at_300k_phoenix` | 2021-04-01 | same, $300,000 — Phoenix |
| `growth_dallas` | 3.3189 | index growth 2000 avg → 2026 Q2 (ratio) — Dallas |
| `threshold_joint_dallas` | 215600.0 | 2000 purchase price above which an index-typical gain exceeds $500,000 (USD, to $100) — Dallas |
| `gain_at_200k_dallas` | 463800.0 | gain at 2026 Q2 of a $200,000 2000 purchase that rose like the index (USD, ILLUSTRATIVE) — Dallas |
| `cross_quarter_at_200k_dallas` | None | first quarter the $200,000 purchase's gain exceeded $500,000 (null = not by 2026 Q2) — Dallas |
| `stay_quarter_at_200k_dallas` | None | first quarter from which the $200,000 gain stayed above $500,000 through 2026 Q2 — Dallas |
| `gain_at_300k_dallas` | 695700.0 | same, $300,000 purchase — Dallas |
| `cross_quarter_at_300k_dallas` | 2021-10-01 | same, $300,000 — Dallas |
| `stay_quarter_at_300k_dallas` | 2021-10-01 | same, $300,000 — Dallas |
| `growth_chicago` | 2.3392 | index growth 2000 avg → 2026 Q2 (ratio) — Chicago |
| `threshold_joint_chicago` | 373400.0 | 2000 purchase price above which an index-typical gain exceeds $500,000 (USD, to $100) — Chicago |
| `gain_at_200k_chicago` | 267800.0 | gain at 2026 Q2 of a $200,000 2000 purchase that rose like the index (USD, ILLUSTRATIVE) — Chicago |
| `cross_quarter_at_200k_chicago` | None | first quarter the $200,000 purchase's gain exceeded $500,000 (null = not by 2026 Q2) — Chicago |
| `stay_quarter_at_200k_chicago` | None | first quarter from which the $200,000 gain stayed above $500,000 through 2026 Q2 — Chicago |
| `gain_at_300k_chicago` | 401800.0 | same, $300,000 purchase — Chicago |
| `cross_quarter_at_300k_chicago` | None | same, $300,000 — Chicago |
| `stay_quarter_at_300k_chicago` | None | same, $300,000 — Chicago |
| `growth_us` | 3.0536 | index growth 2000 avg → 2026 Q2 (ratio) — United States (national index) |
| `threshold_joint_us` | 243500.0 | 2000 purchase price above which an index-typical gain exceeds $500,000 (USD, to $100) — United States (national index) |
| `gain_at_200k_us` | 410700.0 | gain at 2026 Q2 of a $200,000 2000 purchase that rose like the index (USD, ILLUSTRATIVE) — United States (national index) |
| `cross_quarter_at_200k_us` | None | first quarter the $200,000 purchase's gain exceeded $500,000 (null = not by 2026 Q2) — United States (national index) |
| `stay_quarter_at_200k_us` | None | first quarter from which the $200,000 gain stayed above $500,000 through 2026 Q2 — United States (national index) |
| `gain_at_300k_us` | 616100.0 | same, $300,000 purchase — United States (national index) |
| `cross_quarter_at_300k_us` | 2023-04-01 | same, $300,000 — United States (national index) |
| `stay_quarter_at_300k_us` | 2023-04-01 | same, $300,000 — United States (national index) |
| `threshold_single_us` | 121700.0 | national threshold for a single seller ($250,000 limit) |
| `threshold_joint_min` | 114700.0 | lowest metro threshold |
| `threshold_joint_max` | 373400.0 | highest metro threshold |
| `threshold_joint_min_metro` | miami | metro with lowest threshold |
| `threshold_joint_max_metro` | chicago | metro with highest threshold |
| `metros_threshold_under_200k` | 5 | metros (of 12) with threshold < $200,000 |
| `metros_threshold_under_300k` | 11 | metros (of 12) with threshold < $300,000 |
| `metros_threshold_under_300k_names` | ['boston', 'dallas', 'denver', 'los_angeles', 'miami', 'new_york', 'phoenix', 'san_diego', 'san_francisco', 'san_jose', 'seattle'] | those metros |
| `metros_crossed_at_200k` | 5 | metros where a $200,000 purchase's gain exceeds $500,000 by 2026 Q2 |
| `metros_crossed_at_300k` | 11 | same, $300,000 |
| `cpi_base` | 160.1 | CPI-U May 1997 |
| `cpi_now` | 334.98 | CPI-U August 2026 |
| `excl_joint_1997_in_now` | 1046000.0 | $500,000 of May 1997 in August 2026 prices (USD, to $1,000) |

## Hằng số luật (trích nguyên văn ở hồ sơ `sources.json` → `provisions`)

| Claim ID | Giá trị | Nguồn |
|---|---|---|
| `excl_joint_limit_usd` | 500000 | 26 U.S.C. 121(b)(2)(A) |
| `excl_single_limit_usd` | 250000 | 26 U.S.C. 121(b)(1) |
| `exclusion_effective_month` | 1997-05 (sales after 1997-05-06) | Pub. L. 105-34 note |
| `ownership_use_test` | 2 of the 5 years before sale (assumed met) | 26 U.S.C. 121(a) |
| `basis_at_death_rule` | basis = value at death (stated, not computed) | 26 U.S.C. 1014(a)(1) |
| `long_term_gain_rule` | held > 1 year → long-term gain | 26 U.S.C. 1222(3) |
| `surviving_spouse_window_years` | 2 | 26 U.S.C. 121(b)(4) |
| `buy_year` | 2000 | viewer identity (card) |
| `illustrative_price_200k_usd` | 200000 | ILLUSTRATIVE 2000 purchase price (model param `prices`) |
| `illustrative_price_300k_usd` | 300000 | ILLUSTRATIVE 2000 purchase price (model param `prices`) |
| `metro_count` | 12 | metros (metro divisions/MSAs) in the comparison — n_metros of hồ sơ |
| `sale_quarter` | 2026 Q2 | latest quarter in every index file |
| `ctx_us_only` | US federal tax rule only; state tax not modeled | phạm vi |
| `ctx_history` | history, not a forecast | gen bảo vệ |
