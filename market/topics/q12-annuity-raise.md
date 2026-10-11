# Hồ sơ cầu — Does a 2% Annuity Raise Really Keep Up With Prices?

Đề tài: dòng #12 trong `topics/queue.md` · id `q12-annuity-raise` · **Làm mới: 2026-10-11** (làm lại khi > 30 ngày, `playbook/episode.md` §1b.1).
Sinh bằng `python3 toolkit/market/report.py topics` từ `~/market-cache/` (ngoài git). Không số liệu thô; nhãn và chỉ số **tự tính, không phải chỉ số YouTube**. Câu hỏi, hoàn cảnh, điểm yếu: Haiku tóm từ bình luận đã lọc (diễn đạt lại, không trích nguyên văn) — máy viết, có thể sai.

| Mục | Nhãn | Cách tính (tự tính) |
|---|---|---|
| Mức cầu (trừ thời sự) | **vừa** | trung vị lượt xem/ngày của 10 video gắn đề tài mạnh nhất (≤ 24 tháng, bỏ video cờ thời sự), chia ba bậc trên 21 đề tài |
| Khoảng trống | **cao** | video đầu bảng có phát lại dữ liệu lịch sử thật không: cao = không video nào, vừa = 1, thấp = ≥ 2 (Haiku đọc tiêu đề + mô tả) |
| Số video gắn đề tài | vừa | embeddings, chỉ cặp khớp cao (cosine ≥ 0.55, biên ≥ 0.04) |
| Dải thời lượng | 8–15 phút | tứ phân vị 25–75 % của video đầu bảng cùng đề tài, làm tròn ra phút nguyên |

## Câu hỏi khán giả (xếp theo trọng số: like + 2 × phản hồi, tự tính)
1. Does a fixed annuity's guaranteed payout keep pace with inflation over a long retirement, and what does the real purchasing power look like after 10 to 20 years? — trọng số cao
2. How do annuity payout rates compare with safe alternatives like Treasuries, CDs, bond ladders, or high-yield savings, once fees, taxes, and risk are counted? — trọng số cao
3. What happens to the money at death: do heirs receive anything, and how do period-certain, refund, or cash-refund options change the trade-off? — trọng số cao
4. Which annuity type fits which situation: immediate income annuity, deferred annuity, fixed indexed, MYGA, or inflation-adjusted SPIA, and what do the inflation riders (COLA) actually cost? — trọng số vừa
5. How much can an insurer's failure or changing future rates affect an annuity, and how do state guaranty associations limit that risk? — trọng số vừa

_Ghi chú máy: Only a small set of comments was provided (mostly rebuttals and a few personal situations), so the questions, situations, and requests are partly inferred from the topic. Weights reflect the relative frequency and weight of the comments that point to each theme._

## Ba hoàn cảnh điển hình (tổng hợp, không phải người thật — nhân vật dẫn đường dựng từ đây, vẫn ILLUSTRATIVE)
- A retiree in their late 60s with a mid-sized pension pot who wants a simple, predictable income and is weighing a lump sum against an annuity purchase
- A widowed or single parent deciding whether to leave a legacy for children versus locking in lifetime income for themselves
- A near-retiree in their 30s to 50s who is saving aggressively and asks whether an annuity's stated payout is a good return on the amount they put in

## Điểm yếu đối thủ (khán giả phàn nàn / máy thấy)
- Headline payout or yield figures are presented without explaining that they are payout rates rather than interest rates, and without showing the principal and what it would take to break even
- Inflation impact is shown only as a percentage or a single chart, without a year-by-year real-dollar illustration of how purchasing power erodes
- Little attention is paid to how the outcome changes for different lifespans, heirs, or market rate environments, so the analysis feels one-sided in either direction
- Phương pháp của 6 video đầu bảng: 4 giả định cố định, 1 ý kiến, không tính, 1 tin tức.

## Video đối thủ theo tập (đầu bảng theo lượt xem; liên kết để WRITER/REVIEWER xem, không chép)

| Kênh | Video | Thời lượng | Phương pháp |
|---|---|---|---|
| Nanalyze | [SIWaHTeSDSM](https://youtu.be/SIWaHTeSDSM) | 10–15 phút | giả định cố định |
| Diamond NestEgg | [qFuVEfm68ps](https://youtu.be/qFuVEfm68ps) | 15–20 phút | giả định cố định |
| Learning to Retire | [aX-RQJP8_IA](https://youtu.be/aX-RQJP8_IA) | 5–10 phút | giả định cố định |
| Stan The Annuity Man | [yFDgRQk6Wl8](https://youtu.be/yFDgRQk6Wl8) | 5–10 phút | ý kiến, không tính |
| Steve Larsen | [TSxVZprmHZE](https://youtu.be/TSxVZprmHZE) | 5–10 phút | giả định cố định |

## Video vượt trội cùng đề tài (cho dòng G1)

- chưa có video vượt trội ≥ 3× (không thời sự) gắn chắc vào đề tài này trong các kênh đã kéo

## Mẫu tiêu đề (khuôn trừu tượng, không chép) và thumbnail
- Annuity vs Bond Ladder: Which Keeps Up With Inflation Over N Years?
- Annuity Payouts Explained: What Your Heirs Actually Get at Death
- Inflation-Adjusted vs Level Annuity: Which Costs More in Real Dollars?
- Thumbnail: theo mẫu thắng chung ở `market/REPORT.md` §3 (đề tài này chưa đủ mẫu riêng).

## Từ khoá mô tả
annuity inflation protection, fixed annuity vs bond ladder, SPIA payout explained, annuity cost of living rider, annuity heirs death benefit, retirement income annuity

## Đề tài khán giả yêu cầu (→ hàng đợi nhãn "từ khán giả" nếu chưa có)
- A side-by-side calculator-style walkthrough comparing an annuity with a bond or CD ladder over 20 to 30 years, in real dollars
- A practical guide to inflation-adjusted versus level annuities, including how COLA riders are priced
- A breakdown of what happens to an annuity at death under each payout option, with a worked example
