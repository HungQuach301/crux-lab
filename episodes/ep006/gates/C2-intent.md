# C2 — Ý đồ kiểm máy + kiểm mù lời (ghi TRƯỚC khi chạy; không sửa sau khi thấy kết quả)

Ngày 2026-10-08. `quality-framework.md` §4 C2, `episode.md` §2–§3.
- **(a) Máy:** `story/check_script.py` (mẫu `playbook/templates/check_script.py`, regex S10 đọc từ `checks/py/r_content.py` ở **LOCK mới nhất của `main` = d93276a4**): claim 100 %, S10 = 0, "US only", "history, not a forecast", ASR, mật độ số, M1–M6 ước ở **2,75 từ/s**, độ dài ước ở **2,52 từ/s** (`101` ≥ 495 s ≈ 1.250 từ nói, ≤ 540 s), mid-roll, khuôn tỉ lệ (THAM KHẢO ±5 điểm). Đạt hết.
- **(b) Kiểm mù lời (headless, `blind.py`):** 6 người đọc Sonnet (5 T + 1 G) + 1 người chấm; **thêm 2 người đọc model khác** (luật mỗi 3 tập, Tập 6: 1 Opus + 1 Haiku, `headless.sh --model`), cùng gói lời, cùng người chấm, **không tính vào ngưỡng** — so với 6 người Sonnet, ghi ledger, lệch đạt/trượt hoặc lệch loại khối → nêu ở G1.
  - Ngưỡng: đúng (câu hỏi + đáp án) **≥ 5/6**; câu khuyên **0/6**; mất chú ý: **một loại khối** (phương pháp / định nghĩa / số dày / nhân vật) được **≥ 2/6** nêu → WRITER mới sửa khối đó (`episode.md` §2); **không loại khối nào ≥ 4/6** (ngưỡng cổng).
  - Dừng sớm: gặp câu khuyên đầu tiên hoặc 2 sai; không dừng sớm khi đạt. Tối đa 2 vòng.
  - Dự phòng ghi trước: khối mất chú ý → rút còn 1 câu lời + thẻ V7 + mô tả (mẫu đoạn phương pháp). Vẫn trượt → giữ bản điểm cao nhất, nêu ở G1.
- **(c) Năm luật nhân vật (REVIEWER, `quality-framework.md` §7 mục 8):** nhân vật dẫn đường trước 0:45, qua phần phương pháp, câu kết của người đó; M6 ≤ 90 s; vật cụ thể có claim; câu đỉnh ≤ 15 từ (đếm); kết quay về câu hỏi nhân vật.
- **Móc:** REVIEWER chấm 3 phương án theo story §1 + M1–M6; so cặp vòng tròn chỉ khi REVIEWER không tách được. M1–M6 đo lại trên **bản đọc thật** (ElevenLabs Eric, `story/table_read.py`) trước G1; M4 ước (2,75 từ/s) so với M4 đo, nêu tên lệch.

## Vòng 3 (sau G1, phương án b) — ghi TRƯỚC khi chạy · 2026-10-08 (phiên P2)
Lệnh G1 (`gates/G1-answer.md`): WRITER MỚI thêm ≈ 90 từ chất có nguồn → **kiểm máy ĐẠT không cờ `--g1-short`** (`101` ≥ 505 s ước = ≥ 1.275 từ nói, mẫu sửa theo lessons T6-1; regex S10 ở LOCK f3089787 sau merge K4.0) → **kiểm mù lại hồi 2–3 theo ngưỡng C2**.
- **Mẫu:** toàn bộ lời v3 (`c2/sample.py` → `c2/sample-r3.txt`; người đọc cần ngữ cảnh hồi 1 để trả lời câu hỏi chính), cùng vai, cùng 6 câu hỏi, cùng rubric `c2/rubric.md` (không sửa) như vòng 2. **6 người đọc Sonnet mới** (5 T + 1 G) + 1 người chấm độc lập (`blind.py`). Không thêm người đọc model khác (luật mỗi 3 tập đã chạy ở vòng 1).
- **Ngưỡng (C2, không đổi):** đúng ≥ 5/6; khuyên 0/6; không loại khối nào ≥ 4/6. Khối mất chú ý **nằm trong hồi 2–3** (S13–S30) được một loại khối nêu ≥ 2/6 → WRITER mới sửa khối đó (vòng 4 tối đa, luật 3 vòng/lỗi). Khối ở hồi 1/kết (S01–S12, S31–S32) chép vào bảng, so với vòng 2 (phương pháp 2/6 · định nghĩa 2/6 · số dày 2/6) — đã xếp sửa bằng hình ở C3–C4, không mở vòng lời.
- **Riêng nhịp thêm mới:** nếu ≥ 2/6 nêu đúng nhịp thêm (cảnh WRITER vòng 3 thêm) là chỗ mất chú ý → nhịp đó là độn trong mắt người xem → bỏ nhịp, **dừng hỏi chủ dự án** (lệnh G1: không đủ chất mà không độn thì hỏi).
- Dừng sớm: câu khuyên đầu tiên hoặc 2 sai; không dừng sớm khi đạt.
