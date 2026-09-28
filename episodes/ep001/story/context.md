# Tập 1 — Bối cảnh (context)

Mục đích: thế giới người xem đang sống, trước khi có nhân vật hay con số nào của nhân vật. Mọi dữ kiện dưới đây do WRITER tự tính từ CSV trong repo; mỗi dòng ghi file · chuỗi · ngày. Nguồn gốc: `F` = `data/normalized/mortgage30_weekly.csv` (FRED `MORTGAGE30US`, Freddie Mac PMMS, lãi trung bình 30 năm cố định, theo tuần, danh nghĩa; tải 2026-09-28, xem `data/sources.json`). `H` = `data/normalized/hmda_refi_costs.csv` (HMDA, CFPB/FFIEC; lọc: khoản vay thế chấp thứ nhất, 30 năm, đã giải ngân, có `total_loan_costs`; xem `data/hmda-sources.json`). Chờ DATA gán claim ID trong `numbers.md`.

## 1. Chuyện gì đã xảy ra với lãi suất

- **Đáy:** 2,65% tuần 2021-01-07 — mức thấp nhất của cả chuỗi (2.896 tuần, từ 1971-04-02). [F]
- Lãi dưới 3% trong 55 tuần, từ 2020-07-16 đến 2021-11-10. [F]
- **Đỉnh:** 7,79% tuần 2023-10-26 — cao nhất kể từ tuần 2000-11-10 (cũng 7,79%). [F]
- **Tháng 10/2023** (tháng các hộ minh hoạ vay): bốn tuần 7,49 · 7,57 · 7,63 · 7,79; trung bình 7,62%. [F]
- **Sau đó lãi giảm nhưng không thẳng:** chạm 5,98% tuần 2026-02-26 (thấp nhất kể từ tháng 10/2023), rồi đi lên lại. [F]
- **Mức mới nhất:** 7,03% tuần 2026-09-24 — thấp hơn trung bình tháng 10/2023 là 0,59 điểm. [F]
- **"Cửa sổ 1 điểm" đã mở rồi đóng:** lãi thấp hơn 7,62% ít nhất 1 điểm (≤ 6,62%) trong 67 tuần kể từ tháng 11/2023; đợt dài nhất kéo dài từ tuần 2025-08-14 đến tuần 2026-07-23; từ 2026-07-30 lãi lại trên 6,62%. [F]

Luôn nói kèm: "history, not a forecast"; "US only"; PMMS là mức trung bình toàn quốc, không phải lãi của một hộ cụ thể. Freddie Mac đổi phương pháp PMMS ngày 2022-11-17 (trích dẫn ở `data/sources.json`).

## 2. Ai đang ở trong hoàn cảnh này

Những hộ vay mua nhà hoặc vay lại khi lãi ở gần đỉnh 2023. Họ ký ở mức cao nhất trong hơn hai mươi năm, trong khi người vay năm 2021 trả dưới 3%. Ba năm sau, họ thấy lãi trên bảng tin thấp hơn khoản vay của mình, và câu hỏi tự đến: "giờ vay lại có đáng không?"

Dữ liệu HMDA cho thấy làn sóng vay lại (rate-and-term, mã 31) co lại rồi quay về [H]:
- 2021: 3.089.298 khoản; 2023: 97.298 khoản; 2024: 307.588; 2025: 488.241.

## 3. Vay lại không miễn phí

Phí đóng hồ sơ (`total_loan_costs`) trung vị của khoản vay lại rate-and-term, năm 2025 [H]:
- mọi quy mô: $5.124 (khoản vay trung vị $375.000);
- dưới $150k: $3.667; $750k trở lên: $5.034.

Phí gần như không theo quy mô khoản vay, nên với khoản nhỏ nó là phần trăm lớn (3,41% trung vị), với khoản lớn là phần trăm nhỏ (0,47%). [H, cột `cost_p50_pct`, 2025]

## 4. Người xem thường nghe gì

- Quy tắc truyền miệng: "chỉ vay lại khi lãi giảm ít nhất 1 điểm." (cần nguồn, xem dưới)
- Công thức của phần lớn máy tính online: hoà vốn = phí ÷ số tiền trả hằng tháng giảm được. (cần nguồn)

## 5. Điều họ không biết

- Quy tắc 1 điểm không nhìn phí, quy mô khoản vay, hay thời gian họ còn ở trong nhà. Cùng một mức giảm có thể hoà vốn nhanh với khoản lớn và rất chậm với khoản nhỏ (số cụ thể chờ `numbers.md`).
- Công thức "phí ÷ tiết kiệm tháng" bỏ qua việc khoản mới bắt đầu lại 30 năm nên trả gốc chậm hơn; khoản cũ càng lâu năm, chênh lệch càng lớn (`review-m1b/break-even-methods.md`).
- Vì vậy câu hỏi đúng không phải "lãi giảm bao nhiêu" mà "với khoản vay của tôi, giảm bao nhiêu thì phí được trả lại trước khi tôi bán hoặc chuyển đi".

## Cần DATA tìm nguồn

| Dữ kiện muốn dùng | Vì sao câu chuyện cần | Nguồn sơ cấp gợi ý |
|---|---|---|
| Câu "refinance when rates drop 1%" là lời khuyên phổ biến | Đây là "điều người xem thường nghe" mà tập kiểm chứng | Bài/FAQ của Freddie Mac hoặc Fannie Mae; CFPB; hoặc trích nguyên văn một bài báo lớn (ghi rõ là truyền miệng, không phải khuyến nghị chính thức) |
| Máy tính hoà vốn dùng "phí ÷ tiết kiệm tháng" | Đặt ra cách tính mà tập chỉ ra giới hạn | Trang refinance calculator/hướng dẫn của CFPB, Freddie Mac, Fannie Mae |
| Bao nhiêu khoản vay đang có lãi ≥ 7% / vay năm 2023 | Cho người xem thấy "không chỉ mình tôi" | FHFA National Mortgage Database (phân bố lãi khoản đang lưu hành) |
| Chủ nhà thường ở bao lâu trước khi bán | Nối hoà vốn với mốc bán 3 và 7 năm | NAR Profile of Home Buyers and Sellers (median tenure); hoặc American Housing Survey (Census) |
| PMMS mô tả người vay nào (điểm tín dụng, trả trước) | Nói rõ lãi của một hộ có thể khác trung bình | Trang phương pháp PMMS của Freddie Mac |
| Phí đóng hồ sơ gồm những gì | Giải thích $5.124 là gì cho người xem | CFPB Closing Disclosure; HMDA filing guide (định nghĩa `total_loan_costs`) |

## Logline ứng viên (EN)

1. In October 2023, a household locked in the highest mortgage rates since 2000 — three years later, we measure exactly how far rates must fall before a refinance pays back what it costs.
2. The "refinance when rates drop 1%" rule treats a small loan and a large loan the same way; we run three households through the real numbers to see when it holds and when it breaks.
3. A refinance window opened for almost a year and then closed; for households who borrowed at the 2023 peak, we find the rate drop at which the closing costs actually come back.
