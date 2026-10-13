# Kiểm hợp lệ hồ sơ (topic-dossier.md §4) — bổ sung khi chọn làm Tập 7 (P1, 2026-10-11)

| Mục | Kết quả | Bằng chứng |
|---|---|---|
| 1. `model.json` có kind khớp checks hoặc `newKindNeeds` đủ năm phần | ĐẠT | `kindStatus: "new"`; `newKindNeeds`: inputs, computation, outputs, invariants, dataNow (không đặt tên kind — phiên K) |
| 2. Mọi đại lượng của card và câu diễn giải có trong `quantities` | ĐẠT | 18 đại lượng = 18 số của `result.json`; `statements.json` chỉ dùng các tên này |
| 3. Mọi câu `statements.json` ra True | ĐẠT 11/11 | `python3 calc.py --statement N` trên bản ghim (SHA khớp `sources.json`, `episodes/ep007/data/raw/dossier-pin/`) |
| 4. Ngày "hiện tại" của dữ liệu ghi trong `sources.json` | ĐẠT | `lastObservation: 2026-09-24`; Tập 7 làm mới tới 2026-10-08 |
