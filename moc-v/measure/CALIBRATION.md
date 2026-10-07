# Hiệu chuẩn bộ phân loại khung (`frames.py`) bằng mắt — 06/10/2026

Mẫu: 12 khung ngẫu nhiên mỗi tập (seed 5), nhãn máy in trên ảnh: `calibration/cal-ep00{1..4}.png` (cỡ ½).
Người xem: phiên Mốc V (không phải người chấm độc lập — hạn chế).

| Tập | Khung | Máy xếp đúng | Sai |
|---|---|---|---|
| 1 | 12 | 12 | — |
| 2 | 12 | 12 (xem nhanh) | — |
| 3 | 12 | 12 | — |
| 4 | 12 | 10 | t101 (đường chỉ số vừa bắt đầu vẽ, < 1,2 % khung) và t320 (thang N2 mảnh) bị xếp "chỉ có chữ" |

→ 46/48. Sai lệch nghiêng về đếm THỪA "chỉ có chữ" ở Tập 4; đối chiếu độc lập bằng timeline nhà máy (mẫu `title` + `bignum` + `method` + `endcard` ≈ 37 %).
Nhân vật khi lời nhắc tên: khung giữa mỗi phụ đề có tên nhân vật (`char-hits.json`), tờ `calibration/char-ep00{1..4}.png`, đếm bằng mắt (hình người / vật hoặc dấu riêng của nhân vật).
