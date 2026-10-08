# C2 — Ý đồ kiểm máy + kiểm mù lời (ghi TRƯỚC khi chạy; không sửa sau khi thấy kết quả)

Ngày 2026-10-08. `quality-framework.md` §4 C2, `episode.md` §2–§3.
- **(a) Máy:** `story/check_script.py` (mẫu `playbook/templates/check_script.py`, regex S10 đọc từ `checks/py/r_content.py` ở **LOCK mới nhất của `main` = d93276a4**): claim 100 %, S10 = 0, "US only", "history, not a forecast", ASR, mật độ số, M1–M6 ước ở **2,75 từ/s**, độ dài ước ở **2,52 từ/s** (`101` ≥ 495 s ≈ 1.250 từ nói, ≤ 540 s), mid-roll, khuôn tỉ lệ (THAM KHẢO ±5 điểm). Đạt hết.
- **(b) Kiểm mù lời (headless, `blind.py`):** 6 người đọc Sonnet (5 T + 1 G) + 1 người chấm; **thêm 2 người đọc model khác** (luật mỗi 3 tập, Tập 6: 1 Opus + 1 Haiku, `headless.sh --model`), cùng gói lời, cùng người chấm, **không tính vào ngưỡng** — so với 6 người Sonnet, ghi ledger, lệch đạt/trượt hoặc lệch loại khối → nêu ở G1.
  - Ngưỡng: đúng (câu hỏi + đáp án) **≥ 5/6**; câu khuyên **0/6**; mất chú ý: **một loại khối** (phương pháp / định nghĩa / số dày / nhân vật) được **≥ 2/6** nêu → WRITER mới sửa khối đó (`episode.md` §2); **không loại khối nào ≥ 4/6** (ngưỡng cổng).
  - Dừng sớm: gặp câu khuyên đầu tiên hoặc 2 sai; không dừng sớm khi đạt. Tối đa 2 vòng.
  - Dự phòng ghi trước: khối mất chú ý → rút còn 1 câu lời + thẻ V7 + mô tả (mẫu đoạn phương pháp). Vẫn trượt → giữ bản điểm cao nhất, nêu ở G1.
- **(c) Năm luật nhân vật (REVIEWER, `quality-framework.md` §7 mục 8):** nhân vật dẫn đường trước 0:45, qua phần phương pháp, câu kết của người đó; M6 ≤ 90 s; vật cụ thể có claim; câu đỉnh ≤ 15 từ (đếm); kết quay về câu hỏi nhân vật.
- **Móc:** REVIEWER chấm 3 phương án theo story §1 + M1–M6; so cặp vòng tròn chỉ khi REVIEWER không tách được. M1–M6 đo lại trên **bản đọc thật** (ElevenLabs Eric, `story/table_read.py`) trước G1; M4 ước (2,75 từ/s) so với M4 đo, nêu tên lệch.
