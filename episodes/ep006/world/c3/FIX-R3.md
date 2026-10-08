# C3 · FIX-R3: s29-three, cùng séc, khác tháng bắt đầu (D-009 E6, sửa bằng hình)
**Vì sao:** vòng 2 s29 nghĩa 2/2, khuyên 1/2. Một người đọc bám vào ca xấu nhất của Carl (≈ 4 thùng) rồi khuyên "COLA". Ba hàng xếp Edna · Ruth · Carl, đọc như so ba loại khoản trả. Séc thì nhỏ và không có nhãn.
**Đổi (chỉ `s29-three/scene.js`; mã chung không đổi):**
- Cột xếp theo thời gian: Edna (−5,7) · Carl (0,6) · Ruth (6,9).
- Ở đồ thị có một trục "start month" tỉ lệ năm (1945–2030, y 806) với ba mốc Jan 1949 · Jan 1966 · Aug 2006. Mỗi cột có đường nối từ tên xuống mốc của mình. Tháng bắt đầu chuyển từ cột xuống dưới mốc.
- Trục, mốc, nhãn mốc và "start month" ban đầu màu muted. Đến "month" (15,41 s) chúng chuyển sang ink, có emph, nét dày hơn, và giữ 5,3 s đến hết đoạn.
- Séc to hơn: cbase 1,0, cw 0,62, người h 1,6, nên séc năm 20 cao ≈ 140 px trên khung 1080. Một ngoặc ink chung nối đỉnh ba séc, kèm nhãn "same check: +2% a year" (claim two_pct_growth_20y_pct, 6 từ, 48 px). Ngoặc và nhãn hiện từ khi chuyển chế độ xong (7,45 s) đến hết đoạn.
- Tiêu đề rút còn "crates at year 20" (bỏ "same 2% raise" để không lặp nhãn séc). Đã đổi `label_cues.d1.crates` trong spine.py cho khớp.
- Ba cột cùng màu, cùng cỡ, cùng cách xử lý. Carl không có màu hay độ phóng riêng. Không thêm nhãn khuyên hay câu đối trọng.
- Máy cThree: tâm (−0,25, 1,15), cách 46,8. wThree0/wThree chỉnh nhẹ để thấy đủ cả ba cột.
**Không đổi:** mốc giờ, động tác, sự kiện âm, mật độ sfx. Độ dài vẫn 20,69 s nên `spans.json` giữ nguyên. Ba đoạn đạt không đổi: spine.json của chúng không có diff.
**Kiểm:** comment_guard OK. 4 spine đều qua quy tắc 2/3/7. Đã xem khung dải (540/1080, `render_shots.js --stills`), không có vi phạm. Chưa chạy build_seg, verify hay sync_audit.
**Rủi ro:** (1) Khi máy nhìn thẳng, hàng thùng thấp (≈ 37 px ở 1080), thùng sáng/tối vẫn phân biệt được. (2) Đường nối Carl dài và chéo. (3) Ngoặc chung đi qua phía trên đầu ba người, có thể bị đọc như một "nhóm" thay vì "cùng cỡ".
