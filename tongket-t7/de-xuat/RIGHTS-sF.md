# Đề xuất thêm `RIGHTS.md` §F — Footage ngoài (tongket-t7, chưa áp)

## F1. Danh sách trắng (theo thứ tự ưu tiên; dùng bậc có **số nhỏ nhất** có hình phù hợp)
| Bậc | Nguồn | Giấy phép | Phải kiểm từng tệp | Ghi trên hình / mô tả |
|---|---|---|---|---|
| 1 | **Tác phẩm của nhân viên chính phủ liên bang Mỹ** khi làm nhiệm vụ (17 U.S.C. §105: NASA, NOAA, USGS, các bộ ngành) | phạm vi công cộng | ảnh do nhà thầu/bên thứ ba chụp **không** thuộc §105 → chỉ dùng tệp cơ quan ghi rõ "public domain". **Tư liệu NARA/LoC phần lớn không phải tác phẩm §105**: tệp ghi "No known restrictions" chỉ là **đánh giá của tổ chức, không bảo đảm** → xếp bậc 3, lưu bản chụp nhãn quyền (URL + ngày + băm), ghi "đánh giá của tổ chức" trong RIGHTS; **không** dùng phù hiệu, logo cơ quan (vd NASA insignia bị hạn chế); không dùng ảnh của chính quyền bang (luật khác nhau) | "Source: <cơ quan>, <năm>" |
| 2 | **Natural Earth** (bản đồ) · **Census TIGER/Line** · **OpenStreetMap dữ liệu** | Natural Earth: phạm vi công cộng · TIGER: phạm vi công cộng · OSM: **ODbL** (dữ liệu) | OSM: chỉ dùng **dữ liệu**, tự vẽ bằng màu kênh (thành sản phẩm từ dữ liệu, ghi công); **không** dùng ô bản đồ (tile) của OSM, vì phần đồ hoạ tile là BY-SA | OSM: "© OpenStreetMap contributors" trên hình + mô tả |
| 3 | **CC0 / Public Domain Mark** (Smithsonian Open Access, Met Open Access, Wikimedia Commons tệp ghi CC0/PD) | CC0 / PDM | đọc trang tệp, không đọc trang bộ sưu tập; PDM chỉ hợp lệ khi tổ chức gắn nhãn có thẩm quyền | "Source: <tổ chức>, <năm>" |
| 4 | **Pexels / Pixabay** | giấy phép riêng của nền tảng (không phải CC0): cho dùng thương mại, không bắt ghi công | **đọc giấy phép lúc tải** và lưu bản chụp (URL + ngày + băm SHA-256 của văn bản giấy phép); loại ảnh có người nhận ra được mặt, logo/nhãn hiệu, tác phẩm nghệ thuật, ảnh gắn nhãn tạo bằng AI | "Photo: <tác giả>/<nền tảng>" (tự nguyện) + năm nếu biết; không biết năm → không dùng làm tư liệu có năm |
| 5 | **CC BY** (4.0 ưu tiên) | CC BY | ghi công đủ TASL (tiêu đề, tác giả, nguồn, giấy phép); không cắt xén làm đổi nghĩa | ghi công trên hình hoặc trong mô tả + RIGHTS |

## F2. Danh sách cấm
CC **NC** (phi thương mại: kênh có quảng cáo) · CC **ND** (không cho chỉnh sửa: kênh luôn phủ tông, cắt, thêm chuyển động) · **CC BY-SA cho hình/video** (điều khoản chia sẻ tương tự lan sang tác phẩm ghép) · quyền **không rõ** hoặc không trích được văn bản giấy phép · **logo, nhãn hiệu, giao diện sản phẩm** · **người thật trong vai nhân vật** (nhân vật kênh là ILLUSTRATIVE, không mặt) · đoạn của kênh YouTube khác, đài tin tức, "nhúng miễn phí" của kho ảnh thương mại · ảnh/video tạo bằng AI trình bày như tư liệu.

## F3. Trần và cách ghép (giữ ngôn ngữ hình kênh — cine-lab #49, #50, #93)
- **Trần:** ≤ 20 % thời lượng tập (Tập 8 thử ≤ 15 %); mỗi lần ≤ 6 s liền; không mở tập (5 s đầu ở thế giới — quy tắc 7) và không trùng số neo.
- **Chuyển động:** luôn có chuyển động máy (đẩy/lia chậm); điểm chính của ảnh (`focus`) nằm **trên** dải chú thích, rà một khung mỗi ảnh trước khi dựng (cine #49).
- **Tông:** phủ bảng màu kênh (grade về token + hạt nhẹ), không để màu ảnh gốc đứng riêng.
- **Hoà từ 3D:** mở đoạn bằng cảnh 3D nối tiếp rồi hoà ≥ 0,8 s (cine #93: cắt thẳng 3D ↔ ảnh thì 2/3 người xem nói "đổi chất liệu", kể cả khi có hoà 1,4 s). **Ưu tiên đặt ảnh trong thế giới** (tờ ảnh trên bàn, màn hình, bảng) hơn là toàn khung.
- **Dòng nguồn:** nguồn ảnh bên phải, nguồn số bên trái, cùng trên dải chú thích; không để một dòng che dòng kia (cine #50, #68).

## F4. Trung thực
- Ảnh minh hoạ **không làm bằng chứng**: không đi cùng claim số; mang nhãn minh hoạ khi không phải tư liệu đúng sự kiện.
- Tư liệu (`archival`) ghi **năm + nguồn trên hình**; năm không xác minh được → không dùng.
- Bản đồ tự vẽ từ dữ liệu ghi nguồn dữ liệu và năm của dữ liệu.

## F5. Thủ tục
1. Ghi dòng RIGHTS **trước khi** dựng (mã `X-<tập>-<n>`, URL tệp, giấy phép trích nguyên văn + link, ngày tải, bậc 1–5, phạm vi YT).
2. Lưu tệp gốc ngoài git (`work/external/`); trong repo chỉ có RIGHTS + băm SHA-256.
3. Checks A39 chặn khi thiếu hồ sơ, giấy phép cấm hoặc vượt trần. Ngoài danh sách trắng → **hỏi chủ dự án** (ngoại lệ pháp lý, CHARTER §5).
