# Ghi chú cho phiên kiểm — Tập 2

Phiên này KHÔNG sửa `checks/`. Đề xuất `rate-path-history` (bản trước) **đã bỏ**: K3.5 viết loại `float-vs-fixed-replay` (nhánh `checks-k35`, LOCK `bd1948d9…`, chủ dự án duyệt 2026-10-01).

## Tập 2 dùng K3.5 thế nào
- `contract.json → model.kind = float-vs-fixed-replay`; `params`: `principal 50000`, `termMonths 120`, `fixedRate 9.0`, `floatStartRate 7.5`, `firstStart 1954-01`, `indexFloor 0`, không `rateCap`, `periodBreaks ["1981-01"]`, `spreads` −1…3 bước 0,25 (bỏ 0,25/0,75… dưới 0), `index {file: data/normalized/tb3ms_monthly.csv, dateColumn: month, valueColumn: rate}`.
- `out/model.json` theo `fvf_compare` (tham số nhắc lại, tổng hợp, `windows`, `periods`, `sensitivity`), số chưa làm tròn. Phần mở rộng phạm vi (b) chưa có khoá ở `out/model-extra.json` (không đọc bởi S01).
- **Chạy thử bằng mã K3.5 trên bản sao (SHA khớp LOCK):** `fvf_compare` 3 060 phép so, 0 lệch, không trường lạ; 34 khoá S05 tính được; 3 bất biến đạt. (2026-10-01)
- `out/claims.json`: tỉ lệ ghi chưa làm tròn (dung sai 0,005); tháng dùng claim số `worst_start_year`/`worst_start_month`.

## Claim chưa có khoá K3.5 (ứng viên K3.6 — danh sách chốt SAU C2, chỉ những claim kịch bản thật sự dùng)
Đánh dấu `k36` trong `out/claims.json`. Hiện có (trước C2):
- tỉ lệ theo khoảng chênh **tách theo thời kỳ** (`gap*_early`, `gap*_late`);
- xấu nhất / trung vị **theo khoảng chênh** (`gap*_worst`);
- **nhiều mức trần** trong một mô hình (`cap12/15/18/25_*`);
- khoản trả ngoài `maxPayment`: `var_first_payment`, `median_max_payment`, `share_payment_above_fixed`;
- `share_rate_above_fixed` (tỉ lệ cửa sổ có lãi vượt `fixedRate`), `worst_peak_rate` (maxRate của cửa sổ xấu nhất).
Gói C2 sẽ báo danh sách cuối để chủ dự án mở K3.6 một lần.
