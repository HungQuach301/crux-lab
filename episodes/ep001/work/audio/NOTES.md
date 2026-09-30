# Luồng A (tiếng) · C5 — ghi chú

## ĐIỂM TIẾP TỤC (đọc trước)
29/09/2026, sau khởi động lại lần 2 (agent A trước bị giết).
- Mã mix: `work/audio/src/{mix,events,takes}.py` (commit `04b4e7a`). Chạy lại: `python3 episodes/ep001/work/audio/src/events.py && python3 episodes/ep001/work/audio/src/mix.py` (tạo stem/master/tempo-map/cues/sfx-events/manifest/report; cache `work/audio/cache/*.npy` — xoá `music.npy` khi đổi `render_music`).
- Việc dở của lần tiếp tục này: (1) S14 — hai điểm quảng cáo 241,54 / 372,2 s không có ≥ 1 s ≤ −40 dBFS (nhạc phồng +3 dB và nhấn felt ở cú cắt). Sửa: nhạc (và room +8 dB) im như khoảng lặng [beat] trong khe lời cảnh của điểm quảng cáo, không nhấn felt ở hai cú cắt đó (bỏ khỏi `accents` của tempo-map), tiếng dữ liệu không đụng, lời không đụng. (2) dựng lại (nohup, log `work/audio/mix.log`), (3) kiểm manifest, (4) tự kiểm luật K3.1 trong scratch `A-audio/` (video.mp4 = animatic 720p + master, CHỈ để kiểm tiếng; P mux bản thật), (5) chạy lại `preprod/dossier_c5.py` để tension-map đo từ stem.
- Mỗi bước xong: một dòng `ledger.md`, commit `git commit -- <đường dẫn>`.
