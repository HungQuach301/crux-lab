# H2 · Đuôi end screen (S13, 18 s) — kế hoạch

Khung 1920×1080 (số px @1080p). YouTube đặt 2 ô video + 1 nút đăng ký đè lên hình; hình nền chỉ chừa chỗ, **không vẽ chữ hay nút giả**.

## Nối từ cảnh cuối (S12.5 "History, not a forecast.")
Cảnh cuối của H2 là dải địa hình T-bill kết thúc ở "hôm nay" (8/2026), bên phải trống. Đuôi giữ đúng hình đó:
1. 0–1,2 s: ray 9%, hạt thoi và mọi nhãn mờ đi (0,35 s mỗi thứ, token `timing.fadeSec`); dải địa hình **co và dời** sang trái: x 96–900, y 560–900, alpha 40%. Điểm cuối "hôm nay" giữ một chấm `accent` nhỏ.
2. 1,2–2,0 s: từ điểm "hôm nay", **khoảng trống bên phải** (nơi "không lần chạy nào cho thấy được") mở ra thành hai khung viền `grid` 4 px — đó là chỗ của hai ô video: phần "tiếp theo" của lịch sử là video kế tiếp.
3. 2,0–18 s: đứng yên (≤ 20 px/s trôi nhẹ của dải địa hình nếu cần), nhạc; lời S13.1–S13.2 ở 0–6 s.

## Vị trí phần tử YouTube (đặt trong Studio, khớp khung viền)
| Phần tử | Hộp (x, y, w, h) @1080p | Ghi chú |
|---|---|---|
| Video 1 ("Another replay from this channel", video gần nhất/đề xuất) | 1040, 120, 768, 432 | 16:9, khung viền `grid` vẽ sẵn lệch ra 12 px |
| Video 2 (playlist hoặc video phù hợp người xem) | 1040, 600, 768, 432 | đáy 1032, cách mép dưới 48 px |
| Nút đăng ký | tâm (300, 300), Ø 220 | nằm trên dải địa hình, vùng trống phía trên nửa leo |

## Hình nền
- Nền `bg #0E1116`; dải địa hình `accent` 40% (đường) + 6% (diện tích); không ray, không bể, không thùng, không số, không huy hiệu (không còn số của Leah trên màn hình).
- Không chữ trên hình (YouTube tự vẽ tiêu đề video); nếu cần một câu, dùng "History, not a forecast." ở bậc `caption` 64 px `ink-muted`, x 96, y 1000, tắt trước khi các ô video hiện (2,0 s).

## Kiểm
- Tổng 18 s (trong 15–20 s); phần tử YouTube hiện từ 2,0 s.
- Khung viền chỉ là chỗ chừa: nếu YouTube đổi kích thước phần tử, viền vẫn ở dưới, không chạm chữ YouTube (khoảng đệm 12 px).
