# Hồ sơ cầu — 15-Year Mortgage or a 30-Year Paid in 15?

Đề tài: dòng #13 trong `topics/queue.md` · id `q13-15-vs-30-mortgage` · **Làm mới: 2026-10-11** (làm lại khi > 30 ngày, `playbook/episode.md` §1b.1).
Sinh bằng `python3 toolkit/market/report.py topics` từ `~/market-cache/` (ngoài git). Không số liệu thô; nhãn và chỉ số **tự tính, không phải chỉ số YouTube**. Câu hỏi, hoàn cảnh, điểm yếu: Haiku tóm từ bình luận đã lọc (diễn đạt lại, không trích nguyên văn) — máy viết, có thể sai.

| Mục | Nhãn | Cách tính (tự tính) |
|---|---|---|
| Mức cầu (trừ thời sự) | **cao** | trung vị lượt xem/ngày của 10 video gắn đề tài mạnh nhất (≤ 24 tháng, bỏ video cờ thời sự), chia ba bậc trên 21 đề tài |
| Khoảng trống | **cao** | video đầu bảng có phát lại dữ liệu lịch sử thật không: cao = không video nào, vừa = 1, thấp = ≥ 2 (Haiku đọc tiêu đề + mô tả) |
| Số video gắn đề tài | cao | embeddings, chỉ cặp khớp cao (cosine ≥ 0.55, biên ≥ 0.04) |
| Dải thời lượng | 10–24 phút | tứ phân vị 25–75 % của video vượt trội cùng đề tài, làm tròn ra phút nguyên |

## Câu hỏi khán giả (xếp theo trọng số: like + 2 × phản hồi, tự tính)
1. Is it better to prepay the mortgage or invest the extra money, given the loan's interest rate and expected market returns? — trọng số cao
2. How much faster does a 30-year loan pay off with extra monthly principal, and how much payment increase is needed to hit a target payoff date? — trọng số cao
3. Does a yearly lump-sum principal payment work as well as steady monthly extra payments? — trọng số vừa
4. How can PMI be removed early through home value increases, reappraisal, or reaching 20% equity, and what are the steps? — trọng số vừa
5. Why does extra principal not lower the monthly interest charge right away, and when does reamortizing or recasting make sense? — trọng số vừa

## Ba hoàn cảnh điển hình (tổng hợp, không phải người thật — nhân vật dẫn đường dựng từ đây, vẫn ILLUSTRATIVE)
- A homeowner with a low fixed rate who has spare monthly cash, weighing whether to make extra principal payments, invest the difference, or keep reserves for a move or emergencies.
- A buyer in a high-cost metro area with a large monthly payment and little room in the budget, wondering whether a 15-year payoff is realistic and how to handle PMI or escrowed taxes first.
- A veteran or near-retiree with a VA or other government-backed loan who wants to be debt free before retiring, while still paying heavy state and local property taxes.

## Điểm yếu đối thủ (khán giả phàn nàn / máy thấy)
- Treats early payoff as the default best choice and gives little weight to opportunity cost, investment returns, or liquidity.
- Assumes viewers can easily afford large extra payments and rarely shows how to plan around tight budgets or high-cost housing.
- Glosses over differences between loan types (FHA mortgage insurance, VA rules), escrow, and property taxes, so the numbers may not apply to everyone.
- Phương pháp của 6 video đầu bảng: 6 giả định cố định.

## Video đối thủ theo tập (đầu bảng theo lượt xem; liên kết để WRITER/REVIEWER xem, không chép)

| Kênh | Video | Thời lượng | Phương pháp |
|---|---|---|---|
| Home Loan Education | [EbJAgIuORTg](https://youtu.be/EbJAgIuORTg) | 20–30 phút | giả định cố định |
| Bob Sharpe | [ittb9eOt46M](https://youtu.be/ittb9eOt46M) | 10–15 phút | giả định cố định |
| Home Loan Education | [9bTPEGduDww](https://youtu.be/9bTPEGduDww) | 20–30 phút | giả định cố định |
| Erin Talks Money · Erin Moriarity | [R_9DQ7KrQJc](https://youtu.be/R_9DQ7KrQJc) | 15–20 phút | giả định cố định |
| The Shred Method™ | [siRuke_ZlvI](https://youtu.be/siRuke_ZlvI) | 5–10 phút | giả định cố định |

## Video vượt trội cùng đề tài (cho dòng G1)

- Home Loan Education — [EbJAgIuORTg](https://youtu.be/EbJAgIuORTg) — 20–30 phút — ≥ 5× (tự tính)
- Home Loan Education — [9bTPEGduDww](https://youtu.be/9bTPEGduDww) — 20–30 phút — ≥ 5× (tự tính)
- Bob Sharpe — [ittb9eOt46M](https://youtu.be/ittb9eOt46M) — 10–15 phút — ≥ 5× (tự tính)

## Mẫu tiêu đề (khuôn trừu tượng, không chép) và thumbnail
- X vs Y: Which Costs More Over N Years?
- Paying Extra on a N-Year Loan: How Many Years Does It Really Save?
- Removing PMI Early: When It Works, When It Doesn't, and What It Costs
- Thumbnail: theo mẫu thắng chung ở `market/REPORT.md` §3 (đề tài này chưa đủ mẫu riêng).

## Từ khoá mô tả
15 year vs 30 year mortgage, extra mortgage principal payment, pay off mortgage early, prepay mortgage vs invest, remove PMI from mortgage, mortgage amortization schedule

## Đề tài khán giả yêu cầu (→ hàng đợi nhãn "từ khán giả" nếu chưa có)
- A video on whether to pay off credit cards and student loans before extra mortgage principal.
- A side-by-side comparison of investing versus prepaying that covers cash flow, monthly bill coverage, and the risk of tying up money in home equity.
- A follow-up video on the next strategy covered in the series.
