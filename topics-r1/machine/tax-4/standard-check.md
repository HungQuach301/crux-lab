# tax-4 — kiểm chuẩn hồ sơ (playbook/topic-dossier.md §4), 04/10/2026

Lệnh tái hiện: `cd topics-r1/machine/tax-4 && python3 calc.py --statement all -v` (mỗi câu: `python3 calc.py --statement N`).
Chế độ mặc định `python3 calc.py` in đúng JSON như trước khi bổ sung (đã `diff` trước/sau: trùng khớp).

| # | Kiểm | Kết quả |
|---|---|---|
| 1 | `model.json` có `kind` khớp checks hoặc `newKindNeeds` đủ năm phần | **ĐẠT.** Không loại nào trong bảng "Loại mô hình" (`retirement-6040`, `refinance-breakeven`, `float-vs-fixed-replay`) khớp đề tài (phép tính thuế theo luật, không phát lại chuỗi). `kindStatus: "new"`, `kind: null` (tên do phiên K đặt); `newKindNeeds` có đủ `inputs` (file dữ liệu, cột, hằng số luật kèm cite), `params`, `computation`, `outputs`, `invariants` (7 bất biến kiểm được). |
| 2 | Mọi đại lượng nêu trong card và câu diễn giải có trong `quantities` | **ĐẠT.** 35 đại lượng: 16 id của `result.json → numbers`, 4 đại lượng dẫn xuất chỉ in ở `calc.py --statement` (`premium_per_hour_usd`, `marginal_bracket_pct`, `breakeven_markup_usd`, `ot_advantage_per_hour_usd`), 15 hằng số luật/tham số mô hình kèm cite. Mọi tên trong `uses` của 34 câu đều có trong `quantities`; mọi chữ số trong 34 câu đều đến từ một đại lượng (kiểm mồ côi trong `calc.py`), trừ nhãn biểu mẫu `W-2`, `1099` (khai trong `labels`). Mỗi `meaning` nêu phạm vi (người lao động mẫu $32, năm thuế 2026, nhánh tăng ca hay nhánh việc thứ hai). |
| 3 | Mọi câu trong `statements.json` ra `True` | **TRƯỢT 1/34.** 33 câu `True`. Câu 21 (claim-risk.md: "The general rule is an extra 5 dollars an hour at the 22% bracket…") ra `False`: số 5 là của ví dụ $32, không phải quy tắc chung (ở $40 cùng bậc 22% cần ≈ $6,25). Ghi tại `ERRATA.md` E1 kèm đề xuất sửa; câu chưa bị sửa, `expected: false`. Hai ghi chú tham khảo (A1 "typical" ≠ trung bình; A2 năm 2025 chưa có trích dẫn) không làm câu nào ra `False`. |
| 4 | Ngày "hiện tại" của dữ liệu ghi trong `sources.json` | **ĐẠT.** `sources.json → series[AHETPI].lastObservation` = `{"date": "2026-06-01", "value": "32.38"}` (lấy về 2026-10-01); khớp dòng cuối `data/AHETPI.csv` và `result.json → numbers.ahe_date`. |

**Kết luận:** hồ sơ trượt mục 3 cho tới khi chủ dự án chấp nhận (hoặc thay) đề xuất sửa E1 trong `claim-risk.md`.

Phạm vi câu đã kiểm: `card.json` (title, viewer, decision, promise), `result.json` answer (4 câu), guess (1),
changesDecision (2), assumptions có số (5), limits có số (2), và 16 câu của `claim-risk.md` có số hoặc khẳng định
về kết quả. Các câu còn lại của `claim-risk.md` là tiêu đề, lệnh biên tập ("No advice.", "Say \"about\".") hoặc giới
hạn phạm vi không chứa số ("Tipped income is excluded.") và không có mục.
