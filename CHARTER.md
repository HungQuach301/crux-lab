# CRUX — HIẾN CHƯƠNG v2.2

Chủ dự án: Hung Quach. v2.1 (29/09/2026): khung chất lượng 3 lớp, 6 cổng, ba tham chiếu. v2.2 (04/10/2026, D-005): 3 cổng GU + 3 cổng TỰ ĐỘNG, danh sách việc tự quyết, vai REVIEWER, bỏ phép che chữ/số. Tài liệu này là nguồn thẩm quyền số một; mọi file khác phải khớp với nó.

## 0. Khởi động mọi phiên
Phiên của một tập đọc `CHARTER.md`, `playbook/quality-framework.md`, `playbook/episode.md`, rồi `PLAN.md`, `ledger.md` của tập và **chỉ các file được nêu tên** trong PLAN. Phiên tổng kết và phiên R&D đọc thêm `playbook/lessons.md`, `taste-ledger.md`.

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

- Khi mâu thuẫn: luật cứng > dữ liệu khán giả > gu chủ dự án > chuyên gia > mẫu hình > kinh điển > ý kiến model.

## 5. Chuẩn chất lượng — khung 3 lớp (`playbook/quality-framework.md`)
- **Định nghĩa:** người xem, xem một lần, đánh giá tập ngang ba tham chiếu (`playbook/references.md`): Vox (truyện), 3Blue1Brown (hình mang nghĩa), WSJ "three charts" (thể loại).
- **Ba lớp:** L1 Kỹ thuật (máy, Chặn: số liệu, claim và nguồn, ILLUSTRATIVE, quyền tài sản, file, âm lượng, ASR, chính sách nền tảng) · L2 Nghề (kiểm mù và phiếu; máy chỉ cảnh báo; luật phân cấp Chặn / Chính / Tham khảo) · **L3 Khán giả (thước đo cuối):** chủ dự án xem một lần ở C6; sau phát hành, số liệu YouTube. Kiểm mù do agent độc lập, mù tập chấm; bên dựng không chấm mình.
- **Ưu tiên:** cảm xúc > truyện > nhịp > đường mắt > bố cục. **Chống Goodhart:** không chỉ tiêu số lượng cho kỹ thuật nghệ thuật; ±5% quanh ngưỡng phải nêu tên; không thủ thuật.
- **Sáu cổng mỗi tập:** C1 Ý tưởng → C2 Kịch bản → C3 Thiết kế và giọng → C4 Animatic (chốt truyện) → C5 Render và L1 → C6 Chấm cuối. **C1, C3, C6 là cổng GU**: chủ dự án quyết, gói ≤ 3 câu. **C2, C4, C5 là cổng TỰ ĐỘNG**: ngưỡng ghi trước, tối đa 2 vòng, nhánh dự phòng đặt sẵn; qua thì báo issue để chủ dự án phủ quyết, không dừng chờ. Thước đo hình là cổng gốc (tắt tiếng, giữ chữ/số) ở C3, C4.
- **Nhân dạng (gen được bảo vệ):** "we" chỉ người phân tích; không khuyên; không dự báo thị trường; "US only"; "history, not a forecast" khi dùng dữ liệu lịch sử. Không dùng thế giới 3D.
- **Đạt phát hành:** không lỗi Chặn, không hồi quy; chủ dự án duyệt ở C6.

## 6. Tiến hoá
- Bộ gen (hợp đồng, tri thức, sổ gu, bài học; không phụ thuộc model) thay đổi qua mỗi tập sao cho độ thích nghi đo được tăng, luôn trong các bất biến do chủ dự án giữ.
- Ba vòng: mỗi tập (lỗi → `playbook/lessons.md`, sổ gu hoặc luật); mỗi chu kỳ (thí nghiệm có đối chứng → giữ biến thể thắng); mỗi thế hệ model (benchmark → đổi → tỉa). Lên bậc tự chủ theo bằng chứng.

## 7. Hệ miễn dịch
1. Không biến thể nào được sửa bộ đo đang chấm nó; bộ đo chỉ đổi qua vai riêng và cần chủ dự án duyệt.
2. Không có số đo trên sản phẩm cuối thì coi như chưa làm, chưa cải thiện.
3. Mỗi miễn trừ trong luật kiểm phải có tiêu chí thay thế; không có điểm mù không được canh.
4. Hạn mức kích thước bộ gen; bắt buộc tỉa khi đổi model.
5. Việc irreversible chỉ chủ dự án quyết: phát hành công khai, chi tiêu mới, tài khoản và secret, nhà cung cấp mới, sửa hiến chương, sửa gen được bảo vệ, chọn giọng cuối (#158). Gu không bao giờ tự quyết: giọng và model giọng, hướng hình, bảng màu, nhạc và cách phối, cấu trúc truyện, cold open, logline, tiêu đề, thumbnail. Phiên chỉ tự quyết việc trong **danh sách đóng** (`quality-framework.md` §6); việc khác vào gói cổng GU kế tiếp.

## 8. Vai trò
| Vai | Làm | Không làm |
|---|---|---|
| Chủ dự án | Định hướng, gu, duyệt gói, quyết irreversible, chịu trách nhiệm; tác giả – đạo diễn (`AUTHORSHIP.md`) | Không dựng, không viết luật |
| Phiên điều phối (P1/P2/P3) | Mỗi tập 3 phiên ngắn (`playbook/episode.md`); giữ `PLAN.md`, chạy cổng, giao kiểm mù; duy nhất merge vào `main` | Không tự quyết gu; không sửa luật kiểm; không chấm kiểm mù |
| Phiên dựng | Dựng trọn tập theo đầu bài | Không sửa luật kiểm |
| Phiên kiểm (K) | Viết và giữ luật; một lần mỗi tập, ngay khi claim C2 chốt; đặt tên kind/params; tính lại số | Không dựng |
| REVIEWER | Agent độc lập; soát mọi gói và issue cổng theo checklist cố định trước khi gửi | Không dựng, không quyết |
| Phiên R&D | Đề xuất biến thể bộ gen; chạy thí nghiệm | Không tự áp dụng khi chưa đủ bậc |

## 9. Chỉ số
Chất lượng (điểm phiếu chấm, tỷ lệ luật đạt, lỗi số = 0) · Khán giả (giữ chân ở giây 30, thời lượng xem, CTR, giờ xem) · Hiệu quả (số lần chủ dự án tham gia/tập, vòng mỗi cổng, lượt agent, ký tự giọng, thời gian, token) · Tiến hoá (biến thể đề xuất/thử/giữ, độ khớp kiểm mù AI với chủ dự án) · Cảnh báo (việc không phải tập > 20%, chu kỳ không ra tập, máy móc phình to, hồi quy).

## 10. Thẩm quyền và kênh chỉ dẫn
Thứ tự: hiến chương → quyết định (`decisions/`) → `playbook/quality-framework.md` → spec thể loại → sổ gu. Chỉ dẫn của chủ dự án đi qua issue chỉ dẫn và gói duyệt; phiên chỉ nhận việc gắn với một tập hoặc một chỉ dẫn.
