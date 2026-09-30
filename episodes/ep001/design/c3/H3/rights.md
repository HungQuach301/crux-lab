# H3 — Quyền tài sản

Mọi hình trong `F1–F3.mp4`, dải và poster do mã trong `src/` vẽ (canvas 2D) từ dữ liệu dưới đây. Không dùng ảnh, icon, đồ hoạ hay âm thanh của bên thứ ba. Không tải hay chép tham chiếu (Vox, 3Blue1Brown, WSJ).

| Tài sản | Loại | Nguồn | Giấy phép (trích nguyên văn) | Phạm vi | Ghi chú |
|---|---|---|---|---|---|
| Inter 400/600/700 (latin woff2) | Font | `toolkit/render/fonts/` (gói @fontsource/inter), mục `F-INTER` trong `RIGHTS.md` gốc | SIL Open Font License 1.1. `RIGHTS.md` gốc ghi "chưa trích nguyên văn; trích trước C5" — H3 không có quyền truy cập văn bản giấy phép trong repo nên **chưa trích**; kế thừa trạng thái của `F-INTER`. | Nhúng vào khung hình render (YT) | Font chỉ nạp qua `@font-face` đường dẫn tương đối; không chép file font. |
| MORTGAGE30US (Freddie Mac PMMS, tuần 2025-12-04 → 2026-09-24) | Dữ liệu | https://fred.stlouisfed.org/series/MORTGAGE30US, mục `D-FRED-1` trong `RIGHTS.md` gốc | FRED: "Copyrighted: Citation required … you may use these data series with proper attribution of the source and acknowledgment that you obtained the data from FRED" (https://fred.stlouisfed.org/legal/) | YT: hiển thị đường và số, ghi nguồn trên khung F1: "Freddie Mac PMMS via FRED". DL: **không** — `src/data.js` sinh cục bộ, nằm trong `.gitignore` (E1-A2). | |
| HMDA LAR 2025 (phí trung vị, khoản vay trung vị) | Dữ liệu | https://ffiec.cfpb.gov/data-browser/ — qua `out/claims.json`, `out/model.json` | Theo `RIGHTS.md` gốc (mục HMDA) | Hiển thị số đã tổng hợp | Chỉ số tổng hợp của tập, không dữ liệu từng khoản vay. |
| Mô hình tái cấp vốn | Mã/số của dự án | `episodes/ep001/model/`, `out/model.json` | Của dự án | — | `build_data.py` tính lại dư nợ theo cùng quy ước và assert khớp claim. |
| Mã `src/*` | Mã | Viết mới cho H3 | Của dự án | — | Tự viết; không dùng `toolkit/render/` engine. |

Không có tài sản nào cần chủ dự án quyết thêm cho H3 (không screenshot báo, không tài liệu liên bang, không bản đồ).
