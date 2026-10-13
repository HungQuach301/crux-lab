# REVIEW P4 — gói phát hành Tập 7 (REVIEWER, 13/10/2026, chỉ đọc)
**Kết luận: ĐẠT có sửa**: 0 CHẶN · 1 CHÍNH · 2 PHỤ. Tiêu đề T2 đúng nguyên văn G1/G2 (58 ký tự); `package-check.md` ĐẠT.

Đã soát, đạt:
1. Số: mọi số trong mô tả/ảnh là `display` của claim, đúng nghĩa câu kịch bản: $120 = giá đường lui (S01.1/S33.3); about $613 = 15-year trừ phần bắt buộc 30-year (S05.1); $21,622 (S06.3); $6,097/$29,502/$16,631 trung vị (S13–S15.1); fewer than 1 in 5 (S15.2); Leo $13,231/$74/$793 (S29–S30). Riêng phạm vi câu thì xem CHÍNH-1.
2. Không khuyên, không dự báo: grep guarant/beat/clear/earn/better/best/should/will/your = 0. The bar = "interest no longer charged… not an investment return", "before taxes"; không so với đầu tư.
3. "US only · history, not a forecast" có ở cuối mô tả và trên cả 3 ảnh. Tessa, Leo mang ILLUSTRATIVE; cả 3 ảnh có hình nhân đều có nhãn ILLUSTRATIVE.
4. Mô tả mở bằng "30 year mortgage paid in 15". Chương 0:54/3:12/7:24/9:27 so với đầu hồi 54.9/192.1/444.2/567.1 s: lệch ≤ 0.9 s, mỗi chương ≥ 10 s. 4 trích dẫn FRED (MORTGAGE30US/15US, OBMMIC30YF/15YF) khớp từng chữ `terms.citation` trong `sources.json`.
5. Ảnh: ≤ 4 chữ lớn ("$120 A MONTH?", "THE BAR"). Vật thể đúng tên trong lời: the stack (chồng vàng cạnh nhà), the bar (thanh xám + tờ đô). Không vật cấm (thước ở thumb-2 là vạch kích thước, không phải mũi tên). Thumb-2 không nêu 7.40%. Chữ lớn đọc được ở 168×94.
6. Tag: 5 cụm, không invest/PMI/stocks/rent.
7. "$120 a month" đứng cùng câu với "the week of October 8, 2026" ở dòng 1; đoạn Tessa và khối phương pháp cũng ghi tuần dữ liệu.

Mục sửa:
- CHÍNH-1 · `description.md` đoạn 3, câu 3–4 · Lỗi: "about 15 months late / $733 a month / $8,792 once a year / 184 months / about $8,200" là claim ở lãi tuần 8/10/2026 (`*_now`, `yearly_*`), nhưng đứng ngay sau câu lịch sử 1991–2026 nên đọc như đúng cho mọi tuần; "about $8,200 more" thiếu vế so sánh. Câu sửa: "At Tessa's rates of the week of October 8, 2026, paying the 30-year exactly what the 15-year costs ends about 15 months late; finishing in 180 months takes $733 a month on top of the required payment. The same extra sent as $8,792 once a year ends in 184 months and charges about $8,200 more in interest than paying it monthly."
- PHỤ-1 · `thumb-1.png` · Lỗi: bóng nhà phủ nửa trái chồng tiền, thêm một vạch dọc mảnh trên chồng; ở 168×94 the stack đọc thành khối tối. Câu sửa: "Keep thumb-1, but light the gold stack fully (no house shadow on it) and remove the thin vertical line above it, so the gold slices read at phone size."
- PHỤ-2 · `thumb-3.png` · Lỗi: the stack đứng cạnh hai cột lãi chứ không cạnh nhà, nhà rất nhỏ, một hình chứa hai ý. Đề xuất dùng thumb-1 làm ảnh chính, thumb-2 làm phương án thử. Nếu giữ thumb-3: "Remove the two interest columns; show only the gold stack beside Tessa's house, as large as in thumb-1."
Ghi chú (không phải lỗi): dòng "US only · history, not a forecast" trên ảnh không đọc được ở 168×94; chấp nhận vì mô tả đã có.

**Áp (P4):** CHÍNH-1 áp nguyên câu sửa. PHỤ-1, PHỤ-2 (thumbnail): giữ, ghi trong `HUONG-DAN-DANG.md` để chủ dự án chọn (bóng trên chồng là ánh sáng của thế giới đã duyệt; vạch dọc là đường dẫn nhãn của cảnh). Chi REVIEWER $0,85.
