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
1. Do the hidden costs of owning (property taxes, maintenance, closing costs, HOA) get counted alongside the hidden costs of renting (forced moves, rent increases, renter's insurance)? — trọng số cao
2. How much do the results change under different assumptions: mortgage rate, investment return, rent growth, and how long you stay? — trọng số cao
3. Does renting really build wealth, or do most renters fail to invest the difference consistently? — trọng số cao
4. What happens if the landlord sells or ends the lease, and what does a forced move actually cost? — trọng số vừa
5. Which choice fits a specific life stage, such as retirement, aging in place, raising kids, or needing flexibility for work? — trọng số vừa

## Ba hoàn cảnh điển hình (tổng hợp, không phải người thật — nhân vật dẫn đường dựng từ đây, vẫn ILLUSTRATIVE)
- A homeowner who lives with aging parents and rents out their own house so the tenant covers the mortgage, weighing whether to keep the property or sell.
- A retiree or widowed senior who is tired of upkeep and considering selling to rent, balancing stable fixed costs against a limited income and rising rents.
- A young family with a stable job debating between a mortgage for long-term stability and renting while investing the down payment and monthly savings.

## Điểm yếu đối thủ (khán giả phàn nàn / máy thấy)
- Ignores or underweights the risk of landlords ending leases, which forces moves, packing, and new searches that add real costs.
- Leaves out property taxes, closing costs, maintenance, and renter's insurance, so the totals on each side are incomplete.
- Relies on unrealistic inputs such as a fixed high stock return, flat rent, and an assumption that renters will invest every saved dollar.
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
- [Option A] vs [Option B] at [Age]: Which Costs More Once Hidden Expenses Count?
- Renting vs Buying Over [N] Years: The Assumptions That Flip the Answer
- Should You Rent or Own in [Life Stage]? A Full Cost Breakdown
- Thumbnail: theo mẫu thắng chung ở `market/REPORT.md` §3 (đề tài này chưa đủ mẫu riêng).

## Từ khoá mô tả
rent vs buy a home, renting vs buying total cost, is renting a waste of money, homeownership hidden costs, buy or rent calculator, renting in retirement

## Đề tài khán giả yêu cầu (→ hàng đợi nhãn "từ khán giả" nếu chưa có)
- A follow-up showing a family of four's full monthly budget, including utilities, food, and everyday spending, for both renting and buying.
- A sensitivity analysis showing how results change with different mortgage rates, shorter ownership periods, and different rent growth rates.
- A video told from the perspective of a paid-off homeowner in a small town, covering the stability and fixed-cost side of owning.
