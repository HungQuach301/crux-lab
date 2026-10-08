# Giao phiên K — Tập 6 (`episode.md` §7) · 2026-10-08

**Không mở phiên K riêng** (lệnh chủ dự án 08/10): phiên K lô đang chạy song song trên nhánh `checks-k40` (D-011 Q3, merge `main` trước C3 Tập 6). Tệp này là đầu vào cho lô đó: **cần một kind MỚI**. Tên kind và params do K quyết. Tự merge chỉ khi đủ D-008 §2 (chỉ thêm kind/luật mới, selftest đạt, luật cũ không đổi hành vi, 0 lệch); phần lô sửa luật cũ → hỏi chủ dự án.

## Cần kind MỚI
Không dòng nào trong bảng "Loại mô hình" (`checks/CONTRACT.md`, LOCK d93276a4) phủ "khoản trả tăng một tỉ lệ cố định mỗi năm so với tăng trưởng một chỉ số giá tháng, qua mọi cửa sổ H năm". Lý do từng kind: `topics-r1/machine/retire-1/model.json` → `noExistingKind` (gần nhất `lock-vs-roll-replay`: nó nhân lãi của một chuỗi LÃI; ở đây đầu vào là tỉ số MỨC chỉ số và vế cố định tăng ở mỗi kỷ niệm).
- **Đặc tả:** `topics-r1/machine/retire-1/model.json` → `newKindNeeds` (inputs, computation, outputs, invariants, dataNow).
- **Mở rộng của tập:** nhân vật dẫn đường ILLUSTRATIVE bắt đầu 2006-08 (đường theo kỷ niệm k = 0..20: `guide_*`), theo thập kỷ bắt đầu (`by_decade_*`), lưới tăng (`raise_grid_*`, `raise_needed_half/all_20y_pct`), 25 năm, độ vững trên CPI-W và PCE (`robust_cpiw_*`, `robust_pce_*`, `cpiu_from_pce_start_*` — CPI-U cắt về tháng đầu của PCE để so cùng khoảng), dải ≥ 90 % / ≥ 75 % (`share_2pct_at_least_*`), năm khoản đều chạm mức cuối của khoản 2 % (`median_year_level_reaches_2pct_end_median`, `guide_year_level_reaches_2pct_end`).
- **Luật dữ liệu K nên kiểm (bất biến):** ô trống của chỉ số (CPIAUCNS 2025-10) là THIẾU, không phải 0 — cửa sổ chạm nó bị bỏ (H=20: tháng bắt đầu 2005-10; H=25: 2000-10), nên 715 = 716 − 1 và 655 = 656 − 1; tháng mới nhất = quan sát cuối (2026-08), không cửa sổ 20 năm nào bắt đầu sau 2006-08; hoà ở min/max → tháng sớm nhất (kiểm độc lập: không có hoà ở ngưỡng giữ sức mua, gần nhất cách 0,18 điểm).
- **Bản tính bên dựng:** `episodes/ep006/model/model.py` → `out/model.json` (`params`, `raw`, `rounded`). Kiểm độc lập **43/43** (`model/independent/report.md`, agent mới, chỉ từ định nghĩa `numbers.md`).
- **Dữ liệu:** `episodes/ep006/data/fetch.py --verify` (FRED CPIAUCNS chính; CPIAUCSL đối chiếu: % đổi 12 tháng 943/943 trong 0,5 điểm → `data.crosscheck`; CWUR0000SA0, PCEPI độ vững). Cả bốn "Public Domain: Citation Requested". bls.gov 403 → không R-CPI-E.

## Danh sách claim
`episodes/ep006/numbers.md`; claim dùng trong lời: comment `<!-- claims -->` của `story/script.md` (chốt ở C2, xem mục dưới).

## Luật tập đề xuất (K xét)
1. Mọi khung có nhân vật dẫn đường, đối trọng hay ví dụ $ mang ILLUSTRATIVE (`characters.<k>.illustrative: true`).
2. Mọi khung có số lịch sử mang "history, not a forecast" (S17 kiểu Tập 3–4: `claims.conditions` với pattern `history, not a forecast`), và mọi khung nêu sức mua mang "CPI-U" hoặc "US consumer prices" (giỏ quốc gia ≠ giỏ người về hưu).
3. Không khung/câu nào so tổng tiền nhận được giữa khoản đều và khoản 2 % (giá niên kim không mô hình hoá) — ứng viên cho luật kiểu A20 `claims.forbiddenAmounts` (terms: "more money", "pays more", "total").
4. A26 (chỉ báo): câu ghép số hiện tại `cpi_yoy_latest_pct` (12 tháng tới 2026-08) với số lịch sử 20 năm phải gọi tên cả hai kỳ.
