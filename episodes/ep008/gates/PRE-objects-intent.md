# Tiền kỳ (c) — Ý đồ đọc mù clip vật thể MỚI (ghi TRƯỚC khi chạy; luật tạm 13/10; không sửa sau khi thấy kết quả)

Ngày 2026-10-13. Mẫu: clip 540p 5–8 s (`work/objclip/<vật>.mp4`, dựng `preprod/objclip/`), **tắt tiếng, giữ chữ/số**, cắt dải 6 khung (`toolkit/blind/strips.py`, cả clip). Người đọc: **2 headless Sonnet mới mỗi vật** (khoá Console, `--read`, chỉ thấy một PNG tên hex); lệch → người thứ 3 (≥ 2/3). Người chấm: 1 headless độc lập, mù, nhãn ngẫu nhiên, rubric dưới (A28: câu khuyên = `advice_stated`). Dự kiến 6–9 lượt đọc + 3 chấm (≈ $0,5).

**Câu hỏi cố định (tiếng Anh):** "These are 6 frames, in time order, from a short muted animation. 1. What is this showing? 2. What changes over time? 3. What does it mean? 4. What advice, if any, would a viewer take from this? 5. Did the animation itself suggest this, or is it your own conclusion?" Vai: người thuê nhà Mỹ 2026 tự hỏi thuê có tốn hơn mua không (hồ sơ cầu câu 1).

## Rubric nghĩa (ghi trước; "ý người xem phải đọc ra")
| Vật | Đúng nghĩa (1) cần đủ | 0,5 | 0 |
|---|---|---|---|
| **N1 the street** | (a) dãy nhà = nhiều thời điểm/tháng mua khác nhau xếp theo thời gian (1991 → 2016); (b) nhà sáng đèn = mua có kết quả tốt hơn thuê (sau 10 năm), nhà tối/cửa vàng = thuê tốt hơn; (c) phần lớn sáng, có một đoạn tối | đủ 2/3 | ≤ 1/3 hoặc chỉ tả hình ("houses light up") |
| **N2 the rent tag** | (a) thẻ trên căn hộ = mức tiền thuê giả định (đổi 5 → 4 → 6 %); (b) khi mức thuê đổi, số nhà sáng đèn đổi theo (thuê cao hơn → nhiều nhà sáng hơn); (c) kết quả mua/thuê phụ thuộc vào tiền thuê giả định | đủ 2/3 | ≤ 1/3 |
| **N3 Nina + đèn riêng** | (a) một người (nhân vật chính, minh hoạ) có đèn/ánh sáng riêng đi theo; (b) cô đứng giữa căn hộ (thuê) và ngôi nhà (mua), quay nhìn rồi bước về phía giữa; (c) cô đang cân nhắc thuê hay mua | đủ 2/3 | ≤ 1/3 |

Cờ `advice_stated` (hình/chữ nêu hay ngụ ý mua/thuê/chờ) → vật trượt ngay. `advice_inferred`, `caution_only`: báo, không chặn.
**Ngưỡng mỗi vật:** 2/2 đúng (điểm 1, không `advice_stated`) → ĐẠT; 0/2 → TRƯỢT; lệch → người thứ 3, đạt khi ≥ 2/3.
**Trượt → đổi loại hình trước G1** (luật tạm 13/10 (c); E6 sửa bằng hình trước, nhãn là cách cuối), tối đa 2 vòng mỗi vật (luật tạm: ≤ 2 vòng mỗi lỗi cả tập); vòng 2 vẫn trượt → G1 nêu bản trước/sau cho chủ dự án. Mỗi vòng ghi `fix: picture|label` + lý do.
