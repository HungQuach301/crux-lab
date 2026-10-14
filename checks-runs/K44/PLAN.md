# PLAN Phiên K lô Tập 8 (K4.4 + K4.4b, K4.4.1 chưa khoá) — đóng 14/10/2026 (≤ 1 trang)

**Nhánh:** `checks-k44` (từ `main` @ `c7358285`, merge `main` tổng kết Tập 7 @ `3489318`) · **Khoá:** K4.4 LOCK `a35970a8…` → K4.4b LOCK `b4551642…` (trên `main`).

## 1. Trạng thái
- **K4.4 (tự khoá, `main` @ `44229bc1`):** A33 (A12/A13/R01 lỗi máy), A38 (SH07 1 Short; F11/P01 `package.thumbnails`, 0 từ Tập 8), A39 + A44 (F13 CHẶN, F15 CHÍNH; đối chứng thật ảnh LoC 1936), A40 (nguyên tắc; báo cáo lỗi thật/pháp lý/thủ tục), A41 (a) bộ lấy mẫu đọc nháp ≠ 1080p, (b) R09; A42 (mẫu check_script 4/5 cột); A45 → S23 CHÍNH; A43 → nhánh nhà máy. Python 440/440, trang 67/67. REVIEWER ĐẠT có sửa (đã sửa), $1,63.
- **Gói (13/10) → trả lời 14/10: 1a, 2a, 3a → K4.4b (`main` @ `7f8a0da1`):** A14 medium.en cho tên riêng sở hữu cách; S02 hồi `limits`/`methodActs`; S07 `termNames`; S09 tập chỉ danh nghĩa không cần nhãn hình; cổng gốc so hai bản = chẩn đoán; sửa rò ffmpeg bộ lấy mẫu. Tập 7: A14, S02 FAIL→PASS; S07 52→18, S09 2.384→0 khung khi bên dựng khai. Python 448/448, trang 67/67. REVIEWER ĐẠT có sửa (đã sửa), $1,10.
- **A32 (đo, $6,32):** 3 lượt đọc lại master Tập 6 = 20/16/19 trên 23; luật ghi trước không đạt đối chứng.
- **K4.4.1 (A29) — CHƯA KHOÁ:** Tập 6 trùng byte (ấm 65 s thay 6.615 s); Tập 7 không trùng byte vì hai lượt --no-cache cũng khác nhau; 33 luật trang trùng mọi chỉ số (`a29/RESULT.md`).

## 2. Việc tiếp (≤ 3) và treo
1. Chủ dự án chọn tiêu chí A29 (`checks-appeal.md` hàng chờ K4.4 mục 2): (a) khoá `a29/K441-A29.patch` theo "cache = lượt đã điền + mọi luật trùng"; (b) sửa nguồn không tái lập rồi đo lại.
2. Lô K sau: hiệu chuẩn cổng gốc 5 người đọc/nhịp (đối chứng dương mạnh, ghi trước ngưỡng, ≈ $15–20).
3. Bên dựng Tập 8: footage khai `external[]` + RIGHTS §F6 (cột Bậc); hợp đồng khai `termNames`/`basis` khi cần; `package.thumbnails: 0` (đã có).
- Treo: A41 (a) đối chiếu 540p/1080p; A43 (nhà máy); REVIEWER K4.4b PHỤ 8 (try/finally sampler, cùng A29).

## 3. Quyết định đã có
13/10 lệnh mở phiên + cập nhật (A38–A45, A39 thay luật footage, A40 nguyên tắc) · 14/10 gói 1a, 2a, 3a.

## 5. Chi
Console (headless): A32 $6,32 + REVIEWER K4.4 $1,63 + K4.4b $1,10 = **$9,05** (trần $15). 0 agent con. Tải medium.en ≈ 1,5 GB (Hugging Face).
