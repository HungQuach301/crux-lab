# H2 · Quyền tài sản (C3, 01/10/2026)

| Tài sản | Nguồn | Giấy phép / điều khoản | Phạm vi trong H2 |
|---|---|---|---|
| Phông Inter 400/600/700 (woff2) | `toolkit/render/fonts/` (đã có trong repo, giấy phép `toolkit/render/fonts/LICENSE-Inter-OFL-1.1.txt`) | SIL Open Font License 1.1 | mọi chữ trên khung, dải, thumbnail; nạp bằng `@font-face` từ đường dẫn cục bộ, không nhúng `data:` |
| Token màu/chữ | `episodes/ep001/design/c3/final/tokens.json` (Crux, tự làm) | của dự án | đọc trực tiếp khi render, không chép |
| Chuỗi lãi T-bill 3 tháng (TB3MS, Board of Governors H.15, qua FRED) | `episodes/ep002/data/raw/TB3MS.csv` (tải 01/10/2026, SHA-256 trong `data/sources.json`) | FRED: "Public Domain: Citation Requested" | dải địa hình, mọi đường thả nổi, kết quả các thùng; dữ liệu suy ra nằm trong `work/data.js` (**không commit**, `.gitignore` của thư mục) |
| Kết quả mô hình | `episodes/ep002/out/claims.json` (Crux) | của dự án | mọi số trên hình qua `CL(claimId)` |
| Mã dựng (`src/*.js`, `src/*.py`, `src/render_all.sh`) | viết mới cho H2; khung `engine.js`/`render.js` theo mẫu mã Tập 1 (`episodes/ep001/design/c3/final/src/`, Crux) | của dự án | — |
| Công cụ | Chromium headless (Playwright, `/opt/pw-browsers`), ffmpeg/libx264 trên máy | chỉ là công cụ; không đóng gói vào sản phẩm | render khung, mã hoá H.264 |

- Không có ảnh, video, âm thanh, biểu tượng, logo hay thương hiệu bên thứ ba; mọi hình vẽ bằng canvas 2D từ mã.
- Không tài sản bên thứ ba dạng `data:` (chỉ dùng `toDataURL` để chuyển khung PNG từ trình duyệt ra đĩa).
- Không dùng, không tải, không trích khung từ ba video tham chiếu (`playbook/references.md`); "hình mang nghĩa" chỉ là tinh thần.
- Không âm thanh (clip câm).
