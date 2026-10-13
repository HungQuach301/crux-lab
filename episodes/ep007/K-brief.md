# Giao phiên K — Tập 7 (`episode.md` §7) · 2026-10-11

**Cần kind MỚI** (không dòng nào của bảng "Loại mô hình", `checks/CONTRACT.md` LOCK 4d688acd, phủ "hai chuỗi lãi tuần, so khoản trả đều của hai kỳ hạn trên mọi tuần ghép"; gần nhất `refinance-breakeven` / `ltv-first-passage` chỉ có một chuỗi lãi). Tên kind + params do K quyết. Chạy cùng lô K Tập 7 (A29 cache trang, A30 móc Shorts, A31 độ dài theo format) **trước C4**.
- **Đặc tả:** `topics-r2/machine/debt-1/model.json` → `newKindNeeds` (inputs, computation, outputs, invariants, dataNow).
- **Mở rộng của tập:** tuần hiện tại 2026-10-08 (`*_now`), thời kỳ (`era*`), nhân vật đối trọng tuần 2021-01-07 (`leo_*`), mô phỏng tháng trả thêm hằng tháng vs một lần mỗi năm (`monthly_extra_*`, `yearly_lump_*`), mốc = lãi 30 năm (`bar_now`, `r30_min/max`, `share_r30_ge_now`).
- **Bất biến K nên kiểm:** chỉ tuần có cả hai chuỗi (1991-08-30 →); làm tròn chỉ ở đầu ra (5 đại lượng hiệu/tích lệch 1 ở chữ số cuối nếu tính từ số đã làm tròn — kiểm độc lập); `months_at_pay15_now` là công thức liên tục (194,6), không phải số kỳ (195); trung vị `era2020_median_r30` = 6,275 (hiển thị "about 6.3%").
- **Bản tính bên dựng:** `model/model.py` → `out/model.json` (`quantities`). Kiểm độc lập **57/57** (`model/independent/report.md`).
- **Dữ liệu:** `data/fetch.py --verify` (FRED MORTGAGE30US, MORTGAGE15US chính — "Copyrighted: Citation Required"; OBMMIC30YF/OBMMIC15YF đối chiếu nội bộ, 510/510 trong 0,5 điểm → `data.crosscheck`).
## Danh sách claim
`numbers.md`; claim dùng: comment `<!-- claims -->` của `story/script.md` (C2 v3) + cột claims của `story/beats.md`.
## Luật tập đề xuất (K xét)
1. Mọi khung có Tessa/Leo hoặc ví dụ $ mang ILLUSTRATIVE; mọi số "hiện tại" kèm "this week's rates" (claim-risk: chỉ đúng ở lãi khảo sát 2026-10-08 trên $320,000).
2. Không câu/khung nào gọi mốc 7,4 % là lợi suất đầu tư, "guaranteed return", hay so với lợi suất thị trường (`claims.forbiddenTerms` kiểu A20: "guaranteed", "risk-free", "beats the market").
3. Không câu/khung nào nói chênh lãi 30–15 năm "always" một con số (chênh 0,2–1,0 điểm).
