# C1 — kết quả kiểm mù kể lại logline (vòng 1)

| nhãn | file | vai | điểm | khuyên | overclaim | đúng | lý do người chấm |
|---|---|---|---|---|---|---|---|
| R1 | 58ad037d | T | 1 | True | False | không | Has all three ideas (1997 limit noted in Q4, historical metro data, 2000 price threshold); Q5 suggests a tax professional if above the number. |
| R2 | 345e2b4c | T | 1 | True | False | không | Has all three ideas; Q5 recommends talking to a tax professional if near or over the threshold. |
| R3 | f4d491fb | G | 1 | False | False | đúng | Has all three ideas; Q5 only says check your own price against the threshold and look into it, with no sell/keep or professional advice. |
| R4 | 3ee00eb6 | T | 0.5 | True | False | không | Gets the historical data and the threshold but never mentions the limit being unchanged since 1997; Q5 suggests a tax professional. |
| R5 | 2112a1fc | T | 1 | True | False | không | Has all three ideas; Q5 mentions perhaps talking to a tax professional. |
| R6 | 6c94f2d9 | T | 1 | True | False | không | Has all three ideas; Q5 suggests looking into the tax, perhaps with a tax professional, before deciding to sell. |

**Vai đích đúng: 0/5** (ngưỡng ≥ 4/5) → **CHƯA ĐẠT**. Hiểu đúng (điểm 1): 5/6 người đọc (4/5 T + G). Overclaim 0/6. Chỗ khó hiểu: 0/6 ("a home that rose like its metro area's average" 2/6 nói hơi đặc nhưng hiểu được).
Lý do trượt duy nhất: **5/6 cờ khuyên**, tất cả cùng một dạng — câu 5 "nếu trên ngưỡng thì xem lại thuế / hỏi chuyên gia thuế trước khi bán". Theo rubric ghi trước ("gặp chuyên gia thuế…" là lời khuyên hành động), người chấm tính là khuyên; phiên không sửa điểm.

**Không chạy vòng 2 ở C1 (phiên quyết, ghi lý do):** (1) nguyên tắc tốc độ — logline không có câu khuyên; cờ đến từ suy diễn của người đọc khi được hứa "một con số tự đối chiếu"; (2) cùng tín hiệu được đo lại chặt hơn ở C2 (kiểm mù cả kịch bản, câu khuyên phải 0/6) — WRITER được giao câu đối trọng đúng chỗ này; (3) trần 60 agent cả tập (vòng 2 = 7 agent). Ý đồ cho phép "tối đa 2 vòng", không bắt buộc vòng 2. Gói G1 đưa logline kèm điểm, ghi **chưa đạt**, và đề xuất bản sửa L1b.

**L1b (đề xuất, chưa kiểm mù):** thêm câu đối trọng cuối: "It will not tell you what you owe or what to do: improvements and selling costs lower a real profit, and no home is exactly average."

Nguyên văn trả lời: `c1/answers.json`; điểm: `c1/scores.json`; khoá: `c1/key.json`, `c1/label-key.json`.
