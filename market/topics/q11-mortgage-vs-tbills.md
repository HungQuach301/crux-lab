# Hồ sơ cầu — 3% Mortgage vs T-Bills: Where Should the $500 Have Gone?

Đề tài: dòng #11 trong `topics/queue.md` · id `q11-mortgage-vs-tbills` · **Làm mới: 2026-10-11** (làm lại khi > 30 ngày, `playbook/episode.md` §1b.1).
Sinh bằng `python3 toolkit/market/report.py topics` từ `~/market-cache/` (ngoài git). Không số liệu thô; nhãn và chỉ số **tự tính, không phải chỉ số YouTube**. Câu hỏi, hoàn cảnh, điểm yếu: Haiku tóm từ bình luận đã lọc (diễn đạt lại, không trích nguyên văn) — máy viết, có thể sai.

| Mục | Nhãn | Cách tính (tự tính) |
|---|---|---|
| Mức cầu (trừ thời sự) | **cao** | trung vị lượt xem/ngày của 10 video gắn đề tài mạnh nhất (≤ 24 tháng, bỏ video cờ thời sự), chia ba bậc trên 21 đề tài |
| Khoảng trống | **thấp** | video đầu bảng có phát lại dữ liệu lịch sử thật không: cao = không video nào, vừa = 1, thấp = ≥ 2 (Haiku đọc tiêu đề + mô tả) |
| Số video gắn đề tài | cao | embeddings, chỉ cặp khớp cao (cosine ≥ 0.55, biên ≥ 0.04) |
| Dải thời lượng | 14–20 phút | tứ phân vị 25–75 % của video vượt trội cùng đề tài, làm tròn ra phút nguyên |

## Câu hỏi khán giả (xếp theo trọng số: like + 2 × phản hồi, tự tính)
1. Should I pay off my low-rate mortgage early or invest the money, and which option holds up better if I lose my job? — trọng số cao
2. Should I build a 6-12 month emergency fund before making extra mortgage payments? — trọng số cao
3. When I lose my job, should I sell all my investments or withdraw only what I need until I'm re-employed? — trọng số cao
4. Does a 3% mortgage still make sense to keep once I factor in inflation, the mortgage interest deduction, and the after-tax rate? — trọng số vừa
5. Would a hybrid approach, splitting extra money between payoff and investing, work better than choosing one strategy? — trọng số vừa

## Ba hoàn cảnh điển hình (tổng hợp, không phải người thật — nhân vật dẫn đường dựng từ đây, vẫn ILLUSTRATIVE)
- Mid-40s to 50s homeowner with 15-20 years left on a 30-year mortgage at 3-4%, splitting extra cash between investing and principal, and choosing based on peace of mind as much as the math.
- Single-income household that wants the house paid off for job-security reasons, possibly after a past layoff, and treats the payoff as protection against losing the home.
- Near-retirement household that has already paid off the mortgage and lives on pension or dividend income, weighing liquidity, taxes, and how withdrawals affect healthcare subsidies.

## Điểm yếu đối thủ (khán giả phàn nàn / máy thấy)
- Ignores liquidity risk and the emergency fund: home equity is illiquid, so the comparison leaves out what happens during a job loss or medical emergency.
- Oversimplifies taxes and inflation: it doesn't account for itemized mortgage interest deductions, non-deductible principal withdrawals in retirement, or how fixed payments lose real value over time.
- Uses fixed return assumptions and an incomplete time horizon, often leaving out rent avoided or saved, the spending of freed-up cash, and the effects of market volatility over the full loan term.
- Phương pháp của 6 video đầu bảng: 2 dữ liệu lịch sử thật, 3 giả định cố định, 1 ý kiến, không tính.

## Video đối thủ theo tập (đầu bảng theo lượt xem; liên kết để WRITER/REVIEWER xem, không chép)

| Kênh | Video | Thời lượng | Phương pháp |
|---|---|---|---|
| Erin Talks Money · Erin Moriarity | [cjFIFu7eI6k](https://youtu.be/cjFIFu7eI6k) | 20–30 phút | dữ liệu lịch sử thật |
| Home Loan Education | [jBhOfdzgy8E](https://youtu.be/jBhOfdzgy8E) | 15–20 phút | giả định cố định |
| Bob Sharpe | [rikT1MHdDYg](https://youtu.be/rikT1MHdDYg) | 15–20 phút | dữ liệu lịch sử thật |
| Home Loan Education | [8kSSRN2ooU4](https://youtu.be/8kSSRN2ooU4) | 15–20 phút | ý kiến, không tính |
| Bob Sharpe | [cavk66DEdOM](https://youtu.be/cavk66DEdOM) | 10–15 phút | giả định cố định |

## Video vượt trội cùng đề tài (cho dòng G1)

- Home Loan Education — [jBhOfdzgy8E](https://youtu.be/jBhOfdzgy8E) — 15–20 phút — ≥ 5× (tự tính)
- Home Loan Education — [8kSSRN2ooU4](https://youtu.be/8kSSRN2ooU4) — 15–20 phút — ≥ 5× (tự tính)
- Home Loan Education — [3hIh9xT1C1o](https://youtu.be/3hIh9xT1C1o) — 10–15 phút — ≥ 5× (tự tính)

## Mẫu tiêu đề (khuôn trừu tượng, không chép) và thumbnail
- X% Mortgage vs Y% Index Fund: Which Wins Over N Years?
- Pay Off the House or Build a Cash Cushion? A Job-Loss Scenario Explained
- The Break-Even Rate: When Prepaying Your Mortgage Beats Investing
- Thumbnail: theo mẫu thắng chung ở `market/REPORT.md` §3 (đề tài này chưa đủ mẫu riêng).

## Từ khoá mô tả
mortgage payoff vs investing, prepay mortgage early, low interest mortgage strategy, emergency fund before paying off mortgage, mortgage vs index fund returns, early mortgage payoff calculator

## Đề tài khán giả yêu cầu (→ hàng đợi nhãn "từ khán giả" nếu chưa có)
- A job-loss scenario that compares selling investments with withdrawing only what's needed until re-employment.
- A retirement-stage comparison covering taxes, ACA subsidies, and withdrawal planning after the mortgage is paid off.
- A break-even calculator or rate threshold showing when prepaying beats investing, based on the user's own rate and time horizon.
- A hybrid-strategy walkthrough that shows how to split extra money between prepayment and investing over time.
- A Canada-specific or mortgage-renewal explanation, since payments can change at each term renewal.
