# Hồ sơ cầu — Rental property vs index funds — real history replay

Đề tài: từ hạt giống trong `topics/queue.md` · id `s2-rental-vs-index-history` · **Làm mới: 2026-10-11** (làm lại khi > 30 ngày, `playbook/episode.md` §1b.1).
Sinh bằng `python3 toolkit/market/report.py topics` từ `~/market-cache/` (ngoài git). Không số liệu thô; nhãn và chỉ số **tự tính, không phải chỉ số YouTube**. Câu hỏi, hoàn cảnh, điểm yếu: Haiku tóm từ bình luận đã lọc (diễn đạt lại, không trích nguyên văn) — máy viết, có thể sai.

| Mục | Nhãn | Cách tính (tự tính) |
|---|---|---|
| Mức cầu (trừ thời sự) | **cao** | trung vị lượt xem/ngày của 10 video gắn đề tài mạnh nhất (≤ 24 tháng, bỏ video cờ thời sự), chia ba bậc trên 21 đề tài |
| Khoảng trống | **vừa** | video đầu bảng có phát lại dữ liệu lịch sử thật không: cao = không video nào, vừa = 1, thấp = ≥ 2 (Haiku đọc tiêu đề + mô tả) |
| Số video gắn đề tài | cao | embeddings, chỉ cặp khớp cao (cosine ≥ 0.55, biên ≥ 0.04) |
| Dải thời lượng | 10–22 phút | tứ phân vị 25–75 % của video vượt trội cùng đề tài, làm tròn ra phút nguyên |

## Câu hỏi khán giả (xếp theo trọng số: like + 2 × phản hồi, tự tính)
1. Does the comparison count every source of return on both sides, including rent collected, leverage, appreciation, and reinvested cash flow? — trọng số cao
2. How do taxes change the outcome, including depreciation, deductible expenses, capital gains on sale, and yearly taxes on dividends? — trọng số cao
3. What do time, effort, vacancies, repairs, and tenant problems cost compared with a passive index fund, and are they priced into the result? — trọng số cao
4. Are the inputs realistic, such as purchase price, mortgage rate, rent level, property tax growth, insurance, and selling costs? — trọng số vừa
5. Can someone do both, and which path fits a given income, risk tolerance, and willingness to manage property? — trọng số vừa

## Ba hoàn cảnh điển hình (tổng hợp, không phải người thật — nhân vật dẫn đường dựng từ đây, vẫn ILLUSTRATIVE)
- A salaried professional with a modest down payment saved, deciding between buying a first rental and contributing the same money to tax-advantaged index fund accounts.
- A near-retiree who owns a paid-off rental and is weighing whether to sell and move the proceeds into funds to reduce landlord work while keeping similar income.
- A younger investor who already owns a primary home and has a steady monthly surplus, wondering whether to add a rental or keep investing in index funds.

## Điểm yếu đối thủ (khán giả phàn nàn / máy thấy)
- Compares one property against a lump sum or a differently funded stock portfolio, so the contribution amounts and timing are not equal.
- Leaves out tax effects such as depreciation, deductions, capital gains, and yearly dividend taxes, or ignores selling costs entirely.
- Treats the rental as if it runs itself, ignoring management time, vacancy, maintenance, and the chance of a single-property concentration risk.
- Phương pháp của 6 video đầu bảng: 4 giả định cố định, 1 ý kiến, không tính, 1 dữ liệu lịch sử thật.

## Video đối thủ theo tập (đầu bảng theo lượt xem; liên kết để WRITER/REVIEWER xem, không chép)

| Kênh | Video | Thời lượng | Phương pháp |
|---|---|---|---|
| Logical Money | [bbP8Mr_MThk](https://youtu.be/bbP8Mr_MThk) | 15–20 phút | giả định cố định |
| Pranjal Kamra | [9FYOUIZnZjU](https://youtu.be/9FYOUIZnZjU) | 10–15 phút | ý kiến, không tính |
| MoneywithSwAbi | [2MTkmrpltbQ](https://youtu.be/2MTkmrpltbQ) | 10–15 phút | dữ liệu lịch sử thật |
| Tom – Lazy Real Estate | [LoQNLmpzPfE](https://youtu.be/LoQNLmpzPfE) | 20–30 phút | giả định cố định |
| Samuel Leeds | [fNRfwdIPXwU](https://youtu.be/fNRfwdIPXwU) | 10–15 phút | giả định cố định |

## Video vượt trội cùng đề tài (cho dòng G1)

- Logical Money — [bbP8Mr_MThk](https://youtu.be/bbP8Mr_MThk) — 15–20 phút — ≥ 5× (tự tính)
- Tom – Lazy Real Estate — [LoQNLmpzPfE](https://youtu.be/LoQNLmpzPfE) — 20–30 phút — ≥ 5× (tự tính)
- MoneywithSwAbi — [2MTkmrpltbQ](https://youtu.be/2MTkmrpltbQ) — 10–15 phút — ≥ 5× (tự tính)

## Mẫu tiêu đề (khuôn trừu tượng, không chép) và thumbnail
- [Asset A] vs [Asset B]: Who Wins After [N] Years Once Taxes and Costs Are Counted?
- I Gave [Strategy A] and [Strategy B] the Same Monthly Cash: Here Is the Honest Result
- [Strategy A] or [Strategy B]? A Fair Scorecard With Vacancies, Taxes, and Time Costs Included
- Thumbnail: theo mẫu thắng chung ở `market/REPORT.md` §3 (đề tài này chưa đủ mẫu riêng).

## Từ khoá mô tả
rental property vs index funds, real estate vs stock market returns, rental property ROI calculation, index fund returns comparison, real estate depreciation tax benefits, passive income rental vs ETF

## Đề tài khán giả yêu cầu (→ hàng đợi nhãn "từ khán giả" nếu chưa có)
- A video explaining REITs as a way to get property exposure without owning or managing a building.
- A comparison of REITs against owning commercial rental property for income.
- A side-by-side look at REITs, direct residential rentals, and index funds for someone who wants monthly income.
