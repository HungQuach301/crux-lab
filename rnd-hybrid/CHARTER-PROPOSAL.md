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

---

## B. Vòng 2 (14/10/2026) — đề xuất "gen lai A+C" (thay mục A ở trên, theo lựa chọn của chủ dự án 14/10)

Phiên **không áp dụng**. Sửa CHARTER là việc của chủ dự án (§6). Mục A ở trên đề xuất chế độ (b) "cắt giấy 2D". Chủ dự án đã chọn hướng khác: **giấy trong thế giới 3D** (khung A), cộng chất in của khung B, cộng tư liệu đứng riêng (khung C). Đề xuất mới như sau.

**Thay gạch đầu dòng gen 3D trong §4 bằng:**
> - **thế giới 3D tối giản là hình chính** (D-010: low-poly, màu kênh, không chân thực ảnh, máy quay 3D, ánh sáng theo hồi, không chi tiết trang trí vô nghĩa).
>   Nhân vật và đạo cụ **có thể là tấm giấy cắt** đứng trong thế giới đó:
>   - tấm phẳng có độ dày, đổ bóng thật;
>   - mặt in nét mực, bán sắc, vân giấy;
>   - nhân vật **có mặt biểu cảm** (rig vẽ bằng mã), rõ là hoạt hình, mang nhãn ILLUSTRATIVE, không mang tên hay diện mạo người thật, không ảnh/video do AI sinh.
>
>   Số luôn nằm trên thẻ/đồ thị dựng bằng mã, có dòng nguồn trên hình.
> - **tư liệu** (RIGHTS §F) chỉ đứng riêng **toàn khung**:
>   - không dán nhân vật lên ảnh;
>   - ≤ 6 s mỗi lần, ≤ 20 % thời lượng;
>   - hoà vào và hoà ra ≥ 0,7 s về cảnh 3D cùng địa điểm;
>   - có năm và nguồn trên hình;
>   - không làm bằng chứng cho số.

**Vì sao (số đo vòng 2, `REPORT.md` §vòng 2):** mọi lợi thế của nhà máy vẫn giữ được: vật thể 3D, góc máy, ánh sáng theo hồi, cache theo cảnh, tất định. `render_shots.js` của nhà máy dùng nguyên trạng. Phần mới chỉ là một mẫu cắm `rnd-hybrid/v2/` (≈ 450 dòng). Cảm xúc nhân vật (ưu tiên số một của §4) có thêm nhờ mặt biểu cảm. Tư liệu thật đứng riêng nên tránh được lỗi "ghép chất liệu" của khung C.

**Đánh đổi:**
- **Thẩm mỹ:** chưa có số đo đối chứng. Đọc mù 2 người chưa chạy (`blind/PHIEU-v2.md`). Điều kiện duyệt là đọc mù cộng phiếu L3 trên một chương thử.
- **Thời gian máy:** cao hơn 2D (xem REPORT).
- **Thể loại:** "nhân vật không mặt" (D-010) trở thành "nhân vật giấy có mặt". Đây là thay đổi thể loại, phải do chủ dự án quyết.

**Việc kéo theo (không làm ở phiên này):**
1. `checks-appeal.md` gom các luật sau cho phiên K:
   - luật giả định nhân vật không mặt;
   - trang kiểm `window.CHECKS` cho thẻ giấy 3D (chữ trên texture chưa vào log chữ của lớp phủ);
   - F13/F15 hiểu "toàn khung + hoà ≥ 0,7 s" thay cho "đặt ảnh trong thế giới" (§F3 hiện ưu tiên ảnh nằm trong thế giới).
2. RIGHTS §F3: thêm dòng "chế độ lai: ảnh đứng riêng toàn khung, không ghép nhân vật".
3. Chuyển `rnd-hybrid/v2/{paper3d,illus2d}.js` và `cutout/rig.js` vào `toolkit/` khi đã dùng ở ≥ 1 tập (CHARTER §2.1).
