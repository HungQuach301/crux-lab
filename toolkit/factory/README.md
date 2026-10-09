# toolkit/factory — nhà máy dựng (Mốc B)

Một lệnh: `bash toolkit/build.sh episodes/epNNN/episode.yaml [--workers 4] [--fmt jpeg|rgba] [--no-cache]`

| File | Việc |
|---|---|
| `spec.py` | Kiểm `episode.yaml` (format lab/101, mid-roll, scope excerpt, claim tồn tại, custom_symbols ≤ 2 → hỏi, Shorts 2–3) trước mọi gọi API |
| `voice.py` | ElevenLabs `with-timestamps` mỗi cảnh một lần, cache SHA-256 (lời nói + voice + model + seed + settings), ký tự → mốc từ |
| `build.py` | spec → giọng → giải "@câu[:từ][$][+s]" → `timeline.json` + `captions.srt` (≤ 2×42 ký tự, 1–7 s) → [world] → render đoạn đổi → [splice] → trộn + loudnorm 2 lượt → master → [artefacts] → 3 phần 720p → Shorts (1080×1920, −14 LUFS mỗi Short) → qc |
| `render.js` + `page.html` | Playwright, mỗi worker một trang; khung trung gian JPEG q 0,95 (hoặc RGBA để đo); mỗi đoạn một file H.264 ghép bằng concat copy; log engine mỗi 6 khung |
| `lib/engine.js`, `lib/templates.js` | Engine canvas (sàn chữ, tương phản, vùng an toàn, va chạm, nhãn ILLUSTRATIVE/history, đẩy máy) và 10 mẫu |
| `music.py` | Trộn lời + nhạc nền ở mức Tập 3 (A07 20 dB, né 1–4 kHz 13 dB), ghi stem voice/music |
| `qc.py` | Luật làm việc của bên dựng (không thay `checks/`) → `out/factory/qc.md`; F-2 hộp chữ giao nhau = CẢNH BÁO (không làm trượt) |
| `excerpt_checks.py` | Chạy các luật `checks/` không cần trang trên đoạn trích (kiểm LOCK trước) |

File nặng (video, cache đoạn, wav) ở `episodes/epNNN/work/factory/` (không commit); báo cáo ở `episodes/epNNN/out/factory/`.
**Take giọng được commit** ở `episodes/epNNN/voice-takes/` (`<băm16>.mp3` + `<băm16>.json`: băm SHA-256 của lời nói + voice + model + seed + settings, văn bản, alignment). Đổi container không sinh lại giọng (Tập 4 mất cache → 8.148 ký tự EL sinh lại). Dung lượng ≈ 16 KB/s lời (mp3 128 kbps) ≈ 8 MB/tập 8 phút kể cả take thử.
Đoạn render được cache theo băm (đặc tả shot + mốc đã giải + mã engine/mẫu/trang/render + claims/tokens/dữ liệu + khoảng khung).
**Đối trọng (bắt buộc):** `counterweights:` trong `episode.yaml`, mỗi dòng `{id, text, claims: [...] | when: historical|numbers, attach?: history}`. `spec.py` gom mọi dòng hồ sơ đòi (nhãn "Counterweight on screen" trong `story/script.md` của cảnh được dựng, `Always say "…"` trong claim-risk, giả định `contract.json`); thiếu trường hoặc thiếu dòng → `build.sh` dừng. Engine hiện dòng trên mọi khung có claim kích hoạt; qc kiểm mỗi dòng ≥ 1 s.
**Nhạc nền:** `audio.music` (+ `music_cmd` để sinh lại) → `music.py`: nhạc dưới lời 20 dB (cách đo A07), dải 1–4 kHz né lời 13 dB, như Tập 1–3; rồi loudnorm 2 lượt. Đã chạy trên S04 Tập 3: A07 19,99 dB, A08 né 7,9 dB, −14,0 LUFS, −1,5 dBTP.
**Nhạc hiệu kênh (F-12, C3 Tập 6 08/10: theme A):** `toolkit/factory/theme/` = `ident-A.wav` (3,0 s, −16 LUFS), `close-A.wav` (khúc đóng 10,5 s, chạm 8,42 s), `theme.json` — đúng từng byte bản duyệt (nhánh ep006 `episodes/ep006/world/music/out/`, sinh bằng `theme.py` của tập). Opt-in trong `audio:`, `music.post` chạy sau trộn/ghép đoạn thế giới, trước loudnorm (2D và thế giới như nhau): `ident: {after: S03, wav?, db?}` → `IDENT_S` 3 s cuối đuôi cảnh `after` phát WAV (mặc định ident-A, đường dẫn từ gốc repo; đuôi ≥ 3 s, lời lấn vào → dừng), mức = lời của tập + `db` (−2 LU), nhạc nền nhường 0,25 s; `close_lift_db: 12` (+ `close_lift_s: 0.5`, `close_lift_delay_s: 0`) → sau chữ cuối (mốc từ cuối ∨ lời tắt trên stem voice) stem music lên +12 dB trong 0,5 s, khi còn lời nhạc không đổi. Khúc đóng tự đặt vào bed của tập (`music_cmd`). Không khai → không chạm file (master trùng byte). Test `toolkit/tests/test_factory_f12.py`: −14,0 LUFS, −1,0 dBTP, A07 19,97 dB sau khi nâng.

## Thế giới 3D (D-010, Mốc V) — `toolkit/factory/world/`
"Một thế giới, hai chế độ máy quay". Khai trong `episode.yaml`: `world: [{id, dir, scenes: [S04, S05]}]` (`dir` chứa `spine.py` + `scene.js` của đoạn).
`spec.py` chặn khi thiếu file hoặc cảnh lạ; `build.py` bước `world` gọi `world/build_seg.py` cho từng đoạn (spine đọc lời từ `out/factory/timeline.json`
qua biến `CRUX_TIMELINE`, `spine.words_from_timeline`) và dừng nếu tổng spine ≠ độ dài các cảnh; `spec.py` chặn cảnh không liền / chồng hai đoạn.
**Ghép vào master (F-5, `world/splice.py`):** bước `splice` (sau `render`) thay đúng các khung [f0, f1) của các cảnh đoạn chiếm bằng video đoạn
(số khung đoạn ≠ tổng cảnh hoặc fps khác → dừng; khác kích thước → co giãn), rồi mã hoá lại CẢ master một lần với thông số của `render.js`
(`ENCODE_H`: CBR 17M, preset fast, bt709). Trong `mix`: lời vẫn là track lời của tập (stem voice của đoạn chỉ dùng đo mức, không cộng);
`music`/`data`/`sfx`/`room` của đoạn cộng vào stem `music`/`sonify`/`sfx`/`room` tại t0 của đoạn, nhân tỉ lệ RMS lời tập/lời đoạn; nhạc nền
của tập tắt trong khoảng đoạn (fade 0,5 s ngoài mép); `mix-raw` = tổng đúng các stem; rồi loudnorm 2 lượt như cũ.
`timeline.json`: cảnh/shot bị thay có `world: <id>`, thêm `world: [{id, scenes, t0, t1, f0, f1}]`; nhật ký khung 2D trong khoảng đoạn bị bỏ (qc
chỉ xét khung 2D còn trong master). Báo cáo `out/factory/splice.json` (đoạn, cảnh, t0/t1, khung, sha256 video/stem đoạn, picture vào/ra, stem,
mix-raw, master.wav, video). Test: `toolkit/tests/test_world_splice.py`.
Giới hạn: shot 2D của cảnh bị thay vẫn render (cache) dù không vào master.

**Trang kiểm của tập (F-7, checks-appeal A11):** bước `artefacts` ghi `out/page.json` → `work/factory/page/index.html`, MỘT file HTML tự chứa
(`world/episode_page.py`: mọi module ES — three, `core.js`, `lib3d.js`, `scene.js` của mỗi đoạn và thư viện tập — nạp từ blob: URL, JSON của
`loadJSON` và phông Inter nhúng sẵn; mở bằng `file://`, không máy chủ) cung cấp `window.CHECKS` của `checks/CONTRACT.md` §Page cho mọi đoạn `world:`:
`seek(t)` theo giờ của tập (chọn đoạn, dựng `frame(t − t0)`), `objects()` (chữ: role/hộp/cỡ/màu/nền pill/khoảng claim khớp `display` của
`claims.json`; `ILLUSTRATIVE` = role badge; nét lớp phủ = role line; vật 3D khai `userData.checks` và `O.shape({...})` = hình có role/case/year…),
`layer(text|glyph|graphics|only|notext|all)`, `freeze(t)` (giữ vị trí/hướng/fov máy quay), `?res=1080`. `core.CK.on` chỉ bật ở trang này: khung
render không đổi (MD5 trùng với core cũ khi tắt dither). Để luật trang S06 thấy "mọi tháng mua", scene.js gắn `case`/`year` lên vật dữ liệu
(`mesh.userData.checks = {role: 'series', case: '1991-01'}` hoặc `O.shape({role, world: [[x,y,z]…], case})`). Chạy tay: `python3 toolkit/factory/world/episode_page.py episodes/epNNN/episode.yaml`.
**Artefact F11 (F-8):** `audio.py` tách tiếng động tác máy quay (`whoosh_*`, `swish`, `sound` của moves) thành stem `whoosh` (cùng thang và
side-chain tuyến tính → sfx + whoosh = lớp sfx cũ; tổng stem của tập = mix-raw); `render_shots.js` ghi máy quay thật mỗi khung (`.cam.json`) →
`out/camera.json` (`world/artefacts.py`: tâm = giao tia nhìn giữa khung với mặt phẳng biểu đồ z = 0, zoom = 20 / bề rộng nhìn thấy ở đó, đơn vị thế
giới; tốc độ máy theo bề rộng khung không phụ thuộc thang này; khung ngoài đoạn thế giới đứng yên) và `out/sonify-events.json` (mỗi âm dữ liệu ở
khung nó thật sự vang sau khi dời vào khe lời, `audio-report.json data_events`).
**Banding (F-6, checks F08):** `core.CK.dither` (mặc định 2): `material.dithering` của three + dither CỐ ĐỊNH theo màn hình ±4 mã (TPDF, ô 2×2 ở
1080) ở điểm ảnh tối (luma < 72) trước khi mã hoá — mẫu đứng yên sống qua hai lần x264 (nhiễu đổi theo khung bị khung P xoá). `?dither=0` tắt.
**Shorts từ đoạn thế giới (F-9):** Short có khoảng nằm trọn trong một đoạn `world:` được DỰNG LẠI 1080×1920 từ scene.js của đoạn
(`world/shorts.py`, `render_shots.js --span a,b --orient v`): cùng máy quay, khung = cửa sổ dọc của mặt phẳng thiết kế rộng 1080/`scale` px
(`scale` của Short trong `episode.yaml`, mặc định 0,75; 3D render đúng cửa sổ bằng `setViewOffset`, không cắt ảnh 16:9); chữ của cảnh nâng lên
≥ 56 px, xuống dòng và đẩy vào vùng an toàn dọc (`qc.py SAFE['v']`), chữ nhỏ (< 48 px, nhãn trục) đã nâng mà đè chữ vẽ trước bị bỏ (`log.v.dropped`); lớp bắt buộc dọc của nhà máy: móc, ILLUSTRATIVE + "US only · history, not a
forecast" trên MỌI khung có chữ số, đối trọng của tập xoay 3 s; thẻ cuối 1,5 s của engine 2D; tiếng cắt từ master, loudnorm −14 LUFS / −1,5 dBTP.
Short vắt qua hai đoạn → đường 2D cũ. Mọi Short giờ ra 1080×1920 dù `res` của tập là 540.

| File | Việc |
|---|---|
| `lib3d.js` | Thư viện vật thể có tham số W1–W10 (nhà, chồng tiền mệnh giá cố định, xà, người không mặt, vệt, bó đường, khiên, khu phố, căn hộ, hàng thùng + séc `Crates`/`Check`) — `visual-library` §5 |
| `core.js` | Máy quay theo tư thế + động tác hữu hạn từ spine, trọng số chế độ đồ thị, lớp phủ 2D (chữ ≥ 48 px, nền mờ), nhật ký quy tắc 1 + F-2 (chữ có thứ tự vẽ `n`/`plate`; `lines` = nét moveTo/lineTo của lớp phủ, toạ độ 1920×1080; đường cong và đường 3D không ghi) + `log.cam` (máy quay thật). `CK`: trang kiểm (`on`, `mode` = lớp, `freezeCam`, `claims`), khung dọc (`view`), dither (F08); `O.shape()` khai hình dữ liệu cho trang kiểm |
| `episode_page.py` + `episode_page.js` | Trang kiểm một-file của tập (`window.CHECKS` trên mọi đoạn `world:`) + `out/page.json` |
| `artefacts.py` | `out/camera.json` (máy quay 3D → 2.5D của CONTRACT) + `out/sonify-events.json` từ sản phẩm `build_seg.py` |
| `shorts.py` | Short 9:16 dựng lại từ đoạn thế giới (cửa sổ dọc, sàn 56 px, lớp bắt buộc dọc), tiếng −14 LUFS, nhật ký khung cho `qc.py` |
| `spine.py` | Spine v2: `Anchors` ("@câu[:từ][$]"), `beats_from`, `window` (giữa hai từ khoá ± pad), `move_sounds`, `shots_for`, `check_rules` (2/3/7), `words_from_timeline` |
| `onset.py` | Đầu từ = lúc nghe được (năng lượng), không phải mốc TTS |
| `render_shots.js` + `page.html` | Render theo cảnh, cache SHA-256 (mã thư viện + cảnh + spine + dữ liệu + khoảng + độ phân giải + khung dọc), resume, lỗi trang = dừng, nhật ký 0,1 s, máy quay mỗi khung (`.cam.json`); `--span a,b` (một khoảng, chia khúc 5 s), `--orient v` (Short dọc), `--dither 0|1|2` |
| `audio.py` | Lời + nhạc theo bản đồ căng (`music_plan`) + âm dữ liệu + sfx + whoosh (tiếng máy quay, stem riêng) từ `spine.events`, `mix` {music_db, data_db}, −14 LUFS; `data_events` (giờ nốt vang) |
| `verify_seg.py` | Quy tắc 1/2/3, cắt cứng, tỉ lệ chế độ, C14 (bản 1080p), F-2 trên sản phẩm cuối |
| `sfx_labels.py` | F-2: sfx/phút, tối đa trong 10 s, sfx đè từ thường, sfx trên từ khoá (SNR lời/sfx từ stem; < 10 dB → BLOCK); hộp chữ giao nhau / đường lớp phủ (`log.lines`) cắt chữ (cả hai đọc được → BLOCK, đang mờ → WARN). Ngưỡng là hằng đầu file (tạm, A19). Chạy tay: `python3 toolkit/factory/world/sfx_labels.py <spine.json> <video.log.json> [<video>.audio]` |
| `sync_audit.py` | Đồng bộ lời/hình/âm ±0,2 s bằng ASR (faster-whisper) — chạy tay |
| `lint_comments.py` | Bắt "chú thích nuốt mã" |
| `build_seg.py` | Một lệnh: lint → spine → render → audio → mux → verify (F-2 BLOCK cũng dừng); báo giờ render thật (`<out>.build.json`) |
| `splice.py` | F-5: ghép đoạn vào master của tập — hình (thay khung, mã hoá lại một lần) + tiếng (lớp đoạn vào stem tập, `whoosh` tuỳ chọn) + `splice.json` |
| `vendor/package.json` | three 0.186.1 (`npm ci`; node_modules không commit) |

Giờ render đo được (4 lõi, SwiftShader, 3 worker, 540p): Tập 4 đoạn 69,6 s → 135,5 s; Tập 5 đoạn 34 s → 76 s (≈ 2 s máy/s phim); cache trúng → < 1 s.
