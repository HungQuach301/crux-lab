# toolkit/factory — nhà máy dựng (Mốc B)

Một lệnh: `bash toolkit/build.sh episodes/epNNN/episode.yaml [--workers 4] [--fmt jpeg|rgba] [--no-cache]`

| File | Việc |
|---|---|
| `spec.py` | Kiểm `episode.yaml` (format lab/101, mid-roll, scope excerpt, claim tồn tại, custom_symbols ≤ 2 → hỏi, Shorts 2–3) trước mọi gọi API |
| `voice.py` | ElevenLabs `with-timestamps` mỗi cảnh một lần, cache SHA-256 (lời nói + voice + model + seed + settings), ký tự → mốc từ |
| `build.py` | spec → giọng → giải "@câu[:từ][$][+s]" → `timeline.json` + `captions.srt` (≤ 2×42 ký tự, 1–7 s) → render đoạn đổi → trộn + loudnorm 2 lượt → master → 3 phần 720p → Shorts → qc |
| `render.js` + `page.html` | Playwright, mỗi worker một trang; khung trung gian JPEG q 0,95 (hoặc RGBA để đo); mỗi đoạn một file H.264 ghép bằng concat copy; log engine mỗi 6 khung |
| `lib/engine.js`, `lib/templates.js` | Engine canvas (sàn chữ, tương phản, vùng an toàn, va chạm, nhãn ILLUSTRATIVE/history, đẩy máy) và 10 mẫu |
| `qc.py` | Luật làm việc của bên dựng (không thay `checks/`) → `out/factory/qc.md` |
| `excerpt_checks.py` | Chạy các luật `checks/` không cần trang trên đoạn trích (kiểm LOCK trước) |

File nặng (video, cache đoạn, giọng) ở `episodes/epNNN/work/factory/` (không commit); báo cáo ở `episodes/epNNN/out/factory/`.
Đoạn render được cache theo băm (đặc tả shot + mốc đã giải + mã engine/mẫu/trang/render + claims/tokens/dữ liệu + khoảng khung).
Nhạc nền (`audio.music`) có đường trộn ducking nhưng **chưa chạy thử** (demo S04 chỉ có lời).
