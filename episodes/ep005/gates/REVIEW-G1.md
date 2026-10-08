# REVIEWER — gói G1 Tập 5 · 2026-10-06

Đã đọc: `episode.md` §1, §3.9, §8; CHARTER §5; `gates/G1.md`; đối chiếu `C1-logline.md`, `C1-blind.md`, `C2-blind.md`, `REVIEW-C2.md`, `ledger.md`, `PLAN.md` §5, `numbers.md`, `data/sources.json` (provisions), `story/script.md`, `story/beats.md`, `review-g1/table-read.json`, `model/independent/report.md`. Chạy `check_script.py`: **ĐẠT** (70 câu, ≈ 8:19, khuôn hook +4,0 · limits −4,8).

## Kết luận: **ĐẠT có sửa** (8 sửa chữ trong G1.md; kịch bản không có lỗi CHẶN mới)

## (1) Đối chiếu số
Khớp: cold open H-A = S01.1–S02.2 nguyên văn; M1 2,8 · M2 22,84 · M3 8,96 · M4 9,41 · M5 29,25 s (table-read.json, đúng chữ S01–S04 hiện tại); vòng 1 M4 10,08 s (ledger); 23 tháng, ≈ 8 năm (99 kỳ), 1/7 (14,7 %), 10/2005 · 112, Owen 13 · Grace 23 · Victor 112; 58,6 % / 15,6 %; 55/55; kiểm mù C1 2/2 + 2/2, C2 vòng 1 S19 4/6, vòng 2 6/6 · khuyên 0 · S18 3/6; 8,9 / 36 nghìn mỗi lượt; EL 1.234 + 410 = 1.644. Token cộng từ ledger: kiểm mù 0,300 · dựng 0,249 · WRITER 0,311 (78 %) · checks 0,072 · REVIEWER 0,121 thực → tổng 1,45 chỉ đúng khi tính REVIEWER G1 ≈ 0,1 và điều phối ≈ 0,3 là **ước**.
Sai/không khớp: khuôn tỉ lệ cold open +4,5 (thực +4,0); "7/9 nhịp then chốt loại 1" (beats: 8/9, chỉ KEY-1 loại 2); "headless 26 lượt" (ledger: 3 × (6 + 1) = 21); "Agent 12/40" (ledger 10 + REVIEWER G1 = 11); danh sách "5 CHẶN → đã sửa" trộn CHẶN với CHÍNH (MSPUS = K-2, hình cột = K-1) và nói đã sửa cả nguồn luật, trong khi C-3 (nguồn mốc 75 %) vẫn treo — chính là ngoại lệ.

## (2) Ngoại lệ 75 %
Đúng loại ngoại lệ (CHARTER §5 "số không xác minh được nguồn"), khuyến nghị (a) hợp lý. Hai chỗ chưa đúng:
- G1 khẳng định "là quy định của Fannie Mae/Freddie Mac (B-8.1-04, 8203.2)" như đã biết — chưa trích được nên phải nói là chưa kiểm.
- Phương án (b): số 58,6 % đúng claim (`shareA_ltv24_le80`) nhưng **đảo nghĩa**, không chỉ "đổi nghĩa": 58,6 % là đa số, nên S12.4 "clearing a lender's early bar by then was not [common]" thành sai và đối trọng "trên giấy ≠ gỡ" mất số đỡ. 80 % ở 2 năm cũng không được gọi là "mốc sớm của bên cho vay". Phạm vi (b) còn thiếu S12.4, S18.4 ("not the lender's step") và hình B03, B09, B12, B18 (đường 75 %, nhãn "often 75% in early years").

## (3) Thiếu / nói quá
- Logline L2 bị cắt bằng "…" che câu "Most buyers expect close to a decade of insurance, because that's how long the payment schedule takes to reach 80% of the price" — cùng kiểu lỗi C-1 (gắn việc hết bảo hiểm với 80 %), lại là phỏng đoán "most buyers". Chủ dự án duyệt logline nên phải thấy câu này.
- Danh sách host bị chặn: `sources.json` ghi fanniemae/freddiemac/files.consumerfinance.gov/fhfa.gov/federalregister.gov; "ecfr, govinfo" không có trong hồ sơ.

## (4) Kịch bản hiện tại
Không có lỗi CHẶN mới. Không khuyên (S01.2 là câu hỏi; S18.4 điều kiện, không mệnh lệnh; S18.6 đối trọng), không dự báo (S03.5, S20.3). Luật: S07.1 (xin huỷ ở 80 % giá trị gốc theo lịch, 4901(2)(A)/4902(a)), S08.1 (tự hết ở 78 %, đang trả đúng hạn, 4902(b)), S09.1 (gỡ theo giá trị = chuẩn riêng của bên cho vay, CFPB) đúng; S17.4 thận trọng đúng (4902(a)(4) giá trị không giảm — Victor có chỉ số dưới giá gốc). Số S10.1 (1/1991–7/2016), S05.1 (Q2), S20.2 (13 → 112 tháng) khớp claim. Rủi ro còn lại chỉ là 75 % (S03.3, S12.3–S12.4, S18.4) → ngoại lệ. Hàng chờ (không chặn): `numbers.md` vẫn gọi người mua là Nora/Ben/Carla, kịch bản dùng Grace/Owen/Victor — thống nhất trước khi chốt.

## (5) Độ dài
3 câu + 1 ngoại lệ, đúng §1. "Ghi chú" có thể gọn hơn nhưng không bắt buộc.

## Sửa G1.md (cũ → mới)
1. `Khuôn tỉ lệ: cold open +4,5 và giới hạn −4,8 điểm %` → `Khuôn tỉ lệ: cold open +4,0 và giới hạn −4,8 điểm %`
2. `(7/9 nhịp then chốt là loại 1)` → `(8/9 nhịp then chốt là loại 1)`
3. `gói C2 ĐẠT có sửa (5 CHẶN → đã sửa: câu móc nói sai luật 80 %, mô tả MSPUS, dải năm, hình cột, nguồn luật)` → `gói C2 ĐẠT có sửa (5 CHẶN: C-1 câu móc sai luật 80 %, C-2 dải năm, C-4 nguồn 4902(a), C-5 claim định tính → đã sửa; C-3 nguồn mốc 75 % → còn treo, xem ngoại lệ; thêm 2 CHÍNH sai nghĩa đã sửa: MSPUS, hình cột)`
4. `REVIEWER ≈ 0,22/0,45` → `REVIEWER ≈ 0,22/0,45 (0,12 thực + ≈ 0,1 ước cho soát G1)`; `Agent 12/40; headless 26 lượt` → `Agent 11/40; headless 21 lượt`
5. `là quy định của Fannie Mae/Freddie Mac (Servicing Guide B-8.1-04, 8203.2), nhưng` → `theo máy là quy định của Fannie Mae/Freddie Mac (Servicing Guide B-8.1-04, 8203.2) — chưa kiểm nguyên văn vì`
6. `**fanniemae.com, freddiemac.com (và ecfr, govinfo, federalregister) bị proxy chặn**` → `**fanniemae.com, freddiemac.com (và files.consumerfinance.gov, fhfa.gov, federalregister.gov) bị proxy chặn**`
7. Dòng (b) → `(b) Bỏ "75 percent" khỏi lời và hình: S03.3 → "lender policy: request, appraisal, minimum time"; S12.3–S12.4 bỏ 15,6 %, chỉ nói định tính có nguồn CFPB ("lenders set their own standards for removal on value"); S18.4 bỏ "the lender's step"; hình B03/B09/B12/B18 bỏ đường 75 %. **Không** thay bằng 58,6 % (≤ 80 %): đó là đa số, làm đảo kết luận S12.4 và mất đối trọng "trên giấy ≠ gỡ". Cần WRITER mới + kiểm lại M4 + kiểm mù lại S12.`
8. Sau câu trích logline L2, thêm: `Câu bị lược: "Most buyers expect close to a decade of insurance, because that's how long the payment schedule takes to reach 80% of the price" — gắn việc hết bảo hiểm với 80 % (kiểu lỗi C-1); nếu duyệt L2 thì dùng: "On the schedule alone, you can't even ask to cancel it for about 8 years."`
