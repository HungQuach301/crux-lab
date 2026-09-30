# Luồng A (tiếng) · C5 — ghi chú

## ĐIỂM TIẾP TỤC (đọc trước)
**Trạng thái 30/09 00:45: xong cả 4 việc** (S14 sửa + dựng lại `3bf66d2`, tension-map `fbad523`, tự kiểm dưới đây). Còn mở: xem "Việc mở".

29/09/2026, sau khởi động lại lần 2 (agent A trước bị giết).
- Mã mix: `work/audio/src/{mix,events,takes}.py` (commit `04b4e7a`). Chạy lại: `python3 episodes/ep001/work/audio/src/events.py && python3 episodes/ep001/work/audio/src/mix.py` (tạo stem/master/tempo-map/cues/sfx-events/manifest/report; cache `work/audio/cache/*.npy` — xoá `music.npy` khi đổi `render_music`).
- Việc dở của lần tiếp tục này: (1) S14 — hai điểm quảng cáo 241,54 / 372,2 s không có ≥ 1 s ≤ −40 dBFS (nhạc phồng +3 dB và nhấn felt ở cú cắt). Sửa: nhạc (và room +8 dB) im như khoảng lặng [beat] trong khe lời cảnh của điểm quảng cáo, không nhấn felt ở hai cú cắt đó (bỏ khỏi `accents` của tempo-map), tiếng dữ liệu không đụng, lời không đụng. (2) dựng lại (nohup, log `work/audio/mix.log`), (3) kiểm manifest, (4) tự kiểm luật K3.1 trong scratch `A-audio/` (video.mp4 = animatic 720p + master, CHỈ để kiểm tiếng; P mux bản thật), (5) chạy lại `preprod/dossier_c5.py` để tension-map đo từ stem.
- Mỗi bước xong: một dòng `ledger.md`, commit `git commit -- <đường dẫn>`.

## Tự kiểm C5 (30/09/2026)
Luật từ `origin/main` `fda4840` (checks LOCK `81cf3997…`, `git archive`, không sửa) chạy trên bản sao gốc tập (scratch `A-audio/root`, symlink vào `episodes/ep001`).
`out/video.mp4` **tạm** = hình animatic 720p + `master.wav` (AAC 320k) — chỉ để các luật đọc tiếng từ video chạy được; P mux bản thật rồi chạy lại A01–A06, A09, A14, S14, T1, T3 (các luật đọc master qua video).

| Luật | Cấp | Kết quả | Số đo |
|---|---|---|---|
| A01 | CHẶN | PASS | −14,0 LUFS |
| A02 | CHẶN | PASS | −1,5 dBTP (trước AAC) |
| A04 / A05 / A06 | CHẶN | PASS | |
| A14 | CHẶN | **TRƯỢT** | 124 từ khoá, thiếu 1: S18.4 "Walt's" → "Waltz" (stem lời một mình cũng "Waltz"; lỗi đồng âm của take giọng, đã ghi ở VOICE C4 v3.2) |
| A18 | CHÍNH | PASS | 1 giọng (elevenlabs, Eric, eleven_v3) |
| L1 | CHÍNH | PASS | tỉ lệ lời/dữ liệu 1–4 kHz, bách phân vị 10 = 26,9 dB; 0 từ khoá mất |
| T1 | THAM KHẢO | PASS | 266 ô, 80% nghe được trong khoảng nghỉ; dải khai 98% năng lượng stem sonify |
| T2 | THAM KHẢO | PASS | |
| T3 | THAM KHẢO | TRƯỢT | 16 khoảng lặng; 2 lối vào quá 400 ms (22,68 s: 0,57; 290,84 s: 0,49) — nền (pad) tự tụt > 3 dB trong 0,4 s trước khoảng lặng vì không có nốt mới 1,3 s trước đó, nên luật đo lối vào từ sớm hơn; sàn room đạt |
| S14 | THAM KHẢO | PASS | im 240,31–241,83 (1,52 s) và 370,97–372,35 (1,38 s) |
| A03 | THAM KHẢO | TRƯỢT | LRA 3,8 LU (ngưỡng 6–10) |
| A07 A08 A09 A12 A13 A17 R02 | | PASS | A12: 17 accent, 100% trên cú cắt, 100% có onset |
| A11 | THAM KHẢO | TRƯỢT | 0 sự kiện sfx (bảng S2 không có lớp sfx) |
| A10 | THAM KHẢO | MISSING | cần `out/camera.json` (P) |

## Việc mở
1. **A14 (CHẶN)**: "Walt's" ở S18.4 — cần chủ dự án/P2 quyết (sinh lại câu/cảnh S18, hay giải thích). A không đụng lời.
2. **T3 (tham khảo, gu G-003)**: hai lối vào chậm. Cách sửa có thể: giữ mức nền phẳng trong 0,5 s trước khoảng lặng [beat] rồi mới nhả τ 90 ms — đổi cảm giác vào khoảng lặng mà chủ dự án đã duyệt ở vòng 3 → hỏi trước khi làm.
3. A03 LRA 3,8 (tham khảo): hệ quả của lời ưu tiên (G-006) + nhạc −20 dB dưới lời; không đổi nếu không có chỉ dẫn.
