# Đề xuất CHARTER §4, vòng 3 (rnd-hybrid, 14/10/2026). CHỈ ĐỀ XUẤT

Phiên này **không** sửa `CHARTER.md`, `checks/` hay toolkit/factory. Sửa hiến chương và gen được bảo vệ là việc của chủ dự án (CHARTER §6). Văn bản dưới đây thay cho mục A, B của `rnd-hybrid/CHARTER-PROPOSAL.md` (vòng 1–2), theo các lựa chọn của chủ dự án ngày 14/10:
- A (giấy trong 3D) cộng chất in B, rồi C tư liệu đứng riêng;
- sau đó H4: 3D có xương + hậu kỳ toàn khung;
- sau đó H4′: người lớn Quaternius thay cho Kenney chibi.

Số đo dẫn chứng lấy từ `v3/REPORT.md`.

---

## Đ1. Gen hình "thế giới 3D minh hoạ có người" (thay gạch đầu dòng gen 3D của §4)

> - **thế giới 3D là hình chính** (D-010: low-poly, màu kênh, máy quay 3D, ánh sáng theo hồi, không chi tiết trang trí vô nghĩa).
> - **Người** là mô hình 3D có xương, nguồn **CC0** (hiện: Quaternius UBC/UAL [Standard]), đi bằng clip cử động có sẵn.
>   - Mặt là nét vẽ của kênh (`rig.js`), chiếu lên đầu, đổi theo cảm xúc. Không dùng mặt điêu khắc chân thực.
>   - Trang phục theo thời kỳ, làm bằng màu và đạo cụ.
>   - Mang nhãn ILLUSTRATIVE; không mang tên hay diện mạo người thật.
> - **Toàn khung** (người, vật, nhà) đi qua **một hậu kỳ chung**: toon 4 bậc, nét mực 2 px theo depth/normal, bán sắc, vân giấy.
> - **Số** chỉ nằm trên thẻ chữ hoặc đồ thị dựng bằng mã, có dòng nguồn trên hình.

| | |
|---|---|
| **Ưu** | Giữ toàn bộ lợi thế nhà máy: vật thể, góc máy, cache theo cảnh, tất định. Có người với cảm xúc đọc được (ưu tiên số một của §4), thứ mà "nhân vật không mặt" (D-010) thiếu. Cận và trung cận làm được. Một hậu kỳ làm mọi tài sản ngoài ra cùng một chất |
| **Nhược** | Thân Quaternius miễn phí chỉ có tỉ lệ "Superhero": vai rộng, ngực nở, dáng đứng chờ hơi "võ". Phiên che bớt bằng làm phẳng thân thành khối áo và dùng clip đứng nói chuyện, **chưa hết**. Mặt vẽ trên đầu tròn trơn, nhìn gần vẫn có nguy cơ "ma-nơ-canh" (xem tờ khung) |
| **Tác động** | D-010 "nhân vật không mặt" thành "nhân vật có mặt vẽ". Đây là đổi **thể loại**, chủ dự án quyết. `checks/`: các luật giả định không mặt, và chữ trên thẻ 3D nằm trong texture nên không vào log chữ lớp phủ. Gom vào `checks-appeal.md` cho phiên K |
| **Rủi ro** | Giờ máy (Đ4). Người mẫu chung của Quaternius có thể trông giống nhau giữa các kênh khác dùng cùng gói ("inauthentic content", `POLICY.md` §2), nên cần trang phục và mặt riêng của kênh. Gói miễn phí có thể đổi phiên bản, nên giữ SHA-256 trong RIGHTS |

## Đ2. Khi nào dùng
> Dùng cho **chương lịch sử, con người** (quyết định của một hộ, một nhân viên ngân hàng, một đám đông). Chương dữ liệu thuần vẫn là đồ thị và vật thể 3D không người, như hiện nay. Mỗi chương chọn một chế độ, không trộn trong cùng một cảnh.

- **Ưu:** người chỉ xuất hiện ở chỗ mang cảm xúc, nên không tăng giờ máy cho chương số liệu.
- **Nhược:** phải ghi chế độ cho từng chương trong spine.
- **Tác động:** thêm trường `mode: people|world` ở spine (đề xuất cho nhà máy, không làm ở R&D).
- **Rủi ro:** chương lai (có người cộng đồ thị) dễ lố. Đề xuất cắt cảnh rõ khi đổi chế độ.

## Đ3. Ảnh tư liệu: ≤ 6 s, đứng riêng toàn khung
> Tư liệu (RIGHTS §F) chỉ **toàn khung**, **không dán nhân vật lên ảnh**. Mỗi lần ≤ 6 s liền; hoà vào ≥ 0,7 s và hoà ra ≥ 0,8 s về cảnh 3D cùng địa điểm. ≤ 20 % thời lượng tập. Năm và nguồn trên hình. Không đi kèm claim số.

- **Ưu:** người xem thấy thật thời ấy, không lẫn chất liệu. Clip v2 và v3: 4,27 s, 9,1 %.
- **Nhược:** RIGHTS §F3 hiện **ưu tiên** "đặt ảnh trong thế giới". Đề xuất này đảo thứ tự cho chế độ có người.
- **Tác động:** sửa câu §F3 và A39/F15 ở phiên K.
- **Rủi ro:** năm trên ảnh theo catalog có thể lệch năm sự kiện (LoC 1931 so với đóng cửa 12/1930). Bắt buộc đối chiếu nguồn gốc như `v2/CLAIMS.md`.

## Đ4. Luật nguồn và giấy phép mô hình 3D (RIGHTS §F7)
> Repo công khai: chỉ commit tệp **CC0**, có `License.txt` của tác giả. Mỗi gói một dòng RIGHTS §F7, gồm URL tải, câu giấy phép nguyên văn, ngày tải, SHA-256 zip. Tệp không CC0 chỉ tải lúc dựng vào `rnd-hybrid/v3/assets/nonfree/` (đã `.gitignore`). Không mua gói trả phí khi chưa có quyết định. Không dùng Mixamo (cần tài khoản), không dùng mô hình tạo bằng AI, không dùng mô hình người thật.

- **Ưu:** kiểm được, dựng lại được.
- **Nhược:** gói CC0 miễn phí giới hạn (UBC Standard chỉ có Superhero, UAL Standard 43 clip, không có clip "ký").
- **Tác động:** RIGHTS §F7 (đã ghi ở vòng 3).
- **Rủi ro:** nhầm giấy phép khi tác giả đổi bản. Luôn đọc `License.txt` **trong zip** chứ không đọc trang bán.

## Đ5. Chi phí và giờ máy mỗi phút phim (máy hiện tại: 4 lõi, WebGL phần mềm)
| Hướng | Giờ máy / s phim (1080p, 4 worker) | → mỗi phút phim | Chi API |
|---|---|---|---|
| v2 (giấy trong 3D, A + B) | 54 s | ≈ 54 phút | giọng ≈ 0,19 $ / 45 s |
| H4 (Kenney chibi + hậu kỳ) | 35 s | ≈ 35 phút | 0 |
| H4′ (Quaternius + hậu kỳ), đoạn lượn 6 s | 51 s | ≈ 51 phút | 0 |
| clip v3 (H4′, 47 s) | xem `v3/REPORT.md` | | 0 (dùng lại giọng v2) |

> Đề xuất: ghi giờ máy mỗi phút phim vào báo cáo tập, và chặn chế độ "có người" khi một tập 10 phút vượt 10 giờ máy cho đến khi có GPU hoặc tối ưu (bóng 1024, bỏ MSAA, giảm người ở hậu cảnh).

- **Ưu:** chi API gần 0.
- **Nhược:** giờ máy cao với WebGL phần mềm.
- **Tác động:** lịch dựng tập dài hơn.
- **Rủi ro:** máy chung bị chiếm lâu.

## Đ6. Áp thử
> Áp thử Đ1–Đ5 cho **một chương lịch sử của Tập 9 "How the 30-year mortgage was invented"** (≈ 60–90 s). Lời phải đối chiếu nguồn gốc theo `v2/CLAIMS.md`. Phải qua: đọc mù 2 người tắt tiếng (2 lượt, `v3/BLIND.md`), phiếu L3 của chủ dự án ở G2. Nếu hai kết quả kém hơn chương cùng chủ đề dựng bằng thế giới 3D không người thì rút về.

- **Ưu:** đo trên tập thật, quy mô nhỏ, rút lui được.
- **Nhược:** thêm một vòng R&D trong tập.
- **Tác động:** spine Tập 9 cần trường chế độ.
- **Rủi ro:** đọc mù bằng headless là **mô hình đọc, không phải người**. Chỉ dùng để chẩn đoán, không làm cổng (CHARTER §4 chống Goodhart).
