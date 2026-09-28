# Tập 1 — gói duyệt M1b (tóm tắt 1 trang)

**Câu hỏi:** Ở mức chênh lãi suất nào thì tái cấp vốn hoàn lại được chi phí đóng hồ sơ? *(US only; history, not a forecast)*
**Độ dài dự kiến:** 10:29. Đọc thử liền mạch: 10:00. Cold open: 14.7 s. Câu móc lại: 0:30–0:42.

**Cold open (G-007): một người, một khoảnh khắc.**
Tháng 10/2023, Maya vay $375,000 với lãi 7.62%. Tuần này lãi trung bình 30 năm là 7.03%. Bên cho vay chào tái cấp vốn với phí $5,124. Tiền đó bao giờ mới quay về?

**Luận điểm (sửa phương pháp):** phần lớn máy tính chia phí cho số tiền trả hằng tháng giảm được, và ra **24 tháng**. Nhưng khoản vay mới bắt đầu lại 30 năm; khi tính cả dư nợ còn lại, Maya hoà vốn sau **30 tháng**. Nếu lãi chỉ giảm 0.25 điểm, cách chia hứa 38 tháng, còn tính cả dư nợ thì không bao giờ hoà vốn. Bảng so sánh: `break-even-methods.md`.

**Ba nhân vật (G-008; ILLUSTRATIVE, số liệu là trung vị HMDA 2025 theo quy mô khoản vay):**

| | Khoản vay | Phí | Giảm mỗi tháng | Hoà vốn (có dư nợ) | Bán sau 3 năm | Bán sau 7 năm | Cần giảm để hoà vốn trong 36 tháng |
|---|---|---|---|---|---|---|---|
| Dan | $115,000 | $3,667 | $68 | 75 tháng | lỗ $1,777 | lãi $386 | 1.12 điểm |
| Maya | $375,000 | $5,124 | $221 | 30 tháng | lãi $1,039 | lãi $8,093 | 0.5 điểm |
| Priya | $1,005,000 | $5,034 | $593 | 11 tháng | lãi $11,482 | lãi $30,387 | 0.2 điểm |

| Hồi | Câu hỏi | Bước ngoặt | Trả lời |
|---|---|---|---|
| 1 (0:17) | Hoá đơn của Maya có bất thường không? | Hoá đơn gần như không lớn lên theo khoản vay: Dan chịu 3.4% số tiền vay, Priya 0.5% | Máy tính thông thường: $5,124 ÷ $221 = 24 tháng. "Or has it?" |
| 2 (2:57) | Phép chia đó bỏ sót gì? | Khoản vay mới bắt đầu lại 30 năm; sau 24 tháng Maya nợ nhiều hơn $1,133 | 24 → 30 tháng; Dan lỗ nếu bán sau 3 năm; Priya hoà vốn sau 11 tháng |
| 3 (5:37) | Trong 13 đợt giảm thật từ 1971 thì sao? | 3 đợt: lãi giảm tiếp 1 điểm trước khi lần đầu hoà vốn; các khoản vay trong lịch sử còn mới nên hai cách gần như trùng | Trả lời vòng mở: Maya cần 0.5 điểm, Dan 1.12, Priya 0.2; hôm nay giảm 0.59 điểm, tức Maya lãi nếu giữ nhà quá 30 tháng |

**Giọng (theo hồi, wpm):** cold-open 154.5, act1 155.8, act2 153.6, act3 158.3, method 151.1, outro 157.2. Chi tiết: `../script/table-read-notes.md`.
**Âm thanh theo dữ liệu:** S2 (chủ dự án chọn, không lấn lời), đã có trong animatic.

**Trong gói:** `summary.md` · `animatic-0000-0080.mp4` (0:00–1:20: cold open và câu móc lại, có giọng và tiếng S2; hình là storyboard) · `table-read-full.m4a` · `break-even-methods.md` · `sb-01…04.png`
