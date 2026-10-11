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
1. Should I prepay my low-rate mortgage or invest the extra money instead? — trọng số cao
2. How do I make extra principal payments so they actually cut interest and shorten the loan? — trọng số cao
3. How can I remove PMI early, and does this strategy work with VA or FHA loans? — trọng số cao
4. Can an average household afford extra principal payments, or is this only realistic in cheaper housing markets? — trọng số vừa
5. Is a 15-year loan better than a 30-year loan I pay down early, and what does each cost monthly? — trọng số vừa

## Ba hoàn cảnh điển hình (tổng hợp, không phải người thật — nhân vật dẫn đường dựng từ đây, vẫn ILLUSTRATIVE)
- Mid-career homeowner with a 2.5% to 3.5% mortgage who prepays aggressively, then redirects the freed payment to investing or a leisure fund.
- Recent buyer with PMI whose home value rose after purchase, asking whether a lender reappraisal can remove PMI before 20% equity is reached.
- Veteran or military household on a VA or similar loan with no PMI, making large extra payments toward a debt-free retirement target.

## Điểm yếu đối thủ (khán giả phàn nàn / máy thấy)
- Ignores opportunity cost: commenters argue that investing or a high-yield savings account can beat prepaying a low-rate loan.
- Assumes viewers can afford large extra payments, which is unrealistic in high-cost markets like Southern California.
- Glosses over loan-type differences (FHA mortgage insurance rules, VA loans, flat amortization in some countries) and the risk of secured debt like HELOCs.
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
- [Strategy] vs [Alternative]: The Real Break-Even on a [Rate]% Loan
- I Paid Off My [Loan Type] in [N] Years: The Exact Monthly Math
- Should You Prepay a [Loan Type] or Invest? Honest Numbers for [Income Level]
- Thumbnail: theo mẫu thắng chung ở `market/REPORT.md` §3 (đề tài này chưa đủ mẫu riêng).

## Từ khoá mô tả
extra mortgage principal payments, prepay mortgage vs invest, remove PMI early reappraisal, how to pay off mortgage early, VA loan extra payments, mortgage payoff calculator

## Đề tài khán giả yêu cầu (→ hàng đợi nhãn "từ khán giả" nếu chưa có)
- A follow-up video comparing investing and prepaying that includes cash flow, monthly bill coverage, and liquidity.
- A debt payoff order video covering credit cards first, then student loans.
- A detailed walkthrough of lump-sum yearly principal payments, including reamortization and whether to request a recast.
