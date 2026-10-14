# Trước/sau Tập 4–7 — khoá K4.4b (A14, S02, S07, S09)

Trước = `checks/` của `main` sau K4.4 (LOCK `a35970a8`); sau = K4.4b. `checks-runs/K44/ba.py` trên gốc tạm (symlink, không ghi vào tập). page.json: Tập 5 `run-c5c`, Tập 6 A29 --no-cache, Tập 7 A29 --no-cache (master bản giao `529471f0…`). "+ khai" = bản sao hợp đồng/claims của Tập 7 có khai của bên dựng: `claims.termNames` (`\b(15|30)-year\b`, `paid off in 15 years`, `in 15 years`) và `basis: nominal` cho 29 claim tiền (`ep007-declare.json`).

| Tập | Luật | Trước | Sau | Ghi chú |
|---|---|---|---|---|
| 4 | A14 / S02 / S07 / S09 | MISSING | MISSING | không có video / page.json trong container |
| 5 | A14 | MISSING | MISSING | không có video |
| 5 | S02 / S07 / S09 | PASS | PASS | |
| 6 | A14 / S02 / S07 / S09 | PASS | PASS | |
| 7 | **A14** | FAIL (3 từ: "Tessa's" ×3) | **PASS** | medium.en nghe đúng S09.3, S15.3, S25.2 |
| 7 | **S02** | FAIL (thẻ phương pháp không thấy "US only", "history, not a forecast") | **PASS** | hồi `limits` (S32 "What this leaves out") |
| 7 | S07 | FAIL (52 số lời chưa đăng ký) | FAIL (52) | luật chỉ miễn khi hợp đồng khai `termNames` |
| 7 | S07 + khai | FAIL (52) | FAIL (**18**) | còn: "$320,000" ×3 (claim `principal` chưa gắn câu/cảnh), "15" ngoài tên sản phẩm ×4, năm 1990/2000/2010 chưa đăng ký … — việc của bên dựng (ghi `spoken`) |
| 7 | S09 | FAIL (29 claim thiếu `basis`; 2.384 khung thiếu nhãn) | FAIL (như trước) | chưa khai `basis` |
| 7 | S09 + khai | FAIL (2.384 khung; "nominal" chưa nói) | FAIL (**0 khung**; "nominal" chưa nói 1) | nhãn trên hình không còn đòi; phần lời K3.2 giữ theo 3a |
