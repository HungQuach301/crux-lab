**REVIEWER: ĐẠT** — không có mục CHẶN; 6 CHÍNH, 5 GỢI Ý. Kết luận tạm của REPORT (TRƯỢT ở B22) là trung thực; tôi không thấy chỗ hạ đích. Nhưng có một số đếm sai và vài chỗ REPORT chưa nêu.

Tôi đã đọc: brief, INTENT, REPORT, diff 3 tệp nhà máy, đoạn **b-s04-s08** và **d-s13-s23** (bản giao so với bản F-14), 4 tệp tally, các tệp `out/*.json`. Tôi đã chạy `test_factory_f14` (5/5 OK) và `test_world*` (48 OK, 1 bỏ qua). Diff `checks/` và `episodes/` so với `origin/main` đều rỗng. Không sửa tệp nào.

### CHẶN (0)

### CHÍNH (6)
1. **Số cổng gốc sai: 20/23, đúng ra 21/23.** Tally `root-f14v3` có 20 nhịp ĐẠT (B01 và B14 TRƯỢT, B22 chờ). Lượt đọc lại `root-f14v3-rr` cho B14 ĐẠT (1 · 0,5 · 1), B22 TRƯỢT. Vậy còn 21/23, khớp với danh sách TRƯỢT của chính REPORT (chỉ B01, B22). Kết luận TRƯỢT không đổi. — `toolkit/factory/f14/REPORT.md:17` và `:26`.
2. **B01 tụt so với đối chứng cùng phiên nhưng REPORT không gọi tên.** `root-ctl` cho B01 1 · 1 ĐẠT; F-14 cho 0,5 · 0,5 ("no 9 lit stated"), và không có lượt đọc lại 3 người. Luật ghi trước so với bản giao (bản giao B01 cũng TRƯỢT) nên không phạm luật. Nhưng cách so với đối chứng cùng phiên mà REPORT §5.2 tự đề xuất sẽ tính B01 là nhịp tụt thứ hai. — `REPORT.md:25`, `root-f14v3/tally-new.json:7`.
3. **Goodhart nghiêng: 8 trong 27 cue cũ đổi từ trượt sang đạt R07 chủ yếu nhờ đổi cách đo, từ "motion" sang "label".** Các cue này có thêm hoặc đổi khoá `label_cues`: c2.level, d1.climbed, f0.most, f4.ruths (trước là khoá `f4.ruth`, không khớp cue), f7.start, g1.forty, g2.half, g3.carls.
   - Các nhãn tôi đã soát đều có thật và đúng lời: "level check", "Ruth: 90.4%", "8 of 10 crates" ở "most".
   - Riêng `f7.start` = 'Carl' hiện ở câu S23.1 "from one start to another", trong khi không ai nói chữ "Carl".
   - REPORT không nêu rằng cách đo đổi trên các cue này.
   - Nguồn: `ep006/world/c4/d-s13-s23/spine.py` (label_cues), `b-s04-s08/spine.py:80`, `out/f14-r07-local.json:604`.
4. **Đổi số trên hình, trái INTENT §4.** Nhãn `b0.rises` bỏ chữ "+2% a year" để giữ quy tắc 1 ở chế độ thế giới. REPORT không nêu. — `toolkit/factory/f14/ep006/world/c4/b-s04-s08/spine.py:80`.
5. **Ghi "3%" là ĐẠT trước khi chạy cách đo đã ghi trước.** INTENT quy định đo bằng `textTrack`, nhưng REPORT ghi ĐẠT dựa trên nhật ký trang. Con số 0,15 s cũng không có trong tệp `out/` nào. Nên ghi "chờ". — `REPORT.md:16`.
6. **Nguồn gốc các lượt chấm chưa rõ.**
   - Một lượt chấm đối chứng bị ghi đè.
   - Bản F-14 v3 được chấm hai lần (thư mục `first-grading/`), nhưng không ghi vì sao chấm lại và vì sao giữ lượt nào.
   - Con số đối chứng 19/23 lại là cơ sở cho đề xuất nới luật cổng gốc, nên cần biết rõ nó từ lượt nào.
   - Nguồn: `REPORT.md:28`, `:58`, `root-f14v3/first-grading/`.

### GỢI Ý (5)
7. Nhãn `b0.never` lệch +5,93 s nhưng không có trong danh sách nhãn lệch của REPORT. — `out/f14-build-report.json:190`, `REPORT.md:50`.
8. R07 đo theo điểm ảnh nên tính cả lúc một track `life` bắt đầu đúng ở từ khoá. Ví dụ `f6.social` lệch 0,01 s chính là lúc track `cpiw` bắt đầu, cũng là track gây B22 tụt. Nên báo bao nhiêu cue đạt nhờ `life` bắt đầu ở từ. — `out/f14-r07-local.json`.
9. `life_keys` có tham số `hold_at_end` không dùng, và docstring nói "nội suy" trong khi hàm chỉ sắp xếp. — `toolkit/factory/world/spine.py:171`.
10. Lời khẳng định "spine.json trùng byte khi không khai `f14`" chỉ là "kiểm bằng tay", không lưu sha trước/sau. Mã thì rõ là opt-in: `build_seg`, `verify_seg` chỉ chạy khi có khoá `f14`, `check_rules` mặc định `episode_t0=None`, và test chạy OK. Nên lưu sha hoặc thêm test. — `toolkit/tests/test_factory_f14.py:2`.
11. Cổng gốc được dùng làm vòng sửa (v1 → v3: B08, B16) nên mất một phần giá trị là phép đo giữ riêng. REPORT có nêu; đề nghị ghi rõ điều này trong kết luận. — `REPORT.md:30`.

### Những gì đã kiểm và ổn
- **Chống Goodhart:** R07 có báo cả trên 118 cue của bản giao (110/118 = 93,2 %, tôi tính lại khớp; 121/129 = 93,8 % khớp). Cách đo cục bộ cho bản giao ra đúng 70,3 %, bằng số của checks. `life` không bị `spine_pace` đếm. Spine về 0 chỉ nhờ cue mới, và REPORT nói thẳng điều này (chỉ tính cue cũ vẫn là 7 · 4).
- **Gen §4:** không có lắc, thở hay trôi kiểu sin trong scene F-14. Cả 21 track `life` ở hai đoạn b và d đều có `what` gắn với một đại lượng của câu. Các nhãn mới "rent / medical care / gasoline" và "level check" đúng là từ được nói.
- **Phạm vi:** không chạm `checks/`, `episodes/ep006` hay tệp Tập 7/8.
- **Số đo:** freezedetect 44,83 s khớp với tổng từng quãng; bản giao 206,01 s đo cùng `measure.py`. R07 đủ bộ và CHẶN được ghi đúng là "chờ checks".
- **Rủi ro nghĩa:** B22 được nêu kèm nguyên nhân hợp lý. B01 thì chưa (mục 2).