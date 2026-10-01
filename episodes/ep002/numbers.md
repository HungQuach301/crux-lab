# Tập 2 — Bảng số (sinh bởi `build_numbers.py` từ `out/model.json`; không gõ tay)

Mọi số của tập phải trỏ về một claim ID ở đây. Kiểm độc lập: `model/independent/compare.json` (85/85 đại lượng, 753/753 cửa sổ, 0 lệch). Mốc dữ liệu: TB3MS tới **August 2026** (3.72%), tải 2026-10-01.

**ILLUSTRATIVE**: mọi số của khoản vay (cặp lãi 7.5%/9%, $50,000, 10 năm) là của một khoản vay minh hoạ; chỉ số TB3MS là dữ liệu thật. "History, not a forecast." Phạm vi (b) đánh dấu `b`.

| Claim ID | Hiển thị | Lời (gợi ý) | Công thức | Loại | Minh hoạ | Phạm vi |
|---|---|---|---|---|---|---|
| `loan` | $50,000 |  | loan amount (model param) | param | có | a |
| `term` | 10 years (120 monthly payments) |  | term (model param) | param | có | a |
| `fixed_rate` | 9% |  | fixed rate offer (model param) | param | có | a |
| `var_start` | 7.5% |  | variable rate at origination (model param) | param | có | a |
| `gap_start` | 1.5 points |  | fixed_rate − var_start | param | có | a |
| `index_today` | 3.72% |  | TB3MS, last observation 2026-08 | data | không | a |
| `margin` | 3.78 points |  | var_start − index_today | model | có | a |
| `tb_peak` | 16.30% | May 1981 | max TB3MS 1934-01..2026-08 | data | không | a |
| `n_starts` | 753 |  | start months with a full 120-month window, 1954-01..2016-09 | model | có | a |
| `first_start` | January 1954 |  | first start month | model | có | a |
| `last_start` | September 2016 |  | last start month with 120 months of data | model | có | a |
| `n_early` | 324 |  | start months 1954-01..1980-12 | model | có | a |
| `n_late` | 429 |  | start months 1981-01..2016-09 | model | có | a |
| `fixed_int` | $26,005 |  | total interest, 9% fixed, 120 months | model | có | a |
| `n_costlier` | 107 |  | windows with Difference > 0 | model | có | a |
| `share_all` | 14.2% | about 1 in 7 | share of start months where variable total interest > fixed | model | có | a |
| `share_early` | 28.4% | more than 1 in 4 | share costlier, starts 1954-1980 | model | có | a |
| `share_late` | 3.5% | about 1 in 30 | share costlier, starts 1981 on | model | có | a |
| `median_diff` | −$3,832 | $3,832 less | median Difference (negative = variable cheaper) | model | có | a |
| `worst_diff` | +$11,219 |  | max Difference | model | có | a |
| `worst_start` | April 1977 |  | start month of the max Difference | model | có | a |
| `worst_peak_rate` | 19.3% |  | highest monthly variable rate in the worst window | model | có | a |
| `worst_share_of_fixed` | 43% |  | worst_diff / fixed_int | model | có | a |
| `best_diff` | −$15,295 |  | min Difference | model | có | a |
| `best_start` | August 1981 |  | start month of the min Difference | model | có | a |
| `max_rate_any` | 20.6% | window starting February 1972 | highest monthly variable rate in any window | model | có | a |
| `share_rate_above_fixed` | 76.2% | about 3 in 4 | share of windows whose variable rate exceeded 9% in some month | model | có | a |
| `fixed_payment` | $633.38 |  | level payment, 9%, 120 months | model | có | b |
| `var_first_payment` | $593.51 |  | first payment at 7.5% | model | có | b |
| `max_payment` | $863.36 |  | highest variable monthly payment, any window | model | có | b |
| `median_max_payment` | $643.28 |  | median over windows of the highest monthly payment | model | có | b |
| `share_payment_above_fixed` | 58.4% | more than half | share of windows where the variable payment exceeded the fixed payment in some month | model | có | b |
| `gapm10_share` | 72.9% |  | share costlier, start gap -1.0 points | model | có | b |
| `gapm10_early` | 92.9% |  | gap -1.0: 1954-1980 | model | có | b |
| `gapm10_late` | 57.8% |  | gap -1.0: 1981 on | model | có | b |
| `gapm10_worst` | +$20,217 |  | gap -1.0: worst Difference | model | có | b |
| `gapm05_share` | 64.7% |  | share costlier, start gap -0.5 points | model | có | b |
| `gapm05_early` | 88.0% |  | gap -0.5: 1954-1980 | model | có | b |
| `gapm05_late` | 47.1% |  | gap -0.5: 1981 on | model | có | b |
| `gapm05_worst` | +$18,383 |  | gap -0.5: worst Difference | model | có | b |
| `gap00_share` | 57.9% |  | share costlier, start gap 0.0 points | model | có | b |
| `gap00_early` | 79.0% |  | gap 0.0: 1954-1980 | model | có | b |
| `gap00_late` | 42.0% |  | gap 0.0: 1981 on | model | có | b |
| `gap00_worst` | +$16,566 |  | gap 0.0: worst Difference | model | có | b |
| `gap05_share` | 42.5% |  | share costlier, start gap 0.5 points | model | có | b |
| `gap05_early` | 68.5% |  | gap 0.5: 1954-1980 | model | có | b |
| `gap05_late` | 22.8% |  | gap 0.5: 1981 on | model | có | b |
| `gap05_worst` | +$14,766 |  | gap 0.5: worst Difference | model | có | b |
| `gap10_share` | 31.3% |  | share costlier, start gap 1.0 points | model | có | b |
| `gap10_early` | 54.9% |  | gap 1.0: 1954-1980 | model | có | b |
| `gap10_late` | 13.5% |  | gap 1.0: 1981 on | model | có | b |
| `gap10_worst` | +$12,983 |  | gap 1.0: worst Difference | model | có | b |
| `gap15_share` | 14.2% |  | share costlier, start gap 1.5 points | model | có | b |
| `gap15_early` | 28.4% |  | gap 1.5: 1954-1980 | model | có | b |
| `gap15_late` | 3.5% |  | gap 1.5: 1981 on | model | có | b |
| `gap15_worst` | +$11,219 |  | gap 1.5: worst Difference | model | có | b |
| `gap20_share` | 8.8% |  | share costlier, start gap 2.0 points | model | có | b |
| `gap20_early` | 20.4% |  | gap 2.0: 1954-1980 | model | có | b |
| `gap20_late` | 0.0% |  | gap 2.0: 1981 on | model | có | b |
| `gap20_worst` | +$9,472 |  | gap 2.0: worst Difference | model | có | b |
| `gap25_share` | 6.0% |  | share costlier, start gap 2.5 points | model | có | b |
| `gap25_early` | 13.9% |  | gap 2.5: 1954-1980 | model | có | b |
| `gap25_late` | 0.0% |  | gap 2.5: 1981 on | model | có | b |
| `gap25_worst` | +$7,743 |  | gap 2.5: worst Difference | model | có | b |
| `gap30_share` | 4.5% |  | share costlier, start gap 3.0 points | model | có | b |
| `gap30_early` | 10.5% |  | gap 3.0: 1954-1980 | model | có | b |
| `gap30_late` | 0.0% |  | gap 3.0: 1981 on | model | có | b |
| `gap30_worst` | +$6,033 |  | gap 3.0: worst Difference | model | có | b |
| `cap12_share` | 13.3% |  | share costlier, rate capped at 12% | model | có | b |
| `cap12_early` | 26.2% |  | cap 12: 1954-1980 | model | có | b |
| `cap12_worst` | +$6,590 |  | cap 12: worst Difference | model | có | b |
| `cap15_share` | 13.9% |  | share costlier, rate capped at 15% | model | có | b |
| `cap15_early` | 27.8% |  | cap 15: 1954-1980 | model | có | b |
| `cap15_worst` | +$9,821 |  | cap 15: worst Difference | model | có | b |
| `cap18_share` | 14.2% |  | share costlier, rate capped at 18% | model | có | b |
| `cap18_early` | 28.4% |  | cap 18: 1954-1980 | model | có | b |
| `cap18_worst` | +$11,137 |  | cap 18: worst Difference | model | có | b |
| `cap25_share` | 14.2% |  | share costlier, rate capped at 25% | model | có | b |
| `cap25_early` | 28.4% |  | cap 25: 1954-1980 | model | có | b |
| `cap25_worst` | +$11,219 |  | cap 25: worst Difference | model | có | b |

## Ghi chú

- **Sửa câu chữ của hồ sơ.** `result.json → answer` và `claim-risk.md` viết cửa sổ xấu nhất (bắt đầu 4/1977) "peaking at 20.6%". Sai: cửa sổ đó đỉnh **19.26%** (`worst_peak_rate`); 20.6% là đỉnh của cửa sổ bắt đầu February 1972 (`max_rate_any`), cửa sổ này đắt hơn $6,185. Số `max_variable_rate_any_window` của hồ sơ đúng theo định nghĩa ('any window'); chỉ câu tóm tắt ghép sai. Tập dùng hai claim riêng.
- **Độ nhạy với quan sát tháng 9/2026** (FRED công bố 1/10/2026): kết quả không phụ thuộc giá trị chỉ số hôm nay trừ khi sàn 0 chạm; thử 3.2–4.2 → share 14.2%, worst $11,219 không đổi. Chỉ `index_today` và `margin` đổi.
- Cửa sổ chồng nhau: 753 tháng bắt đầu không phải 753 phép thử độc lập (claim-risk).
