# Đầu bài sửa C4 Tập 7 — vòng 2 (P3, 11/10): S21 lớp trả thêm (CHÍNH, đổi loại hình lần nữa), S24, đoạn f (verify CHẶN). KHÔNG render

Nhánh `ep007`. Làm trong `/home/user/crux-lab`, sửa tệp; **không commit, không push**. Không in, không ghi khoá API.
**Chỉ sửa tệp trong `episodes/ep007/world/c4/{e-s21-s24,f-s25-s28}/`** (spine.py, scene.js, spine.json). **Không sửa `world/c4kit.{js,py}`, `world/obj7.js`, `c3kit.*`, `derive.py`, claims** — đoạn khác đã render, đổi kit làm hỏng cache. Vật dùng lại (vd `Bill` của obj7.js, `TrackC4` của c4kit) thì nhập và dựng thêm trong scene.js của đoạn; cần đổi kit thật sự → dừng, mô tả.

## Đã sửa gì, vì sao (PLAN §4)
| Vòng | Cảnh | Lỗi | Sửa | Kết quả đo | Còn |
|---|---|---|---|---|---|
| C3 r3 | S21 | lớp trả thêm `ink` trên ô `ink-muted`: 2/2 người đọc "all blocks white" | lớp phủ 72 % mặt ô | đạo diễn r1+r3 lặp: không thấy lớp | CHÍNH (C3 câu 1) |
| C4 l2 | S21 | (đổi loại hình 1) tấm dày phát sáng rơi vào từng cột, ô bắt buộc tối hẳn | | **thử nhanh tắt tiếng 2/2: "the tiles turn white"**, khung cuối = lưới trắng đều | vòng này |
| C4 r1 | a, b, d | bố cục (F-2, cắt mép, nhãn neo sai) | `briefs/builder-c4-fix-r1.md` | chưa render | — |

## Sửa
1. **S21 — lớp trả thêm phải thấy BẰNG HÌNH (lỗi CHÍNH, C3-answer câu 1; lessons T6-7: vòng trước trượt cùng câu trả lời → đổi loại hình).** Câu người đọc tắt tiếng phải tả được: *"each month gets an extra bill/payment placed on top, and the track then ends exactly at the 15-year mark"*. Cách đề xuất (bên dựng chọn chi tiết, giữ ý):
   - phần trả thêm của mỗi tháng = **một tờ đô la** (`Bill` của obj7.js — vật tiền đã dùng ở S25, người xem nhận ra là tiền), **nhỏ hơn ô** (≈ 55–65 % cạnh ô), **đặt lên mặt ô**; ô bắt buộc giữ màu tối `ink-muted` và **vẫn thấy quanh tờ tiền** ở mọi khung — tuyệt đối không phủ kín ô, không đổi màu cả ô;
   - tờ tiền **đến từ tay/cửa nhà Tessa** (đi một đường ngắn tới cột đầu) rồi rải vào từng cột-năm theo nhịp (mỗi cột một nốt, như lượt 2), không "rơi từ trời"; giữ thứ tự nhân quả đã làm (ô trễ hiện sau khi cột tới vách; ô trễ rút về khi tiền tới, tắt hẳn trước nhãn);
   - khung cuối S21 (và đuôi): lưới **hai màu rõ** — ô tối + tờ tiền sáng trên mỗi ô; máy 3/4 thấy độ nổi của tờ tiền;
   - nhãn giữ "to finish in 180 months: / about $733 extra on top of the $2,216 required"; "about 15 months late" giữ.
   - S23 bắt đầu từ trạng thái cuối S21: **12 tờ tiền của mỗi năm** trượt về ô thứ 12 thành **một xấp** (khối năm = xấp 12 tờ, khe đếm được) — thay khối tấm trắng hiện tại, cùng ý đã có. Lưới không đổi màu không lý do.
2. **S24:** khay "tài khoản" (đường nét đứt, ≈ khung tập 441 s) **đè lên tên "Tessa · ILLUSTRATIVE"** — dời khay ra chỗ trống (không đè chữ, không đè vật), giữ ý "12 tờ chờ trong tài khoản" + "what it earns there: not counted".
3. **Đoạn f — verify CHẶN F-2:** "đường × the bar: 7.40% a year, before taxes" 19,1–26,4 s (8 mẫu); WARN "đường × any other use" 21,2–26,7 s. Sửa bố cục để không đường nào cắt nhãn. **Đồng thời bỏ đường nét đứt nối đầu thanh với bóng "any other use"** (khung 22–26 s: nét đứt nằm ngang đúng độ cao thanh → mời đọc "so ngang mốc / phải vượt", trái C3 câu 5): bóng đứng tách, lên xuống liên tục qua cả trên lẫn dưới độ cao thanh, không có vạch so ngang; nhãn "any other use" đi theo bóng; khung cuối/đuôi bóng đang chuyển động, không ở ngang thanh. Thước khắc sàn → thanh giữ.

## Kiểm (không render)
`python3 toolkit/tests/comment_guard.py episodes/ep007/world`; `spine.py` + kiểm quy tắc của e, f; `node --import ./episodes/ep007/c4/smoke/register.mjs episodes/ep007/c4/smoke/run.mjs <đoạn>` cho e, f (0 chữ giao nhau/đường cắt chữ, 0 ra mép, 0 vi phạm quy tắc 1); tổng timeline không đổi (602,70 s). Có thể trích ≤ 6 khung từ `work/factory/world/e-s21-s24-720.mp4` (bản lượt 2) để xem trước khi sửa.

## Trả về (≤ 20 dòng)
Mỗi mục đã sửa thế nào (S21: một câu mô tả hình mới cho ý đồ kiểm mù); kết quả kiểm khai; rủi ro.
