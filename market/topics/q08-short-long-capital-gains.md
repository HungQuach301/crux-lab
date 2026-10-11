# Hồ sơ cầu — Sell at 11 Months or Wait for the Lower Tax Rate?

Đề tài: dòng #8 trong `topics/queue.md` · id `q08-short-long-capital-gains` · **Làm mới: 2026-10-11** (làm lại khi > 30 ngày, `playbook/episode.md` §1b.1).
Sinh bằng `python3 toolkit/market/report.py topics` từ `~/market-cache/` (ngoài git). Không số liệu thô; nhãn và chỉ số **tự tính, không phải chỉ số YouTube**. Câu hỏi, hoàn cảnh, điểm yếu: Haiku tóm từ bình luận đã lọc (diễn đạt lại, không trích nguyên văn) — máy viết, có thể sai.

| Mục | Nhãn | Cách tính (tự tính) |
|---|---|---|
| Mức cầu (trừ thời sự) | **thấp** | trung vị lượt xem/ngày của 10 video gắn đề tài mạnh nhất (≤ 24 tháng, bỏ video cờ thời sự), chia ba bậc trên 21 đề tài |
| Khoảng trống | **cao** | video đầu bảng có phát lại dữ liệu lịch sử thật không: cao = không video nào, vừa = 1, thấp = ≥ 2 (Haiku đọc tiêu đề + mô tả) |
| Số video gắn đề tài | vừa | embeddings, chỉ cặp khớp cao (cosine ≥ 0.55, biên ≥ 0.04) |
| Dải thời lượng | 7–20 phút | tứ phân vị 25–75 % của video đầu bảng cùng đề tài, làm tròn ra phút nguyên |

## Câu hỏi khán giả (xếp theo trọng số: like + 2 × phản hồi, tự tính)
1. How do I choose which specific shares or tax lots to sell so I control the gain or loss, and how do I find that option at my broker? — trọng số cao
2. Does my brokerage honor lot-level selection, or does it force FIFO, LIFO, or average cost for the whole year, and does this differ by account type? — trọng số cao
3. How do I tell whether a sale counts as short-term or long-term, and what does waiting past the one-year mark actually save? — trọng số vừa
4. If every lot I own shows a gain, which lots should I sell first, and can gains from other investments such as options be offset? — trọng số vừa
5. Do lot-selection tactics work inside an IRA or other retirement account, where capital gains tax normally doesn't apply? — trọng số thấp

_Ghi chú máy: Only vài short comments were provided, most with low weight, so the ranking and some items are inferred from the topic and the video titles._

## Ba hoàn cảnh điển hình (tổng hợp, không phải người thật — nhân vật dẫn đường dựng từ đây, vẫn ILLUSTRATIVE)
- An investor with a low-income or zero-rate tax year who wants to realize gains tax-free by selling higher-basis lots in stages across the year.
- An investor whose broker defaults to FIFO and who can't find a lot-selection setting, and who is deciding whether to change settings or switch brokerages.
- A long-term holder with a large position in one stock that has grown many times over, weighing whether to sell near the one-year mark or hold longer, possibly considering the rules that apply at age 65.

## Điểm yếu đối thủ (khán giả phàn nàn / máy thấy)
- Examples present rare or extreme scenarios as if they were typical, and viewers push back that ordinary sales wouldn't be affected.
- Strategies are presented as tax savings even though they only defer the bill; viewers point out that the tax eventually comes due and that loss harvesting or donation may matter more.
- Holding-period math is sometimes wrong, so a future sale is treated as long-term when it would be short-term and taxed at a higher rate.
- Phương pháp của 6 video đầu bảng: 2 giả định cố định, 4 ý kiến, không tính.

## Video đối thủ theo tập (đầu bảng theo lượt xem; liên kết để WRITER/REVIEWER xem, không chép)

| Kênh | Video | Thời lượng | Phương pháp |
|---|---|---|---|
| Toby Mathis Esq · Tax Planning & Asset Protection  | [JpufIL0n00I](https://youtu.be/JpufIL0n00I) | 15–20 phút | giả định cố định |
| Michael D. Brennan | [wqdyIDumuNM](https://youtu.be/wqdyIDumuNM) | 15–20 phút | giả định cố định |
| Upstox Pro | [ub4yCbtFBIg](https://youtu.be/ub4yCbtFBIg) | 5–10 phút | ý kiến, không tính |
| FinoMoji: Stock Market Educator 📈 | [dBHUJXp7sZI](https://youtu.be/dBHUJXp7sZI) | 15–20 phút | ý kiến, không tính |
| Financial Enhancement Group | [2CY3i1EFC9I](https://youtu.be/2CY3i1EFC9I) | 5–10 phút | ý kiến, không tính |

## Video vượt trội cùng đề tài (cho dòng G1)

- chưa có video vượt trội ≥ 3× (không thời sự) gắn chắc vào đề tài này trong các kênh đã kéo

## Mẫu tiêu đề (khuôn trừu tượng, không chép) và thumbnail
- Sell Now or Wait Past 12 Months: What the Tax Bill Looks Like at Each Date
- Which Shares to Sell First: Lot Selection vs FIFO Across Brokerages
- Deferral vs Elimination: When Delaying a Capital Gains Tax Bill Actually Helps
- Thumbnail: theo mẫu thắng chung ở `market/REPORT.md` §3 (đề tài này chưa đủ mẫu riêng).

## Từ khoá mô tả
tax lot selection, specific identification cost basis, short-term vs long-term capital gains, FIFO vs specific lot, holding period capital gains, capital gains tax strategy

## Đề tài khán giả yêu cầu (→ hàng đợi nhãn "từ khán giả" nếu chưa có)
- A broker-by-broker walkthrough showing how to turn on specific lot identification and where to find it in each app.
- A clear answer on whether lot selection and tax-lot tactics apply inside IRAs and other retirement accounts.
- A worked example combining lot selection with options gains and losses.
- A comparison of deferring gains versus harvesting losses or donating appreciated shares as exit strategies.
- A breakdown of whether borrowing against a portfolio to reduce taxable income is a sound approach.
