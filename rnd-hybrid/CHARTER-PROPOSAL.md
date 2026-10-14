# Đề xuất sửa CHARTER §4 (gen được bảo vệ) — rnd-hybrid, 14/10/2026

Phiên R&D **không áp dụng**: sửa hiến chương / gen được bảo vệ là việc chỉ chủ dự án quyết (CHARTER §6). Dưới đây là văn bản đề xuất, sẵn để dán
nếu duyệt, kèm điều kiện và việc kéo theo ở `checks/` (gom sang `checks-appeal.md` cho phiên K, phiên này không chạm `checks/`).

## A. Mở rộng gen hình — "chế độ hình lai"
**Hiện tại (§4, gạch đầu dòng gen):** "thế giới 3D tối giản: low-poly, màu kênh, không chân thực ảnh, nhân vật không mặt, không chi tiết trang trí không
mang nghĩa (D-010). **Thế giới 3D là hình chính;**"

**Đề xuất thay bằng:**
> - **hình kênh có hai chế độ, mỗi chương chọn một:** (a) thế giới 3D tối giản (D-010: low-poly, màu kênh, không chân thực ảnh, nhân vật không mặt);
>   (b) **hình lai**: dữ liệu dựng bằng code + tư liệu phạm vi công cộng (RIGHTS §F, năm + nguồn trên hình) + **nhân vật cắt giấy do Claude vẽ bằng
>   SVG** (thư viện `toolkit/cutout`, có mắt/miệng biểu cảm, màu kênh, rõ là hoạt hình, mang nhãn ILLUSTRATIVE, **không** mang tên/diện mạo người
>   thật, không ảnh/video do AI sinh). Cảnh có số luôn là cảnh dữ liệu dựng bằng code; nhân vật và sticker không mang số chưa có claim. Không trang
>   trí không mang nghĩa ở cả hai chế độ.

**Vì sao (số đo của phiên, `REPORT.md`):** clip thử 46,9 s dựng 100 s máy ở 1080p (≈ 2,2 s máy/s phim, 4 lõi), tất định trùng byte, cảnh trung vị
2,79 s (17 cảnh) — nhịp gần tham chiếu GoDocs (1,9 s) mà không cần khung 3D; chi API 666 ký tự giọng; 0 $ nhà cung cấp hình. Nhân vật có biểu cảm
mang được **cảm xúc** (ưu tiên số một của §4) ở những chương lịch sử/con người mà vật thể 3D không mặt mang khó.

**Đánh đổi (5 tiêu chí):** tốc độ ↑ (cảnh 2D không cần spine/3D), chi phí ↓, mở rộng ↑ (chữ trên hình dịch được → bản địa hoá); **chất lượng: chưa
có số đo đối chứng** (đọc mù 2 người tắt tiếng chưa chạy) → điều kiện duyệt là đọc mù + phiếu L3 trên một chương thử; rủi ro "inauthentic content"
của YouTube tăng nếu khuôn mẫu lặp (`POLICY.md` §2). Công chủ dự án: +1 lần tải ảnh tư liệu/tập cho tới khi mở host LoC/NARA.

**Việc kéo theo (không làm ở phiên này):**
1. `checks-appeal.md`: luật nào giả định "nhân vật không mặt"/"thế giới 3D là hình chính" (tỉ lệ chế độ, R08/R09 bản đồ liền mạch, F13/F15 footage)
   cần biết chế độ (b); trang kiểm `window.CHECKS` cho mẫu `cutout`/`archival` (hiện chỉ engine 2D ghi log chữ thẳng; sticker xoay vẽ thẳng lên canvas,
   chưa vào log).
2. `RIGHTS.md` §F3 "hoà từ 3D ≥ 0,8 s": trong chế độ (b) ảnh nằm trên bàn giấy (cùng chất liệu) — cần quy tắc riêng, đo bằng cine.
3. `playbook/references.md`: thêm GoDocs (nhịp, nhân vật lịch sử có cảm xúc, móc chuỗi thất bại) và Fortune of Nations (bản đồ, sticker, bảng điểm) làm
   tham chiếu **công thức**, không sao chép (như D-013 §5).
4. Chuyển `rnd-hybrid/cutout/` → `toolkit/cutout/` khi đã dùng ở ≥ 1 tập (CHARTER §2.1).

(Thumbnail: chủ dự án 14/10 giữ quyết định **không thumbnail** (D-013 mục 2) — phần đề xuất thumbnail đã bỏ.)
