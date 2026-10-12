# F-14 · Báo cáo — nhịp hình trên Tập 6 dựng lại (11/10/2026)

Phiên nhà máy F-14 (`tongket-t6/F14-brief.md`), nhánh `factory-f14`. Ý đồ + ngưỡng ghi trước: `INTENT.md` (§7 bổ sung trước lần đo đầu).
Bản dựng lại: 1080p, cùng kịch bản / 30 take giọng (0 ký tự EL) / nhạc / claim, 6 đoạn bản F-14 ở `ep006/` chồng lên worktree — `episodes/ep006`
của nhánh không đổi. Master F-14: SHA-256 `3a97e6ed200ffbe1364034c57b74a626b116a1defbffb81f89fdb60dec707904` (không commit, 1,16 GB; dựng lại:
`bash toolkit/factory/f14/rebuild.sh build`). Đối chứng: master bản giao `f96da0ea…5edcaa74` (`sha256sum -c` OK).

## v4 · 12/10/2026 (INTENT §8 ghi trước, chủ dự án duyệt) — **F-14 v4 TRƯỢT** (cổng gốc)

v4 = v3 + ba sửa đã duyệt: B22 (hai dải CPI-W/PCE hiện đủ ở từ khoá, bỏ life `cpiw`/`pce`, thêm đổi trạng thái ở "same"/"often"/"most"),
V11 (tiêu đề thẻ V7 hiện từ "card" + 0,15 s), 9 cue R07 đổi hình bằng VẬT đúng từ (`c2.level` đèn mức sáng lại, `c4.bigger` hai séc chớp,
`d1.climbed` quầng đệm, `f0.most` thùng chớp, `f4.ruths` thanh ≥ mốc chớp, `f7.start` tường mờ + 3 thanh sáng, **không** tên Carl, `g1.forty`/`g2.half`/`g3.carls`);
nhãn neo vào từ MỞ ý; đếm thùng theo bậc, thanh 50/50 bậc+tuyến (freeze). `node --check` mã cảnh trước build. Nhánh rebase lên `origin/main` @ `76ef2b1`, test chạy lại
(`test_factory_f14` 5/5). Master v4 1080p: SHA-256 `800bb58c7b4a25ea9bd7895e6ad42e72ba4bd8968736913e62482faddbd41d3f` (không commit).

| Thước (đích ghi trước) | Đối chứng | v4 | Kết |
|---|---|---|---|
| **Cổng gốc §8 (i)** ≥ 20/23, advice_stated 0 | **19/23** đọc lại cùng phiên (TRƯỢT B01, B10, B13, B30) | **19/23** (TRƯỢT B01, B13, **B14**, B30), advice_stated 0 | **TRƯỢT** |
| **(iii)** nhịp ĐẠT ở đối chứng mà tụt ở v4 → 3 người đọc mới + 2 người chấm | — | B14: ctl 1·1·0,5 ĐẠT / v4 0,5·0,5·1 **vẫn tụt** · B24: ctl 1·1·1 / v4 0,5·1·1 ĐẠT | **TRƯỢT** (B14) |
| **(iv)** B22 ĐẠT | 1·1 | **1·1** | ĐẠT |
| freezedetect ∩ lời < 60 s | 206,01 s | **47,85 s** (16 quãng; v3 44,83) | ĐẠT |
| R07 (1) checks khoá, mọi cue ≥ 90 % | 70,3 % | **94,6 %** (122/129; luật nay THAM KHẢO ≥ 92 % → PASS) | ĐẠT |
| R07 (2) đọc chặt 118 cue bản giao, cùng cách đo ≥ 90 % | 70,3 % | **94,1 %** (111/118; trang checks v4 và nhật ký render cho cùng số) | ĐẠT |
| "3%" ≤ 0,2 s (textTrack checks) | 1,29 s | **0,09 s** (459,70 − 459,61) | ĐẠT |
| CHẶN 0 | 0 | **0** (36/36) | ĐẠT |
| spine quãng tĩnh > 8 s (chỉ báo) | 7 · 4 | **0 · 0** | ĐẠT |
| (báo) CHÍNH | 13/13 | **14/14 — V11 ĐẠT** (0 va chữ) | sửa v3 đã ăn |
| (báo) REG so `run-c5d` | — | **PASS**: 95 luật so được, 0 hồi quy CHẶN | |
| (báo) R08 | FAIL (7) | **PASS (0)** | |

**Kết luận v4: TRƯỢT** — chỉ ở cổng gốc (§8 (i) 19/23 < 20 và (iii) B14 tụt sau 3 người đọc mới). Mọi số chính khác ĐẠT. Theo `episode.md` §9: Tập 8 **không** mở `deep` trên F-14 v4.
Không hạ đích, không merge.

**Cổng gốc v4 chi tiết** (`root_v4.py`; người đọc Sonnet MỚI, rubric mới, gộp thận trọng): gói chung `root-v4/` (92 nhãn, đối chứng + v4 trộn, 2 người chấm) →
ctl 18 + chờ B16 · v4 18 + chờ B14, B24, B30. Đọc lại theo (iii) `root-v4-rr/` (B14, B24, cả hai bản, 3 người đọc mới mỗi bản, 12 nhãn một gói, 2 người chấm).
Người thứ 3 cho nhịp tách đôi (như cũ) `root-v4-p3/` (B16 ctl → ĐẠT, B30 v4 1·0·0 → TRƯỢT; gói riêng chấm lại cả 3 câu trả lời của nhịp đó).
- **B14 (S14, "gần như mọi ô `warn`, cụm `cushion` mỏng ở mép trái"):** dải 6 khung hai bản gần như trùng điểm ảnh (cùng "kept up: 17 of 715", "about 1 in 42");
  khác thấy được: ở khung 2–4 v4 có vệt xanh lam trên cụm thanh đầu (bản giao: xanh `cushion`) — nguồn trong mã v4 chưa truy xong (ứng viên: highlight `hi` của thanh 1949 mới thêm ở `d-s13-s23/scene.js`).
  Người đọc v4 nói "trả cố định mất sức mua" nhưng 2/3 không nói "hầu như không tháng nào theo kịp" → 0,5. Có thể là nhiễu người đọc (ở gói đọc lại, đối chứng cũng có
  một 0,5), nhưng luật ghi trước tính là tụt → TRƯỢT. Nếu muốn v5: tìm và bỏ vệt lam đó trong S14 để S14 trùng bản giao.
- **B30:** TRƯỢT ở cả hai bản (ctl 0,5·0,5; v4 1·0·0) → không tính tụt nhưng kéo (i) xuống 19. **B10:** đối chứng TRƯỢT, v4 ĐẠT. **B01, B13:** TRƯỢT cả hai.
- Đối chứng đọc lại hôm nay 19/23 (bản giao 20/23, lượt v3 19/23) — biên nhiễu ±1–2 nhịp vẫn lớn hơn khoảng cách tới ngưỡng 20.

**Đính chính v3:** R07 §7 đọc chặt của v3 là **91,5 %** (đo đúng bằng `r07_local.py --like`), không phải 86,4 % (86,4 % là ước lượng dùng lại kết quả của bản giao cho 9 cue).
v3 vẫn TRƯỢT vì cổng gốc (B22).

**Môi trường checks v4:** checks LOCK hiện hành `dc4981b3` (main @ `76ef2b1`). `episodes/ep006/contract.json` của **worktree** (không commit) đổi `lock`
`4d688acd` → `dc4981b3` để `checks_split.sh` chạy (lần đầu dừng "contract.json lock ≠ checks/LOCK"); không sửa `checks/`. Bộ lấy mẫu trang bị dừng ở trần 2 h (16/31 cảnh có cache),
chạy tiếp `RESUME=1 KEEP=1` → xong 31/31; tổng ≈ 2 h 48. Luật THAM KHẢO mới của LOCK này có A12 ERROR (TypeError trong `checks/py/r_audio.py`), A13 FAIL (`max |stretch-1|` 165,7 — đơn vị có vẻ sai),
R01 MISSING (`out/tension-map.png`) — không là đích, ghi vào đây để phiên K xem. Báo cáo: `out/checks-v4/report.{json,md}`, `page.json.gz`; số đo `out/v4/`.

**Chi v4 (Console headless, 0 agent con):** cổng gốc gói chung $3,06 · đọc lại 3 người $0,43 · người thứ 3 $0,24 → $3,73; REVIEWER v4 xem dưới. Cả F-14 ≈ $11,1 + REVIEWER v4 (trần cảnh báo $45: dưới trần).
**Giờ máy v4:** checks ≈ 2 h 48 (lấy mẫu trang 2 lần chạy: 2 h dừng ở trần + 48 min; v3 1 h 47 + 25 min).

# v1–v3 (11/10)

## 1. Đích và số thật

| Thước | Đích | Đối chứng (bản giao) | F-14 (dựng lại) | Kết |
|---|---|---|---|---|
| quãng tĩnh có lời > 8 s (spine_pace) | 0 · cả nhãn 0 | 7 · 4 | **0 · 0** | ĐẠT (chỉ báo) |
| ″ chỉ tính cue của bản giao (INTENT §7) | báo | 7 · 4 | 7 · 4 | báo: hết tĩnh là nhờ cue hình MỚI gắn từ (mục 2) |
| freezedetect ∩ lời (số chính) | < 60 s | 206,01 s (51 quãng) | **44,83 s** (15 quãng) | **ĐẠT** |
| R07 ±0,2 s (số chính) — checks khoá | ≥ 90 % cả hai cách (INTENT §7) | 70,3 % (83/118, FAIL) | (1) checks khoá **93,8 %** (121/129, PASS; giọng lệch trung vị 0,00 s) · (2) 118 cue cũ theo luật R07 93,2 % (110/118); **118 cue cũ, giữ cách đo của bản giao cho 9 cue nay có nhãn neo: 86,4 % (102/118)** | (1) ĐẠT · (2) **TRƯỢT** theo §7 đọc chặt (mục 1b) |
| nhãn "3%" | ≤ 0,2 s | 1,29 s (textTrack) · 1,26 s (G2) | **0,09 s** (textTrack checks: 459,70 − 459,61; nhật ký trang 0,15 s) — `out/f14-3pct.json` | **ĐẠT** |
| cổng gốc (khoá nghĩa, số chính) | ≥ 20/23 và mọi nhịp ĐẠT ở bản giao vẫn ĐẠT (tụt → đọc lại 3 người) | 20/23 bản giao · **19/23 đọc lại cùng phiên** | **21/23**, advice_stated 0; **B22 tụt, đọc lại 3 người vẫn tụt** (1 · 0,5 · 0,5) | **TRƯỢT** (luật ghi trước) |
| CHẶN | 0 | 0 (36/36) | **0 (36/36)**; REG: 0 hồi quy CHẶN trên 98 luật so được với `run-c5d` | **ĐẠT** |
| (báo) CHÍNH | — | 13/13 | **12/13: V11 TRƯỢT** — 1 mẫu 0,1 s ở 510,2 s: tiêu đề thẻ V7 "How we know this" hiện khi "dollars paid out: not compared" còn mờ dần (F-14 dời lúc tắt nhãn về đúng "card") → tập "CHỜ GIẢI THÍCH" | do F-14 gây ra; sửa một dòng (mục 5) |
| (báo) R08 / V14 | — | R08 FAIL (7) · V14 FAIL | R08 **PASS (0)** · V14 FAIL như cũ ("first-5 s beats not in the world" 1: quy tắc 7 đã đổi theo F-14 c) | |

**Kết luận: F-14 TRƯỢT** — cổng gốc (B22 tụt sau đọc lại 3 người) và R07 theo INTENT §7 đọc chặt (86,4 % < 90 %). Đạt: freezedetect 206 → **44,8 s**, R07 checks 70,3 → **93,8 %**, "3%" 1,29 → **0,09 s**, CHẶN **0**, spine 7 → **0**. Mới hỏng: V11 (CHÍNH, 1 mẫu). Không hạ đích; không merge — báo số cho phiên điều phối.

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
- Token phiên chính (`episodes/ep006/c5/session_tokens.py`, lúc đóng): 357 lượt, sinh ra 0,30 triệu, đầu vào mới 0,73 triệu → **trần 1,02 triệu**;
  đọc cache 148,5 triệu.
- Môi trường checks: lượt đầu ERROR/MISSING vì thiếu dữ liệu FRED ghim (tải lại `data/fetch.py --verify`: **sha256 khớp bản ghim**), Shorts chưa chép vào `out/shorts`, và PyAV 19 không nhận `metadata_errors` của faster-whisper → ghim `av==13.1.0` (môi trường, không đổi checks/); chạy lại phần Python với trang đã lấy mẫu. Báo cáo: `out/checks/report.{json,md}`, `page.json.gz`.
- Giờ máy: 1080p đầy đủ lần đầu ≈ 1 h 55 (thế giới 67 min, Shorts 12 min); hai lần dựng lại sau cổng gốc ≈ 1 h + 45 min (cache theo cảnh); 7 vòng nháp
  360p ≈ 15 min/vòng; checks khoá: lấy mẫu trang 1 h 47 (4 job) + luật Python ≈ 25 min.

## 5. Đề xuất (không tự áp)
1. Điều phối/chủ dự án quyết với số trên. Ứng viên v4 nếu muốn: (i) B22 — hai dải CPI-W/PCE hiện đủ ở từ khoá (bỏ life `cpiw`/`pce`); (ii) V11 — tiêu đề thẻ V7 hiện từ "card" + 0,15 s; (iii) R07 §7 — không sửa được bằng nhãn (đó chính là điều §7 chặn): cần đổi hình bằng vật ở 9 cue đó. Mỗi vòng ≈ 1,5 h máy + checks ≈ 2 h + cổng gốc ≈ $2; đo lại cả cổng.
2. `checks-appeal.md` (đề xuất cho phiên K): luật "không nhịp nào tụt" của cổng gốc cần biên nhiễu — đối chứng đọc lại cùng phiên "tụt" 4 nhịp không đổi hình;
   đề xuất so với **đối chứng cùng phiên** và cho mỗi nhịp tụt 3 người đọc mới + 2 người chấm, hoặc ngưỡng theo số nhịp.
3. Nhà máy: comment_guard không bắt chú thích cuối dòng chèn giữa dict/khai báo nhiều biến (nuốt mã 3 lần trong phiên) — thêm kiểm `node --check` trên
   bản sao `.mjs` vào bước lint.
