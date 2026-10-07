# C3 — ý đồ cổng gốc 3 hình mới (ghi TRƯỚC khi chạy; không sửa sau khi thấy kết quả)

Ngày 2026-10-07. Hình mới: **N1** lịch trả góp (B06), **N3** gập đường thành cột (B10), **N2** cột theo tháng mua + đuôi chậm (B13). Dải 6 khung **tắt tiếng** từ clip có chuyển động `review-c3/strips/*.png` (thời điểm: `review-c3/spans.json`); bản sao tên hex trong `c3/root/`.
- **Người đọc:** headless có ảnh (`toolkit/blind/headless.sh --read`), mỗi lượt MỚI, chỉ mở một PNG; 2 người mỗi hình; lệch nhau → người thứ 3; hình đạt khi ≥ 2/3 (dừng khi 2 người đầu cùng kết quả).
- **Vai T:** "You are an American in your late 20s or early 30s, renting, who has saved about 10% of a home's price and is thinking about buying your first home."
- **Câu hỏi** (như C3 Tập 4): 1. What idea is this animation showing? 2. What changes over time across the frames? 3. What does it mean? 4. What advice, if any, would a viewer take from this?
- **Chấm:** người chấm độc lập mù tập; nghĩa 1 / 0,5 / 0 so với "muted read" của `review-c3/spans.json`; cờ khuyên theo **A9** (thận trọng chung — tự kiểm số, hỏi bên cho vay — không tính; khuyên mua/chờ/bán/chọn tính). Người đọc đúng = nghĩa 1 và khuyên_tính false.
- **Ngưỡng mỗi hình:** ≥ 2/3 đúng, khuyên_tính 0. Trượt → **sửa bằng hình trước** (D-009, E6), nhãn là cách cuối; ≤ 3 vòng mỗi hình; khoá nghĩa (bản sau không thấp hơn bản tốt nhất).
