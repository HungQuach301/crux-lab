# topics-r1 — errata sau đóng băng (2026-10-04, theo lệnh chủ dự án)

Đóng băng gốc: `FREEZE.md` (`d16d1b4`). Các tệp dưới đây được sửa **sau** đóng băng theo lệnh chủ dự án (quyết định vòng 2, mục 2 và 4); SHA trong `FREEZE.md` là của bản gốc (các tệp trên sẽ lệch SHA — đúng như dự kiến), kết quả chấm và kiểm hợp lệ vòng 1 không đổi.

| Hồ sơ | Tệp | Sửa | Lý do |
|---|---|---|---|
| debt-2 | `result.json` `answer` | "…with the variable rate peaking at 20.6%" → "…with the variable rate in that window peaking at 19.26%. The highest variable rate in any window was 20.6% (window starting 1972-02)." | 20,6 % là `max_variable_rate_any_window` (cửa sổ 1972-02), không phải đỉnh của cửa sổ xấu nhất 1977-04 (19,26 %). |
| debt-2 | `result.json` `numbers` | thêm `worst_peak_rate` = 19.26, `max_rate_window_start` = 1972-02-01; định nghĩa `max_variable_rate_any_window` nêu phạm vi "ALL 753 windows" | Định nghĩa mỗi số phải nêu phạm vi (D-004 sửa đổi 1, V6). |
| debt-2 | `calc.py` | in thêm hai số trên; các số cũ không đổi | |
| debt-2 | `claim-risk.md` | sửa câu "peaks at 20.6% in the worst path"; thêm cảnh báo không ghép số của hai cửa sổ | |
| tax-4 | `result.json` `answer` | "22.3% vs 29.6%" → "22.32% vs 29.65%"; "33% of the overtime pay" → "33.33%" | Render theo làm tròn của ID (`side_total_tax_rate_on_extra_pct` = 29.65; 29,6 % sai làm tròn). |
| tax-4, tax-2 | `model.json`, `statements.json`, `calc.py --statement`, `standard-check.md` | bổ sung theo `playbook/topic-dossier.md`; tax-4 35/35 câu True, tax-2 24/24 True; mục §4 đạt cả bốn | Chuẩn hồ sơ v1 cho đề tài trong hàng đợi. |
| tax-4 | `claim-risk.md`, `result.json` `answer`, `calc.py` docstring | "quy tắc chung +$5/giờ ở bậc 22 %" → "+$5 cho ví dụ này; quy tắc chung ≈ một phần mười mức lương làm thêm giờ" (công thức kèm); "typical" → "average" | Bộ kiểm câu bắt: $5 chỉ đúng cho ví dụ $32 (cùng loại lỗi debt-2). Chi tiết: `machine/tax-4/ERRATA.md`. |
| tax-2 | `sources.json` `provisions` | thêm 26 U.S.C. 121(b)(4) (cửa sổ 2 năm cho vợ/chồng goá) và 1222(3) (lãi vốn dài hạn), trích nguyên văn law.cornell.edu, kiểm bằng `quote_in` | Câu có nội dung luật nhưng thiếu nguồn. Chi tiết: `machine/tax-2/ERRATA.md`. |

Lưu ý: hồ sơ debt-2 đã đi vào Tập 2 (`episodes/ep002/`); phiên này không chạm thư mục tập. retire-4 không sửa (phiên Tập 3 đang dùng và tự bổ sung).
