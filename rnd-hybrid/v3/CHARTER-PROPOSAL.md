# Đề xuất CHARTER §4, vòng 3 (rnd-hybrid, 14/10/2026). CHỈ ĐỀ XUẤT

Phiên này **không** sửa `CHARTER.md`, `checks/` hay toolkit/factory. Sửa hiến chương và gen được bảo vệ là việc của chủ dự án (CHARTER §6).

Đề xuất này thay bản nháp H4′ trước đó. Nó viết theo lựa chọn của chủ dự án ngày 14/10:
- chương lịch sử dùng **P3, tranh in báo 1930 (2.5D)**;
- phần "Today" dùng **biến thể màu sạch** của cùng bộ người.

Số đo dẫn chứng lấy từ `v3/REPORT.md`, `v3/BLIND.md` và `v3/gate/`.

---

## Đ1. Gen hình chương lịch sử: "tranh in báo thời kỳ, 2.5D"
> - Chương lịch sử, con người dùng **tranh khắc mực vẽ bằng mã**: gạch chéo theo độ tối, màu trầm sepia của giấy báo.
>   - Người, nhà, đồ vật **cùng một mức cách điệu**: cùng bộ vẽ `figure1930.js` và `street2d.js`.
>   - Các tấm tranh **xếp lớp trong 3D**; máy trượt tạo thị sai.
> - **Không gạch** trên mặt, tay, chữ và thẻ chữ.
> - Kiến trúc và trang phục đúng thời kỳ. **Không** dùng mô hình người tải về, **không** dùng ảnh hay video do AI sinh.
> - Nhân vật mang nhãn ILLUSTRATIVE, có mặt vẽ (mắt, lông mày, miệng) theo cảm xúc.
> - Số chỉ nằm trên **thẻ chữ** (serif đậm, nền giấy, viền mực), kèm dòng nguồn trên hình.

| | |
|---|---|
| **Ưu** | Một chất liệu cho người và nền: không lặp lại lỗi ma-nơ-canh của H4′, không có cảnh "phẳng nhàm" như v2, vì có thị sai và lớp. Màu và nét gần ảnh tư liệu cùng thời, nên chuyển sang ảnh tư liệu êm hơn. Rẻ: 15 s máy mỗi giây phim (v2: 54 s). Tất định |
| **Nhược** | Người là tấm phẳng: chỉ đổi tư thế bằng thay tấm, không có khớp động, và máy không vòng ra sau được. Nét mảnh dễ nhoè khi YouTube nén. Đã qua cổng 360p, nhưng chưa kiểm trên điện thoại thật |
| **Tác động** | D-010 ("thế giới 3D low-poly là hình chính, nhân vật không mặt") cần một **ngoại lệ cho chương lịch sử**. Đây là đổi **thể loại**, chủ dự án quyết. Ở `checks/`: chữ trong texture tranh không vào log chữ của lớp phủ. Gom vào `checks-appeal.md` cho phiên K |
| **Rủi ro** | Chất "báo cũ" dễ bị đọc là trang trí hoài cổ nếu dùng ngoài chương lịch sử. 3/4 lượt đọc mù gọi hình là "cắt giấy (có gạch chéo)" (`blind/raw/`), nghĩa là chưa ai thấy đây là tranh khắc |

## Đ2. Khi nào dùng, và chuyển sang "Today"
> - P3 **chỉ** dùng cho chương lịch sử, trước khoảng năm 1960.
> - Phần hiện tại dùng **biến thể màu sạch** của cùng bộ người: kiểu `paper`, không gạch, trang phục hôm nay.
> - Từ lịch sử sang hôm nay có **một chuyển cảnh chủ ý**. Hiện là lau ngang "mực → màu" 0,9 s, có mép giấy.
> - Chương dữ liệu thuần vẫn dùng thế giới 3D không người (D-010).

| | |
|---|---|
| **Ưu** | Người xem biết ngay đang ở "khi đó" hay "bây giờ" |
| **Nhược** | 3/4 lượt đọc mù thấy cặp đôi ở "Today" "đột ngột, không biết họ là ai" (`BLIND.md`). Cần cầu nối hình (ảnh Walt trên tường, hoặc thẻ "the same loan, 30 years") |
| **Tác động** | Spine cần trường `era: history|today` theo chương (đề xuất cho nhà máy) |
| **Rủi ro** | Lạm dụng chuyển cảnh |

## Đ3. Ảnh tư liệu: ≤ 6 s, toàn khung, liền mạch với P3
> - Tư liệu (RIGHTS §F) chỉ **toàn khung**, không dán nhân vật lên ảnh.
> - Mỗi lần ≤ 6 s liền, tổng ≤ 20 % thời lượng.
> - Phủ tông **cùng bảng sepia** với P3, thêm vân in ngang nhẹ.
> - Hoà vào 0,7 s, hoà ra 0,8 s về cảnh P3 cùng địa điểm.
> - Năm và nguồn trên hình; không đi kèm claim số.

| | |
|---|---|
| **Ưu** | Clip v3: 4,27 s (9,1 %), ảnh và tranh cùng sắc độ |
| **Nhược** | Cả 4 lượt đọc mù vẫn thấy "đổi chất liệu" (ảnh thật nhiều chi tiết), dù cả 4 nhận ra lớp hoà và chữ CLOSED đè lên "giúp nối phần nào". Một lượt thấy ảnh giống biểu tình hơn cảnh rút tiền (`BLIND.md`) |
| **Tác động** | RIGHTS §F3 hiện ưu tiên "đặt ảnh trong thế giới". Đề xuất đảo lại cho chế độ này (A39/F15 ở phiên K) |
| **Rủi ro** | Năm catalog lệch năm sự kiện (LoC ghi 1931, ngân hàng đóng cửa 12/1930). Bắt buộc đối chiếu nguồn gốc như `v2/CLAIMS.md` |

## Đ4. Cổng máy "nén giả YouTube" trước mọi bản nháp
> Trước khi dựng clip, các khung mẫu (cận người, toàn cảnh có chữ chính) phải qua cổng tự động `v3/gate/youtube_gate.py`:
> 1. nén x264 1080p ≈ 8 Mbps, rồi hạ xuống 360p;
> 2. trong vùng chữ và vùng mặt, đo Michelson sau ngưỡng Otsu và chiều cao vùng;
> 3. ngưỡng ghi trước: chữ ≥ 0,35 và cao ≥ 9 px; mặt ≥ 0,35 và cao ≥ 14 px.
>
> Trượt thì giảm mật độ gạch rồi chạy lại, tối đa 2 vòng, sau đó đi tiếp và ghi lệch. Đây là **chẩn đoán**: ngưỡng chưa hiệu chuẩn trên đối chứng (CHARTER §4 chống Goodhart).

| | |
|---|---|
| **Ưu** | Bắt sớm lỗi "đẹp ở 1080p, nhoè trên điện thoại". Chạy nhanh, tất định |
| **Nhược** | Vùng kiểm phải khai trong scene (`window.ROI`). Michelson không đo được "đọc hiểu" |
| **Tác động** | Thêm một bước vào lịch tập; không đụng `checks/` |
| **Rủi ro** | Tối ưu theo con số. Vì vậy luôn kèm tự xem ảnh 360p |

## Đ5. Nguồn và giấy phép hình
> - Mọi người, nhà, đồ vật **dựng bằng mã** của kênh. Không mô hình người tải về, không Mixamo, không nhà cung cấp ảnh/video AI.
> - Tài sản ngoài chỉ gồm ảnh tư liệu theo RIGHTS §F (danh sách trắng, cấm NC/ND/BY-SA cho hình, không người thật còn sống) và mô hình CC0 (RIGHTS §F7) khi thật cần.
> - Repo công khai: chỉ commit tệp CC0.

| | |
|---|---|
| **Ưu** | Không rủi ro giấy phép cho nhân vật; diện mạo riêng của kênh |
| **Nhược** | Mỗi trang phục hay kiến trúc của thời kỳ khác phải vẽ thêm bằng mã |
| **Tác động** | Các gói Kenney/Quaternius ở `v3/assets/` chỉ còn là hồ sơ R&D |
| **Rủi ro** | Không có |

## Đ6. Chi phí và giờ máy (máy hiện tại: 4 lõi, WebGL phần mềm)
| Hướng | Giờ máy / s phim (1080p, 4 worker) | Mỗi phút phim | Chi API |
|---|---|---|---|
| v2 (giấy trong 3D) | 54 s | ≈ 54 phút | giọng ≈ 0,19 $ / 45 s |
| H4′ (Quaternius, đã bác), đoạn lượn 6 s | 51 s | ≈ 51 phút | 0 |
| **P3 clip v3** | **15,2 s** (712 s / 46,9 s) | **≈ 15 phút** | 0 (dùng lại giọng v2) |
| Đọc mù 2 người × 2 lượt (headless, khoá Console) | | | 0,549 $ |

> Đề xuất ghi giờ máy mỗi phút phim và chi đọc mù vào báo cáo của mọi tập dùng P3.

| | |
|---|---|
| **Ưu** | Một tập 10 phút ≈ 2,5 giờ máy |
| **Nhược** | Khởi động trang lâu hơn khi cảnh có nhiều người (vẽ canvas) |
| **Tác động** | Không có |
| **Rủi ro** | Không có |

## Đ7. Áp thử
> Áp Đ1–Đ6 cho **một chương lịch sử của Tập 9 "How the 30-year mortgage was invented"** (≈ 60–90 s). Đây là cùng câu chuyện với clip v3: 3–5 năm trả dồn, ngân hàng đóng cửa 12/1930, FHA 1934 cho vay tới 80 % trong tối đa 20 năm, năm 1954 lên 30 năm.
> - Lời phải đối chiếu nguồn gốc theo `v2/CLAIMS.md`.
> - Phải qua: cổng nén 360p (Đ4); đọc mù 2 người tắt tiếng 2 lượt (chẩn đoán); phiếu L3 của chủ dự án ở G2.
> - Nếu phiếu L3 kém hơn chương cùng chủ đề dựng bằng thế giới 3D không người thì rút về.

| | |
|---|---|
| **Ưu** | Thử trên tập thật, quy mô nhỏ, rút lui được |
| **Nhược** | Thêm một vòng R&D trong lịch tập |
| **Tác động** | Spine Tập 9 cần trường `era` |
| **Rủi ro** | Đọc mù bằng mô hình (headless) **không phải người**. Chỉ dùng chẩn đoán, không làm cổng |
