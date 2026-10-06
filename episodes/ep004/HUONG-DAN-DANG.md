# Hướng dẫn đăng — Tập 4

Theo G2 của chủ dự án (2026-10-06, `gates/G2-answer.md`, issue [#41](https://github.com/HungQuach301/crux-lab/issues/41)): phương án (b) một vòng; cổng gốc vòng 2 **6/7 ĐẠT** (`gates/C4-root-r2.md`).

## File
- **Video:** `ep004-youtube.mp4` — ghép 3 phần trên nhánh tạm [`ep004-delivery`](https://github.com/HungQuach301/crux-lab/tree/ep004-delivery) @ `f01ff9b` theo `JOIN.md`. SHA-256 phải là `30090de0f5260238c87d186c7727e1b32ecba411892e399c565c8fe53e6fbd73` (243.200.494 byte; 1080p 8 Mb/s), mã hoá từ bản gốc `82120cfc52fc2f1a9ee3885a0fbe6be795333444e340e06900e7aa6f5e0c9d09`. Dài 8:01,6.
- **Tiêu đề:** **T1** "Bought Your Home in 2000? The $500,000 Tax-Free Limit Test".
- **Mô tả và chương:** `episodes/ep004/out/package/description.md` — dán nguyên văn; 10 chương dạng `m:ss Tiêu đề`, bắt đầu 0:00. Dòng nguồn: "FHFA House Price Index via FRED".
- **Phụ đề:** `episodes/ep004/out/captions.srt` (tiếng Anh).
- **Thumbnail:** **T1** (`out/package/thumb-1.png`, "11 of 12 / metros past the cap") mặc định; **Test & Compare: T1, T3, T2** (`thumb-1..3.png`).
- **Mid-roll:** đúng mốc `out/adbreaks.json`: **3:00 (180,05 s)** và **5:49 (349,30 s)** — cả hai cách đầu/cuối ≥ 2 phút; nhạc đã hạ về 0 quanh mốc.
- **Shorts** (không commit — `out/shorts/` dựng lại bằng lệnh trong `gates/C6.md`; tải từ phiên nếu cần): SH1 (S06, 35,1 s) "A fixed cap vs a rising gain" · SH2 (S10, 22,5 s) "12 cities, one price" · SH3 (S11, 25,7 s) "Over the cap once ≠ for good". Mỗi Short gắn link video chính (Related video).

## Trước khi bấm đăng: claim có hạn dùng
- **Chỉ số FHFA (mọi ngưỡng, lãi, quý vượt):** dữ liệu đến **quý 2/2026**. FHFA công bố quý 3/2026 khoảng cuối tháng 11/2026 và sửa các quý cũ. Lời (S18.2) và mô tả đã nói "revised every quarter", nên **đăng trước hay sau đợt công bố đều giữ nguyên**; không cập nhật số.
- **Giới hạn $500,000 / $250,000 (26 U.S.C. 121):** không đổi từ 5/1997. Nếu luật đổi trước ngày đăng → dừng, hỏi lại (sai nghĩa).
- **CPI-U tháng 8/2026** (≈ $1,046,000 ở S08): giá trị lịch sử, không hết hạn.

## Giữ nguyên (đã quyết ở C4/G2) — `out/explanations.json`
- Luật trang S02, S06–S09, S17, C07, V03, V08, V09, V11, V12, C02, C05, C14; **F11, F12**: ngoại lệ Tập 4 (nhà máy chưa xuất `page.json`) — việc treo lô K.
- **S03/S04:** FRED làm nguồn (fhfa.gov bị proxy chặn). **L1:** không có lớp sonify.
- **B11** (S11, Miami) trượt cổng gốc vòng 2 (nhãn trục bị đọc là giá trị nhà) — phát hành có ghi, không vòng 3. **S18** giữ (kiểm mù 2/4). EL 11.702 ký tự.

## Sau khi đăng (G3)
- Ghi link video, ngày đăng vào `episodes/ep004/audience.md`.
- Báo phiên đã tải xong → phiên merge `ep004` vào `main` và xoá `ep004-delivery` (proxy chặn xoá → chủ dự án xoá: GitHub → Branches → Delete).
- Mốc 7 ngày: một ảnh chụp YouTube Studio cho chat chiến lược (`audience.md`).
