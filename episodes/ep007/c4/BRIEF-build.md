# C4 Tập 7 — lượt 1/2 (bên dựng, 11/10): khung cả tập + đoạn a (S01–S03 + ident), b (S04–S09). Chưa render

## Tệp
- `episode.yaml` (`scope: full`, `res: 720`, 33 cảnh + đuôi, 6 hồi theo `=== … ===`, `audio` ident/close, 2 mid-roll, 4 đối trọng, `world:` 7 đoạn, 3 Short nháp)
- `contract.json` (giữ `model`, `lock`, `format`; điền `characters`, `claims`, `coverage`, `data`, `sonification`, `shorts`, `artefacts`; bỏ `pending`)
- `c4/build_inputs.py` (gen + `--timeline` khô 0 ký tự EL + `--bed` + `--out`), `c4/smoke/` (kiểm khai scene.js không render + giờ hiện nhãn so với cue)
- `world/c4kit.{py,js}`, `world/music/{tension,bed}.py`, `world/derive.py` (+12 chuỗi hiển thị), `world/wlib.py` (take cả tập `review-g1/voice-scenes.json`)
- `world/c4/a-s01-s03/`, `world/c4/b-s04-s09/` (spine.py + scene.js); `world/c4/{c,d,e,f,g}-*/` = khung tối thiểu (`c4kit.stub`/`stubScene`) cho lượt 2

## Số đo
- Timeline khô nhà máy **602,70 s (10:02,7)**, 33/33 take trúng cache, EL 0 ký tự. Đoạn: a 0–54,93 · b 54,93–189,33 · c –294,17 · d –358,60 · e –442,70 · f –489,20 · g –602,70.
- MR1 **188,58 s** (lời S09 hết 187,833; cả bản trộn lặng [187,93; 189,33] = 1,40 s) · MR2 **441,94 s** (lời S24 hết 441,187; lặng [441,29; 442,70] = 1,41 s; 160,8 s tới cuối).
- Số neo (lặng 0,75 s trong đuôi cảnh trước): S06.1 "$2,948 a month", S18.1 "$20,374", S28.1 "about 1 week in 5".
- `spec.py --duration 602.7`: OK · `comment_guard`: OK · `numbers_said`: ≤ 2 số mới/cảnh · spine a, b: quy tắc 2/3/7 OK, lặng neo/MR1 không âm, không `land` đè từ khoá.
- Kiểm khai (`c4/smoke/run.mjs`, 0,1 s): a 550 khung, b 1.345 khung — 0 lỗi JS, 0 vi phạm quy tắc 1, 0 khung đồ thị trong 5 s đầu, 0 chữ < 48 px,
  0 hộp chữ giao nhau, 0 chữ số ngoài claim, mọi nhãn ≥ max(1 s, từ/3); nhãn hiện sau cue +0,08…+0,17 s (lấy mẫu 0,1 s).
- SH06 (Inter Bold 64 px, rộng 936): SH1 "The price of a fallback" 700 px · SH2 "Same payment, months late" 872 px · SH3 "What an extra dollar earns" 829 px — 1 dòng.

## Hàng chờ C4 (gates/C3.md §3) đã làm
- **Tessa** (`c4kit.js figure/gesture`): người W4 tròn xoay → quay đầu không thấy; thêm cánh tay (buông dọc thân), cử động = nghiêng người / giơ tay / gật,
  mỗi cái là sự kiện `S.gestures` đúng lúc vật chạm/dâng: a 5 (bó chạm 5,94; thẻ 30 năm; tờ đô la; lãi 7.40%), b 12 (thanh 30 năm dâng, khoảng đường lui, dâng qua vạch, chồng dựng, tháp lãi, 15 bó đáp).
- **S01**: nhãn giá ở **5,94 s** (máy vào đồ thị 5,00–5,52); chồng **đúng một bó** (dừng sau bó đầu); khoản vay $320,000 = **tấm giấy vay** (`LoanTag`, cột + tấm trước góc nhà,
  hiện ở "borrowing") mang nhãn "$320,000 loan · week of Oct 8, 2026"; bó duy nhất ra cửa → chồng, sau 5,94 s không vật nào ở cửa.
- **S06**: chồng chỉ dựng từ "Over" (15 bó, nhịp 0,16 s, xong trước "twenty-one"); nhãn $2,948 **đúng "forty"** (đỉnh qua vạch "forty" − 0,08 s; đồ thị từ 48,45 s để "required"
  hiện 2,1 s trước khi dâng); **đẩy máy vào đỉnh thanh** (lát warn ≈ 47 px ở 1080 / 23 px ở 540, trước ≈ 8); "same" = lát **tách, lơ lửng** đúng từ (cue hình mới, nốt dữ liệu);
  thang thanh 1/980 → đỉnh 3,01, chồng 15 bó 2,55 **thấp hơn**, đứng cách 1,15 về trái, nhãn riêng hai dòng lệch trái.
- **Âm**: mật độ sfx a 16,4/phút, b 16,5/phút, tối đa 5 trong 10 s; `land` của đổi chế độ không đè đầu từ khoá (kiểm trong `c4kit.finish`).

## Lệnh dựng (từ gốc repo; phiên chính chạy nền)
```
python3 episodes/ep007/world/derive.py
python3 episodes/ep007/c4/build_inputs.py --timeline            # gen + out/factory/timeline.json + work/factory/music/bed.wav (0 ký tự EL)
python3 toolkit/tests/comment_guard.py episodes/ep007/world
for s in a-s01-s03 b-s04-s09; do python3 episodes/ep007/world/c4/$s/spine.py && \
  node --import ./episodes/ep007/c4/smoke/register.mjs episodes/ep007/c4/smoke/run.mjs $s; done
for s in a-s01-s03 b-s04-s09; do python3 toolkit/factory/world/build_seg.py episodes/ep007/world/c4/$s --res 720 \
  --out episodes/ep007/work/factory/world/$s-720.mp4; done              # cùng đường ra với bước world của build.py → cache dùng lại
for s in a-s01-s03 b-s04-s09; do python3 toolkit/factory/world/sync_audit.py episodes/ep007/work/factory/world/$s-720.mp4 \
  episodes/ep007/work/factory/world/$s-720.sync.json --spine episodes/ep007/world/c4/$s/spine.json; done
# cả tập (sau lượt 2): bash toolkit/build.sh episodes/ep007/episode.yaml && python3 episodes/ep007/c4/build_inputs.py --out
```
