# Duyệt đạo diễn: E5d, ep005, cold open 34 s (bản xem trước 540p)

Nguồn đã xem: sheet-1/2 (khung cách 0,5 s), audio.png, transcript.txt, events.txt, intent.txt. Quy ước: sự kiện thấy lần đầu ở khung t thì xảy ra trong khoảng (t−0,5; t]. Chuẩn lệch cho phép là ±0,2 s so với onset trên waveform.

## 1. Lệch hình / lời / âm; chỗ hình khác ý đồ

| # | Mốc | Lời (onset) | Hình thấy được | Âm | Sai số / nhận định |
|---|---|---|---|---|---|
| 1 | c0 | "saved" 0,707 / "ten" 1,13 | Chồng teal của người xem chưa có ở 0,5, đã có ở 1,0 (đã nằm yên) | tick 1,13 | Hình đặt xuống trong (0,5; 1,0], nghĩa là sớm hơn tick 0,13–0,63 s. Nếu mục tiêu là "ten" thì có thể vượt ±0,2. Cần đo pixel lại; hình phải *chạm đất đúng* tick. |
| 2 | c1 | "insurance" 5,656 | Khiên vàng trên mái + nhãn "buy now + mortgage insurance" ở 5,5 | land 5,66 | Hình nằm trong (5,0; 5,5], sớm hơn land 0,16–0,66 s. Ở 5,5 khiên đã gần chạm mái nên chắc nằm trong biên, nhưng chưa khẳng định được. |
| 3 | c1 | "renting" 7,26 | Nhãn "keep renting, keep saving" mờ ở 7,0, rõ ở 7,5 | — | Bắt đầu fade trước lời (≤7,0, tức sớm ≥0,26 s). Nhãn tên, chấp nhận được, nhưng nên bắt đầu đúng 7,26. |
| 4 | c1 | "twenty" 8,457 | Vạch vàng (mốc 20 %) đã có ở 7,5; chồng lớn lên thấy ở 8,5 | rise 8,46 | Chồng lớn khớp. Vạch 20 % hiện cùng nhãn "renting", sớm khoảng 1 s so với "twenty". |
| 5 | c2 | "eight" 13,753 | **Đường lịch trả nợ đã chạm vạch 80 % ở năm 8 trong khung 13,5**. Nhãn "about 8 years" (có glow) thấy ở 14,0 | chime 13,75 | Nhãn khớp. Nhưng cú *chạm vạch*, tức sự kiện dữ liệu chính, xảy ra ≤13,5, **sớm ít nhất 0,25 s** (khung 13,0 đường mới tới khoảng năm 6,5). Vượt chuẩn. Đường phải chạm đúng 13,75 cùng chime. |
| 6 | c3 | "replayed" 15,697 | Tiêu đề/footer đổi ở 15,5 (đang chuyển). Bó đường bắt đầu thấy ở 16,0 | ticks mềm | Khớp (trong (15,5; 16,0]). |
| 7 | c3 | "typically" 21,508 | Đường điển hình sáng + nhãn "typical" ở 21,5 | nốt sáng | Khớp. |
| 8 | c3 | "slow" 22,344 | Đường vàng "slow cases" ở 22,5 | nốt trầm | Khớp. |
| 9 | c4 | "eighty" 26,046 | Chồng vay 88 % → 85 % → 82 % → "80% on paper" ở 26,0 | chime 26,05 | Khớp (giới hạn khung). |
| 10 | c4 | "value" 27,187 / "index" 28,72 | **Không có sự kiện hình nào** 26,0–29,0 | — | Hai cue trong intent không có hình đi kèm. Nhãn "home value by a national price index" đã nằm sẵn từ 23,5. |
| 11 | c5 | "removed" 31,82 | "insurance still on" thấy ở 32,0. Không thấy khiên rung (khung 0,5 s không bắt được) | thud 31,82 | Khớp. |

**Hình khác ý đồ:**
- c0: intent ghi "chồng tiền MỜ = giá nhà". Thực tế là cột đặc, xám nhạt, cao gấp khoảng 1,5 lần căn nhà, trông như "nhà trên cột ống khói" chứ không đọc ra là "giá". Chồng của người xem nằm **dẹt ngang** dưới đất nên mắt không so được với đoạn teal 10 % ở chân cột (một bên đo theo chiều cao, một bên theo chiều ngang).
- c1: "chồng của người xem lớn dần tới vạch 20 %" lại diễn ra **ở chân căn nhà**, không ở phía căn hộ. Về không gian, lối "thuê tiếp" không có vật thể nào của mình: căn hộ đứng trơ.
- c4: "GIÁ TRỊ nhà lớn theo chỉ số". Chồng xanh gần như không đổi chiều cao, còn chồng vay co lại rất ít. Ý chỉ đọc được qua con số %, 3D không làm ra nghĩa.
- c5: chồng vay xám cao khoảng 68 % cột giá (đo trên khung 32,0), không khớp mốc nào đã nói (80 %). Chồng teal tiết kiệm **vẫn lớn thêm** cạnh người xem dù câu chuyện đang ở lối "đã mua". Hai lối bị trộn vào một cảnh.
- c5 (WORLD): Source, badge "ILLUSTRATIVE" và footer hai dòng **vẫn nằm trên màn hình** 29,5–33,5. Vi phạm quy tắc "chữ/số chỉ ở CHART".
- Badge **"ILLUSTRATIVE"** nằm trên biểu đồ mà lời nói "We replayed real U.S. prices". Mâu thuẫn trực tiếp về độ tin cậy.

## 2. Chuyển cảnh và chuyển chế độ

| Mốc | Loại | Lý do | Đánh giá |
|---|---|---|---|
| 2,175–3,175 | pull wYou→wFork | cần thấy hai lối | Lý do đúng, nhưng máy lùi **trước** câu hỏi (câu hỏi bắt đầu 4,10), trong lúc đang nói "home's price". Sau đó 3,2–5,5 khung đứng yên với hai lối chưa có nghĩa. Liền mạch nhưng **lệch nhịp**: lùi trúng chữ "price" làm mất điểm nhấn của câu móc. |
| 9,0–10,1 | mode wFork→cSched | lịch trả nợ = đường theo thời gian | Liền mạch về chuyển động (9,5: căn hộ trượt trái, vạch 80 % dạng thanh 3D vào từ phải). Nhưng sang CHART thì nhà, khiên, người đều rời khung, và đồ thị trôi trong khoảng đen trống. Không có vật nào **mang** từ thế giới sang (chồng teal 10 % lẽ ra phải thành điểm 90 % của đường). **Gãy về nghĩa**, không gãy về hình. |
| 15,5 | đổi nội dung CHART tại chỗ | — | Cross-fade tiêu đề và footer, đường lịch + "about 8 years" giữ lại làm mốc so sánh. Ý tốt nhưng gây chồng chữ (xem mục 4). |
| 23,137–24,137 | pan cSched→cDef | định nghĩa cần hai chồng | Lý do đúng. Nhưng đường "slow cases" chỉ sống khoảng 0,6 s (22,5→23,1) rồi bị lia đi: **cắt mất điểm nhấn** vừa dựng. |
| 29,142–30,042 | mode cDef→wHouse | bảo hiểm gắn với nhà | Chồng vay xám đi theo sang thế giới, liền mạch. Chồng **xanh "home value"** biến thành cột giá xám/teal: mã màu **GÃY** (giá trị = xanh ở CHART, giá = xám ở WORLD, teal = tiền tiết kiệm). Land 30,04 đè lên "That's" 30,00. |

## 3. Nhịp

- **5 s đầu: móc yếu.** 0–3 s chỉ có một hình nhân đứng cạnh một tòa tháp, không có căng thẳng, không có câu hỏi bằng hình. Thứ duy nhất chuyển động là chồng dẹt đặt xuống. Nhạc ở mức khoảng −50 dBFS, gần như không nghe. Khiên (thứ đầu tiên có nghĩa "chi phí") tới 5,5 s, đã quá cửa sổ móc. So với Vox (vào bằng mâu thuẫn trong 2–3 s): chưa đạt.
- **Chùng:** 3,2–5,5 (khung tĩnh 2,3 s sau cú lùi); 14,0–15,5 (đồ thị đứng, đúng pause 14,48–15,54, chấp nhận được); 19,5–21,4 (bó đường đã vẽ xong, không có gì mới cho tới "typically"); **26,0–29,1** ("80% on paper" đứng 3 s, "value"/"index" không có hình).
- **Dồn/rối:** 16–23 s. Bó 307 đường + đường lịch cũ + "about 8 years" + "typical" + "slow cases" + tiêu đề + source + badge + footer hai dòng trong một khung 540p. Thời gian để đọc "slow cases" quá ngắn trước khi lia.
- Điểm hay: "typical" chạm 80 % sau khoảng 1,5–2 năm, ngay cạnh đường lịch 8 năm. Đây là phát hiện mạnh nhất của đoạn, nhưng **không được đánh dấu** (không có khoảng cách/mũi tên), nên người xem phải tự suy ra.

## 4. Lớp bắt buộc (source, badge, disclaimer); đọc trên điện thoại

- Các lớp này không đè lên dữ liệu chính, nhưng chiếm khoảng 25 % chiều cao khung (dòng source trên, hai dòng footer dưới) và **lọt sang WORLD** ở c5.
- Cỡ chữ: tiêu đề đồ thị, nhãn trục (0/2/4…, 90 %/80 %), footer ước khoảng 10–12 px trên khung 540p. Trên điện thoại cầm dọc xem video ngang thì **không đọc được**. "about 8 years", "typical", "80% on paper" là đọc được tối thiểu.
- Chồng chữ: "about 8 years" ngồi sát/đè vạch 80 % và lấn hàng nhãn trục "6 · 8" (khung 14,0–23,0). "typical" đè nhãn trục "2" (21,5–23,0). Nhãn "slow cases" bị đỉnh bó đường (>100 %) chạm sát tiêu đề (22,5–23,0).
- Cắt mép: 29,5 nhà bị cắt mép trái khi máy đang chạy (khung chuyển tiếp, chấp nhận). 23,5 nhà nhỏ và chồng xanh sát mép phải. Không thấy chữ bị cắt.
- Badge "ILLUSTRATIVE" màu vàng cùng tông với "slow cases" và khiên, nên tranh mắt với dữ liệu.

## 5. Âm

- **Lời:** rõ. Voice đỉnh khoảng −10 dBFS, nhạc khoảng −40…−30, cách 15–25 dB. Không thấy chỗ nhạc hay data che lời.
- **Nhạc theo căng–chùng:** đường tension (0,15→0,8 ở 15,6→0,1) được tôn trọng về mức, nhưng 0–4 s quá nhỏ cho một cold open. Đỉnh 0,8 rơi vào đoạn bó đường, đúng chỗ. Hai accent 13,75/26,05 trùng chime, tốt.
- **Kết thúc:** voice hết 32,24, nhạc nhả dần tới khoảng −55 ở 34 s. Không có điểm khép (button/cadence), đoạn kết **trôi** chứ không đóng. Thud 31,82 đúng "removed" nhưng mức thấp (khoảng −38), nên "chưa gỡ được" thiếu lực.
- **Âm dữ liệu:** 11 nốt 10,6–22,3. Ở c2 mỗi năm một nốt thì hợp lý. Nhưng 307 đường chỉ có vài tick, khó nghe thành "nhiều tháng". "Nốt sáng/nốt trầm" cho typical/slow có trên waveform (khoảng 21,5–22,3) nhưng ngắn, rồi bị whoosh_push 23,14 nuốt.
- **Hiệu ứng thừa/đè:** whoosh_soft 2,17 nằm dưới "home's price". whoosh_mode 9,0 đè đuôi "percent?" (8,88–9,2). land 30,04 đè "That's". Bốn whoosh + ba land/chime trong 34 s thì hơi dày, trong đó **land 10,1** không có hình "chạm" nào tương ứng.

## 6. 3D: làm ý rõ hơn hay chỉ trang trí

- Phần làm nghĩa: khiên đặt lên mái (chi phí bảo hiểm gắn với căn nhà). Khiên vẫn trên mái ở c5 ("still on"). Chồng vay xám theo sang WORLD.
- Phần chủ yếu trang trí: cột giá cao nhìn như kiến trúc chứ không như tiền. Căn hộ không bao giờ làm gì. Hình nhân "You" không có hành động (không cầm, không bước). Hai chồng ở c4 gần như tĩnh, con số làm hết việc.
- **Tỉ lệ 10 % so với giá:** đoạn teal ở chân cột trông khoảng 8–10 % chiều cao cột, đạt. Nhưng chồng riêng của người xem nằm dẹt nên không so được với 10 %. Vạch 20 % là một thanh ngang vàng, không đọc ra là "gấp đôi".
- **90 % → 80 %:** trục dọc chỉ 80–100 % (không có 0). Hợp lệ cho đường tỉ lệ, nhưng dốc 90→80 trông thoai thoải trong khoảng ~40 px nên cảm giác "chậm 8 năm" có. Ở c4, 88 %→80 % làm chồng vay co khoảng 9 %, gần như không nhận thấy. Chồng vay cuối ở c5 cao khoảng 68 % cột giá, **không khớp 80 %**.

## 7. Chấm điểm (so với Vox / 3Blue1Brown / WSJ)

| Tiêu chí | Điểm | Lý do ngắn |
|---|---|---|
| Hình mang nghĩa | **3** | Bó đường + typical/slow là dữ liệu thật, đắt. Khiên mang nghĩa. Nhưng 3D phần lớn là đạo cụ, mã màu gãy, tỉ lệ c5 sai, badge ILLUSTRATIVE mâu thuẫn lời. |
| Liền mạch hình–lời–âm | **3** | Khoảng 9/11 cue khớp. Cú chạm 80 % ở c2 sớm ≥0,25 s. "value/index" không hình. Chữ chart lọt sang WORLD. Ba SFX đè lời. |
| Nhịp | **2** | Không móc trong 5 s. Ba quãng chùng 2–3 s. 16–23 s rối rồi bị cắt ngay sau điểm nhấn. |
| Âm | **3** | Lời sạch, mix an toàn. Mở đầu nhạc quá nhỏ, kết không khép, sonification mỏng, whoosh dày. |

### Năm sửa quan trọng nhất

1. **0,0–4,1 (móc):** dựng mâu thuẫn ngay. Chồng teal của người xem đứng **dọc** cạnh đoạn teal 10 % ở chân cột giá, cột 90 % xám còn lại "lơ lửng". Tick khi chồng chạm đất đúng "ten" 1,13. Dời cú pull sang 3,2–4,0 (pause), và nâng nhạc lên tension ≥0,4 từ 0 s.
2. **13,0–13,75:** giãn tốc độ vẽ đường lịch để nó **chạm vạch 80 % đúng 13,75** cùng chime (hiện chạm ≤13,5). Dời "about 8 years" lên trên vạch, tránh hàng nhãn trục.
3. **21,5–24,1:** giữ "typical" và "slow cases" ít nhất 1,2 s. Đánh dấu khoảng cách typical (~2 năm) với lịch (8 năm). Bỏ hoặc mờ đường lịch cũ và bớt bó đường (giảm opacity) để giảm rối. Lùi pan sang trong pause 23,06–23,86.
4. **26,0–29,1:** cho "value" (27,19) làm chồng xanh **lớn lên** rõ, và "index" (28,72) làm hiện nhãn chỉ số. Thống nhất một mã màu cho giá trị/giá xuyên hai chế độ (xám = giá, teal = tiền mình, xám đậm = vay).
5. **29,1–34,0:** tắt Source/badge/footer khi về WORLD. Chồng vay ở c5 phải bằng đúng 80 % cột giá. Bỏ chồng teal tiết kiệm lớn thêm. Cho khiên rung + thud rõ hơn (nâng khoảng 6 dB) ở 31,82 và khép bằng một cadence nhạc thay vì để trôi. Đồng thời gỡ badge "ILLUSTRATIVE" khỏi biểu đồ dữ liệu thật (c3) hoặc đổi nhãn cho đúng.
