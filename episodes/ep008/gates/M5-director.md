# M5 Tập 8 — lượt đạo diễn máy trên nháp r2 (chẩn đoán, D-010 §6; `prod/director.py r2`, chi $0,26)

Nguyên văn `review-m5/r2/director.md`. Một lượt headless (khoá Console, 0 agent con), 4 tấm × 12 khung + lời có mốc giây. Điểm 4 trục (cảm xúc · tắt tiếng · nhịp · bố cục): phần 1 (0–185 s) 2·3·3·2 · phần 2 (185–451) 3·4·3·3 · phần 3 (451–580) 3·3·3·3 · phần 4 (580–626) 2·3·2·2.

Luật (§1a): lời phê chỉ thành việc sửa khi phép thử của vai sở hữu cũng trượt ở đúng chỗ đó. Đối chiếu:

| Lời phê (mốc) | Phép thử vai sở hữu ở cùng chỗ | Xử lý |
|---|---|---|
| 23/38 s: lưới vuông trước khi thấy phố; 38 s gần như toàn tối đọc thành "thuê gần như luôn thắng" | cổng gốc B02, B03 lật xuống (chẩn đoán) | **nêu G2** (cổng gốc không mở vòng — 14/10); hướng: hàng nhà góc thấp sáng dần trước, lưới từ trên để sau |
| 162/177 s: thẻ "5%" trên cửa — thiết bị của cả tập — không đọc được | "chỗ muốn tua" S07 2/3 + cổng gốc B07 lật xuống (thiếu "thẻ trên cửa") | **đề xuất sửa hình ở G2** (cận thẻ trên cửa rồi lùi về hộp; đoạn b ≈ 11 phút máy + ghép) — không dựng trong chặng này vì checks đủ bộ đang chạy trên r2 |
| 262/351 s: "dark" = nâu sáng hơn nhà chưa lộ (xanh navy); nhà tối nhất có cửa vàng phát sáng | — (liền mạch: màu lựa chọn đúng thiết kế — người thuê hơn = cửa warn) | **câu hỏi màu ở G2**: cửa warn phát sáng đọc thành "sáng"; phương án: cửa người-thuê-hơn tối hẳn, nhà chưa lộ xám |
| 285/307 s: tiêu đề chồng chú giải; 3 số cùng lúc (3 in 4, 75.6%, 75 of 307) | cổng gốc B13–B15 ĐẠT | chỉ báo |
| 440 s: hàng ô xám bên phải khi lời nói "cửa tối đã hết" (tháng chưa đủ 15 năm dữ liệu) | B22–B23 ĐẠT | chỉ báo; G2: ô "chưa có dữ liệu" mờ hơn |
| 521/532 s: số trên hình không đọc (73.6 % …); biến thể T-bill không đổi hình | cổng gốc B27 ĐẠT; checks claims (xem M5-checks) | chỉ báo |
| 564–575 s: điểm của Nina nhỏ ở góc, không nhãn 56.8 % | B32 ĐẠT | chỉ báo |
| 593–605 s: bảng điểm che dãy tối; cảnh rộng đứng 8 s với Nina nhỏ | "chỗ muốn tua" S31 2/3 (lý do: tóm tắt) | nêu G2 cùng câu hỏi cắt lời S31 |
| 609–617 s: câu hỏi còn trên hình khi lời trả lời | B33 ĐẠT | chỉ báo |

Ghi nhận: người phê nói "khung đứng 8 s" ở 601–605 s — trên nháp máy đang tiến chậm (vòng nhịp), mắt đọc tấm tĩnh không thấy; freezedetect 0 s.
