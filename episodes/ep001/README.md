# Tập 1 — "Ở mức chênh lãi suất nào thì tái cấp vốn hoàn lại được chi phí đóng hồ sơ?"

Đề tài 7, dòng 1 (vay và nợ, quyết định về nhà). Phiên D1, nhánh `ep001`.

## Trạng thái: DỪNG ở A-M0c, chờ chủ dự án chọn phương án dữ liệu chi phí đóng hồ sơ

| Bước | Trạng thái |
|---|---|
| A-M0a: toolkit theo cấu trúc crux-lab, tách khỏi `checks/` | **xong**: `toolkit/README.md`, mục "Sửa ở Tập 1, bước 0" |
| A-M0b: mẫu 10 giây chạy đầu cuối, chạy luật lên mẫu | **xong**: `m0-sample/README.md`. 41 PASS; 3 trượt thật (T1, R03, A15), đã ghi cách xử lý cho M1 |
| A-M0c: lãi suất FRED `MORTGAGE30US` | **xong**: `data/raw/MORTGAGE30US.csv`, `data/sources.json` (SHA-256, URL, ngày tải, điều khoản trích nguyên câu); đối chiếu độc lập với Optimal Blue `OBMMIC30YF` (507 tuần, lệch tối đa 0,38 pp, dung sai 0,5 pp, 0 tuần ngoài dung sai) |
| A-M0c: chi phí đóng hồ sơ HMDA | **KHÔNG TẢI ĐƯỢC** → điều kiện dừng. Chi tiết và 3 phương án: [`data/HMDA-ACCESS.md`](data/HMDA-ACCESS.md) |
| A-M1 (mô hình, kịch bản, đọc thử, storyboard, hợp đồng, gói duyệt) | **chưa làm** (dừng theo đầu bài) |

## Lý do dừng

HMDA cấp khoản vay (có trường `total_loan_costs`) chỉ tải được từ `files.ffiec.cfpb.gov`. Chính sách mạng của môi trường chặn host này (proxy 403), và bản S3 công khai trả `AccessDenied`. API tổng hợp của `ffiec.cfpb.gov` tải được nhưng không có trường chi phí. Vì bản lọc theo bang cũng nằm trên cùng host bị chặn, phương án "mẫu theo bang" cũng không làm được trong môi trường này.

## Việc chủ dự án cần quyết

1. **Phương án dữ liệu chi phí đóng hồ sơ** (`data/HMDA-ACCESS.md`). Khuyến nghị: mở `files.ffiec.cfpb.gov` trong Network access của môi trường, rồi chạy M1 với trung vị HMDA thật.
2. **Điều khoản `MORTGAGE30US`.** FRED xếp chuỗi này vào loại *"Copyrighted: Citation Required"*: được dùng khi ghi nguồn khi hiển thị hoặc công bố (câu trích ở `data/sources.json`). Nhưng điều khoản FRED cũng cấm *"Redistribute any third party’s proprietary content, including any graphs, maps, images, logos, data, or datasets, for commercial use without first obtaining express written permission from the data provider."* Theo đọc của phiên này:
   - hiển thị đường lãi suất trong video có ghi nguồn là được;
   - **công bố lại file dữ liệu** (ví dụ "bảng tính mô hình công khai" ở `persona.md`, cơ chế 2) trên kênh có quảng cáo có thể cần Freddie Mac cho phép bằng văn bản.
   Đây là việc irreversible và pháp lý, nên chủ dự án quyết. Trang điều khoản của Freddie Mac (`freddiemac.com`) cũng bị chặn ở môi trường này.
3. **Mức âm thanh theo dữ liệu** (`m0-sample/README.md`, bảng mức tăng): cần nghe bằng tai trước khi dùng cho cả tập.

## Thư mục

- `data/`: dữ liệu và script tải lại (`python3 episodes/ep001/data/fetch.py`; kiểm SHA: `--verify`).
- `m0-sample/`: mẫu 10 giây (gốc thử riêng, cùng cấu trúc với gốc tập).
