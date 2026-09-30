# Hiệu chuẩn bộ đo kiểm mù mới — ý đồ (ghi TRƯỚC khi chạy)

Chủ dự án duyệt 29/09/2026 (C1, câu 2). Chạy **một lần** trên logline C1; **không chấm lại C1** (C1 đã chọn C).

## Mẫu (mỗi mẫu một file tên ngẫu nhiên, mỗi agent một file)
- **Ứng viên L-A v2**, **ứng viên L-B v2** (nguyên văn trong `C1-blind.md`, vòng 2).
- **Đối chứng yếu:** logline Cổng A bản cũ (có đáp án bằng số, "we find…").
- Mỗi mẫu: 5 người đọc vai khán giả đích + 1 người đọc phổ thông = 18 agent mới.

## Câu hỏi cố định (tiếng Anh)
Vai khán giả đích:
> Open exactly one file: `<path>`. Do not open, list or search for any other file. It contains the one-line pitch (logline) of a YouTube video. Answer as this viewer: **you are an American currently paying a mortgage you signed between 2022 and 2024.** Answer in English:
> 1. In your own words: what is this video about, who is it about, and what question will it answer? (2–3 sentences)
> 2. Would you click to watch it? Choose one: Yes / Maybe / No, with one sentence on why.
> 3. Is any word or idea unclear? If so, point to it.

Người đọc phổ thông: như trên, thay câu vai bằng "Answer as an ordinary YouTube viewer."

## Tiêu chí "phân biệt được" (chỉ tính 5 người đọc vai khán giả đích)
- Đếm "Yes" mỗi mẫu. Bộ đo **phân biệt được** khi: Yes(đối chứng yếu) ≤ min(Yes(L-A), Yes(L-B)) − 2.
- Ngược lại (đối chứng yếu được "muốn xem" ngang ứng viên) → **báo chủ dự án, không tự sửa bộ đo**.
- Ghi thêm "Maybe" và "kể đúng" (tiêu chí TC1–TC3 của `C1-intent.md`) để tham khảo; không dùng để kết luận.
