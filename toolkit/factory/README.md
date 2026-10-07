# toolkit/factory — nhà máy dựng (Mốc B)

Một lệnh: `bash toolkit/build.sh episodes/epNNN/episode.yaml [--workers 4] [--fmt jpeg|rgba] [--no-cache]`

| File | Việc |
|---|---|
| `spec.py` | Kiểm `episode.yaml` (format lab/101, mid-roll, scope excerpt, claim tồn tại, custom_symbols ≤ 2 → hỏi, Shorts 2–3) trước mọi gọi API |
| `voice.py` | ElevenLabs `with-timestamps` mỗi cảnh một lần, cache SHA-256 (lời nói + voice + model + seed + settings), ký tự → mốc từ |
| `build.py` | spec → giọng → giải "@câu[:từ][$][+s]" → `timeline.json` + `captions.srt` (≤ 2×42 ký tự, 1–7 s) → render đoạn đổi → trộn + loudnorm 2 lượt → master → 3 phần 720p → Shorts → qc |
| `render.js` + `page.html` | Playwright, mỗi worker một trang; khung trung gian JPEG q 0,95 (hoặc RGBA để đo); mỗi đoạn một file H.264 ghép bằng concat copy; log engine mỗi 6 khung |
| `lib/engine.js`, `lib/templates.js` | Engine canvas (sàn chữ, tương phản, vùng an toàn, va chạm, nhãn ILLUSTRATIVE/history, đẩy máy) và 10 mẫu |
| `music.py` | Trộn lời + nhạc nền ở mức Tập 3 (A07 20 dB, né 1–4 kHz 13 dB), ghi stem voice/music |
| `qc.py` | Luật làm việc của bên dựng (không thay `checks/`) → `out/factory/qc.md` |
| `excerpt_checks.py` | Chạy các luật `checks/` không cần trang trên đoạn trích (kiểm LOCK trước) |

File nặng (video, cache đoạn, wav) ở `episodes/epNNN/work/factory/` (không commit); báo cáo ở `episodes/epNNN/out/factory/`.
**Take giọng được commit** ở `episodes/epNNN/voice-takes/` (`<băm16>.mp3` + `<băm16>.json`: băm SHA-256 của lời nói + voice + model + seed + settings, văn bản, alignment). Đổi container không sinh lại giọng (Tập 4 mất cache → 8.148 ký tự EL sinh lại). Dung lượng ≈ 16 KB/s lời (mp3 128 kbps) ≈ 8 MB/tập 8 phút kể cả take thử.
Đoạn render được cache theo băm (đặc tả shot + mốc đã giải + mã engine/mẫu/trang/render + claims/tokens/dữ liệu + khoảng khung).
**Đối trọng (bắt buộc):** `counterweights:` trong `episode.yaml`, mỗi dòng `{id, text, claims: [...] | when: historical|numbers, attach?: history}`. `spec.py` gom mọi dòng hồ sơ đòi (nhãn "Counterweight on screen" trong `story/script.md` của cảnh được dựng, `Always say "…"` trong claim-risk, giả định `contract.json`); thiếu trường hoặc thiếu dòng → `build.sh` dừng. Engine hiện dòng trên mọi khung có claim kích hoạt; qc kiểm mỗi dòng ≥ 1 s.
**Nhạc nền:** `audio.music` (+ `music_cmd` để sinh lại) → `music.py`: nhạc dưới lời 20 dB (cách đo A07), dải 1–4 kHz né lời 13 dB, như Tập 1–3; rồi loudnorm 2 lượt. Đã chạy trên S04 Tập 3: A07 19,99 dB, A08 né 7,9 dB, −14,0 LUFS, −1,5 dBTP.

## Thế giới 3D (D-010, Mốc V) — `toolkit/factory/world/`
"Một thế giới, hai chế độ máy quay". Khai trong `episode.yaml`: `world: [{id, dir, scenes: [S04, S05]}]` (`dir` chứa `spine.py` + `scene.js` của đoạn).
`spec.py` chặn khi thiếu file hoặc cảnh lạ; `build.py` bước `world` gọi `world/build_seg.py` cho từng đoạn (spine đọc lời từ `out/factory/timeline.json`
qua biến `CRUX_TIMELINE`, `spine.words_from_timeline`) và dừng nếu tổng spine ≠ độ dài các cảnh. Ghép vào master: BACKLOG F-5.

| File | Việc |
|---|---|
| `lib3d.js` | Thư viện vật thể có tham số W1–W9 (nhà, chồng tiền mệnh giá cố định, xà, người không mặt, vệt, bó đường, khiên, khu phố, căn hộ) — `visual-library` §5 |
| `core.js` | Máy quay theo tư thế + động tác hữu hạn từ spine, trọng số chế độ đồ thị, lớp phủ 2D (chữ ≥ 48 px, nền mờ), nhật ký quy tắc 1 |
| `spine.py` | Spine v2: `Anchors` ("@câu[:từ][$]"), `beats_from`, `window` (giữa hai từ khoá ± pad), `move_sounds`, `shots_for`, `check_rules` (2/3/7), `words_from_timeline` |
| `onset.py` | Đầu từ = lúc nghe được (năng lượng), không phải mốc TTS |
| `render_shots.js` + `page.html` | Render theo cảnh, cache SHA-256 (mã thư viện + cảnh + spine + dữ liệu + khoảng + độ phân giải), resume, lỗi trang = dừng, nhật ký 0,1 s |
| `audio.py` | Lời + nhạc theo bản đồ căng (`music_plan`) + âm dữ liệu + sfx từ `spine.events`, `mix` {music_db, data_db}, −14 LUFS |
| `verify_seg.py` | Quy tắc 1/2/3, cắt cứng, tỉ lệ chế độ, C14 (bản 1080p) trên sản phẩm cuối |
| `sync_audit.py` | Đồng bộ lời/hình/âm ±0,2 s bằng ASR (faster-whisper) — chạy tay |
| `lint_comments.py` | Bắt "chú thích nuốt mã" |
| `build_seg.py` | Một lệnh: lint → spine → render → audio → mux → verify; báo giờ render thật (`<out>.build.json`) |
| `vendor/package.json` | three 0.186.1 (`npm ci`; node_modules không commit) |

Giờ render đo được (4 lõi, SwiftShader, 3 worker, 540p): Tập 4 đoạn 69,6 s → 135,5 s; Tập 5 đoạn 34 s → 76 s (≈ 2 s máy/s phim); cache trúng → < 1 s.
