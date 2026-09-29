# K2 — hiệu chỉnh T1 (định nghĩa lại) và L1 (mới)

Chuẩn là phán đoán của chủ dự án (sổ gu G-005, G-006 trên nhánh `ep001`; chỉ dẫn K2 vòng 2). Mọi báo cáo ở đây chạy dưới khoá ghi trong trường `lock`.

| Gốc | Nguồn | Phán đoán của chủ dự án | T1 (≥ 0,60) | L1 (≥ 20 dB) |
|---|---|---|---|---|
| **Bài D vòng 3** | master `6531f6c8…` + stem M3 (`crux-spike-opus55`) | "chưa có tiếng dữ liệu" → **T1 phải trượt** | **FAIL**: 39/355 = 0,11 (dải 1,5–8 kHz); mở ra 40 Hz–16 kHz: 0,16 | MISSING (không có stem `sonify`) — xem `../D-r3-6531f6c8/K2/` |
| **m0 gốc (0 dB)** | stem `sonify` của `m0-sample` hạ 10 dB | "vẫn bị lấn" → **L1 phải trượt** | PASS: 10/13 (0,77) | **FAIL**: −7,9 dB |
| **S2** (minimal) | `review-m1/sonify-S2.mp4`; dải theo cue sheet M1b: 60–270 Hz + 4,5–7 kHz | chọn; "nghe thấy", "không lấn lời" → **phải đạt cả hai** | **PASS**: 10/13 (0,77); dải khai chứa 94,6% năng lượng | **PASS**: 26,9 dB; 0 từ khoá mất |
| S1 (breath) | `review-m1/sonify-S1.mp4`, 125–500 Hz | tham khảo | PASS: 0,77 | PASS: 22,6 dB |
| S3 (mallet) | `review-m1/sonify-S3.mp4`, 125–1000 Hz | tham khảo | PASS: 0,85 | FAIL: 16,1 dB |
| m0 (+10 dB) | stem thật của `m0-sample` | "vẫn bị tiếng dữ liệu lấn" | PASS: 0,92 | FAIL: −17,9 dB |
| m0d | lớp tách từ `m0-sample/work/preview.mp4` | kiểm cách tách | PASS: 0,92 (giống m0) | FAIL: −15,3 dB (lệch 2,7 dB so với m0) |

## Cách dựng gốc hiệu chỉnh (`mkroots.py`; `E` = bản checkout nhánh `ep001`)

- Bộ duyệt M1 chỉ có bản mix mp4 cho S1–S3 (AAC 256 kbps; cùng lời, nhạc, hiệu ứng như m0; chỉ lớp tiếng dữ liệu khác). Lớp tiếng dữ liệu = mix / g − (voice + music + sfx + whoosh + room của m0), g bình phương nhỏ nhất (1,134). Kiểm cách tách trên m0, nơi có stem `sonify` thật (gốc `m0d`): T1 giống hệt, L1 lệch 2,7 dB. Nhiễu AAC cộng vào lớp tách ra, nên L1 của S1–S3 là cận dưới (thận trọng).
- **m0 gốc (0 dB)**: bản đã commit là bản +10 dB (`SONIFY_GAIN_DB=10` trong README của mẫu); gốc `m0-0dB` = stem `sonify` × 10^(−10/20), master = tổng stem (AAC 320k) ghép với hình của bản xem trước.
- Master 25 MB của m0 không được commit; gốc `m0` dùng `work/preview.mp4` làm `out/video.mp4` chỉ cho phép kiểm "stem ~ master" của T1.
- Sự kiện: `out/sonify-events.json` và `out/checks/page.json` của `m0-sample`.
- **Dải tần** (`cal-bands.json`): S2 theo cue sheet M1b (`ep001` @ `bbc28fb`: nhịp trầm MIDI 36–60, tick lọc 4,5–7 kHz). S1, S3, m0: không có cue sheet cho dải, phiên kiểm lấy dải bội tám chứa ≥ 80% năng lượng lớp tách ra.

## Nhận xét

- Ba điểm bắt buộc đều đúng: bài D trượt T1 (xa ngưỡng, kể cả khi mở dải); m0 gốc trượt L1; S2 đạt cả T1 và L1.
- Ngưỡng T1 hạ từ 0,75 xuống 0,60: với dải đúng cue sheet S2 còn 0,77 (sát 0,75); D ở 0,11. Ngưỡng L1 giữ 20 dB (không cần nâng).
- m0 (gốc và +10 dB) đạt T1 nhưng trượt L1: T1 một mình không bắt được "lấn lời", nên cần L1.
- Ngưỡng là **tạm**; hiệu chỉnh lại sau Tập 1 bằng H8.
