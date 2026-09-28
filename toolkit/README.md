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
| `voice/` | `normalize.js`, `speak.js`, `pauses.js` | `src/av/normalize.js`, `src/d/speak.js`, `src/d/pauses.js` | Chuẩn hoá lời: số, năm, tiền, % thành chữ đọc được; chèn chỗ nghỉ. |
| `voice/` | `d_el_voice.py`, `d_el_voice_one.py` | `audio/` | TTS ElevenLabs qua proxy: mỗi câu tối đa 4 take, không giãn thời gian, chọn take theo từ khoá và wpm. |
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

Mọi file khác giữ nguyên văn. Tất cả qua `node --check` và `python3 -m py_compile`. **Chưa chạy lại đầu cuối trong repo này.**

## Phải biết trước khi dùng

- **Đường dẫn vẫn theo bố cục repo bài D.** Ví dụ: `out/…`, `out/m3/root`, `render-d/prod/…`, `ROOT = dirname/..`. Phiên dựng Tập 1 chỉnh đường dẫn theo thư mục tập của mình (`episodes/<tập>/`).
- **`m3-glue.js` chứa dữ liệu của bài D**, ví dụ bảng `MATCH` của các match cut. Thay trước khi dùng.
- **`d_el_voice.py` và `d_choose.py` nhập `key_words`, `match_keys` từ `checks/py/r_audio.py`.** Đây là thiết kế cố ý: bên dựng dùng đúng định nghĩa của bên kiểm, chỉ đọc. `checks/` đang trống. Đến khi Phiên K1 cung cấp hàm tương đương, hai file này chưa chạy được. Hàm cũ của bài D có lỗi stem không đối xứng và lỗi nối `&` (audit §4.1–4.2).
- **Khoá ElevenLabs do proxy môi trường gắn** (header `xi-api-key`). Khoá không có trong code, lệnh hay log. Giọng đang dùng: Eric `eleven_v3`, dự phòng `eleven_multilingual_v2`. Đây là giọng tạm, không phải quyết định #158.
- **Lỗi đã biết của trang dựng:** nhãn bị nhân đôi hoặc nhoè khi máy quay chuyển (audit §3a, D-2). Nhãn trong cold open của bài D đã sửa bằng cách vẽ tại giữa phơi sáng; các cảnh khác chưa sửa.
- **Phụ thuộc:**
  - Node 20+ và `playwright` (Chromium có sẵn ở `/opt/pw-browsers`);
  - Python 3 với `numpy`, `scipy`, `requests`, `faster-whisper`;
  - `ffmpeg` (bài D tự cài bằng `apt-get`).
  Chưa có `package.json` ở repo này. Tập 1 tạo khi cần.
