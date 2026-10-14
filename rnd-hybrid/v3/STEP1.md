# R&D vòng 3 · Bước 1: mẫu chọn hướng H4 | H3 (14/10/2026). Chờ chủ dự án chọn

**Nhận xét của chủ dự án và nguyên nhân:** nhân vật và vật thể phẳng nên nhàm. `paperFigure()` chỉ là một tấm phẳng dày 14 mm, đạo cụ cũng vậy.

Hai hướng dựng cùng 3 cảnh, cùng máy quay, cùng đèn (`v3/lib/sets.js`):
- **S1:** 1930, đám đông trước ngân hàng đóng cửa;
- **S2:** 1934, người vay ký hợp đồng FHA;
- **S3:** lưới trả dần 20 → 30 năm (mỗi cột 1 năm, 12 ô = 12 kỳ trả; ô cao theo khoản trả tháng, minh hoạ ở lãi 5 %, không ghi số).

Mỗi hướng có thêm **đoạn 6 s máy lượn 25°** quanh Walt. Cả hai cắm vào `toolkit/factory/world/render_shots.js` nguyên trạng.

| | **H4: 3D có xương + hậu kỳ toàn khung** | **H3: giấy gấp 3D + giấy 5 lớp** |
|---|---|---|
| Khung 1080p | `out/H4-S1/S2/S3-1080.jpg` | `out/H3-S1/S2/S3-1080.jpg` |
| Đoạn lượn 6 s | `out/H4-orbit-6s-1080.mp4` | `out/H3-orbit-6s-1080.mp4` |
| Tờ so sánh | `out/H4-vs-H3.jpg` (3 cảnh, trái H4, phải H3) · `out/orbit-H4-vs-H3.mp4` (hai đoạn lượn cạnh nhau) | |
| Người | Kenney *Mini Characters* (CC0): **xương thật** (chân, thân, tay, đầu), clip có sẵn trong GLB. Dùng: `idle` (đứng chờ), `emote-no`, `holding-right`, `sit`, cộng `interact-right` chỉ cho tay phải khi ký, `emote-yes`. Trang phục 1930: đổi bảng màu (dạ xám/nâu/than, sơ mi kem) và thêm **mũ phớt** dựng bằng khối gắn vào xương đầu | rig.js tách **5 lớp** (tay sau · chân sau · thân + chân trước · đầu, mũ, mặt · tay trước), cách nhau 3,5 cm theo z. Mỗi lớp cong nhẹ (uốn parabol), có lưng giấy kraft, đổ bóng lên lớp sau. Mặt in nét mực, bán sắc, vân giấy (chất B) |
| Mặt / cảm xúc | Decal vẽ bằng `drawFace` của rig.js trên xương đầu, đổi theo cảm xúc (lo, buồn, sốc, vui). Màu da lấy từ chính mô hình | Như vòng 2 (rig.js), nhưng mặt nằm ở lớp đầu riêng |
| Đạo cụ / nhà | Kenney *Furniture Kit*, *City Kit Commercial/Suburban* (CC0) cộng ngân hàng low-poly của v2. **Mọi thứ cùng một hậu kỳ:** toon 4 bậc, nét mực Sobel theo depth/normal (2 px), bán sắc chấm 45° ở vùng tối, vân giấy, viền tối | Tự dựng: khối **giấy gấp** (mặt hơi lõm, nếp tối), **cột giấy cuộn** có mép dán, trán tường lăng trụ, bàn ghế gấp, ô lưới gấp |
| Giờ máy (1080p, 4 lõi, swiftshader) | 3 khung: **7 s**, gồm cả khởi động trang. Lượn 6 s: **208 s tường**, 4 worker (≈ **35 s máy / s phim**) | 3 khung: **38 s** (khởi động lâu vì vẽ 65 lớp giấy). Lượn 6 s: **573 s tường** (≈ **96 s máy / s phim**) |
| Walt trong đoạn lượn | ≈ 66 % chiều cao khung | ≈ 64 % chiều cao khung |
| Chi | **0 $** (không gọi API) | **0 $** |
| Tái dùng | **Cao.** Thêm người = thêm tệp GLB CC0 + bảng màu; 31 clip có sẵn; hậu kỳ một lần áp cho mọi cảnh | **Trung bình.** Mỗi tư thế, biểu cảm, đạo cụ phải vẽ hoặc dựng tay; không có chuyển động khớp (giấy chỉ trượt, xoay) |

## Nhận định (của phiên, không phải đọc mù)
- **H4** có khối thật, ánh sáng đi quanh nhân vật khi máy lượn, và chuyển động có sẵn. Nét mực và bán sắc làm người, vật, nhà ra cùng một chất. Đổi lại, nhân vật là **chibi khối vuông** của Kenney: dễ thương, nhưng gần game hơn phim tài liệu. Mặt decal phẳng dán trên mặt khối, và chưa có clip "ký" riêng (đang dùng `interact-right` cho tay phải).
- **H3** giữ chất giấy và nét vẽ tay của vòng 2, có chiều sâu hơn tấm phẳng (5 lớp, bóng giữa các lớp, đạo cụ gấp có khối). Nhưng nhân vật vẫn **xoay theo máy** để không lộ cạnh. Khi máy lượn 25°, cảm giác 3D chủ yếu đến từ đạo cụ và thị sai giữa các lớp. Người không cử động khớp, và giờ máy cao gấp ≈ 2,7 lần H4.

## Đã sửa trong lúc dựng
- **H4, nét mực:** ở 1080p nét gần như không thấy, nên tăng lên 2 px và hạ ngưỡng depth/normal (commit `d67a822`). Đã dựng lại H4.
- **H3, lần dựng đoạn lượn đầu hỏng:** `TimeoutError`, vì 4 trang cùng khởi động quá 180 s (vẽ bán sắc cho 65 lớp). Đã bỏ bán sắc ở lớp của đám đông; Walt vẫn giữ. Sau đó có một lỗi cú pháp do chú thích nuốt mất cuối dòng, cũng đã sửa. Các số giờ máy ở bảng trên là của lần dựng chạy được.

## Nguồn & giấy phép
RIGHTS.md §F7: 4 gói Kenney, **CC0 1.0**, trích nguyên văn `License.txt` cùng SHA-256 của zip. Chỉ tệp CC0 nằm trong repo (`v3/assets/kenney/`, 4,6 MB). `.gitignore` có `rnd-hybrid/v3/assets/nonfree/` cho tệp không phải CC0 về sau; vòng này không có tệp nào như vậy. KayKit Adventurers (CC0) đã xét nhưng không dùng, vì nhân vật giả tưởng không hợp năm 1930.

## Tái lập
`cd toolkit/factory/world/vendor && npm ci`, rồi từ gốc repo chạy `bash rnd-hybrid/v3/render.sh` (khung tĩnh dựng bằng `--stills 0.5,1.5,2.5`, đoạn lượn là 6 cảnh 1 s ở t = 10–16).
