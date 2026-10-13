# REVIEW G2 — Tập 7 · 2026-10-13 · REVIEWER (chỉ đọc)
**Kết luận: ĐẠT có sửa** — 0 CHẶN · 4 CHÍNH · 5 PHỤ. Sửa xong 4 mục CHÍNH là gửi được, không cần chạy thêm.

**CHÍNH-1 · §1 "6/21 và 7/21":** chấm lại `regrade/` theo luật gộp thận trọng (C4-intent §A: lấy điểm thấp nhất; một người chấm bật cờ là tính) không ra hai số này. Lượt 1 = 5/21 (B04 B08 B10 B23 B25; B15 còn chờ người thứ 3). Lượt 2 = 6/21 (B01 B08 B10 B15 B25 B28; B04 còn chờ). `tally.md` = 7/21 (B09 còn chờ). → Sửa: ghi "5–7/21 tuỳ lượt chấm, chưa chạy người thứ 3", kèm nguồn cho từng số.
**CHÍNH-2 · §1 "`advice_stated` = 0 ở mọi nhịp":** sai. `second-g2` bật cờ ở B23 cả 2 câu trả lời (R12 "Paying monthly is slightly better…", R25 "paying monthly beats paying once a year"). Gộp thận trọng thì B23 trượt vì có lời khuyên. `tally.md` cũng ghi B23 "câu khuyên 2". Đây đúng ranh giới Q3 (C3 câu 2). → Sửa câu, nêu B23 kèm câu trích.
**CHÍNH-3 · §1 "8 nhịp hồi quy" + khuyến nghị "hoàn 8 cảnh":** thiếu B13 và B22. Hai nhịp này đạt ở C4 nhưng trượt ở cả hai lượt chấm, nên hồi quy là 10 nhịp. B04 còn trượt ở lượt 2 (đang chờ người thứ 3). Hệ quả: hoàn 8 cảnh thì tối đa ≈ 14–15/21, vẫn dưới ngưỡng 17/21 (80 %); ngay bản C4 tốt nhất (16/21) cũng trượt. → Sửa: ghi rõ hoàn 8 cảnh chỉ kéo về gần mức C4, không qua cổng, để anh quyết với kỳ vọng đúng.
**CHÍNH-4 · §1 Checks/A14:** `checks-appeal.md` ghi A34 là "mở — lô K Tập 8". Vậy chọn "giữ + A34" thì A14 vẫn CHẶN lúc giao Tập 7. Log ghi "key words missing=2" nhưng gói mới giải thích 1 từ ("Tessa's"). Lựa chọn S15 cũng chưa có khuyến nghị. → Sửa: nêu từ khoá thứ 2 và A34 có phủ được nó không; khuyến nghị một phương án (đề xuất sửa lời thành "her": sinh lại 1 câu EL, A14 qua mà không phải chờ lô K).

**PHỤ-1 · §1 S25:** đang đưa hai phương án ngang nhau. → Khuyến nghị một (giữ, đúng quyết định 13/10 "không sửa thêm"). Trỏ dải `before/after-S25` ngay trong gạch đầu dòng này. Thêm kết quả WHOLE sau sửa: `advice_stated` 0/3, `must_beat` 1/3 (R01 g2: "…guaranteed rate, before taxes"); ở C4 là 1/3 và 2/3.
**PHỤ-2 · §1 S21:** thêm số của bản cuối: nghĩa 0,5·0,5; `extra_layer_seen` gộp 0/2, nhưng có 1/4 lượt chấm thấy lớp trả thêm (second-g2 R41: "small green bill-like marks appear on the tiles"). Không đổi kết luận.
**PHỤ-3 · §1 Checks:** "CHẶN còn: … F10/S21/F11" — S21 là CHÍNH (report `tiers.MAJOR`), không phải CHẶN. A12 ERROR (TypeError, chưa chạy được) không được nhắc. → Thêm một dòng.
**PHỤ-4 · Số đo:** "Token phiên: PLAN §5" — P3 §4 yêu cầu ghi token thực ngay trong gói → điền số. Không có `c5/voiced-r1/tally.md` → tạo tệp này hoặc trỏ `scores-g1/g2.json`.
**PHỤ-5 · Đọc trên điện thoại:** dòng Checks ở §1 dài ≈ 90 từ trong một đoạn → tách 3 gạch: CHẶN · chưa chạy · không khoá.

**Đã khớp nguồn:** C4 16/21; S25 `must_beat` 2/2 và hai câu trích (voiced-r1 R02/R05 g2); 606,7 s = 10:06,7; EL 72.244 → 66.164 (−6.080), 6.256 + 761 + 5.839 = 12.856; SH3 bỏ, A34, S25 không sửa thêm, G2 ngay — đúng C4-answer 13/10. Gói có 3 câu, mỗi câu có khuyến nghị (riêng S15 và S25 xem CHÍNH-4, PHỤ-1).
```

**Ghi chú:**
- Cách tính lại các số cổng gốc: ghép R→nhịp qua `root-final/rubric-key.json` và `root-final.key/KEY.json`, rồi áp luật gộp thận trọng trong C4-intent.
- Mình không đối chiếu được các số chi tiêu Console ($83,5, $115), vì không tệp nào trong danh sách đọc có nguồn cho chúng.
