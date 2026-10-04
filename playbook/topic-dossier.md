# Chuẩn hồ sơ đề tài (v1, 04/10/2026) — yêu cầu cho chat Mốc 3

Áp cho mọi đề tài **vào `topics/queue.md` từ nay**. Đề tài đã có trong hàng đợi thì bổ sung khi được chọn làm tập (P1 kiểm trước C1). Lý do: Tập 2 mất 2 vòng khoá K (K3.5, K3.6) vì tên kind và danh sách claim chốt muộn; câu tóm tắt sai trong hồ sơ debt-2 không bị V3 bắt (`playbook/lessons.md` E8, E9).

## 1. Thư mục hồ sơ (giữ như `topics-r1/machine/<id>/`)
`card.json` · `calc.py` · `result.json` · `sources.json` · `novelty.json` · `claim-risk.md`, cộng thêm **`model.json`** (mục 2) và **`statements.json`** (mục 3).

## 2. `model.json` — khớp `checks/`
```json
{"kind": "float-vs-fixed-replay",
 "kindStatus": "existing",
 "params": {"…": "đúng tên và kiểu trong bảng 'Loại mô hình' của checks/CONTRACT.md"},
 "quantities": [{"name": "share_all", "meaning": "tỉ lệ cửa sổ thả nổi tốn hơn tổng", "unit": "%", "from": "result.json → answer.share"}],
 "newKindNeeds": null}
```
- `kind` phải là một dòng có sẵn trong bảng "Loại mô hình" của `checks/CONTRACT.md` (`kindStatus: "existing"`), **hoặc** `kindStatus: "new"` kèm `newKindNeeds`. `newKindNeeds` mô tả: đầu vào (chuỗi dữ liệu, cột), phép tính một đoạn, đại lượng ra, bất biến kiểm được. Trường này là đặc tả cho phiên K; hồ sơ **không đặt tên kind mới** (tên do phiên K quyết).
- `quantities`: **mọi đại lượng** mà card, tiêu đề, lời hứa hay câu diễn giải dùng. Mỗi đại lượng có tên, nghĩa một câu, đơn vị, và nơi lấy trong `result.json`.

## 3. `statements.json` — câu diễn giải được kiểm với số
```json
[{"text": "The worst window started in April 1977, when rates peaked at 19.26%.",
  "uses": ["worst_start", "worst_peak_rate"],
  "check": "calc.py --statement 3 → True"}]
```
- Mọi câu diễn giải trong hồ sơ (tóm tắt, `answer`, `guess`, `changesDecision`, `claim-risk.md`) phải có một mục ở đây.
- Mỗi số trong câu phải là một đại lượng của mục 2, **lấy từ cùng một đối tượng**: cùng một cửa sổ, cùng một kỳ, cùng một khoảng chênh. Lỗi debt-2 là ghép tháng của cửa sổ 4/1977 với đỉnh lãi 20,6% của cửa sổ 2/1972.
- `calc.py` có chế độ `--statement N` tính lại các số trong câu từ dữ liệu và in `True`/`False`. Hồ sơ hợp lệ khi mọi câu ra `True`.

## 4. Kiểm hợp lệ (máy đề tài tự chạy, ghi vào `REPORT.md`)
1. `model.json` có `kind` khớp checks hoặc `newKindNeeds` đủ năm phần.
2. Mọi đại lượng nêu trong card và câu diễn giải có trong `quantities`.
3. Mọi câu trong `statements.json` ra `True`.
4. Ngày "hiện tại" của dữ liệu ghi trong `sources.json` (lessons A10).

Hồ sơ trượt một mục thì không vào hàng đợi.
