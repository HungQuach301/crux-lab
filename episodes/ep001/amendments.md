# Amendments của Tập 1

Các quyết định của chủ dự án làm lệch spec thể loại hoặc luật kiểm, chỉ áp cho Tập 1.

| # | Ngày | Quyết định | Lệch khỏi | Nguồn |
|---|---|---|---|---|
| E1-A1 | 2026-09-29 | Cold open dài ~20 s (cold open A, 55 từ) được chấp nhận vì G-009 cần bối cảnh trước nhân vật. Luật S15 (cold open ≤ 15 s) trượt ở Tập 1 là trượt đã được duyệt, không sửa. | DX-S1 (cold open ≤ 15 s), luật S15 | Chủ dự án, Cổng A (`gates/gate-A.md`); sổ gu "G-009 · Cổng A" trên main |
| E1-A2 | 2026-09-29 | Repo public: dữ liệu thô của bên thứ ba không phải public domain (FRED MORTGAGE30US, OBMMIC30YF và bản chuẩn hoá chép nguyên chuỗi) không commit nữa; tải lại bằng `data/fetch.py`, kiểm bằng SHA-256 trong `data/sources.json`. Máy kiểm cần chạy `fetch.py` trước. HMDA (public domain, CFPB) giữ nguyên. | DX-H4 (commit dữ liệu gốc kèm SHA) | Chủ dự án, chỉ dẫn sau Cổng A |
