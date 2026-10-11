# Hồ sơ cầu — Sell at 11 Months or Wait for the Lower Tax Rate?

Đề tài: dòng #8 trong `topics/queue.md` · id `q08-short-long-capital-gains` · **Làm mới: 2026-10-11** (làm lại khi > 30 ngày, `playbook/episode.md` §1b.1).
Sinh bằng `python3 toolkit/market/report.py topics` từ `~/market-cache/` (ngoài git). Không số liệu thô; nhãn và chỉ số **tự tính, không phải chỉ số YouTube**. Câu hỏi, hoàn cảnh, điểm yếu: Haiku tóm từ bình luận đã lọc (diễn đạt lại, không trích nguyên văn) — máy viết, có thể sai.

| Mục | Nhãn | Cách tính (tự tính) |
|---|---|---|
| Mức cầu (trừ thời sự) | **thấp** | trung vị lượt xem/ngày của 10 video gắn đề tài mạnh nhất (≤ 24 tháng, bỏ video cờ thời sự), chia ba bậc trên 21 đề tài |
| Khoảng trống | **cao** | video đầu bảng có phát lại dữ liệu lịch sử thật không: cao = không video nào, vừa = 1, thấp = ≥ 2 (Haiku đọc tiêu đề + mô tả) |
| Số video gắn đề tài | vừa | embeddings, chỉ cặp khớp cao (cosine ≥ 0.55, biên ≥ 0.04) |
| Dải thời lượng | 7:36–19:06 | tứ phân vị 25–75 % của video đầu bảng cùng đề tài |

## Câu hỏi khán giả (xếp theo trọng số: like + 2 × phản hồi, tự tính)
1. How do I pick specific tax lots when selling, and which brokerages actually allow it instead of forcing FIFO or LIFO? — trọng số cao
2. Is a sale a short-term or long-term gain, and how does the sell date change the tax bill? — trọng số cao
3. Does lot-level selection or the same tax-lot math work inside an IRA? — trọng số vừa
4. When every lot shows a gain, which lots should I sell first to minimize tax on a large appreciated position? — trọng số vừa
5. Does deferring the gain actually help, or only delay it? What about loss harvesting, donating shares, or borrowing against the position? — trọng số vừa

_Ghi chú máy: Based on about 25 short comments, so the weights are rough. Situations and weaknesses are partly inferred from the topic and the recurring rebuttals rather than from many direct complaints._

## Ba hoàn cảnh điển hình (tổng hợp, không phải người thật — nhân vật dẫn đường dựng từ đây, vẫn ILLUSTRATIVE)
- A retiree or low-income seller who has a zero-rate tax year and sells appreciated shares in pieces each quarter, choosing lots to stay in the 0% bracket.
- An investor whose brokerage forces year-wide FIFO or LIFO, so they can't choose lots and want to know whether switching brokers or accounts is worth it.
- A long-term holder of one concentrated stock bought years ago with a gain of over 2000%, who wants to sell or diversify without a large tax bill.

## Điểm yếu đối thủ (khán giả phàn nàn / máy thấy)
- Presents lot selection as a universal trick, but viewers report it's only available at some brokerages and needs the right account setup.
- Uses an example with a 2026 sale that viewers say is a short-term gain, not long-term, which undermines the core claim.
- Calls the strategy a way to avoid tax, while viewers point out it mostly defers the gain and the example is too rare to apply to typical sales.
- Phương pháp của 6 video đầu bảng: 2 giả định cố định, 4 ý kiến, không tính.

## Video đối thủ theo tập (đầu bảng theo lượt xem; liên kết để WRITER/REVIEWER xem, không chép)

| Kênh | Video | Thời lượng | Phương pháp |
|---|---|---|---|
| Toby Mathis Esq · Tax Planning & Asset Protection  | [JpufIL0n00I](https://youtu.be/JpufIL0n00I) | 17:18 | giả định cố định |
| Michael D. Brennan | [wqdyIDumuNM](https://youtu.be/wqdyIDumuNM) | 19:12 | giả định cố định |
| Upstox Pro | [ub4yCbtFBIg](https://youtu.be/ub4yCbtFBIg) | 6:00 | ý kiến, không tính |
| FinoMoji: Stock Market Educator 📈 | [dBHUJXp7sZI](https://youtu.be/dBHUJXp7sZI) | 19:06 | ý kiến, không tính |
| Financial Enhancement Group | [2CY3i1EFC9I](https://youtu.be/2CY3i1EFC9I) | 7:36 | ý kiến, không tính |

## Video vượt trội cùng đề tài (cho dòng G1)

- chưa có video vượt trội ≥ 3× (không thời sự) gắn chắc vào đề tài này trong các kênh đã kéo

## Mẫu tiêu đề (khuôn trừu tượng, không chép) và thumbnail
- Which Tax Lot Do You Sell? Same Shares, Different Tax Bill
- Short-Term vs Long-Term: How Your Sell Date Changes What You Owe
- Deferral or Avoidance? What a Capital Gains Strategy Really Saves
- Thumbnail: theo mẫu thắng chung ở `market/REPORT.md` §3 (đề tài này chưa đủ mẫu riêng).

## Từ khoá mô tả
tax lot selection, specific identification cost basis, short term vs long term capital gains, FIFO vs LIFO brokerage, capital gains tax on stocks, holding period capital gains

## Đề tài khán giả yêu cầu (→ hàng đợi nhãn "từ khán giả" nếu chưa có)
- A step-by-step guide to finding and using specific lot selection at Fidelity, Schwab, Vanguard, and Robinhood.
- A check of whether lot selection and cost-basis rules apply to IRA and other tax-advantaged accounts.
- A video on holding-period math, showing exactly when a lot crosses from short-term to long-term.
- A comparison of deferral, loss harvesting, charitable donation, and selling losers, with their trade-offs.
