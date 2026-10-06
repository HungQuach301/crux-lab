# K3.8 — Tập 3 (main @ a291ef7) chạy đủ bộ: khoá cũ `a20c6878…` (tuần tự) so với khoá K3.8 (song song 4 tiến trình)

**Bản đo:** bản sao `git archive origin/main` + video giao YouTube `ep003-youtube.mp4` (SHA `1274f9f6…`, ghép từ nhánh `ep003-delivery`), dữ liệu FRED ghim (`fetch.py --verify`), `design/c3/work/data.js` dựng lại. Không có stem (không commit) → 13 luật cần stem MISSING ở cả hai lần, như `moc-b/SPEED.md`. Baseline REG: `review-c5/checks-run5/report.json`. Máy 4 lõi, 15 GB.

## Thời gian
| | Khoá cũ (tuần tự) | Khoá K3.8 (`K_JOBS=4`) | Chạy lại, không đổi gì (cache cảnh) |
|---|---|---|---|
| Bộ lấy mẫu trang | 3.347 s (55,8 phút) | 2.315 s (38,6 phút) | ≈ 2 s (11/11 cảnh trúng cache; đo trên S09–S11: 355 s → 2 s) |
| Cả bộ | **3.814 s (63,6 phút)** | **2.776 s (46,3 phút)** | ≈ phần Python (ASR đã cache) |

- Lần khoá cũ chạy song song với thử nghiệm nhỏ (S09–S11) trong ~15 phút đầu, nên con số "trước" hơi cao; số sạch của Mốc B: 56,5 phút.
- Song song chỉ nhanh **1,45×** (ước A3: 3×): mỗi tiến trình là Chromium + 2 ffmpeg, máy 4 lõi đã bận ~3 lõi khi tuần tự; cảnh dài nhất (S04, 72 s) đặt sàn. Lợi lớn là **chạy lại**: cảnh không đổi dùng cache.

## Kết quả từng luật
- `page.json`: **trùng từng số** với bản tuần tự (mọi trường cũ: luật trang, textTrack, claim, chartEvents, điểm ảnh, ví dụ); khác duy nhất là hai trường mới `rules.S17` và `motionTrack`; tập tài nguyên đã nạp (F12) trùng.
- `report.json`: 82 luật cũ — **mọi số đo và trạng thái trùng**, fingerprint trùng, trừ 3 luật đổi định nghĩa có chủ ý:
  - **S05** (fingerprint đổi: thêm so tên / danh sách / null cho kind mới) — PASS → PASS, số như cũ.
  - **S14** (A4: số điểm chèn theo `format`, khoảng 120 s) — FAIL → FAIL (Tập 3 khai 0 điểm chèn ở `adbreaks.json`).
  - **S15** (A2/A4: bỏ trần cold open, sàn tổng lab 540 s) — FAIL → FAIL; số liệu khác: không còn "cold open s", tổng 572 s nay **đạt** sàn 540 s; vẫn trượt vì thứ tự hồi (Tập 3 không có `ident`).
- Luật mới: S17 PASS (Tập 3 không có claim `conditional`), S18 MISSING (THAM KHẢO: `script.json` Tập 3 chưa gắn vai hook/promise), SH01–SH05 PASS ("hợp đồng trước D-006, không có Short").
- Kết luận tập: TRƯỢT → TRƯỢT, cùng lý do (13 luật cần stem MISSING; REG 2 hồi quy do MISSING). Không luật CHẶN nào đổi kết quả.

## A7 — hiệu chuẩn "đứng hình khi có lời" (chưa thành luật)
Lời (ASR master, 473,5 s) nằm trong đoạn ≥ 3 s không đối tượng nào đổi hộp ≥ 1 px / độ mờ ≥ 0,01 (`motionTrack`): **405,6 s**; cảnh S04: **56,0 s** (qc nhà máy, cả khung: 66,8 s). Số cả tập cao vì `objects()` cho hộp trên mặt phẳng biểu đồ, không tính chuyển động máy (`camera.json`): phép đo phải cộng chuyển động máy trước khi đặt ngưỡng, rồi hiệu chuẩn trên Tập 1–2.
