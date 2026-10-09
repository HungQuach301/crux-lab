# S01/S05 trước C4 (P3b, 09/10) — LOCK 4d688acd (K4.1, gồm kind K4.0.2)

- `contract.json`: phần `model` theo `checks-runs/K402/contract-ep006-draft.json` (`kind: fixed-raise-vs-index-windows`, `index.name: "cpiu"` → khoá `cpiu_from_pce_start_*` giữ tên), `model.claims` = 45 khoá của `numbers.md` (đồng nhất), `claims.illustrative` = `guide_*` + `worst_window_years_2pct_fell_20y`; `claims.forbiddenAmounts` theo K-brief (3).
- Dữ liệu: `data/fetch.py --verify` → SHA 4/4 khớp `sources.json`.
- **S01 PASS:** 89 khoá so, 0 lệch, 0 phần không tính lại.
- **S05 PASS:** 45/45 claim khớp, 8/8 bất biến, 0 thiếu cờ ILLUSTRATIVE — chạy trên gốc tạm với `out/claims.json` dựng từ `out/model.json raw` (giá trị chưa làm tròn; 7 khoá suy ra lấy từ `by_decade`/`raise_grid`/`guide_path`). `out/claims.json` thật do nhà máy ghi ở C4 → S05 chạy lại trong checks đủ bộ.
- Báo cáo: `S01-S05-pre.json`.
