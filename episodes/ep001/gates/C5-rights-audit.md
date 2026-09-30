# C5 — Rà quy ước quyền §8 (P2, 30/09/2026)

Khoá kiểm: K3.3 `beffb49b…` (main `c6bdaea`), SHA tính lại khớp `checks/LOCK`.

**1. Tìm `data:` trong mã dựng và bản dựng trang** (`grep -rE "data:(image|font|audio|video|application)"` trên `animatic/`, `design/`, `out/page.json`, `toolkit/`):
- Trang dựng tập (`animatic/film.html`, `animatic/src/*`, `build/film.js`): **0**. Phông Inter nạp bằng file (`toolkit/render/fonts/*.woff2`), đã khai trong `out/visual-assets.json`.
- 2 chỗ có `data:` nằm ngoài bản dựng tập: `design/c3/H2/src/render.js` (trang xem thử hướng H2 ở C3, không chọn) và `design/c3/final/src/cards.js` (thẻ hợp đồng hình C3). Cả hai chỉ nhúng Inter (OFL, đã khai F-INTER) và ảnh do dự án tự render; không vào video phát hành.

**2. Nguồn đầu vào của bước ghép hậu kỳ** (`out/video.mp4` = hình + tiếng):
| Đầu vào | Nguồn | RIGHTS.md |
|---|---|---|
| Hình 1080p | render của trang dựng (`animatic/src`, three.js MIT, Inter OFL) | F-INTER; three.js ghi trong `out/rights.json` |
| Lời đọc | ElevenLabs Eric `eleven_v3` (take theo cảnh, `out/voice/takes.json`) | V-ERIC (ToS 31/3/2026 §(c)(ii), gói Creator) |
| Nhạc, tiếng dữ liệu, room tone | sinh bằng mã `work/audio/src/mix.py` (numpy, không mẫu) | A-MUSIC |
| Số liệu trên hình | FRED MORTGAGE30US, CFPB HMDA | D-FRED-1, D-HMDA |

Không có lớp phủ, clip chèn hay âm thanh nào khác ở bước ghép.
