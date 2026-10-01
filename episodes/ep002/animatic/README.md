# Tập 2 · C4 — Animatic toàn tập (S01–S13)

ANIMATIC C4, 01/10/2026, theo `BRIEF.md`. Hệ hình đã ký `design/c3/final/` (D2 + E2), kịch bản v5 `story/script.md`, nhịp `story/beats.md`. Không commit/push.

**Xem:** `out/animatic-720p.mp4` (9:45,6 · 1280×720 · 30 fps · H.264 + lời tạm AAC · 20,2 MB) · `out/silent-720p.mp4` (không tiếng, cho kiểm mù · 10,7 MB) · dải `strips/KEY-n.png` + `KEY-n-masked.png` (7 nhịp) và `strips/Sxx.png` (13 cảnh) · kiểm máy `check-report.json` · kiểm 25% `legibility.md`.

## Cách dựng
- **Không thêm gu.** `src/film.js` nạp nguyên hai engine đã ký (`design/c3/final/src/engine.js` = H2, `src/h3/engine.js` = H3) và nhập **nguyên văn** bảy clip đã ký: K1 r2 (`k1.js`), K2 vòng sửa (`k2.js`), K3/K5/K6 (`h3/scenes.js`), K4 bản hũ (`k4.js`, có sửa kỹ thuật việc 0), K7 r2 (`k7.js`). Mỗi clip chạy qua một **bẻ thời gian** (`warp`): mốc khung của clip được ghim vào neo câu + từ khoá, nên chuyển động đúng như bản ký, chỉ chậm/nhanh/giữ theo lời. Các cảnh không phải KEY dùng lại vật của hệ, mã chép từ mã ký vào `src/lib.js` (thẻ lời mời, người, sườn T-bill, cửa sổ 10 năm, dải 753 ô, vòng, hũ, chồng xu, `jarRun` = `k4.js` có tham số).
- **Định thời (việc 1):** `src/make_timing.py` lấy take `use` trong `review-c2/table-read.json` (không gọi ElevenLabs), faster-whisper `small.en` CPU tạo mốc từng từ, căn (difflib) vào chữ nói của câu `Sxx.n` script v5 → `timing.json`; ghép lời bằng ffmpeg (aresample 44100, mono, apad: 0,8 s sau mỗi cảnh; S11 kéo tới 24 s cho thẻ; S13 đuôi 16 s; chèn 2,0 s nghỉ sau S10.1 — `INSERT` — để mỗi số S10.1 giữ ≥ 3 s, lời không đổi), mỗi cảnh tròn khung. Neo: `src/anchors/Sxx.json` → `src/build_anchors.py` → `anchors.json` (107 neo, 0 từ khoá không thấy). Giọng mới: xoá `work/asr/`, chạy lại `make_timing.py`, `build_anchors.py`, dựng lại.
- **Dải:** 6 khung = tâm của 6 khoảng bằng nhau trong khoảng câu của nhịp (`timing.json`; KEY-7 nối S09.4→S10.3 qua hai cảnh). Bản che dùng cờ dựng của chính hai engine (`FLAGS.mask` / `FLAGS.MASK`): khối `surface #171B22` đúng hộp chữ; huy hiệu: H2 thay cả viên, H3 giữ viên vàng và che chữ (như dải ký K3/K5/K6).
- **Dựng lại:** `python3 src/make_timing.py && python3 src/build_anchors.py && src/render_all.sh && node src/render.js --strips && python3 src/check.py && python3 src/assemble.py` (render cần `NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`; dữ liệu `design/c3/final/work/data.js`, `h3data.js` từ `build_data.py` của C3). `work/` không commit.

## Bảng cảnh
Giây máy: Chromium headless + canvas 2D, CPU 4 lõi, 3 cảnh song song (lần dựng cuối). Tổng ≈ 36 phút máy, ≈ 14 phút tường; ghép 50 s.

| Cảnh | Dài (s) | Nhịp KEY (khoảng câu, giây tuyệt đối) | Giây máy | Khác bản ký / ghi chú |
|---|---|---|---|---|
| S01 | 27,0 | KEY-1 S01.2–S01.3 (9,5–26,1) | 107 | S01.1 chỉ chữ: "July 1, 2026" + "Grad PLUS ends for new graduate students" (hệ không có lịch/biểu mẫu) |
| S02 | 40,3 | — | 152 | chữ chính sách (claim) + khung chi phí viền `ink-muted`, khối liên bang `grid`, phần còn lại viền `ink` "private lender" → cắt sang hình K2 (hai thẻ) |
| S03 | 59,5 | KEY-2 S03.5–S03.8 (98,2–125,5) | 211 | S03.1–2: hình K2 + chữ "$50,000 over 10 years", "$633.38 / $593.51 a month" trên thẻ (thay phong bì); S03.3–4: K1 r2; KEY-2 = K2 nguyên bản, bước "0" neo ở đầu S03.8 (hình đi trước lời) để dải thấy đủ 3 → 1.5 → 0 → đảo |
| S04 | 50,1 (take v5.2) | KEY-5 S04.1–S04.2 (126,8–145,4) | 173 | thêm chữ "US only" (việc 4); S04.3 chồng xu K6 (cao theo `fixed_int`, `worst_diff`, không in số); S04.4 chạy lại K2; S04.5 một thẻ trống; S04.6 sườn tới "today" + "History, not a forecast" |
| S05 | 47,5 | KEY-3 S05.2–S05.4 (178,9–217,6) | 197 | sau "April 1977": vòng quanh ô tệ nhất (không thêm số); S05.5 hình K2 ở 1.5 points |
| S06 | 39,3 | KEY-4 S06.1–S06.5 (222,8–261,1) | 152 | K4 bản sửa C3d + nhãn "not to scale" cạnh khối đỏ (C4 Q3a); S06.5 cùng hình K4 cho lần chạy giảm 8/1981 — **hũ thang riêng** ($15,295 = đầy) |
| S07 | 58,3 | — | 212 | sườn hai nửa, đỉnh "16.3%", hai cửa sổ (4/1976, 11/2000) + hũ (thang $16,000, khối đỏ dưới hũ **cùng thang**), "August 1981", "−$15,295", 753 ô + vòng tệ nhất, "28.4%" (nhắc) |
| S08 | 61,2 (take v5.1 59,95 s + nghỉ 1,25 s: khe quảng cáo 2 ≥ 1,0 s ở ≤ −40 dBFS, đo 1,38 s) | KEY-6 S08.1–S08.7 (320,5–372,1) | 204 | K6 nguyên bản; S08.5 (khoản trả $863.36) chỉ có lời (K6 không có vật khoản trả); S08.8 dựng lại bố cục cuối K6 + đường trần đứt nét hạ dần, khối đỏ co theo `cap15_worst`, `cap12_worst` |
| S09 | 55,4 (take v5.2) | KEY-7 S09.4→S10.3 (396,7–460,4) | 235 | S09.1 hình K2 ở 1.5; KEY-7 = K7 r2 nguyên bản tới "20.4"; từ đó cùng bố cục K7 r2 vẽ bằng `lib.k7At` (mã k7.js, khe cho trực tiếp) để thêm "8.8%" (2 điểm) và "4.5%" (3 điểm) + "of all starts", mỗi lúc một số |
| S10 | 67,3 (take v5.2 + 2,0 s nghỉ sau S10.1) | (tiếp KEY-7 tới S10.3) | 243 | S10.1: núm NHẢY (lật kiểu K2) 1 → 0 → −1 điểm (−1: thanh thả nổi trên thanh cố định, khe `warn`), cột đỏ nhảy lên; mỗi bậc **một số**: tỉ lệ chung "31.3% / 57.9% / 72.9% of all starts" (`spread1_share`, `spread0_share`, `spreadm1_share`), giữ đủ 3,17 / 3,23 / 3,13 s, hai cột "before 1981" / "from 1981" luôn trên hình (chủ dự án C4 Q3a; số từng nửa + tệ nhất chuyển vào mô tả). S10.2: nhảy VỀ 3 điểm, vòng + "April 1977" (`gap_worst_start_all`); S10.3: lớp đỏ trái nhấp nháy nhẹ + "10.5%" (`min_gap_early`). Khung 6 dải KEY-7 ở 3 điểm. S10.5 K7 cuối (nhấp nháy); S10.6 K7 2 → 3; S10.7 sườn |
| S11 | 24,0 | — | 98 | thẻ phương pháp (việc 3) |
| S12 | 39,6 | — | 138 | K7 ở 1.5 (đỏ nhấp nháy nhẹ); thẻ trống + 5 nhãn điều bị bỏ ngoài; K7 cuối; "History, not a forecast" |
| S13 | 16,0 | — | 61 | sườn mờ + ô trống cho phần tử end screen, không chữ |
| **Tổng** | **585,6** | | **2 182** | |

Ghi rõ: **khối đỏ K4 không cùng thang với hũ** (trên hình có nhãn "not to scale", `ink-muted` 48 px) ($7,577 ↔ 150 px so với $1,046 ↔ 380 px), như bản ký; hũ S06.5 cũng thang riêng. Riêng S07 hũ và khối đỏ cùng một thang.

## Kiểm máy (`check-report.json`, `src/check.py`)
0 số ngoài claim (13/13 cảnh; claim ID từng cảnh ở `claimsUsed`) · 0 chuỗi ngoài vùng an toàn (x 96, trên 64, dưới 40 @1080) · chữ nhỏ nhất 48 px @1080 · tương phản nhỏ nhất 7,50:1 · chữ→nét nhỏ nhất 7,4 px @720 (S10) · huy hiệu ILLUSTRATIVE có ở mọi khung kiểm có số chỉ thuộc claim minh hoạ (0 thiếu) · neo khai báo = neo dùng (0 thừa) · 0 từ khoá không thấy. Tự kiểm chạy trên mỗi khung thứ 6 + mọi khung dải. "History, not a forecast" (S04.6, S12.5, thẻ S11) và "US only" (S04.2, thẻ S11) có cả lời lẫn chữ.

## Cần chủ dự án xem
1. **Vật ngoài hệ thay bằng ký hiệu gần nhất:** lịch/biểu mẫu S01.1 và S02 → chữ + khung chi phí trơn (`ink-muted`/`grid`/`ink`); phong bì S03.2/S08.5 → số trên thẻ (S03) hoặc chỉ lời (S08); đường trần S08.8 → vạch đứt `ink-muted` kiểu ray + nhãn "rate cap"; năm vật S12.3 (chỉ số, trần, đồng hồ cát, hoá đơn, ví) → 5 nhãn chữ quanh thẻ trống; khe end screen S13 → khung `grid`.
2. **KEY-7 (sửa theo luật chủ dự án: dải không kết ở chiều "đỏ tăng"):** S10.1 nhảy rời 1 → 0 → −1 (không quét mượt), rồi S10.2 nhảy về 3 và giữ tới hết nhịp; khung 6 ở 3 điểm. Các bậc −1/0/1 và 8.8%/4.5% vẽ bằng bản chép mã k7.js (`lib.k7At`), không phải clip 10 s. Khe đảo (−1) vẽ `warn` trên thanh cố định — hình mới trong bố cục K7 (luật hệ: khởi đầu đảo = warn). Mỗi bậc S10.1 chỉ một số (tỉ lệ chung), giữ ≥ 3 s nhờ 2,0 s nghỉ chèn sau S10.1. Vòng "April 1977" là khung `ink` trên lớp đỏ trái. S10.6 không in "+$6,033" (đang hiện 10.5%).
3. KEY-2: bước "0" và "đảo" neo vào đầu S03.8 ("Real offers differ… bigger") chứ không đúng chữ "zero"/"negative" (cuối câu), để 6 khung dải thấy đủ bốn trạng thái.
4. Hai thang hũ khác nhau (K4/S06.1–4 vs S06.5 vs S07), xem trên.
5. Tiêu đề thẻ phương pháp viết "Treasury bill rate" (không ghi "3-month": số 3 không có claim riêng).

## Giới hạn
- Lời tạm = take C2 (`review-c2/takes`), không nhạc/hiệu ứng; mốc câu từ ASR (lệch ±0,1–0,3 s; số đọc khác chữ được rải đều).
- Chuyển cảnh là nhúng nền 0,44 s. Các đoạn giữ lâu ở bố cục K7 (S10.2–3, S10.5, S12.1, S12.4) có nhịp nhấp nháy nhẹ trên lớp đỏ.
- Chưa kiểm mù (P chạy theo `gates/C4-intent.md` trên `strips/KEY-*-masked.png`).

## Nhãn nghĩa C4c (a) — chỉ thêm chữ, không thêm vật/gu
Màu `ink` (nhãn cột giữ `ink-muted`); không số; không câu khuyên/dự báo. Giây hiện = lúc hiện đủ (không tính mờ vào/ra), theo `timing.json` hiện hành; không cảnh nào đổi độ dài. Tự kiểm: chữ→nét ≥ 10 px @720, tương phản ≥ 7,5:1.

| Nhịp | Nhãn | Cỡ @1080 | Từ | Cần (s) | Hiện (s) | Chỗ |
|---|---|---|---|---|---|---|
| KEY-2 (S03.5–S03.8) | "Different offers" | 64 (caption) | 2 | 0,7 | 7,5 | dòng trên các thẻ, từ đầu KEY-2 tới S03.6 |
| KEY-2 | "Head start = fixed − variable" | 64 | 5 | 1,7 | 20,0 | cùng chỗ, từ S03.6 tới hết cảnh (lúc điểm bắt đầu nhảy 1.5 → 0 → đảo) |
| KEY-5 (S04.1–S04.2) | "Leah's loan, replayed from every start month" | 64 | 7 | 2,3 | 18,4 | dòng dưới, suốt K5 (S04.1–S04.2) |
| KEY-6 (S08) | "Worst replay: variable vs fixed interest" | 64 | 6 | 2,0 | 60,3 | dòng dưới, cả S08 (giữ "Starting April 1977", "43% more") |
| KEY-7 (S09.2–S10.3, S10.5–6, S12.1, S12.4) | "Share of starts that cost more" | 48 (note) | 6 | 2,0 | 47,9 (S09) + 25,5 + 28,4 (S10) + 13,2 + 8,2 (S12) | tiêu đề trên hai cột |
| KEY-7 | "Bigger head start →" | 54 (label) | 3 | 1,0 | như trên | trái hai cột, mũi tên chỉ vào cột |
| KEY-7 | nhãn nửa: "1954–1980" / "1981 on" (CL `period_early_label` / `period_late`) | 54, `ink-muted` | 1 / 2 | 0,7 | như trên | dưới từng cột (trước là "before 1981" / "from 1981") |

Ghi chú: (1) "1954–1980" qua claim phụ `period_early_label` (cha `n_early`), "1981 on" qua `period_late`. (2) Để nhãn có mặt suốt KEY-7, toàn bộ hình K7 nay vẽ bằng `lib.k7Clip`/`k7At`: chép mã `k7.js`, cùng lịch khe và độ mờ nhãn, cộng thêm các nhãn mới. Clip `k7.js` đã ký không đổi. (3) Lời nhắc KEY-5 ở S11 không có hình K5, nên không gắn nhãn ở đó.

## C5 · luồng P — trang dựng, render 1080p30, checks (01/10/2026)
**Trang dựng** `film.html` + `build/film.js` (esbuild, `src/build_page.mjs`; `npm ci`), dữ liệu `work/c5/data-h2.js`, `data-h3.js` (`src/build_c5_data.py` từ dữ liệu C3; FRED, không commit). Cùng mã cảnh C4 (sNN.js, film.js, lib.js, hai engine và các clip đã ký), vẽ ở tỉ lệ 1 trên canvas 1920×1080. Lúc build chỉ thay hai dòng của mỗi engine đã ký (TOK qua `fetch` → `window.TOK_E`; `window.DATA` → `DATA_H2`/`DATA_H3`) và dòng `fetch` thẻ phương pháp ở s11.js, để một trang chứa được cả hai engine; không đổi gì khác.
`window.CHECKS` (checks/CONTRACT.md §Page): `seek(t)` dựng khung t; `objects()` = đối tượng màn hình theo thứ tự vẽ, lấy từ proxy ghi lệnh vẽ `src/rec.js` (mỗi lệnh fill/stroke/fillRect/strokeRect/fillText có số thứ tự, hộp, màu, độ mờ; chữ có `claims` = vùng hiện display của claim hoặc số lấy từ display; huy hiệu ILLUSTRATIVE `role:"badge"` kèm viên nền; tô màu nền = `card`; nhúng nền giữa hai cảnh nhân độ mờ của mọi thứ vẽ trước); `layer(name, ids)` vẽ lại đúng khung đó chỉ giữ một số lệnh; `freeze` không làm gì (phim không có máy quay: `out/camera.json` đứng yên, zoom 1). Trường hợp S06: hai cột KEY-7 mang `case` `period-1954-1980` / `period-1981-on`, vòng + "April 1977" ở S10.2 mang `worst-1977-04`.
**Render:** `src/render_c5.sh` (3 hàng song song, `src/render_c5.js`: RGBA → ffmpeg CRF 8 trung gian, BT.709 limited) → `src/assemble_c5.py` (mã Tập 1: libx264 High, CBR 24 Mb/s, dither luma nhẹ chống banding, GOP 2 s; mux `out/audio/master.wav` mặc định → AAC-LC 48 kHz stereo 320k). `out/video.mp4` 17 568 khung = 585,6 s, SHA-256 `f8c2f3f4f2916c6aa919c71ed3ddbfb5df2c6ab3d1161b67b9eff7b8de4fe5c2` (không commit; lần 1 `cb2dd0ef…`). Hình trung gian `work/c5/picture-1080.mp4` `2a4370a1…`; master `0266dc8c…` (= `out/audio/manifest.json`). Giây máy: cảnh 206–590 s mỗi cảnh (≈ 0,3 s/khung, 3 hàng ≈ 25 phút tường); mã hoá giao 38 phút; mux 51 s.
**Tệp P khác:** `out/page.json` (url `animatic/film.html`, `ready` chờ `window.CHECKS`), `out/camera.json` (một mục mỗi khung), `design/tokens.json` (mọi màu trang vẽ, xuất từ token đã ký; không bảng màu chuỗi).

### Chữ mới người xem thấy ở C5 (báo chủ dự án)
- **S09 (CHẶN) gốc tiền:** nhãn khung "dollars of the day" (`ink-muted`, 48 px @1080) mọi lúc có số $ trên hình: S02 (dưới "$20,500 a year" / "$100,000 total"), S03 (trên thẻ cố định, dưới "$633.38 a month"; cùng lúc "$50,000 over 10 years"), S07 (dưới "−$15,295"), S08 (cạnh "$26,005", cùng nhịp nhãn K6). S10 không còn số $ trên hình.
- **S02 (CHẶN) giả định trên màn hình, trong và ngoài thẻ phương pháp:** dòng thẻ "No grace period · no fees · no rate cap" → "Repayment starts at once · no fees · no rate cap" (61 từ, cần 20,3 s, thẻ hiện đủ 21,0 s; độ dài không đổi); S07 nhãn sườn "Treasury bill rate" (`ink-muted` 48 px); S12.3 nhãn đổi: "a rate cap" → "no rate cap"; "a grace period" → "repayment starts at once" (một dòng dưới thẻ trống; "your own budget" sang trái thẻ).
- **S11 (tham khảo):** không thêm. `worst_diff` ($11,219) và `share_late` (3.5%) chỉ được nói ở S05, nên không có cảnh nào khác được gắn số qua CL() mà vẫn đúng luật "chỉ nơi lời đã nói".

### Checks (bản sao `origin/main` checks, LOCK K3.6 `2fcc9fcc…` khớp; `run.sh … --first`; báo cáo `out/checks/report.json`)
Lần 1: TRƯỢT — CHẶN F11, S02; CHÍNH V03, V08, V09, C14. Sửa trong mã hình: S02 (nhãn "repayment starts at once" thành một dòng, S12), V08/C14 (khung đỉnh của cú nhúng nền: độ mờ đối tượng = 0), V09 (hình thoi của Leah mang `char: leah`, `shape: diamond`). Dựng lại S12, ghép lại, chạy lại.
**Lần 2: 58 PASS · 23 FAIL · 1 MISSING — TRƯỢT chỉ vì F11 (CHẶN):** 6 thumbnail C6 (`out/package/thumb-{1,2,3}.png/.json`) chưa giao. Mọi CHẶN khác đạt (F01–F06, F08–F10, F12, A01, A02, A04–A06, A14, S01–S10, C07, REG).
**CHÍNH còn trượt: V03** — 2 394 mẫu, tất cả là viên nền huy hiệu ILLUSTRATIVE: viên của hệ đã ký kéo tới x 1840–1842 (vùng an toàn 96–1824); chữ của huy hiệu nằm trong. Sửa được bằng cách dời huy hiệu sang trái 18 px (đổi vị trí đã ký; cần chủ dự án), hoặc giải thích trong `out/explanations.json`.
THAM KHẢO trượt: A03 A10 A11 A15 A16 A17 S11 S12 S15 R02 R03 R05 R06 V02 V05 V10 C10 C12 C13 T2 T3; P01 MISSING (thumbnail C6).
