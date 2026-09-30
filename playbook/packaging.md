# Đóng gói phát hành (tiêu đề, thumbnail, hai dòng đầu mô tả): BẢN NHÁP

Bản nháp, 30/09/2026 (PACKAGING, Tập 1, nhánh `ep001-v2`). **Chưa là luật.** Chủ dự án duyệt ở bước tổng kết Tập 1. Tài liệu này không sửa CHARTER; mục 5 chỉ là đề xuất cho Tập 2.

Bối cảnh: gói C5 của Tập 1 (T1 + thumb-3) đạt mọi luật đếm được, nhưng chủ dự án nhận xét: *"chỉ đạt kỹ thuật, chưa đạt sức hút"*. Gói v2 (`episodes/ep001/out/package/v2/`) được làm lại theo quy trình dưới đây.

## 1. Nguyên tắc (không phải luật đếm)

Các con số ở mục 3 là **ngưỡng sàn** để phát hiện lỗi, không phải mục tiêu. Tối ưu cho con số thì được thumbnail sạch nhưng không ai bấm (bài học A1, B2 trong `lessons.md`).

1. **Một lời hứa, nói bằng hai kênh.** Tiêu đề và thumbnail cùng phục vụ **một** câu hỏi người xem đang có. Chúng bổ sung cho nhau: tiêu đề nói điều hình không nói được, hình cho thấy điều chữ phải giải thích dài. Không lặp chữ của nhau.
2. **Nói với một người cụ thể.** Viết cho "người Mỹ đang trả góp khoản vay ký 2022–2024, trong tay có lời mời refinance", không cho "người quan tâm tài chính". Người đó phải nhận ra mình trong 1 giây.
3. **Sức hút đến từ sự thật lạ, không từ phóng đại.** Móc tốt nhất là một kết quả có thật của phim mà người xem không đoán được (khoản vay nhỏ cần cắt nhiều hơn). Nếu móc cần một từ vượt claim ("always", "your loan", "banks hide"), bỏ móc đó, đừng bỏ claim.
4. **Mọi con số là một claim.** Số trên thumbnail, trong tiêu đề hay mô tả phải là `display` của một claim trong `out/claims.json`, đúng đơn vị: *điểm phần trăm* khác *phần trăm*. Nếu chủ dự án đưa số không khớp claim (ví dụ −0.33% so với claim 0.32), báo lại, đề xuất cách viết đúng, không tự sửa ý.
5. **Số của nhân vật minh hoạ mang nhãn minh hoạ.** Nếu nhãn làm hỏng hình, bỏ số chứ đừng bỏ nhãn. Còn không thì chấp nhận cảnh báo P01 và ghi rõ lý do.
6. **Không khuyên, không dự báo, không đồng hồ đếm ngược giả.** "Missed it?" là câu hỏi, được dùng. "Rates will rise, act now" thì không.
7. **Dùng hệ hình đã ký.** Thumbnail dựng từ chính vật thể và token của phim (C3), để người bấm vào thấy đúng thứ đã được hứa.
8. **Người chọn là chủ dự án.** Người làm gói đưa phương án kèm bằng chứng. Kiểm mù chỉ để tham khảo.

## 2. Thư viện kiểu móc

Mỗi tập thử ít nhất 3 kiểu khác nhau, mỗi kiểu 2 cách viết. Cột "Rủi ro" là chỗ móc dễ vượt claim nhất.

| Kiểu móc | Cơ chế | Ví dụ Tập 1 | Rủi ro / cách kiểm |
|---|---|---|---|
| **Nghịch lý** | Kết quả ngược trực giác | "Why a Smaller Loan Needs a Bigger Rate Cut to Be Worth It" | Nghịch lý phải đúng trong điều kiện của phim (phép thử 3 năm); ghi điều kiện trong mô tả |
| **Chi phí ẩn** | Có một khoản người xem chưa tính | "The Refinance Cost That Isn't in the Fees" | Không nói ai "giấu" nếu không có nguồn; không gọi thứ không phải phí là "fee" |
| **"Người như tôi"** | Gọi đúng nhóm người xem | "Got a 2023 Mortgage? The 1-Point Rule May Not Fit Your Loan" | Nói về "your" thì dùng "may", vì phim chỉ chứng minh cho nhân vật minh hoạ |
| **Cửa sổ / thời điểm** | Có một khoảnh khắc đã qua hoặc đang tới | thumb-W: 5.98% + "Missed it?" | Dễ thành dự báo hoặc thúc ép. Chỉ nói điều đã xảy ra, có ngày |
| **Cú sốc con số** | Một con số lớn, lạ, đúng | "$5,124" + "+$1,133" | Số phải là claim; số nhân vật cần nhãn minh hoạ; không làm tròn lên cho kêu |
| **Luật quen bị thử** | Lấy quy tắc ai cũng nghe, kiểm lại | "1-point rule" | Tên luật đúng đơn vị (điểm, không phải %); "bị thử" khác "bị bác bỏ" |
| **Câu hỏi của người xem** | Lặp nguyên câu người xem gõ tìm | T1 "How Big a Rate Cut Makes a Refinance Worth It?" | An toàn nhưng phẳng: nên làm đối chứng |
| **So sánh cặp** | Hai người, cùng điều kiện, kết quả khác | "Same Rate Cut, Opposite Results …" | "Opposite" chỉ đúng trong một phép thử; nói rõ phép thử |

## 3. Kiểm 3 lớp

**L1: đúng và đọc được (máy + người làm gói, bắt buộc trước khi đưa phương án)**
- *Claim*: mỗi số và mỗi khẳng định trỏ về claim ID (bảng trong `titles.md`); đơn vị đúng; số minh hoạ có nhãn.
- *Ngôn từ*: quét regex ADVICE/FORECAST/FOUR/WE_BAD của S10 trên tiêu đề, mô tả, bình luận ghim, chữ thumbnail.
- *Độ dài*: tiêu đề ≤ 60 ký tự (đếm bằng máy); hai dòng đầu mô tả ~150 ký tự và chứa từ khoá chính.
- *Quyền*: font và tài sản đã khai trong `RIGHTS.md`; không logo hay thương hiệu của bên khác.
- *Đọc được*: xem ảnh ở 25% (320×180) và 10% (128×72); tương phản ≥ 3:1 ở 10% trong mọi hộp chữ; chữ ≥ 90 px là tham khảo (P01). Số chữ ≤ 4 là hướng dẫn, không phải quota.
- *Màu*: chữ và mảng phẳng dùng màu token. **Đề xuất sửa P01**: đo tỉ lệ token trên vùng chữ và mảng phẳng, không đo trên cả ảnh 3D. Ảnh H1 có vật liệu đã ký (gỗ, tường) nên tỉ lệ token toàn ảnh chỉ 45–94%, dù không có màu nào ngoài hệ.

**L2: tay nghề và nhất quán thương hiệu (người làm gói tự đánh giá, rồi một agent mới đọc)**
- Một ý bằng hình, đọc được khi tắt chữ (che chữ, hỏi "ảnh này nói gì").
- Cùng vật thể, màu và chữ với phim (C3). Nhân vật giữ đúng màu và hình (Walt vàng/tam giác, Anjali đỏ/vuông).
- Tiêu đề và thumbnail bổ sung, không lặp.
- Đứng cạnh các video khác trong kết quả tìm kiếm: có nổi không? (thẻ `cards/`).

**L3: so cặp mù (tham khảo) + chủ dự án chọn**
- Thẻ kết quả tìm kiếm (thumbnail + thời lượng + tiêu đề + tên kênh), mỗi cặp một ảnh, cả hai thứ tự, tên hex ngẫu nhiên, khoá `key.json` mở sau.
- Câu hỏi cố định, vai người xem cố định (bài học B5). Agent mới cho mỗi ảnh.
- Hai bộ: gói (tiêu đề + thumbnail) và chỉ thumbnail (cùng tiêu đề), để tách tác động của hình khỏi chữ.
- Tính: tỉ lệ thắng mỗi gói, độ lệch vị trí (tỉ lệ chọn "1"), lý do lặp lại. Không chốt bằng điểm. Chủ dự án đọc lý do và chọn.
- Sau khi đăng: YouTube **Test & Compare** (tối đa 3 thumbnail) là phép đo thật. So cặp mù chỉ để chọn 3 ứng viên.

## 4. Quy trình Tập 1 v2 (ghi lại để làm lại được)

1. Đọc claims, `numbers.md`, lời phim; liệt kê 5–8 "sự thật lạ" có claim.
2. Viết 2 tiêu đề cho mỗi hướng móc chủ dự án chọn; đếm ký tự; quét S10; ghi claim cho từng tiêu đề.
3. Mỗi hướng một thumbnail: dựng still từ engine C3 (`preprod/thumbs_v2/render.js`), ghép chữ phẳng, ghi hộp chữ; tự kiểm (`selfcheck.py`: claim, cỡ chữ, tương phản 10%, ảnh 25%/10%).
4. Hai dòng đầu mô tả: 2 phương án, cùng lời hứa.
5. Vật liệu so cặp mù (`pack_test.js`).
6. Phiếu tải lên: tags, hashtag, mục khai báo, giờ đăng đề xuất, câu mời bình luận, bình luận ghim, end screen.
7. Báo căng thẳng (số không khớp claim, nhãn minh hoạ và P01, "đang đóng" và "đã đóng") cho chủ dự án. Không tự quyết phần gu.

## 5. Đề xuất cho Tập 2: đưa gói phát hành vào cổng (chưa sửa CHARTER)

Tập 1 đóng gói ở cuối (C5), sau khi phim đã xong, nên gói phải nói bằng hình của phim nhưng không ảnh hưởng ngược lại được phim. Đề xuất:

| Cổng | Thêm gì | Vì sao |
|---|---|---|
| **C1 Ý tưởng** | Lời hứa = **tiêu đề nháp** + kiểu móc (2–3 hướng từ thư viện mục 2), người xem cụ thể, "sự thật lạ" dự kiến (đợi DATA xác nhận). Kiểm mù ý tưởng bằng thẻ chỉ tiêu đề. | Nếu không viết được một tiêu đề hút mà vẫn đúng claim, ý tưởng chưa đủ. Móc chọn ở C1 dẫn cold open. |
| **C3 Thiết kế** | Mỗi hướng thiết kế kèm **một concept thumbnail** dựng từ chính hệ hình (vật thể, token). Chừa sẵn: vật thể "anh hùng" đọc được ở 10%, chỗ cho huy hiệu minh hoạ ≥ 90 px nếu định in số nhân vật. **Chừa đuôi end screen 15–20 s** trong kế hoạch dựng. | Tập 1 không có đuôi end screen và không có chỗ cho huy hiệu lớn: hai căng thẳng này sinh ra vì gói đến muộn. |
| **C6 Chấm cuối** | Chốt gói: 3 thumbnail cho Test & Compare, 1–2 tiêu đề, mô tả, phiếu tải lên; so cặp mù L3; chủ dự án chọn trong cùng gói quyết định C6 (≤ 3 câu hỏi). | Gói được duyệt cùng phim, theo cùng quy tắc kiểm mù. |

Đề xuất sửa luật (cho K-review, không tự áp):
- **P01**: đổi "token share toàn ảnh ≥ 97%" thành "chữ và mảng phẳng: màu token; vật 3D: vật liệu đã ký (`design/c3/final/tokens.json → materials`)". Thêm ngoại lệ có lý do cho huy hiệu ILLUSTRATIVE < 90 px, hoặc đặt cỡ huy hiệu riêng cho thumbnail.
- **Thêm luật tham khảo P02** (gói): tiêu đề ≤ 60 ký tự; mỗi số trong tiêu đề/thumbnail/mô tả khớp `display` của claim; quét S10 trên chữ của gói.
