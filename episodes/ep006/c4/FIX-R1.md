# C4 vòng sửa 1 (P3b, 09/10) — danh sách việc (chỉ lỗi khách quan + nhận xét lặp ở cả hai lượt đạo diễn + nghĩa 0,5 của cổng gốc)

Nguồn: `gates/C4-director-A.md`, `gates/C4-director-B.md` (giờ = giờ của tập; đoạn bắt đầu ở: a 0 · b 51,23 · c 149,67 · d 208,93 · e 329,43 · f 455,27 — đọc `out/timeline.json` để đổi sang giờ đoạn), `gates/C4-root.md` (cổng gốc tắt tiếng), dải `review-c4/strips/<Bxx>.png`, animatic `out/video.mp4` (720p @ 0af1076).

## Đã sửa gì, vì sao (vòng trước)
| Vòng | Đoạn | Lỗi | Sửa | Kết quả |
|---|---|---|---|---|
| C4 lượt 1 | c | F-2 nhãn trục × nhãn | nhãn trục xuống hàng dưới khi lùi máy | 104 → 0 |
| C4 lượt 1 | f | F-2 đường × "42.4%" | số vào trong thanh; lùi máy thang; thẻ V7 nới | 177 → 0 |
| C4 lượt 2 | c, f | quy tắc 7 (5 s đầu mỗi đoạn ở thế giới) | c mở ở thế giới (Ruth, séc, hàng thùng); f dời chuyển chế độ | verify OK |
| F-13 | nhà máy | mux `-shortest` rơi khung | bỏ `-shortest` (một dòng, ep006) | splice OK, 536,6 s |

## Luật vòng này
- **Không đổi lời, không đổi mốc spine/độ dài đoạn, tổng 536,6 s giữ nguyên** (trần 9:00). Không thêm chữ (bài học Tập 4: hình nghèo, nhiều chữ — ưu tiên bớt chữ, làm hình mang nghĩa). Số và nhãn so sánh chỉ ở đồ thị chính diện (quy tắc 1).
- **Mép an toàn:** mọi chữ và vật mang nghĩa nằm trong [96, 1824] × [vùng trên dải nhãn góc, trên dải chân trang] ở toạ độ 1920×1080; không vật 3D nào đè dải chân trang "US only · history, not a forecast" hay nhãn góc. C14 chỉ đo ở 1080p → tự kiểm bằng phát lại `frame()` + bề rộng chữ thật (cách của vòng c/f: `label_check` trong `toolkit/factory/world/sfx_labels.py`) và hộp chiếu của vật 3D.
- **Nhãn ≥ 1 s mỗi 3 từ** (làm tròn lên).
- Số hiện **đúng lúc lời nói số** (± 0,3 s), không trễ 2,5–5 s.
- Không sửa `c4kit.js`/`c4kit.py` (dùng chung); cần thì báo phiên chính. Không render, không build, không git commit.
- Kiểm: `python3 toolkit/tests/comment_guard.py episodes/ep006/world`, `spine.py` của đoạn → "checks OK", phát lại F-2 = 0, `python3 episodes/ep006/c4/build_inputs.py --timeline` → 536,6 s.

## Việc theo đoạn
**a (S01–S03 + ident):** khung đen 49,5–51,2 (ident: hình nhạc hiệu phải thấy — thế giới tối dần chứ không đen kịt; ít nhất cảnh/dấu kênh mờ); nhãn Ruth cắt mép trái 34,5–35; S03 gần trống 28–35 (cả hai lượt). **Nghĩa B01** (0,5/0,5: "9 lit and growing card unclear" — thẻ séc lớn lên phải thấy rõ lớn dần, đếm 9 sáng rõ ở khung cuối). **Nghĩa B03** (0,5/0,5: người đọc thấy đường Ruth kết thúc "well below", ý đúng là **chỉ hơi dưới** 100 % — 90,4 %: thang trục/đường phải cho thấy sát vạch).
**b (S04–S08):** cắt mép trái 61–77,5 ("level check: never changes", hàng thẻ đều), chữ đè đầu Ruth 68–69; "check · first price" cắt mép trái 93–116,5; "(90.4%)" cắt mép phải 129,5–131 và nhãn 8 từ chỉ ~2,5 s; "level check today…" cắt mép trái 135,5–149,5; S06 hai cột đứng yên ~25 s (cả hai lượt) — thêm chuyển động mang nghĩa (cột giá dâng theo năm, máy đứng ở từ khoá).
**c (S09–S12):** hàng thùng đè dải chân trang 155,5–185; nhãn giá trị nằm trên đường 163,5–185; "rising check: there after 20 years" chồng "first check" 199–208,5; "first check" ngoài mép phải ở tư thế cNear0 (vòng trước ghi lại).
**d (S13–S23):** "80.7"/"54.3" cắt mép phải 267,5–298; dải thùng đè "first check" 290,5–297,5; ba dòng nhãn trên cột 300–305 (S19); nhãn CPI-U/CPI-W/PCE trên đồ thị chồng 312,5–323 (S21–S22); số trễ 2,5–5 s ở 259,6–280,5; lưới đứng yên ~24 s S13 và ~40 s S16–S17 / ~80 s một đồ thị phẳng 217–298 (cả hai lượt) — thêm động tác/biến đổi mang nghĩa theo lời. **Nghĩa B15** (0,5/0,5: "meaning of 'kept up' missed" — cụm ô xanh 1947–1949 phải đọc ra là "giữ được sức mua", phần còn lại tới ô Ruth là không).
**e (S24–S29):** hàng thùng sót lại cắt mép trái 339,5–386; thanh xanh lớn không nhãn 341,5–367; nhãn ô nhỏ Ruth/Carl đè thanh xanh 357,5–367 (sáu dòng chữ một lúc); Edna: người/thùng cắt mép phải 386,5–404 và 420,5–432,5 (thẻ và hàng thùng không hiện 394–404); khung gần trống 334, 386; số trễ 362,9–382,5. **S29 không đổi ý hình** (ngoại lệ C3, chỉ sửa mép/khung nếu có).
**f (S30–S32):** thang 3D không nhãn và cắt mép phải 455,5–461; thùng/cột cắt mép trái lúc chuyển 486, 500, 517; thẻ 3D lộ dưới thẻ V7 510,5–516; số trễ 458 → 462,5; outro đứng yên ~11 s không cue 518–529 (cả hai lượt). **Nghĩa B32** (0,5/0,5: người đọc thấy khoản **đều** — thẻ séc của Ruth phải đọc ra là khoản **tăng** +2 %/năm, như khung mở đầu).

## Trả về (≤ 12 dòng)
Mỗi việc: đã sửa / không sửa (lý do); file đổi; số đo phát lại (F-2, mép, thời lượng nhãn); 536,6 s giữ nguyên.
