# HMDA: chi phí đóng hồ sơ — không tải được từ môi trường này (điều kiện dừng A-M0c)

Ngày kiểm: 2026-09-28, Phiên D1. Nguồn theo đầu bài: HMDA (ffiec.cfpb.gov), khoản vay mục đích tái cấp vốn (`loan_purposes=31`), đã giải ngân (`actions_taken=1`), trường chi phí khoản vay (`total_loan_costs`, có từ dữ liệu 2018). Nguồn này cũng là nguồn đã ghi ở `genre-spec/channel/topic-source-map.md`, đề tài 7.

## Đã thử

| Đường | Kết quả |
|---|---|
| `https://ffiec.cfpb.gov/v2/data-browser-api/view/aggregations?states=DE&years=2023&actions_taken=1&loan_purposes=31` | **200.** Trả về `count` và `sum` của số tiền vay (DE 2023: 1.667 khoản, tổng $766.405.000). API này **không** có trường chi phí khoản vay, nên không tính được trung vị chi phí. |
| `https://ffiec.cfpb.gov/v2/data-browser-api/view/csv?states=DE&years=2023&actions_taken=1&loan_purposes=31` | 301, chuyển tới `https://files.ffiec.cfpb.gov/data-browser/datasets/2023/filtered-queries/one-year/304c785938dde714541e36fd743583db.csv` |
| `https://files.ffiec.cfpb.gov/…` (file CSV cấp khoản vay, cả bản lọc theo bang) | **proxy 403** (`CONNECT tunnel failed, response 403`; trạng thái proxy ghi `connect_rejected … host: files.ffiec.cfpb.gov:443`). Chính sách mạng của môi trường chặn host này. |
| `https://ffiec.cfpb.gov/v2/data-browser-api/view/nationwide/csv?…` | 405 |
| `https://s3.amazonaws.com/cfpb-hmda-public/prod/snapshot-data/2023/2023_public_lar_csv.zip`, `…/one-year-data/…`, `…/data-browser/…` | S3 `AccessDenied` |
| `https://www.consumerfinance.gov/…`, `https://files.consumerfinance.gov/` (báo cáo "Data Point" có trung vị chi phí) | proxy 403 |
| `https://api.census.gov/`, `https://www.freddiemac.com/` | proxy 403 (ghi lại để biết; không phải nguồn của đề tài 7) |

Vì cả bản lọc theo bang cũng nằm trên `files.ffiec.cfpb.gov`, phương án "mẫu theo bang" **cũng bị chặn** trong môi trường hiện tại. Kích thước không phải vấn đề: bản lọc theo bang DE năm 2023 chỉ có 1.667 dòng.

## Đề xuất (chủ dự án chọn)

1. **Mở host (khuyến nghị).** Thêm `files.ffiec.cfpb.gov` vào danh sách domain được phép của môi trường (Network access, trong phần cài đặt môi trường cloud). Sau đó:
   - tải bản lọc **toàn quốc** theo từng năm 2018–2025 bằng Data Browser (`loan_purposes=31`, `actions_taken=1`), đọc theo luồng, chỉ giữ các cột cần (`loan_amount`, `total_loan_costs`, `interest_rate`, `lien_status`, `loan_type`, `occupancy_type`), tính trung vị theo năm và theo nhóm quy mô khoản vay, không lưu file gốc vượt 95 MB mà lưu SHA-256, URL, ngày tải và script tải lại;
   - nếu bản toàn quốc quá lớn cho hạn mức đĩa: mẫu theo bang (ví dụ 6 bang lớn theo số khoản tái cấp vốn), gắn rõ "mẫu N bang" trên màn hình và trong claim.
2. **ILLUSTRATIVE kèm dải nhạy.** Không dùng HMDA. Chi phí đóng hồ sơ là biến kịch bản gắn ILLUSTRATIVE, quét một dải (ví dụ $2.000–$8.000) và cho thấy điểm hoà vốn thay đổi thế nào trên cả dải. Chỉ lãi suất là số có nguồn. Nhược: câu hỏi của tập ("chênh lãi nào hoàn lại chi phí đóng") mất nửa nguồn thật; claim chi phí không còn là dữ liệu.
3. **Chủ dự án tải hộ.** Chủ dự án tải các file CSV đã lọc (theo năm, toàn quốc hoặc theo bang) từ `ffiec.cfpb.gov/data-browser` và đưa vào repo hoặc một kho ngoài; phiên sau chỉ đọc file đó. File > 95 MB thì cần Git LFS hoặc nơi lưu khác.

Phiên này **không** tự chọn nguồn thay thế (DX-H5: cần domain mới thì báo tên, không tự đổi nguồn). Điều khoản dùng dữ liệu HMDA chưa trích được vì trang điều khoản cũng nằm sau host bị chặn; phải trích nguyên câu khi tải được.
