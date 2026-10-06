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
| `midpoint_binding_rate_min` | 12.56 | 12.56% | lowest observed monthly rate (1971+, August 1980) at which the 78% schedule falls after month 180 (midpoint binds; smooth threshold ≈ 12.544%); last such month May 1985 | data/raw/MORTGAGE30US.csv | history |
| `sched80_min_A / max_A` | 58 / 132 | 58–132 payments | 80% schedule over set A purchase-month rates (2.68%–9.64%) | data/raw/MORTGAGE30US.csv | history |
| `nA` | 403 | 403 purchase months | set A: purchase months 1991-01..2024-07 with 24 later index months | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv |  |
| `shareA_ltv24_le80` | 0.586 | 58.6% | set A share with B_24/(H[t+24]/H[t]) ≤ 0.80 | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv | history |
| `shareA_ltv24_le75` | 0.156 | 15.6% | same, ≤ 0.75 (lender early-year rule, see value_removal_ltv_early) | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv | history |
| `nB` | 307 | 307 purchase months | set B: 1991-01..2016-07, ≥ 120 later index months (2016-07 has exactly 120) | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv |  |
| `medianB_months_to80` | 23 | 23 months | median over set B of first k with index LTV ≤ 0.80 | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv | history |
| `minB_months_to80` | 13 | 13 months | fastest in set B | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv | history |
| `shareB_over60` | 0.147 | 14.7% (about 1 in 7) | set B share with first k > 60 | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv | history |
| `maxB_months_to80` | 112 | 112 months (9 yr 4 mo) | set B worst first k | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv | history |
| `maxB_start` | 2005-10-01 | October 2005 | purchase month of maxB (earliest on ties) | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv | history |
| `shareB_le_sched80` | 0.906 | 90.6% | set B share where index reached 80% no later than the schedule at that month's rate | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv | history |
| `buyer_fast_*` | 2004-01-01 | Nora: bought January 2004 at 5.71%; 80% on paper after 13 months (schedule: 86) | set B month; fast = min T (ties → latest calendar year, then earliest month in that year; 10 months tie at 13: 2003-06 and 2004-01…2004-09), typical = T = median (latest such month), slow = max T. Index change to that month +11.2%; LTV at 24 mo 0.725 | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv | ILLUSTRATIVE, history |
| `buyer_typical_*` | 2014-06-01 | Ben: bought June 2014 at 4.16%; 80% on paper after 23 months (schedule: 71) | set B month; fast = min T (ties → latest calendar year, then earliest month in that year; 10 months tie at 13: 2003-06 and 2004-01…2004-09), typical = T = median (latest such month), slow = max T. Index change to that month +9.8%; LTV at 24 mo 0.784 | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv | ILLUSTRATIVE, history |
| `buyer_slow_*` | 2005-10-01 | Carla: bought October 2005 at 6.07%; 80% on paper after 112 months (schedule: 90) | set B month; fast = min T (ties → latest calendar year, then earliest month in that year; 10 months tie at 13: 2003-06 and 2004-01…2004-09), typical = T = median (latest such month), slow = max T. Index change to that month -3.3%; LTV at 24 mo 0.867 | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv | ILLUSTRATIVE, history |
| `mspus_latest` | 410700.0 | $410,700 (Q2 2026) | FRED MSPUS, 2026-04-01 (quarterly median sales price) | data/raw/MSPUS.csv | justifies ex_price |
| `ex_price` | 400000 | $400,000 | illustrative price, MSPUS rounded down to a round number | param | ILLUSTRATIVE |
| `ex_loan` | 360000.0 | $360,000 | 0.90 × ex_price (down payment $40,000) | param | ILLUSTRATIVE |
| `ex_payment_pi` | 2361.94 | $2,362/month | level principal+interest, 360 months at rate_latest (no taxes, insurance, PMI) | data/raw/MORTGAGE30US.csv | ILLUSTRATIVE |
| `ex_target80 / ex_target78` | 320000 / 312000 | $320,000 / $312,000 | 0.80 / 0.78 × ex_price; reached at payment 99 / 114 | param | ILLUSTRATIVE |
| `ex_extra_down_for_20` | 40000 | $40,000 more | 20% − 10% of ex_price (what waiting for 20% means in cash) | param | ILLUSTRATIVE |
| `pmi_premium` | none | — | No PMI premium amount: no cited source; the episode states none | — | not modeled |
| `pmi_required_below20` | 0.80 | PMI usually required under 20% down | conventional loan with down payment < 20% (LTV > 80%) usually carries PMI: CFPB "Lenders generally require consumers to purchase PMI if their down payment is less than 20 percent"; GSE charters bar buying conventional 1–4 unit loans over 80% of value without credit enhancement (e.g. insurance) | sources.json provisions (CFPB en-122, CFPB 2015-08-04 release, 12 U.S.C. 1717(b)(2), 1454(a)(2)) | rule |
| `borrower_request_conditions` | 4 conditions | written request, good history, current, value not below original (if holder asks) + no subordinate lien | 12 U.S.C. 4902(a)(1)–(4): conditions on borrower-requested cancellation at the 80% (original value, schedule) date | sources.json provisions (12 U.S.C. 4902(a)) | rule |
| `value_removal_rule` | lender/investor rule | removal on current value = lender's/investor's own standard | not a federal right: CFPB "Some lenders and servicers may allow removal of PMI under their own standards" / "Loan investors, including Fannie Mae and Freddie Mac, often create their own PMI cancellation guidelines" | sources.json provisions (CFPB en-202) | rule |
| `value_removal_ltv_early` | 0.75 | 75 percent (current value, early years) | investor current-value termination: LTV ≤ 75% of current value when seasoned 2–5 years (≤ 80% after 5 years); appraisal/BPO, payment history (Fannie Mae Servicing Guide B-8.1-04; Freddie Mac 8203.2) | **PENDING verbatim**: fanniemae.com / freddiemac.com blocked 2026-10-06 (sources.json provisions, status NOT RETRIEVED); = param lenderLtvEarly | rule; unverified quote |
| `value_removal_seasoning_years` | 2 | at least 2 years (minimum wait) | minimum seasoning before current-value termination at ≤ 75%; ≤ 80% after 5 years (same guides) | **PENDING verbatim** (as above) | rule; unverified quote |
| `slowB_n` | 45 | 45 purchase months (= shareB_over60 × nB) | set B months with first k > 60 | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv | history |
| `slowB_years` | 2005–2009 | purchases from 2005 through 2009 | purchase years of all slowB months; first slowB_first 2005-05-01, last slowB_last 2009-02-01 (contiguous: none before 2005-05 or after 2009-02) | data/raw/HPIPONM226N.csv + data/raw/MORTGAGE30US.csv | history |
| `hpi_peak_month` | 2007-06-01 | June 2007 (index 226.0) | max HPIPONM226N before 2012 (national pre-slump peak) | data/raw/HPIPONM226N.csv | history |
| `hpi_trough_month` | 2012-01-01 | January 2012 (index 175.8, −22.2% from peak) | min HPIPONM226N after hpi_peak_month, before 2015 (slump low); slowB months run from 25 months before the peak into the decline | data/raw/HPIPONM226N.csv | history |
| `buyer_slow_index_peak` | 0.0433 | +4.3% at month 20 (June 2007) | slow buyer (2005-10): max of H[t+k]/H[t]−1 over k = 1..112 (to month reaching 80% on paper) | data/raw/HPIPONM226N.csv | history, ILLUSTRATIVE |
| `buyer_slow_index_trough` | −0.1885 | −18.8% at month 75 (January 2012) | slow buyer (2005-10): min of H[t+k]/H[t]−1 over k = 1..112; at month 112 still −3.3% | data/raw/HPIPONM226N.csv | history, ILLUSTRATIVE |
| `robust_cs_medianB / maxB` | 23 / 119 (2006-04-01) | not for screen | same method on Case-Shiller national NSA (crosscheck); shareB_over60 0.147, shareA ≤80 0.561, ≤75 0.233 | data/raw/CSUSHPINSA.csv | robustness |

Tên người mua (Nora / Ben / Carla) là gợi ý, chọn cuối ở C1 (kiểm ASR). Cả ba thuộc tập B. Nora (1/2004) và Carla (10/2005) mua cách nhau 21 tháng: điểm "thời điểm mua" của tập.
