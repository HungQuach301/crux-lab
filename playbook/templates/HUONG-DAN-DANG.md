# Hướng dẫn đăng — Tập {N}

Mẫu chuẩn mỗi tập (Mốc B, theo `episodes/ep003/HUONG-DAN-DANG.md`). P3 điền sau G2. Chủ dự án làm theo ở G3.

## File
- **Video:** `ep{NNN}-youtube.mp4`. Ghép các phần trên nhánh tạm `ep{NNN}-delivery` theo lệnh trong `JOIN.md`. SHA-256 phải là `<sha>`, mã hoá từ bản gốc `<sha bản gốc>`.
- **Tiêu đề:** **<mã>** "<tiêu đề>".
- **Mô tả và chương:** `episodes/ep{NNN}/out/package/description.md`. Dán nguyên văn; chương dạng `m:ss Tiêu đề`, bắt đầu 0:00.
- **Phụ đề:** `episodes/ep{NNN}/out/captions.srt` (tiếng Anh).
- **Thumbnail:** **<T?>** mặc định; **Test & Compare:** <T1, T2, T3> (`out/package/thumb-1..3.png`).
- **Mid-roll:** đặt đúng mốc trong `out/adbreaks.json`. Không có mốc nào trong 2 phút đầu hay 2 phút cuối.
- **Shorts:** `out/shorts/short-1..3.mp4`. Mỗi Short có tiêu đề riêng (trong `out/shorts/README.md`) và gắn link video chính (Related video).

## Trước khi bấm đăng: claim có hạn dùng
Liệt kê mọi claim phụ thuộc ngày đăng (lãi công bố theo kỳ, luật có hiệu lực từ ngày …). Với mỗi claim:
- **ngày đăng trước <ngày>:** giữ nguyên;
- **từ <ngày>:** cập nhật theo nguồn chính thức → `numbers.md` + `out/claims.json` → mô tả → một dòng `ledger.md`. Lời/hình chỉ sửa khi câu sai nghĩa; khi đó là ngoại lệ, hỏi lại.

## Giữ nguyên (đã quyết ở G2)
Các lỗi CHÍNH đã giải thích trong `out/explanations.json` (hàng chờ) — liệt kê id + một dòng.

## Sau khi đăng (G3)
- Ghi link video, ngày đăng vào `episodes/ep{NNN}/audience.md`.
- Báo phiên đã đăng và tải xong → phiên xoá nhánh giao (proxy chặn → chủ dự án xoá: GitHub → Branches → Delete).
- Mốc 7 ngày: một ảnh chụp YouTube Studio cho chat chiến lược (`playbook/templates/audience.md`).
