# Tập 1 — gói duyệt M1 (tóm tắt 1 trang)

**Câu hỏi:** Ở mức chênh lãi suất nào thì tái cấp vốn hoàn lại được chi phí đóng hồ sơ? *(US only; history, not a forecast)*
**Độ dài dự kiến:** 10:39 (đọc thử liền mạch 10:09). Cold open 14.7 s · câu móc lại 0:30–0:43.

**Đáp án của phim** (khoản tái cấp vốn trung vị HMDA 2025: dư nợ $375,000, chi phí đóng $5,124, lãi cũ 7.62% = trung bình October 2023):
cắt 0.25 điểm → hoà vốn sau 80 tháng · 0.5 → 41 tháng · 1 → 21 tháng · 2 → 11 tháng.
Muốn hoà vốn trong 36 tháng (ILLUSTRATIVE) cần cắt **0.56 điểm**; khoản dưới $150,000 cần 1.32, khoản từ $750,000 chỉ cần 0.2.

| Hồi | Câu hỏi | Bước ngoặt | Trả lời (cái giá bằng đô la và tháng) |
|---|---|---|---|
| 1 (0:17) | Tái cấp vốn tốn bao nhiêu? | Chi phí gần như không tăng theo quy mô khoản vay: 3.4% với khoản dưới $150,000, 0.5% với khoản từ $750,000 | Trung vị $5,124 (IQR $3,443–$8,270); hoà vốn = chi phí ÷ số tiền trả tháng giảm được |
| 2 (3:22) | Lãi phải giảm bao nhiêu? | Đường cong dốc đứng dưới 0.5 điểm; quy mô khoản vay đổi ngưỡng | Ngưỡng phụ thuộc quy mô khoản vay và thời gian giữ; 36/60/84 tháng → 0.56/0.33/0.24 điểm |
| 3 (6:08) | Trong các đợt giảm thật thì sao? | 5/13 đợt: lãi giảm thêm một điểm trước khi lần tái cấp vốn đầu kịp hoà vốn | Cắt 1 điểm: hoà vốn 10–21 tháng qua cả 13 đợt kể từ 1971 (mọi trường hợp đều hiện). Trả lời vòng mở, rồi nêu giới hạn |

**Dữ liệu:**
- FRED `MORTGAGE30US` (Freddie Mac PMMS): chỉ hiển thị kèm ghi nguồn, **không công bố lại file**; mô tả video trỏ link nguồn gốc. Đối chiếu với Optimal Blue: lệch tối đa 0,38 pp.
- HMDA 2018–2025: 8 năm, đọc theo luồng; file thô không lưu (SHA-256 + URL trong `data/hmda-sources.json`). Lọc: đã giải ngân, mục đích 31/32, lien 1, kỳ hạn 360 tháng.

**Cần chủ dự án:**
1. Nghe `animatic-0000-0120.mp4` (cold open + câu móc lại, hình là storyboard) và `table-read-full.m4a`. Danh sách chỗ sửa: `script/table-read-notes.md`.
2. Điều khoản dữ liệu HMDA chưa trích được câu nào (trang điều khoản ở consumerfinance.gov, host bị chặn): cần trích trước khi phát hành (DX-H4).
3. Vài luật khoá gắn với bài D (S01, S03–S06, V04, V09) cần phiên kiểm làm hợp đồng cho mô hình của tập này (`contract.json`).
4. **Chọn bảng âm cho tiếng dữ liệu** (sổ gu G-005, G-006): nghe mù `sonify-S1.mp4`, `sonify-S2.mp4`, `sonify-S3.mp4` trên loa điện thoại. Cùng mẫu 10 giây, cùng độ to, cùng luật (ép xuống khi có lời, bỏ 1–4 kHz khi có lời, đặt vào khe giữa âm tiết, giữ ánh xạ cao độ). Giải mã ở `key.json`; mở sau khi chọn. Mục âm sắc trong cue sheet để trống tới khi chọn. Xung đột với T1 đã ghi cho Phiên K: `../checks-notes.md`.

**Trong gói:** `summary.md` · `animatic-0000-0120.mp4` · `table-read-full.m4a` · `sonify-S1/S2/S3.mp4` · `sonify-metrics.json` · storyboard `sb-01.png` … `sb-05.png` (bản gốc: `../preprod/storyboard/`)
