# REVIEWER — soát ý đồ kiểm mù C4 Tập 6 (`gates/C4-intent.md`) · 2026-10-09, trước khi chạy

**Kết luận: ĐẠT có sửa.** Phải sửa 2 mục CHẶN trước lượt đọc đầu tiên. Khớp lệnh chủ dự án (C3 câu 1, câu 3; K4.1 câu 3): bản có lời cả tập + S29, khuyên sản phẩm = 0, hai rubric song song, 2 người chấm, đối chứng, lệch thì giữ rubric cũ, "hỏi công ty bảo hiểm / hỏi báo giá" = caution_only. Danh sách nhịp loại 1 **đúng** `beats.md`: 23 nhịp loại 1, 7 nhịp loại 2; loại 1 = 23/30 = 77 % ≥ 60 % (§5.8). Dừng sớm, gộp hai người chấm (điểm thấp nhất, cờ khi một người bật) và chấm hai rubric khớp `packets.py tally`.

## CHẶN
1. **Đối chứng âm khác chủ đề và không đo được điều cần đo.** Mẫu mượn của Tập 5 S06 (thế chấp nhà, đã chấm theo vai người thuê nhà) phạm §2.8: đối chứng âm phải "cùng chủ đề, cùng dữ kiện". Đưa cho vai T, mẫu này hầu như chắc chắn ra 0 cờ, nên ≤ 1/3 không chứng minh gì. Nó cũng không thử được chỗ rubric mới tách advice_stated khỏi advice_inferred. Sửa mục E, gạch **Âm** thành:
   > "**Âm (cặp khớp):** dải 6 khung thật của S29 + lời S29 + **một câu trung tính cùng độ dài, không hành động**: *"So the same raise ended in three different places, set by the month each one started."* Kỳ vọng `advice_stated` ≤ 1/3 người đọc. Cờ `advice_inferred` ở mẫu âm được ghi lại: rubric cũ bắt được mà rubric mới không bắt thì đó chính là chỗ hai rubric phân biệt. Mẫu Tập 5 S06 chỉ chạy làm kiểm tra phụ, không thuộc điều kiện dùng rubric mới."
2. **Rubric "đúng nghĩa" của B, C, E chưa có trong ý đồ** (§5.1: rubric ghi trước khi chạy). Hiện văn bản đáp án chỉ do mã dựng mới (`c4/blind_c4.py`) viết ra. Ranh giới khuyên cũng chưa có ví dụ, trong khi người chấm C2 v3 dao động 5/6 → 1/6 trên đúng kiểu câu này. Thêm vào mục D:
   > "**Nghĩa (B):** chép nguyên văn 'Đúng câu hỏi' + 'Đúng đáp án' của `c2/rubric.md`. **Nghĩa (C, E):** muted read B29 nguyên văn + 'cùng 2 %, kết quả do tháng bắt đầu'. **Ranh giới khuyên** (chủ dự án C3 câu 3): 'ask the insurer how much smaller the rising check starts' / 'ask what an inflation-linked option would cost' = caution_only. 'weigh / consider / prefer / compare and choose the inflation-adjusted (COLA) option' = câu khuyên. Cả hai người chấm nhận đúng đoạn này."

## CHÍNH
3. **Mục B chưa nói hệ quả khi trượt.** Nếu câu khuyên đến từ lời thì không sửa được, vì mục F cấm đổi lời. Thêm: "B trượt (≥ 1/3 theo rubric cũ) → **dừng, hỏi chủ dự án** kèm câu trích, như C; không mở vòng sửa."
4. **Ngoại lệ S29 ở A chưa chạy được bằng công cụ.** `packets.py tally` đưa mọi nhịp có cờ khuyên vào `advice_beats`, và cổng ra FAIL. Thêm: "S29 ở A: chỉ xét nghĩa (≥ 2/3 nghĩa 1). Cờ khuyên của S29 ghi vào bảng nhưng gỡ khỏi `advice_beats` bằng tay. Báo cả hai con số: verdict của tally và verdict sau ngoại lệ."
5. **Câu 5 dẫn dắt.** Câu hỏi nhắc 'narration' trong khi dải A tắt tiếng. Câu hỏi còn ngầm cho rằng đã có lời khuyên ngay cả khi câu 4 trả 'none'. Sửa: "A dùng nguyên văn §5.3: *Did the animation itself suggest this, or is it your own conclusion?* B/C/E: *Did the video itself (picture, on-screen text or narration) suggest this, or is it your own conclusion?* Cả hai thêm: *If you gave no advice in 4, answer 'none'.* A và B/C/E dùng hai khoá riêng."
6. **Chưa nêu tên vùng ±5 %** (§2.2). Thêm: "23 nhịp: đạt cần 19/23 (82,6 %). 18/23 (78,3 %) và 19/23 nằm trong ±5 % quanh ngưỡng nên phải nêu tên."
7. **Rubric mới dựa vào lời người đọc tự nhận** (câu 5). Người chấm không thấy lời video nên không đối chiếu được 'video nói' với 'tôi tự suy'. Thêm: "Báo bảng câu 5 (video / tự suy / none) theo từng mẫu. Mẫu dương mà bị chấm `advice_inferred` thay vì `advice_stated` → ghi 'rubric mới hụt mẫu dương'."

## PHỤ
8. Mỗi tấm 12 khung không làm được bằng `strips.py`, vì công cụ này cố định 6 khung. Ghi: "Tấm 12 khung dựng bằng `sheet()` trong `c4/blind_c4.py` (mã mới, ghi SHA ảnh), không phải `strips.py`."
9. Lời C (S29, S28) phải lấy từ `out/captions.srt`, giống B ("như người xem nghe"), không lấy từ `script.md`.
10. Ghi trước số lượt và token (`episode.md` §2): "A 46 lượt (+ người thứ 3) ≈ 0,5 triệu; B/C/E 12 lượt; chấm 2 × 2 gói."
11. Chạy tally A với `--classes` (bảng phân loại đã báo, SHA-256), đúng §5.8.
