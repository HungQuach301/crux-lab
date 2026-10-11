# Hồ sơ cầu — 1-Year CD Pays More Than a 5-Year: Roll or Lock?

Đề tài: dòng #10 trong `topics/queue.md` · id `q10-cd-ladder` · **Làm mới: 2026-10-11** (làm lại khi > 30 ngày, `playbook/episode.md` §1b.1).
Sinh bằng `python3 toolkit/market/report.py topics` từ `~/market-cache/` (ngoài git). Không số liệu thô; nhãn và chỉ số **tự tính, không phải chỉ số YouTube**. Câu hỏi, hoàn cảnh, điểm yếu: Haiku tóm từ bình luận đã lọc (diễn đạt lại, không trích nguyên văn) — máy viết, có thể sai.

| Mục | Nhãn | Cách tính (tự tính) |
|---|---|---|
| Mức cầu (trừ thời sự) | **thấp** | trung vị lượt xem/ngày của 10 video gắn đề tài mạnh nhất (≤ 24 tháng, bỏ video cờ thời sự), chia ba bậc trên 21 đề tài |
| Khoảng trống | **cao** | video đầu bảng có phát lại dữ liệu lịch sử thật không: cao = không video nào, vừa = 1, thấp = ≥ 2 (Haiku đọc tiêu đề + mô tả) |
| Số video gắn đề tài | vừa | embeddings, chỉ cặp khớp cao (cosine ≥ 0.55, biên ≥ 0.04) |
| Dải thời lượng | 14:42–16:24 | tứ phân vị 25–75 % của video đầu bảng cùng đề tài |

## Câu hỏi khán giả (xếp theo trọng số: like + 2 × phản hồi, tự tính)
1. Which cash vehicle pays the most right now: T-bills, CDs, high-yield savings, or money market funds, and how do the rankings shift after a rate hike? — trọng số cao
2. Why not buy T-bills directly through TreasuryDirect and build a ladder instead of paying for an ETF or fund? — trọng số cao
3. How do state and federal taxes change the ranking, and when do munis or T-bill ETFs beat taxable options? — trọng số vừa
4. Is it worth locking a 1-year or 5-year CD now, or is a rolling short-term ladder better if rates keep moving? — trọng số vừa
5. Does the comparison account for share price changes and dividend reinvestment when the alternative is an equity income fund like SCHD? — trọng số thấp

## Ba hoàn cảnh điển hình (tổng hợp, không phải người thật — nhân vật dẫn đường dựng từ đây, vẫn ILLUSTRATIVE)
- A saver with $10,000 in cash buys a 12-month CD each month so that one CD matures each month and the money stays liquid.
- A taxable-account investor in a high-income-tax state holds a T-bill ETF and weighs it against a municipal money market fund and a bond ETF.
- A retiree with a large lump sum compares locking a multi-year CD against manually rolling four-week T-bills, and asks whether the hassle is worth the extra yield.

## Điểm yếu đối thủ (khán giả phàn nàn / máy thấy)
- Ignores state income tax exemption on Treasury interest, which changes the ranking for viewers in high-tax states such as California.
- Leaves out the most recent 26- and 52-week T-bill auction rates, which viewers say matter more than the funds discussed.
- Uses an unrealistic $400,000 lump-sum premise and treats SCHD as a yield play, ignoring price appreciation and dividend reinvestment.
- Phương pháp của 6 video đầu bảng: 3 ý kiến, không tính, 3 giả định cố định.

## Video đối thủ theo tập (đầu bảng theo lượt xem; liên kết để WRITER/REVIEWER xem, không chép)

| Kênh | Video | Thời lượng | Phương pháp |
|---|---|---|---|
| Rob Berger | [BkHhGbtb2EM](https://youtu.be/BkHhGbtb2EM) | 15:48 | ý kiến, không tính |
| Dividend Hustle Mark | [bN_KMvvItrI](https://youtu.be/bN_KMvvItrI) | 18:12 | giả định cố định |
| Dividend Hustle Mark | [B18i-RrxQpg](https://youtu.be/B18i-RrxQpg) | 14:42 | giả định cố định |
| Dividend Hustle Mark | [38XFfYhfYUg](https://youtu.be/38XFfYhfYUg) | 16:24 | giả định cố định |
| The Algorithm Investor | [xEyXGHjs0TQ](https://youtu.be/xEyXGHjs0TQ) | 10:18 | ý kiến, không tính |

## Video vượt trội cùng đề tài (cho dòng G1)

- chưa có video vượt trội ≥ 3× (không thời sự) gắn chắc vào đề tài này trong các kênh đã kéo

## Mẫu tiêu đề (khuôn trừu tượng, không chép) và thumbnail
- [Instrument A] vs [Instrument B]: Which Pays More After Tax Over [N] Months?
- Ladder or Lock? What [Cash Vehicle] Earns Over [N] Years When Rates Move
- Build a [N]-Rung [Cash Product] Ladder: Liquidity vs Yield at [Rate Level]
- Thumbnail: theo mẫu thắng chung ở `market/REPORT.md` §3 (đề tài này chưa đủ mẫu riêng).

## Từ khoá mô tả
CD ladder, T-bills vs CDs, high yield savings rates, TreasuryDirect ladder, after-tax cash yield, money market vs T-bill ETF

## Đề tài khán giả yêu cầu (→ hàng đợi nhãn "từ khán giả" nếu chưa có)
- Step-by-step TreasuryDirect T-bill ladder build, including reinvestment and reimbursement timing
- After-tax comparison of T-bills, CDs, money market funds, and municipal bond funds across federal and state brackets
- Comparison of floating-rate Treasury ETFs against CDs and T-bills for cash in a rising-rate environment
- Monthly CD ladder walkthrough showing how to keep one maturity per month
