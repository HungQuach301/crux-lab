# C5 · Luồng P (hình) — ghi chú

## TIẾP TỤC Ở ĐÂY (cập nhật sau mỗi chặng)
- 30/09 C6 — **ĐANG CHẠY.** Chủ dự án: dòng chân "Dollars of the day = …" giữ S01, bỏ S06/S07 (commit `2cd1865`, bản góc: `nb(…, 'Nora is illustrative.')`, nhánh near giữ nguyên). Quét đối tượng K3.3 S09 (objrules.js origin/main, bản sao nháp) S01/S06/S07: 0 thiếu, chân S06/S07 = "Nora is illustrative." (`work/c5/logs/c6-s09-scan.txt`). Render lại CHỈ S06 S07 (1 hàng đợi, `logs/queue-c6.txt`), rồi `animatic/src/c6_pipeline.sh` (nohup, tiếp tục được: bước nào đầu ra mới hơn đầu vào thì bỏ qua; chờ tối đa 150 phút, thoát nếu hàng đợi chết): check.py → `assemble_c5.py --picture-only` → `--mux-only` (master hiện tại) → luật tệp K3.3 (`CHK=<nháp>/checks` bản sao origin/main, LOCK beffb49b) → `logs/c6-*.txt|json`, sha256 `logs/c6-sha256.txt`. Nếu container khởi động lại: `npm ci && node src/build_page.mjs` (film.js mới hơn S06/S07 cũ), `nohup animatic/src/render_c5.sh S06 S07 > work/c5/logs/queue-c6.txt 2>&1 &` rồi `CHK=… nohup animatic/src/c6_pipeline.sh > work/c5/logs/c6-pipeline.txt 2>&1 &`.
- 30/09 06:10 — **XONG.** `out/video.mp4` (không commit, .gitignore; sha256 bắt đầu `991e196a7bd80516`): 1920×1080 H.264 High yuv420p BT.709 tv, 30/1 CFR, 17 739 khung = 591,3 s, video CBR 24,0 Mb/s (dither luma c0s=4 + tune grain), AAC-LC 48 kHz stereo 285,8 kb/s đo, 0 chapter. Luật tệp K3.3 (LOCK beffb49b): F01–F08, F10, A01, A02, A04–A06 ĐẠT 14/14 (F08 trước sửa 5,19 %). Hình: `work/c5/picture-1080.mp4`; manifest `work/c5/logs/assemble.json`. `check.py` ALL OK.
- Còn mở: `--probe-crf` (CRF 16 mỗi cảnh tốn bao nhiêu) chưa chạy (~60 phút máy); sampler trang toàn phim + run.sh đầy đủ là việc của P2.

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
