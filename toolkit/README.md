# toolkit/ — bộ công cụ v0 (dùng lại, không phải nền tảng)

Đây là bộ công cụ đã chạy thật ở bài D. Phiên B0 chép nó vào đây ngày 2026-09-28 để Tập 1 dùng lại.

Nó **không phải nền tảng**. Code thực thi là đồ dùng một lần (CHARTER §3.1). Phiên dựng Tập 1 được sửa, chép, hay bỏ bất cứ file nào ở đây. Chỉ tách thành công cụ chung khi một bước đã làm tay ≥ 3 lần (CHARTER §2.2).

**Nguồn:** repo [crux-spike-opus55](https://github.com/HungQuach301/crux-spike-opus55), nhánh `claude/opus55-cine-phase-d-jw6me1` @ `76613cfa756e2604770043435f79eb00e269e2b6`. Phim r3 (master `6531f6c8…`) được dựng bằng chính các file này.

## Nội dung

| Thư mục | File | Nguồn gốc (bài D) | Việc |
|---|---|---|---|
| `render/` | `engine.js`, `page.js`, `page.html`, `cameras.js`, `scenes.js`, `BUILDERS.md`, `fonts/` | `render-d/prod/*`, `render-av/fonts/` | Trang dựng Chromium: biểu đồ trên mặt phẳng, parallax, máy quay có quán tính, chữ HUD sắc nét. Mỗi phần tử vẽ ra được khai báo làm đối tượng hợp đồng (`window.CHECKS`). `scenes.js` chứa các helper (`K`) và, làm ví dụ, các builder hồi 1 của bài D. |
| `render/` | `render.js` | `render-d/prod/render.js` | Playwright → khung PNG → ffmpeg; render theo đoạn `--from/--to`. |
| `render/` | `m3-merge.js`, `m3-encode-range.js`, `m3-splice.js` | `src/d/` | Ghép các đoạn render. Render lại riêng từng cảnh rồi ghép vào master tại keyframe, không render lại cả phim. |
| `voice/` | `normalize.js`, `speak.js` | `src/av/normalize.js`, `src/d/speak.js` | Chuẩn hoá lời: số, năm, tiền, % thành chữ đọc được. (`pauses.js`, chèn "..." giả để ép tốc độ đọc, đã xoá 2026-09-29 theo G-010 và `playbook/quality-framework.md`.) |
| `voice/` | `d_el_voice.py`, `d_el_voice_one.py` | `audio/` | TTS ElevenLabs qua proxy: mỗi câu tối đa 4 take, không giãn thời gian. **Từ 2026-09-29:** một model giọng cả tập (model dự phòng tắt, `MAX_FALLBACK = 0`); wpm chỉ là cảnh báo, không dùng làm đích để chọn take (G-010). |
| `voice/` | `d_asr.py`, `d_choose.py` | `audio/` | faster-whisper (small.en, int8): chép lời từng take, lấy mốc từ, chọn take. |
| `audio/` | `d_m2_audio.py` | `audio/d_m2_audio.py` | Nhạc sinh bằng code (phối theo hồi, leitmotif), sound design, sonification, khoảng lặng có chuyển tiếp, ducking đa dải, master −14 LUFS và limiter true peak, ghi stem. |
| `audio/` | `m3-sonify-events.js` | `src/d/` | Đọc trạng thái trang theo từng khung, sinh sự kiện âm thanh theo dữ liệu. |
| `audio/` | `loudness.py`, `d_music_selfsim.py`, `d_tension.py` | `audio/` | Đo BS.1770; đo độ tự tương đồng của nhạc; đo bản đồ căng–chùng. |
| `finish/` | `m3-glue.js`, `m3-finish.sh`, `frame-change.py` | `src/d/` | Sinh các file hợp đồng: tempo map, transitions, silences, phụ đề, cues, sfx-events. Mux hình và tiếng, xuất bản xem trước, đo frame-change. |

## Đã bỏ khi chép

- **Toàn bộ phần 3D** (CHARTER §5; BRIEF-D-amendments 11):
  - `render-d/look/` (world.js, three.js);
  - `render-d/engine.js`, `run-step0.js`, `step0.html`, `prof-step0.js` (render thử cảnh 3D, DOF, blur 8×);
  - `preprod/visual-bible.md`, `preprod/visual-grammar.md`;
  - hàm `physical()` (âm thanh gió, mưa, nước, sấm của thế giới lookdev) trong `d_m2_audio.py`, cùng lớp `amb` và dòng sổ giấy phép của nó.
  Các số hạ nhạc quanh số được đọc (`out/physical.json` → `numbers`) vẫn giữ; tên file là di sản.
- **Nội dung riêng của bài D:**
  - mô hình, claims, kịch bản, shot list;
  - `scenes-a2.js`, `scenes-a3.js`, `scenes-end.js`, `cameras-m3.js`, `data.js`;
  - `src/d/m3-build.js` (dựng `data.js` từ mô hình bài D).
- **Công cụ không còn dùng:**
  - `d_tts.py` (gpt-4o-mini-tts, đã thay bằng ElevenLabs theo amendment 1);
  - `d_tableread.py` (giãn thời gian bằng rubberband, bị cấm với giọng ElevenLabs);
  - `d_el_audition.py` (thử giọng mù, đã xong);
  - `src/d/m3-media.sh` (đẩy master lên nhánh media);
  - `m3-post.sh`, `m3-r2-finish.sh` (điều phối riêng của bài D);
  - toàn bộ công cụ bài B/C (`render/`, `render-motion/`, `render-av/`, `audio/av_*`).
- **`checks/`** của bài D: không chép. Phiên K1 viết luật mới.

## Sửa khi chép

1. `render/page.html`:
   - đường dẫn font trỏ tới `fonts/`;
   - bỏ các thẻ `<script>` của cảnh riêng bài D.
2. `voice/speak.js`: `require('../av/normalize')` → `require('./normalize')`.
3. `audio/d_m2_audio.py`: bỏ phần 3D như trên.

Mọi file khác giữ nguyên văn. Tất cả qua `node --check` và `python3 -m py_compile`.

## Sửa ở Tập 1, bước 0 (Phiên D1, 2026-09-28)

**Bố cục mới.** Mọi công cụ nhận **gốc tập** (`episodes/<tập>/`, hoặc một gốc thử như `episodes/ep001/m0-sample/`), qua đối số hoặc biến `EP_ROOT`:

| Ở đâu | Chứa gì |
|---|---|
| `<gốc>/out/` | file hợp đồng (`checks/CONTRACT.md`) |
| `<gốc>/render/data.js`, `scenes-ep.js` | dữ liệu trang dựng và các builder cảnh của tập; `toolkit/render/page.html?root=<gốc>` nạp hai file này |
| `<gốc>/edit/glue.json`, `cues.json`, `description.md` | quyết định dựng của tập mà `m3-glue.js` trước đây viết cứng (bảng match cut, khoảng lặng, accent, điểm quảng cáo, impact, tempo theo hồi, cue sheet, mô tả với `{act:…}`/`{scene:…}`) |
| `<gốc>/work/` | file làm việc không giao: `picture.mp4`, `stills/`, `render-run.json`, `text-first.json`, `audio-report.json`, `preview.mp4` |
| `$FRAMES_DIR` (mặc định `<tmp>/crux-frames/<tập>/`) | các phần render không nén |

**Tách khỏi `checks/`.** `voice/d_el_voice.py` và `voice/d_choose.py` không còn nhập gì từ `checks/`. Bên dựng có hàm riêng `voice/keywords.py` (`key_words`, `match_keys`: số so theo giá trị và đơn vị, tên riêng, thuật ngữ của tập; gộp token ASR kiểu "18" ".63" "%"). Đây là bộ lọc chọn take của bên dựng, không phải luật A14; máy kiểm vẫn đo trên master bằng định nghĩa của nó. `python3 toolkit/voice/keywords.py` chạy test tự kiểm.

**Âm thanh theo dữ liệu (sổ gu G-001).** `audio/d_m2_audio.py`:
- ghi stem riêng `sonify` (không trộn vào `sfx`), đúng `checks/CONTRACT.md`;
- **không** hạ lớp này dưới lời nữa (bài D hạ −10 dB dưới lời và −16 dB quanh số, nên không nghe thấy);
- âm sắc mới đặt năng lượng ở 1,5–8 kHz (cao độ gốc MIDI 72–96, bồi âm 2–5): đường vẽ là một âm liên tục có rung nhẹ, cao độ theo độ dốc và pan theo x; điểm là tiếng gảy sáng theo trục y; cột là âm vút lên cao độ theo giá trị; bộ đếm là tiếng tích 3–8 kHz;
- nhạc được khoét 9 dB ở 1,5–8 kHz trong lúc có tiếng dữ liệu;
- sổ giấy phép ghi vào `<gốc>/out/music-ledger.json`.
- `audio/sonify_palettes.py` (Tập 1, sau khi chủ dự án nghe m0, sổ gu G-005/G-006): ba bảng âm (mallet, breath, minimal) với luật chung: sidechain −8 dB dưới lời, bỏ 1–4 kHz khi có lời, dời nốt vào khe âm tiết, giữ ánh xạ cao độ, cân cùng độ to. Bảng được chọn sẽ thay hàm `sonify()` của `d_m2_audio.py` ở M2.

**Khác:** `render/render.js`, `m3-merge.js`, `m3-encode-range.js`, `m3-splice.js`, `audio/m3-sonify-events.js`, `finish/m3-finish.sh`, `finish/m3-glue.js`, `voice/d_asr.py`, `voice/d_el_voice_one.py` đổi đường dẫn theo bảng trên. `m3-finish.sh` nhận gốc tập làm đối số.

**Chạy đầu cuối:** đã chạy trên mẫu 10 giây `episodes/ep001/m0-sample/` (xem `README.md` ở đó).

## Phải biết trước khi dùng

- **Còn di sản bài D trong code:** `scenes.js` giữ các builder hồi 1 của bài D làm ví dụ; `d_m2_audio.py` còn bảng động lực theo cảnh (`SECT`) và leitmotif hai nhân vật gắn id cảnh của bài D (không khớp id nào của tập khác thì không có tác dụng).
- **Khoá ElevenLabs do proxy môi trường gắn** (header `xi-api-key`). Khoá không có trong code, lệnh hay log. Giọng đang dùng: Eric `eleven_v3`, dự phòng `eleven_multilingual_v2`. Đây là giọng tạm, không phải quyết định #158.
- **Lỗi đã biết của trang dựng:** nhãn bị nhân đôi hoặc nhoè khi máy quay chuyển (audit §3a, D-2). Nhãn trong cold open của bài D đã sửa bằng cách vẽ tại giữa phơi sáng; các cảnh khác chưa sửa.
- **Phụ thuộc:**
  - Node 20+ và `playwright` (Chromium có sẵn ở `/opt/pw-browsers`);
  - Python 3 với `numpy`, `scipy`, `requests`, `faster-whisper`;
  - `ffmpeg` (bài D tự cài bằng `apt-get`).
  Chưa có `package.json` ở repo này. Dùng `playwright` cài toàn cục: `export NODE_PATH=$(npm root -g)`.

## Playbook v2 (04/10/2026, Phiên T2): script hoá ba bước đã làm tay ≥ 3 lần

Ngoại lệ được chủ dự án duyệt (D-005). Test: `python3 -m unittest discover -s toolkit/tests -v` (cần `ffmpeg`, `ffprobe`, `git`; không cần mạng).

| Thư mục | File | Việc | Đã làm tay |
|---|---|---|---|
| `blind/` | `strips.py` | Cắt dải kiểm mù: 6 khung tâm 6 lát bằng nhau trong [t0, t1], lưới 3×2 đánh số, cùng bố cục Tập 2; ghi thời điểm khung và SHA-256 | Tập 1 C4; Tập 2 C3, K1/K7 ×3, K2/K4/K5 ×2, C4 ×3 |
| `blind/` | `packets.py` | `deal` chia mẫu (thư mục hex, một file, khoá ngoài thư mục người đọc); `packet` gói người chấm mù tập (nhãn ngẫu nhiên, rubric nghĩa / tả hình); `tally` gộp điểm, luật câu khuyên, **dừng sớm**, cổng chỉ tính nhịp loại 1; `next` liệt kê nhịp cần người đọc thứ 3 | Tập 1 C1–C4; Tập 2 ≈ 15 lượt kiểm mù |
| `deliver/` | `deliver.py` | Mã hoá bản tải YouTube (bitrate khuyến nghị theo độ phân giải và fps, audio copy, +faststart); chia phần 90 MB; `SHA256SUMS`; `JOIN.md` lệnh ghép Windows/Mac; tuỳ chọn commit lên nhánh mồ côi `epNNN-delivery` qua worktree tạm và đẩy (thử lại 2/4/8/16 s) | Tập 2: bản gốc, CRF 18, phần 477 MiB, phần 150 MiB, phần 90 MB |

### Ứng viên tự động hoá khác — chỉ liệt kê, CHƯA viết mã
| Ứng viên | Số lần đã làm tay |
|---|---|
| Kiểm máy kịch bản: claim ID có thật, S10, "US only", "history, not a forecast" | Tập 2: 5 lần (v1–v5) |
| Chạy checks trên bản sao khoá (`git archive` + so SHA LOCK) | Tập 2: 5 lần (K3.4, K3.5 thử, K3.6, C5, C6) |
| Ghép clip gói cổng xem trên điện thoại | Tập 2: 6 lần (C2, C3, C3c, C4, C6 nổi bật, nhạc A/B) |
| Ghi quyết định cổng vào `taste-ledger.md`, `AUTHORSHIP.md`, `ledger.md` | Tập 2: 11 lần |
| Sinh giọng theo cảnh, chỉ cảnh đổi chữ (`episodes/ep002/story/table_read.py`) → chuyển vào `toolkit/voice/` | Tập 1: 1 (v3.2); Tập 2: 4 (table read v3, v5, C5 S08, C5 S04/S09/S10) |
| Mix + kiểm tiếng lại trên video thật | Tập 2: 3 lần |
| So cặp gói phát hành (tiêu đề, thumbnail) | Tập 1: 1; Tập 2: 2 |
| Kiểm 25% đọc được | Tập 1: 1; Tập 2: 2 (animatic, thẻ phương pháp) |
| Mô phỏng mù màu cặp màu | Tập 1: 1; Tập 2: 1 — chưa đủ 3 lần |

### Thư viện hình
`visual-library/`: ký hiệu đã qua kiểm mù ở Tập 1–2, bảng màu E2, phông, mã tham chiếu, ảnh xem trước. Xem `visual-library/README.md`.
