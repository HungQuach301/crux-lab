# REVIEWER · gói G2 Tập 4 (+ soát bù gói C3) — 2026-10-06

REVIEWER độc lập (Opus), chỉ đọc. Checklist `quality-framework.md` §7 (1–5), §5, §6, §8; `episode.md` §5; `prompts/P3.md` việc 4; D-008; `checks-appeal.md` A9; `topics-r1/machine/tax-2/claim-risk.md`.

## Kết luận: **TRƯỢT** (1 CHẶN · 7 CHÍNH · 9 THAM KHẢO)

Sửa CHẶN và CHÍNH đều là sửa chữ trong gói/sổ, thêm một lượt chấm lại theo ý đồ ghi trước, và dựng lại **chỉ thumb-1**. Không cần dựng lại video ngoài 3 cảnh mà phương án (b) đã nêu.

**Đã kiểm, ĐẠT:**
- `contract.json`: kind `fixed-cap-vs-index-growth`, `params` khớp `checks-runs/K38/ep004-kind.json`, khớp đủ, output `out/model.json`.
- `out/claims.json`: 131 claim. Giá trị không lệch giá trị chưa làm tròn trong `out/model.json` raw (0 lệch).
- Thumbnail: mọi chữ và số trên `thumb-1..3` đều có claim và đúng display: 11, 12, ×3.1, 2023 Q2, ≈ $114,700, ≈ $373,400, $300,000, May 1997. Độ dài thanh T1 đúng tỉ lệ (Chicago ≈ $401,700, Miami ≈ $1,308,000).
- `description.md`: mọi số có claim và khớp. Gồm $558,100, ×3.8, Q2 2022 và Q2 2023, 5/12 và 11/12, Miami Q4 2006 và Q2 2019, 12 ngưỡng, ≈ $243,500 và ≈ $121,700, ≈ $1,046,000 (`excl_joint_1997_in_now`).
- Không có câu khuyên hay dự báo (S10) trong mô tả và thumbnail. Chân "US only · history, not a forecast" có trên cả 3 thumbnail. ILLUSTRATIVE có trên T1 và T2. T3 là ngưỡng, không phải illustrative, nên không cần.
- `out/script.json`: `role: hook` là S01.1, `role: promise` là S01.3. Điều kiện "rose like the average" nằm ở S01.2 và S01.3.
- Ý đồ ghi trước, không sửa sau kết quả:
  - `C3-intent` (2bf3439) có trước vòng 1.
  - `C4-blind-intent` (f73f8eb) có trước e65450c.
  - `C4-root-intent` (df3b5a1) có trước câu trả lời 4ab23b4.
  - Cả ba chỉ có một commit. Rubric gốc C4 (`review-c4/root/rubric.md`) chép đúng nguyên văn "muted read" trong `story/beats.md`.
- Gói G2 có 3 câu, mỗi câu có khuyến nghị. Đã nêu: cổng gốc 4/7, S18 2/4, so cặp thumbnail chỉ một người đọc.
- C5: SH01–SH05 ĐẠT cả 3 Shorts (`C5.md:8`, `report.md:74-78`). CHÍNH 10 dòng không đạt, cả 10 có giải thích trong `out/explanations.json`.

## CHẶN

1. **`gates/G2.md:12,21` và `gates/C4-root.md:52,56`: báo sai nguyên nhân trượt cổng gốc; B11 không đạt.**
   - **Cờ khuyên bị bỏ qua.** Bảng chấm độc lập `review-c4/root/scores.md` có 3 cờ khuyên tính theo A9:
     - B06 `a2a37b58` (chắc): "shouldn't wait on a sale";
     - B10 `9c8e7df4` (yếu): "how I time the sale";
     - B11 `79af2335` (biên): "while I decide when to sell".
   - **Luật áp dụng.** Theo §5.6, "có câu khuyên thì nhịp trượt ngay". Theo §5.8, có câu khuyên ở bất kỳ nhịp nào thì cổng trượt. Ý đồ C4 không được nới khung.
   - **Hệ quả cho B11.** B11 phải TRƯỢT ngay sau người đọc 1, không được gọi người thứ 3. Người thứ 3 lại do **điều phối tự chấm**. G2 không nói điều này.
   - **Kết quả thật:** cổng gốc **3/7 = 43 %**. Cổng còn trượt vì câu khuyên, không chỉ vì nhãn. G2 viết "trượt vì nhãn, không vì nghĩa lời" và "A9 khuyên_tính 0/12". Con số 0/12 chỉ đúng cho C3, đặt ở đây gây hiểu lầm.
   - **Sửa câu 1 của G2:** "Cổng gốc 3/7 (B06, B10, B11, B15 trượt). B06, B10 và B11 có cờ khuyên A9 (chờ/canh thời điểm bán): theo §5.6 thì nhịp trượt ngay. B11 trước ghi 2/3 nhờ người thứ 3 do điều phối chấm, nay bỏ."
   - **Sửa phương án (b):**
     - Sửa nhãn B06, B10, B15. Ở B06, B10, B11, thêm đối trọng chống đọc thành "canh thời điểm bán" nếu chủ dự án cho đó là gu.
     - Chấm lại **B06, B10, B11, B15** bằng người đọc mới và người chấm độc lập, theo ý đồ vòng 2 ghi trước (file mới `C4-root-r2-intent.md`). Ý đồ cũ ghi "không vòng 2", nên vòng 2 cần chủ dự án duyệt trong câu 1.
   - **Thêm phương án (b′):** chủ dự án quyết cờ "chờ/canh thời điểm bán" mức yếu/biên có tính theo A9 hay không. Đây là việc đổi luật, cần chủ dự án.
   - **Sửa `C4-root.md:52,56`:** B11 → "TRƯỢT (cờ khuyên người 1, §5.6)", cổng → 3/7. Không cần dựng thêm video ngoài 3 cảnh của (b).

## CHÍNH

1. **`gates/G2.md:12`: không nêu hạn chế của đối chứng âm.**
   - `C4-blind.md:11-14`: hình V4 tự mang một lựa chọn sản phẩm, nên 2/2 người đọc có khuyên_tính. Thận trọng chung chỉ 1/2.
   - Vì vậy điều kiện A9 ("cờ thận trọng chung phải xuất hiện cả ở đối chứng") chỉ đạt một phần, trong khi việc duyệt N1/N2 dựa vào A9.
   - Sửa: thêm vào câu 1 "đối chứng âm có hạn chế (hình V4 mang lựa chọn; thận trọng chung 1/2)".
2. **`out/package/thumb-1.png` / `thumb-1.json` (chữ "11 of 12"), `G2.md:26`: chữ lớn thiếu đơn vị.**
   - Người đọc so cặp (`G2-thumbs.md:7`) đọc thành "most homes like mine blew past the $500,000 limit". Đây đúng là câu nói quá mà claim-risk cấm ("Most 2000 buyers now exceed the limit").
   - Sửa: "11 of 12 metros" hoặc "11 of 12 cities" (claim `metro_count`). **Dựng lại chỉ thumb-1**, không đụng video.
3. **`gates/G2.md:17`: phương án nhãn B10 "vạch dọc tại $800,000 ("gain = $500,000")" dùng số không có claim.**
   - Trong `out/claims.json` không có giá trị 800000.
   - Sửa: chọn vế 1 (tiêu đề đơn vị), hoặc thêm claim `value_at_cap_300k` (300k + 500k) vào `numbers.md`, model và claims trước khi dùng.
4. **`gates/G2.md:33-46`: hàng chờ CHÍNH thiếu L1 (không có lớp sonify).**
   - `out/explanations.json` mục L1 ghi rõ "Queued for G2 as a CHÍNH item".
   - Ngoại lệ C4 (`C4-answer.md:1`) chỉ phủ luật trang, không phủ L1.
   - Sửa: thêm mục "L1 CHÍNH: không có lớp sonify, giữ (ghi nhận)" vào câu 3.
5. **`gates/G2.md:36` (F11): mô tả sai thành phần.**
   - Trong 17 file "không khai", 3 file là `out/package/thumb-1..3.png` thuộc gói G2 (`report.json` F11). Ba file này nay đã có và phiên tự khai được trong `contract.json` (§6.1).
   - Sửa: khai 3 thumbnail vào contract và chạy lại checks. F11 còn 14 file pipeline cũ + `page.json`; P01 (đang MISSING `thumb-1.png`) được đo. Đổi chữ câu 3 mục 1 cho đúng.
6. **`PLAN.md:15` và `ledger.md`: lệch với gói (checklist §7.5).**
   - PLAN vẫn ghi C4 "cổng gốc nhịp loại 1 chưa chạy" và không có dòng C5, G2.
   - `ledger.md` không có dòng cho: kiểm mù gộp C4, trả lời chủ dự án C4, cổng gốc C4 (10+1 người đọc, người chấm), các agent G2 (thumbnail, so cặp, tóm tắt AI) cùng token.
   - Sửa: cập nhật bảng cổng PLAN (C4 XONG TRƯỢT 3/7 sau sửa CHẶN; C5 XONG; G2 CHỜ) và bổ sung các dòng ledger trước khi điền "Token so trần" ở `G2.md:9`.
7. **`gates/G2.md:5`: không nêu tên chỉ số trong ±5 % quanh ngưỡng (checklist §7.3).**
   - Danh sách ở `out/checks/report.md:15-21`: F04 16,61 Mb/s (ngưỡng ≥ 16,0, CHẶN), F06 280 kb/s (≥ 272, CHẶN), F07, A18, S15.
   - Sửa: thêm một dòng. Lưu ý F04/F06 có thể tụt khi mã lại sau (b).

## THAM KHẢO

1. **`gates/G2.md:48-49`:** "Nghe lại rows/rose" thực chất là yêu cầu thứ 4 nằm ngoài 3 câu. Nên gộp thành một mục của câu 3.
2. **`gates/G2.md:34`: Shorts.**
   - SH1 (S06) và SH2 (S10) cắt từ nhịp trượt cổng gốc. Nên khuyến nghị: nếu chọn (a) thì chỉ đăng SH3, chưa đăng SH1/SH2 cho tới khi chấm lại.
   - `C5.md:6` ghi "đối trọng dọc luân phiên 3 s". Cần nói rõ ILLUSTRATIVE và "history, not a forecast" có cùng lúc trên **mọi** khung có số (`episode.md` §5) hay chỉ luân phiên. Nếu chỉ luân phiên thì phải sửa nhánh dọc và dựng lại SH1–SH3.
3. **`out/package/description.md:7`:** "puts a home like the average" → "puts a home that rose like its metro area's average" (claim-risk "Always say"). Chỉ sửa chữ.
4. **`out/package/thumb-2.png` / `G2.md:27`:** ghép "Cap: $500,000 / Prices: ×3.1" dễ bị đọc thành "trần mất 2/3 giá trị". Claim-risk chỉ cho phép nói mất giá theo CPI. Có thể đổi chữ phụ thành "US home prices ×3.1 since 2000 · cap unchanged", hoặc giữ T2 ở vị trí cuối Test & Compare như đề xuất.
5. **`gates/C4.md:20`:** đảo thứ tự thanh S09/S10 (lớn ở dưới) là bố cục, ngoài §6.6 (chỉ nhãn). `C5.md:6` sửa bố cục thanh dọc trong Shorts cũng vậy. Nên liệt kê ở câu 1 hoặc câu 3 để chủ dự án ghi nhận.
6. **`gates/C4-root-intent.md`:** commit df3b5a1 lúc 07:42:27, chỉ trước câu trả lời 4ab23b4 (07:44:24) 2 phút, cho 10 người đọc chạy lần lượt. `rubric.md` commit sau câu trả lời (nội dung chép nguyên văn beats nên không hại). Nên ghi giờ chạy từng người đọc để chứng minh thứ tự.
7. **C3, `gates/C3-intent.md:3`:** hẹn nguyên văn ở `gates/C3-blind.md`, nhưng file này không có; nguyên văn nằm ở `review-c3/r1|r2/answers.md`. Thêm vào đó, `review-c3/r2/answers.md:1` gộp gạch đầu dòng của 2 người đọc, nên không còn nguyên văn (§5.5). Sửa: thêm con trỏ và ghi chú vào `C3-tally.md`.
8. **C3, `design/c3/NOTES.md` (vòng 2):** nhãn B14 "Each rung: the 2000 price where the gain hits the cap" dài 11 từ, vượt mức "≤ ~8 từ" của ý đồ (`C3-intent.md:33`). Chủ dự án đã ký N1/N2 bản này, nên chỉ ghi nhận.
9. **C3, `gates/C3.md:9-10,15`:**
   - Câu 2 và câu 3 không có dòng "Khuyến nghị" (§7).
   - Gói gửi khi không có REVIEWER. D-008 §5 nay cấm làm vậy.
   - Nội dung số của gói C3 trung thực: báo TRƯỢT vì câu khuyên 12/12, nghĩa 6/6, dừng sớm đúng luật.
   - B08/B14 ở C4 dùng lại kết quả C3 vòng 2, đúng ý đồ. Nhưng S14 đã sinh lại giọng (S14.5) sau C3, nên thời điểm khung B14 trong bản cuối có thể khác dải C3.
   - Không cần sửa; ghi vào ledger.
