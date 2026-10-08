# Hiệu chuẩn thước CHỈ BÁO (tổng kết Tập 5 §3.2–3.3, áp mục 9 và 14) — 08/10/2026

Thước ở `toolkit/indicators/` (README ở đó). Tất cả **chỉ báo**, không phải ngưỡng, không chặn tập (CHARTER §4: thước mới phải hiệu chuẩn trước khi dùng). Không sửa `checks/`.

**Mẫu hiệu chuẩn** (luật đặt trước khi chạy, như chủ dự án duyệt 08/10):
- **Tập 1** — đối chứng ÂM (thẻ chữ 2D, trước Mốc V): thước phải xếp Tập 1 **dưới** Tập 4 v3k và Tập 5. Video `episodes/ep001/review-c6/ep001-full-720p.mp4` (9:51).
- **Tập 4 v3k** — đoạn chứng minh Mốc V, L3 4·4·4·4·4·4: `moc-v/review/proof-a-ep004-v3k-540p.mp4` (69,6 s), spine `moc-v/seg/ep004/spine.json`.
- **Tập 5** — bản phát hành, L3 4·4·4·4·4·4: `episodes/ep005/review-g2/full-720p.mp4` (7:46), spine `episodes/ep005/world/c4/*/spine.json`.
- Thước nhịp có thêm **đối chứng DƯƠNG**: animatic C4 Tập 5 (spine @ `b70a0db`, bản đạo diễn A xem) phải bắt 4 quãng tĩnh đạo diễn A nêu: 0:44–0:55, 1:09–1:25, 1:58–2:30, 4:07–4:38.
- **Luật giữ/bỏ:** thước xếp Tập 1 không thấp nhất → **bỏ**. Thước không đo được Tập 1 → giữ chỉ báo, ghi "chưa có đối chứng âm".

## Bảng xếp hạng

| Thước | Tập 1 (âm) | Tập 4 v3k | Tập 5 | Đối chứng dương | Xếp đúng? | Kết luận |
|---|---|---|---|---|---|---|
| **Nhịp trên spine** — quãng có lời không cú máy/không vật đổi trạng thái > 8 s (`spine_pace.py`) | không đo được (không có spine) | **0** quãng | **6** quãng (dài nhất 16,4 s, 4:25.7–4:42.2) | C4 @ b70a0db: 6 quãng, **trúng 2/4** (1:09 ✓, 4:07 ✓; 0:44 ✗, 1:58 ✗) | — | **GIỮ chỉ báo, chưa hiệu chuẩn** (đối chứng dương 2/4; A23 chưa thành luật) |
| ↳ biến thể chỉ cú máy + cắt | — | 1 | 19 | C4: 18 quãng, trúng 4/4 | — | không phân biệt (bắt mọi thứ) → không dùng |
| ↳ biến thể đo trên video (chênh khung 0,5 s < 0,3/255) | 0,51 quãng/phút | 0 | 0,13/phút | C4: trúng 1/4 | đúng | đối chứng dương 1/4 → không dùng |
| **Đa dạng khung nhìn** — máy quay (`viewpoints.py camera`) | **20** khung, 2,0/phút, cụm lớn nhất **58,5 %** | không có `camera.json` | **104** khung, 13,4/phút, cụm lớn nhất **6,8 %** | — | **đúng** | **GIỮ chỉ báo** |
| ↳ tư thế máy đặt tên trên spine (`viewpoints.py spine`) | — | 8, 6,9/phút, cụm 30,7 % | 33, 4,3/phút, cụm 6,8 % | — | — | chỉ báo phụ (đoạn 70 s không so được với cả tập) |
| **Chấm mù khung** — 3 người chấm headless có ảnh, 60 khung trộn (`blind.py frames`) | **6,20** (R1 6,19 · R2 5,99 · R3 6,42) | 5,35 (5,86 · 5,57 · 4,62) | **4,88** (4,59 · 4,64 · 5,42) | — | **SAI** (3/3 người chấm cho Tập 1 > Tập 5) | **BỎ** |
| **Xem liền mạch mù** — 3 người xem headless, tờ khung 2,5 s + lời (`blind.py flow`) | liền mạch 5,67 · 1,32 điểm chung/phút (13) | 5,67 · **3,45**/phút (4) | **7,67** · 0,39/phút (3) | — | **SAI** (v3k ≤ Tập 1) | **BỎ** |

Mục 14 (cine-lab Q28, Q30), cùng mẫu: xem phần cuối.

## Đọc kết quả
- **Nhịp trên spine.** "Thay đổi" trên spine gồm cả mốc vật thể đổi trạng thái rất nhỏ (một nhãn số đổi, một chồng lớn thêm) mà người xem thấy là đứng hình → bắt được 2 quãng có cú máy thưa, trượt 2 quãng có hoạt ảnh nhỏ (0:44 ba khối trụ đứng im nhưng có mốc hiện; 1:58 cận cảnh 32 s có đường vẽ dần). Bỏ mốc vật thể thì bắt đủ 4 nhưng báo 18 quãng ở C4 và 19 ở bản cuối đã duyệt L3 — không phân biệt. **Chưa có định nghĩa "đổi mang nghĩa" đo được trên spine**; cần cờ độ lớn thay đổi ở beat (vd `change: major|minor`) — việc của bên dựng Tập 6, rồi hiệu chuẩn lại. A23 giữ trạng thái `mở`.
- **Đa dạng khung nhìn.** Xếp đúng và đúng chiều lý do cine-lab (tập 1 cine-lab 52 khung → tập 6 19): Tập 1 Crux 58,5 % thời lượng ở một khung (khung đồ thị phẳng H3 cố định). v3k không đo được bằng máy quay (đoạn Mốc V dựng trước khi nhà máy ghi `camera.json`).
- **Chấm mù khung — bỏ.** Người chấm ưa khung 2D chữ to, rõ của Tập 1 hơn khung thế giới 3D (đúng điều cine-lab #73/#71 cảnh báo: thước tự tạo kết luận). Không dùng làm ngưỡng hay chỉ báo; gu hình vẫn do L3.
- **Xem liền mạch mù — bỏ.** Người xem coi mỗi lần chuyển chế độ thế giới ↔ đồ thị (D-010, thiết kế đã duyệt) là "đổi phong cách": đoạn v3k 70 s có 4 lần → 3,45/phút. Điểm chung của Tập 5 (59 s ident; 4:16; 7:34) chỉ ghi lại, không sửa.

## Token (trần, headless) và giờ máy
Chấm mù khung 0,114 triệu (3 lượt × 60 ảnh); xem liền mạch 0,205 triệu (9 lượt). Thước máy (spine, máy quay, video) 0 token, < 1 phút máy mỗi tập.
