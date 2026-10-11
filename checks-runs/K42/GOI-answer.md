# Câu trả lời gói K4.2 (chủ dự án, 11/10/2026)

> 1a, 2b. Câu 2 lấy 2b vì trần CHẶN lab 660 s + sàn deep 840 s tạo vùng trống 11–14 phút không format nào hợp lệ; trần để CHÍNH, phần còn lại như 2a (sàn theo format, S14 deep 2–3 mid-roll cách ≥ 180 s chỉ áp deep, S15 sàn deep 840 s). Viết, selftest, báo trước/sau Tập 4–7, merge. Việc nặng (nếu có) chạy headless qua khoá Console, 0 agent con, không in khoá ra đâu.

- **Câu 1 → (a):** `packets.py tally` mặc định `--advice-rubric new`; hai rubric lệch → cổng theo rubric mới (cũ chỉ báo).
- **Câu 2 → (b):** F07 (CHÍNH, giữ cấp) theo format: `101` 480–540 · `lab` 540–660 · `deep` 840–1020 s; không thêm F13. S14 `deep` 2–3 mid-roll, cách nhau ≥ 180 s (chỉ `deep`). S15 sàn `deep` 840 s.
