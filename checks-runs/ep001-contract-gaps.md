# Tập 1 — chỗ lệch giữa `episodes/ep001/contract.json` và schema hợp đồng tập (K2)

Đối chiếu `episodes/ep001/contract.json` (nhánh `ep001` @ `10b5438`) với `checks/CONTRACT.md` mục "Hợp đồng tập". **Phiên K2 không sửa file của bên dựng.** Luật dùng trường thiếu báo MISSING.

| # | Trường | Hợp đồng ep001 hiện có | Schema cần | Luật bị MISSING |
|---|---|---|---|---|
| 1 | `model.kind` | không có; `model.code`, `model.tests`, `model.recompute` (công thức bằng chữ) | `"refinance-breakeven"` (máy kiểm đã có bản tính lại) | S01, S05 |
| 2 | `model.params` | không có; số đầu vào chỉ nằm trong chữ `characters.median.what` ("balance $375,000, closing costs $5,124") | `{loan: 375000, cost: 5123.53, oldRate: 7.62, termMonths: 360, breakEvenTargets: {sp36: 36}, classes: {small: {loan, cost}, big: {loan, cost}}}` | S01, S05 |
| 3 | `model.claims` | không có | ví dụ `{"be10": "breakEven:1.0", "sp36_mid": "spreadFor:36", …}` | S05 |
| 4 | phần `history` của `out/model.json` (13 đợt giảm lãi, zig-zag ≥ 1 điểm) | có trong mô hình | máy kiểm chưa có bản tính lại cho phần này; khi có `model.kind` và `params`, S01 sẽ liệt kê `history`, `costSharesByYear`, `fixedSharePre2018` là "không tính lại" và **trượt** tới khi phiên kiểm viết thêm (hoặc bên dựng khai chúng trong `notModel` kèm lý do, cần duyệt) | S01 |
| 5 | `data.sources` | không có (chỉ `data.rates`, `data.costs` bằng chữ) | `"data/sources.json"` | S03, S04 |
| 6 | `data.hosts` | không có | `{primary: [miền của FRED và của nguồn HMDA, như trong `data/sources.json`, `data/hmda-sources.json`], crosscheck: ["stlouisfed.org"]}`; Optimal Blue `OBMMIC30YF` cũng lấy từ FRED | S03 |
| 7 | `data.crosscheck[]` | không có; có sẵn `data/normalized/crosscheck_weekly.csv` (`week, mortgage30us, obmmic30yf_weekmean`) và dung sai 0,5 pp trong chữ | `[{series: "rate30", primary: {file: "data/normalized/crosscheck_weekly.csv", key: "week", column: "mortgage30us"}, crosscheck: {…, column: "obmmic30yf_weekmean"}, tolerance: 0.5, used: "crosscheck"}]` | S04 |
| 8 | `data.terms.hmda` | "OPEN": chưa trích được câu điều khoản | S03 đòi `terms.quote` ≥ 20 ký tự cho mọi file nguồn: khi chạy, S03 sẽ **trượt** tới khi trích được (DX-H4) | S03 (FAIL) |
| 9 | `coverage[]` | không có; bản tóm tắt M1 hứa "cắt 1 điểm: hoà vốn 10–21 tháng qua cả 13 đợt kể từ 1971 (mọi trường hợp đều hiện)" | `[{attribute: "case", act: "act3", values: [13 mã đợt]}]`, và trang gắn `case` lên phần tử của từng đợt | S06 |
| 10 | `sonification.stem`, `sonification.bandsHz` | không có; cue sheet để trống âm sắc, không khai dải | ví dụ S2: `{stem: "sonify", bandsHz: [[40, 250]]}` (S2 có 97% năng lượng dưới 250 Hz); phải chứa ≥ 50% năng lượng stem `sonify` | T1 |
| 11 | `characters.<k>.words` | không có | cách kịch bản gọi tên nhân vật (ví dụ median: `["median", "median refinance"]`; small: `["under $150,000", "smaller loans"]`) | S16 |
| 12 | `scenarios` | không có (thời gian giữ 36/60/84 tháng chỉ là claim `hold36`, `hold60`, `hold84`) | `{hold36: {what, words: ["36 months", "three years"]}, …}` | S16 (tuỳ chọn, nhưng giúp đạt) |
| 13 | `artefacts` | khoá `"M1 (this milestone)"`, `"M2/M3 (per checks/CONTRACT.md)"`; mục có chữ chú thích và dấu ngoặc nhọn (`out/audio/stems/{voice,…}.flac`, `out/voice/ (table read takes)`) | khoá `M1`, `M2`, `M3`; mỗi mục là đường dẫn hoặc glob (`out/audio/stems/*.flac`) | F11 |
| 14 | `characters.note` | chuỗi ghi chú trong `characters` | được phép (mục không phải object bị bỏ qua) | — |
| 15 | màu nhân vật | `cmedian` = `#f2f4f7` (trùng màu chữ `ink`), `clarge` = `#4c8dff` (trùng màu chuỗi `rate`) | schema không cấm; ghi để chủ dự án xem: V04 đo màu **chính** của hình mang `char`, nên đường lãi suất cùng màu không làm trượt, nhưng người xem có thể nhầm nhân vật "large" với đường lãi suất | — |

Đúng schema: `episode`, `characters.<k>.color` (tên token có trong `design/tokens.json` của tập), `shape` (`solid`/`dashed`), `side` (`left`/`centre`/`right`), `claims.core`, `claims.decisive`, `claims.illustrative`, `model.output`.

Hai nhân vật `median` và `small` cùng hình `solid`: được phép (V04 chỉ đòi màu khác nhau; hình phải đúng hình đã khai).

## Thử bản tính lại `refinance-breakeven` trên mô hình của Tập 1

Với `params` như dòng 2 (chưa có `classes`), bản tính lại độc lập của máy kiểm so 20 giá trị của `out/model.json` (đầu vào; `cases` 0,25 / 0,5 / 1 / 2 điểm: tiền trả cũ, mới, tiết kiệm, tháng hoà vốn; `sp36.mid`): **0 lệch**. Phần chưa tính lại: `sp36.small`, `sp36.big` (cần `classes`), `costSharesByYear`, `fixedSharePre2018`, `history`.
