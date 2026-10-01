# C4 gốc · vòng 2 — Ý đồ (ghi TRƯỚC khi sửa/chạy; không sửa sau)

Lệnh chủ dự án C4c (01/10/2026): (a) sửa KEY-2, 5, 6, 7 chỉ bằng nhãn chữ mang nghĩa, không thêm vật/gu.
**Giữ nguyên** toàn bộ `gates/C4-orig-intent.md`: vai, câu hỏi, tiêu chí "đúng nghĩa" vs "chỉ tả hình", chấm 1/0,5/0, nhịp đọc đúng khi tổng ≥ 2/3, cổng ≥ 6/7. Thêm điều kiện của chủ dự án:
1. **Câu có tính khuyên:** người chấm độc lập đánh dấu riêng mọi câu trả lời có tính khuyên ("X is safer/better", "act now"…). **Nhịp nào còn ≥ 1 câu như vậy thì chưa đạt, dù điểm nghĩa đủ.**
2. **Kiểm cả 7 nhịp** (để bắt nhãn mới làm hỏng nhịp đã đạt). 3 người đọc **mới** mỗi nhịp, mẫu là dải `animatic/strips/KEY-n.png` dựng lại sau khi sửa.
3. **Tối đa 2 vòng** (vòng 1 = lần kiểm `gates/C4-orig-blind.md`; đây là vòng 2). Đạt (≥ 6/7, tính cả điều kiện 1) → render, đi tiếp C5. Trượt → tự chuyển (b): duyệt ngoại lệ, render, ghi `ledger.md` và `taste-ledger.md` cả điểm che chữ lẫn điểm cổng gốc; không hỏi lại.

**Ràng buộc nhãn** (kiểm trước khi chạy): mỗi nhãn ≤ ~8 từ, ≥ 40 px quy về 1080p, hiện ≥ 1 giây cho mỗi 3 từ. KEY-2 tách hai dòng hoặc hai khung ("Different offers" / "Head start = fixed − variable"). KEY-7 tách rõ hai nửa ("1954–1980" / "1981 on"). Mọi nhãn qua S10, không chứa số ngoài claim.
Nguyên văn và bảng: `gates/C4-orig-blind-r2.md`.
