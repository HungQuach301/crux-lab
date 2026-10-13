# CRUX — HIẾN CHƯƠNG v5

Chủ dự án: Hung Quach. v3 (05/10/2026, D-006): 3 cổng G1/G2/G3, rút gọn. v4 (06/10/2026, D-009, D-010): chất lượng là ưu tiên tuyệt đối; thế giới 3D tối giản. v5 (13/10/2026, D-013): mô hình xưởng 6 mốc, 1 Short, không thumbnail, footage ngoài có trần. Đây là nguồn thẩm quyền số một. Chi tiết nằm ở playbook; mọi file khác phải khớp với hiến chương.

## 1. Định vị
- **Kênh:** `us-personal-finance`, tiếng Anh Mỹ, không lộ mặt, data-explainer. Ba định dạng: `lab` (9–11 phút), `101` (8–9 phút), `deep` (14–17 phút, chỉ khi đủ ba điều kiện không độn và nhà máy đạt nhịp hình trước — D-012, `episode.md` §9), kèm **1 Short** mỗi tập (D-013).
- **Định vị:** *phòng thí nghiệm quyết định tài chính*. Mỗi tập trả lời một quyết định cụ thể bằng mô phỏng trên dữ liệu thật; nguồn và phương pháp minh bạch.
- **Ba trụ nội dung:** vay và nợ · nghỉ hưu và đầu tư dài hạn · thuế và chính sách.
- **Mục tiêu:** tập đạt chuẩn → khán giả → nhiều kênh → thương mại hoá phương pháp kiểm chứng.

## 2. Bất biến vận hành
1. Không có tập thì không có nền tảng. Chỉ tự động hoá bước đã làm tay ≥ 3 lần và đo được tốn công chủ dự án.
2. Nhịp đo bằng tập. Không mở chu kỳ mới khi tập trước chưa xong hoặc chưa huỷ có lý do.
3. Việc không phải tập ≤ 20 % công sức; mỗi hạng mục trả lời "giúp tập kế tiếp thế nào?".
4. Mọi thay đổi chấm theo **5 tiêu chí**: tốc độ phát hành, chất lượng, ít công chủ dự án, chi phí, khả năng mở rộng. Làm xấu một tiêu chí thì nêu đánh đổi. **Chất lượng là ràng buộc, không phải tiêu chí để đổi chác** (D-009): nội dung, hình, âm và sự liền mạch giữa chúng không bao giờ bị hy sinh; tốc độ, chi phí, công chủ dự án chỉ tối ưu khi số đo trên sản phẩm cuối (có đối chứng) chứng minh chất lượng không giảm.
5. Hiến chương < 2 trang.

## 3. Nguyên tắc thiết kế
Xây hợp đồng, không xây cơ chế (code là đồ dùng một lần). Tích luỹ dữ liệu độc quyền: sổ gu, claim, dữ liệu có phiên bản, kho tập, số liệu khán giả. Đo trước, xây sau. Điều phối mỏng; thuê nền tảng, không tự xây. Mỗi lớp có ≥ 2 nhà cung cấp đã thẩm định. Phản ứng theo tín hiệu, không theo dự đoán.

## 4. Chất lượng (`playbook/quality-framework.md`)
- **Định nghĩa:** người xem xem một lần, đánh giá tập ngang ba tham chiếu (`playbook/references.md`): Vox (truyện), 3Blue1Brown (hình mang nghĩa), WSJ (thể loại).
- **Ba lớp:**
  - **L1 Kỹ thuật:** máy, luật khoá SHA, cấp CHẶN.
  - **L2 Nghề:** kiểm mù độc lập (headless, chỉ giữ vòng từng đổi quyết định; móc đo bằng mốc giây ở C2); máy chỉ cảnh báo; lượt đạo diễn máy là công cụ chẩn đoán, không phải ngưỡng (D-010 §6).
  - **L3 Khán giả:** phiếu L3 của chủ dự án ở G2 là **thước đo cuối trước phát hành**; sau phát hành là số liệu YouTube.
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
  - thế giới 3D tối giản: low-poly, màu kênh, không chân thực ảnh, nhân vật không mặt, không chi tiết trang trí không mang nghĩa (D-010). **Thế giới 3D là hình chính;**
  - **footage ngoài** (ảnh, video, bản đồ) chỉ làm **tư liệu**, không thay thế thế giới: chỉ nguồn trong danh sách trắng `RIGHTS.md` §F, ≤ 20 % thời lượng (trần riêng từng tập ở §F), mỗi lần ≤ 6 s liền, luôn có chuyển động, hoà từ cảnh 3D hoặc đặt trong khung của thế giới, phủ tông kênh; **năm + nguồn trên hình**; ảnh minh hoạ **không làm bằng chứng** cho số; không người thật trong vai nhân vật (D-013).

## 5. Ba cổng (`playbook/episode.md`)
| Cổng | Khi | Chủ dự án quyết |
|---|---|---|
| **G1** | Sau tiền kỳ (M2) | Đề tài, logline, kịch bản (cấu trúc, mở đầu, chương, kết), **vật thể + animatic** (thay C3), tiêu đề. Đề tài + logline duyệt theo lô cả mùa |
| **G2** | Sau kiểm định trên nháp (M5) | Bản nháp 540p (phiếu L3), Short (mô tả + mốc). Không thumbnail; mô tả/chương/tag do máy viết ở M6 |
| **G3** | Sau 1080p một lần (M6) | Đăng |

- **Các bước còn lại là TỰ ĐỘNG** (6 mốc, `episode.md` §1): ngưỡng ghi trước, **tối đa 2 vòng mỗi lỗi**, nhánh dự phòng đặt sẵn, không chờ.
- **Chất lượng trước (D-009):** lỗi CHÍNH phải sửa trước phát hành. Ngoại lệ duy nhất: sửa làm hỏng một yếu tố chất lượng khác — gói nêu yếu tố đó, kèm số đo hoặc bản trước/sau, chủ dự án chọn.
- **Token:** trần chỉ để cảnh báo; vượt thì báo số thực trong gói; không cắt bước chất lượng (kiểm mù, lượt đạo diễn, REVIEWER) vì token. Cảnh báo thêm: đọc cache ≤ 60 triệu/tập, ≤ 150 lượt/phiên (D-013).
- **Ngoại lệ phải hỏi:**
  - đổi kịch bản đã duyệt;
  - số không xác minh được nguồn;
  - rủi ro pháp lý/bản quyền;
- **Đạt phát hành:** không lỗi CHẶN, không lỗi CHÍNH chưa sửa, không hồi quy, phiếu L3 của chủ dự án **≥ 4 ở mọi dòng** (dòng < 4 → sửa rồi chấm lại; ngoại lệ chủ dự án ghi lý do ở `gates/G2.md` và sổ gu).

## 6. Tiến hoá và miễn dịch
- **Ba vòng học:**
  - mỗi tập: lỗi → `lessons.md`, sổ gu hoặc luật;
  - mỗi chu kỳ: thí nghiệm có đối chứng;
  - mỗi thế hệ model: benchmark → đổi → tỉa.
- **Không biến thể nào sửa bộ đo đang chấm nó.** Luật kiểm chỉ đổi qua phiên K, chủ dự án duyệt; đề xuất đổi luật gom ở `checks-appeal.md`. Không có số đo trên sản phẩm cuối thì coi như chưa làm.
- **Chỉ chủ dự án quyết:**
  - việc không đảo ngược được: phát hành, chi tiêu mới, tài khoản/secret, nhà cung cấp mới, sửa hiến chương hoặc gen được bảo vệ;
  - gu: giọng, hướng hình, màu, nhạc, cấu trúc truyện, logline, tiêu đề. Móc do máy chọn; chủ dự án đổi khi muốn.
- Phiên chỉ tự quyết trong danh sách đóng (`quality-framework.md` §6).

## 7. Vai trò
| Vai | Làm | Không làm |
|---|---|---|
| Chủ dự án | Định hướng, gu, duyệt G1/G2/G3, quyết việc không đảo ngược được (`AUTHORSHIP.md`) | Không dựng, không viết luật |
| Phiên điều phối (mỗi chặng một phiên ngắn tới cổng kế, mở bằng "Chạy Tập N" — D-011, D-013) | Giữ `PLAN.md`, chạy cổng, giao kiểm mù; đóng bằng PLAN ≤ 1 trang; **duy nhất merge `main`** | Không tự quyết gu, không sửa luật, không chấm kiểm mù |
| WRITER / REVIEWER | Viết theo `story.md` / soát gói G1, ý đồ kiểm định, gói G2 | Không quyết |
| Vai xưởng (D-013): Đạo diễn sáng tạo, Thiết kế hình, Previz, Editor, Giám sát liền mạch, Line producer | Mỗi vai một đầu bài headless, một phép thử riêng (`episode.md` §1a) | Không quyết gu, không đổi kịch bản đã duyệt |
| Phiên K | Viết, giữ luật; xử lý `checks-appeal.md` theo lô; mở riêng chỉ khi cần kind mới | Không dựng |
| Phiên R&D / tổng kết | Đề xuất biến thể, thí nghiệm, tổng kết tập | Không tự áp dụng khi chưa duyệt |

## 8. Chỉ số
- **Chất lượng:** phiếu L3, luật đạt, lỗi số = 0.
- **Khán giả:** CTR, giữ chân giây 30, thời lượng xem, điểm rời (`audience.md`).
- **Hiệu quả:** số lần chủ dự án tham gia/tập (kèm phút), vòng/cổng, số agent, ký tự giọng, thời gian, token thực đọc từ log phiên (trần = đầu vào mới + sinh ra, đọc cache, lượt/phiên, so với mức cảnh báo), giờ render.
- **Cảnh báo:** việc không phải tập > 20 %, chu kỳ không ra tập, máy móc phình, hồi quy.

## 9. Thẩm quyền
Hiến chương → `decisions/` → `quality-framework.md` → `story.md` và spec thể loại → sổ gu. Chỉ dẫn của chủ dự án đi qua issue và gói duyệt. Mọi phiên mở bằng `toolkit/verify.sh`, chạy đúng nhánh lệnh ghi.
