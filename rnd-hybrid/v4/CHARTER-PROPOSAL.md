# Đề xuất CHARTER cuối, đóng R&D rnd-hybrid (vòng 4, 14/10/2026). CHỈ ĐỀ XUẤT

Phiên này **không** sửa `CHARTER.md`, `checks/` hay toolkit/factory. Sửa hiến chương và chuyển mã vào nhà máy là việc của chủ dự án (CHARTER §6) và của phiên nhà máy F-17.

Đề xuất này thay mọi bản trước, gồm `v3/CHARTER-PROPOSAL.md` (P3) và bản nháp H4′. Nó dựa trên lần chủ dự án duyệt vòng 4 có điều kiện.

Số đo dẫn chứng lấy từ:
- `v4/REPORT.md`;
- `v4/out/meas/table.md`;
- hai tờ ghép `v4/out/SHEET-before-after.jpg` và `v4/out/SHEET-history.jpg`.

---

## Đ1. Lớp ánh sáng điện ảnh `cine`, opt-in (F-17)
> Thế giới 3D của nhà máy được thêm một lớp ánh sáng **tuỳ chọn**, khai bằng khoá `cine` trong spine.json, như F-14. Không khai thì khung render trùng byte bản cũ.
>
> Lớp gồm:
> - HDRI Poly Haven CC0 qua PMREM, chọn theo hồi;
> - vân vật liệu CC0 cho đường, tường, mái, gỗ và giấy (≤ 1024 px);
> - bóng mềm;
> - GTAO;
> - độ sâu trường ảnh có xét độ sâu, theo chủ thể;
> - chỉnh màu theo hồi, kèm hạt phim tất định;
> - người khối của lib3d thành bóng ngược sáng có viền sáng, không mặt.
>
> Lớp chữ 2D không đi qua hậu kỳ.
>
> **Điều kiện bật trong một tập.** Đây là các điều kiện phiên đề xuất, rút từ giới hạn trong `v4/REPORT.md`. Chủ dự án duyệt "có điều kiện" nhưng không liệt kê điều kiện, nên chủ dự án sửa danh sách nếu khác ý:
> 1. **Màu dữ liệu không đổi nghĩa.**
>    - Vật dữ liệu (`userData.checks.role` series/bar) không nhận vân màu, và chỉ nhận 0,15 phản xạ môi trường.
>    - Thêm luật kiểm thứ tự độ sáng giữa các màu dữ liệu, trước và sau lớp. Cột vốn tối hơn thì sau lớp vẫn phải tối hơn.
>    - Lỗi đã thấy ở Tập 7, cảnh c 85 s: cột "hi" từ tối hơn thành sáng hơn.
> 2. **Cảnh đồ thị giữ nền tối** (`sky: 0`). Trời HDRI chỉ hiện ở cảnh thế giới.
> 3. **DOF:**
>    - cảnh rộng khẩu ≤ 0,12, vì DOF mạnh làm cảnh thành sa bàn đồ chơi;
>    - DOF rõ chỉ dùng cho cảnh cận;
>    - bắt buộc dùng bokeh có xét độ sâu, vì bản gốc của three tạo quầng quanh người.
> 4. **Ngân sách máy:** khai giờ máy mỗi phút phim trong báo cáo tập.
>    - Mặc định AO chỉ cho cảnh cận, hoặc chạy ở nửa độ phân giải (chưa đo, phải đo trước khi chốt).
> 5. **Khung cận 1080p trước khi dựng tiếp.** Mỗi tập bật `cine` phải gửi chủ dự án 1 khung cận người và 1 khung dữ liệu ở 1080p, bản trước và sau, rồi mới dựng cả tập (`LESSONS.md` L3).
> 6. **Tất định:** dựng hai lần trùng byte trên một khung của tập.

| | |
|---|---|
| **Ưu** | Sửa đúng nguyên nhân "phẳng" (`LESSONS.md` L2): cùng mã cảnh nhưng có không khí, chiều sâu và vật liệu. Không đụng `core.js`, `lib3d.js` hay `scene.js` của tập: bọc bằng 3 dòng. Tất định (PNG trùng MD5 `194d4bec…`). Tài sản CC0 nhỏ (18 tệp, ≤ 2 MB mỗi tệp), có SHA-256. Chi API 0 $ |
| **Nhược** | **Đắt:** 5,1–7,4 s/khung 1080p so với 0,4–1,1 s (gấp 6,9–12,8 lần). Một tập 10 phút ≈ 7–9 giờ máy với 4 worker, so với ≈ 0,5–1,3 giờ. AO tốn +1,6–2,4 s/khung, DOF +1,3–1,5 s, HDRI +0,5–1,1 s. Viền sáng của người vẫn hơi giống nét viền dán. Còn vệt sáng mảnh ở mép (MSAA lệch bộ đệm độ sâu) |
| **Tác động** | Nhà máy: thêm `toolkit/factory/world/cine/` (từ `rnd-hybrid/v4/light/`) và khoá spine `cine: {look, focus, aperture, sky, override}`, cộng bảng hồi theo tập. `render_shots.js` cần MIME cho `.hdr`/`.jpg` (hiện trả octet-stream, vẫn chạy được). Thêm luật kiểm màu dữ liệu ở checks-appeal cho phiên K. D-010 ("low-poly tối giản, không chân thực ảnh") cần ghi rõ: vân và ánh sáng được phép, hình khối vẫn tối giản |
| **Rủi ro** | Ánh sáng đổi phương theo hồi làm bóng đổ khác bản đã duyệt (bóng chồng tiền ở cảnh cận mất vì ngược sáng). Lạm dụng DOF cho cảnh rộng sẽ quay lại "đồ chơi". Thời gian dựng tăng mạnh, dễ bị cắt lớp lúc vội; khi đó chỉ được cắt theo thứ tự AO → DOF, không cắt luật màu dữ liệu. Lớp phụ thuộc chi tiết nội bộ của three 0.186 (accessor `render`, fragment BokehPass), nên phải kiểm lại khi nâng three |

## Đ2. Chương lịch sử không vẽ người
> Chương lịch sử (trước khoảng năm 1960) **không có người minh hoạ**, chỉ dùng ba loại hình:
> 1. **Ảnh tư liệu toàn khung** (LoC hoặc nguồn theo danh sách trắng RIGHTS §F1) như một bản in.
>    - Chỉnh tông cùng bảng màu hồi, hạt tất định, viền giấy mảnh trên nền tối.
>    - **Chữ in serif** cho mốc có nguồn (theo `v2/CLAIMS.md`), nhãn ARCHIVE PHOTO, dòng nguồn.
>    - Không dán gì lên ảnh.
> 2. **Phim công cộng:** chỉ dùng mục mà trang lưu trữ ghi rõ Public Domain (vd Prelinger trên archive.org, `licenseurl` publicdomain). Ghi RIGHTS §F6, kèm SHA-1 khớp trang và SHA-256.
>    - Xử lý: ổn định (vidstab 2 lượt), chỉnh tông cùng bảng màu, viền 4:3 trên nền tối.
>    - Không dùng hình có người còn sống nhận diện được.
> 3. **Vật thể số liệu 3D đã lên đèn** (Đ1), không người. Ví dụ K2: sổ cái 20 → 30 năm, mỗi ô là một tháng trả.
>
> Mỗi lần dùng ảnh hoặc phim: ≤ 6 s liền, tổng ≤ 20 % thời lượng chương (giữ từ v3).

| | |
|---|---|
| **Ưu** | Hết hẳn vấn đề "người vẽ bằng mã trông phẳng/đồ chơi" ở chương lịch sử. Tư liệu thật có sức nặng hơn tranh minh hoạ. Vật thể số liệu 3D nối được sang phần hiện tại bằng cùng ánh sáng. K1 dựng chỉ 0,36 s/khung |
| **Nhược** | Phụ thuộc kho tư liệu: không phải mốc nào cũng có ảnh hay phim PD phù hợp. Chưa có **bản đồ** PD/CC0 đúng nghĩa (bản đồ trong phim Prelinger là bản đồ quảng cáo, dùng sẽ hiểu sai). Phim Prelinger độ phân giải thấp (640×480), nên mềm ở 1080p. Ở đoạn đã thử, bước ổn định không có tác dụng đo được (máy gốc đứng yên) |
| **Tác động** | RIGHTS §F3 hiện ưu tiên "đặt ảnh trong thế giới", nên cần đảo lại cho chương lịch sử (A39/F15 ở phiên K). Chữ in serif hiện vẽ thẳng bằng `O.ctx`, **không vào nhật ký chữ của trang kiểm**: nhà máy cần `O.text` có tuỳ chọn font serif trước khi dùng thật. Spine cần trường `era: history|today` |
| **Rủi ro** | Ảnh tư liệu dễ bị đọc sai: đọc mù vòng 3 thấy ảnh LoC giống biểu tình. Tiêu đề chữ in giúp được, nhưng chưa kiểm lại. Năm catalog có thể lệch năm sự kiện (LoC ghi 1931, ngân hàng đóng cửa 12/1930), nên bắt buộc đối chiếu nguồn gốc. Nhãn "Public Domain" của kho là **đánh giá của tổ chức, không phải bảo đảm** |

## Đ3. Bỏ hẳn các hướng nhân vật vẽ bằng mã
> **Không** mở lại các hướng:
> - giấy cắt hoặc giấy nhiều lớp (v1, v2, H3, P1);
> - chibi Kenney (H4);
> - Quaternius (H4′);
> - tượng sa bàn (P2);
> - tranh in báo 2.5D (P3).
>
> Nhân vật ở phần hiện tại giữ `Person` của lib3d (không mặt), dưới lớp `cine` (Đ1). Mã và tài sản của các hướng đã bỏ nằm lại `rnd-hybrid/` làm hồ sơ R&D, không chuyển vào nhà máy.

| | |
|---|---|
| **Ưu** | Dừng vòng lặp tốn công: 4 vòng hỏng cùng một kiểu (`LESSONS.md` L1). Nhà máy giữ một loại người duy nhất, đã qua checks. Không rủi ro giấy phép với mô hình người |
| **Nhược** | Mất khả năng kể chuyện bằng gương mặt và biểu cảm. Cảm xúc chỉ còn qua dáng, cử chỉ và ánh sáng. Móc `posture` của lớp có sẵn nhưng **chưa dùng**, nên dáng cảm xúc mới chưa được thử |
| **Tác động** | Gỡ đề xuất Đ1 và Đ2 của `v3/CHARTER-PROPOSAL.md` (P3 và biến thể "Today"). Ngoại lệ D-010 cho chương lịch sử không còn cần. `rnd-hybrid/v3/` và `v3/assets/` (Kenney, Quaternius, CC0) giữ làm hồ sơ, không dùng trong tập |
| **Rủi ro** | Người khối không mặt có thể vẫn bị thấy là "đồ chơi" ở cảnh cận nếu ánh sáng kém. Vì vậy điều kiện Đ1.5 (khung cận 1080p cho chủ dự án xem trước) là bắt buộc |

## Đ4. Áp thử
> Áp Đ1–Đ3 trên **một đoạn thế giới của tập tiếp theo** (cảnh cận + cảnh dữ liệu) và **một chương lịch sử của Tập 9** ("How the 30-year mortgage was invented", ≈ 60–90 s, cùng các mốc K1/K2).
> - Chuyển lớp vào nhà máy (F-17) **sau** khi chủ dự án xem khung cận 1080p.
> - Rút về nếu phiếu L3 của chủ dự án ở G2 kém hơn bản không lớp, hoặc nếu luật màu dữ liệu trượt.

| | |
|---|---|
| **Ưu** | Thử thật, quy mô nhỏ, rút lui được |
| **Nhược** | Thêm giờ máy (≈ 7–9 giờ cho mỗi 10 phút nếu bật đủ lớp) |
| **Tác động** | Phiên F-17 ở nhà máy, gồm test tất định và test luật màu |
| **Rủi ro** | Đánh giá thẩm mỹ chưa có đọc mù vòng 4. Hình đã thay đổi mà chưa đo lại khả năng đọc |
