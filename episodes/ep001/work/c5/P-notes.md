# C5 · Luồng P (hình) — ghi chú

## TIẾP TỤC Ở ĐÂY (cập nhật sau mỗi chặng)
- 30/09 01:25 — Commit: `dc4894d` (sửa hình, CHECKS, page/camera/tokens), `bea45a6` (render_c5.sh, assemble_c5.py), `1c950f8`/`cd15ae6` (ảnh trước/sau ghi chú gốc tiền `review-c5/basis/`, camera.json theo định thời mới b5b91f1: 17 739 khung).
- Định thời mới (P2 `b5b91f1`, S18 lời mới): `build/film.js` dựng lại 01:04. Cảnh dựng bằng bundle cũ: S10, S17, S02 (không đổi nội dung: định thời cục bộ S01–S17 y hệt) và S20 cũ (lệch pha lấy mẫu 0,02 s → đang render lại ở hàng 4). S18 cũ bị dừng ("FAILED S18" 01:04 là cố ý), đã render lại.
- Chặng 2 đang chạy: 4 hàng đợi. Chạy lại khi container khởi động lại (render.js bỏ qua cảnh có mp4+log mới hơn build/film.js; S10/S17/S02 cũ hơn build → nếu phải chạy lại, `touch work/c5/scenes/S10.mp4 work/c5/logs/S10.json` … là đúng vì nội dung không đổi, hoặc để render lại):
```
cd episodes/ep001 && R=animatic/src/render_c5.sh; L=work/c5/logs
nohup $R S10 S06 S14 S07 S09 S03 > $L/queue-1.txt 2>&1 &
nohup $R S17 S02 S16 S01 S05 S13 S12 > $L/queue-2.txt 2>&1 &
nohup $R S20 S18 S04 S08 S15 S19 S11 > $L/queue-3.txt 2>&1 &
```
- Mã hoá giao bản (P2 duyệt 01:10): trung gian CRF 8; giao bản CBR 24 Mb/s nal-hrd=cbr (F04 ≥ 16 Mb/s đo từ gói) + dither luma `noise=c0s=3:c0f=t` (F08: S17 61 % → 0 %); `--probe-crf` ghi CRF 16 tốn bao nhiêu mỗi cảnh.
- Sau render: `python3 animatic/src/assemble_c5.py --picture-only --probe-crf` → chờ `out/audio/master.wav` mới hơn 00:56 30/09 (P2 trộn lại 17 740 khung) → `python3 animatic/src/assemble_c5.py --mux-only` → `python3 animatic/src/check.py`.

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
