# Ghi chú cho phiên kiểm — Tập 2

Phiên này KHÔNG sửa `checks/`. Đề xuất `rate-path-history` (bản trước) **đã bỏ**: K3.5 viết loại `float-vs-fixed-replay` (nhánh `checks-k35`, LOCK `bd1948d9…`, chủ dự án duyệt 2026-10-01).

## Tập 2 dùng K3.5 thế nào
- `contract.json → model.kind = float-vs-fixed-replay`; `params`: `principal 50000`, `termMonths 120`, `fixedRate 9.0`, `floatStartRate 7.5`, `firstStart 1954-01`, `indexFloor 0`, không `rateCap`, `periodBreaks ["1981-01"]`, `spreads` −1…3 bước 0,25 (bỏ 0,25/0,75… dưới 0), `index {file: data/normalized/tb3ms_monthly.csv, dateColumn: month, valueColumn: rate}`.
- `out/model.json` theo `fvf_compare` (tham số nhắc lại, tổng hợp, `windows`, `periods`, `sensitivity`), số chưa làm tròn. Phần mở rộng phạm vi (b) chưa có khoá ở `out/model-extra.json` (không đọc bởi S01).
- **Chạy thử bằng mã K3.5 trên bản sao (SHA khớp LOCK):** `fvf_compare` 3 060 phép so, 0 lệch, không trường lạ; 34 khoá S05 tính được; 3 bất biến đạt. (2026-10-01)
- `out/claims.json`: tỉ lệ ghi chưa làm tròn (dung sai 0,005); tháng dùng claim số `worst_start_year`/`worst_start_month`.

## K3.6 — claim kịch bản v3 dùng mà K3.5 chưa có khoá (danh sách chốt sau C2, 26 claim)
Sinh bằng máy từ `story/script.md` v3 × `out/claims.json` × `contract.json → model.claims`. Đề xuất khoá (chỉ đặc tả):

| Nhóm | Claim | Khoá đề xuất |
|---|---|---|
| Tỉ lệ theo khoảng chênh **và** thời kỳ | `gap00/10/20/30/m10_early`, `gap00/10/20/30/m10_late` | `shareCostlierAtSpread:<điểm>:<tháng đầu thời kỳ>` |
| Xấu nhất theo khoảng chênh | `gap00/10/20/30/m10_worst`, `gap_worst_start_all` (mọi khoảng chênh cùng 1977-04) | `worstDifferenceAtSpread:<điểm>`, `worstStartAtSpread:<điểm>` (Year/Month) |
| Nhỏ nhất qua mọi khoảng chênh theo thời kỳ | `min_gap_early` (10,5% > 0) | `minShareCostlierOverSpreads:<thời kỳ>` |
| Khoản trả ngoài `maxPayment` | `var_first_payment` ($593.51), `first_payment_gap` ($39.87) | `floatFirstPayment` (fixedPayment − floatFirstPayment suy ra) |
| Thuộc tính cửa sổ | `worst_peak_rate` (19,26%: maxRate của cửa sổ xấu nhất), `share_rate_above_fixed` (76,2%: % cửa sổ có tháng lãi > fixedRate), `worst_share_of_fixed` (43% = worstDifference / fixedTotalInterest) | `worstWindowMaxRate`, `shareRateAboveFixed`, (tỉ số suy ra từ hai khoá có sẵn) |
| Ngày dạng chuỗi | `first_start`, `last_start`, `worst_start`, `best_start` | đã có dạng số `…Year/…Month`; K3.6 chỉ cần chấp nhận claim ngày `YYYY-MM-01` so sau chuẩn hoá |

Không dùng trong v3 (không cần khoá): lưới trần `cap*`, `median_max_payment`, `share_payment_above_fixed`, `gap*` ở 0,5/2,5.

## K3.6 đã merge (LOCK `2fcc9fcc`, 01/10/2026)
Đã áp: 72 khoá S05 (`contract_build.py`), claim chưa làm tròn, `claims.illustrative`. Chạy thử S01/S05 trên bản sao: PASS, 0 lệch. `gap_worst_start_all` dùng `worstStartAtSpread:1.5` (một khoảng chênh); K3.6 tự xác nhận 1977-04 ở cả 15.
