# Vòng 3 · Khung phong cách P1 | P2 | P3 (14/10/2026). DỪNG chờ chủ dự án chọn

**Bối cảnh:** chủ dự án đã bác H4′ (`STEP2-STOP.md`) và bỏ hẳn mô hình người tải về. Cả 3 hướng dưới đây đều **dựng hoàn toàn bằng mã**, không dùng tài sản ngoài nào.

**Luật áp cho mọi khung:**
- trong một khung, thân, mặt, quần áo và nhà ở **cùng một mức cách điệu**;
- kiến trúc và trang phục đúng năm 1930: áo khoác dài tới gối, mũ phớt (không mũ chóp cao), váy dài tới mắt cá, mũ chuông (cloche) cho nữ, nhà gạch có cửa sổ khung kéo, phào mái, mái hiên sọc, biển chữ serif vẽ tay, thang thoát hiểm, ngân hàng tân cổ điển, đèn phố gang;
- không có đồ vật hiện đại.

**Hai khung chung:**
- **K1:** cận một người đàn ông lo âu trước ngân hàng đóng cửa, tháng 12/1930 (ngày đóng cửa theo `v2/CLAIMS.md`).
- **K2:** toàn cảnh đám đông trước ngân hàng.

**Tệp:**
- Tờ 3×2: `style/out/STYLE-3x2.jpg` (cột P1, P2, P3; hàng trên K1, hàng dưới K2).
- Bản 1080p từng khung: `style/out/{P1,P2,P3}-{K1,K2}-1080.jpg`.

| | **P1: giấy nhiều lớp nâng cấp** | **P2: sa bàn tượng nhỏ** | **P3: tranh in báo 1930 (2.5D)** |
|---|---|---|---|
| Người | Vẽ lại theo tỉ lệ người lớn (~7,5 đầu, `style/figure1930.js`). Trang phục 1930 vẽ tay, viền mực. Tách **5 lớp** (tay sau · chân sau · thân · đầu + mũ · tay trước), mỗi lớp cong nhẹ, có mép giấy, cách nhau 3 cm, **đổ bóng lên nhau** | Tượng dựng từ **khối bo tròn**. Áo khoác, mũ phớt, váy, mũ chuông là **khối thật** (lathe, capsule, rounded box). Mặt tối giản: mắt, lông mày nghiêng theo cảm xúc, miệng là ống cong | Cùng bộ vẽ người với P1, nhưng nét **khắc**: gạch chéo theo độ tối, màu kéo về giấy báo sepia. Mặt chỉ có nét, không gạch (cho dễ đọc) |
| Nhà | Khối giấy gấp, mặt tiền in vẽ tay (`style/street2d.js`). Ngân hàng: mặt tiền in, cột giấy cuộn 3D, bậc gấp thật | Cùng chất "thạch cao sơn": tường gạch sơn, cửa sổ lõm có khung kéo, phào, mái hiên sọc, biển sơn chữ serif. Ngân hàng: cột trụ thật, trán tường đùn | Mặt tiền vẽ khắc trên các **tấm phẳng xếp ở nhiều độ sâu** (trời, phố, ngân hàng, 4 hàng người, tiền cảnh), máy 3D tạo thị sai |
| Ánh sáng / hậu kỳ | Đèn hồi khủng hoảng (trời lạnh, đèn bù ấm), bóng thật, vân giấy, viền tối | Đèn hồi khủng hoảng, đèn phố gang phát sáng, bóng mềm. **Độ sâu trường ảnh nông** theo depth (kiểu tilt-shift sa bàn) | Không đèn 3D: mọi sắc độ nằm trong nét khắc. Sương màu giấy báo tách lớp xa |
| Đọc trên điện thoại | Mặt người tiền cảnh rõ; người ở hậu cảnh nhỏ, phẳng | Mặt rõ ở K1. K2 là ấn tượng sa bàn (mờ ngoài vùng nét) | Tương phản mạnh, chữ CLOSED và BANK rất rõ. Gạch chéo dày có thể nhoè ở 360p, **chưa kiểm** trên máy thật |
| Giờ máy (2 khung 1080p, gồm khởi động trang) | 16,7 s | 8,5 s | 13,1 s |
| Tất định (dựng lại 2 lần) | trùng byte | trùng byte | trùng byte |
| Chuyển động khi làm clip | Lớp giấy xoay, trượt theo khớp; biểu cảm đổi tấm đầu. Không xoay quá ~35° kẻo lộ mép | Khớp thật (vai, khuỷu, cổ) xoay được; đi bộ bằng mã; máy lượn tự do | Thị sai giữa các lớp và máy trượt. Người đổi tư thế bằng cách thay tấm (như P1). Máy không vòng ra sau được |
| Rủi ro | Gần với v2 mà chủ dự án thấy "phẳng nên nhàm"; 5 lớp chỉ thấy rõ ở cận | Dễ thành "game đồ chơi" nếu ánh sáng phẳng. Đám đông đông người tốn hình học (46 tượng vẫn nhanh) | Nhiều nét mảnh: phải kiểm nén YouTube và màn hình nhỏ. Chất "báo cũ" hợp chương lịch sử, khó dùng cho phần hôm nay |

## Ghi chú trung thực
- **Chi:** 0 $ (không API). Không mô hình tải về, nên không có dòng RIGHTS mới.
- **Chưa đạt ở P1 K1:** tờ CLOSED bị nhãn năm che một phần, và người đàn ông chưa nghiêng đủ để thấy rõ 5 lớp.
- **Chưa đạt ở P2:** lông mày và miệng vẫn nhỏ ở cỡ cận này.
- **Chưa đạt ở P3:** ở K2 tỉ lệ người với ngân hàng hơi nhỏ.
- **Trong lúc dựng, đã sửa lỗi P1:** nhà giấy bị chôn nửa dưới vì `position.set` ghi đè độ cao.
- **Bước sau** (khi chủ dự án chọn, không mở thêm vòng chọn phong cách): dựng clip v3 bằng hướng được chọn, cùng lời/giọng v2, kèm các sửa a–d. Sau đó đọc mù 2 người × 2 lượt qua headless khoá Console, rồi viết lại `v3/CHARTER-PROPOSAL.md`.

## Tái lập
Từ gốc repo:
`NODE_PATH=$(npm root -g) node toolkit/factory/world/render_shots.js rnd-hybrid/v3/style/<p1|p2|p3> 1080 x.mp4 --stills 0.5,1.5 --stills-dir <thư mục>`
