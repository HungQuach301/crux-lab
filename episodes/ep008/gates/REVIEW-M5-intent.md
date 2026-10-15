**Kết luận: ĐẠT có sửa.** Không có lỗi CHẶN. Có 5 lỗi CHÍNH cần sửa vào `M5-intent.md` và commit trước khi chạy.

**Lệnh chủ dự án ở G1 được giữ đủ:** ≤ 2 vòng mỗi lỗi, không mở C3 riêng, theo LOCK K4.4, không dựng 1080p trước G2 (chỉ 3 khung tĩnh, đúng như G1 cho phép), trần $25 (dự kiến ≈ $11–12). Các bước M5 trong playbook đều có mặt. Chỗ thiếu nằm ở phép thử của Editor và của Giám sát liền mạch.

**CHÍNH**
1. **§2, luật "hồi quy → đọc lại một lần (2 người mới)" lệch một chiều.** Chỉ nhịp trượt được đọc lại, nhịp đạt may thì không. Như vậy điểm tổng được nắn sau khi đã thấy kết quả. **Sửa:** tổng điểm cổng lấy theo lượt đọc đầu. Lượt đọc lại chỉ dùng để xác nhận lỗi cần sửa, không được thay điểm.
2. **§1, tiêu chí "0 CHẶN chưa giải thích" để ngỏ.** CHẶN nào cũng có thể "giải thích" sau khi thấy kết quả. **Sửa:** ghi ngay bây giờ danh sách ID luật CHẶN dự kiến trượt vì thiếu kind `rent-buy-twin-replay` (lấy từ `K-brief.md`). Mọi CHẶN ngoài danh sách đó là trượt thật.
3. **§1, luật đo ở M6 chỉ ghi "C14…".** **Sửa:** liệt kê đúng các luật K4.4 đánh dấu phụ thuộc độ phân giải: F05, F08, R03, R04, V05, V10, V08, V12, C14. Thêm một câu: các luật này trên 540p chỉ để báo, vì phần đối chiếu 540p/1080p của A41 (a) chưa chạy (để ở K4.4.1).
4. **§1, chưa chặn đường thêm `claims.allowTerms` cho S23 sau khi thấy lượt trúng.** Thêm ngoại lệ lúc đó là sửa bộ đo. **Sửa:** ngoại lệ chỉ được thêm kèm lý do ≥ 5 từ, mỗi ngoại lệ liệt kê ở G2. Nếu S23 trúng câu lời đã duyệt thì giữ là CHÍNH và nêu, không tự miễn.
5. **§4, phép thử của Editor bị nới so với `episode.md` §1a.** Quãng có lời không đổi hình > 8 s theo playbook phải = 0, ý đồ chỉ "liệt kê". Ý đồ còn thiếu kiểm mù "chỗ muốn tua" (không đoạn nào bị ≥ 2/3 người đọc chọn). Nhãn "chỉ báo" chỉ áp cho bài nhớ lại. **Sửa:** khôi phục hai ngưỡng này, ghi rõ mẫu và người đọc.

**PHỤ**
6. **§4, liền mạch còn thiếu so với §1a.** Thiếu "số trên hình = lời", "chuyển hồi đúng kiểu khai" (R09) và "màu lựa chọn đúng". Footage mới ghi "có nguồn". F15 đòi: kiểu tư liệu cần năm + nguồn, kiểu minh hoạ cần nhãn "illustrat…" và không mang số claim. F15 còn cấm footage trong 5 s đầu. **Sửa:** khai bản đồ Natural Earth là tư liệu hay minh hoạ, rồi bổ sung các mục còn thiếu.
7. **§4, freezedetect chưa định nghĩa "có lời".** **Sửa:** ghi rõ "có lời" là phần chồng với vùng stem giọng trên −45 dBFS, đúng như cách K đo.
8. **§2, chưa khoá rubric và cách cắt dải khung.** **Sửa:** ghi SHA của `beats.md` dùng ở M2 r2, chép nguyên văn "ý cần đọc 
