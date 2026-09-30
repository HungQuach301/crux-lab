# C3 — Ý đồ kiểm mù ý nghĩa khung hình (ghi TRƯỚC khi chạy)

Ý đồ từng khung do từng designer viết và commit trước khi render: `design/c3/H1/intent.md` (`71ee5a8`), `H2/intent.md` (`9db568f`), `H3/intent.md` (`f7a62d9`). Tiêu chí chung (từ `design/c3/BRIEF.md`):

| Khung | Ý phải đọc được khi tắt tiếng (P2 chấm "đúng" khi câu trả lời có đủ) |
|---|---|
| F1 | (a) lãi giảm xuống thấp một thời gian rồi lên lại; (b) một người đã có thể tiết kiệm một khoản mỗi tháng; (c) khoản đó đã mất/không còn. |
| F2 | (a) có một khoản phí/hoá đơn; (b) tiền tiết kiệm cộng dồn theo tháng để bù; (c) một khoản thêm (nợ/dư nợ) làm điểm bù đủ trễ từ khoảng 24 sang 30 tháng. |
| F3 | (a) hai khoản vay/nhà rất khác cỡ; (b) phí gần như nhau; (c) khoản nhỏ tiết kiệm ít hơn nên cần giảm lãi nhiều hơn (hoặc bù chậm hơn nhiều). |

## Cách chạy
- AI không xem được video → mỗi khung ghép **một file PNG**: dải 6 khung theo thời gian (trên) + khung cuối lớn (dưới). Chủ dự án vẫn xem clip có chuyển động (G-011).
- 3 người đọc mới cho mỗi khung (9 khung × 3 = 27), vai khán giả đích. Mỗi người một file tên ngẫu nhiên. Đối chứng yếu: 1 khung storyboard tĩnh của bản v1 (`review-m1b/sb-03.png`, loại chủ dự án chê "khó hiểu ý nghĩa") × 3 người đọc.
- Câu hỏi cố định (tiếng Anh):
> Open exactly one file: `<path>`. Do not open, list or search for any other file. It shows a silent animation from a YouTube video: the top row is six moments in order, left to right; the large image below is the last moment. The sound is off. Answer as this viewer: you are an American currently paying a mortgage you signed between 2022 and 2024. Answer in English:
> 1. In two or three sentences: what is this animation telling you? What happens, and what is the point?
> 2. Which part, if any, did you not understand?
> 3. Which words or numbers could you not read?

## Tiêu chí qua
- Một khung **đọc đúng** khi ≥ 2/3 người đọc đủ (a)(b)(c).
- Kết quả mỗi hướng = số khung đọc đúng /3 và số lượt đúng /9. Không có ngưỡng loại hướng (chủ dự án chọn hướng); kết quả là bằng chứng cho gói.
- Nếu đối chứng yếu cũng được "đọc ra ý rõ" ≥ 2/3 → ghi "câu hỏi không phân biệt được".
