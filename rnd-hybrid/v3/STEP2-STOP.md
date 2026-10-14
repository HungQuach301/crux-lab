# Vòng 3 · Bước 2 DỪNG: chủ dự án bác H4′ (14/10/2026)

**Đã dừng:** lượt dựng clip v3 1080p (H4′) dừng bằng PID (`kill` theo PID của build.py, render_shots.js, headless_shell; không dùng `pkill -f`). Lúc dừng đã xong **8/19 cảnh** (cache ở `rnd-hybrid/work/v3clip/`, ngoài git). **Chưa chạy đọc mù** (chưa gọi headless, chi Console 0 $). Bước 2 chi **0 $**, vì clip dùng lại giọng v2.

## Lý do chủ dự án bác (đã xem `v3/out/H4p-close-1080.jpg`)
- **Thân Quaternius là người mẫu trần.** Áo chỉ là màu sơn lên thân, nên trông như đồ bó.
- **Mặt biểu tượng (rig.js) gắn lên đầu bán thực tế** ra ma-nơ-canh.
- **Lỗi hình:** mũ xuyên qua đầu, cổ áo răng cưa.
- **Nhà Kenney mái xanh** là ngoại ô hiện đại, không phải năm 1930.
- **Gốc rễ:** thân, mặt, quần áo và nhà ở **các mức cách điệu khác nhau**.

**Quyết định:** bỏ hẳn mô hình người tải về. Các gói Quaternius và Kenney vẫn ở repo (CC0, RIGHTS §F7) như hồ sơ R&D, nhưng không dùng cho hướng mới.

## Phần đã có (giữ lại để tham khảo)
- `v3/lib/quat.js`: thân Quaternius, trang phục theo vùng xương, mặt chiếu theo bề mặt.
- `v3/clip/seg/{world4.js,scene.js}`, `v3/clip/build.py`: clip v3, đã sửa a–d trong biên đạo.
- `v3/clip/luma.py`: đo độ sáng các cảnh đêm của clip v2 (trước sửa) được trung bình **72,9/255** (E 83,6 · F 45,5 · G 63,3 · H 92,4 · J 79,5). Clip v3 dựng chưa xong nên chưa có số "sau".
- `v3/CHARTER-PROPOSAL.md`: bản nháp viết cho H4′. Phải viết lại theo hướng được chọn ở vòng khung phong cách.
- `v3/blind/prompt.tmpl`: đầu bài đọc mù theo PHIEU-v2, chưa dùng.

## Bước mới
Khung phong cách P1 (giấy nhiều lớp nâng cấp) · P2 (sa bàn tượng nhỏ) · P3 (tranh in báo 1930, 2.5D), mỗi hướng 2 khung K1, K2. Xem `v3/STYLE-FRAMES.md`.
