# Hồ sơ cầu — Does a 2% Annuity Raise Really Keep Up With Prices?

Đề tài: dòng #12 trong `topics/queue.md` · id `q12-annuity-raise` · **Làm mới: 2026-10-11** (làm lại khi > 30 ngày, `playbook/episode.md` §1b.1).
Sinh bằng `python3 toolkit/market/report.py topics` từ `~/market-cache/` (ngoài git). Không số liệu thô; nhãn và chỉ số **tự tính, không phải chỉ số YouTube**. Câu hỏi, hoàn cảnh, điểm yếu: Haiku tóm từ bình luận đã lọc (diễn đạt lại, không trích nguyên văn) — máy viết, có thể sai.

| Mục | Nhãn | Cách tính (tự tính) |
|---|---|---|
| Mức cầu (trừ thời sự) | **vừa** | trung vị lượt xem/ngày của 10 video gắn đề tài mạnh nhất (≤ 24 tháng, bỏ video cờ thời sự), chia ba bậc trên 21 đề tài |
| Khoảng trống | **cao** | video đầu bảng có phát lại dữ liệu lịch sử thật không: cao = không video nào, vừa = 1, thấp = ≥ 2 (Haiku đọc tiêu đề + mô tả) |
| Số video gắn đề tài | vừa | embeddings, chỉ cặp khớp cao (cosine ≥ 0.55, biên ≥ 0.04) |
| Dải thời lượng | 8:48–14:18 | tứ phân vị 25–75 % của video đầu bảng cùng đề tài |

## Câu hỏi khán giả (xếp theo trọng số: like + 2 × phản hồi, tự tính)
1. Do annuity payouts actually beat bonds, Treasuries, or high-yield alternatives once you compare them on the same basis? — trọng số cao
2. Does a 2% COLA or inflation-adjusted annuity keep my purchasing power intact, and what does that protection cost? — trọng số cao
3. What happens to the money if I die early, and can heirs get any of it? — trọng số cao
4. How much do fees, surrender charges, caps, and seller commissions reduce what I actually receive? — trọng số vừa
5. How long do I need to live for an annuity to break even compared with investing and withdrawing on my own? — trọng số vừa

## Ba hoàn cảnh điển hình (tổng hợp, không phải người thật — nhân vật dẫn đường dựng từ đây, vẫn ILLUSTRATIVE)
- A 69-year-old with about $100k in a 401(k) and a similar amount in a Roth IRA is considering annuitizing half at 71 to get a simple, steady paycheck.
- A retiree whose late father bought an annuity that paid nothing to the family after death is now weighing whether to put part of a $300k portfolio into one.
- A 35-year-old plans to invest $40k a year and asks whether an annuity quoted at 8% would return the full amount paid in, and how that compares with index funds.

## Điểm yếu đối thủ (khán giả phàn nàn / máy thấy)
- Treats a quoted payout rate as if it were an interest rate or a total return, without explaining the difference.
- Headline payout figures ignore inflation, so later payments are presented without showing how much they will buy.
- Skips what happens at death, and does not disclose fees, surrender charges, caps, or the seller's commission.
- Phương pháp của 6 video đầu bảng: 4 giả định cố định, 1 ý kiến, không tính, 1 tin tức.

## Video đối thủ theo tập (đầu bảng theo lượt xem; liên kết để WRITER/REVIEWER xem, không chép)

| Kênh | Video | Thời lượng | Phương pháp |
|---|---|---|---|
| Nanalyze | [SIWaHTeSDSM](https://youtu.be/SIWaHTeSDSM) | 14:18 | giả định cố định |
| Diamond NestEgg | [qFuVEfm68ps](https://youtu.be/qFuVEfm68ps) | 19:48 | giả định cố định |
| Learning to Retire | [aX-RQJP8_IA](https://youtu.be/aX-RQJP8_IA) | 8:48 | giả định cố định |
| Stan The Annuity Man | [yFDgRQk6Wl8](https://youtu.be/yFDgRQk6Wl8) | 9:30 | ý kiến, không tính |
| Steve Larsen | [TSxVZprmHZE](https://youtu.be/TSxVZprmHZE) | 7:48 | giả định cố định |

## Video vượt trội cùng đề tài (cho dòng G1)

- chưa có video vượt trội ≥ 3× (không thời sự) gắn chắc vào đề tài này trong các kênh đã kéo

## Mẫu tiêu đề (khuôn trừu tượng, không chép) và thumbnail
- [Product] vs [Alternative]: Which Pays More After Inflation Over [N] Years?
- Will an Annuity Outlast You? Break-Even Math at Ages [X] vs [Y]
- What Happens to an Annuity When You Die? The [Heir Scenario] Explained
- Thumbnail: theo mẫu thắng chung ở `market/REPORT.md` §3 (đề tài này chưa đủ mẫu riêng).

## Từ khoá mô tả
income annuity inflation, annuity vs bond ladder, annuity COLA rider cost, annuity death benefit heirs, annuity break-even age

## Đề tài khán giả yêu cầu (→ hàng đợi nhãn "từ khán giả" nếu chưa có)
- Strategies for retirees with no heirs who want to spend down to zero safely
- A side-by-side comparison of annuities versus a bond or CD ladder, including taxes
- Break-even math showing how long you must live to come out ahead of the alternatives
- How annuity death benefits and beneficiary transfers work, including for a sole heir
- Whether it makes sense to buy an annuity while young versus later in retirement
