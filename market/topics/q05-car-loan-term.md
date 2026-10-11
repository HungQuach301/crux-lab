# Hồ sơ cầu — 60 vs 72 Months on a $35,000 Car Loan

Đề tài: dòng #5 trong `topics/queue.md` · id `q05-car-loan-term` · **Làm mới: 2026-10-11** (làm lại khi > 30 ngày, `playbook/episode.md` §1b.1).
Sinh bằng `python3 toolkit/market/report.py topics` từ `~/market-cache/` (ngoài git). Không số liệu thô; nhãn và chỉ số **tự tính, không phải chỉ số YouTube**. Câu hỏi, hoàn cảnh, điểm yếu: Haiku tóm từ bình luận đã lọc (diễn đạt lại, không trích nguyên văn) — máy viết, có thể sai.

| Mục | Nhãn | Cách tính (tự tính) |
|---|---|---|
| Mức cầu (trừ thời sự) | **vừa** | trung vị lượt xem/ngày của 10 video gắn đề tài mạnh nhất (≤ 24 tháng, bỏ video cờ thời sự), chia ba bậc trên 21 đề tài |
| Khoảng trống | **cao** | video đầu bảng có phát lại dữ liệu lịch sử thật không: cao = không video nào, vừa = 1, thấp = ≥ 2 (Haiku đọc tiêu đề + mô tả) |
| Số video gắn đề tài | vừa | embeddings, chỉ cặp khớp cao (cosine ≥ 0.55, biên ≥ 0.04) |
| Dải thời lượng | 10–13 phút | tứ phân vị 25–75 % của video đầu bảng cùng đề tài, làm tròn ra phút nguyên |

## Câu hỏi khán giả (SUY TỪ ĐỀ TÀI — chưa có bình luận đã lọc cho đề tài này; trọng số là ước của máy, làm mới ở Việc 0)
1. How much total interest does a 72-month loan cost compared with a 60-month loan on the same amount? — trọng số cao
2. What monthly payment can I comfortably afford on my income once insurance, fuel, and maintenance are included? — trọng số cao
3. Is a longer loan term ever worth it to keep the monthly payment low, and when does it become a trap? — trọng số cao
4. How do I work out the price of a car I can afford using a simple rule based on salary or take-home pay? — trọng số vừa
5. Will I owe more than the car is worth for most of a long loan, and how does that affect trading or refinancing? — trọng số vừa

_Ghi chú máy: No audience comments were provided, so all questions, situations, weaknesses, and requests are inferred from the topic and the video titles. Weights are estimates, not measured frequencies._

## Ba hoàn cảnh điển hình (tổng hợp, không phải người thật — nhân vật dẫn đường dựng từ đây, vẫn ILLUSTRATIVE)
- A first-time buyer with a steady salary who is choosing between a 60-month and a 72-month payment that fits a monthly budget but stretches the total cost.
- A household already stretched by rent or a mortgage that wants to add a second car and is tempted by the lowest possible monthly payment.
- A borrower a year into a 72-month loan who wants to know whether to refinance, pay extra, or keep going, and how much equity they have.

## Điểm yếu đối thủ (khán giả phàn nàn / máy thấy)
- Frequently skips the total-cost comparison and focuses on the monthly payment alone, which leaves the true price unclear.
- Often assumes a single affordability rule of thumb without showing how insurance, fuel, and maintenance change the result for different incomes.
- Likely to present the math without a worked example using realistic interest rates and an actual payoff schedule, so viewers cannot check it themselves.
- Phương pháp của 6 video đầu bảng: 6 giả định cố định.

## Video đối thủ theo tập (đầu bảng theo lượt xem; liên kết để WRITER/REVIEWER xem, không chép)

| Kênh | Video | Thời lượng | Phương pháp |
|---|---|---|---|
| Velocity Channel | [JW6UzQDzwRk](https://youtu.be/JW6UzQDzwRk) | 10–15 phút | giả định cố định |
| Honest Finance | [wr5lf_7HB60](https://youtu.be/wr5lf_7HB60) | 5–10 phút | giả định cố định |
| The Dog Kaisetsu | [6gm_fBvUN-E](https://youtu.be/6gm_fBvUN-E) | 10–15 phút | giả định cố định |
| Joe Invests | [aeNSXwkO0wY](https://youtu.be/aeNSXwkO0wY) | 10–15 phút | giả định cố định |
| Finance Flow | [Rz4517v4aRA](https://youtu.be/Rz4517v4aRA) | 15–20 phút | giả định cố định |

## Video vượt trội cùng đề tài (cho dòng G1)

- chưa có video vượt trội ≥ 3× (không thời sự) gắn chắc vào đề tài này trong các kênh đã kéo

## Mẫu tiêu đề (khuôn trừu tượng, không chép) và thumbnail
- X vs Y: Which Costs More Over N Years?
- How Much Can You Afford on a Salary of $X? (Full Breakdown)
- The Hidden Cost of Stretching a Loan from N to M Months
- Thumbnail: theo mẫu thắng chung ở `market/REPORT.md` §3 (đề tài này chưa đủ mẫu riêng).

## Từ khoá mô tả
car loan term length, 72 month car loan, how much car can I afford, auto loan interest calculator, car payment budget, negative equity car loan
