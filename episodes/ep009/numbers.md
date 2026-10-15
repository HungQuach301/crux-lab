# Claim — Tập 9 (Việc 0; claim ID = khoá `quantities` của `out/model.json`)

Dữ liệu (`data/fetch.py`, tải 2026-10-15; không commit): 4 chuỗi FRED của Tập 8 ở **đúng bản ghim** (HPIPONM226N đến 2026-07, CUUR0000SEHA đến 2026-08, MORTGAGE30US đến 2026-10-08, TB3MS) — **4/4 SHA trùng Tập 8**; tổng lợi nhuận cổ phiếu Mỹ: **Kenneth R. French Data Library**, Fama/French 3 Factors monthly (tệp "created using the 202608 CRSP database"), Mkt-RF + RF = lợi nhuận giá trị-trọng mọi cổ phiếu Mỹ niêm yết NYSE/AMEX/NASDAQ, cổ tức tái đầu tư, **trước phí và thuế**; đối chiếu Shiller (S&P Composite, URL Yale dừng 2023-09): $1 → 25,81 vs 25,24 trên 1991-01..2023-05 (`model/independent/report.md`).
`model/model.py`: quỹ tiền mặt **tái lập đúng Tập 8** (75.6 %, $157,104 trung vị, 6/2006 −$82,385, 4/2012 +$483,975). **Kiểm độc lập** (headless Sonnet, chỉ đọc data/raw + định nghĩa): **34/34 dòng trùng**.

**Quyền dữ liệu (kiểm trước khi viết, chủ dự án 15/10):** FRED — như Tập 8 (Public Domain: Citation Requested / Copyrighted: Citation Required, trích ở `data/sources.json`). French — trang ghi "Copyright Eugene F. Fama and Kenneth R. French", **không có câu giấy phép**, tải tự do không đăng ký; dữ liệu dựng từ CRSP. Cách dùng: chỉ kết quả suy ra (tỉ lệ, số đô của nhân vật ILLUSTRATIVE), **không** phân phối lại tệp, không vẽ lại chuỗi tháng; ghi nguồn trên hình và mô tả "Source: Kenneth R. French Data Library (CRSP data)". Không nói "S&P 500" (nhãn hiệu; chuỗi là mọi cổ phiếu Mỹ). Đây là **câu hỏi quyền cho chủ dự án ở G1** (RIGHTS `D-FRENCH`), không chặn viết. Không dùng: FRED SP500 (Pre-Approval Required, giá không cổ tức), Damodaran (năm, tệp 2021).

**Luật nói:** không khuyên (mua/thuê/đầu tư); "history, not a forecast"; "US only"; lợi nhuận cổ phiếu **trước phí và thuế** (biến thể phí 1 %/năm → 55.0 %), không thuế lãi vốn, không thuế nhà; "the whole US stock market", không tên chỉ số thương hiệu; người thuê đầu tư **mọi** tháng, kể cả khi quỹ tụt (183/307 cửa sổ quỹ có lúc dưới $92,000) — kỷ luật là giả định, biến thể "không để dành chênh hằng tháng" (lump) 63.8 %; nhà = chỉ số FHFA quốc gia; tiền thuê khởi đầu là GIẢ ĐỊNH (5 %, neo 7/2026) — độ nhạy: với quỹ cổ phiếu, đa số lật ở **5.06 %** ≈ đúng giả định 5 % → câu "the answer sits on the rent tag"; dải Census 4.83–5.59 % → 47.2–58.3 %; nhân vật ILLUSTRATIVE; quỹ cổ phiếu ≠ khuyên mua cổ phiếu; không gọi tập là "first".

Độ nhạy (tỉ lệ cửa sổ người mua hơn, 10 năm): neo 4 % → tiền mặt 64.2 / cổ phiếu 30.9; 5 % → 75.6 / 49.5; 6 % → 92.2 / 62.2.

| Claim ID | Giá trị | Hiển thị | Định nghĩa |
|---|---|---|---|
| `n_10y` | 307 | 307 start months | 10-year windows from 1991-01 |
| `last_10y` | 2016-07 | July 2016 | last start |
| `share_buyer_ahead_cash_10y` | 75.6 | about 3 in 4 (75.6%) — Episode 8 result, reproduced | share of windows with buyer advantage > 0, renter pot = cash |
| `share_buyer_ahead_stocks_10y` | 49.5 | about half (49.5%; 152 of 307) | share of windows with buyer advantage > 0, renter pot = stocks |
| `n_renter_ahead_stocks_10y` | 155 | 155 of 307 | windows with advantage <= 0, pot = stocks |
| `median_adv_stocks_10y` | -5827 | $5,827 behind (about even) | median buyer advantage, pot = stocks |
| `n_flip_to_renter_10y` | 80 | 80 start months | buyer ahead with cash pot, renter ahead with stock pot |
| `n_flip_to_buyer_10y` | 0 | none | renter ahead with cash pot, buyer ahead with stock pot |
| `share_buyer_ahead_lump_10y` | 63.8 | about 2 in 3 (63.8%) | share of windows with buyer advantage > 0, renter pot = lump |
| `share_buyer_ahead_stocks_fee_10y` | 55.0 | 55.0% | share of windows with buyer advantage > 0, renter pot = stocks_fee |
| `share_buyer_ahead_cash_15y` | 100.0 | every one (100%) | share of windows with buyer advantage > 0, renter pot = cash |
| `share_buyer_ahead_stocks_15y` | 21.9 | about 1 in 5 (21.9%) | share of windows with buyer advantage > 0, renter pot = stocks |
| `n_15y` | 247 | 247 | 15-year windows from 1991-01 |
| `share_buyer_ahead_stocks_5y` | 53.4 | 53.4% | share of windows with buyer advantage > 0, renter pot = stocks |
| `era_2002-2007_share_stocks` | 0.0 | none of 72 (0%) | era share buyer ahead, pot = stocks |
| `era_2002-2007_share_cash` | 8.3 | 6 of 72 (8.3%) | era share buyer ahead, pot = cash |
| `era_1990s_share_stocks` | 67.6 | about 2 in 3 (67.6%) | era share buyer ahead, pot = stocks |
| `era_2009-2016_share_stocks` | 78.0 | nearly 4 in 5 (78.0%) | era share buyer ahead, pot = stocks |
| `adv_2006-06_stocks_10y` | -261689 | $261,689 behind | buyer advantage for start 2006-06, pot = stocks |
| `adv_2006-06_cash_10y` | -82385 | $82,385 behind | buyer advantage for start 2006-06, pot = cash |
| `adv_2012-04_stocks_10y` | 237632 | $237,632 ahead | buyer advantage for start 2012-04, pot = stocks |
| `adv_2012-04_cash_10y` | 483975 | $483,975 ahead | buyer advantage for start 2012-04, pot = cash |
| `adv_1991-01_cash_10y` | 48410 | $48,410 ahead | buyer advantage for start 1991-01, pot = cash |
| `adv_1991-01_stocks_10y` | -485063 | $485,063 behind | buyer advantage for start 1991-01, pot = stocks |
| `stocks_growth_1991-01_10y` | 4.92 | almost 5 times (4.92x) | 10-year growth of $1 in stocks from 1991-01 |
| `worst_start_stocks_10y` | 1991-01 | January 1991 | start with smallest buyer advantage (best for renter), pot = stocks |
| `best_start_stocks_10y` | 2012-10 | October 2012 | start with largest buyer advantage, pot = stocks |
| `best_adv_stocks_10y` | 297855 | $297,855 ahead | largest buyer advantage, pot = stocks |
| `stocks_growth_median_10y` | 2.46 | about 2.5 times (2.46x) | median 10-year growth of $1 in US stocks (total return), over start months |
| `n_stocks_lost_10y` | 16 | 16 start months | 10-year windows where $1 in stocks ended below $1 |
| `stocks_growth_worst_start_10y` | 1999-03 | March 1999 | start with the smallest 10-year stock growth |
| `stocks_growth_worst_10y` | 0.77 | 0.77x (down 23%) | smallest 10-year growth of $1 |
| `n_stocks_lost_buyer_ahead_10y` | 16 | all 16 stay lit | of the windows where $1 in stocks ended below $1, buyer ahead (stock pot) |
| `n_pot_below_start_stocks_10y` | 183 | 183 of 307 (more than half) | windows where the stock pot dipped below $92,000 at some month-end |
| `min_pot_stocks_10y` | 54310 | $54,310 | lowest month-end stock pot in any window |
| `share_stocks_beat_house_10y` | 88.9 | 88.9% (about 9 in 10) | share of windows, stocks grew more than house index |
| `flip_yield_stocks_10y` | 5.06 | about 5.1% | anchor yield at which buyer-ahead share (stock pot) falls to 50% (10y) |
| `hvs_yield_2025Q4` | 4.83 | 4.83% a year | Census HVS 12 x median asking rent / median asking sales price, 2025Q4 |
| `hvs_yield_2026Q1` | 5.59 | 5.59% a year | Census HVS 12 x median asking rent / median asking sales price, 2026Q1 |
| `share_hvs_2025Q4_stocks_10y` | 47.2 | 47.2% | share buyer ahead, stock pot, that anchor |
| `share_hvs_2026Q1_stocks_10y` | 58.3 | 58.3% | share buyer ahead, stock pot, that anchor |
| `price` | 400000.0 | $400,000 | model parameter (as Episode 8) |
| `savings_usd` | 92000 | $92,000 | model parameter (as Episode 8) |
| `down_usd` | 80000 | $80,000 | model parameter (as Episode 8) |
| `closing_usd` | 12000 | $12,000 | model parameter (as Episode 8) |
| `sell_pct` | 6 | 6 percent | selling cost share |
| `owner_cost_pct` | 2.5 | 2.5 percent a year | property tax 1.0 + insurance 0.5 + repairs 1.0 (Episode 8 assumption) |
| `yield_anchor_pct` | 5.0 | 5 percent | anchor yield (assumption, Episode 8) |
| `fee_pct` | 1.0 | 1 percent a year | fee/tax-drag variant stocks_fee |
| `stocks_last` | 2026-08 | August 2026 | Last month of the Fama/French monthly file. |
| `hpi_last` | 2026-07 | July 2026 | Last month of the FHFA index file. |
