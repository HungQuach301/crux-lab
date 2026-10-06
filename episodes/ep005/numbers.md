# Claim — Tập 5 (Việc 0; claim ID = khoá của `out/model.json` → `rounded`)

Dữ liệu (FRED, tải 2026-10-06, `data/fetch.py`; không commit): HPIPONM226N tới **2026-07**, MORTGAGE30US tới **2026-10-01**, MSPUS tới 2026-04; đối chiếu CSUSHPINSA (tới 2026-07), OBMMIC30YF (tới 2026-10-05).
Bản ghim hồ sơ `topics-r2/machine/debt-2/sources.json`: SHA khớp cả hai; phần đầu file mới trùng từng dòng (không sửa số cũ). File mới chỉ thêm tuần 2026-10-01 (7.28%).
Tính: `model/model.py` (viết lại từ đặc tả, không gọi calc.py). Mọi số tập A/B trùng `result.json` hồ sơ 17/17. Câu diễn giải: `model/statements.py --all` → 17/17 True.

**Cảnh báo:** calc.py hồ sơ lấy tháng lãi = `max(rate)` → chạy trên dữ liệu mới sẽ ra **2026-10 (7.28%, 1 tuần), 104/119 tháng**. Mô hình tập dùng *tháng đủ tuần cuối cùng* = 2026-09 (6.862%, 99/114). Ghi luật này lên thẻ phương pháp.
Đối chiếu: lãi PMMS vs Optimal Blue 7 ngày: 508/508 tuần trong 0,5 điểm (lệch lớn nhất 0.384). Chỉ số giá: % đổi theo tháng FHFA vs Case-Shiller: 374/426 tháng trong 0,5 điểm (52 tháng lệch ghi ở `mismatches`; Case-Shiller là trung bình 3 tháng). Kết quả chính trên Case-Shiller: trung vị vẫn 23 tháng, >60 tháng vẫn 14,7%.

**Luật nói (claim-risk):** "80% on paper" ≠ PMI đã gỡ (gỡ theo giá trị do bên cho vay: thẩm định, thời gian tối thiểu, thường 75% những năm đầu). Không khuyên mua/chờ. Không dự báo. "History, not a forecast" cho mọi dòng `history`. Người mua và ví dụ $400,000 là ILLUSTRATIVE. Không nêu phí PMI (không nguồn).

| Claim ID | Giá trị | Hiển thị | Định nghĩa | Nguồn | Ghi chú |
|---|---|---|---|---|---|
| `rate_month_latest` | 2026-09-01 | September 2026 | latest complete calendar month of weekly PMMS (next weekly date falls in a later month) | data/raw/MORTGAGE30US.csv |  |
| `rate_latest` | 6.862 | 6.86% | mean of the 4 weekly rates dated 2026-09 | data/raw/MORTGAGE30US.csv |  |
| `rate_partial` | 7.28 | 7.28% (1 week) | 2026-10-01 single week; NOT used (incomplete month) | data/raw/MORTGAGE30US.csv | context only |
| `sched80_months_latest` | 99 | 99 payments (~8 years) | first k with B_k ≤ 0.80 of price at rate_latest; 90% loan, 360-mo level payment | data/raw/MORTGAGE30US.csv |  |
| `sched78_months_latest` | 114 | 114 payments (9.5 years) | first k with B_k ≤ 0.78 | data/raw/MORTGAGE30US.csv |  |
| `midpoint_months` | 180 | 15 years (ends month 181) | 12 U.S.C. 4902(c): PMI may not be required past the 1st day of the month after the amortization midpoint (if current); stated rule | sources.json provisions | rule |
| `midpoint_binding_rate_min` | 12.56 | 12.56% | lowest monthly rate (1971+) at which the 78% schedule falls after month 180 (midpoint binds); last such month May 1985 | data/raw/MORTGAGE30US.csv | history |
| `sched80_min_A / max_A` | 58 / 132 | 58–132 payments | 80% schedule over set A purchase-month rates (2.68%–9.64%) | data/raw/MORTGAGE30US.csv | history |
| `nA` | 403 | 403 purchase months | set A: purchase months 1991-01..2024-07 with 24 later index months | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv |  |
| `shareA_ltv24_le80` | 0.586 | 58.6% | set A share with B_24/(H[t+24]/H[t]) ≤ 0.80 | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv | history |
| `shareA_ltv24_le75` | 0.156 | 15.6% | same, ≤ 0.75 (lender early-year rule) | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv | history |
| `nB` | 307 | 307 purchase months | set B: 1991-01..2016-07, >120 later index months | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv |  |
| `medianB_months_to80` | 23 | 23 months | median over set B of first k with index LTV ≤ 0.80 | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv | history |
| `minB_months_to80` | 13 | 13 months | fastest in set B | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv | history |
| `shareB_over60` | 0.147 | 14.7% (about 1 in 7) | set B share with first k > 60 | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv | history |
| `maxB_months_to80` | 112 | 112 months (9 yr 4 mo) | set B worst first k | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv | history |
| `maxB_start` | 2005-10-01 | October 2005 | purchase month of maxB (earliest on ties) | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv | history |
| `shareB_le_sched80` | 0.906 | 90.6% | set B share where index reached 80% no later than the schedule at that month's rate | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv | history |
| `buyer_fast_*` | 2004-01-01 | Nora: bought January 2004 at 5.71%; 80% on paper after 13 months (schedule: 86) | set B month; fast = min T (ties → latest year), typical = T = median (latest such month), slow = max T. Index change to that month +11.2%; LTV at 24 mo 0.725 | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv | ILLUSTRATIVE, history |
| `buyer_typical_*` | 2014-06-01 | Ben: bought June 2014 at 4.16%; 80% on paper after 23 months (schedule: 71) | set B month; fast = min T (ties → latest year), typical = T = median (latest such month), slow = max T. Index change to that month +9.8%; LTV at 24 mo 0.784 | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv | ILLUSTRATIVE, history |
| `buyer_slow_*` | 2005-10-01 | Carla: bought October 2005 at 6.07%; 80% on paper after 112 months (schedule: 90) | set B month; fast = min T (ties → latest year), typical = T = median (latest such month), slow = max T. Index change to that month -3.3%; LTV at 24 mo 0.867 | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv | ILLUSTRATIVE, history |
| `mspus_latest` | 410700.0 | $410,700 (Q2 2026) | FRED MSPUS, 2026-04-01 (quarterly median sales price) | data/raw/MSPUS.csv | justifies ex_price |
| `ex_price` | 400000 | $400,000 | illustrative price, MSPUS rounded down to a round number | param | ILLUSTRATIVE |
| `ex_loan` | 360000.0 | $360,000 | 0.90 × ex_price (down payment $40,000) | param | ILLUSTRATIVE |
| `ex_payment_pi` | 2361.94 | $2,362/month | level principal+interest, 360 months at rate_latest (no taxes, insurance, PMI) | data/raw/MORTGAGE30US.csv | ILLUSTRATIVE |
| `ex_target80 / ex_target78` | 320000 / 312000 | $320,000 / $312,000 | 0.80 / 0.78 × ex_price; reached at payment 99 / 114 | param | ILLUSTRATIVE |
| `ex_extra_down_for_20` | 40000 | $40,000 more | 20% − 10% of ex_price (what waiting for 20% means in cash) | param | ILLUSTRATIVE |
| `pmi_premium` | none | — | No PMI premium amount: no cited source; the episode states none | — | not modeled |
| `robust_cs_medianB / maxB` | 23 / 119 (2006-04-01) | not for screen | same method on Case-Shiller national NSA (crosscheck); shareB_over60 0.147, shareA ≤80 0.561, ≤75 0.233 | data/raw/CSUSHPINSA.csv | robustness |

Tên người mua (Nora / Ben / Carla) là gợi ý, chọn cuối ở C1 (kiểm ASR). Cả ba thuộc tập B. Nora (1/2004) và Carla (10/2005) mua cách nhau 21 tháng: điểm "thời điểm mua" của tập.
