**ĐẠT có sửa.** Không còn lỗi CHẶN hay CHÍNH; còn 7 lỗi PHỤ. Lượt này chạy ở chế độ chỉ đọc, không có Bash, nên tôi không xem được `git log -3 -p`. Tôi đối chiếu thẳng trên các tệp hiện tại.

**Các mục của lượt 2: đã sửa đúng**
- **CHÍNH 1:** phiên K không bị đếm thiếu, lập luận ở `REPORT.md:10` đứng được. K-PLAN ghi đến 17:58 phiên đã dùng ≥ 0,93 triệu. Cộng với lượt cuối 0,68 triệu thì ra ≈ 1,61, vẫn ≤ 1,86. Vậy `modelUsage` cuối đã gồm cả lượt 1. Còn lỗi trích nguồn, xem PHỤ 1.
- **CHÍNH 2–5:** đã sửa đủ ở `packaging.md:113`, `PACKAGING-BRIEF.md:24` ("Kit (proposed, pending owner approval)"), `REPORT.md:79`, `thumbs.py:91-97`, `checks_split.sh:23-25`, `REPORT.md:209`.
- **PHỤ 1–5, 7, 9–15:** đã sửa đúng. Trong đó `check_script.py:386` chỉ áp cho `deep`, còn `brief.py:72` giờ in cảnh báo. PHỤ 6 và PHỤ 8 mới sửa một phần, xem PHỤ 2 và PHỤ 3 dưới đây.

**CHẶN:** không có.

**CHÍNH:** không có.

**PHỤ**
1. **`REPORT.md:10, 27`:** trích nguồn sai.
   - Vấn đề: K-PLAN §5 (`K-PLAN.md:44`) chỉ có 927.431 "đến 17:58", không có số "lượt 2 = 0,85". K-PLAN cũng ghi "gồm 3 agent con", còn REPORT nói log đếm 2.
   - Sửa: "K-PLAN §5 ghi ≥ 0,93 đến 17:58 (lượt 1); lượt 2 ≈ 0,85 đo từ transcript cục bộ". Thêm vào dòng 27: "K-PLAN ghi 3 agent con, log đếm 2".
2. **`lessons.md:189` (T6-4):** vẫn ghi "chỉ cảnh đổi lấy mẫu lại", trong khi `episode.md:258` đã thêm ý "đầy đủ khi A29 qua K".
   - Sửa: chép cùng câu đó vào T6-4.
3. **`REPORT.md:148-152` (§4f):** chưa ghi rằng điểm trong `rescore.json` chấm bằng mã cũ (không có trường `model`). §4c chỉ nói phần ảnh.
   - Sửa: thêm dưới bảng: "điểm chấm trước khi sửa mã; chạy lại ở P3 Tập 7".
4. **`packaging.md:111` và `thumbs.py:4-7`:** nói "qua claim-risk", nhưng mã chỉ kiểm khi có `--ep`. Thiếu `--ep` thì chỉ in cảnh báo rồi chạy tiếp. Dòng hướng dẫn cách gọi (dòng 6-7) cũng chưa có `--ep`.
   - Sửa: thêm `--ep episodes/epNNN` vào dòng mẫu, và ghi "(bắt buộc `--ep`)" ở `packaging.md:111`. Hoặc cho `thumbs.py` thoát lỗi khi thiếu `--ep` mà không có `--no-api`.
5. **`REPORT.md:85` và §5 câu 2:** nói quá bằng chứng.
   - Vấn đề: con số "trung vị ~15–16 phút" lấy từ `market/REPORT.md` §4. Nhưng chính T6-12 (`lessons.md:197`) nói số này phải tính lại sau khi loại kênh của mình. Câu 2 vẫn khuyến nghị `deep` mà không nói điều đó.
   - Sửa: thêm "(chưa tính lại sau khi loại kênh mình, T6-12; ít khả năng đổi kết luận vì chỉ có một kênh)" ở cả §3 và câu 2.
6. **`REPORT.md:207` (§6 BƯỚC 1):** "OWN_CHANNELS (T6-12)" nằm trong danh sách "mục được duyệt", nhưng §5 không còn câu nào hỏi về nó.
   - Vấn đề: phiên P1 có thể chờ một câu trả lời không bao giờ có, hoặc tự "hoàn lại" mục này.
   - Sửa: "OWN_CHANNELS (T6-12): đã áp, không cần duyệt; chỉ chạy việc treo q01/q17 và `market/REPORT.md` §4".
7. **`REPORT.md:209` (§6):** "(deep chỉ khi F-14 đã đạt trước G1)" biến khuyến nghị thành luật.
   - Vấn đề: chưa có nhánh cho trường hợp chủ dự án bác 1d mà vẫn chọn `deep`.
   - Sửa: "Format theo câu trả lời 2. Nếu câu trả lời chọn deep nhưng 1d bị bác hoặc F-14 chưa đạt trước G1 → nêu mâu thuẫn ở G1 lô (episode.md §9 'nhà máy trước'), không tự chọn."

**Đọc lại §5 và §6:**
- §5 có đúng 3 câu, câu nào cũng có khuyến nghị kèm đánh đổi.
- Bộ nhận diện kênh và chi Console đều để chờ chủ dự án duyệt.
- §6 rẽ nhánh đúng cho 1g. Thứ tự merge (merge main, rồi tạo ep007, rồi chạy `verify.sh`) đúng với CHARTER §7.
- Ngoài PHỤ 5–7, tôi không thấy câu nào tự quyết việc của chủ dự án hay mâu thuẫn với quy trình.