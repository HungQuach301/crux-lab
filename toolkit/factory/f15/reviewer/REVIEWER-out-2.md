# REVIEWER lượt 2: F-15 (`factory-f15` @ ed240aa, so `origin/main` 7f8a0da)

**Kết luận: ĐẠT có sửa.** Mã giữ được bất biến "trùng byte khi không bật cờ". Trước khi squash cần sửa hai chỗ: lời T12 trong REPORT trái bằng chứng, và ảnh LoC có logo ngân hàng. Không có phát hiện CHẶN.

Phạm vi: tôi chỉ đọc tệp, xem `git diff`/`git log` và vài JSON. Không chạy render, checks hay test.

## 1. Bất biến "opt-in hoặc trùng byte khi không bật cờ"
- **Đạt.** Không khai `--res/--spp/--resume`/plate thì:
  - đường dẫn, cache và tên đoạn thế giới giữ như cũ (`_cdir`, `rel()` cho ra đúng chuỗi cũ);
  - `core.js` vẫn `antialias` và `PR=1`; `render_shots.js` giữ nguyên cờ ffmpeg; `plate.js` chỉ vào khoá cache khi `scene.js` có nhắc tới nó;
  - `shorts.assemble(scale=False)` và `episode_page` (url = đường đích) không đổi;
  - `qc.py` đọc `B.work`, khi build không nguyên tử thì vẫn là tệp cũ;
  - `promote()` vào `<tập>/out` chỉ đụng camera.json, sonify-events.json, page.json (artefacts.py không ghi thư mục con).
- **Đạt.** `spec.yaml_bool_traps`: tôi quét ep003–ep007, không có bẫy YAML nào, nên tập cũ không bị thêm BLOCK. (PyYAML không coi `y` là bool, nên `ep003/episode.yaml:40` không bị bắt.)
- **PHỤ** `build.py:264`: khi spec BLOCK, `build-report.json` vẫn bị ghi đè vào `out_final`. Vậy câu "trượt thì bản cũ giữ nguyên" không đúng cho báo cáo ở nhánh này.
- **PHỤ** `build.py:193` + `guard.py:55`: giới hạn worker ≤ số nhân − 1 áp dụng cả khi không khai cờ. Docstring nói "số worker không đổi byte khung", nhưng chính REPORT §5.2 cho thấy đoạn e phụ thuộc thứ tự cảnh trong worker. Nên sửa lời.
- **PHỤ** `verify.sh:44`: lượt nhận dạng thử (ASR) và mục three.js chạy cả khi không có `--install`. Container offline chưa có model sẽ TRƯỢT ở chỗ trước đây ĐẠT. REPORT §5b đã ghi.

## 2. Đúng/sai mã
- **`bg.sh:29,40`: đúng.** Với `setsid -f nohup bash -c`, `$$` của bash là PID = PGID, và `stop` TERM rồi KILL cả nhóm.
  - **PHỤ:** `alive` chỉ kiểm tiến trình đầu nhóm (con mồ côi thì `stop` báo "không chạy"); `cd "$1"` không kiểm lỗi; có thể dùng lại PID cũ.
- **`verify.sh`: đúng.** `pipefail` không làm hỏng các dòng `$(… | head)`. Nhánh ASR chỉ ghim `av==14.2.0` khi có `--install` và lỗi là `AV`.
- **`api.sh:21`: cờ đúng.** Có `--disallowedTools Task,Agent,Workflow` và `--max-budget-usd`. Đường thoát 5 khi có `tool_use` Task/Agent chưa có lượt thử nào. Xem thêm T12 ở mục 3.
- **`draft_overlay.py:32-33`, PHỤ:** không chặn khi `dst` nằm trong repo hoặc trùng `src`. Gọi tay vào tập thật sẽ đè `out/video.mp4` và stems.
- **`fetch.py`:**
  - Đạt: bắt buộc giấy phép nguyên văn (`:97`); `--loc` kiểm `rights_advisory` và lưu bản chụp.
  - **PHỤ** `:82`: `--loc` không ép bậc 5.
  - **PHỤ** `:58`: dòng RIGHTS cắt SHA bản chụp còn 16 ký tự.
  - **PHỤ** `:65`: mã đã có thì bỏ qua, kể cả khi SHA tệp mới khác.
- **`map.py:143`, CHÍNH:** dòng nguồn cứng `"Map: U.S. Census Bureau; Natural Earth"` không có năm dữ liệu. RIGHTS F4 bắt bản đồ ghi nguồn và năm (GENZ2017). Mọi tập dùng `map.py` sẽ lặp lỗi này.
- **`plate.js`:**
  - **PHỤ** `:80-83`: khi đẩy dòng nguồn lên một dòng, không kiểm va chạm với dòng `numbers` (tuy hai dòng ở hai phía).
  - **PHỤ** `:110`: `drawMap` sập nếu `L.id` không có trong bản đồ.
  - **PHỤ:** độ dài hoà ≥ 0,8 s chỉ dựa vào dữ liệu khai, mã không ép.

## 3. REPORT so với bằng chứng và INTENT
Đích không bị hạ: INTENT chỉ có một commit (989fc39, trước mọi lượt đo); T1–T14 trong REPORT trùng INTENT §3. T3 0,419 và T7 đều ghi TRƯỢT.

Từng dòng khớp bằng chứng:

| # | Bằng chứng | Khớp |
|---|---|---|
| T1 | 9/9 (cả `-rebased`) | có |
| T2 | 0,9843, S23 0,9813, khung thấp nhất 0,9748 | có |
| T3 | 6.173 + 47 = 6.220 / 14.855 = 0,419 | có |
| T4–T6 | 95 % → 98 %, 0 bỏ sót | có |
| T7 | đếm từ tally: 17 / 9, cùng phán quyết 10/21 | có |
| T10 | 25/25 SHA, `diff` rỗng | có |
| T11 lượt lại | 162 s, `rc=0` | có |
| T13 | 0/41, 0 khung chữ đè chữ | có |

Chỗ nói quá hoặc sai:
- **CHÍNH** `REPORT.md:25` (T12): REPORT viết "init không có Task/Agent/Workflow". Nhưng `out/T12-api.json:3-5,19-21` cho thấy **`Workflow` có trong công cụ lúc init** ở `cap.jsonl` và `sub.jsonl`. `sub.jsonl` chính là lượt thử agent con. Chỉ `cap2` sạch. Cách sửa: chạy lại lượt thử agent con với `api.sh` hiện tại (≈ $0,01), hoặc hạ T12 xuống "ĐẠT một phần".
- **PHỤ** `REPORT.md:8`: còn câu "**Không merge.**", trái với dòng 3.
- **PHỤ** `REPORT.md:7,86,68`: các SHA `6c42086`, `086fcee`, `dcf23c1` là SHA trước rebase, không còn trên nhánh và sẽ mất sau squash. SHA hiện tại: 989fc39, 0622a13, e22fd2d. Đầu bài lượt này cũng dẫn 6c42086.
- **PHỤ** `REPORT.md:36`: câu "6/7 đoạn hình + toàn bộ tiếng trùng bản giao" trên mã rebase không có tệp bằng chứng mới; `T2-segments-vs-delivered.json` là của ngày 13/10. T1 rebase và T11 lượt lại chạy trên cùng container, không phải "container mới".
- **PHỤ** §3/§1b: T4–T6 đo dưới LOCK `dc4981b3`, chưa chạy lại dưới `b4551642`. §3 có ghi LOCK, nhưng §1b nên nói rõ.
- **PHỤ:** bằng chứng T9 là số chép tay (cache đã xoá, `out/T9-T14.md:1`).

## 4. Bản quyền và an toàn
- **Ba dòng X-F15-1..3 (`RIGHTS.md:57-59`): đúng.** Đủ 10 cột, bậc đúng (2/2/5), trích nguyên văn, có ngày và SHA. Bản chụp LoC có `rights_advisory` "No known restrictions on publication." khớp, kèm câu "không bảo đảm".
- **CHÍNH: ảnh LoC (X-F15-3) có logo và chữ "Fifth Third Bank" rõ trên hình** (`footage-trial/out/sheet.jpg`). RIGHTS F2 cấm "logo, nhãn hiệu", nhưng REPORT §1b gọi T13 là ĐẠT và dòng RIGHTS ghi như đã sạch. Clip 540p và `sheet.jpg` (có ảnh này) lại được commit, trái F5.2 ("trong repo chỉ RIGHTS + băm"). Cách sửa: thay ảnh, hoặc bỏ mp4/sheet khỏi commit và ghi "vi phạm F2, chỉ dùng thử" vào dòng RIGHTS.
- **PHỤ:** X-F15-1 trích TechDoc của TIGER/Line, trong khi dữ liệu là GENZ2017 qua us-atlas. Cột Ghi nguồn và dòng nguồn trên hình bản đồ thiếu năm (F4, xem `map.py:143`).
- **Clip theo F3/F4: đạt.** Mở bằng 3D, plate từ 1,0 s, hoà vào 1,2 s; năm 2009 + nguồn có trên hình; dòng nguồn không đè chú thích (0 khung chữ đè chữ).

## 5. README nhà máy và phạm vi tệp
- **Đạt.** `toolkit/factory/README.md:11-14` ghi đủ quy ước nháp: F08, F01, SH01 chỉ tin ở 1080p; bộ lấy mẫu trang không rẻ hơn ở nháp, chờ A29.
- **Đạt.** Diff chỉ chạm `toolkit/` và `RIGHTS.md`. Không đụng `episodes/` (kể cả ep008) hay `checks/`.
- **PHỤ:** squash sẽ đưa vào main khoảng 52 nghìn dòng (`ssim-frames.log` 18 nghìn dòng, ba báo cáo checks khoảng 7 nghìn dòng mỗi tệp) và 2 MB mp4. Nên cân nhắc cắt bớt.

## 6. Kết luận
**ĐẠT có sửa.** Trước squash cần:
1. Sửa T12: chạy lại lượt thử agent con, hoặc ghi "ĐẠT một phần".
2. Xử lý ảnh LoC có logo (F2): thay ảnh, hoặc bỏ clip/sheet khỏi commit.
3. Thêm năm dữ liệu vào dòng nguồn của `map.py`.
4. Bỏ câu "Không merge." và cập nhật các SHA sau rebase trong REPORT.
