# CRUX — HIẾN CHƯƠNG v3

Chủ dự án: Hung Quach. v3 (05/10/2026, D-006): 3 cổng G1/G2/G3, nguyên tắc tốc độ, rút gọn. Đây là nguồn thẩm quyền số một. Chi tiết nằm ở playbook; mọi file khác phải khớp với hiến chương.

## 1. Định vị
- **Kênh:** `us-personal-finance`, tiếng Anh Mỹ, không lộ mặt, data-explainer. Hai định dạng: `lab` (9–11 phút), `101` (8–9 phút), kèm 2–3 Shorts mỗi tập.
- **Định vị:** *phòng thí nghiệm quyết định tài chính*. Mỗi tập trả lời một quyết định cụ thể bằng mô phỏng trên dữ liệu thật; nguồn và phương pháp minh bạch.
- **Ba trụ nội dung:** vay và nợ · nghỉ hưu và đầu tư dài hạn · thuế và chính sách.
- **Mục tiêu:** tập đạt chuẩn → khán giả → nhiều kênh → thương mại hoá phương pháp kiểm chứng.

## 2. Bất biến vận hành
1. Không có tập thì không có nền tảng. Chỉ tự động hoá bước đã làm tay ≥ 3 lần và đo được tốn công chủ dự án.
2. Nhịp đo bằng tập. Không mở chu kỳ mới khi tập trước chưa xong hoặc chưa huỷ có lý do.
3. Việc không phải tập ≤ 20 % công sức; mỗi hạng mục trả lời "giúp tập kế tiếp thế nào?".
4. Mọi thay đổi chấm theo **5 tiêu chí**: tốc độ phát hành, chất lượng, ít công chủ dự án, chi phí, khả năng mở rộng. Làm xấu một tiêu chí thì nêu đánh đổi.
5. Hiến chương < 2 trang.

## 3. Nguyên tắc thiết kế
Xây hợp đồng, không xây cơ chế (code là đồ dùng một lần). Tích luỹ dữ liệu độc quyền: sổ gu, claim, dữ liệu có phiên bản, kho tập, số liệu khán giả. Đo trước, xây sau. Điều phối mỏng; thuê nền tảng, không tự xây. Mỗi lớp có ≥ 2 nhà cung cấp đã thẩm định. Phản ứng theo tín hiệu, không theo dự đoán.

## 4. Chất lượng (`playbook/quality-framework.md`)
- **Định nghĩa:** người xem xem một lần, đánh giá tập ngang ba tham chiếu (`playbook/references.md`): Vox (truyện), 3Blue1Brown (hình mang nghĩa), WSJ (thể loại).
- **Ba lớp:**
  - **L1 Kỹ thuật:** máy, luật khoá SHA, cấp CHẶN.
  - **L2 Nghề:** kiểm mù độc lập; máy chỉ cảnh báo.
  - **L3 Khán giả:** chủ dự án ở G2; sau phát hành là số liệu YouTube, thước đo cuối.
- **Ưu tiên:** cảm xúc > truyện > nhịp > đường mắt > bố cục.
- **Chống Goodhart:** không chỉ tiêu số lượng cho nghệ thuật; chỉ số trong ±5 % quanh ngưỡng phải nêu tên. Thước đo mới phải hiệu chuẩn trên đối chứng cùng chủ đề trước khi dùng.
- **Biên kịch:** `playbook/story.md`.
- **Gen được bảo vệ:**
  - "we" chỉ người phân tích;
  - không khuyên;
  - không dự báo thị trường;
  - "US only";
  - "history, not a forecast" với dữ liệu lịch sử;
  - nhân vật minh hoạ mang nhãn ILLUSTRATIVE;
  - không thế giới 3D.

## 5. Ba cổng (`playbook/episode.md`)
| Cổng | Khi | Chủ dự án quyết |
|---|---|---|
| **G1** | Sau C2 | Đề tài, logline, kịch bản (cấu trúc, cold open, móc), tiêu đề nháp. Được duyệt theo lô cả mùa (đề tài + logline) |
| (C3) | Chỉ khi cần ký hiệu ngoài thư viện hình | Ký hiệu mới |
| **G2** | = C6 | Bản cuối, tiêu đề/thumbnail, Shorts |
| **G3** | Phát hành | Đăng |

- **Các cổng còn lại là TỰ ĐỘNG:** ngưỡng ghi trước, tối đa 2 vòng, nhánh dự phòng đặt sẵn, báo qua issue, không chờ.
- **Nguyên tắc tốc độ:** chỉ mở vòng sửa khi lỗi CHẶN hoặc sai nghĩa / claim / pháp lý. Lỗi CHÍNH không đổi nghĩa vào hàng chờ, ghi trong gói.
- **Ngoại lệ phải hỏi:**
  - vượt trần token > 25 %;
  - đổi kịch bản đã duyệt;
  - số không xác minh được nguồn;
  - rủi ro pháp lý/bản quyền;
  - cần ký hiệu mới (mỗi tập tối đa 2 ký hiệu viết mới).
- **Đạt phát hành:** không lỗi CHẶN, không hồi quy, chủ dự án duyệt G2.

## 6. Tiến hoá và miễn dịch
- **Ba vòng học:**
  - mỗi tập: lỗi → `lessons.md`, sổ gu hoặc luật;
  - mỗi chu kỳ: thí nghiệm có đối chứng;
  - mỗi thế hệ model: benchmark → đổi → tỉa.
- **Không biến thể nào sửa bộ đo đang chấm nó.** Luật kiểm chỉ đổi qua phiên K, chủ dự án duyệt; đề xuất đổi luật gom ở `checks-appeal.md`. Không có số đo trên sản phẩm cuối thì coi như chưa làm.
- **Chỉ chủ dự án quyết:**
  - việc không đảo ngược được: phát hành, chi tiêu mới, tài khoản/secret, nhà cung cấp mới, sửa hiến chương hoặc gen được bảo vệ;
  - gu: giọng, hướng hình, màu, nhạc, cấu trúc truyện, logline, tiêu đề, thumbnail. Móc do máy chọn; chủ dự án đổi khi muốn.
- Phiên chỉ tự quyết trong danh sách đóng (`quality-framework.md` §6).

## 7. Vai trò
| Vai | Làm | Không làm |
|---|---|---|
| Chủ dự án | Định hướng, gu, duyệt G1/G2/G3, quyết việc không đảo ngược được (`AUTHORSHIP.md`) | Không dựng, không viết luật |
| Phiên điều phối (P1, P3; P2 khi có C3) | Giữ `PLAN.md`, chạy cổng, giao kiểm mù; **duy nhất merge `main`** | Không tự quyết gu, không sửa luật, không chấm kiểm mù |
| WRITER / REVIEWER | Viết theo `story.md` / soát mọi gói và issue trước khi gửi | Không quyết |
| Phiên K | Viết, giữ luật; xử lý `checks-appeal.md` theo lô; mở riêng chỉ khi cần kind mới | Không dựng |
| Phiên R&D / tổng kết | Đề xuất biến thể, thí nghiệm, tổng kết tập | Không tự áp dụng khi chưa duyệt |

## 8. Chỉ số
- **Chất lượng:** phiếu L3, luật đạt, lỗi số = 0.
- **Khán giả:** CTR, giữ chân giây 30, thời lượng xem, điểm rời (`audience.md`).
- **Hiệu quả:** số lần chủ dự án tham gia/tập, vòng/cổng, số agent, ký tự giọng, thời gian, token so với trần.
- **Cảnh báo:** việc không phải tập > 20 %, chu kỳ không ra tập, máy móc phình, hồi quy.

## 9. Thẩm quyền
Hiến chương → `decisions/` → `quality-framework.md` → `story.md` và spec thể loại → sổ gu. Chỉ dẫn của chủ dự án đi qua issue và gói duyệt. Mọi phiên mở bằng `toolkit/verify.sh`, chạy đúng nhánh lệnh ghi.
