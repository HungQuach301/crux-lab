# tax-4 — kiểm chuẩn hồ sơ (playbook/topic-dossier.md §4), 04/10/2026

Lệnh tái hiện: `cd topics-r1/machine/tax-4 && python3 calc.py --statement all -v` (mỗi câu: `python3 calc.py --statement N`).
Chế độ mặc định `python3 calc.py` in đúng JSON như trước khi bổ sung (đã `diff` trước/sau: trùng khớp).

| # | Kiểm | Kết quả |
|---|---|---|
| 1 | `model.json` có `kind` khớp checks hoặc `newKindNeeds` đủ năm phần | **ĐẠT.** Không loại nào trong bảng "Loại mô hình" (`retirement-6040`, `refinance-breakeven`, `float-vs-fixed-replay`) khớp đề tài (phép tính thuế theo luật, không phát lại chuỗi). `kindStatus: "new"`, `kind: null` (tên do phiên K đặt); `newKindNeeds` có đủ `inputs` (file dữ liệu, cột, hằng số luật kèm cite), `params`, `computation`, `outputs`, `invariants` (7 bất biến kiểm được). |
| 2 | Mọi đại lượng nêu trong card và câu diễn giải có trong `quantities` | **ĐẠT.** 37 đại lượng: 16 id của `result.json → numbers`, 5 đại lượng dẫn xuất chỉ in ở `calc.py --statement` (`premium_per_hour_usd`, `marginal_bracket_pct`, `breakeven_markup_usd`, `ot_advantage_per_hour_usd`, `breakeven_markup_share_of_ot_rate_pct` — thêm theo E1), 16 hằng số luật/tham số mô hình kèm cite (thêm `EMPLOYEE_PAYROLL_PCT` = 7,65 theo E1, cite 26 U.S.C. 3101(a) + 3101(b)(1), cả hai đã có trong `sources.json` và đều được `calc.py` kiểm câu trích). Mọi tên trong `uses` của 35 câu đều có trong `quantities`; mọi chữ số trong 35 câu đều đến từ một đại lượng (kiểm mồ côi trong `calc.py`), trừ nhãn biểu mẫu `W-2`, `1099` và số `1` trong công thức `(1 - …)` của câu 22 (khai trong `labels`; công thức được claim `markup_tenth_of_ot_rate_at_22pct` kiểm). Mỗi `meaning` nêu phạm vi (người lao động mẫu $32, năm thuế 2026, nhánh tăng ca hay nhánh việc thứ hai). |
| 3 | Mọi câu trong `statements.json` ra `True` | **ĐẠT 35/35** (sau errata 2026-10-04). Lần kiểm đầu: TRƯỢT 1/34 — câu 21 cũ ("The general rule is an extra 5 dollars an hour at the 22% bracket…") ra `False` vì số 5 là của ví dụ $32, không phải quy tắc chung (ở $40 cùng bậc 22% cần ≈ $6,25). Ngày 2026-10-04 chủ dự án ra lệnh sửa: E1 áp dụng đúng đề xuất trong `ERRATA.md` — câu cũ thay bằng hai câu: 21 ("For this example … about $5 an hour more …") và 22 ("The general rule … about a tenth more … (premium x 22% / (1 - 7.65% - 22%) per hour)"); các câu sau dời số +1 (cũ 22–34 → 23–35); cả hai `expected: true`, ra `True`. A1 cũng áp dụng ("typical" → "average" trong `result.json` answer và docstring `calc.py`). A2 (năm 2025 chưa có trích dẫn; nay là câu 34) vẫn mở, không làm câu nào ra `False`. Mặc định `python3 calc.py` và mọi số trong `result.json` không đổi (đã `diff` trước/sau). |
| 4 | Ngày "hiện tại" của dữ liệu ghi trong `sources.json` | **ĐẠT.** `sources.json → series[AHETPI].lastObservation` = `{"date": "2026-06-01", "value": "32.38"}` (lấy về 2026-10-01); khớp dòng cuối `data/AHETPI.csv` và `result.json → numbers.ahe_date`. |

**Kết luận:** hồ sơ ĐẠT cả bốn mục sau errata E1 + A1 (áp dụng 2026-10-04 theo lệnh chủ dự án). Lưu ý: `claim-risk.md`, `result.json`, `calc.py` đổi nên mã SHA-256 trong `topics-r1/FREEZE.md` không còn khớp cho ba tệp này.

Phạm vi câu đã kiểm: `card.json` (title, viewer, decision, promise), `result.json` answer (4 câu), guess (1),
changesDecision (2), assumptions có số (5), limits có số (2), và 17 câu của `claim-risk.md` có số hoặc khẳng định
về kết quả. Các câu còn lại của `claim-risk.md` là tiêu đề, lệnh biên tập ("No advice.", "Say \"about\".") hoặc giới
hạn phạm vi không chứa số ("Tipped income is excluded.") và không có mục.
