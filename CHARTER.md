# CRUX — HIẾN CHƯƠNG v2 (bản nháp, chờ chủ dự án duyệt)

Chủ dự án: Hung Quach. Thay thế CHARTER v1 khi được duyệt. Tài liệu này là nguồn thẩm quyền số một; mọi file khác phải khớp với nó.

## 1. Định vị
- **Kênh:** `us-personal-finance`, tiếng Anh Mỹ, không lộ mặt, data-explainer, 8–15 phút.
- **Định vị:** *Phòng thí nghiệm quyết định tài chính.* Mỗi tập trả lời một quyết định cụ thể bằng mô phỏng đầy đủ trên dữ liệu thật, nguồn và phương pháp minh bạch.
- **Ba dòng nội dung:** (1) vay và nợ; (2) nghỉ hưu và đầu tư dài hạn qua lịch sử; (3) thuế và chính sách, tác động bằng con số.
- **Mục tiêu:** tập đạt chuẩn → khán giả → nhiều kênh → thương mại hoá phương pháp kiểm chứng cho tổ chức.

## 2. Bất biến vận hành: không có tập, không có nền tảng
1. Tập đầu tiên chính là nền tảng; nền tảng rút ra từ việc đã lặp lại, không thiết kế trước.
2. Quy tắc ba lần: chỉ tự động hoá một bước sau khi đã làm tay ≥ 3 lần và đo được nó tốn thời gian của chủ dự án.
3. Nhịp đo bằng tập: mỗi chu kỳ kết thúc bằng một tập (phát hành được hoặc có gói duyệt); không mở chu kỳ mới khi tập trước chưa xong hoặc chưa huỷ có lý do.
4. Một luồng trước, song song sau; mỗi tập một nhánh hoặc thư mục riêng.
5. Việc không phải tập ≤ 20% công sức mỗi chu kỳ; mỗi hạng mục phải trả lời "việc này giúp tập kế tiếp thế nào?".
6. Hiến chương giữ dưới 2 trang; spec lớn lên theo từng tập.

## 3. Tám nguyên tắc thiết kế
1. Xây hợp đồng, không xây cơ chế; code thực thi là đồ dùng một lần.
2. Tích luỹ dữ liệu độc quyền: sổ gu, sổ claim, dữ liệu có phiên bản, kho tập kèm điểm, dữ liệu khán giả.
3. Đánh giá trước, xây sau; mỗi model mới phải làm nhà máy gọn hơn.
4. Lớp điều phối mỏng nhất có thể; thuê từ nền tảng, không tự xây.
5. Mỗi lớp (LLM, giọng, video, render) có ≥ 2 nhà cung cấp đã thẩm định.
6. Con người đứng đúng chỗ; đo số phút duyệt của chủ dự án mỗi tập.
7. Không đầu tư thứ cần hơn một chu kỳ model mới hoàn vốn, trừ tài sản ở nguyên tắc 1–2.
8. Phản ứng theo tín hiệu, không theo dự đoán cứng.

## 4. Năm khâu và hai thành phần lõi
| Khâu | Nhiệm vụ |
|---|---|
| 1. Đầu bài | Đề tài, luận điểm, spec thể loại, sổ gu |
| 2. Dựng | Một phiên model hiện hành dựng trọn tập theo hợp đồng |
| 3. Kiểm độc lập | Luật khoá SHA; bên dựng không sửa luật; tính lại số độc lập; đối chiếu điểm ảnh; cổng hồi quy |
| 4. Duyệt người | Gói clip ngắn xem trên điện thoại; phiếu chấm; ghi sổ gu |
| 5. Phát hành và học | Dữ liệu khán giả, A/B tiêu đề và thumbnail; bài học ngược về khâu 1 |

- **Động cơ tiến hoá:** kho tập kèm kết quả; benchmark A–D; phiên R&D định kỳ; thí nghiệm có đối chứng; tỉa khi đổi model.
- **Kho tri thức nghề:** kinh điển, thư viện mẫu, chuyên gia (tuỳ chọn), dữ liệu khán giả, hội đồng phê bình (model đã hiệu chỉnh). Khi mâu thuẫn: luật cứng > dữ liệu khán giả > gu chủ dự án > chuyên gia > mẫu hình > kinh điển > ý kiến model.

## 5. Chuẩn chất lượng
- **Luật cứng, không nhân nhượng:** lỗi số liệu = 0; mọi số có claim và nguồn; số không nguồn gắn ILLUSTRATIVE; chính sách nền tảng.
- **Nhân dạng (gen được bảo vệ):** "we" chỉ người phân tích; không khuyên; không dự báo thị trường; "US only"; "history, not a forecast" khi dùng dữ liệu lịch sử.
- **Chuẩn thể loại = tay nghề:** cấu trúc hồi, vòng mở, câu móc lại, cái giá cụ thể, nhịp căng–chùng, âm thanh theo dữ liệu, mix, kỹ thuật file, khả năng tiếp cận. Không dùng thế giới 3D cho thể loại này.
- **Đạt phát hành:** máy kiểm không trượt luật cứng, không hồi quy; điểm phiếu chấm của chủ dự án trung bình ≥ 4/5, không câu dưới 3.

## 6. Tiến hoá
- **Định nghĩa:** bộ gen (hợp đồng và tri thức, không phụ thuộc model) thay đổi qua mỗi chu kỳ sao cho độ thích nghi đo được tăng; thay đổi do hệ thống sinh, chọn lọc, lưu giữ, luôn trong các bất biến do chủ dự án giữ.
- **Cấp số nhân:** khi model mạnh lên, mức thích nghi nhảy bậc và tốc độ tiến hoá tăng mà không cần thiết kế lại; bị giới hạn bởi vòng chậm nhất (thời gian duyệt, dữ liệu khán giả, chính sách).
- **Ba vòng:** mỗi tập (lỗi → luật hoặc sổ gu); mỗi chu kỳ (R&D → thí nghiệm → giữ biến thể thắng); mỗi thế hệ model (benchmark → đổi → tỉa → nâng chuẩn).
- **Bậc:** L1 học có hướng dẫn (xuất phát) → L2 tự tiến hoá trong vùng an toàn → L3 theo thế hệ model → L4 sinh sản. Lên bậc theo bằng chứng.

## 7. Hệ miễn dịch
1. Không biến thể nào được sửa bộ đo đang chấm nó; bộ đo chỉ đổi qua vai riêng và cần chủ dự án duyệt.
2. Không có số đo trên sản phẩm cuối thì coi như chưa làm, chưa cải thiện.
3. Mỗi miễn trừ trong luật kiểm phải có tiêu chí thay thế; không có điểm mù không được canh.
4. Hạn mức kích thước bộ gen; bắt buộc tỉa khi đổi model.
5. Việc irreversible chỉ chủ dự án quyết: phát hành công khai, chi tiêu mới, tài khoản và secret, nhà cung cấp mới, sửa hiến chương, sửa gen được bảo vệ, chọn giọng cuối (#158).

## 8. Vai trò
| Vai | Làm | Không làm |
|---|---|---|
| Chủ dự án | Định hướng, gu, duyệt gói, quyết irreversible, chịu trách nhiệm | Không dựng, không viết luật |
| Phiên dựng | Dựng trọn tập theo đầu bài | Không sửa luật kiểm |
| Phiên kiểm | Viết và giữ luật; chấm độc lập; tính lại số | Không dựng |
| Phiên R&D | Đề xuất biến thể bộ gen; chạy thí nghiệm | Không tự áp dụng khi chưa đủ bậc |

## 9. Chỉ số
Chất lượng (điểm phiếu chấm, tỷ lệ luật đạt, lỗi số = 0) · Khán giả (giữ chân ở giây 30, thời lượng xem, CTR, giờ xem) · Hiệu quả (chi phí/tập, phút duyệt/tập, vòng sửa/tập) · Tiến hoá (biến thể đề xuất/thử/giữ, độ khớp hội đồng phê bình với chủ dự án, độ trễ học, hệ số nhảy bậc) · Cảnh báo (việc không phải tập > 20%, chu kỳ không ra tập, máy móc phình to, hồi quy).

## 10. Thẩm quyền và kênh chỉ dẫn
Thứ tự: hiến chương → quyết định (`decisions/`) → spec thể loại → sổ gu. Chỉ dẫn của chủ dự án đi qua issue chỉ dẫn và gói duyệt; phiên chỉ nhận việc gắn với một tập hoặc một chỉ dẫn.
