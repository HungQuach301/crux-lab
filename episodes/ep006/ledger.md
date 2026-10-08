# Ledger — Tập 6 (ep006)

Mỗi dòng: một agent con hoặc một lô headless. Loại việc (`episode.md` §8): dựng · điều phối · kiểm mù · khác (WRITER, REVIEWER, Việc 0, kiểm độc lập, phiên K). Cột Token: agent con = số công cụ báo (cỡ ngữ cảnh, chỉ để phân loại — **không phải** trần); headless = **trần** (input + cache_write + output) cộng từ JSON đầu ra. Trần thật của phiên: PLAN §5 (`from_events.py`).

| Ngày | Cổng | Loại việc | Ai / lệnh | Việc | Token | Kết quả |
|---|---|---|---|---|---|---|
| 2026-10-08 | Việc 0 | điều phối | phiên chính (lệnh) | `data/fetch.py` (FRED CPIAUCNS/CPIAUCSL/CPI-W/PCE), calc.py hồ sơ chạy lại, `model/model.py`, `statements.py`, `numbers.md`, hồ sơ retire-1 `model.json` + `statements.json` | — | SHA ghim khớp hồ sơ; calc.py 12/12 = result.json; câu 9/9; đối chiếu SA/NSA 943/943 trong 0,5 điểm; bls.gov 403 (không R-CPI-E) |
| 2026-10-08 | Việc 0 | khác (kiểm độc lập) | agent general-purpose (không đọc model.py/calc.py) | tính lại từ định nghĩa numbers.md | 60.370 | **43/43 khớp**, 9/9 câu; rủi ro chữ "2010s" (không cửa sổ nào bắt đầu sau 2006-08) → luật nói |
| 2026-10-08 | C1 | kiểm mù | headless 6 đọc + 1 chấm | L1, L2 × (2 T + 1 G) | 22.910 (trần) | L1 3/3, L2 3/3, khuyên 0, overclaim 0 → L1 (luật hoà ghi trước) |
