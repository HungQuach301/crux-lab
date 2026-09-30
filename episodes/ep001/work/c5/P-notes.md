# C5 · Luồng P (hình) — ghi chú

## TIẾP TỤC Ở ĐÂY (cập nhật sau mỗi chặng)
- 30/09 00:40 — Chặng 1 xong, commit `dc4894d` (sửa hình, S07/S08/S09 trên hình, CHECKS, page.json, camera.json, tokens). `build/film.js` cuối dựng 00:3x: **không dựng lại** trước khi render xong (render.js coi mọi cảnh cũ hơn `build/film.js` là hết hạn).
- Chặng 2 đang chạy: render 1080p, 3 hàng đợi từ 00:40 UTC. Tiếp tục (bỏ qua cảnh đã xong) — chạy lại đúng lệnh này:
```
cd episodes/ep001 && R=animatic/src/render_c5.sh; L=work/c5/logs
nohup $R S10 S06 S14 S07 S09 S03 > $L/queue-1.txt 2>&1 &
nohup $R S17 S02 S16 S01 S05 S13 S12 > $L/queue-2.txt 2>&1 &
nohup $R S20 S18 S04 S08 S15 S19 S11 > $L/queue-3.txt 2>&1 &
```
- Sau render: `python3 animatic/src/assemble_c5.py` (ghép `work/c5/picture-1080.mp4` + mux `out/video.mp4`), `python3 animatic/src/check.py`, rồi D chạy `build.py`.

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
