Bạn là REVIEWER độc lập của Crux (Opus). Soát kịch bản C2 Tập 7 TRƯỚC G1. Chỉ đọc, không sửa tệp. Không agent con. Mỗi lệnh Bash là MỘT lệnh (không &&, ;, pipe).

Đọc: `CHARTER.md` §4 (gen được bảo vệ) · `playbook/quality-framework.md` §7 (checklist REVIEWER, mục 1–2, 3, 8, 10) · `playbook/story.md` · `playbook/episode.md` §3 (mục 9–12) · `episodes/ep007/numbers.md` · `topics-r2/machine/debt-1/claim-risk.md` · `episodes/ep007/story/script.md` · `episodes/ep007/story/beats.md` · `episodes/ep007/story/hooks.md` · `episodes/ep007/gates/C2-intent.md` · `episodes/ep007/gates/C2-blind.md` · `market/topics/q13-15-vs-30-mortgage.md`.
Có thể chạy: `python3 episodes/ep007/story/check_script.py episodes/ep007/story/script.md --cast Tessa,Leo`.

Soát:
1. Claim-risk: mọi số trong lời và chữ trên hình có claim ĐÚNG đối tượng (cùng tuần, cùng thời kỳ); không câu nào đọc như khuyên ("monthly beats yearly" có thành mệnh lệnh không?), không dự báo; câu "the bar … any other use of that dollar has to clear it to come out ahead" có overclaim không (trước thuế, không rủi ro, thanh khoản)?; "history, not a forecast", "US only", ILLUSTRATIVE.
2. Năm luật nhân vật (§7 mục 8): đếm từ câu `{peak}`; câu kết là của Tessa và trả lời câu hỏi cold open; M6.
3. Hồ sơ cầu (§7 mục 10): đếm câu hỏi khán giả trả lời (câu → cảnh), điểm yếu đối thủ, video neo (§3.12).
4. Kiểm mù C2: ý đồ có bị sửa sau kết quả không; kết luận "cờ khuyên vòng 2 là mơ hồ rubric" có đứng vững không (so câu 6 vòng 1 `episodes/ep007/c2/r1/*.json` với vòng 2 `c2/r2/*.json` và `scores.json` hai vòng).
5. Chấm 3 móc HA/HB/HC theo story §1 + M1–M6, mỗi cái 1 dòng lý do, xếp hạng; HB đang dùng.
6. Lỗi văn: câu mơ hồ (ví dụ S30.1 "And it was bigger"), câu dài ở đỉnh, chỗ số dày (S11–S18) nên chuyển lên hình.
Trả về: **ĐẠT / ĐẠT có sửa / TRƯỢT**; danh sách CHẶN / CHÍNH / PHỤ, mỗi dòng: cảnh, vấn đề, sửa đề xuất (nguyên văn câu mới nếu là lời). ≤ 40 dòng.
