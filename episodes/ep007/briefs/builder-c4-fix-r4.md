# Đầu bài sửa C4 Tập 7 — vòng 4 (P3, 12/10): khoá nghĩa S21 (về bản vòng 2) + B31. KHÔNG render

Nhánh `ep007`. Làm trong `/home/user/crux-lab`, sửa tệp; **không commit, không push**. Không in, không ghi khoá API.
**Chỉ sửa tệp trong `episodes/ep007/world/c4/{e-s21-s24,g-s29-s33}/`**. Không sửa kit, obj7, claims. Lệnh kiểm: lệnh đơn, không `cd … &&`.

## Đã sửa gì, vì sao (PLAN §4)
| Vòng | Cảnh | Lỗi | Sửa | Kết quả đo (cổng gốc tắt tiếng) | Còn |
|---|---|---|---|---|---|
| C4 v2 (`0c07423`) | S21 | lớp trả thêm không thấy | tờ đô la 62 % ô trên mỗi ô | B21 nghĩa **1 · 1**, extra 0/2 | |
| C4 v3 (`d90f411`) | S21 | — | cận cảnh một ô nhận tờ tiền | B21 nghĩa **0,5 · 0,5**, extra 0/2 → **thấp hơn v2 → tự loại (khoá nghĩa, lessons V2)** | về v2 |
| C4 v3 | S23 | khối năm không đọc ra | xấp năm hạ ô 12/24/36… | B23 1/3 (r1 0/2) → giữ v3 | — |
| C4 r1 | S31 | | | B31 1 · 0,5 · 0 → TRƯỢT ("empty third slot not noticed") | vòng này |

## Sửa
1. **S21 về đúng hình của vòng 2** (`git show 0c07423:episodes/ep007/world/c4/e-s21-s24/scene.js` và `spine.py`): bỏ cận cảnh một ô + động tác máy vào/ra của nó, giữ tờ đô la trên mỗi ô như v2, giữ nhãn và nhân quả như v2. **Giữ nguyên mọi thay đổi vòng 3 của S22–S24** (xấp năm hạ ô 12/24/36…, ô giữa mờ, máy đẩy vào vách, Tessa giơ tay, không đổi góc giữa câu). Đồng thời giữ sửa vòng 3 không thuộc cận cảnh nếu không đụng S21 hình (nhãn "about 15 months late" trên nền tối, tên Tessa không chạm lưới). Ghi rõ đã lấy gì từ v2, gì từ v3.
2. **S31 (B31 "an empty third slot beside the two houses with a blank beam and a blank stack, labelled with where each comes from"):** người đọc không thấy ô thứ ba. Làm **ô thứ ba thấy rõ bằng hình**: nền/đế có viền sáng nét đứt cùng cỡ lô nhà, một thanh trống và một chồng trống (viền, không đặc) đứng trong ô đó, hiện lên có nốt và máy hướng vào nó khi lời nói "Any fixed-rate borrower" (S31.1); hai nhãn "your bar = …" / "your stack = …" có dây dẫn chỉ đúng vào thanh trống / chồng trống. Không thêm số.
3. Tổng timeline 602,70 s không đổi; mọi cue ±0,2 s.

## Kiểm (bắt buộc)
`python3 toolkit/tests/comment_guard.py episodes/ep007/world`; `python3 episodes/ep007/world/c4/e-s21-s24/spine.py`; `python3 episodes/ep007/world/c4/g-s29-s33/spine.py`; smoke e, g (`node --import ./episodes/ep007/c4/smoke/register.mjs episodes/ep007/c4/smoke/run.mjs <đoạn>`): 0 lỗi, 0 chồng chữ, 0 ra mép, 0 quy tắc 1.

## Trả về (≤ 15 dòng)
Đã làm gì; kết quả kiểm; rủi ro.
