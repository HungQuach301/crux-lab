# REVIEWER — ý đồ kiểm mù C4 Tập 7 (trước khi chạy lượt đọc nào)

Vai: REVIEWER (`playbook/quality-framework.md` §7). Chỉ đọc, không sửa tệp. Không in hay ghi khoá API.
Đọc: `episodes/ep007/gates/C4-intent.md`, `episodes/ep007/c4/blind_c4.py`, `episodes/ep007/gates/C3.md` §2–§3 + "Anh chọn", `episodes/ep007/gates/C3-answer.md`, `episodes/ep007/gates/C3-root-intent.md`, `episodes/ep007/c2/rubric-r3.md`, `episodes/ep007/story/beats.md` (cột loại + muted read), `toolkit/blind/packets.py` (packet, tally), mẫu Tập 6 `episodes/ep006/gates/C4-intent.md` + `episodes/ep006/gates/REVIEW-C4-intent.md`.

Soát:
1. Ý đồ có đo đúng ba chốt của C3-answer (câu 1 S21 lớp trả thêm thấy bằng hình + kiểm mù lại; câu 2 S23–S24 `advice_stated` = 0; câu 5 S25 không "phải vượt / guaranteed") không; ngưỡng có ghi trước rõ, không mơ hồ; có lỗ nào cho phép "đạt" mà ý chưa đọc ra.
2. Mã `blind_c4.py` làm đúng ý đồ: mẫu (dải/tấm/lời như người xem nghe), mù (không lộ tên dự án, đáp án), cờ phụ `extra_layer_seen`, `must_beat_or_guaranteed` đến được người chấm và được đếm (kể cả ở nhánh ảnh `root` — tally ảnh của packets.py có đếm cờ phụ không?), gộp thận trọng.
3. Rubric khuyên MỚI dùng đúng ranh giới của Tập 7 (c2/rubric-r3.md), có gì lệch.

Trả về `episodes/ep007/gates/REVIEW-C4-intent.md` (≤ 30 dòng — bạn chỉ có công cụ đọc: in toàn văn tệp đó trong câu trả lời cuối, phiên chính ghi): ĐẠT / ĐẠT có sửa / TRƯỢT; mỗi mục CHẶN / CHÍNH / PHỤ một dòng: chỗ, lỗi, sửa đề xuất.
