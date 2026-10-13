Bạn là WRITER MỚI của Crux (vòng sửa 2, C2 Tập 7). Không agent con, không commit. Mỗi lệnh Bash là MỘT lệnh `python3 …` (không cd, &&, ;, pipe). Chỉ sửa `episodes/ep007/story/script.md` và `episodes/ep007/story/beats.md`.

Đọc: `playbook/story.md` §3 (đoạn phương pháp = 1 câu lời + thẻ V7 + mô tả), `episodes/ep007/story/script.md` (cảnh S32, S25, S31), `episodes/ep007/story/beats.md` (nhịp của S32), `episodes/ep007/numbers.md` (đầu tệp: luật nói).

Đã sửa gì, vì sao: kiểm mù lời vòng 1 (`episodes/ep007/c2/r1/`) đúng 6/6, khuyên 0/6, nhưng **6/6 người đọc mất chú ý ở khối giới hạn/phương pháp S32** ("weekly US survey averages… strong credit", "principal and interest only: no property taxes…") — trượt ngưỡng cổng (không loại khối nào ≥ 4/6). 4/5 người đọc vai "trả thêm hay đầu tư" nói phần "đầu tư" chưa được trả lời (đúng: tập không mô hình lợi suất thị trường).

Sửa (dự phòng ghi trước ở `gates/C2-intent.md`):
1. **S32 → đúng 1–2 câu lời**, giữ nguyên văn bắt buộc "US only" và "history, not a forecast" và "doesn't say which loan to take". Toàn bộ giới hạn khác (khảo sát tuần cho người tín dụng tốt, điểm/phí; chỉ gốc + lãi, không thuế nhà/bảo hiểm/PMI/khấu trừ; mốc trước thuế và không so lợi suất thị trường; giá trị đường lui khi mất việc không đo; số của Tessa chỉ đúng ở lãi tuần này trên $320,000) chuyển lên **thẻ phương pháp V7** (beats.md, chữ trên hình ngắn) và **mô tả** (ghi "description" trong beats.md). Giới hạn duy nhất nên còn nói: một câu ngắn ở S25 (sau S25.3) hoặc S31 rằng tập **không kiểm** lợi suất đầu tư nào có vượt mốc hay không — mốc là thước để người xem tự đặt lựa chọn của mình cạnh (không khuyên, không mệnh lệnh, không số mới).
2. Không đổi cảnh khác, không thêm số mới. Độ dài vẫn phải ≥ 540 s ước (checker báo).
3. Chạy `python3 episodes/ep007/story/check_script.py episodes/ep007/story/script.md --cast Tessa,Leo` tới khi ĐẠT (tối đa 4 lượt); cập nhật khối đầu ra checker ở đầu script.md và một dòng "C2 v2 changes".
Trả về (≤ 8 dòng): ĐẠT/TRƯỢT, độ dài ước, M1–M6, S32 mới (nguyên văn), câu mới ở S25/S31 (nguyên văn).
