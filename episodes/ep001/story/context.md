# Tập 1 — Bối cảnh (context)

Mục đích: thế giới người xem đang sống, trước khi có nhân vật hay con số nào của nhân vật. Claim ID lấy từ `episodes/ep001/numbers.md` (cập nhật 2026-09-28). Dòng không có claim ID là số WRITER tự tính từ CSV; **chưa được dùng trong lời** cho tới khi DATA cấp ID. `F` = `data/normalized/mortgage30_weekly.csv` (FRED `MORTGAGE30US`, Freddie Mac PMMS, lãi trung bình 30 năm cố định, theo tuần, danh nghĩa). `H` = HMDA (CFPB/FFIEC), `data/normalized/hmda_refi_costs.csv`.

Mốc ngày: **the week ending September 24, 2026** [anchor_date]. Không bao giờ viết "this week".

## 1. Chuyện gì đã xảy ra với lãi suất

- **Đáy:** 2.65% [low], tuần kết thúc January 7, 2021 [low_date] — thấp nhất từ 1971 [y1971]. Tới ngày mốc, lãi cao hơn đáy 4.38 điểm [rise_since_low].
- **Đỉnh 2023:** 7.79% [peak2023], tuần 2023-10-26 — cao nhất kể từ năm 2000 [peak2023_since].
- **Tháng 10/2023** [oct2023] (tháng các hộ minh hoạ vay): trung bình 7.62% [r_old].
- **Một năm qua:** 6.30% [r_year_ago] tuần 2025-09-25; 7.03% [r_today] tuần kết thúc 2026-09-24 — cao nhất kể từ January 16, 2025 [today_since]. So với 10/2023, giảm 0.59 điểm [cut_today].
- Chưa có claim ID (không dùng trong lời): đáy gần nhất 5.98% tuần 2026-02-26; "cửa sổ ≤ 6.62%" từ 2025-08-14 đến 2026-07-23. [F]

Luôn nói kèm: "history, not a forecast"; "US only"; PMMS là trung bình toàn quốc, dựa trên hồ sơ gửi Freddie Mac (trích FRED, `ctx_pmms_profile` nửa đầu). Phần "20% down, excellent credit" **chưa xác minh — không nói**.

## 2. Ai đang ở trong hoàn cảnh này

Những hộ vay khi lãi ở gần đỉnh 2023. Trong các khoản vay mua nhà năm 2023 (lien 1, 30 năm), 30% [purch23_ge7] — 881,835 khoản [purch23_n_ge7] — có lãi từ 7% trở lên. Đây là tỉ lệ trong số khoản giải ngân năm 2023, không phải trong số khoản còn dư nợ hôm nay.

Năm 2025 có 488,241 khoản vay lại đổi lãi/kỳ hạn [n31]; lãi trung vị của khoản mới là 6.00% [rate31_p50]. Chuỗi số khoản 2021–2024 (3,089,298 → 97,298 → …) là WRITER tự tính từ H, **chưa có claim ID**.

## 3. Vay lại không miễn phí

"Loan costs" (HMDA `total_loan_costs` = Closing Disclosure mục D: phí khởi tạo và dịch vụ; **không gồm** "Other Costs" như thuế, phí đăng ký, trả trước) [ctx_tlc]. Lời nói "loan costs", không nói "all closing costs".

Trung vị 2025 [y2025]: $5,124 [cost_median] (một nửa số người trả trong khoảng $3,443 [cost_p25] – $8,270 [cost_p75]). Khoản nhỏ: $3,667 [cost_small], bằng 3.4% khoản vay [share_small]. Khoản lớn conforming: $5,514 [cost_large], 0.8% [share_large]. Mọi quy mô: 1.5% [share_median]. Phí gần như không đổi theo quy mô, nên phần trăm chênh nhau rất lớn.

## 4. Người xem thường nghe gì

- Vạch một điểm: không khẳng định là quy tắc phổ biến (chưa có nguồn, `ctx_rule1pct`); lời nói "You may have heard…", rồi người phân tích thử "1-point line" [s10].
- Phép chia hiển nhiên: phí ÷ số tiền trả hằng tháng giảm được. Không nói "máy tính online dùng công thức này" (chưa có nguồn, `ctx_formula`); trình bày như phép tính ai cũng làm được.

## 5. Điều họ không biết

- Quy tắc một điểm không nhìn phí, quy mô khoản vay, hay thời gian họ còn ở trong nhà.
- Phép chia bỏ qua việc khoản mới bắt đầu lại 30 năm nên trả gốc chậm hơn (`review-m1b/break-even-methods.md`).
- Câu hỏi đúng: "với khoản vay của tôi, giảm bao nhiêu thì phí được trả lại trước khi tôi bán hoặc chuyển đi?"

## Cần DATA tìm nguồn (trạng thái theo numbers.md §6b)

| Dữ kiện | Trạng thái | Cách xử lý trong kịch bản |
|---|---|---|
| Trích nguyên văn quy tắc 1% | CHƯA DÙNG ĐƯỢC | không khẳng định; lời dùng "You may have heard… We tested that one-point line" [s10] |
| Công thức phí ÷ tiết kiệm của máy tính | chỉ có ví dụ CFPB, không công thức | trình bày là phép chia của người xem |
| Tỉ lệ khoản đang lưu hành lãi ≥ 6% (NMDB) | CHƯA DÙNG ĐƯỢC | thay bằng [purch23_ge7] |
| Số năm ở nhà trước khi bán (NAR/AHS) | CHƯA DÙNG ĐƯỢC | hỏi người xem; dùng kịch bản 3 và 7 năm [y3, y7] ILLUSTRATIVE |
| PMMS: 20% trả trước, tín dụng tốt | chờ xác minh | không nói |
| Chuỗi số khoản vay lại 2021–2024; đáy 5.98% (2026-02-26) | chưa có claim ID | không dùng |

## Logline ứng viên (EN)

1. In October 2023, a household locked in the highest mortgage rates since 2000; three years later, we measure exactly how far rates must fall before a refinance pays back what it costs.
2. A one-point drop treats a small loan and a large loan the same way; we test that line on three households to see where it holds and where it breaks.
3. For households who borrowed at the 2023 peak, we find the rate drop at which the loan costs of a refinance actually come back, and why it is different for every loan.
