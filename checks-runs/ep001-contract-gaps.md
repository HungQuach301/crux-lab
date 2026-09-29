# Tập 1 — chỗ lệch giữa `episodes/ep001/contract.json` và schema hợp đồng tập (K2)

Đối chiếu `episodes/ep001/contract.json` (nhánh `ep001` @ `bbc28fb`, bản M1b) với `checks/CONTRACT.md` mục "Hợp đồng tập". **Phiên K2 không sửa file của bên dựng.** Luật dùng trường thiếu báo MISSING.

| # | Trường | Hợp đồng ep001 hiện có | Schema cần | Luật bị MISSING |
|---|---|---|---|---|
| 1 | `model.kind` | không có; `model.code`, `model.tests`, `model.recompute` (công thức bằng chữ) | `"refinance-breakeven"` | S01, S05 |
| 2 | `model.params` | không có; đầu vào chỉ nằm trong chữ | xem khối JSON dưới đây (đã thử: khớp 619/619 giá trị của `out/model.json`) | S01, S05 |
| 3 | `model.claims` | không có | ví dụ `{"be_bal_maya": "maya.withBalance", "cut36_maya": "maya.cut36", "be_simple_maya": "maya.simple", "sav_maya": "maya.monthlySavings", …}` | S05 |
| 4 | `data.sources`, `data.hosts`, `data.crosscheck[]` | không có (chỉ `data.rates`, `data.costs` bằng chữ) | `sources: "data/sources.json"`; `hosts: {primary: [miền FRED và miền nguồn HMDA như trong data/sources.json, data/hmda-sources.json], crosscheck: ["stlouisfed.org"]}`; `crosscheck: [{series: "rate30", primary: {file: "data/normalized/crosscheck_weekly.csv", key: "week", column: "mortgage30us"}, crosscheck: {…, column: "obmmic30yf_weekmean"}, tolerance: 0.5, used: "crosscheck"}]` | S03, S04 |
| 5 | `data.terms.hmda` | "OPEN": chưa trích được câu điều khoản | S03 đòi `terms.quote` ≥ 20 ký tự cho mọi file nguồn: S03 sẽ **trượt** tới khi trích được (DX-H4) | S03 (FAIL) |
| 6 | `coverage[]` | không có; kịch bản và shot list hứa "all 13 break-evens … every case shown" (`a3-range`) | `[{attribute: "case", act: "act3", values: [13 mã đợt]}]`, và trang gắn `case` lên phần tử của từng đợt | S06 |
| 7 | `sonification` | không có; cue sheet M1b đã khai âm sắc S2 (nhịp trầm MIDI 36–60, tick lọc 4,5–7 kHz) nhưng chưa ghi vào hợp đồng | `{stem: "sonify", bandsHz: [[60, 270], [4500, 7000]]}` | T1 |
| 8 | `characters.<k>.words` | nhân vật `maya`, `dan`, `priya` chưa có `words` | ví dụ `maya: ["Maya", "she", "her"]` — lưu ý S16 khớp nguyên từ; đại từ nên tránh nếu cảnh có hai nhân vật | S16 |
| 9 | `characters.<k>.illustrative` | "ILLUSTRATIVE" chỉ ghi trong chữ `what` | `illustrative: true` cho cả ba (S05 kiểm mọi claim của họ gắn ILLUSTRATIVE) | S05 (kiểm thiếu) |
| 10 | `scenarios` | không có (giữ 36/84 tháng chỉ là claim `hold36`, `y3`, `y7`) | `{hold36: {what, words: ["36 months", "three years"]}, …}` | S16 (tuỳ chọn) |
| 11 | `artefacts` | khoá `"M1 (this milestone)"`, `"M2/M3 (per checks/CONTRACT.md)"`, thêm khoá ghi chú; mục có chữ chú thích và `{…}` | khoá `M1`, `M2`, `M3`; mỗi mục là đường dẫn hoặc glob (`out/audio/stems/*.flac`) | F11 |
| 12 | `characters.note` | ghi chú trong `characters` | được phép (mục không phải object bị bỏ qua) | — |
| 13 | màu nhân vật | `cmedian` (Maya) = `#f2f4f7`, trùng màu chữ; `clarge` (Priya) = `#4c8dff`, trùng màu chuỗi `rate` | schema không cấm; ghi để chủ dự án xem | — |

Đúng schema: `episode`, `characters.<k>.color` (token có trong `design/tokens.json`), `shape`, `side`, `claims.core`, `claims.decisive`, `claims.illustrative`, `model.output`.

## `model.params` đã thử (bản tính lại độc lập của phiên kiểm)

```json
{"scenario": {"oldRate": 7.62, "paymentsMade": 35, "todayRate": 7.03, "termMonths": 360, "netHorizons": [36, 84], "byCutOf": "maya"},
 "characters": {"maya": {"loan": 375000, "cost": 5123.53}, "dan": {"loan": 115000, "cost": 3667.05}, "priya": {"loan": 1005000, "cost": 5033.725}},
 "history": {"series": {"file": "data/normalized/mortgage30_weekly.csv", "dateColumn": "date", "rateColumn": "rate"}, "swingPoints": 1.0,
             "spreads": [0.5, 1.0, 2.0], "loan": 300000, "termMonths": 360,
             "costShares": {"file": "data/normalized/hmda_refi_costs.csv", "filter": {"purpose": "refinance (31)", "loanSize": "all sizes"},
                            "yearColumn": "year", "shareColumn": "cost_p50_pct"}}}
```

Với tham số này, S01 so **619 giá trị** của `out/model.json` (ba nhân vật, `mayaByCut`, `gapAtSimpleBreakEven`, tỉ lệ chi phí theo năm, 13 đợt × 3 mức cắt): **0 lệch, không còn phần nào chưa tính lại**. Ba quy ước câu mô tả trong hợp đồng để ngỏ, phiên kiểm chọn và ghi vào `CONTRACT.md` (bên dựng nên ghi rõ trong `model.recompute`): trung bình tháng không làm tròn khi so; khoản vay lịch sử $300,000 từ tháng đỉnh; "đợt giảm tiếp" là thấp hơn **hẳn** lãi mới − spread.

## Luật về lời trên kịch bản M1b (`out/script-draft.json`)

- S13 (K2, G-009): **trượt**, một chuỗi câu vụn ở cold open ("Maya locked in 7.62%." / "This week's average: 7.03%." / "Refinancing costs $5,124." / "So when does that money come back?"). CV câu ≥ 4 chữ = 0,38 (đạt).
