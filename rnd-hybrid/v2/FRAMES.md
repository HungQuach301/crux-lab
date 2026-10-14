# R&D hình lai vòng 2 · Bước 1: khung phong cách (14/10/2026) — chờ chủ dự án chọn

Cùng một khoảnh khắc ("1931: hàng người trước ngân hàng đóng cửa, Walt lo lắng"), ba ảnh tĩnh 1920×1080. Cả ba dùng bảng màu kênh, rig.js (Walt mặt lo lắng), nhãn ILLUSTRATIVE, không dùng AI sinh hình.
Cả ba cắm vào `toolkit/factory/world/render_shots.js --stills` **nguyên trạng** (mỗi khung = một đoạn `scene.js` + `spine.json`). Nhà máy trên main và `checks/` không bị sửa.

| Khung | Tệp | Chi phí (đo) | Độ khó tái dùng |
|---|---|---|---|
| **A** giấy trong 3D | `frames/out/A-1080.png` | API 0 $; 7,8 s máy/khung đầu (gồm mở trình duyệt), sau đó ≈ 1,6 s/khung ở 1080p, 1 worker | **Thấp.** `v2/paper3d.js`: `paperFigure`, `Bank`, `Row`, `Street`, `Lamp`, `ACT` (đèn theo hồi). Tập mới đổi toạ độ và hồi. Chuyển động máy quay 3D dùng thẳng `core.Camera` |
| **B** minh hoạ 2D giàu | `frames/out/B-1080.png` | API 0 $; ≈ 5,5 s/khung (vẽ lại bán sắc mỗi khung; cache nền tĩnh sẽ giảm mạnh) | **Cao.** Nền vẽ tay bằng toạ độ cho từng khung cảnh, mỗi bối cảnh mới phải vẽ lại. Máy quay chỉ có pan/zoom 2D, mất góc máy 3D của nhà máy |
| **C** ảnh tư liệu + giấy | `frames/out/C-1080.png` | API 0 $; ≈ 1,5 s/khung; ảnh LoC miễn phí, mất ≈ 10 phút người cho hồ sơ quyền mỗi ảnh | **Trung bình.** Mã dùng lại được (LUT tông kênh + `inkChar`), nhưng mỗi cảnh cần một ảnh có thật, đúng năm, đúng sự kiện, kèm dòng RIGHTS. Trần §F3 là ≤ 20 % thời lượng tập, ≤ 6 s liền |

Hai lần dựng lại cho ra khung trùng byte: A `bbff35ad…`, B `66262cfd…`, C `430f0d4c…` (SHA-256 16 ký tự đầu). Nhìn nhanh cả ba: `frames/out/ABC-contact.jpg`.

## Từng khung
- **A**: nhân vật và đạo cụ là tấm giấy có dày thật: mặt in, 3 lớp mép, lưng kraft. Viền sáng nằm lệch về phía đèn ngược. Bóng thật đổ theo đường bao giấy (`customDepthMaterial`). Ba lớp sâu: Walt ở tiền cảnh; hàng 7 người giấy, ngân hàng low-poly (bậc thềm, 6 trụ, trán tường, cửa đóng, tờ CLOSED) và đèn phố ở trung cảnh; dãy phố và đường chân trời trong sương ở hậu cảnh. Ánh sáng là hồi `crisis1931`: trời lạnh, đèn phố ấm, đèn bù mặt.
- **B**: nét mực 3–7 px, chuyển màu theo ánh sáng, bán sắc (halftone) ở phía tối, vân giấy, mưa. Nền vẽ chi tiết gồm nhà gạch, cửa sổ sáng có quầng, ngân hàng có trụ khía rãnh, vỉa hè ướt phản chiếu.
- **C**: ảnh LoC cắt 16:9, phủ tông kênh (LUT #0E1116 → muted → giấy #EDE4CF), làm mờ nhẹ, thêm hạt và tối dần về phía Walt để tách lớp. Walt giấy có bóng đổ lên ảnh. Ảnh chỉ có tên nguồn và năm, không đi kèm claim số (§F4).

## Cần biết
- **C, quyền ảnh:** `rights_advisory` ghi nguyên văn ở RIGHTS §F6 dòng `X-RND-1`, bậc 5 (đánh giá của tổ chức, không bảo đảm). Tệp gốc để ở `work/external/` (ngoài git).
- **C, độ khớp với câu chuyện:** ảnh là **đám đông giơ biển phản đối dưới mưa**, không phải một hàng người xếp hàng. Vì vậy tiêu đề phụ của C đổi theo nhãn LoC thành "Depositors gather outside a failed bank".
- **C, năm của ảnh:** LoC ghi năm 1931. Theo hiểu biết chung, Bank of United States đóng cửa ngày 11/12/1930, **nhưng phiên chưa kiểm** điều này. Nếu chọn C thì phải đối chiếu nguồn gốc trước khi viết năm vào lời.
- **C, vị trí dòng nguồn:** Walt chiếm mép phải, nên dòng nguồn đặt ở góc trên trái thay vì bên phải dải chú thích (§F3). Bản dựng động sẽ đặt lại cho đúng.
- **A, thứ còn thô:** Hàng người ở trung cảnh hơi tối vì bị ngược sáng. Đèn phố đứng chắn trước bậc thềm. Tờ CLOSED nhỏ, khó đọc ở 1080p.
- **B, thứ còn thô:** cột đèn đứng đè lên mặt tiền, hàng người hơi to so với cửa.

## Tái lập
`cd toolkit/factory/world/vendor && npm ci`, rồi từ gốc repo:
`NODE_PATH=$(npm root -g) node toolkit/factory/world/render_shots.js rnd-hybrid/v2/frames/<A|B|C> 1080 x.mp4 --stills 0 --stills-dir rnd-hybrid/work/stills`.
Khung C cần `rnd-hybrid/work/external/bank1931_crop.jpg`; cách tạo xem RIGHTS §F6 `X-RND-1`.
