# C5b — kiểm mù lại nhịp có hình đổi đáng kể (chủ dự án 08/10: nghĩa không thấp hơn C4)

Dải từ `out/video.mp4` (1080p, C5b `235f4cb`), khoảng = khoảng C4 dịch theo đầu cảnh mới (`review-g2/strip-spans.json`). Người đọc headless có ảnh, rubric như C4 (`gates/C4-root-intent.md`).
| Nhịp | C5b | Tốt nhất C4 | Kết luận |
|---|---|---|---|
| B02 | 1/3 (khuyên 1, 0,5 một) | 2/2 | **thấp hơn → sửa** |
| B03 | 2/2 | 2/2 | ĐẠT |
| B11 | 2/2 | 2/2 | ĐẠT |
| N2 S13 | nghĩa 2/2 (tắt tiếng; ngoại lệ C3) | — | — |
| B14 | 2/2 | 2/2 | ĐẠT |
| B16 | 2/2 | 2/2 | ĐẠT |
| B17 | 2/2 | 2/2 | ĐẠT |
| B18 | 0/2 (0,5 + 0,5: thiếu ba bảng + quạt nhanh→chậm; đọc đường trắng thành giá) | 2/2 | **thấp hơn → sửa** |
**Chốt chặn có lời:** S06 3/3 · S13 3/3, khuyên 0 → ĐẠT. Token: người đọc 196.094 + 12.211 + 74.080, chấm 33.736 + 7.246 + 14.198. Dữ liệu `c5/root-r1/`, `c5/root-r1x/`, `c5/voiced-r1/`.

## C5c vòng 1 (sửa B02, B18 — `c5/root-r2/`)
| Nhịp | Kết quả | Chẩn đoán |
|---|---|---|
| B02 | 0/2 (0,5 + 0,5) | tiêu đề "Loan ÷ home value on paper" hiện từ phần chỉ có lịch → người đọc lấy quạt lịch sử làm ý chính, bỏ mốc lịch 8 năm |
| B18 | 0/2 (0,5 + 0,5) | bố cục mới "ba bảng rồi gộp chung trục" lệch ý "ba bảng cạnh nhau"; đọc vạch 80 % thay vì 75 % |
Không tốt hơn C5b → vòng 2: về bố cục C4 tốt nhất, chỉ giữ phần luật bắt buộc (màu V09, chữ S10, tấm nền, nhãn "on paper" chỉ trên khung có claim trên giấy). Token 49.695 + 12.910.

## So C4 ↔ C5c đủ mẫu (ghi TRƯỚC khi chạy, 2026-10-08)
Lý do: dải C5b gần trùng điểm ảnh với C4 mà điểm khác (n = 2–3) → nghi nhiễu. **Phép so:** mỗi nhịp B02, B18 — dải **C4 tốt nhất** (`review-c4/strips/B02-S02.r2.png` = bản v1/v2 đạt 2/2; `B18-S18.r2.png` = bản v2 đạt 2/2) và dải **C5c** (`review-g2/strips/B02-S02.png`, `B18-S18.png`), **6 người đọc mới mỗi dải** (24 lượt), cùng câu hỏi/vai, chấm bằng **một** người chấm cho cả 24 nhãn trộn (nhãn có id dải, không có phiên bản), cùng đáp án hiện hành (`review-c4/spans.json`).
**Quyết định ghi trước:** C5c giữ nếu số người đọc đúng (nghĩa 1 + không khuyên_tính) của C5c **≥** của C4 cho từng nhịp (nghĩa không thấp hơn C4). C5c < C4 ở nhịp nào → nhịp đó về bố cục C4 (giữ phần luật bắt buộc) ở vòng 2. Kết quả ghi nguyên văn bên dưới, không chạy lại.

### Kết quả so đủ mẫu (`c5/cmp-c4-c5c/`, 24 lượt, một người chấm; token 296.448 + 46.325)
| Nhịp | C4 tốt nhất | C5c | Quyết định (ghi trước) |
|---|---|---|---|
| B02 | 5/6 (khuyên 1) | **6/6** | C5c ≥ C4 → **giữ C5c** |
| B18 | 1/6 (nghĩa 0,5 ×5: bản C4 không có ba bảng) | **5/6** | C5c ≥ C4 → **giữ C5c** |
Kết luận: các điểm thấp ở n = 2–3 (C5b, C5c vòng 1) là nhiễu mẫu nhỏ; bản C5c đạt nghĩa ≥ C4 ở mọi nhịp loại 1. Bài học: so phiên bản bằng 6 người đọc/dải cùng một người chấm (đề xuất cho tổng kết Tập 5).
