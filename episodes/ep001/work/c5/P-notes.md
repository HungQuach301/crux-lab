# C5 · Luồng P (hình) — ghi chú

## TIẾP TỤC Ở ĐÂY (cập nhật sau mỗi chặng)
- 30/09 05:15 — Render bản góc xong 20/20 (02:13–03:36 UTC, 2 hàng đợi, log `queue-c*.txt`; `logs/S*.json` commit `da54dac`); `check.py` ALL OK (`259ff5c`). Ghép lần 1 (c0s=3, tune animation) + mux với master 03:49 → `out/video.mp4` đạt F01–F07, F10, A01/A02/A04–A06 nhưng **F08 5,19 %** (> 5). Đang ghép lại: dither c0s=4 + `-tune grain` (thử S16: 0,0 %), rồi mux lại (ghi đè nguyên tử `out/video.mp4`).
- Nếu container khởi động lại: `cd episodes/ep001 && nohup python3 animatic/src/assemble_c5.py > work/c5/logs/assemble-full.txt 2>&1 &` (ghép + mux, ~70 phút), rồi kiểm tệp: `python3 <main>/checks/py/run.py episodes/ep001 --only F01,F02,F03,F04,F05,F06,F07,F08,F10,A01,A02,A04,A05,A06 --first` (ffmpeg trong PATH; hoàn lại `out/checks/report-partial.*` sau đó, không phải của P).
- Mã hoá (P2 duyệt): trung gian CRF 8; giao bản CBR 24 Mb/s nal-hrd=cbr (F04) + dither luma; AAC 320k (đo 285,8 kb/s), không chapter, không metadata.

## Dựng lại trang (không commit `build/`, `src/data.js`)
```
cd episodes/ep001/animatic && npm ci && node src/build_page.mjs          # build/film.js (esbuild: src/ + three 0.186.1)
python3 src/build_data.py                                              # src/data.js (FRED/HMDA cục bộ, không commit)
NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node src/export_camera.js   # out/camera.json
```

## File trang nạp (F12 · `out/checks/page.json → resources`)
| File | Loại | Ghi chú |
|---|---|---|
| `animatic/film.html` | document | trang dựng (`out/page.json.url`) |
| `animatic/src/data.js` | script | số liệu FRED/HMDA + claims dựng bởi `src/build_data.py` (không commit) |
| `animatic/build/film.js` | script | bundle esbuild của `src/*.js`, `timing.json`, `anchors.json`, `src/tokens.json`, three.js 0.186.1 (MIT) |
| `toolkit/render/fonts/inter-latin-{400,600,700}-normal.woff2` | font | Inter, OFL 1.1 (họ "Inter", khai trong `out/visual-assets.json`) |

Không ảnh, không texture file, không mô hình 3D file: mọi hình 3D dựng bằng mã (three.js), texture vẽ bằng canvas trong trang. Không URI `data:` nào được nạp (bundle chỉ có mã three.js kiểm tra chuỗi `data:`).
