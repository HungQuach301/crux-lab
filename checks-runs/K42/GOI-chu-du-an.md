# Gói chủ dự án — Phiên K lô Tập 7 (K4.2), sửa luật cũ · 11/10/2026

Phần **chỉ thêm** đã tự merge `main` (D-008 §2): kind `term-pair-weekly-replay` cho Tập 7, luật mới SH06 (A30). A29 hoãn (`checks-appeal.md`, lô K4.2). Hai mục dưới **đổi hành vi luật/cổng cũ** nên cần chủ dự án duyệt trước khi K viết và merge. Chưa có mã nào cho hai mục này trên `main`.

## Câu 1 — A28: cổng khuyên của kiểm mù theo rubric mới, mặc định
**Hiện nay** (`toolkit/blind/packets.py tally`, K4.1): cổng mặc định rubric **cũ** (mọi cờ khuyên, kể cả người đọc tự suy); khi hai rubric cho kết quả khác nhau, cổng **giữ rubric cũ** kể cả khi gọi `--advice-rubric new`. Vì vậy Tập 6 (C4) và Tập 7 (C2) đều phải dùng quyết định riêng của chủ dự án.
**Đề xuất:** mặc định `new`: câu khuyên ở mọi ngưỡng = `advice_stated` (video nêu). Khi hai rubric lệch, **cổng theo rubric mới**. `advice_inferred` và `caution_only` vẫn được báo, REVIEWER đọc câu trích. Thêm ca test mặc định mới vào `toolkit/tests/test_toolkit_v2.py`.
**Bằng chứng (C4 Tập 6, `episodes/ep006/gates/C4-answer.md`):** rubric cũ trượt 3/3 bản có lời, S29 2/3, 17/23 nhịp gốc, gần như toàn bộ do `advice_inferred` (kể cả nhịp đã qua C3). Rubric mới chỉ còn 0/3 · 0/3 · 1 nhịp (B08). Đối chứng trên hình thật: dương 3/3, âm 0/3.
**Giới hạn:** A28 muốn kiểm thêm trên C4 Tập 5, nhưng điểm C4 Tập 5 được chấm theo rubric cũ, không có cờ `advice_stated`. Muốn có số thì phải chấm lại bằng headless (ước vài USD).
- **(a) Có** — đổi mặc định, lệch thì theo rubric mới. *Khuyến nghị:* hai tập đã chạy theo cách này. Một bộ đối chứng cùng chủ đề đạt cả dương lẫn âm.
- (b) Có, nhưng chấm lại C4 Tập 5 trước khi đổi.
- (c) Không — giữ như hiện nay, mỗi tập quyết riêng.

## Câu 2 — A31: độ dài và mid-roll theo format (`deep` đã duyệt, D-012)
**Hiện nay:** F07 (CHÍNH) là 480–900 s cho mọi format, nên một tập `deep` dài hơn 15:00 sẽ trượt. S14 đếm mid-roll `lab` 2 · `101` 1 và chưa có `deep`. S15 có sàn `lab` 540 s.
**Đề xuất K (đã chỉnh từ A31):**
- F07 lấy **sàn** theo format (CHÍNH): `101` 480 · `lab` 540 · `deep` 840 s.
- Luật **mới** F13 cho **trần cứng** (CHẶN): `101` 540 · `lab` 660 · `deep` 1020 s.
- S14 cho `deep`: 2–3 mid-roll, mỗi điểm cách nhau ≥ 180 s. Điều kiện khoảng cách **chỉ áp cho `deep`**.
- S15 thêm sàn `deep` 840 s.

**Hồi tố trên báo cáo các tập trước:**
- Sàn `lab` 540 s làm Tập 4 (`lab`, 481,6 s) trượt F07; trước đây Tập 4 đạt.
- Tập 5 (`101`, 462,6 s) đã trượt từ trước và vẫn trượt.
- Tập 6 (`101`, 536,6 s), Tập 1 (591 s) và Tập 2 (586 s) đạt.
- Nếu áp khoảng cách ≥ 180 s cho `lab` thì Tập 1, 2, 4 trượt (hai mid-roll cách 131 / 159 / 169 s). Vì vậy K đề xuất chỉ áp cho `deep`.

**Phương án:**
- **(a) Có** cả bốn ý trên. *Khuyến nghị:* khớp `CHARTER.md` §1 (lab 9–11, 101 8–9, deep 14–17) và D-012 (mid-roll 2–3).
- (b) Như (a), nhưng trần để CHÍNH, không thêm luật CHẶN (giữ lý do K3: "chặn độ dài dễ dẫn tới giãn thời gian").
- (c) Chỉ thêm `deep` (F07 840–1020, S14, S15 cho `deep`). `lab`/`101` giữ 480–900.

Trả lời ngắn, ví dụ: "1a, 2a". K viết, chạy selftest và báo cáo trước/sau trên Tập 4–7, rồi merge theo câu trả lời. Phải xong trước C5 nếu Tập 7 hoặc Tập 8 là `deep`.
