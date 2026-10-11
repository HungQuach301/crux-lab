# C4 — trả lời của chủ dự án (Tập 6) · 2026-10-09 (phiên P3b)

Câu hỏi: rubric khuyên của cổng C4 (gói trong chat P3b; `gates/C4-blind.md`, `gates/C4-root.md`). Nguyên văn câu 1 của lệnh chốt an toàn:

> Câu rubric C4 (thay a/b/c): cổng khuyên Tập 6 dùng rubric MỚI — điều kiện qua = advice_stated 0 (cả tập, S29, cổng gốc); advice_inferred và caution_only chỉ báo, REVIEWER đọc từng câu trích; rubric cũ chạy song song để báo. Lý do: đối chứng hình thật phân biệt đúng (dương 3/3, âm 0/3), rubric cũ trượt cả nhịp đã qua C3. Ghi gates/C4-answer.md, taste-ledger, checks-appeal.md (đề xuất lô K đổi cổng mặc định). CHƯA sửa hình.

| Mục | Quyết định |
|---|---|
| Cổng khuyên Tập 6 | **rubric mới**: qua khi `advice_stated` = 0 ở bản có lời cả tập, S29 và cổng gốc (`packets.py tally --advice-rubric new`; bản có lời đếm cột "advice_stated (mới)") |
| `advice_inferred`, `caution_only` | chỉ báo; REVIEWER đọc từng câu trích |
| Rubric cũ | chạy song song, chỉ báo |
| Áp vào kết quả đã có | bản có lời cả tập 0/3 · S29 0/3 → **ĐẠT** (chốt C3 câu 1, câu 3 xong). Cổng gốc vòng 0: `advice_stated` chỉ **B08** (1 người chấm) → B08 vào danh sách đọc lại cùng nhịp nghĩa 0,5 (B01, B03, B15, B32) |
| Lệnh kèm | đóng phiên ngay (hạn mức tuần ≈ 6 %): không agent mới, không kiểm mù, không vòng sửa |
