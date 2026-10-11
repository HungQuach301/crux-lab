# Hồ sơ cầu — $1,000 Emergency: Tap the 401(k) or Use the Card?

Đề tài: dòng #15 trong `topics/queue.md` · id `q15-401k-vs-card` · **Làm mới: 2026-10-11** (làm lại khi > 30 ngày, `playbook/episode.md` §1b.1).
Sinh bằng `python3 toolkit/market/report.py topics` từ `~/market-cache/` (ngoài git). Không số liệu thô; nhãn và chỉ số **tự tính, không phải chỉ số YouTube**. Câu hỏi, hoàn cảnh, điểm yếu: Haiku tóm từ bình luận đã lọc (diễn đạt lại, không trích nguyên văn) — máy viết, có thể sai.

| Mục | Nhãn | Cách tính (tự tính) |
|---|---|---|
| Mức cầu (trừ thời sự) | **vừa** | trung vị lượt xem/ngày của 10 video gắn đề tài mạnh nhất (≤ 24 tháng, bỏ video cờ thời sự), chia ba bậc trên 21 đề tài |
| Khoảng trống | **cao** | video đầu bảng có phát lại dữ liệu lịch sử thật không: cao = không video nào, vừa = 1, thấp = ≥ 2 (Haiku đọc tiêu đề + mô tả) |
| Số video gắn đề tài | vừa | embeddings, chỉ cặp khớp cao (cosine ≥ 0.55, biên ≥ 0.04) |
| Dải thời lượng | 7–18 phút | tứ phân vị 25–75 % của video đầu bảng cùng đề tài, làm tròn ra phút nguyên |

## Câu hỏi khán giả (xếp theo trọng số: like + 2 × phản hồi, tự tính)
1. When does borrowing from a 401(k) beat tapping the emergency fund or carrying credit card debt, and what does each option really cost in interest, taxes, and lost growth? — trọng số cao
2. What happens to the account if you leave or lose your job while a 401(k) loan is outstanding, and how fast must it be repaid? — trọng số cao
3. How does a 401(k) hardship withdrawal differ from a loan in taxes, penalties, and repayment, and when is each one actually allowed? — trọng số cao
4. Does a 401(k) loan hurt employer matching contributions or long-term compounding while it is being repaid? — trọng số vừa
5. Where should a true emergency fund live (high-yield savings, money market, Roth contributions), and how does that compare to revolving card debt at high APRs? — trọng số vừa

_Ghi chú máy: Only vài short comments were provided, mostly about vài(k) loans for home purchases and debt payoff. Hardship withdrawals and emergency-fund placement have little direct audience signal, so those items are inferred from the topic and video titles._

## Ba hoàn cảnh điển hình (tổng hợp, không phải người thật — nhân vật dẫn đường dựng từ đây, vẫn ILLUSTRATIVE)
- A household with a $1,000 car repair and a credit card balance at a high APR, weighing whether to pay with the card, drain savings, or borrow from the 401(k).
- A worker in their 30s who recently changed jobs and wants to know whether a 401(k) loan from the old employer is still safe to take or repay.
- A late-career saver close to 59.5 with a mortgage at a mid-6% rate considering whether a 401(k) loan could replace mortgage payments.

## Điểm yếu đối thủ (khán giả phàn nàn / máy thấy)
- Advice often treats all 401(k) loans as either always good or always terrible, without weighing the borrower's job stability and cash-flow situation.
- Comparisons tend to ignore the tax double-taxation point on loan repayments and the lost market growth during the loan period.
- Few videos give a concrete, numeric side-by-side of hardship withdrawal, loan, emergency fund, and card debt for the same $1,000 need.
- Phương pháp của 6 video đầu bảng: 4 ý kiến, không tính, 2 giả định cố định.

## Video đối thủ theo tập (đầu bảng theo lượt xem; liên kết để WRITER/REVIEWER xem, không chép)

| Kênh | Video | Thời lượng | Phương pháp |
|---|---|---|---|
| Holy Schmidt! | [FqS9sI8N1oI](https://youtu.be/FqS9sI8N1oI) | 15–20 phút | ý kiến, không tính |
| Money With Britt  | [L8M9ri_FMAg](https://youtu.be/L8M9ri_FMAg) | 5–10 phút | ý kiến, không tính |
| Debra's Money Journey | [5c5jthMEKmw](https://youtu.be/5c5jthMEKmw) | 15–20 phút | ý kiến, không tính |
| Mitlin Financial Inc® | [zmgnrV9EGjk](https://youtu.be/zmgnrV9EGjk) | 5–10 phút | giả định cố định |
| The Wealth Workshop | [f2BpN0ody_o](https://youtu.be/f2BpN0ody_o) | 5–10 phút | ý kiến, không tính |

## Video vượt trội cùng đề tài (cho dòng G1)

- chưa có video vượt trội ≥ 3× (không thời sự) gắn chắc vào đề tài này trong các kênh đã kéo

## Mẫu tiêu đề (khuôn trừu tượng, không chép) và thumbnail
- 401(k) Loan vs Credit Card: Which Costs More for a $X Emergency Over N Years?
- Emergency Fund vs Hardship Withdrawal: What Each Choice Really Costs
- Job Change With a 401(k) Loan: What Happens and What to Do Before the Deadline
- Thumbnail: theo mẫu thắng chung ở `market/REPORT.md` §3 (đề tài này chưa đủ mẫu riêng).

## Từ khoá mô tả
401k loan, 401k hardship withdrawal, emergency fund, credit card debt, emergency savings, retirement account borrowing

## Đề tài khán giả yêu cầu (→ hàng đợi nhãn "từ khán giả" nếu chưa có)
- A worked example comparing a 401(k) loan, a hardship withdrawal, and card debt for the same $1,000 expense over several years.
- A walkthrough of what happens to a 401(k) loan if you change jobs, including rollover and repayment deadlines.
