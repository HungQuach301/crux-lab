# Mốc V · Ý đồ kiểm mù cổng gốc (ghi TRƯỚC khi chạy, 06/10/2026)

**Mẫu:** 4 bản của cùng đoạn 69,6 s Tập 4 (S04.5 → S07.3): **R** = bản đã phát hành (cắt 93,44–163,60 s từ `ep004-youtube.mp4`), **A** (vật thể thật 2D), **B** (vật thể thật 3D, nhà dựng bằng mã), **C** (hình học liên tục). Thứ tự và tên mẫu bị xáo, người đọc chỉ thấy tên file hex.
**Nhịp loại 1 (2 nhịp/bản):**
- **K1** = b3→b8 (lời S06.1–S06.6; R: 116,87–150,07 s gốc). Ý người xem phải đọc ra: *"Lãi trên giấy của một căn nhà (minh hoạ, lên giá như trung bình Phoenix) tăng dần theo năm, vượt một mức trần cố định $500,000 vào khoảng Q2 2022, tụt lại một chút, và ở trên trần từ Q2 2023."*
- **K2** = b9→hết (lời S07.1–S07.3). Ý phải đọc ra: *"Lãi của họ (≈ $558,100) đã vượt trần $500,000; giá nhà vùng Phoenix gấp khoảng 3,8 lần năm 2000."*
**Dải:** `toolkit/blind/strips.py` 6 khung tắt tiếng, GIỮ chữ/số, tâm 6 lát bằng nhau.
**Người đọc:** headless `toolkit/blind/headless.sh --read` (sonnet), không ngữ cảnh dự án, vai: *"You are a 58-year-old US homeowner who bought a house in 2000."* Câu hỏi cố định (tiếng Anh): (1) What idea is this sequence of 6 frames from a muted video trying to show? (2) What changes across frames 1→6? (3) What does it mean for someone like you? (4) What advice, if any, would a viewer take from this?
**Người chấm:** headless độc lập, mù bản (chỉ thấy nhãn ngẫu nhiên + rubric). 1 = đúng nghĩa (đủ các ý trong câu "phải đọc ra"; K1 phải nói đường là LÃI/lợi nhuận, không phải giá nhà); 0,5 = đúng hướng nhưng sai một ý (vd đọc thành giá nhà, thiếu mốc); 0 = khác. Cờ khuyên theo A9: khuyên mua/bán/giữ/canh thời điểm bán/sản phẩm tài chính → tính; thận trọng chung (tự kiểm số, hỏi chuyên gia thuế) → không tính.
**Dừng sớm (§5.6):** 2 người đọc đầu cùng kết quả thì dừng; lệch thì người thứ 3; nhịp ĐẠT khi ≥ 2/3 đúng (điểm 1, không khuyên tính).
**Ngưỡng hướng:** đạt cả K1 và K2. So R để biết hướng có hơn bản phát hành không. Không sửa ý đồ sau khi thấy kết quả.
**Hạn chế ghi trước:** người đọc cùng model tương quan cao (tongket-t4 §2c); dải tĩnh không bắt được chuyển động (G-011) — chuyển động được chấm ở lượt đạo diễn.
