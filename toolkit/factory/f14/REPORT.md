# F-14 · Báo cáo — nhịp hình trên Tập 6 dựng lại (11/10/2026)

Phiên nhà máy F-14 (`tongket-t6/F14-brief.md`), nhánh `factory-f14`. Ý đồ + ngưỡng ghi trước: `INTENT.md` (§7 bổ sung trước lần đo đầu).
Bản dựng lại: 1080p, cùng kịch bản / 30 take giọng (0 ký tự EL) / nhạc / claim, 6 đoạn bản F-14 ở `ep006/` chồng lên worktree — `episodes/ep006`
của nhánh không đổi. Master F-14: SHA-256 `3a97e6ed200ffbe1364034c57b74a626b116a1defbffb81f89fdb60dec707904` (không commit, 1,16 GB; dựng lại:
`bash toolkit/factory/f14/rebuild.sh build`). Đối chứng: master bản giao `f96da0ea…5edcaa74` (`sha256sum -c` OK).

## 1. Đích và số thật

| Thước | Đích | Đối chứng (bản giao) | F-14 (dựng lại) | Kết |
|---|---|---|---|---|
| quãng tĩnh có lời > 8 s (spine_pace) | 0 · cả nhãn 0 | 7 · 4 | **0 · 0** | ĐẠT (chỉ báo) |
| ″ chỉ tính cue của bản giao (INTENT §7) | báo | 7 · 4 | 7 · 4 | báo: hết tĩnh là nhờ cue hình MỚI gắn từ (mục 2) |
| freezedetect ∩ lời (số chính) | < 60 s | 206,01 s (51 quãng) | **44,83 s** (15 quãng) | **ĐẠT** |
| R07 ±0,2 s (số chính) — checks khoá | ≥ 90 % cả hai cách (INTENT §7) | 70,3 % (83/118) | ⏳ checks khoá đang chạy — bản sao cách đo: (1) **93,8 %** (121/129) · (2) 118 cue cũ theo luật R07 93,2 % (110/118); **118 cue cũ, giữ cách đo của bản giao cho 9 cue nay có nhãn neo: 86,4 % (102/118)** | **TRƯỢT** theo §7 đọc chặt (mục 1b) |
| nhãn "3%" | ≤ 0,2 s | 1,29 s (textTrack) · 1,26 s (G2) | ⏳ textTrack (cách ghi trước) · tham khảo nhật ký trang 1080p 0,15 s (`out/f14-3pct.json`) | chờ |
| cổng gốc (khoá nghĩa, số chính) | ≥ 20/23 và mọi nhịp ĐẠT ở bản giao vẫn ĐẠT (tụt → đọc lại 3 người) | 20/23 bản giao · **19/23 đọc lại cùng phiên** | **21/23**, advice_stated 0; **B22 tụt, đọc lại 3 người vẫn tụt** (1 · 0,5 · 0,5) | **TRƯỢT** (luật ghi trước) |
| CHẶN | 0 | 0 (36/36) | ⏳ checks đang chạy | chờ |

**Kết luận tạm (trước checks khoá): F-14 TRƯỢT** — cổng gốc (B22) và R07 theo INTENT §7 đọc chặt (86,4 % < 90 %). Freezedetect (44,8 s) và spine (0 · 0) đạt; "3%", R07 chính thức và CHẶN chờ checks khoá. Không hạ đích.

**1b. R07 — vì sao đọc chặt.** 9 cue cũ (`c2.level`, `c4.bigger`, `d1.climbed`, `f0.most`, `f4.ruths`, `f7.start`, `g1.forty`, `g2.half`, `g3.carls`) nay có nhãn neo vào từ, nên luật R07 đo chúng bằng `textTrack` (nhãn) thay cho chênh khung; cả 9 vào ±0,2 s (ở bản giao chỉ 1). Các nhãn là thật và đúng lời, trừ `f7.start` = "Carl" (tên hiện ở "start", câu S23.1 không nói "Carl"). INTENT §7 ghi "cùng tên cue, cùng cách đo" → giữ cách đo cũ cho 9 cue đó: 102/118 = **86,4 %** → TRƯỢT. Cue đo bằng chênh khung ở cả hai bản: 26/46 → **39/46** (cải thiện thật, không nhờ nhãn).

**1c. Cổng gốc là phép đo dùng để sửa:** v1 → v3 đã sửa theo kết quả cổng (B08, B16) nên v3 không còn là phép đo giữ riêng hoàn toàn; số v3 là lượt đọc MỚI (người đọc mới) trên video mới.

### Cổng gốc chi tiết (rubric MỚI `gates/C4-answer.md`, 2 người đọc Sonnet + 2 người chấm, gộp thận trọng; `root_new.py`)
| | Bản giao (P3c) | Đối chứng đọc lại cùng phiên (`root-ctl`) | F-14 v3 (`root-f14v3`, + `root-f14v3-rr`) |
|---|---|---|---|
| TRƯỢT | B01, B15, B04 (0,5) | B09, B10, B12, B13 (0,5 · 0,5 …) | B01 (0,5 · 0,5) · B22 (đọc lại 3 người 1 · 0,5 · 0,5) |
| ĐẠT | 20/23 | 19/23 | **21/23** (B09, B12 qua người đọc thứ 3; B14 tụt ở lần chấm lại rồi ĐẠT khi đọc lại 3 người) |
| advice_stated | 0 | 0 | 0 |
- **Nhiễu đo lớn hơn độ phân giải của luật "không nhịp nào tụt":** cùng master bản giao, đọc lại hôm nay "tụt" B09, B10, B12, B13 (hình không đổi một điểm ảnh); chấm lại CÙNG câu trả lời của F-14 làm B14 đi 1 · 1 → 0,5 · 0,5 và B22 1 · 1 → 1 · 0,5. Vẫn áp đúng luật ghi trước → TRƯỢT; đề nghị phiên K/điều phối xem lại luật (mục 5).
- **B22 (S22, ba dải CPI-U / CPI-W / PCE):** F-14 cho hai dải CPI-W và PCE "chạy theo tháng bắt đầu" suốt câu (life `cpiw`, `pce`). Người chấm: "PCE contrast muddled", "teal placement confused" — dải vẽ dần làm khung lấy mẫu sớm thấy dải chưa đủ. Nguyên nhân hợp lý → sửa một dòng (dải hiện đủ ở từ khoá, không chạy) — **chưa làm** (luật: một lượt đọc lại; sửa thêm = ứng viên mới, phải đo lại cả cổng).
- **B01:** TRƯỢT ở F-14 (0,5 · 0,5, "không nói còn 9 thùng sáng" — như bản giao) nhưng ĐẠT ở đối chứng cùng phiên (1 · 1). Theo luật ghi trước (so với bản giao, nơi B01 cũng TRƯỢT) không tính là tụt; so với đối chứng cùng phiên (đề xuất §5.2) thì là nhịp tụt thứ hai. Không đọc lại 3 người.
- **Nguồn gốc các lượt chấm (REVIEWER #6):** đối chứng `root-ctl`: lượt chấm đầu (2 người chấm) bị ghi đè khi thêm người đọc thứ 3 cho B13/B16 (lỗi thao tác: đóng gói lại chỉ gồm câu trả lời mới) → đóng gói lại ĐỦ 48 câu và chấm lại một lượt; số 19/23 là lượt chấm này (lượt đầu, theo bản in còn lại trong nhật ký phiên: 18 ĐẠT + 2 chờ, B09/B10 TRƯỢT, B01 0,5·0,5). F-14 v3: lượt chấm đầu (`root-f14v3/first-grading/`: 20 ĐẠT, B01 TRƯỢT, B09/B12 chờ) → thêm người đọc thứ 3 cho B09/B12 → đóng gói đủ 48 và chấm lại (lượt dùng trong bảng, `tally-new.json`); B14/B22 lệch giữa hai lượt chấm → đọc lại 3 người mới (`root-f14v3-rr`).
- **Đã bắt và sửa trong phiên (vòng v1 → v3):** B08 tụt 0,5 · 0,5 ở v1 vì nhãn "starting sizes: not modeled" bị neo vào từ CUỐI ("model", 1,6 s trước hết đoạn) → ra khỏi dải nhịp; neo vào "bigger" (đầu ý) → 1 · 1. B16 đọc "80.7% above" khi có dải "phần mất" trên vạch trung vị → bỏ dải. Bài học cho (c): **neo nhãn vào từ MỞ ý, không vào từ cuối**.

## 2. Đã làm gì
**Nhà máy (opt-in, không khai `f14` = cũ):** `world/spine.py` — `check_rules(..., episode_t0)` quy tắc 7 chỉ 5 s đầu tập; `major_changes`/`still_major`/`check_f14`
(cờ `changes` major|minor, `label_at` ±0,2 s, `life` phải có `what`); `build_seg.py` in CẢNH BÁO quãng > 8 s không major; `verify_seg.py` đo lệch nhãn
trên nhật ký trang. 6 spine.json Tập 6 sinh lại **trùng byte** khi không khai; `test_factory_f14.py` 5/5, `test_world*` 48 OK.
**Bản F-14 của Tập 6 (`ep006/world/`):** mỗi đoạn khai `changes`, `label_at`, `life` (45 track, mỗi track một dòng `what`). Loại thay đổi:
- (a) vật dữ liệu sống theo câu, đổi hình **tích luỹ** (đếm thùng còn sáng có dải phủ, hai hàng mọc lần lượt "each … its own first check", 20 lần tăng
  xếp chồng, vùng "at least" tô dần, quét theo tháng bắt đầu "the most recent"/"closest to Ruth's own"/"not one", lịch 20 năm "history, not a forecast",
  hai thùng đổi cỡ "health care and housing can weigh differently", 20 vạch năm trả tiền "over a lifetime", dòng thẻ V7 theo thứ tự đọc…);
  một cú lùi chậm có lý do + âm (S12.4 "unusual, or what a raise usually did?").
- (b) cue hình mới gắn từ được nói (vd "rent / medical care / gasoline", "back above each time", "still above its first check", tên Edna/Carl ở S23).
- (c) quy tắc 7 chỉ đầu tập → S30 vào đồ thị trước "three"; nhãn giá trị neo vào từ; sửa các đổi hình bắt đầu sớm/trễ (mờ 0,3–0,8 s trước từ, cú máy
  sát từ khoá làm nền đo R07 lẫn chuyển động).
Ảnh trước/sau 3 quãng tĩnh dài nhất của bản giao (hàng trên bản giao, dưới F-14, 4 khung đều): `img/before-after-S13.3.jpg` (3:41–3:53),
`img/before-after-S03.jpg` (0:29–0:40), `img/before-after-S17.jpg` (4:40–4:50).

## 3. Báo thêm
- qc nhà máy: cùng 6 mục TRƯỢT loại cũ như bản giao (đối trọng đọc ở đoạn thế giới ×4, freezedetect 44,83 s, true peak −1,9 dBTP; bản giao −1,8);
  mới: SH1 F-2 CẢNH BÁO 19 mẫu nhãn giao nhau (Short dọc). Build: quy tắc 1/2/3 = 0, cắt cứng 0, C14 0 vi phạm, F-2 0 BLOCK ở cả 6 đoạn.
- Cảnh báo F-14 (b) còn lại (chỉ báo): **10** quãng có lời > 8 s không có thay đổi `major` theo cờ (dài nhất 16,7 s ở S05.1–S06.1: cú lia sang hai thanh mặc định `minor`; còn lại 8,0–10,8 s) — cờ major khai thận trọng, chưa hiệu chuẩn; nhãn lệch > 0,2 s:
  `b0.never` +5,9 s (tên "level check" ở thế giới hiện từ "never", nhãn có chữ ở đồ thị như cũ), `b1.january` 2,4 s, `d4.lit` −0,9 s, `f0.ten` −0,7 s (dời về "most"), `c3.forty` (chữ chia hai mảnh) — không phải cue R07.
- R07 bản sao, 8 cue còn ngoài ±0,2 s: hai cue ở 0,3 s đầu đoạn (lớp mờ nối đoạn: `e0.every`, `g0.raise`), `a3.every` +0,28, `a5.short` +0,32,
  `f5.twenty` −0,25 (cú lùi kề từ), `b4.took`, `e2.least`, `c4.model` không đo được (đổi hình nhỏ).
- Thước nháp 360p (`loop.sh`) khớp 1080p đủ để lặp: nháp cuối 41,2 s / 1080p 44,8 s freezedetect; R07 95,3 / 93,8 %.

- **Không bỏ số khỏi hình (REVIEWER #4):** nhãn "rising check: +2% a year" vẫn hiện ở đồ thị như bản giao (`b-s04-s08/scene.js`); F-14 chỉ THÊM tên "rising check" (không số) ở thế giới đúng chữ "rises" và đổi chữ của khoá `label_cues['b0.rises']` theo nhãn mới.
- Opt-in (REVIEWER #10): 6 spine.json Tập 6 sinh lại bằng spine.py mới → `git status` không đổi (trùng byte với bản commit); chưa lưu sha riêng.

## 4. Chi phí, token, giờ máy
- Console (headless, 0 agent con): cổng gốc đối chứng $1,58 · F-14 v1 $1,57 · F-14 v3 $2,12 · đọc lại 3 người $0,23 · REVIEWER headless $1,47 → **≈ $7,0** (+ một lượt chấm
  đối chứng bị ghi đè, chưa đếm, ≈ $0,4). REVIEWER: ĐẠT, 0 CHẶN, 6 CHÍNH, 5 GỢI Ý — đã sửa REPORT theo 6 CHÍNH + #7, #9). Trần cảnh báo $45: dưới trần.
- Token phiên chính (`episodes/ep006/c5/session_tokens.py`, tới lúc viết): 289 lượt, sinh ra 0,25 triệu, đầu vào mới 0,60 triệu → **trần 0,84 triệu**;
  đọc cache 120,5 triệu.
- Giờ máy: 1080p đầy đủ lần đầu ≈ 1 h 55 (thế giới 67 min, Shorts 12 min); hai lần dựng lại sau cổng gốc ≈ 1 h + 45 min (cache theo cảnh); 7 vòng nháp
  360p ≈ 15 min/vòng; checks khoá ⏳.

## 5. Đề xuất (không tự áp)
1. Điều phối/chủ dự án quyết với số trên: F-14 TRƯỢT cổng gốc ở đúng một nhịp (B22) theo luật ghi trước. Nếu muốn một ứng viên v4 (B22 hiện dải đủ ở từ),
   phải đo lại cả cổng — khoảng 1 h máy + $2.
2. `checks-appeal.md` (đề xuất cho phiên K): luật "không nhịp nào tụt" của cổng gốc cần biên nhiễu — đối chứng đọc lại cùng phiên "tụt" 4 nhịp không đổi hình;
   đề xuất so với **đối chứng cùng phiên** và cho mỗi nhịp tụt 3 người đọc mới + 2 người chấm, hoặc ngưỡng theo số nhịp.
3. Nhà máy: comment_guard không bắt chú thích cuối dòng chèn giữa dict/khai báo nhiều biến (nuốt mã 3 lần trong phiên) — thêm kiểm `node --check` trên
   bản sao `.mjs` vào bước lint.
