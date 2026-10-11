# Hồ sơ cầu — Rent vs buy a home — real history replay

Đề tài: từ hạt giống trong `topics/queue.md` · id `s1-rent-vs-buy-history` · **Làm mới: 2026-10-11** (làm lại khi > 30 ngày, `playbook/episode.md` §1b.1).
Sinh bằng `python3 toolkit/market/report.py topics` từ `~/market-cache/` (ngoài git). Không số liệu thô; nhãn và chỉ số **tự tính, không phải chỉ số YouTube**. Câu hỏi, hoàn cảnh, điểm yếu: Haiku tóm từ bình luận đã lọc (diễn đạt lại, không trích nguyên văn) — máy viết, có thể sai.

| Mục | Nhãn | Cách tính (tự tính) |
|---|---|---|
| Mức cầu (trừ thời sự) | **cao** | trung vị lượt xem/ngày của 10 video gắn đề tài mạnh nhất (≤ 24 tháng, bỏ video cờ thời sự), chia ba bậc trên 21 đề tài |
| Khoảng trống | **vừa** | video đầu bảng có phát lại dữ liệu lịch sử thật không: cao = không video nào, vừa = 1, thấp = ≥ 2 (Haiku đọc tiêu đề + mô tả) |
| Số video gắn đề tài | cao | embeddings, chỉ cặp khớp cao (cosine ≥ 0.55, biên ≥ 0.04) |
| Dải thời lượng | 11–23 phút | tứ phân vị 25–75 % của video vượt trội cùng đề tài, làm tròn ra phút nguyên |

## Câu hỏi khán giả (xếp theo trọng số: like + 2 × phản hồi, tự tính)
1. Over a realistic holding period, does renting actually cost more than buying once you count interest, taxes, insurance, and maintenance? — trọng số cao
2. How do the numbers change with different mortgage rates, home price growth, and rent increases? — trọng số cao
3. What hidden costs does each option carry, such as closing costs, moving expenses, repairs, and renter's insurance? — trọng số cao
4. Is the money saved by renting actually invested, and does that investment outcome beat home equity? — trọng số vừa
5. How do non-financial factors like stability, control over the home, flexibility, and family needs weigh against the math? — trọng số vừa

_Ghi chú máy: Comments were varied and numerous, so the ranking reflects weight and frequency of the rebuttals and situations. Titles and comment wording are paraphrased, not copied._

## Ba hoàn cảnh điển hình (tổng hợp, không phải người thật — nhân vật dẫn đường dựng từ đây, vẫn ILLUSTRATIVE)
- A dual-income household in a high-cost metro weighing a mortgage against a long-term lease while saving for a down payment
- A retiree or near-retiree deciding whether to sell a paid-off home and rent for lower upkeep and easier aging in place
- A young professional who expects to move for work within a few years and is comparing short-term renting with buying

## Điểm yếu đối thủ (khán giả phàn nàn / máy thấy)
- Assumes investment returns and rent growth without showing sensitivity to different scenarios
- Leaves out transaction costs, property taxes, and the risk of forced moves when landlords end leases
- Treats the comparison as purely financial and ignores lifestyle, emotional, and family factors
- Phương pháp của 6 video đầu bảng: 3 giả định cố định, 2 ý kiến, không tính, 1 dữ liệu lịch sử thật.

## Video đối thủ theo tập (đầu bảng theo lượt xem; liên kết để WRITER/REVIEWER xem, không chép)

| Kênh | Video | Thời lượng | Phương pháp |
|---|---|---|---|
| Logical Money | [nkT_K8l1rEw](https://youtu.be/nkT_K8l1rEw) | 15–20 phút | giả định cố định |
| HinExp | [VSnf3GaGgMU](https://youtu.be/VSnf3GaGgMU) | 15–20 phút | giả định cố định |
| A2D Channel | [9RzbEmPEa8g](https://youtu.be/9RzbEmPEa8g) | 15–20 phút | ý kiến, không tính |
| TED-Ed | [h6CmKF-mN2U](https://youtu.be/h6CmKF-mN2U) | 5–10 phút | ý kiến, không tính |
| MoneywithSwAbi | [YOBf21X3umI](https://youtu.be/YOBf21X3umI) | 10–15 phút | giả định cố định |

## Video vượt trội cùng đề tài (cho dòng G1)

- Logical Money — [nkT_K8l1rEw](https://youtu.be/nkT_K8l1rEw) — 15–20 phút — ≥ 5× (tự tính)
- Retirement 4 the Rest of Us — [oX6bDeoE3bg](https://youtu.be/oX6bDeoE3bg) — 20–30 phút — ≥ 5× (tự tính)
- MoneywithSwAbi — [YOBf21X3umI](https://youtu.be/YOBf21X3umI) — 10–15 phút — ≥ 5× (tự tính)

## Mẫu tiêu đề (khuôn trừu tượng, không chép) và thumbnail
- Renting vs Buying in [City]: Which Wins Over [N] Years?
- Rent or Buy: How Much Do Hidden Costs Change the Answer?
- Buying vs Renting at [Interest Rate]: When Does Each Option Win?
- Thumbnail: theo mẫu thắng chung ở `market/REPORT.md` §3 (đề tài này chưa đủ mẫu riêng).

## Từ khoá mô tả
rent vs buy, renting vs buying a home, is renting a waste of money, buying a house calculator, total cost of homeownership, rent vs buy break-even

## Đề tài khán giả yêu cầu (→ hàng đợi nhãn "từ khán giả" nếu chưa có)
- A follow-up that shows how the result changes with different mortgage rates or shorter ownership periods
- A comparison for a family of four that includes utilities, food, and everyday spending
- A retiree-focused episode covering downsizing, renting, and housing costs on a fixed income
