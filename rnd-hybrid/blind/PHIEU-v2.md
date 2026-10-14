# Phiếu đọc mù TẮT TIẾNG, vòng 2: clip `rnd-hybrid/v2/clip/out/clip-1080.mp4` (2 người, chưa chạy)

Cách làm, ngưỡng ghi trước và chỗ ghi kết quả giữ nguyên như `PHIEU.md`. Xem tắt tiếng hoàn toàn, **một lần**, không tua, không dừng, rồi trả lời ngay; người hỏi không gợi ý. Mỗi người mất khoảng 5 phút. Cần **2 người chưa đọc kịch bản, CLAIMS hay REPORT**, do chủ dự án chọn.

**Vì sao vòng này vẫn chưa chạy:** lệnh phiên cấm agent con và `toolkit/blind/headless.sh` cần Console, mà Console bị khoá. Phiên không có người đọc độc lập, còn tự chấm thì không còn mù.

Câu hỏi giữ như vòng 1. Đáp án gốc đổi theo lời đã sửa bằng nguồn gốc (`v2/CLAIMS.md`):

| # | Câu hỏi (ghi nguyên lời đáp) | Đáp án gốc (người hỏi giữ, không đưa ra) | Chấm |
|---|---|---|---|
| Q1 | Kể lại câu chuyện trong 3 câu. | Năm 1930 ngân hàng chỉ cho vay khoảng nửa giá nhà, trong 3–5 năm, cuối kỳ trả dồn cả khoản. Ngân hàng đóng cửa (12/1930), người gửi tiền đứng ngoài, không vay lại được thì mất nhà. 1934 có FHA: vay tới 80 % giá trị, trả dần mỗi tháng tới 20 năm; 1954 lên 30 năm | 0/1/2 |
| Q2 | Khoản vay năm 1930 có gì nguy hiểm? | Kỳ hạn ngắn 3–5 năm, cuối kỳ phải trả hết một lần ("THE WHOLE LOAN · DUE NOW") | 0/1/2 |
| Q3 | Điều gì thay đổi năm 1934? | FHA bảo hiểm khoản vay mới: tới 80 % giá trị, trả dần mỗi tháng (bậc giảm dần), tới 20 năm, không còn khoản lớn cuối kỳ | 0/1/2 |
| Q4 | Các con số trên màn hình nói gì? (vòng 1 hỏi "con số lớn"; vòng 2 có 5 thẻ số) | ≈ nửa giá · 3–5 năm · tới 80 % giá trị · tới 20 năm · 1954 tới 30 năm. Nhớ đúng ≥ 3 thẻ = 1 điểm | 0/1 |
| Q5 | Nhân vật đội mũ cảm thấy gì, và thay đổi lúc nào? | vui → sốc khi tới hạn → buồn khi mất nhà, lo trước ngân hàng đóng → nhẹ nhõm (1934) | 0/1/2 |
| Q6 | Có cảnh nào khó hiểu hoặc thừa? Ghi giây (ước lượng). | — | ghi lại |
| Q7 | Ảnh tư liệu (đám đông dưới mưa) có cùng "thế giới" với hình giấy 3D không? Có thấy "đổi chất liệu"? | — | có/không + lý do |
| Q8 | Nếu đây là đầu một video 10 phút, bạn có xem tiếp không? Chấm 1–5. | — | điểm |

**Ngưỡng (giữ như vòng 1, chưa hiệu chuẩn):** mỗi người Q1 + Q2 + Q3 ≥ 4/6 và Q5 ≥ 1 thì coi là "truyện đọc được không cần lời". Nếu cả 2 người dưới ngưỡng: sửa hình (không sửa lời), rồi đọc lại 1 vòng.

Kết quả ghi vào `rnd-hybrid/blind/KETQUA.md`. Dải 6 khung cho từng nhóm cảnh (cho người đọc không xem được video) nằm ở `rnd-hybrid/v2/blind-strips/`, tạo bằng `toolkit/blind/strips.py`.
