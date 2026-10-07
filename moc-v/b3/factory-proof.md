# Áp thiết kế vào nhà máy — bằng chứng tái lập (06/10/2026)

Clip so sánh là v3l/E5h — bản sửa khách quan (a)/(b) sau khi chủ dự án chấm L3 trên v3k/E5g; v3l/E5h chưa được chấm L3.

`moc-v/world/*`, `moc-v/proto/audio.py`, `moc-v/proto/sync_audit.py` chuyển (git mv) vào `toolkit/factory/world/`; phần chung của hai
`spine.py` rút thành `toolkit/factory/world/spine.py` (spine v2); thêm `build_seg.py` (một lệnh), luật `world` trong `spec.py`, bước `world` trong `build.py`.
Đường dẫn cũ `moc-v/world/…` trong các báo cáo trước 06/10 là lịch sử.

| Kiểm | Kết quả |
|---|---|
| `spine.json` Tập 4, Tập 5 sinh lại qua spine v2 | **trùng byte** với bản đã duyệt |
| 12 ảnh tĩnh (6 mốc × 2 đoạn) render qua đường nhà máy | **trùng byte** với ảnh render trước khi chuyển (render tất định: hai lần chạy cũ cũng trùng) |
| `audio.py` từ vị trí mới, `mix.wav` hai đoạn | **trùng byte** |
| `build_seg.py moc-v/seg/ep004 --res 540` → so `review/proof-a-ep004-v3l-540p.mp4` | hình MD5 `2e01c052…` = ; tiếng MD5 `366d4aee…` = |
| `build_seg.py moc-v/seg/ep005 --res 540` → so `review/proof-b-ep005-e5h-540p.mp4` | hình MD5 `1764ffc2…` = ; tiếng MD5 `45fe9a38…` = |
| verify (quy tắc 1/2/3, cắt cứng, 5 s đầu thế giới) | cả hai đoạn: 0 · 0 · 0 · 0 · đúng |
| Chạy lại (cache) | 5/5 cảnh trúng, render 0,9 s |
| Selftest `toolkit/tests/test_world.py` | 7/7 OK; mọi test toolkit khác OK; `spec.py` Tập 4: OK |

Giờ render thật (máy 4 lõi, SwiftShader, 3 worker, 540p): Tập 4 69,6 s phim → 135,5 s; Tập 5 34 s → 76,0 s; âm 17,9 s / 8,7 s.
(MD5 = băm luồng đã giải mã: `ffmpeg -i <f> -map 0:v|0:a -f md5 -`.)

Chưa làm (BACKLOG F-5): ghép đoạn thế giới vào master của một tập — làm cùng đoạn thế giới đầu tiên của Tập 5.
