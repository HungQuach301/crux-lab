# Cổng Mốc 3 — báo cáo sẵn sàng (bốn điều kiện đầu vào)

Phiên D1, 2026-09-28. Chi tiết và bằng chứng: [`moc-3-inventory.md`](moc-3-inventory.md). Định nghĩa: [`moc-3.md`](moc-3.md). Tài sản đã chuyển: [`../topic/README.md`](../topic/README.md), 242/242 test đạt.

## Bảng sẵn sàng

| # | Điều kiện đầu vào | Ngưỡng | Hiện có | Đạt? | Việc tối thiểu để đóng | Công sức ước lượng |
|---|---|---|---|---|---|---|
| 1 | Kho ảnh chụp | ≥ 30 chuỗi, ≥ 4 nhà cung cấp, phát hiện thay đổi chạy | **0 chuỗi thật.** Adapter FRED/BLS/Census chưa nối mạng. `diffSnapshots` và nội dung issue chạy như hàm thuần; chưa có lượt chạy định kỳ. | **THIẾU** | (a) Chủ dự án mở domain: `api.stlouisfed.org` (hoặc dùng `fredgraph.csv`, đã chạy được), `api.bls.gov`, `api.census.gov`, và một nhà cung cấp thứ tư trong danh sách trắng nhóm 1–2; cấp khoá nếu cần. (b) Viết `transport` thật và một lệnh `snapshot fetch` ghi `data/snapshots/{publisher}/{seriesId}/{asOfDate}.json`. (c) Chọn 30 chuỗi từ `topic-source-map.md` cho 8 đề tài khả thi. (d) Một lệnh `snapshot diff` chạy tay (không CI). | 1 phiên (khoảng 3–4 giờ) sau khi mạng mở. Chặn bởi quyết định mở domain của chủ dự án. |
| 2 | Thư viện mô hình | ≥ 8 mô hình, mỗi mô hình qua kiểm bốn cấp | 8 mô hình. Cấp 1: 8/8. Cấp 4 chạy thật: **2/8 sạch** (M-006, M-008); 6 mô hình bị nêu giả định chưa khai, M-005 thêm lỗi đơn vị. Kết quả cấp 4 chưa ghi vào file mô hình. `verified`: 0/8. | **THIẾU** | (a) Khai các giả định cấp 4 nêu vào `assumptions` của 6 mô hình, sửa đơn vị M-005. (b) Chạy lại cấp 4 (nhà cung cấp khác Claude; môi trường có `api.openai.com` qua proxy) và ghi `verification.tiers` kèm `evidenceRef`. (c) Chủ dự án duyệt 8 mô hình (con đường duy nhất tới `verified`). | 2–3 giờ máy + khoảng $1 API; **chủ dự án duyệt 8 thẻ** (khoảng 30 phút). |
| 3 | Sensitivity Pass | điểm đảo chiều thật trên ≥ 4 mô hình | Có flip trên **3/8** (M-002, M-007, M-008), nhưng cả ba là đồng nhất thức hoặc ngưỡng luật đã công bố. Flip ẩn, phái sinh: **0**. 6/8 mô hình là "máy tính quy định", không có biến quyết định. | **THIẾU** | Thêm hoặc đổi **ít nhất 4 mô hình quyết định** (A so với B, có output chênh lệch đổi dấu), có tham số quét thật, lý tưởng là `geoVarying`. Ứng viên sẵn từ 8 đề tài khả thi: tái cấp vốn — hoà vốn theo thời gian giữ (đề tài 7, **Tập 1**); trả nợ xe hay đầu tư (3); trước thuế hay sau thuế theo thu nhập và thuế bang (4); HSA so với tài khoản hưu (9). Mỗi mô hình mới cũng phải qua cấp 1 và cấp 4 (điều kiện 2). Chạy `topic/scripts/sensitivity-all.ts`. | 1–2 phiên (mỗi mô hình khoảng 1–1,5 giờ gồm ca tay có nguồn). |
| 4 | Corpus đối thủ | ≥ 200 video, kiểm mới lạ tự động | 38 video **dựng tay**, tức 0 video thật. `checkNovelty` chạy tự động (so từ vựng). Embeddings chưa chọn được model (margin < 0,05 trên tập thăm dò 16 cặp). | **THIẾU** | (a) Chủ dự án chọn và cấp khoá API nền tảng cho `search.list` (irreversible, CHARTER §7.5), rồi mở `googleapis.com` cho môi trường. (b) Nối `transport` của corpus (T-011), xây ≥ 200 video trong hạn mức, đo hạn mức thật (G19). (c) Hiệu chuẩn embeddings: tăng tập thăm dò hoặc đo lại ngưỡng trên corpus thật, chọn model hoặc giữ so từ vựng và ghi giới hạn. | 1 phiên sau khi có khoá. Chặn bởi quyết định chọn nhà cung cấp và cấp khoá. |

**Tổng: 0/4 điều kiện đầu vào đạt.**
- Ba điều kiện (1, 4, và một phần 2) bị chặn bởi **quyết định của chủ dự án**: mở domain, cấp khoá, duyệt mô hình. Không phải bởi code.
- Điều kiện 3 là **khoảng trống nội dung** của thư viện: thiếu mô hình quyết định.

## Phiên Thesis Engine cần có trước khi chạy

1. **Bốn điều kiện đầu vào ở trên.** Cổng ghi rõ "phải có trước khi chấm". WP-015 cũng có checkpoint thấp hơn để **bắt đầu viết** engine (≥ 10 chuỗi từ ≥ 3 nhà cung cấp; corpus có dữ liệu và kiểm mới lạ chạy được; WP-011/013/014 done). Mức này cũng chưa đạt.
2. **Contract thesis chốt.** `topic/contracts/thesis.reference.schema.json` mới là gợi ý của spec. Hai việc phải xong:
   - thống nhất `noveltyVerdict` với đầu ra thật của `checkNovelty` (bốn giá trị `…-in-corpus`, không có `novel`);
   - định nghĩa **thẻ chấm mù chuẩn hoá** (không số, cùng khuôn), tách khỏi thẻ Gate 1.
3. **Nguồn 2 và 3 có nguyên liệu.** Cổng buộc hai nguồn này sinh ≥ 15/20 thesis:
   - nguồn 2 (ngưỡng ẩn) cần Sensitivity Pass có flip thật, tức điều kiện 3;
   - nguồn 3 (câu hỏi chưa ai trả lời) cần corpus thật cộng đại lượng nhu cầu, tức điều kiện 4.
   Thiếu một trong hai thì đợt chấm là "thiếu nguyên liệu", không đo được ý tưởng.
4. **Người chấm và quy trình chấm mù.**
   - 20 thesis đối chứng từ một mô hình khác (giới hạn 10 phút, không thấy kho ảnh chụp);
   - quy trình trộn và xoá nhãn;
   - phiếu ba lựa chọn (A / B / không phân biệt);
   - quyết định có người sống ở Mỹ chấm trục "Đáng quan tâm" hay ghi `chưa đo`. Không có người đó thì kết quả tốt nhất có thể là **"chưa đủ bằng chứng"**, không phải "qua".
5. **Nơi chạy.** Trong crux-lab, engine chạy bằng một lệnh, không workflow theo lịch (theo đầu bài; và WP-015 muốn `.github/workflows/thesis.yml`, mâu thuẫn với D-001). Bank ghi vào thư mục mới, ví dụ `topic/thesis-bank/`.
6. **Liên hệ với Tập 1.** Mô hình hoà vốn tái cấp vốn (A-M1) nên được viết thành một mô hình trong `topic/data/models/` theo `model.schema.json`, có ca cấp 1 từ nguồn công khai và qua cấp 4. Như vậy nó vừa phục vụ tập, vừa đóng một phần điều kiện 2 và 3 (CHARTER §2.1: nền tảng rút ra từ tập).
