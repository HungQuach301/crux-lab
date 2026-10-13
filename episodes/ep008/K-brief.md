# Giao phiên K — Tập 8 (`episode.md` §7) · 2026-10-13

**Cần kind MỚI** (bảng "Loại mô hình" `checks/CONTRACT.md`, LOCK `dc4981b3…`, không có kind nào tính người thuê + người mua; gần nhất `ltv-first-passage`: dư nợ vs chỉ số giá, không tiền thuê). Tên kind + params do K quyết. Chạy cùng **lô K Tập 8 (A34–A37, `checks-appeal.md`)** **trước C4** (PLAN kênh: lô này lẽ ra chạy trước P1 — chưa chạy; P1 không chờ).
- **Đặc tả:** `topics-r2/machine/rent-buy-1/model.json` → `newKindNeeds` (inputs, computation, outputs, invariants, dataNow) — đủ năm phần.
- **Mở rộng của tập (MỚI so với hồ sơ):** quét giả định tiền thuê `sweep` 3,0–7,0 % (bước 0,2) → tỉ lệ người mua hơn 10 năm; `flip_yield_10y` (tỉ lệ giả định mà người mua hơn còn 50 %, chia đôi 40 vòng, 2,42 %); hai mốc Census HVS `hvs_yield_2025Q4` 4,83 %, `hvs_yield_2026Q1` 5,59 % và `share_hvs_*_10y` (73,6 %, 87,3 %) — đầu vào là 4 số trích bản tin Census (chưa có tệp tải: census.gov bị mạng P1 chặn; **K cần đặt cách khai nguồn "số trích văn bản"** hoặc chờ tệp HVS Table 11A/B).
- **Bất biến K nên kiểm:** (ngoài hồ sơ) tỉ lệ người mua hơn **đơn điệu không giảm** theo y_neo trên cả `sweep`; `flip_yield_10y` nằm giữa hai bước quét kề; 307 = số tháng có đủ chuỗi 1991-01…2016-07; mọi cửa sổ kết thúc ≤ 2026-07 (không ngoại suy).
- **Bản tính bên dựng:** `model/model.py` → `out/model.json` (77 đại lượng + `sweep`). 76/76 trùng `result.json` hồ sơ; kiểm độc lập 49/49 (`model/independent/report.md`, `check.py`).
- **Dữ liệu:** `data/fetch.py` (FRED HPIPONM226N, CUUR0000SEHA "Public Domain: Citation Requested"; MORTGAGE30US "Copyrighted: Citation Required"; TB3MS chỉ biến thể). `data.crosscheck`: **chưa có chuỗi đối chiếu** — đề xuất K: CPI tiền thuê ↔ CUSR0000SEHA (SA) % đổi 12 tháng ≤ 0,5 điểm (như Tập 7); HPI ↔ USSTHPI (FHFA all-transactions, quý) % đổi 4 quý.

## Danh sách claim
`numbers.md` (45 dòng nói/hiện); claim dùng: comment `<!-- claims -->` của `story/script.md` (C2) + cột claims của `story/beats.md`.

## Luật tập đề xuất (K xét)
1. Mọi khung có Nina/hai người/ví dụ $ mang ILLUSTRATIVE; mọi câu có tỉ lệ người mua hơn kèm (trên hình hoặc lời gần đó) "rent assumed" (tiền thuê khởi đầu là giả định) — claim-risk hồ sơ câu 6.
2. `claims.forbiddenTerms` (A20): "buying always wins", "throwing money away" (trừ câu hỏi của nhân vật), "wins", "better off", "should buy", "should rent", "first ever" — danh sách từ dễ đọc thành lời khuyên (luật tạm 13/10).
3. Câu "today" (56,8 % < mọi tháng đã phát lại) không đứng cạnh từ dự báo ("will", "next", "likely").
4. **Quy tắc 1 và số trên vật thể:** thẻ RENT (N2) mang chữ số "4% / 5% / 6%" trong chế độ thế giới — K quyết: miễn cho nhãn GIẢ ĐỊNH trên vật (không phải số dữ liệu/so sánh), hay buộc thẻ chỉ hiện số ở chế độ đồ thị.
5. Footage ngoài (luật tạm 13/10): mỗi tệp ghép một dòng `RIGHTS.md` (URL, giấy phép nguyên văn, ngày tải, SHA); khung có tư liệu lịch sử phải có chữ năm + nguồn; tổng thời lượng footage ≤ 15 % (đề xuất luật đo từ `footage` của spine).
