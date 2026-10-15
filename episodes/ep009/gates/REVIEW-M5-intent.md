**Kết luận: ĐẠT có sửa.** Có 1 lỗi CHẶN và 5 lỗi CHÍNH. Cần sửa cả 6 vào `M5-intent.md` và commit trước bước (1).

Phần lớn lệnh chặng được giữ: checks đủ bộ trên 1080p có `cine` ở lần đầu (V12), 7 J/L khớp `kit.CUTS` với offset ≤ 0,5 s, `data_db` 34 với L1 ≥ 20 dB, `aac_true_peak` ≤ −2,0 dBTP, `sfx_real` (60 s, ≤ 4/10 s), cấm thêm `allowTerms` sau khi thấy kết quả, điểm theo lượt đọc đầu (bài học Tập 8 #1), sửa ≤ 2 vòng, trần $15 cứng có điểm ngắt ở $13,5. Đủ các bước M5 của playbook.

**CHẶN**
1. **§6 Content ID ghi "chủ dự án làm, trước G3".** G1 câu 3 đặt "kiểm Content ID = điều kiện G2", nên ghi trước G3 là đã dời điều kiện. **Sửa:** G2 chưa đạt cho tới khi chủ dự án báo kết quả (0 claim, hoặc claim đã xử lý). Gói G2 để sẵn ô kết quả. Ghi rõ bản tải lên riêng tư là (b), có nhạc "Origami".

**CHÍNH**
2. **Đầu bài và §4, `cine`.** Lệnh chặng là 5 cảnh, ý đồ ghi "4 đoạn có lớp (a1, b1, d1, f2)". Tỉ lệ chỉ "ghi tỉ lệ thật", không có ngưỡng trượt. Tỉ lệ này biết được trước khi render. **Sửa:** liệt kê 5 cảnh đinh khai `cine` kèm giây của từng cảnh. Tính trước tổng ≤ 30 % của 8:44 (≤ 157 s). Vượt thì cắt lớp trước khi dựng (b), không để tới sau khi đo.
3. **§1, CHẶN dự kiến chỉ ghi theo cảnh (S01, S05) và theo mô tả mơ hồ ("thêm chế độ quỹ cổ phiếu mới").** Bài học Tập 8 #2 đòi ghi theo ID luật. **Sửa:** ghi đúng ID luật dự kiến trượt ở S01 và S05, theo khiếu nại A48. Luật khác trượt ở S01/S05 vẫn là trượt thật.
4. **§4, freezedetect chưa định nghĩa "có lời".** Đây là bài học Tập 8 #7, chưa áp. **Sửa:** "có lời" = phần chồng với vùng stem giọng trên −45 dBFS. Câu "> 8 s = 0 → liệt kê" viết lại thành: ngưỡng = 0, trượt thì sửa trong ≤ 2 vòng.
5. **§4, lặng trước số neo ghi 0,7–1,0 s, trong khi §5b ghi 0,7–0,9 s.** Ý đồ đang nới ngưỡng của playbook. **Sửa:** ghi 0,7–0,9 s.
6. **Thiếu ngưỡng ghi trước cho M6 khi (b) thành bản M6.** SSIM so nháp ≥ 0,97 (§1, M6) chắc chắn trượt ở các cảnh có `cine`, vì nháp (a) không có lớp. Nếu để vậy sẽ phải sửa bộ đo sau khi thấy kết quả. **Sửa:** ngay bây giờ ghi SSIM ≥ 0,97 cho các cảnh không `cine`. Cảnh có `cine` thì đo bằng `cine_color` (ΔE2000 ≤ 5) thay cho SSIM. Ghi luôn lý do trước cho lần chạy 1080p thứ hai nếu G2 đổi hình hoặc lời (luật của Line producer).

**PHỤ**
7. **§2 và §3 đo trên (a), không có lớp, còn bản phát hành là (b).** **Sửa:** khung dải của các nhịp nằm trong cảnh `cine` lấy từ (b), hạ xuống 540p. Hoặc ghi rõ đây là giới hạn của phép đo.
8. **§2 thiếu các thông số khoá.** **Sửa:** ghi ngưỡng nhịp ĐẠT (≥ 0,8 và không `advice_stated`), SHA của `beats.md` và `root_gate.py` dùng ở M2 (bài học Tập 8 #8).
9. **§4, liền mạch thiếu mục "số trên hình = lời"** (bài học Tập 8 #6). Phép thử J/L chỉ ghi "R09 chỉ báo". **Sửa:** thêm mục số trên hình. Ngưỡng J/L: 7/7 đúng kiểu khai, offset trong ±0,5 s.
10. **§1, sau khi sửa V12/ΔE (sửa cảnh hoặc tắt lớp).** **Sửa:** ghi rằng phải chạy lại luật đó và bước `cine` trên cảnh vừa sửa, rồi mới vào G2.
11. **§4, dòng nguồn trên hình.** **Sửa:** kiểm câu ở S24 khớp nguyên văn câu G1 sửa ("Stock returns: Kenneth R. French Data Library…"). Chạy `sfx_fetch --verify` và kiểm mỗi tệp SFX có một dòng RIGHTS §G.
12. **Chi dự kiến.** Chưa có khoản dự phòng cho vòng sửa, mỗi vòng là một lượt đọc lại. "Cổng gốc M2 ≈ $2,3" ghi là dự kiến, trong khi M2 có thể đã chạy. **Sửa:** ghi số đã chi thực (`total_cost_usd`), cộng khoản dự phòng cho vòng sửa, và thêm luật ngắt 150 % ngân sách mỗi mốc.
13. **Kiểm trước khi dựng.** **Sửa:** kiểm `episode.yaml` có `data_db: 34` và `audio.aac_true_peak` trước bước (a). Gói G2 dùng `templates/L3.md`, kèm 3 khung tĩnh 1080p của cảnh đinh.
