# C5 · Luồng P (hình) — ghi chú

## TIẾP TỤC Ở ĐÂY (cập nhật sau mỗi chặng)
- 30/09 02:15 — K3.3 (LOCK beffb49b) đã vào main → **BASIS_MODE mặc định = corner** (engine.js, render.js; `out/page.json` giữ `animatic/film.html`, mặc định là góc). `build/film.js` dựng lại 02:12. Bản near (đã render đủ 17 cảnh 00:41–02:08, log `near-queue-*.txt`) bỏ.
- Chặng 3 đang chạy: render lại bản góc mọi cảnh có số $ (tất cả trừ S05; S05 giữ bản render định thời mới, log đánh dấu `basisMode: corner` vì không có số $), 2 hàng đợi (giới hạn bộ nhớ: mix của A cần ~10 GB, `work/audio/src/mix_after_render.sh` chờ khi không còn `node render.js`). Chạy lại nếu container khởi động lại (bỏ qua cảnh đã xong):
```
cd episodes/ep001 && R=animatic/src/render_c5.sh; L=work/c5/logs
nohup $R S10 S04 S06 S01 S09 S14 S08 S19 S11 S12 > $L/queue-c1.txt 2>&1 &
nohup $R S02 S20 S17 S18 S16 S15 S07 S03 S13 > $L/queue-c2.txt 2>&1 &
```
- Mã hoá giao bản (P2 duyệt): trung gian CRF 8; giao bản CBR 24 Mb/s nal-hrd=cbr (F04) + dither luma `noise=c0s=3:c0f=t` (F08: S17 61 % → 0 %); `--probe-crf` ghi CRF 16 tốn bao nhiêu mỗi cảnh.
- Sau render: `python3 animatic/src/assemble_c5.py --picture-only --probe-crf`; khi `out/audio/master.wav` mới hơn dòng "=== XONG" của log mix: `python3 animatic/src/assemble_c5.py --mux-only`; rồi `python3 animatic/src/check.py`; báo P2.

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
