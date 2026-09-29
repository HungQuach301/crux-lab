# Tập 1 · C4 — Animatic có chuyển động (toàn tập, S01–S20)

ANIMATIC C4, 29/09/2026. Dựng theo hệ hình đã ký ở C3 (`design/c3/final/system.md`, `tokens.json`, engine `src/engine.js` của C3 final — dùng lại, sửa 4 điểm ghi đầu file) và kịch bản chốt `story/script-v3.1.md`.

**Xem:** `out/animatic-720p.mp4` (9:43,0 · 1280×720 · 30 fps · H.264 + lời tạm AAC · 31,5 MB) · `out/silent-720p.mp4` (không tiếng, cho kiểm mù · 25,0 MB) · dải kiểm mù `strips/Sxx.png` (6 khung/cảnh, lưới 3×2 đánh số 1–6 theo thứ tự đọc; **không** chữ chú thích câu).

## Tệp
| Tệp | Là gì |
|---|---|
| `intent.md` | Ý đồ tắt tiếng từng nhịp (viết và commit **trước** khi render, `fb61ff9`) |
| `timing.json` | Định thời duy nhất animatic đọc: mỗi câu (cảnh, bắt đầu, kết thúc), nghỉ, cửa sổ cảnh. Sinh bằng `src/make_timing.py` từ `out/voice-v31/timeline.json` (TẠM) |
| `anchors.json` | Bảng neo: 146 hành động hình, mỗi cái neo vào câu n + từ khoá (hoặc đầu/cuối câu) + lệch dt; kèm "ý nghĩa khi tắt tiếng" và thời điểm hiện tại. Nguồn: `src/anchors_*.json` → `src/build_anchors.py` |
| `legibility.md` | Kiểm đọc được ở 25% từng cảnh; chỗ trượt/yếu và giải thích |
| `check-report.json` | Kiểm máy từng cảnh: claim ID dùng, 0 số ngoài claim, 0 chuỗi ra vùng an toàn, cỡ chữ nhỏ nhất, neo khai báo/đã dùng, câu-chú-thích, thời gian render |
| `src/` | `engine.js` (C3 final + chữ −20%/sàn 40, 720p, T.a(neo), cờ `sent`), `common.js` (bếp, lá thư, cọc tiền, xấp phí, thước), `table.js` (bàn hoà vốn SF3), `plot.js` (đồ thị SF4), `yard.js` (sân SF5), `s01.js`–`s20.js`, `render.js`, `render_all.sh`, `encode.py`, `assemble.py`, `check.py`, `build_data.py` |

## Định thời thay được (giọng sẽ sinh lại)
Không cảnh nào có giây cứng cho hành động mang nghĩa: mọi hành động gọi `T.a('id')` → câu n + từ khoá trong `anchors.json`, thời điểm tính lại từ `timing.json` lúc render (từ khoá → vị trí ký tự trong câu, nội suy tuyến tính theo thời lượng câu; không tìm thấy → đầu câu, `check.py` báo). Cảnh cắt 0,35 s trước câu đầu của cảnh. Khi có giọng mới:
```
python3 src/make_timing.py <timeline.json mới>    # cùng 105 câu, cùng thứ tự S01–S20
python3 src/build_anchors.py                        # cập nhật thời điểm trong bảng neo, báo từ khoá không thấy
src/render_all.sh && python3 src/check.py && python3 src/assemble.py   # thay review-c4/narration.m4a trong assemble.py nếu đổi file lời
```
Lưu ý: `timeline.json` hiện tại vẫn là lời cũ ở câu 7 ("…where does a loan your size fall?") và câu 10 ("far from alone"); **chữ trên màn hình đã theo bản mới** ("…where would your own loan fall?"). Từ khoá neo của hai câu này ("your", "7 percent") có trong cả bản cũ và mới.

## Cảnh: hướng hình, thời lượng, render
Render: Chromium headless 1194 + SwiftShader (WebGL CPU) cho H1, canvas 2D cho H3; RGBA → PyAV libx264. Máy 4 vCPU, không GPU; chạy 2–3 cảnh song song (số giây máy mỗi cảnh vì vậy cao hơn khi chạy một mình).

| Cảnh | Hướng | Dài (s) | Khung 3D | Giây máy | Máy/giây phim | Khác bảng chọn C3? |
|---|---|---|---|---|---|---|
| S01 Tuần lãi chạm đáy | Kết hợp H3→H1→H3 | 31,8 | 390 | 212 | 6,7 | — |
| S02 Lá thư, câu hứa | H1 | 24,8 | 743 | 252 | 10,2 | — |
| S03 Gần đỉnh | Kết hợp H3→H1 | 18,9 | 295 | 101 | 5,3 | — |
| S04 Nora | H1 | 24,3 | 729 | 227 | 9,4 | — |
| S05 Cửa sổ, vạch 1 điểm | H3 | 42,5 | 0 | 190 | 4,5 | — |
| S06 Đề nghị | Kết hợp H1→H3→H1 | 28,2 | 539 | 234 | 8,3 | — |
| S07 Hoá đơn | Kết hợp H1→H3 | 29,4 | 431 | 209 | 7,1 | — |
| S08 Hai câu trả lời | H3 | 41,7 | 0 | 213 | 5,1 | — |
| S09 Hoà vốn là gì | H1 | 17,3 | 518 | 187 | 10,9 | — |
| S10 Đồng hồ chạy lại | Kết hợp H3→H1 | 49,7 | 972 | 484 | 9,7 | có: thêm đồng hồ 30 năm H3 trước bàn SF3 (kịch bản có đồng hồ) |
| S11 Một phần tư điểm | H3 | 21,8 | 0 | 96 | 4,4 | — |
| S12 Một điểm | H3 | 6,0 | 0 | 26 | 4,3 | — |
| S13 Nửa điểm | H3 | 28,6 | 0 | 117 | 4,1 | — |
| S14 Walt | H1 | 25,6 | 767 | 214 | 8,4 | — |
| S15 Phí không nhỏ đi | Kết hợp H3→H1 | 27,8 | 323 | 201 | 7,2 | có: so ba cặp thanh (vay/phí/tiết kiệm) là đọc thang → H3, rồi cọc $68 tới tháng 75 ở H1 |
| S16 Walt bán sau 3 năm | Kết hợp H1→H3 | 27,1 | 377 | 218 | 8,1 | — |
| S17 Anjali | Kết hợp H1→H3 | 36,1 | 995 | 374 | 10,4 | có: thêm thước rate cut H3 ở câu cuối ("a third of a point") |
| S18 Thước ba mốc | Kết hợp H1→H3 | 45,5 | 116 | 269 | 5,9 | — |
| S19 Điều này không nói | H3 | 25,5 | 0 | 124 | 4,9 | — |
| S20 Câu hỏi ở lại | H1 | 30,4 | 911 | 294 | 9,7 | — |
| **Tổng** | H1 5 · H3 6 · kết hợp 9 | **583,0** | 9 105 / 17 489 | **4 243** (≈ 71 phút máy) | 7,3 | |

Ghép (`assemble.py`: giải mã 20 cảnh, mã hoá CRF 23, gắn lời copy AAC): 287 s. Tổng máy ≈ 76 phút; thời gian tường ≈ 55 phút nhờ chạy song song. Một cảnh được render lại sau sửa (S04, S06–S10, S12, S13, S15) — bảng ghi lần render cuối.

## Số, nhãn, câu hứa
- Mọi số trên màn hình qua `CL(claimId)` → đúng `display` của `out/claims.json`; `check.py` tách mọi token số của mọi chuỗi đã vẽ: **0 số ngoài claim** ở 20/20 cảnh (claim ID từng cảnh: `check-report.json` → `claimsUsed`). Không in số nội suy: không đếm số chạy (bộ đếm 29 tuần = 29 vạch sáng, số chỉ hiện khi đủ), thước tháng chỉ đánh số tháng có claim (18, 24, 30, 36, 38, 75; "3 years", "7 years"), giá trị hồ sơ S04 hiện nguyên số (bản đầu "gõ từng ký tự" in "$375" — đã bỏ). Chiều cao cọc/đường cong lấy từ `model/refi.py` (`src/build_data.py`, có assert với claim), không in.
- **ILLUSTRATIVE** góc trên phải mỗi khi có số của Nora/Walt/Anjali hoặc mốc 3 năm/7 năm.
- Câu hứa trên màn hình (S02, câu-chú-thích): "How big a rate cut makes it worth it for Nora — / and where would your own loan fall? / And why would a smaller mortgage need a bigger cut?".
- S18 thước ba mốc: ba cột rời ($115,000 · $375,000 · $655,000 → 1.12 points · 0.5 point · about a third of a point), không nối; nhà nét đứt "your loan?" trượt và dừng giữa hai mốc, không số; vạch "1-point rule of thumb: fits none"; dòng giả định.
- **Câu-chú-thích** (`sent: true`, 7 chuỗi: "She didn't take it.", câu hứa 3 dòng, "Neither is quite right", "The same line for everyone?", "Back to the letter", "How long do you picture yourself in your home?") có trong video, **bị ẩn trong dải kiểm mù**.

## Giới hạn
- Animatic 720p, chuyển động thô: hình học 3D đơn giản, không chuyển cảnh mềm (cắt thẳng), camera chỉ đẩy chậm; một vài nhãn bay theo vật có thể giật nhẹ. Chưa có ident (≤ 3 s), điểm chèn quảng cáo và thẻ phương pháp/outro sau S20 (không có trong timeline tạm).
- Lời tạm = `review-c4/narration.m4a` (bản ghép từng câu, sẽ sinh lại theo G-015); không nhạc, không hiệu ứng âm.
- Neo từ khoá nội suy theo vị trí ký tự trong câu (chưa có mốc từng từ từ TTS): lệch có thể ±0,3–0,5 s trong câu dài. Khi giọng mới có mốc từng từ (alignment), thay hàm neo trong `engine.js` (`makeT`).
- Kiểm 25% trên khung khó nhất mỗi cảnh (không phải mọi khung); chữ in trên vật 3D không đọc được khi vật xa (có bản chữ phẳng) — `legibility.md`.
- Chưa kiểm mù (P2 chạy trên `strips/` theo `intent.md`).
- Dữ liệu FRED chỉ đọc cục bộ (`src/data.js`, `.gitignore`), không commit; `work/` (cảnh lẻ, log, ảnh 25%) không commit.

## Dựng lại
```
python3 episodes/ep001/data/fetch.py --verify           # nếu thiếu data/normalized/*.csv
python3 episodes/ep001/animatic/src/build_data.py       # -> src/data.js (không commit)
npm i three@0.186.1                                     # thư mục tạm
export THREE_DIR=<tạm>/node_modules/three/build NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers
cd episodes/ep001/animatic/src && ./render_all.sh [S01 …]   # node render.js S05 --still 3,9 cho ảnh thử
python3 check.py && python3 assemble.py
```
