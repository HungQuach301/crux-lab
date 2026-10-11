# C2 — Ý đồ kiểm máy + kiểm mù lời (ghi TRƯỚC khi chạy; không sửa sau khi thấy kết quả)

Ngày 2026-10-11. `quality-framework.md` §4 C2, `episode.md` §1b.4, §2–§3. Mọi lượt headless chạy bằng **khoá Console** (câu trả lời tổng kết Tập 6 1g), 0 agent con.
- **(a) Máy:** `story/check_script.py` (mẫu `playbook/templates/check_script.py` + khuôn `lab`; regex S10 đọc từ `checks/py/r_content.py` ở **LOCK 4d688acd** của `main`): claim 100 %, S10 = 0, "US only", "history, not a forecast", ASR, mật độ số, M1–M6 ước ở **2,66 từ/s**, độ dài ước ở **2,40 từ/s** (`lab` ≥ 540 s, ≤ 660 s; đích chủ dự án ≈ 11 phút), 2 mid-roll, khuôn tỉ lệ `lab` (THAM KHẢO ±5 điểm). Đạt hết.
- **(b) Kiểm mù lời (headless, `blind.py`):** 6 người đọc Sonnet (5 T + 1 G) + 1 người chấm độc lập. Tập 7 không phải tập "model khác" (Tập 6, 9, 12…).
  - **Vai T = người hỏi câu hỏi trọng số cao nhất** của hồ sơ cầu (câu 1: trả thêm gốc hay đầu tư phần tiền thừa), nhập vai hoàn cảnh điển hình 2 (người mua ở đô thị đắt đỏ, khoản trả lớn) — `episode.md` §1b.4; thêm câu hỏi cố định: *"Did the video answer the question you came with? Which part?"*.
  - Ngưỡng: đúng (câu hỏi + đáp án) **≥ 5/6**; câu khuyên **0/6**; mất chú ý: **một loại khối** (phương pháp / định nghĩa / số dày / nhân vật) được **≥ 2/6** nêu → WRITER mới sửa khối đó; **không loại khối nào ≥ 4/6** (ngưỡng cổng). Câu "trả lời câu hỏi mang tới" ≥ 4/5 T có (báo, không chặn).
  - Dừng sớm: gặp câu khuyên đầu tiên hoặc 2 sai; không dừng sớm khi đạt. Tối đa 2 vòng.
  - Dự phòng ghi trước: khối mất chú ý → rút còn 1 câu lời + nhãn hình/thẻ V7 + mô tả (mẫu đoạn phương pháp). Vẫn trượt → giữ bản điểm cao nhất, nêu ở G1.
- **(c) Năm luật nhân vật + móc (REVIEWER headless, `quality-framework.md` §7):** nhân vật dẫn đường trước 0:45, qua phần phương pháp, câu kết của người đó; M6 ≤ 90 s; vật cụ thể có claim; câu đỉnh ≤ 15 từ; kết quay về câu hỏi nhân vật; REVIEWER chấm 3 phương án móc theo story §1 + M1–M6, so cặp chỉ khi REVIEWER không tách được.
- **(d) Bản đọc thử (ElevenLabs Eric) trước G1:** chỉ cold open ≤ 60 s (clip G1) để đo M1–M5 thật — **EL ≤ 1.000 ký tự** cho bước này; cả tập không sinh trước G1 (hạn mức EL chưa đọc được, ledger).
