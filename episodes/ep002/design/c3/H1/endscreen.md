# H1 · Kế hoạch đuôi end screen (S13, 15–20 s)

Toạ độ theo khung 1920×1080 (nhân 2/3 cho bản 1280×720). Đuôi dài **18 s** (S13.1–S13.2 nói ~6 s, còn ~12 s nhạc). YouTube cho đặt end screen trong 5–20 s cuối; ở đây phần tử xuất hiện từ giây 2,0 của đuôi và giữ tới hết (16 s).

## Hình nền: chính bàn lịch sử, lặng xuống
- Vật: **dãy núi T-bill** (1954 → hôm nay, `accent`) nằm thấp ở nửa trái–dưới khung; khay, khung kính, thanh trượt, hũ, xu đã rời bàn.
- Mép phải dãy núi là **"hôm nay"** (8/2026); bên phải nó là mặt bàn trống — đúng hình của S12.5/S10.7 "History, not a forecast": chỗ trống đó là nơi đặt hai ô video.
- Ánh sáng hạ ~40% (đèn chính 170 → 70), chỉ còn sợi dây sáng trên sống núi; tường sau gần `bg #0E1116`, nên ô video và nút đăng ký nằm trên nền tối phẳng, không có vật chuyển động dưới chúng.
- Máy quay: một lần kéo lùi chậm trong 1,2 s đầu, sau đó đứng gần yên (trôi ≤ 5 px/s), không quay vòng.

## Bố cục phần tử YouTube (1920×1080)
| Phần tử | Hộp (x, y, w, h) | Nằm trên |
|---|---|---|
| Video 1 (một tập khác của kênh — "Another replay from this channel", S13.2) | 1136, 120, 688, 387 | tường tối, bên phải "hôm nay" |
| Video 2 (video phù hợp nhất với người xem, YouTube chọn) | 1136, 567, 688, 387 | mặt bàn trống bên phải "hôm nay" |
| Nút đăng ký (tròn) | tâm 300, 260, đường kính 200 | tường tối trên nửa trái dãy núi |
| Vùng an toàn của hình nền (không có vật sáng) | x ≥ 1080 toàn chiều cao; và hình tròn bán kính 140 quanh nút | — |

- Dãy núi chiếm khoảng x 96–1040, y 640–940 (đỉnh 1981 cao nhất), không chạm hộp nào ở trên (cách ≥ 40 px).
- **Không chữ** trong đuôi ngoài một dòng `note` `ink-muted` trên tấm nền `bg`: "Every assumption is in the description" ở (96, 1010), hiện 0,5–6 s rồi mờ đi (khớp S13.1); không đặt dưới phần tử nào. Không huy hiệu ILLUSTRATIVE (không còn số của Leah).

## Chuyển từ cảnh cuối (S12 → S13)
1. S12.5 "History, not a forecast" kết thúc ở cảnh thước + thẻ đề nghị trống trên nền dãy núi (H1: thanh trượt, kẹp xanh, thẻ không tên). 
2. 0,0–1,2 s: thẻ trống bay lên, ra khỏi khung phía trên; thanh trượt, khay và chồng xu **chìm xuống mặt bàn** (dịch y −0,3, mờ) — cùng ngữ pháp "rời bàn"; máy quay kéo lùi và hạ để dãy núi nằm thấp, mặt bàn trống bên phải "hôm nay" lộ ra.
3. 1,2–2,0 s: đèn hạ; sợi dây sáng chạy dọc sống núi từ trái sang phải một lần và dừng ở "hôm nay" (lặp lại chuyển động "lịch sử chạy tới đây và dừng").
4. 2,0 s: YouTube hiện hai ô video và nút đăng ký trong vùng đã chừa; hình đứng yên tới hết 18 s; nhạc đóng ở 18 s.

## Dựng
Cảnh `s13.js` dùng lại `src/world.js` (`ridge`, `ridgeWire`, `table`, `lights`) với tham số đèn thấp; render như K-clip (CPU, 1280×720 hoặc 1920×1080 ở C5). Kiểm: không chuỗi nào trong hộp phần tử; vùng x ≥ 1080 có độ sáng trung bình ≤ L* 12 suốt đuôi.
