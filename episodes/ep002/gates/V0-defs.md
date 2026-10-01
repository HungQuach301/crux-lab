# V0 — Định nghĩa mô hình và dung sai kiểm độc lập (ghi TRƯỚC khi chạy kiểm, không sửa sau)

Ngày 2026-10-01. Người kiểm: một agent con MỚI, không đọc `calc.py` hay `model/model.py`, chỉ đọc file định nghĩa trong thư mục tạm và `TB3MS.csv`.

## Dung sai (ghi trước)
- Ngày: so sau chuẩn hoá `YYYY-MM` ≡ `YYYY-MM-01`. Khác chỉ ở cách viết → ghi ledger, không là lỗi số.
- Số đếm (số tháng bắt đầu): khớp tuyệt đối.
- Đô la làm tròn tới đô: |lệch| ≤ 1.
- Đô la làm tròn tới cent (khoản trả hàng tháng): |lệch| ≤ 0,01.
- Phần trăm làm tròn 0,1: |lệch| ≤ 0,1 **và** nếu lệch ≠ 0 thì phải truy ra là do làm tròn ở mép (giá trị chưa làm tròn ±0,05 quanh mép); ngược lại là lỗi.
- Lãi suất làm tròn 0,01: |lệch| ≤ 0,01.
- Chuỗi 753 cửa sổ (`windows[].diff`): |lệch| ≤ 0,05 đô mỗi cửa sổ; dấu (đắt hơn/rẻ hơn) phải trùng 753/753.

## Định nghĩa lõi (nguyên văn từ `topics-r1/machine/debt-2/result.json`)
Data: TB3MS.csv (FRED TB3MS, 3-Month Treasury Bill Secondary Market Rate, Discount Basis, monthly, percent), 1934-01 through 2026-08 (last value 3.72). Loan: $50,000, 120 monthly payments, interest = balance*rate/1200 each month; the payment is recomputed as the level payment over the remaining months whenever the rate changes (month k=0..119, remaining = 120-k). Fixed loan: 9.00% all 120 months. Variable loan for a start month s: rate_k = 3.78 + max(0, 3.72 + TB3MS[s+k] - TB3MS[s]) (3.72 = latest TB3MS, 3.78 = 7.50 - 3.72, so rate_0 = 7.50 and the index cannot go below zero), unrounded. Start months s: every month from 1954-01 through 2016-09 (last start with 120 months of data). Difference = total variable interest - total fixed interest over the 120 months.

Đại lượng lõi: n_starts; first_start; last_start; fixed_total_interest (round $); share_variable_costlier (% start months with Difference > 0, round 0.1); median_variable_minus_fixed (round $); worst_variable_minus_fixed (max Difference, round $); worst_start; best_variable_minus_fixed (min, round $); max_variable_rate_any_window (round 0.01); n_starts_1954_1980 (1954-01..1980-12); share_costlier_1954_1980; n_starts_1981_on (1981-01..2016-09); share_costlier_1981_on; index_today; margin.

## Định nghĩa mở rộng — phạm vi (b) (viết mới cho Tập 2)
Cùng khoản vay, cùng cửa sổ, cùng cách tính lại khoản trả.
- **Payments.** fixed_payment = level payment of $50,000 at 9.00% over 120 months (round cents). variable_first_payment = payment in month 0 at 7.50% (round cents). For each window, maxPay = highest monthly payment of the variable loan over its 120 months. max_variable_payment_any_window = max of maxPay over the 753 windows (round cents) and its start month; median_window_max_payment = median over windows of maxPay (round cents); share_windows_max_payment_above_fixed = % of windows with maxPay > fixed_payment (round 0.1).
- **Gap grid.** For g in {0.5, 1.0, 1.5, 2.0, 2.5, 3.0}: variable start rate v0 = 9.00 − g, margin = v0 − 3.72, path rate_k = margin + max(0, 3.72 + TB3MS[s+k] − TB3MS[s]); fixed stays 9.00. Report share_costlier (all, 1954–1980, 1981 on), median Difference, worst Difference and its start, best Difference.
- **Cap grid.** For cap c in {12, 15, 18} (percent): base path (v0 = 7.50) with rate_k = min(c, base rate_k). Same outputs as the gap grid.
- **Windows series.** For each of the 753 start months: Difference (round to cents), max rate, maxPay.
