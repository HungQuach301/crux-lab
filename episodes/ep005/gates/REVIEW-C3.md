# REVIEWER — gói C3 Tập 5 (2026-10-07)

**Kết luận: ĐẠT có sửa** (6 sửa chữ trong `gates/C3.md`; clip: 0 CHẶN).

## Đã soát
- Nguồn: `C3.md`, `C3-root.md`, `C3-root-intent.md`, `SPINE-PLAN.md`, `FIX-R2.md`, `FIX-R3.md`, `spans.json`, `c3/root*/scores.json` (+ `key.json`, `grade.json`), `c3/coldopen/r1/scores.json`, `S03-S12-blind.md`, `ledger.md`, `git show 6d17055:moc-v/seg/ep005/scene.js` (E5g).
- Hình: dải N1/N2/N3, hai ảnh r1-vs-r3, 84 khung (1 khung/s) của `c3-clip.mp4`. Âm: ASR `small.en` trên cả clip và trên take S03 `voice-takes/220fafe74f150378.mp3`.

## Số khớp nguồn
- Token 1,13 tr: agent 330.196 + 173.397 + 146.806 = 0,65 · kiểm mù C3 tắt tiếng 83.966 + 80.368 + 75.745 = 0,24 · cold open 57.773 = 0,06 · S03→S12 78.878 = 0,08 · điều phối 0,10 (không có dòng ledger, chấp nhận ước). Cả tập ≈ 2,9 tr: khớp (PLAN 1,45 tr tới G1 + REVIEW-G1, contract, R1 + 1,13).
- EL: 1.234 + 410 + 4.887 + 938 + 1.266 + 443 = **9.178** ✓. Giờ render 0,10 + 0,07 + 0,05 = 0,22 h ✓. Đồng bộ 11 + 4 + 5 + 5 = 25/25 ✓. Spine 20 cảnh, 4/14/2, 31 %/69 %, 21 lần chuyển chế độ, 15 động tác ✓. Cold open E1 2/2 · E2 2/2 · khuyên 0/4 ✓. N1 0/2 → 0/3 → 1/3, N2 0/2 ×3, N3 2/2 ✓. Clip 82,53 s ✓.

## Sai hoặc thiếu (cần sửa)
1. **Nghĩa N1 không phải 3/3 ở mọi vòng:** vòng 1 có 2 người đọc (2/2).
2. **Lỗi E5k bị nói quá:** bản E5g mà chủ dự án chấm L3 KHÔNG có lỗi. Ở commit 6d17055, dòng `slow.material.opacity = …` vẫn là mã chạy. Lỗi chỉ có từ E5h, khi sửa màu làm dòng này rơi vào chú thích (SPINE-PLAN §2 cũng ghi vậy).
3. **Thiếu việc đổi đáp án tắt tiếng trước vòng 3:** muted read N2 đổi từ "turn warn" sang "are set apart in their own colour" (`spans.json`, `muted_read_note`). `FIX-R3.md` lại ghi "không sửa". Đổi đáp án sau khi đã thấy kết quả vòng 1–2 thì phải nêu trong gói.
4. **Người chấm dao động chưa nói hết hệ quả:** nếu giữ lần chấm đầu, N1 vòng 2 là 1/3, ngang vòng 3. "Vòng 3 tốt nhất" vì vậy nằm trong sai số của người chấm. Câu "nhãn bổ sung được chấm riêng" bị viết nhầm: người được chấm riêng là người đọc thứ 3 (`root-r3x`). Lần kiểm S03→S12 cũng phải chấm lại vì rubric thiếu định nghĩa. Ngoài ra, các lần kiểm "có lời" (C2 v2, S03→S12) chỉ dùng **chữ**, không có hình N1/N2.
5. **Hướng dẫn nghe S03 sai chỗ:** clip dừng cold open ở S03.2 (34,7 s), nên S03.3 không có trong clip, và đoạn 0:31–0:42 chỉ là S03.2 cùng phần đầu N1. ASR xác nhận dấu hỏi ở take `220fafe7…` 0:08–0:15. Vì vậy nhãn `Fannie Mae: wait ≥ 2 years · loan ≤ 75%` cũng chưa thấy được trên hình: chữ ở SPINE-PLAN khớp nguyên văn, nhưng phải kiểm ở C4.
6. **Phương án (b) để trống hướng:** N1 là hình duy nhất thiếu dòng đối trọng. Cold open có "A measurement, not a next step", N2 và N3 có "not a reason to buy, rent or wait". Nên đưa thiếu sót này ra làm hướng cụ thể để chủ dự án chọn.

## Sửa chữ cho `C3.md` (cũ → mới)
1. `| N1 lịch | 3/3 ở mọi vòng |` → `| N1 lịch | 2/2 → 3/3 → 3/3 |`
2. `Bản anh chấm L3 (E5g) và các vòng mù E5j/E5k đều chạy trên bản có lỗi này.` → `Lỗi có từ E5h (khi sửa màu); bản anh chấm L3 (E5g) không có lỗi, nhưng các vòng mù E5j/E5k chạy trên bản có lỗi.`
3. Thêm sau gạch "Ba vòng đều sửa…": `- **Đổi đáp án trước vòng 3:** muted read N2 "turn warn" → "are set apart in their own colour" (theo đổi màu, nghĩa giữ; ghi ở spans.json).`
4. `- **Người chấm dao động:** chấm lại cả bộ ở vòng 2 đổi một người đọc từ "không khuyên" thành "khuyên". Từ vòng 3, nhãn bổ sung được chấm riêng.` → `- **Người chấm dao động:** chấm lại cả bộ ở vòng 2 đổi một người đọc N1 từ "không khuyên" thành "khuyên" (theo lần chấm đầu, N1 vòng 2 là 1/3, ngang vòng 3). Từ vòng 3, người đọc thứ 3 được chấm riêng. Kiểm S03 → S12 cũng chấm lại một lần vì rubric thiếu định nghĩa.`
5. `Khi có lời, kiểm mù không thấy câu khuyên: C2 vòng 2 0/6, đoạn S03 → S12 0/6.` → `Kiểm mù bằng lời (chữ, chưa có hình N1/N2) không thấy câu khuyên: C2 vòng 2 0/6, đoạn S03 → S12 0/6.`
6. `anh nghe ở 0:31–0:42 của clip` → `S03.3 không có trong clip (clip dừng ở S03.2); anh nghe take `voice-takes/220fafe74f150378.mp3` 0:08–0:19`. Thêm: `Nhãn Fannie Mae (S03.3) chưa có trên hình C3; kiểm ở C4.`
- Gợi ý cho (b): `(b) Thêm vòng sửa ngoài 3 vòng — vd N1 thêm dòng đối trọng "A measurement, not a next step" (N1 là hình duy nhất thiếu dòng này).`

## Chữ trên hình (clip + dải)
- **R1: 0.** Không có số tiền phí PMI ở đâu. `$2,362/month · principal + interest`, `$360,000 loan` và `6.86%` là các số được phép.
- ILLUSTRATIVE: có ở cold open (lịch), S03.1 (hai chồng), N1, N3 (phần thế giới) ✓. "US only · history, not a forecast": có ở bó đường, N3 khi đồ thị, N2 ✓.
- Quy tắc 1: số chỉ hiện ở đồ thị chính diện. Ở thế giới chỉ có tên ("You", "loan", "typical", "a long tail", "insurance still on") ✓. Ghi chú nhỏ: "typical" và "a long tail" ở N2 thế giới là nhãn so sánh không có số. SPINE-PLAN cho phép, nhưng nên xác nhận khi dựng S13.
- Nhãn mới ≤ 8 từ: "loan balance schedule · set on day one" (7), "each bar's height: months to 80% on paper" (8), "one stretch of purchase months" (5) ✓.
- Nhãn Fannie Mae: không có trong clip (xem sửa 5).

## Phương án và khuyến nghị
- (a) công bằng: nêu rõ là ngoại lệ của luật khoá nghĩa, có cổng chặn ở C4 (bản có lời, S06/S13 phải 0 khuyên). Chứng cứ ủng hộ: câu khuyên giữ cùng dạng qua 3 lần sửa hình, nghĩa luôn đúng, và cold open (cùng nội dung chậm/nhanh) đạt 0/4 khi có dòng đối trọng.
- (c) nói đúng đánh đổi. Câu "khả năng cao vẫn còn câu khuyên" là suy đoán, chấp nhận được.
- (b) cần một hướng cụ thể (gợi ý trên).
- **Khuyến nghị (a): có cơ sở.**

## Hợp với chủ dự án
Gói ngắn, câu hỏi rõ, dòng trả lời gọn. Sau 6 sửa trên vẫn ngắn.
