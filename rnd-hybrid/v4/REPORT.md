# Vòng 4 · ánh sáng điện ảnh + người bóng ngược sáng + chương lịch sử không vẽ người (14/10/2026). DỪNG chờ chủ dự án chọn

**Gói 3 câu:**
1. Lớp ánh sáng opt-in `v4/light/cine.js` bọc nguyên cảnh thật của Tập 7, không sửa dòng nào của nhà máy hay của tập. Lớp gồm HDRI Poly Haven CC0 theo hồi, vân vật liệu CC0, bóng mềm, GTAO, độ sâu trường ảnh theo chủ thể, chỉnh màu và hạt phim, và người viền sáng. Kết quả tất định (hai lần dựng trùng byte).
2. Sau lớp, thế giới có chiều sâu, có không khí và có vật liệu. Đổi lại, một khung 1080p tốn **5–7 s máy thay vì 0,4–1,1 s**. AO là lớp đắt nhất (+1,6–2,4 s/khung), kế đến DOF (+1,3–1,5 s) và HDRI (+0,5–1,1 s).
3. Chương lịch sử không vẽ người dựng được bằng ảnh LoC toàn khung có chữ in (K1) và vật thể số liệu 3D đã lên đèn (K2). Phim Prelinger (Public Domain) đã qua xử lý thử: ổn định, chỉnh tông theo cùng bảng màu, thêm viền.

## Tệp để chọn (chỉ ảnh tĩnh 1080p, không clip)
- **Tờ trước | sau, Tập 7:** `v4/out/SHEET-before-after.jpg`. Gồm 3 cảnh thật: Tessa cận, phố/nhà, dữ liệu.
- **Tờ lịch sử:** `v4/out/SHEET-history.jpg`. Gồm K1 tư liệu, K2 lưới 20 → 30 năm (trước/sau lớp), và phim Prelinger (gốc/đã xử lý).
- **Từng khung 1080p:** `v4/out/stills/*-1080.jpg` (JPEG q95). Kiểm cận Tessa ở 1080p: `v4/out/stills/close-check-1080.png` (cắt rồi phóng ×2, không làm mượt).
- **Phim:** `v4/out/hist/film-{raw,processed}-1080.png`.

**Chọn cảnh.** Tập 7 **không có nhân vật "Nina"**: nhân vật của tập là Tessa và Leo (`episodes/ep007/world/c4kit.js`, `CHAR`). Vì vậy cảnh cận dùng Tessa.

| Cảnh | Đoạn · giây | Hồi (đề xuất) | Ghi chú |
|---|---|---|---|
| Tessa cận | a-s01-s03 · 27 s | 1 · ngày | Tư thế cHand: tay Tessa chỉ tấm giấy vay. Đèn chính đặt **sau lưng** (ngược sáng), DOF theo người |
| Phố / nhà | g-s29-s33 · 3 s | 3 · hoàng hôn | Hai nhà Leo và Tessa |
| Dữ liệu | c-s10-s15 · 85 s | 2 · chiều | Lưới tuần, nhãn "tallest". **Giữ nền tối** (không hiện trời) để chữ và màu dữ liệu đọc được |

## Việc 1: lớp ánh sáng (opt-in, đề xuất F-17)
**Cách gắn, không sửa mã cũ.**
- Mỗi cảnh bọc chỉ có 3 dòng `scene.js` (`v4/ep7/<cảnh>/scene.js`). Nó import `boot` của cảnh gốc rồi gọi `wrap(boot, {look, focus, aperture, sky, override})`.
- Three.js gán `render` bên trong hàm dựng, nên lớp đặt **accessor trên `WebGLRenderer.prototype`**. Lần gán đầu (hàm của three) được cất lại; `core.Stage` vẫn bọc `renderer.render` như cũ.
- Mỗi lần cảnh gọi render, lớp vẽ qua EffectComposer. Các lần render bên trong composer đi thẳng xuống hàm gốc.
- Vì thế nhật ký trang, máy quay, khung dọc và dither F08 của core giữ nguyên. Lớp chữ 2D không đi qua hậu kỳ, nên chữ sắc như cũ.
- Bảng hồi nằm ở `v4/light/looks.js`, gồm `LOOKS` (day / afternoon / dusk) và `ACT` (Tập 7: a, b → ngày; c, d, e → chiều; f, g → hoàng hôn).

| Lớp | Làm gì | Tham số chính |
|---|---|---|
| **HDRI** | Equirect `.hdr` 1k → PMREM, dùng làm `scene.environment` + nền trời (tuỳ `sky`). Hemi đèn cũ ×0,25–0,35, đèn chính đổi màu và phương theo hồi. Sương nhận màu chân trời khi có trời. Vật dữ liệu (`userData.checks.role` = series/bar) chỉ nhận 0,15 phản xạ môi trường | `env`, `skyI`, `key/keyI/keyEl/keyAz`, `fog` |
| **Vân CC0** | Nhận vật liệu theo **màu** của lib3d/tập (thư viện không đặt tên mesh): đường, tường, mái, gỗ, giấy. **Màu dữ liệu không nằm trong bảng.** Giấy chỉ có normal + roughness, giữ đúng màu | `ROLES` |
| **Bóng mềm** | PCF + đĩa Vogel (`shadow.radius` 6–9), bản đồ 2048, `normalBias` | `shadowRadius` |
| **AO** | GTAOPass (16 mẫu) + khử nhiễu Poisson. SimplexNoise của pass được dựng trong lúc `Math.random` bị thay tạm bằng LCG có hạt → tất định | `ao` |
| **DOF** | BokehPass với **fragment riêng có xét độ sâu**: bỏ mẫu gần máy hơn điểm đang xét > 0,35 m. Bản gốc không xét độ sâu nên tạo quầng sáng quanh người (xem Giới hạn). Tiêu điểm theo người (`focus: 'char'`) hoặc tia giữa khung | `aperture` (cảnh rộng 0,08–0,12, cận 0,9) |
| **Grade + hạt** | Sau OutputPass (ACES + sRGB): lift/gamma/gain, S-curve, bão hoà, viền tối. Hạt tam giác 1 px ở 1080, băm theo (điểm ảnh, khung t) → tất định | `grade` theo hồi |

**Tài sản.** `v4/assets/fetch.py` + `manifest.json`: 3 HDRI và 5 bộ vân, đều 1k và đều ≤ 2 MB nên được commit (RIGHTS §F8). Poly Haven **không có vân giấy**, nên "giấy" dùng thạch cao mịn `beige_wall_001`, chỉ lấy normal + roughness.

## Việc 2a: người bóng ngược sáng
- Giữ nguyên `Person` của lib3d (thân viên nang + đầu cầu, tay viên nang của c4kit). **Không vẽ mặt.**
- Vật liệu thân thay bằng bản sẫm: màu nhận diện × 0,05–0,07. Viền sáng là Fresnel × hướng đèn chính: mạnh ở phía đèn, còn 0,15 ở phía kia. Màu viền pha 25 % màu nhận diện (Tessa và Leo khác nhau rất nhẹ).
- Vật cầm tay (tờ đô la) không bị đổi vật liệu.
- Dáng và cử chỉ: dùng lại `gesture` của tập (giơ tay, nghiêng người, gật). Lớp có móc `posture(state, t)` nhưng **chưa dùng**, nên vòng này chưa thêm dáng cảm xúc mới.
- **Kiểm cận 1080p** (`close-check-1080.png`): khối đọc thành bóng người ngược sáng, viền sáng rõ ở phía đèn. Tuy vậy viền còn chạy gần đều quanh cả khối, nên dễ đọc như "nét viền dán" hơn là ánh đèn thật.

## Việc 2b: chương lịch sử không vẽ người
- **K1** (`v4/hist/k1/scene.js`): ảnh LoC cph.3c17261 (RIGHTS X-RND-1) toàn khung như một bản in.
  - Ảnh chiếm 84 % bề ngang, chỉnh tông (đường cong, hai tông giấy ấm / bóng lạnh cùng bảng màu "dusk"), có hạt tất định, viền giấy mảnh và bóng đổ trên nền tối.
  - Chữ in serif: "NEW YORK · DECEMBER 11, 1930 / Bank of United States / ceases operations" (claim s06, nguồn N3 trong `v2/CLAIMS.md`).
  - Chrome: nguồn ảnh "…, 1931" và nhãn ARCHIVE PHOTO.
  - **Không có bản đồ**: chưa có bản đồ PD/CC0 phù hợp. Bản đồ trong phim Prelinger là bản đồ quảng cáo của công ty tài chính, dùng sẽ gây hiểu sai.
- **K2** (`v4/hist/k2/scene.js`): sổ cái 3D, mỗi ô = 1 tháng trả, mỗi cột = 1 năm.
  - 20 cột đầu có vách gỗ = "1934: up to 20 years" (N7 §203(b)(3)).
  - 10 cột accent = "1954: up to 30 years" (N5). Ngôi nhà nằm ở cuối hàng.
  - Dựng trong thế giới đã lên đèn (hồi "dusk"). Không có người.
- **Phim Prelinger** (`v4/hist/film/film.sh`, RIGHTS X-RND-2): *Financing the American Family* (c. 1935, archive.org `licenseurl` publicdomain). Dùng đoạn 36,0–39,8 s (phố Chicago, vỉa hè đông người).
  - Chuỗi xử lý: vidstab 2 lượt → đường cong + hai tông (cùng bảng K1) → hạt có hạt giống → 4:3 cao 930 px → viền giấy trên nền 1920×1080.
  - **Ổn định gần như không có tác dụng ở đoạn này:** trung vị chuyển động toàn cục của `.trf` là 0 px, vì máy quay gốc vốn đứng yên.
  - Gốc chỉ 640×480, nên ở 1080p hình mềm.
  - Chạy 2 lần trùng SHA-256 (`processed.mp4` `0a125aba…`, nằm trong `work/`, không commit).

## Giờ máy mỗi khung (1080p, SwiftShader 4 lõi, 1 trang)
Đo bằng `v4/light/measure.js`: mỗi cấu hình một trang mới, 1 lần làm nóng + trung vị 3 lần (APP.frame + JPEG q0,95 như `render_shots`). Mọi lần đo chạy **tuần tự, không có tiến trình nào khác song song**. Lần đo đầu bị nhiễu vì chạy chung với lượt dựng thử, nên đã bỏ toàn bộ và đo lại. Số thô: `v4/out/meas/measure.jsonl`; bảng: `v4/out/meas/table.md` (`light/table.py`).

| Cảnh | gốc | chỉ HDRI | chỉ vân | chỉ bóng mềm | chỉ rim | chỉ AO | chỉ DOF | chỉ grade | **đủ lớp** | đủ / gốc |
|---|---|---|---|---|---|---|---|---|---|---|
| Tessa cận | 1,07 | 2,63 | 1,71 | 1,52 | 1,50 | 3,86 | 3,02 | 1,81 | **7,36** | 6,9× |
| Phố / nhà | 0,40 | 1,21 | 0,91 | 0,79 | 0,76 | 2,74 | 2,10 | 1,17 | **5,11** | 12,8× |
| Dữ liệu | 0,80 | 1,98 | 1,35 | 1,28 | 1,24 | 2,85 | 2,72 | 1,61 | **5,80** | 7,3× |
| K2 lưới | 0,46 | 1,45 | | | | 3,60 | 2,44 | | **6,09** | 13,3× |
| K1 tư liệu | 0,36 | | | | | | | | | |

**Chi phí ròng từng lớp** (s/khung). Composer (MSAA 4 + output) = "chỉ rim" − gốc; mỗi lớp = lớp riêng − "chỉ rim":

| Cảnh | composer | HDRI | vân | bóng mềm | **AO** | **DOF** | grade + hạt |
|---|---|---|---|---|---|---|---|
| Tessa cận | +0,43 | +1,13 | +0,22 | +0,02 | **+2,36** | **+1,52** | +0,31 |
| Phố / nhà | +0,36 | +0,45 | +0,15 | +0,03 | **+1,98** | **+1,34** | +0,41 |
| Dữ liệu | +0,44 | +0,75 | +0,11 | +0,05 | **+1,61** | **+1,49** | +0,37 |

**Quy ra phim:**
- Đủ lớp ≈ 5–7,4 s/khung → 150–220 s máy cho mỗi giây phim với 1 worker, hoặc ≈ 40–55 s/s với 4 worker.
- Như vậy một tập 10 phút ≈ **7–9 giờ máy**, so với ≈ 0,5–1,3 giờ khi không có lớp (4 worker).
- Bỏ AO thì đủ lớp còn khoảng 3–5 s/khung.
- Tổng của các lớp riêng không cộng thẳng ra "đủ lớp", vì composer chỉ tính một lần và các pass chia nhau bộ đệm.

**Tất định:**
- Tessa cận đủ lớp, dựng ở hai trang độc lập: PNG trùng MD5 `194d4bec…`.
- `film.sh` chạy 2 lần: trùng SHA-256.

**Chi:** **0 $**. Không gọi API, không TTS, không đọc mù. Tài sản đều CC0 hoặc PD miễn phí.

## Giới hạn trung thực
- **"Phố" vẫn là hai nhà giữa khoảng trống.** Ánh sáng làm khoảng trống thành mặt nhựa đường dưới trời hoàng hôn, nhưng không tạo ra con phố. Đó là việc của dựng cảnh, không phải của ánh sáng.
- **Màu dữ liệu lệch nghĩa ở cảnh c.** Các cột "hi" (pha mực sáng) trong bản gốc tối hơn cột vàng, sau khi lên đèn lại sáng hơn (màu kem). Trước khi chuyển sang nhà máy cần một luật kiểm ΔE/độ sáng tương đối giữa các màu dữ liệu, trước và sau lớp.
- **Viền sáng của người** vẫn hơi giống nét viền. Phía xa đèn còn 0,15, nên nhìn gần thấy viền chạy quanh cả khối.
- **DOF:** còn một vệt sáng mảnh trên đỉnh đầu Tessa. Nguyên nhân là mép MSAA của màu lệch với bộ đệm độ sâu (không MSAA).
- **Cảnh rộng có DOF mạnh** tạo cảm giác **sa bàn đồ chơi** (đã thấy ở lượt thử). Vì vậy cảnh rộng chỉ dùng khẩu nhỏ (0,08–0,12), còn DOF rõ chỉ dành cho cảnh cận.
- **Mái ngói** ở cỡ nhà nhỏ trông như nhiễu đỏ.
- **Đèn chính đổi phương theo hồi**, nên bóng đổ khác bản đã duyệt (vd bóng chồng tiền ở cảnh cận biến mất vì ngược sáng).
- **K1:**
  - Chữ serif vẽ thẳng bằng `O.ctx`, nên **không vào nhật ký chữ của trang kiểm**. Khi chuyển sang nhà máy cần `O.text` có tuỳ chọn font serif.
  - Ảnh LoC có biển chữ nên dễ đọc thành biểu tình (đọc mù vòng 3). Tiêu đề in giúp, nhưng chưa kiểm lại.
- **Phim Prelinger:** độ phân giải thấp; ổn định không có tác dụng đo được ở đoạn này. Muốn biết vidstab có cứu được rung phim hay không thì cần thử một đoạn máy cầm tay.
- **Quy trình:** khi dừng lượt đo bị nhiễu, tôi kill **từng PID**, nhưng danh sách PID lấy bằng `pgrep -f`, nên trúng cả shell của chính lệnh đó (lệnh thoát mã 144). Không có `pkill -f`, và không có tiến trình nào ngoài lượt đo bị dừng. Từ đó chỉ kill PID đã xem trong `ps`.
- Không sửa toolkit/factory, `checks/`, ep008 hay `episodes/ep007`. Không dùng mô hình người tải về, không dùng nhà cung cấp ảnh/video AI, không làm thumbnail, không dùng agent con.

## Sau khi chủ dự án chọn
Theo lệnh vòng 4:
1. Viết `CHARTER-PROPOSAL` cuối.
2. Chuyển việc 1 sang nhà máy dưới dạng **F-17**: khoá `cine` opt-in trong spine.json, như F-14.

Gợi ý, chưa làm:
- AO chạy ở nửa độ phân giải (hoặc chỉ cho cảnh cận).
- Luật kiểm màu dữ liệu trước/sau lớp.
- `O.text` serif cho chữ in.
- Thử vidstab trên một đoạn phim rung thật.
