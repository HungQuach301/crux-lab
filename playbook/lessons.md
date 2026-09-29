# Bài học — mọi phiên đọc khi khởi động

Cập nhật: 29/09/2026 (P2). Thêm bài học mới ở cuối mỗi tập; tỉa khi một bài học đã thành luật hoặc hết đúng.

## A. Tập 1 bản cũ (dừng ở Cổng B, 29/09/2026; tag `ep001-v1-stopped`, lưu ở `archive/ep001-v1/`)

| # | Chuyện đã xảy ra | Bài học | Luật bây giờ |
|---|---|---|---|
| A1 | Chất lượng được định nghĩa bằng luật đếm được (wpm mỗi hồi 150–160, cold open ≤ 15 s, ≤ 2 số mới mỗi cảnh, khoảng lặng ≥ 1 s). | Model tối ưu đúng thứ được đếm, không tối ưu thứ người xem cảm. | Số nghề chỉ là **Tham khảo** hoặc cảnh báo (`quality-framework.md` §2–3). |
| A2 | Để kéo wpm vào 150–160: `pauses.js` chèn "..." giả; **104/132 câu** tự đổi từ `eleven_v3` sang `eleven_multilingual_v2` speed 0,70–0,72; thẻ `<break>`. Chủ dự án: *"voice có vấn đề, nhiều đoạn bị cố kéo dài, không ổn định."* | Thủ thuật qua được máy nhưng người nghe thấy ngay. Hai model = hai màu giọng. | G-010. Một model cả tập; không dấu ngắt giả; không giãn; chậm lại bằng khoảng nghỉ giữa câu do dựng đặt. `pauses.js` đã xoá. |
| A3 | Kịch bản M1b lắp từ con số ("vào ngay nhân vật, không bối cảnh, thông tin cụt lủn"). | Số phải đến sau khi người xem cần nó. | G-007, G-008, G-009. Kịch bản viết từ treatment đã duyệt, không từ bảng số. |
| A4 | Storyboard là ảnh tĩnh; duyệt hình bằng ảnh tĩnh. Chủ dự án: *"hình ảnh tĩnh khó hiểu ý nghĩa."* | Hình data-explainer mang nghĩa qua **chuyển động** (cái gì mọc, cái gì cắt nhau). Ảnh tĩnh không kiểm được điều đó. | G-011. Duyệt hình ở animatic có chuyển động (C4), kiểm mù tắt tiếng. |
| A5 | CRITIC (AI) chấm kịch bản 4,71/5; chủ dự án chấm "chưa có kịch bản" (với bản M1b) và dừng ở Cổng B. | Phê bình AI biết người viết muốn gì nên chấm dễ; nó không phải khán giả. | Điểm CRITIC là L2 tham khảo. Cổng qua bằng kiểm mù (agent không ngữ cảnh) + chủ dự án. |
| A6 | Sửa theo máy kiểm: đổi lời 19 câu để S10/S13/S16 qua; cold open bị ép từ 26,65 s xuống 21,94 s và đọc 176 wpm. | Sửa để qua luật làm hỏng câu và nhịp. | Luật chưa phân cấp thì coi là Tham khảo; chỉ Chặn mới buộc sửa. |
| A7 | Cổng B đưa quá nhiều thứ cùng lúc (render? cold open? giọng?) trên một clip 82 s ảnh tĩnh. | Một cổng, một loại quyết định. | 6 cổng; ≤ 3 câu hỏi; clip ≤ 2 phút có chuyển động. |
| A8 | Giữ được: dữ liệu và mô hình (máy kiểm tính lại độc lập 619/619), `numbers.md` với claim ID, ba nhân vật, treatment qua Cổng A, bảng âm S2. | Phần có kiểm độc lập bằng số thì bền. | Tài sản giữ; không làm lại. |
| A9 | fhfa.gov và youtube.com bị proxy chặn; dữ liệu FRED không được commit (repo public, E1-A2). | Ghi nguồn đọc gián tiếp là "đọc qua tìm kiếm"; tải lại bằng `fetch.py --verify`. | DX-H4 theo E1-A2. |
| A10 | "Hiện tại" trong kịch bản trôi theo ngày tải dữ liệu. | Mọi số "hiện tại" phải có **mốc ngày** ghi trong claim và nói ra trong lời hoặc trên màn hình. | C1 chốt mốc ngày. |

## B. Từ Cine Lab (áp được cho Crux)

| # | Bài học | Nguồn | Áp thế nào |
|---|---|---|---|
| B1 | Máy kiểm lời khai thay vì kiểm hình → Goodhart chuyển sang bản khai. | BAI-HOC-BRIEF-D W1 | Đo từ file đã render. |
| B2 | Chỉ tiêu số lượng cho kỹ thuật nghệ thuật khuyến khích nhồi. | W2 | Không quota; mỗi kỹ thuật có lý do. |
| B3 | Luật không phân cấp → sửa lỗi dễ trước, bỏ lỗi quan trọng. | W3 | Chặn / Chính / Tham khảo (K3). |
| B4 | Máy chưa hiệu chuẩn với mắt người → "đạt 71/71" mà phim vẫn dở. | W4 | Luật không phân biệt được bản tốt và bản kém thì hạ cấp. |
| B5 | Một người chấm, không mù → thiên lệch người trong cuộc. | W5 | Kiểm mù ở mọi cổng, agent mới, một file tên ngẫu nhiên, câu hỏi cố định, ghi nguyên văn. |
| B6 | Khoá cứng mà không có người phán quyết khiếu nại. | W6 | Khiếu nại luật đưa lên gói quyết định của cổng kế tiếp. |
| B7 | Phiên kiểm và phiên dựng cùng model → điểm mù chung. | W7 | Khi có thể, kiểm chéo số liệu bằng mã độc lập hoặc nhà cung cấp khác. |
| B8 | Kiểm mù mặt Ida: 2 vòng sửa cùng một trục vẫn 9/10 "búp bê" (đối chứng 0/10). Dừng sau 2 vòng, đưa 3 phương án kèm khuyến nghị. | `reports/m2/MAT-IDA-AI.md` | Tối đa 2 vòng sửa–kiểm; sau đó đưa phương án, kể cả phương án đổi hướng kỹ thuật. |
| B9 | Kiểm mù cần **đối chứng** (mẫu chuyên nghiệp) để biết câu hỏi phân biệt được. | MAT-IDA §1 | Mỗi đợt kiểm mù có ít nhất một mẫu đối chứng khi có mẫu hợp pháp để dùng. |
| B10 | Ảnh tĩnh không đo được cảm xúc đến từ giọng và chuyển động (PA2 "khó đọc" ở ảnh tĩnh, chưa đo khi có tiếng). | MAT-IDA §2 | Duyệt hình bằng clip có chuyển động (G-011). |
| B11 | Truyện phải chốt ở animatic, trước khi tốn công dựng. | KHUNG-CHAT-LUONG §3 | C4 trước C5. |
| B12 | Mọi quyết định sáng tạo ghi AUTHORSHIP kèm đóng góp biểu đạt cụ thể của con người; mọi tài sản vào RIGHTS với nguồn, giấy phép (trích nguyên câu), phạm vi. | CLAUDE.md, AUTHORSHIP.md, RIGHTS.md | `AUTHORSHIP.md`, `RIGHTS.md` ở gốc repo. |

## B2. Bộ đo kiểm mù (Tập 1, C1–C2)

| # | Chuyện đã xảy ra | Bài học |
|---|---|---|
| M1 | Hỏi "muốn xem" từng bản riêng: người đọc vai khán giả đích nói "Yes" với mọi bản (kể cả đối chứng yếu 5/5). | Câu hỏi riêng lẻ bị trần: không phân biệt được. Dùng so cặp ép chọn. |
| M2 | So cặp: đối chứng yếu thắng 19/19 ở cả hai vị trí. P2 ghi "không đạt → C"; chủ dự án sửa: bộ đo đã phân biệt được, chỉ là ứng viên thua. | Tiêu chí "không đạt" phải tách **"không phân biệt được"** với **"ứng viên thua"**. Một bộ đo cho kết quả trái ý đồ vẫn có thể là bộ đo tốt. |
| M3 | Câu hỏi "hiểu" (tóm tắt + đáp án): kịch bản M1b bị chủ dự án chê vẫn được hiểu 3/3. | "Hiểu được" là điều kiện cần, không nói kịch bản hay. Tín hiệu phân biệt nằm ở "chỗ mất chú ý" và "chỗ khó hiểu". |
| M4 | Người đọc vai khán giả đích chọn bản nói với "người như tôi" và cho sẵn ngưỡng tự đối chiếu. | Khớp nhận xét M1 của chủ dự án (G-008) → G-013. |

## C. Vận hành

- Chủ dự án không đọc tài liệu dài; chỉ trả lời gói quyết định (≤ 3 câu, < 1 phút đọc).
- Gu (truyện, giọng, hình, âm sắc, nhạc) không bao giờ tự quyết.
- ElevenLabs: tính ký tự mỗi bước vào ledger tập.
