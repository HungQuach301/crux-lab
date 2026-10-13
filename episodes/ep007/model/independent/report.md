# Kiểm số độc lập — Tập 7 (headless khoá Console, review mode; chỉ đọc data/raw, không đọc model/ hay out/)

Đầu bài: `briefs/independent.md` · log: `logs/independent.jsonl` · chi $0.28

Kết quả: **ĐẠT**. 57/57 đại lượng khớp sau khi làm tròn, không có dòng LỆCH nào. Tôi tính lại từ hai file CSV gốc bằng mã riêng và không mở `model/` hay `out/`. Cả hai chuỗi đều không có ô trống hay ".". Chuỗi 15 năm bắt đầu từ 1991-08-30 nên số tuần ghép là 1833.

**Các dòng LỆCH:** không có.

**KHỚP: 57/57.** Trong đó 5 dòng ghi "KHỚP (làm tròn)": số của bên dựng đúng, nhưng nếu người đọc tính lại từ các số đã làm tròn trên trang thì sẽ lệch ở chữ số cuối.

| id | bên dựng | bạn tính (chưa làm tròn) | tính từ số đã hiển thị | trạng thái |
|---|---|---|---|---|
| fallback_gap_now | 612.55 | 612.5478 | 2828.16 − 2215.62 = 612.54 | KHỚP (làm tròn) |
| extra_principal_needed_now | 732.67 | 732.6689 | 2948.28 − 2215.62 = 732.66 | KHỚP (làm tròn) |
| interest_30on15_now | 210691 | 210691.17 | 2948.28×180 − 320000 = 210690 | KHỚP (làm tròn) |
| interest_30full_now | 477622 | 477621.53 | 2215.62×360 − 320000 = 477623 | KHỚP (làm tròn) |
| yearly_lump | 8792.03 | 8792.0273 | 12 × 732.67 = 8792.04 | KHỚP (làm tròn) |

**Cách hiển thị an toàn:** giữ các số hiện tại vì chúng đúng. Ghi chú một câu rằng các hiệu và tích được tính từ số chưa làm tròn, nên có thể chênh ±1 ở chữ số cuối so với phép tính tay. Một cách khác là hiển thị khoản trả tháng đến cent và các tổng lãi đến chục đô la (ví dụ "≈ $210,690").

Một số giá trị đối chiếu khác (đều khớp):
- pay15_now = 2828.1632, pay30_now = 2215.6154, pay30on15_now = 2948.2843.
- extra_vs15_total_now = 21621.81, months_at_pay15_now = 194.621.
- spread_mean = 0.57490, share_spread_ge_050 = 0.62957, share_extra_ge_now = 0.18658, share_r30_ge_now = 0.18985.
- Số tuần mỗi thời kỳ: 436, 522, 521 và 354.
- Mô phỏng trả thêm hằng tháng: hết nợ sau 180 kỳ, tổng lãi 210691.17. Mô phỏng trả khoản lớn mỗi năm: hết nợ sau 184 kỳ, tổng lãi 218856.78. Chênh lệch 8165.61.

**Định nghĩa mơ hồ hoặc dễ vỡ:**
1. **era2020_median_r30:** số tuần chẵn (354) nên trung vị là trung bình hai giá trị giữa, ra đúng 6.275, nằm ngay điểm giữa hai cách làm tròn. Làm tròn "nửa lên" cho 6.28 (khớp bên dựng). Còn `round(6.275, 2)` của Python ra 6.27, vì 6.275 lưu dưới dạng số thực nhị phân là 6.27499…. Nếu dùng median_low hay median_high thì kết quả cũng khác. Nên ghi rõ "trung bình hai giá trị giữa" và hiển thị 6.275, hoặc chốt quy tắc làm tròn.
2. **months_at_pay15_now:** công thức liên tục cho 194.6 tháng, còn mô phỏng từng tháng thì cần 195 kỳ trả. Đề đã ghi "continuous formula" nên không lệch, nhưng câu chữ trên trang không nên nói "195 kỳ" lẫn với "194.6 tháng".
3. **Lãi trong các mô phỏng:** tôi tính lãi theo dư nợ mỗi tháng, và kỳ cuối chỉ trả đúng phần dư nợ còn lại. Nếu kỳ cuối vẫn trả đủ khoản thì tổng tiền trả sẽ khác, nhưng tổng lãi không đổi. Hiện không gây lệch.
4. **share_spread_ge_050:** so sánh `>= 0.50` có thể bị ảnh hưởng bởi sai số số thực khi tính 30 năm trừ 15 năm. Tôi đã thử cả so sánh thẳng lẫn có dung sai, đều ra 0.62957, nên không ảnh hưởng.

Còn một kiểm tra tôi không chạy được vì lệnh bị từ chối: xem có tuần nào khác cũng đạt r30 = 2.65 hoặc 9.25 không. Đề đã định nghĩa là "first week" nên việc này không ảnh hưởng kết quả.

**Kết luận: ĐẠT.** 57/57 khớp, 5 dòng khớp do làm tròn cần ghi chú cách hiển thị, và 1 dòng nên chốt quy tắc làm tròn (era2020_median_r30 = 6.275).