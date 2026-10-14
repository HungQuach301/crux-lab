# Đọc mù tắt tiếng: clip v3 (P3), 2 "người" × 2 lượt (14/10/2026). CHẨN ĐOÁN, không phải cổng

**Cách chạy:** `v3/blind/run.py` gọi `toolkit/blind/headless.sh`.
- Mỗi lượt là một phiên headless mới, chạy từ thư mục trống, **chỉ có công cụ Read**, 0 agent con.
- Khoá Console truyền qua biến môi trường của tiến trình con. Không in, không ghi ra tệp (đã kiểm `raw/`).
- **Hai "người" là hai mô hình đọc khác nhau, không phải người thật:**
  - **A** = sonnet;
  - **B** = opus.
- **Vật liệu (tắt tiếng, không lời, không kịch bản):**
  - tờ khung 19 ô đánh số: `blind/material/to-khung.png`;
  - 5 dải × 6 khung: `blind/material/strip-*.png`.
- **Câu hỏi:** Q1–Q8 theo `blind/PHIEU-v2.md` (`v3/blind/prompt.tmpl`).
- **Lời đáp nguyên văn:** `v3/blind/raw/{A,B}-{1,2}.json`.

**Chi:** A-1 0,090 $ · A-2 0,079 $ · B-1 0,206 $ · B-2 0,174 $. **Tổng 0,549 $** (`raw/cost.json`).

## Điểm theo đáp án PHIEU-v2
Phiên tự chấm, không mù với đáp án, nên **chỉ mang tính chẩn đoán**.

| | Q1 (0–2) | Q2 (0–2) | Q3 (0–2) | Q4 (0–1) | Q5 (0–2) | Q1+Q2+Q3 | Ngưỡng (≥ 4/6 và Q5 ≥ 1) | Q8 (1–5) |
|---|---|---|---|---|---|---|---|---|
| A lượt 1 | 2 | 2 | 2 | 1 | 2 | **6** | đạt | 3 |
| A lượt 2 | 1 (thiếu trả dồn, 3–5 năm) | 2 | 2 | 1 | 2 | **5** | đạt | 3 |
| B lượt 1 | 1 (thiếu trả dồn) | 2 | 2 | 1 | 2 | **5** | đạt | 4 |
| B lượt 2 | 1 (thiếu trả dồn) | 2 | 2 | 1 | 2 | **5** | đạt | 3 |

**Độ lệch:**
- **Giữa lượt, cùng người:** A lệch 1 điểm (6 → 5, ở Q1). B lệch 0 điểm ở Q1–Q5, Q8 lệch 1 (4 → 3).
- **Giữa người** (trung bình 2 lượt):
  - Q1+Q2+Q3: A 5,5 · B 5,0 (lệch 0,5).
  - Q8: A 3,0 · B 3,5 (lệch 0,5).
  - Q4 và Q5: không lệch. Cả 4 lượt đều đọc đúng chuỗi cảm xúc "vui → lo/buồn khi ngân hàng đóng cửa → vui lại năm 1934".

## Điều cả hai người cùng thấy (dùng để sửa hình, không sửa lời)
| Vấn đề (Q6/Q7) | Số lượt nêu | Ô | Ghi chú sửa |
|---|---|---|---|
| Các thẻ số 1–5 khó hiểu ("đếm gì?"), thẻ "3–5 YEARS" quá nhỏ ở khung mẫu | 4/4 | 4 | Khung mẫu rơi vào lúc thẻ "3–5 YEARS" đang bật. Thẻ cần hiện cùng lúc với lịch, và gắn chữ "years" lên dải |
| Walt đứng trước bức tường trắng, không có thông tin | 4/4 | 17 (N) | Nền là mặt sau sổ cái. Sửa: máy đặt sao cho thấy cột cuối của sổ cái sau lưng Walt |
| "Today": hai nhân vật mới không rõ là ai | 3/4 | 19 (P) | Cần cầu nối, ví dụ Walt già hoặc ảnh Walt trên tường, hay chữ "Today: the same loan, 30 years" |
| Năm 1934 mà ngân hàng vẫn đóng, nhìn như lặp cảnh | 3/4 | 12 (K1) | Cảnh rạng sáng thiếu tín hiệu đổi. Sửa: bỏ tờ CLOSED hoặc mở cửa ở K1 |
| Ảnh tư liệu "đổi chất liệu" | 4/4 | 10 (I) | Cả 4 lượt đều nói lớp hoà và chữ CLOSED đè lên ảnh "giúp nối phần nào". Một lượt (B-1) thấy ảnh giống biểu tình (biển TAX/PAY) hơn cảnh rút tiền: **đúng với nhãn LoC** (đám đông người gửi tiền sau khi ngân hàng đổ). Lời "depositors still crowded outside" khớp, nhưng hình không tự nói ra |
| 8 ô xanh + 1 ô trắng, không khớp 80 % | 2/4 | 15 (L2) | Khung mẫu bị cắt mất 1 ô. Sửa: lùi máy cho đủ 10 ô |

## Giới hạn
- Đây là **mô hình đọc khung**, không phải người xem video. Không có chuyển động, không có nhịp, và người đọc được xem ảnh lâu tuỳ ý.
- Điểm do phiên tự chấm.
- **Không dùng làm cổng** (CHARTER §4 chống Goodhart). Thước đo cuối vẫn là phiếu L3 của chủ dự án ở G2.
- Muốn có đọc mù người thật thì cần 2 người do chủ dự án chọn, theo `blind/PHIEU-v2.md` (xem video tắt tiếng một lần).
