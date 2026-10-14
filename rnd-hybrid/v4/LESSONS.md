# Bài học R&D rnd-hybrid (vòng 1–4, đóng 14/10/2026)

## L1. Bốn vòng nhân vật hỏng cùng một kiểu
| Vòng | Hướng | Chủ dự án nhận xét / kết cục |
|---|---|---|
| 1–2 | Người giấy cắt trong 3D (v1, v2) | "Phẳng nên nhàm" |
| 3 bước 1–2 | Kenney chibi (H4) → Quaternius (H4′) | Bác: thân ma-nơ-canh trần, quần áo sơn lên, mặt ma-nơ-canh, mũ xuyên đầu |
| 3 (khung) | P1 giấy 5 lớp · P2 tượng sa bàn · P3 tranh in báo 2.5D | Chọn P3 |
| 4 (mở đầu) | P3 | Bác: "phẳng" |

**Kiểu hỏng chung:** mỗi vòng đổi **cách vẽ người**, nhưng mọi vòng đặt người vào **cùng một thế giới phẳng**. Kết quả lần nào cũng bị đọc là "phẳng" hoặc "đồ chơi", dù người được vẽ bằng giấy, khối, mô hình tải về hay nét khắc.

Đây là lỗi chẩn đoán: phiên coi nhân vật là biến số, trong khi biến số thật nằm ở chỗ khác (L2). Mỗi vòng tốn một lượt chọn phong cách của chủ dự án mà không tiến gần nguyên nhân.

## L2. Nguyên nhân thật: thế giới thiếu ánh sáng và vật liệu
- `render_shots.js` và `core.Stage` chỉ có đèn studio (hemi + một đèn chính + rim), nền phẳng màu `#0E1116`, vật liệu một màu không vân, không AO, không DOF, không môi trường và không chỉnh màu. Bất kỳ người nào đặt vào đó cũng phẳng.
- Bằng chứng (vòng 4): **cùng mã cảnh Tập 7**, chỉ bọc thêm lớp `cine`, khung đã có chiều sâu, không khí và vật liệu (`v4/out/SHEET-before-after.jpg`).
- Bài học: khi hình "phẳng", kiểm **ánh sáng, vật liệu, hậu kỳ** trước, rồi mới đổi phong cách nhân vật. Đo một khung trước/sau với cùng cảnh rẻ hơn nhiều so với một vòng phong cách mới.

## L3. Luật: khung cận 1080p cho chủ dự án xem trước khi chạy tiếp
- Trước khi dựng clip, chạy đọc mù hay đo hàng loạt cho một hướng hình mới, phải gửi chủ dự án **một khung cận người ở 1080p**. Nếu có, gửi kèm một khung dữ liệu và bản trước/sau. **Dừng chờ duyệt.**
- Lý do: H4′ chỉ bị bác sau khi đã dựng 8/19 cảnh. Lỗi (ma-nơ-canh, mũ xuyên đầu) thấy được ngay ở một khung cận 1080p. Tờ 540p hay khung rộng che lỗi ở người.
- Áp cả với khung ở cỡ nhỏ: soi bằng ảnh cắt phóng ×2 không làm mượt (như `v4/out/stills/close-check-1080.png`). Quầng DOF quanh người ở vòng 4 chỉ thấy được ở cỡ này.

## L4. Luật: không dùng `pgrep -f` để lấy PID khi dừng tiến trình
- Hai lần trong R&D:
  - Vòng 3: vòng chờ `until ! pgrep -f "v3/clip3/build.py"` không bao giờ thoát, vì nó tự khớp với dòng lệnh của chính mình. Hệ thống dừng nó khi hết giờ.
  - Vòng 4: `for p in $(pgrep -f "…measure.js"); do kill $p; done` kill trúng cả shell của chính lệnh đó (mã 144).
- Luật:
  - lấy PID từ `$!` lúc khởi chạy, hoặc từ `ps -eo pid,ppid,cmd` đã **xem bằng mắt**;
  - kill từng PID đã xác định;
  - không dùng `pgrep -f` hay `pkill -f` để chọn tiến trình cần dừng;
  - muốn chờ một tiến trình thì chạy nền và chờ thông báo, hoặc chờ một tệp kết quả.

## L5. Bài học kỹ thuật kèm theo
- **Đo giờ máy chỉ khi không có gì chạy song song.** Lượt đo 1080p đầu của vòng 4 trùng với lượt dựng thử, nên số bị nhiễu và đã bỏ cả lượt.
- **Hậu kỳ có thể đổi nghĩa dữ liệu.** Ánh sáng môi trường làm cột "tối = chưa tới" thành sáng hơn cột vàng. Mọi lớp hình mới phải có luật kiểm thứ tự độ sáng giữa các màu dữ liệu.
- **DOF mạnh ở cảnh rộng = sa bàn đồ chơi**: chính cảm giác chủ dự án muốn tránh.
- **Chú thích chèn giữa dòng nuốt mã:** lặp lại ở vòng 3 (h3, p3). Chỉ chú thích ở cuối dòng; chạy `node --check` và `lint_comments.py` trước khi dựng.
- **Three.js gán `render` trong hàm dựng**, nên vá prototype không bắt được. Cách bọc không sửa mã cũ là accessor trên prototype (`v4/light/cine.js`). Phải kiểm lại khi nâng three.
