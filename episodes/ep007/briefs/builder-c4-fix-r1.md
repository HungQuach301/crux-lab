# Đầu bài sửa C4 Tập 7 — vòng bố cục 1 (P3, 11/10): đoạn d (verify CHẶN) + lỗi bố cục a, b. KHÔNG render

Nhánh `ep007`. Làm trong `/home/user/crux-lab`, sửa tệp; **không commit, không push**. Không in, không ghi khoá API.
**Chỉ sửa tệp trong `episodes/ep007/world/c4/{a-s01-s03,b-s04-s09,d-s16-s20}/`** (spine.py, scene.js, spine.json). **Không sửa `world/c4kit.{js,py}`, `world/obj7.js`, `c3kit.*`, `derive.py`, claims** — đoạn c, e, f, g đang render/đã render, đổi kit làm chúng hỏng cache. Nếu một sửa thật sự cần kit → dừng, mô tả, không làm.

## Đã sửa gì, vì sao (PLAN §4)
| Vòng | Cảnh | Lỗi | Sửa | Kết quả đo | Còn |
|---|---|---|---|---|---|
| C3 r3 | S01, S21, S23, S25 | tiết kiệm 3/3, ô trễ sót, teal = "còn nợ", "guaranteed" | bó từ cửa, N1 ink-muted/ink/warn, gom 12 lớp, bóng tách | 5/5 2/2 | hàng chờ C4 |
| C4 l1–l2 | cả tập | hàng chờ C3 §3, S21 đổi loại hình | (`briefs/builder-c4-1.md`, `-2.md`) | a, b, c verify OK; **d verify CHẶN** | vòng này |

## Đọc
`briefs/builder-c4-1.md`, `-2.md` (luật), `world/c4/{a,b,d}-*/`, `world/c4kit.js` (chỉ đọc), `story/beats.md` B01–B09, B16–B20. Khung thật để xem (≤ 10 ảnh tổng): `work/factory/world/a-s01-s03-720.mp4`, `b-s04-s09-720.mp4`, `.staging-d-s16-s20-720-20937/d-s16-s20-720.mp4` (trích bằng `ffmpeg -ss <t> -frames:v 1`); báo cáo verify `…/.staging-d-s16-s20-720-20937/d-s16-s20-720.mp4.verify.json`.

## Sửa
**Đoạn d (S16–S20) — verify CHẶN F-2:** "đường × $14,210 23,6–61,1 s", "đường × $20,374 34,4–61,1 s" (đường lãi 30 năm màu accent chạy xuyên nhãn thập kỷ); WARN "2010s: rate near 4.03% × typical gap…" 29 s, "đường × $21,345" 50,6–61,1 s. Khung 30 s / 45 s (đoạn) quá chật: hàng chồng tuần + đường lãi + 4 chồng thập kỷ + 4 nhãn hai dòng + 4 ngoặc khoảng cách có nhãn chồng nhau, "0.46 point" đè vùng tên "Tessa · ILLUSTRATIVE". Sửa bằng bố cục, không bỏ ý của beats B16–B20:
- đường lãi không đi qua nhãn: đặt dải đường lãi **phía trên** hàng nhãn (hoặc nhãn thập kỷ dưới chân chồng / trong vùng không có đường), hoặc mờ đường lãi xuống khi nhãn thập kỷ hiện nếu B18 đã nói xong ý "lãi giảm";
- hàng chồng tuần mờ hẳn khi 4 chồng thập kỷ đứng (ý S16–S19 là 4 nhóm), để nhãn và ngoặc có nền sạch;
- ngoặc khoảng cách (B19) đặt **cạnh** từng chồng, nhãn "0.46 point"… không đè chồng, nhãn khác hay tên Tessa; nếu thiếu chỗ thì máy lùi hoặc Tessa ra khỏi khung ở đồ thị (tên ẩn theo như lượt 1 đã làm ở S08–S09).
**Đoạn a:**
- S01: nhãn "price of the fallback: $120 a month" đang neo ở cột biển giấy vay (đọc thành giá của khoản vay) — **neo vào chồng/bó** (đặt trên bó, đường dẫn tới bó); "$320,000 loan · week of Oct 8, 2026" neo vào giấy vay, không chồng lên nhãn giá (khung 9,6 s hai nhãn sát nhau).
- S02–S03 chế độ thế giới: hai thẻ "15-year mortgage" / "30-year paid in 15" thành **hộp đen trống** khi chữ tắt (khung 45–53 s) — giữ tên thẻ (không phải số) ở thế giới, hoặc cho thẻ mờ/thu đi cùng lúc chữ tắt; không để khung hộp rỗng.
**Đoạn b:**
- S06 (đồ thị): chân hai thanh khoản trả chạy xuống **dưới dải chân trang** "US only · history, not a forecast" và bị cắt — nâng khung/máy để chân thanh nằm trên dải; thêm tên thanh "15-year" / "30-year" (chữ, không số) ở chân hoặc đỉnh để người tắt tiếng biết thanh nào.
- S05 (≈ 85 s tập): ngoặc V6 `cushion` "fallback: about $613 a month lower" không thấy ở khung giữa cảnh — kiểm thời điểm hiện và để ngoặc đứng đủ lâu (≥ 1 s/3 từ của nhãn).
- S08 (≈ 160 s tập): nhãn "30-year paid in 15: $210,691" nằm trên tháp $477,622 — neo vào **tháp của nó** (tháp thấp).
- S09 (≈ 180 s tập): tháp lãi bị cắt ở mép phải và dưới huy hiệu ILLUSTRATIVE — máy lùi / dời tháp vào vùng an toàn 90 %.
- Đồng bộ (`sync_audit`, C4 l1): `b7.same` +0,26, `b8.over` +0,45, `c5.normal` +0,57, `a3.price` +0,40 → cue hình đúng đầu từ (±0,2 s).

## Kiểm (không render)
`python3 toolkit/tests/comment_guard.py episodes/ep007/world`; mỗi `spine.py` + kiểm quy tắc; `node --import ./episodes/ep007/c4/smoke/register.mjs episodes/ep007/c4/smoke/run.mjs <đoạn>` cho a, b, d (0 chữ giao nhau, 0 chữ ra mép, 0 vi phạm quy tắc 1); tổng timeline không đổi (602,70 s).

## Trả về (≤ 20 dòng)
Mỗi mục đã sửa thế nào; kết quả kiểm khai; rủi ro; lệnh render lại a, b, d.
