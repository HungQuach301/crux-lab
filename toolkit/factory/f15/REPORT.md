# F-15 · Báo cáo (13–14/10/2026) — vòng dựng ngắn + footage ngoài

**Chủ dự án 14/10: MERGE** dù thử TRƯỢT — ghi rõ: **T3 = 0,419 > 0,40 TRƯỢT** và **T7 TRƯỢT** (thước cổng gốc nhiễu — A32, nay ở main là "chẩn đoán");
**không hạ đích**. Trước merge: mạng mở → chạy lại T11 (FRED tải thật) và T13 (ảnh LoC thật) — §1b; rebase lên `origin/main` @ `7f8a0da` (LOCK
`b4551642`), chạy lại toàn bộ test + T1/T14, REVIEWER một lượt (§5c).

Ý đồ + ngưỡng ghi trước: `INTENT.md` (commit `989fc39`, trước mọi lần đo). Nhánh làm việc `factory-f15` (từ `origin/main` @ `c7358285`), đẩy lên
`claude/clever-hopper-qkzobc`. Không chạm `episodes/ep007`, `ep008`, `checks/` (đo Tập 7 trên bản sao `git worktree` của nhánh `ep007`
ở `/var/tmp/f15/ep007wt` + toolkit F-15 chép đè).

## 1. Kết quả theo đích (INTENT §3)
| # | Thước | Đích | Đo | Kết quả |
|---|---|---|---|---|
| T1 | 7 spine + timeline + captions, 1080p không cờ, container mới | trùng byte | **9/9 trùng** (`out/T1-bytes.json`). Ngoài phạm vi T1 (chỉ báo): `git status` của bản sao sau `build_inputs.py --out` — `out/*` hợp đồng không đổi trừ `out/voice/takes.json` (giờ chạy); `out/factory/splice.json` khác 3 SHA hình (`out/T2-segments-vs-delivered.json`) | **ĐẠT** |
| T2 | SSIM 1080p mới (thu 720p) vs `review-g2/full-720p.mp4` | ≥ 0,97 | **0,9843** (18.202 khung); cảnh kém nhất S23 0,9813; khung thấp nhất 0,9748 (`out/T2-ssim.json`) | **ĐẠT** |
| T3 | giờ máy nháp 540p / 1080p, cache trống | ≤ 0,40 | nháp **6.220 s (1,73 h)** / 1080p **14.855 s (4,13 h)** = **0,419** (`out/T3-*`) | **TRƯỢT** |
| T4 | checks đủ bộ chạy hết trên nháp | thoát 0, 0 ERROR mới | bộ lấy mẫu trang + 100 luật, thoát 0; ERROR duy nhất A12 có ở cả hai bản | **ĐẠT** |
| T5 | CHẶN/CHÍNH FAIL ở 1080p cũng FAIL ở nháp, ngoài R_pix | 0 bỏ sót | **0 bỏ sót** (cả trong R_pix) | **ĐẠT** |
| T6 | đồng phán quyết nháp ↔ 1080p | ≥ 90 % (chỉ báo) | lượt 1: 95 %; sau sửa đường nháp (§3): **98 %** | **ĐẠT** |
| T7 | cổng gốc nháp ↔ 1080p | \|Δ\| ≤ 2 và ≥ 80 % cùng phán quyết | lượt đầu: nháp **17/21** · 1080p **9/21**; cùng phán quyết 10/21 | **TRƯỢT** (xem §4: thước nhiễu hơn đích) |
| T8 | dải kiểm mù trên nháp | đủ dải | 22 dải + 4 tấm (`blind_c4.py strips` → `toolkit/blind/strips.py`) | **ĐẠT** |
| T9 | resume theo khung, ngắt bằng PID | trùng byte | Tập 7 đoạn a cảnh s1 (540p): dừng ở khung 63/142 (`bg.sh stop`), chạy lại giữ 62, dựng 80 → mp4 + nhật ký **trùng byte**; test tổng hợp 9/18 → trùng byte (`out/T9-T14.md`) | **ĐẠT** (chỉ scene thuần, §5.2) |
| T10 | build nguyên tử, lượt trượt | bản cũ trùng byte | lượt 1080p thứ hai trên bản 1080p đã dựng, dừng theo PID giữa build (thư mục tạm đã có timeline): **25/25 tệp** (video, master, stem, Short, phần, báo cáo, artefact) trùng SHA trước/sau (`out/T10-*.sha`); lượt nháp đầu trượt ở `qc` (§5.1) không thay gì (thư mục chưa có bản cũ — chỉ chứng minh không promote); test promote | **ĐẠT** |
| T11 | `verify.sh --install` container mới (13/10; 14/10 → §1b ĐẠT) | dựng được không bước tay; ASR thử đúng | 98 s (`out/T11-verify-install.txt`): `npm ci` three 0.186.1, ASR thử (PyAV 19 hỏng → tự ghim 14.2.0 → 100 % từ), `bed.wav` SHA `57c57cae…` = đường `build_inputs`; rồi 1080p **một lượt, 0 trượt môi trường**. Dữ liệu FRED: `fetch.py --verify` ĐẠT chỉ vì tệp có sẵn trong nhánh `ep007`; tải thật bị mạng chặn | **ĐẠT một phần** (FRED chờ mạng, §6) |
| T12 | `api.sh` chặn agent con + trần chi | Task/Agent từ chối; trần hiệu lực | lượt thử agent con 13/10 chạy TRƯỚC khi cấm `Workflow` (init còn `Workflow` — REVIEWER lượt 2) → **chạy lại 14/10 với `api.sh` hiện tại**: init không có Task/Agent/Workflow; model gọi `ToolSearch select:Task,Agent` → không có, trả "NO SUBAGENT TOOL" (`out/T12-api-rerun.json`); trần $0,005 → `error_max_budget_usd` sau 1 lượt ($0,0065) (`out/T12-api.json`, cap2) | **ĐẠT** (trần kiểm giữa lượt: vượt ≤ 1 lượt) |
| T13 | clip footage 540p 8 s: 1 ảnh LoC + 1 bản đồ (13/10; 14/10 → §1b ĐẠT) | 0 chữ đè chủ thể; 2 dòng RIGHTS | bản đồ South Atlantic (Census qua us-atlas + Natural Earth) + plate **ảnh THAY THẾ** (khung tự dựng) vì `www.loc.gov`/`tile.loc.gov` bị chặn (403); 0/41 khung chữ đè chủ thể; nhãn trễ mốc từ 0–0,08 s; 2 dòng RIGHTS tự ghi (M-USATLAS, M-NE-ADM1) | **ĐẠT một phần** — phần LoC chờ mạng |
| T14 | không bật plate: khung trùng mã cũ | trùng MD5 | Tập 7 đoạn a cảnh s0, s1 (540p) dựng bằng `main` cũ và F-15: mp4 + nhật ký **trùng byte** (`out/T9-T14.md`) | **ĐẠT** |

**Kết luận: TRƯỢT** (T3 0,419 > 0,40; T7 trượt — thước cổng gốc nhiễu hơn đích; T11, T13 một phần — mạng chặn FRED, LoC). Không hạ đích. Điều phối/chủ dự án quyết.

## 1b. Chạy lại sau khi mở mạng (14/10)
| # | Đo | Kết quả |
|---|---|---|
| T11 | `verify.sh factory-f15 --install episodes/ep007` trên checkout chính (không có `data/raw`): `fetch.py --verify` **tải thật** 4 chuỗi FRED + bản ghim hồ sơ, SHA khớp; ASR thử 100 %; `bed.wav` `57c57cae…`; cây git sạch; 162 s (`out/T11-rerun.txt`) | **ĐẠT** |
| T13 | ảnh LoC thật **X-F15-3**: https://www.loc.gov/item/2015631813/ (Carol M. Highsmith, 2015-05-07, dãy nhà bungalow, Huntington WV — **không người, không logo/nhãn hiệu**), `rights_advisory` "No known restrictions on publication." + bản chụp JSON mục (SHA đủ), 1840×1228. (Ảnh chọn trước — 2010630116, ngân hàng Fifth Third — có logo ngân hàng trên hình, RIGHTS F2 cấm → REVIEWER lượt 2 bắt, đã thay; clip/tờ khung chứa ảnh ngoài không còn trong git theo F5.2, chỉ `check.json`.) dòng RIGHTS **F6** bậc 5 (+ X-F15-1 Census bậc 2 — nay có trích nguyên văn TIGER/Line 2017 TechDoc tr. 1-2 (điều khoản §105 chung của Census; dữ liệu dùng là GENZ2017 qua us-atlas); X-F15-2 Natural Earth bậc 2). Dòng nguồn bản đồ trên hình có năm/phiên bản dữ liệu (F4): "Map data: U.S. Census Bureau 2017; Natural Earth 5.2.0-pre" (`map.py --census-year --ne-version` bắt buộc). Clip 540p 8 s (dựng lại bằng `footage-trial/run.sh`; mp4/tờ khung không commit — F5.2): 0/41 khung chữ đè chủ thể, **0 khung chữ đè chữ** (phép kiểm mới), nhãn trễ mốc từ 0–0,08 s | **ĐẠT** |
| T1 (rebase) | mã rebase lên `7f8a0da`, dựng 1080p lại cả tập (render không trúng cache vì khoá gồm `render_shots.js` đã sửa sau lượt 13/10 — 16.674 s): **9/9 spine/timeline/captions trùng byte** (`out/T1-bytes-rebased.json`); 6/7 đoạn hình + toàn bộ tiếng trùng byte bản giao P4 (`out/T1-segments-rebased.json`), đoạn e khác (không tất định, §5.2). Cùng container với lượt 13/10 (không phải container mới) | **ĐẠT** |
| T14 (rebase) | Tập 7 đoạn a cảnh s0, s1 (540p), mã rebase vs `main` c7358285: mp4 + nhật ký trùng byte (`out/T9-T14.md`) | **ĐẠT** |
| test | `python3 -m unittest discover -s toolkit/tests` trên mã rebase: **113 OK** (1 bỏ qua) | **ĐẠT** |
T4–T6 (checks) đo dưới LOCK `dc4981b3` (13/10), **chưa chạy lại dưới `b4551642`** (K4.4b đổi A14/S02/S07/S09 — không thuộc R_pix, không đổi đường nháp).
loc.gov sau Cloudflare: JSON mục trả 429 `cf-mitigated: challenge` nhiều lần → `fetch.py --loc` thử lại lùi dần (lần 6 qua). Phép kiểm "chữ đè chữ" mới thêm
lộ lỗi của lượt 13/10 mà phép kiểm cũ không đo: chú thích và dòng nguồn plate đè nhau, nhãn "Maryland" đè "South Atlantic" → đã sửa (`plate.js`
`drawCredits` đẩy dòng nguồn lên một dòng khi hai dòng giao nhau; nhãn bản đồ đặt lại).

## 2. Giờ máy (Tập 7, 606,7 s, 4 nhân, SwiftShader, 3 worker = số nhân − 1)
| Bước | nháp 540p | 1080p | tỉ lệ |
|---|---|---|---|
| world (7 đoạn: render + audio + verify) | 5.044 s | 12.797 s | 0,39 |
| render/splice/mix/artefacts/parts | 702 s | 1.012 s | 0,69 |
| Shorts (dọc) | 365 s | 932 s | 0,39 |
| qc + spec/voice/resolve | 65 s | 112 s | |
| **tổng** | **6.220 s = 1,73 h** (cột trên cộng 6.176 s + lúc chạy ngoài bước 44 s) | **14.855 s = 4,13 h** | **0,42** |
Nháp: lượt đầu 6.173 s trượt ở `qc` sau mọi bước (lỗi F-15 §5.1), lượt lại 1.459 s (đoạn thế giới trúng cache nhưng audio/verify chạy lại) →
giờ thực của phiên 7.632 s; số "sạch" = lượt đầu + `qc` 47 s. Lượt nháp chạy chồng việc nhẹ của phiên (test, ASR thử, `api.sh`); 1080p chạy trên máy rỗi.
So Tập 7 thật (TONGKET h): P3 ≈ 30 h máy (7 lượt 1080p), P4 dựng lại ≈ 2,9 h (2 trượt môi trường + 1 cắt 2 h). F-15: **1080p một lượt từ đầu, 0 trượt,
qua trần 2 h** (setsid nohup).
**Checks không rẻ hơn ở nháp:** bộ lấy mẫu trang tốn giờ theo trang thế giới 3D, không theo độ phân giải video (1080p: 5,9 h lượt 1 + 0,7 h chạy tiếp).

## 3. Checks đủ bộ (LOCK `dc4981b3`, baseline = báo cáo P4)
| | 1080p mới (`checks/report-1080.json`) | nháp 540p lượt 1 (`report-d540.json`) | nháp, luật Python sau sửa overlay (`report-d540-py2.json`) |
|---|---|---|---|
| PASS/FAIL/MISSING/ERROR | 55/43/1/1 | 50/48/1/1 | 53/45/1/1 |
| CHẶN chưa đạt | A14 S02 S07 S09 C07 | + F04 F05 F08 F11 REG | + **F08** REG |
| CHÍNH chưa đạt | V08 V09 V11 V12 L1 | như 1080p | như 1080p |
| giờ | 5,9 h (treo 1,5 h ở cảnh 34, §5.3) + 0,7 h chạy tiếp | 5,9 h, không treo | 0,34 h (PYONLY) |
CHẶN/CHÍNH chưa đạt của 1080p mới = đúng danh sách P4 trên bản đã giao (`c5/checks-reports/chk-p4-report.json`; P4 thêm SH01–05/REG
MISSING vì thiếu tệp) → bản 1080p dựng lại giữ nguyên chất lượng theo luật.
Năm CHẶN thừa ở nháp lượt 1 đều do **đường nháp**, không do nội dung: F04 (bitrate bản phóng 1,2 Mbps — mã hoá crf thay vì CBR 17M của master;
F04 lọt khỏi R_pix quét trước: luật đọc bitrate qua ffprobe), F05 (vọng lanczos đẩy Y ra ngoài 16–235 0,38 %), F11 (`splice.json` nháp trỏ
`work/factory-r540/world`, bản sao chưa có đường đó), REG (hệ quả). Sửa `draft_overlay.py` (`e22fd2d`): CBR 17M như master,
kẹp Y/C, chép world vào cả hai đường → chạy lại luật Python (`PYONLY=1 RESUME=1`, mẫu trang giữ): còn **F08** (banding 22 % ở 126 s, 134 s,
582 s — dither cố định theo ô 2×2 ở 1080 thành ô 1×1 ở 540 rồi phóng; khác độ phân giải thật, trong R_pix) + REG. **Quy ước dùng nháp:** F08,
F01 (cỡ khung, nay phóng nên ĐẠT), SH01 chỉ tin ở bản 1080p.

## 4. Cổng gốc tắt tiếng (`c4/blind_c4.py` root, 21 nhịp, 2 người đọc, 2 người chấm, không người thứ 3 cho bản nào)
| Lượt | Dải | ĐẠT | chờ người 3 |
|---|---|---|---|
| nháp, lượt 1 (đăng ký cho T7) | nháp | **17** | B21 |
| 1080p, lượt 1 (đăng ký cho T7) | 1080p | **9** | B23 |
| 1080p, đọc lại | **cùng dải 1080p** | 10 | — |
| nháp, đọc lại | **cùng dải nháp** | 7 | B09, B23, B28 |
Dải hai bản gần trùng (SSIM 22 dải 0,974–0,986, `out/T7-strip-ssim-d540-vs-1080.json`; B01 ĐẠT ở cả hai lượt đầu có 0,984). Cùng một dải, hai lượt lệch tới **10 nhịp** (nháp 17 → 7); hai lượt
1080p cùng dải chỉ cùng phán quyết 14/21 (67 %) → đích T7 (≥ 80 %, \|Δ\| ≤ 2) nằm dưới mức nhiễu của thước: T7 không phân biệt được nháp với 1080p
bằng thước này. Bằng chứng: `root-d540/`, `root-1080/`, `root-1080-rr/`, `root-d540-rr/`. Chi $5,52. Đề xuất cho phiên K (checks-appeal, không sửa ở đây):
cổng gốc cần ≥ 3 lượt đọc hoặc người thứ 3 bắt buộc trước khi gọi "hồi quy" (A32).

## 5. Lỗi, giới hạn, phát hiện
1. **Lỗi F-15 (đã sửa `0622a13`):** build nguyên tử ghi đường đích vào báo cáo, `qc.py` đọc Short theo đường đó trong khi tệp còn trong thư mục tạm →
   nháp trượt ở `qc` sau 1,7 h. Sửa: `qc` đọc từ `B.work`; thêm dọn `.new-<pid>` của tiến trình đã chết. Bản cũ không bị chạm (T10 thật).
2. **Đoạn e (S21–S24) Tập 7 không tất định:** dựng lại cảnh s3/s5 cùng mã, cùng khoá cache → byte khác, mọi khung SSIM ≥ 0,988 (render phụ thuộc lịch sử
   trang: thứ tự cảnh trong worker). Cũng là lý do đoạn e khác bản P4 (6/7 đoạn + toàn bộ tiếng trùng byte bản giao). Hệ quả: resume theo khung
   (và cache theo cảnh) chỉ trùng byte với scene "thuần" (`frame(t)` không mang trạng thái); scene e cho khung gần trùng. Hàng chờ: kiểm tất định trong
   `build_seg` (render một cảnh hai lần, so MD5) — mã của tập, không sửa ở đây.
3. **Bộ lấy mẫu trang treo** sau 33/34 cảnh (node rỗi 1,5 h, ≈ 70 ffmpeg đọc video không đóng) → dừng theo PID (`bg.sh stop`: 0 tiến trình sót), `RESUME=1`
   chạy tiếp 0,7 h. Lỗi trong `checks/` → phiên K.
4. Khoá cache render đổi một lần cho mọi đoạn (đổi `core.js`, `page.html`, `render_shots.js` — cine-lab #23): đoạn của tập đang làm dựng lại một lần;
   khung không đổi (T14).
5. `--spp` có, chưa đo tốc độ trên tập (nháp đo ở `spp` mặc định).
6. **Guard nhận nhầm shell của phiên** (lệnh nền có chuỗi `toolkit/build.sh` trong `bash -c "…"`) là build → build tự từ chối (mã 3). Sửa: guard chỉ khớp khi script là chương trình đang chạy (`guard.py`, 12/12 ca thử).
7. Tập 7 dùng ảnh/bản đồ ngoài ngược với gen "thế giới 3D tối giản, không chân thực ảnh" (CHARTER §4) — công cụ có sẵn, **dùng trong tập là quyết định của chủ dự án**.

## 5b. REVIEWER (headless khoá Console, $1,97, `reviewer/REVIEWER-out.txt`): ĐẠT có sửa
Đã sửa theo REVIEWER: T11 → "một phần"; T10 đo lại trên bản 1080p có sẵn (25/25 SHA); bằng chứng T3/T9–T12/T14 vào `out/`; dòng RIGHTS
M-USATLAS ghi rõ điều khoản Census chưa trích; `bg.sh stop` kiểm cả nhóm; chú thích `plate.js`; README ghi trần mặc định $5 của `api.sh`.
Để lại (PHỤ, ghi để điều phối quyết): `promote()` thay từng tệp (chết giữa promote → lẫn cũ/mới, cửa sổ < 1 s); `spec.yaml_bool_traps` đọc
`<root>/episode.yaml` chứ không đọc yml truyền vào; `episodes/ep008/episode.yaml` của nhánh `ep008` @ `24a6565` (chỉ đọc qua `git show`): 0 bẫy YAML boolean; `--resume` dùng chung
khoá cache — với scene không thuần (đoạn e) tệp cảnh dựng tiếp là bản gần trùng; `fetch.py` không tự kiểm chữ giấy phép với `license_url`;
`--name` bắt buộc nên tiêu đề LoC không tự điền; ASR thử chạy ở mọi lần `verify.sh` (≈ 20–60 s, cần model trong cache).

## 6. Mạng (chặn ở proxy, 403 CONNECT)
`www.loc.gov`, `tile.loc.gov` (ảnh LoC), `www2.census.gov` (TIGER/GENZ gốc), `naciscdn.org` (Natural Earth gốc), `fred.stlouisfed.org` (FRED),
`tile.openstreetmap.org`, `commons/upload.wikimedia.org`. Đường thay đã dùng: Census qua gói npm `us-atlas` 3.0.1, Natural Earth qua
`raw.githubusercontent.com/nvkelso/natural-earth-vector`. Mở mạng (cài đặt môi trường → Network access → Allowed domains) rồi chạy
`fetch.py <mục LoC> --loc --dest toolkit/factory/f15/footage-trial/assets …` (đặt tên tệp `loc.jpg`) + `footage-trial/run.sh` để hoàn tất T13.

## 5c. REVIEWER lượt 2 (14/10, trước merge; $2,25, `reviewer/REVIEWER-out-2.md`): ĐẠT có sửa — đã sửa
T12 (chạy lại), ảnh LoC có logo (thay ảnh, F2; clip/tờ khung ra khỏi git, F5.2), `map.py` dòng nguồn có năm dữ liệu (F4), REPORT bỏ "Không merge" + SHA sau rebase, ghi LOCK của T4–T6, bằng chứng T1 rebase. Cũng sửa: `fetch.py --loc` buộc bậc 5, SHA bản chụp đủ 64 ký tự; `drawMap` bỏ nhãn trỏ vùng không có; bỏ log SSIM từng khung và bản .md trùng của báo cáo checks khỏi git. Để lại (PHỤ): báo cáo spec BLOCK vẫn ghi `out_final`; `alive()` của bg.sh chỉ kiểm đầu nhóm; `draft_overlay` không chặn đích trong repo; fetch bỏ qua mã đã có dù SHA khác; X-F15-1 trích TechDoc TIGER/Line (điều khoản chung) cho dữ liệu GENZ2017.

## 7. Chi và token
Console: cổng gốc $5,52 (4 lượt) + thử `api.sh` $0,04 + REVIEWER $1,97 + $2,25 = **$9,78** (trần $15). Headless khoá Console, 0 agent con. Token phiên: §8.

## 8. Token phiên (4 số; đọc 14/10 ≈ 11:45 UTC, trước bản trả lời cuối)
| Nguồn | đầu vào mới | ghi cache | đọc cache | sinh ra | trần (mới + ghi + ra) |
|---|---|---|---|---|---|
| phiên điều phối (`get_session` usage, session_01JjJWbBd8p6ZevQ83UZbT8Z) | 7.535 | 3.754.551 | 67.582.340 | 177.591 | **3,94 triệu** |
| headless khoá Console (4 lượt cổng gốc 2×42 đọc + 8 chấm, REVIEWER, 3 thử `api.sh`) | 752 | 1.143.878 | 3.496.659 | 202.840 | **1,35 triệu** |
| **cộng** | 8.287 | 4.898.429 | 71.078.999 | 380.431 | **5,29 triệu** |
0 agent con. Chi Console $7,52 / trần $15.
