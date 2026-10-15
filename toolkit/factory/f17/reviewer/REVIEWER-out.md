# Soát F-17: kết luận của REPORT trung thực, nhưng mã cần sửa một lỗi chính trước khi merge

Bash bị từ chối giữa phiên. Vì vậy tôi chưa chạy `python3` để tính lại SHA-256 các tài sản và chưa xem được `git log -p` của `cine_color.py`. Các phần còn lại đã soát qua `git diff`, Read và Grep.

## 1. Bất biến "không khai `cine` thì trùng byte"
- Không tìm thấy đường nào làm đổi sản phẩm hay báo cáo khi không khai `cine`:
  - `render_shots.js:38`: `CINE` cần đủ bốn điều kiện: spine có `cine`, res ≥ 1080, khung ngang và không có `--spp`. Thiếu một điều kiện thì `view`, danh sách tệp khoá, URL `page.html` và `rep` đều như cũ.
  - `core.js`: `fam(o)` cho ra `Inter` khi không khai serif. Trường `font` chỉ được thêm khi khai serif.
  - `build_seg.py:153`: bước `cine` chỉ chạy khi có khoá `cine`.
  - Trang kiểm `CK.on` mở `page.html`, không bao giờ mở `cine.html`.
  - T1 khớp với `out/T1-T3-md5.txt`: 8/8 tệp trùng MD5. Khoá cache vẫn đổi một lần, REPORT §5.1 đã ghi việc này.
- **PHỤ** `build_seg.py:153`: khi đoạn có `cine`, chạy 1080p với `--spp`, thì `render_shots` tắt lớp nhưng `build_seg` vẫn chạy `cine_check`. Kết quả là luật chấm một lớp không có trong video, tốn giờ máy và có thể CHẶN oan. Điều kiện ở đây cần khớp với `render_shots.js:38`.
- **PHỤ** `build_seg.py:146-147`: nếu `cine_color.py` lỗi trước khi ghi JSON thì `json.load` ném lỗi thay vì báo trượt gọn.
- **PHỤ** `toolkit/blind/headless.sh:12`: `--disallowedTools Task,Agent,Workflow` được thêm cho mọi lượt, không opt-in. Thực tế không đổi hành vi vì `--tools` đã giới hạn ở `Read` hoặc rỗng. Chú thích ở đầu tệp chưa nhắc dòng này.

## 2. Mã `cine.js`
- **CHÍNH** `cine/cine.js:347`: `keyScenePos` được chụp mỗi khung từ `key.position`, nhưng ngay dòng sau, dòng 348, lại ghi đè vị trí đó bằng đèn của lớp cine. Từ khung thứ hai trở đi, `LockPass` vẽ vật dữ liệu và bóng của chúng theo hướng đèn cine chứ không theo đèn gốc.
  - Lỗi bị che nếu cảnh tự đặt lại đèn mỗi khung, như `episodes/ep007/world/c4kit.js:31`.
  - Lỗi lộ ra nếu cảnh dùng `Studio` của `lib3d.js:125`, vốn chỉ đặt đèn một lần, như K2.
  - T4/T5 của K2 chỉ đo một khung, ngay sau `prepare`, nên không thấy lỗi này.
  - Cách sửa: chụp vị trí gốc một lần trong `prep`, hoặc chỉ chụp khi vị trí khác với giá trị lớp vừa ghi.
- **PHỤ** `cine.js:249`: `mapSize` 2048 của bóng mềm không được trả về giá trị gốc trong pass khoá, nên mép bóng trên vật dữ liệu khác bản gốc.
- **PHỤ** `cine.js:62-66`: hạt phim vẫn cộng vào điểm ảnh dữ liệu (sau `mix`), trái với chú thích "không qua grade". Trung bình xấp xỉ 0 nên luật không bắt.
- **PHỤ** `cine.js:209-211`: pass khoá ẩn vật trong suốt và đường/sprite không phải dữ liệu, nên vật dữ liệu sẽ đè lên kính hay đường phủ nằm trước nó.
- Phần đúng:
  - Ảnh lớp không ghi màu và độ sâu của vật dữ liệu nhưng vẫn đổ bóng. Bản đồ bóng không đọc `colorWrite`, và trạng thái được trả lại trong `finally`.
  - `isXRRenderTarget`: trong three r186 cờ này chỉ đổi `toneMapping`, `outputColorSpace`, màu không đèn và định dạng trong (RGBA16F với HalfFloat). Kết quả giống hệt khi vẽ ra canvas, tôi không thấy tác dụng phụ nào khác. Cờ dễ gãy khi nâng three, REPORT §5.8 đã ghi.
  - `baseScene` trả lại đèn, sương, nền, vật liệu và tham số bóng trong `finally`.
  - DofPass: nới độ sâu bằng `min` trên ô 3×3, tức lấy điểm gần nhất, là đúng.
  - AO nửa độ phân giải: `setSize` được bọc để chia đôi, đúng.
  - Viền: hệ số sàn bằng 0 nên phía xa đèn bằng 0 ngay trong shader. Chỉ Person (thân nang và đầu cầu cùng vật liệu) nhận viền.
  - Mái chọn vân hay vật liệu trơn theo cỡ chiếu mỗi khung.
  - Tất định: `Math.random` chỉ dùng trong `seeded`. Hạt phim là băm của điểm ảnh và t. T3 khớp `230c544b…`.

## 3. Luật màu `cine_check.js` và `cine_color.py`
- Công thức CIEDE2000 đúng: hiệu chỉnh G, cách xử lý hue khi C′ = 0, các hệ số T, Δθ, R_C, S_L, S_C, S_H, R_T, và điểm trắng D65.
- **CHÍNH** `cine_color.py:11` và `:7`: vùng chết ORDER_MIN = 1,0 và ORDER_FLIP = 0,5 không có trong INTENT. INTENT T4/T5 ghi tuyệt đối "đảo thứ tự sáng thì CHẶN". Docstring lại ghi "ngưỡng ghi trước trong INTENT", điều này sai. Vùng chết này nới luật, cặp đảo nhỏ không bị chặn. Cần ghi rõ đây là định nghĩa thêm sau INTENT, và đối chiếu commit nào đưa nó vào (tôi chưa kiểm được vì Bash bị chặn).
- Luật thật sự đảm bảo: phần lõi (sau khi co 2 px, nhóm ≥ 200 điểm ảnh) của mesh có role series/bar/grid, đo ở 3 thời điểm mỗi shot, giữ màu trung bình như trang không lớp.
- Luật không đảm bảo:
  - Phần lớn là tự chấm. Pass khoá vẽ lại chính định nghĩa "trước", nên luật chủ yếu kiểm cơ chế khoá có chạy hay không. Điều này vẫn có giá trị: luật đã bắt 4 lỗi thật.
  - Không đo mép, đường (`isLine`), vật mảnh hoặc nhỏ, và vật mờ dần dưới 0,5.
  - Không đo role `mark`. Trong Tập 7 nhiều vật mang dữ liệu khai role này, vì `lib3d.js:199,239` đặt `role: 'mark'` cho vật có `series`. Chúng không được khoá màu và có thể nhận vân nếu màu trùng bảng `ROLES`.
  - Không đo tương phản với nền hay cảm nhận màu, và không đo các khung ngoài mẫu.
- REPORT §5.2–5.4 đã nêu gần đủ các điểm trên.
- **PHỤ** Đối chứng T4 dùng nhánh `v4: true` trong mã F-17, không dùng mã v4 gốc. Cảnh `k2-v4` và `k2` giống nhau, chỉ khác cờ nên hợp lệ, nhưng REPORT nên nói rõ điều này.

## 4. REPORT so với bằng chứng
- **T1–T3, T4, T5**: khớp tệp. Cụ thể:
  - `still-k2-v4` CHẶN với ΔE 13,74.
  - `a.build3` PASS, 24 mẫu, 89 nhóm, ΔE 1,8.
  - c: 2,93 và 2,94. g: 0,20 và 1,81. Ảnh tĩnh ≤ 1,83.
- **T6**: báo TRƯỢT là trung thực. `a.cine.json` có phía xa 0,148 so với phía gần 1,187, tỉ lệ 0,124. Chỉ số "lõi xa đèn" chỉ là chẩn đoán, không dùng để lật kết quả.
  - **PHỤ** Thước dùng "gần đèn" là n·đèn > 0,2 và "xa đèn" là n·đèn ≤ 0. INTENT ghi "nửa khối", tức hai nửa. Dải (0; 0,2] bị bỏ ra, làm tỉ lệ thuận lợi hơn. Kết luận vẫn là TRƯỢT nên không làm sai kết quả, nhưng cần ghi lại đây là thay đổi so với INTENT.
- **T11**: 3262,6 / 563,3 = 5,79×, khớp `T11-T12-build3-cine.build.json`. `T11-render-cine.json` là build 1 (3390,9 s, tức 6,0×), REPORT đã ghi đúng. Đích không bị hạ.
- **T12**: verify của build 3 trùng bản đối chứng (C14 0/1486, 0 cắt cứng, F-2 không có BLOCK). Build 2 có 2 cắt cứng, REPORT đã khai. Trong bản cine, `sky` của đoạn a đổi thành 0: đó là cấu hình lớp, không phải đặc tả cảnh, và đã được khai.
- **T13**: `tally.json` cho thấy bản gốc còn chờ B01, bản có lớp không còn chờ nhịp nào. REPORT chỉ dùng T13 làm chẩn đoán.
- **PHỤ** `REPORT.md:10`: câu "luật màu và verify bắt năm lỗi" nói quá. Lỗi số 3 (chồng tiền nhận viền) được phát hiện bằng phép đo viền hoặc bằng mắt, không phải bằng luật màu hay verify.

## 5. Quyền tài sản, tệp ngoài phạm vi, khoá API
- RIGHTS §F9 có 8 dòng cho 18 tệp (3 HDRI và 5 bộ vân), mỗi dòng có trích giấy phép CC0 nguyên văn và trỏ SHA-256 về `manifest.json`. Cả 18 tệp đều ≤ 2 MB (lớn nhất 1.435.119 B), cờ `commit` đúng với cỡ.
- `fetch.py` kiểm cờ commit theo cỡ và kiểm SHA. **PHỤ**: `urlretrieve` không đặt timeout. Tôi chưa tính lại SHA vì không chạy được lệnh.
- `.gitignore` thêm `cine/assets/dl/` và `f17/work/`, hợp lý.
- Không có tệp nào bị đổi ngoài `toolkit/`, `RIGHTS.md` và `.gitignore`. `ep008`, `episodes/ep007` và `checks/` không bị chạm.
- Không tìm thấy khoá `sk-ant-…` nào trong `toolkit/`. Chỉ có tên biến `$CONSOLE_API_KEY`.

## 6. Kết luận
**ĐẠT có sửa.** Kết luận TRƯỢT của REPORT (T11 và T6) là trung thực. Trước khi merge cần:
1. Sửa `keyScenePos` ở `cine.js:347`.
2. Ghi rõ vùng chết thứ tự sáng là định nghĩa sau INTENT, và sửa docstring `cine_color.py:7`.
3. Ghi rõ thước T6 khác INTENT, và sửa câu "năm lỗi" ở `REPORT.md:10`.