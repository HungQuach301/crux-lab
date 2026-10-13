# REVIEWER C3 — Tập 7 (headless khoá Console, $1,42)

**KẾT LUẬN: ĐẠT có sửa.** Không có lỗi CHẶN: số khớp claim, mốc ngày đúng, cổng gốc chạy đúng ý đồ ghi trước. Nhưng có 5 lỗi CHÍNH, gồm sai hình–số và gói tự làm trái luật "lặp ≥ 2 nguồn" của chính nó. Sửa chữ trong gói rồi mới gửi chủ dự án.

**Phần đạt (đã kiểm)**
- **Số trên 10 khung:** $120 · $320,000 · $2,828 · $2,948 · $21,622 · $733 · $8,792 · 184/4 · 7.40% đều là đoạn của cột Hiển thị. Không có số ngoài claim. Ghi "week of Oct 8, 2026", không có "this week".
- **Bảng §2 khớp `scores.json`** (r1, s01x, r2). Khoá nhãn được commit trước khi chấm, đọc từ `.git/logs/HEAD`: e5f6ff0 → 98d27d1/d131380, df58dfc → eed2dab. Mỗi đoạn 2 người đọc, người thứ 3 chỉ cho S01, đúng ý đồ.
- **Không câu trích nào thật ra là `advice_stated`.** Cả hai câu S06 v2 "15-year is cheaper" đều được người đọc tự ghi là suy luận của mình, và hình chỉ nêu giá.
- Không còn "has to clear". Màu: `accent` không dùng sai, bó/lát là `warn`, thanh là `ink-muted`. Chữ ≥ 40 px quy về 1080.

**CHÍNH**
1. **S21 khung 5 (`s21-track-5.png`): hình mâu thuẫn số.** Còn một ô `warn` thò qua vách ở góc dưới phải, trong khi nhãn ghi "to finish in 180 months". Đạo diễn đã nêu (#3, 23,67 s) nhưng gói bỏ sót. Thêm vào hàng chờ C4 nguyên văn: *"S21: ô warn sót ngoài vách khi nhãn '180 months' hiện — sai hình–số, sửa bắt buộc (không phải gu)."*
2. **S21: nhãn "+$733 a month" đọc lệch gốc cộng.** Nhãn đứng ngay sau "pay $2,828…", và người đọc 7a05174c hiểu là cộng $733 trên $2,828 (đúng ra $2,828 chỉ cần thêm $120). Nhãn đề xuất: *"to finish in 180 months: required $2,216 + $733 a month"* (claim `pay30_now`, `extra_principal_needed_now`).
3. **S25: đô la "any other use" đọc thành "đã ngang/vượt", và chữ trên hình mất "risk".**
   - Đạo diễn #4 và cả 2/2 người đọc cùng thấy: "a second cash bill extends the bar"; "would have to beat 7.40% to be worth more"; "a guaranteed saving"; "saving is certain".
   - Như vậy là lặp ≥ 2 nguồn, nên theo luật của chính gói phải sửa, không để hàng chờ. §2 chỉ trích câu "compare…", bỏ các câu overclaim này.
   - Sửa hình: đô la thứ hai đứng tách khỏi đầu thanh, độ cao để mở (bóng đứt).
   - Nhãn: *"not tested: how any investment compares, once risk and taxes count"*.
   - Thêm vào §2: *"S25 (2/2, không cờ): 'guaranteed saving' / 'would have to beat 7.40%' — overclaim, sửa ở C4."*
4. **S01: chồng tiền bị đọc thành tiền tiết kiệm (3/3 người đọc).**
   - 6105a63f: "saves money… she saves that much each month"; ee8ce477: "or the savings"; a7993609: "a monthly saving". Đạo diễn #3 cũng nói vậy.
   - 6105a63f bịa nguyên nhân và đọc ngược dấu (chi phí thành tiết kiệm) mà vẫn được 1 điểm, trong khi ee8ce477 bịa nguyên nhân chỉ được 0,5. Chấm cùng chuẩn thì S01 chỉ 1/3, tức TRƯỢT.
   - Câu §3 "S01 giữ" trái luật lặp ≥ 2 nguồn. Thay bằng: *"S01: 3/3 người đọc thấy chồng là 'tiết kiệm' (đạo diễn #3 cũng vậy) — sửa ở C4: nhãn 'fallback price: $120 a month'; đo lại cổng gốc."*
5. **S23 và câu hỏi 2 (`cushion`): lý do và dữ kiện trong gói không đúng.**
   - Cả 2/2 người đọc S23 thấy ô teal là "payments still owed / to come". Họ không nhận ra khối là tiền trả thêm và "không biết 4 tháng muộn hơn cái gì", vậy mà được 1·1. Nghĩa là vai `cushion` không được đọc ra.
   - Ở S21 lớp phủ teal: 58c62277 chỉ tả đúng "the tiles turn green" và gắn với "+$733"; 7a05174c tả "the tiles turn teal". Cả hai không đọc ra màu đó nghĩa là khoảng đường lui.
   - $733 không "lấy từ khoảng đường lui": `cushion` là khoảng $613 (beats.md, Colour roles). $733 = $613 + $120, và chính $120 đó tô `warn` ở S06. Cùng một đô la mang hai màu.
   - Câu 2 viết lại nguyên văn: *"Phần trả thêm $733 = $613 (khoảng đường lui, cushion) + $120 (giá đường lui, warn ở S06). Hiện tô cả $733 cushion; S23 2/2 người đọc thấy teal là 'khoản còn nợ'. Khuyến nghị: tô hai lớp (cushion $613 + đỉnh warn $120) hoặc `ink`; đo lại ở C4."*
   - Nhãn S23 đề xuất: *"ends in 184 months: 4 months later than monthly"*.
   - Câu 1 viết lại: *"Duyệt có điều kiện: W11 vào visual-library §5 sau khi C4 đo lại S21/S23."*

**PHỤ**
- **S06 r2 (`s06-stack-2.png`):** nhãn "$2,948" hiện khi thanh 30 năm còn dưới vạch $2,828 (đạo diễn r2 #2). Ghim nhãn vào đỉnh thanh, thêm vào hàng chờ C4.
- **"Tessa · ILLUSTRATIVE" chồng lên mái nhà** ở S01, S06, S25; ở S21/S23 nhãn nằm trên nhà, xa hình người. "$120 a month" đè mép tường ở `s01-stack-3`. Thêm vào hàng chờ C4.
- **Đồng bộ S06 v2 tụt từ 4/5 (r1) xuống 3/5.** Ghi rõ đây là hồi quy, không chỉ "sửa ở C4".
- **ElevenLabs lệch 5.947 ký tự.** Thêm: *"Nghi phiên K song song dùng cùng khoá; giọng cả tập ước ~N ký tự < 72.750 nên không cần dừng hỏi."*
- **Chi phí REVIEWER còn để trống.** Điền số thật vào §5.
- **Tệp lệch nhau, cần cập nhật:**
  - `world/c3/README.md`: dòng "principal" (numbers.md đã có claim); bảng S21 26,69 s · 5/7 khác `spans.json` 26,29 s và gói 6/7.
  - `beats.md`: B01 cột claim còn `interest_15_now` thay vì `principal`; B06 chữ trên hình chưa đổi sang "extra paid", chưa thêm "$2,828" và "required: $2,216".
  - `numbers.md`: dòng 6 có ghi S23.2 nhưng script không có mốc ngày ở đó.
- **W3 `Beam` "đứng yên"** theo library §5, nhưng S25 cho thanh dâng lên. Ghi đây là ngoại lệ có lý do.

**Câu hỏi cho chủ dự án:** rõ ràng và có khuyến nghị. Nhưng câu 1 và câu 2 phải viết lại như mục CHÍNH-5 trước khi gửi.
