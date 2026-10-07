# Đạo diễn duyệt E5b — ep005 cold open (34 s, 540p)

Nguồn đã xem: sheet-1/2 (khung 0,5 s), audio.png, transcript.txt (ASR), events.txt, intent.txt.
Quy ước: sự kiện thấy lần đầu ở khung t thì đã xảy ra trong khoảng (t−0,5; t]. Chuẩn đồng bộ ±0,2 s. Chỉ gọi là "lệch" khi khung hình chứng minh được vượt qua mức sai số này.

---

## 1. Lệch hình / lời / âm, và chỗ hình khác ý đồ

| Mốc | Lời (ASR) | Hình (khung) | Âm (events) | Đánh giá |
|---|---|---|---|---|
| 0,0–1,0 | "You've"@0,00 | Nhãn "You" chưa có ở 0,0 và 0,5, xuất hiện ở 1,0 | — | **LỆCH, chứng minh được**: nhãn trễ hơn chữ "You've" **≥ 0,5 s** (khoảng (0,5; 1,0]). Câu đầu xưng "You" trong khi hình chưa chỉ ra ai là "You". |
| 1,0 | "saved"@0,70, "10"@1,04 | Chồng tiền nhỏ có ở 1,0, chưa có ở 0,5 | tick 1,13 | Trong sai số (hình ở (0,5; 1,0], tick 1,13). Hình có thể đi trước tick 0,13–0,63 s; chưa chứng minh được là lệch. |
| 0–3 | "ten percent of a home's price" | Chồng giá nhà là khối **đặc, không MỜ**. Chồng 10 % **nằm ngang dưới đất**, không "trong tay" người xem | — | **KHÁC Ý ĐỒ**. Hình không có phép so 10 % với 100 %: một khối đứng (khoảng 16 thếp) và một thếp nằm ngang thì không so được bằng mắt. |
| 2,175–3,175 | "home's price"@2,20–2,88 | Máy lùi trong lúc câu còn đang đọc | whoosh_soft 2,17 | Đúng giờ theo kế hoạch, nhưng lý do lùi máy ("thấy cả hai lối") đi trước câu hỏi 1,9 s. Căn hộ đã có trong khung từ 0,0 (bị cắt mép phải), nên cú lùi chỉ thu nhỏ cảnh. |
| 5,5–6,0 | "mortgage"@5,26, "insurance"@5,66 | Khiên đang rơi ở 5,5, nằm trên mái ở 6,0. Nhãn "buy now + mortgage insurance" có ở 5,5 | land 5,66 | Khớp. Tuy vậy ở 5,5 **nhãn đè lên khiên đang rơi** (chữ chồng hình). |
| 7,0–9,0 | "renting"@7,22, "20 %"@8,38 | Nhãn "keep renting, keep saving" mờ ở 7,0, rõ ở 7,5 (khớp). Chồng của người xem **bắt đầu dài ra trong (7,0; 7,5]** và vẫn dài tiếp tới 9,0 | rise 8,46 | **KHÁC Ý ĐỒ và LỆCH âm–hình**. Không thấy vạch 20 % mờ nên chồng tiền không "chạm" đích nào. Chồng lớn theo chiều ngang, ngay cạnh căn nhà chứ không ở phía căn hộ. Âm "rise" (8,46) đến sau lúc hình bắt đầu lớn **≥ 0,96 s**. |
| 9,0 | "%?" kết thúc 9,22 | Nhãn mờ dần, máy bắt đầu đi | whoosh_mode 9,00 | Whoosh đè lên đuôi chữ "percent" khoảng 0,2 s. Lỗi nhỏ. |
| 10,5 | "schedule"@10,64 | Đường bắt đầu ở 90 % trong (10,0; 10,5] | data notes từ 10,6 | Trong sai số. |
| 13,5–14,0 | "8"@13,54 (intent ghi 13,753) | Ở 13,5 đường **đã chạm vạch 80 %** tại ~8 năm, nhãn "about 8 years" đang hiện. Quầng sáng ở 14,0 | chime 13,75 | **LỆCH hình–âm, chứng minh được**: lúc chạm vạch nằm ≤ 13,5, chime ở 13,75, cách **≥ 0,25 s**. Mốc từ khóa trong intent (13,753) cũng cách ASR (13,54) 0,21 s, khác hẳn mức trung vị 0,005 s đã nêu. Cần đo lại onset của "eight". So với lời thì hình khớp ASR, còn chime trễ. |
| 15,5 | "replayed"@15,70 | Tiêu đề cũ và mới **chồng lên nhau**, không đọc được. Bó đường xuất hiện trong (15,5; 16,0] | tick 15,70 | Bó đường đúng giờ. Crossfade tiêu đề gây chữ chồng. |
| 15,7–20,35 | "…month by month … took" | Bó đường vẽ từ trái sang phải. Từ khoảng 19,0 hình gần như đứng yên (19,0, 19,5, 20,0 giống nhau) | 11 tick đều nhau mỗi 0,466 s, tới 20,35 | Tick chạy như máy đếm nhịp, không gắn với nét vẽ. Khoảng 1 s tick cuối không còn hình nào phản ứng. |
| 21,5 | "typically"@21,50 | Đường điển hình và nhãn "typical" xuất hiện trong (21,0; 21,5] | nốt (data) | Trong sai số. Trên audio.png không tách riêng được nốt "sáng" này. |
| 22,5 | "slow"@22,42 | Đường vàng và nhãn "slow cases" xuất hiện trong (22,0; 22,5] | nốt trầm (data) | Trong sai số. |
| 23,14–24,14 | khoảng nghỉ 23,04–23,86, "On"@23,86 | Lia máy (23,5 đang giữa cú lia) | whoosh_push 23,14 | Khớp. Cú lia trùm lên chữ "On" 0,28 s, chấp nhận được. |
| 24,5–26,0 | "eighty"@26,10 | Nhãn 88 % → 85 % → 82 %, rồi "80 % on paper" ở 26,0 | chime 26,05 | Trong sai số (khung (25,5; 26,0]). Hình có thể sớm tới 0,6 s nhưng không chứng minh được. |
| 29,14–30,04 | khoảng nghỉ 29,16–30,02 | Ở 29,5 thấy **hai vệt thẳng lạc** (đường 80 % và đường đồ thị nhìn phối cảnh) nằm trên mặt đất của thế giới | whoosh_mode 29,14, land 30,04 | Thời điểm khớp. Hai vệt đường trông như lỗi render. |
| 30–32 | "removed"@31,72 | Khiên vẫn trên mái. "insurance still on" xuất hiện trong (31,5; 32,0] | thud 31,82, nhạc dừng 31,82 | Đúng giờ. **KHÁC Ý ĐỒ**: không thấy "chồng vay đã thấp" trong thế giới (chồng dưới nhà và thếp của người xem trông như ở cảnh mở đầu). Không thấy được cú rung của khiên (khung 0,5 s không bắt được, nên không kết luận). |

Ngoài ra có một chỗ trái quy tắc thiết kế: ở chế độ WORLD vẫn có nhãn so sánh ("buy now + mortgage insurance" / "keep renting, keep saving", "insurance still on"). Không có con số, nhưng đây đúng là loại nhãn so sánh mà thiết kế dành riêng cho CHART.

## 2. Chuyển cảnh và chuyển chế độ

1. **Pull 2,2–3,2 (wYou→wFork)**: hình liền mạch, nhưng lý do yếu. Căn hộ đã có sẵn trong khung, nên cú lùi không lộ thêm điều gì mới. Máy dừng ở 3,2 rồi đứng yên tới 4,1 trong khoảng nghỉ: chuyển động không dẫn vào câu hỏi.
2. **Mode 9,0–10,1 (wFork→cSched)**: **GÃY về nghĩa**, dù chuyển động vẫn liên tục. Khung 9,5 gần như trống, chỉ còn căn hộ ở mép trái. Ở 10,0 hiện ra một đồ thị 2D phẳng trên nền đen, không có chồng tiền, không có nhà. Design note ghi "data point is the TOP of a money stack", nhưng đồ thị lịch trả nợ (10–15 s) và bó đường (15,5–23) chỉ là đường kẻ. Điểm 90 % đáng lẽ phải là đỉnh chồng nợ của người xem. Ý "một thế giới, hai chế độ máy" mất ở đây; người xem cảm thấy đó là một cú cắt sang slide.
3. **Đổi dữ liệu 15,5 (cùng cSched)**: không có cú máy. Tiêu đề, trục (thêm 100 %) và dòng chân trang đổi cùng lúc, có một khung chữ chồng. Đây là chuyển đổi nghĩa lớn ("theo lịch" → "theo chỉ số giá") mà không có dấu hiệu hình nào báo trước. Đường lịch 8 năm cũ chìm trong bó đường; nhãn "about 8 years" còn lại nên dễ bị đọc nhầm là nhãn của bó đường.
4. **Pan 23,1–24,1 (cSched→cDef)**: có lý do, liền mạch, đúng khoảng nghỉ. Đây là chuyển cảnh tốt nhất. Khung 23,5 cho thấy hai chỗ nằm trong cùng một không gian.
5. **Mode 29,1–30,0 (cDef→wHouse)**: có lý do. Hai vệt đường lạc ở 29,5 làm bẩn khung. Cũng không có liên kết hình: chồng "loan" xám của cDef không xuất hiện ở căn nhà, nên câu "dù chồng vay đã thấp" không có hình.

## 3. Nhịp

- **5 s đầu: móc yếu.** Khung 0,0 là cảnh rộng, tối, tĩnh: một căn nhà, một hình nhân, một khối nhà bị cắt mép. Không có câu hỏi, không có chuyển động mang nghĩa. Biến cố duy nhất là một thếp tiền rơi ở khoảng 1 s, không có phép so nào để người xem kịp hiểu "10 % là ít". Từ 3,2 tới 5,0 hình đứng yên (khoảng nghỉ 2,88–4,08, rồi "Do you buy now" trên khung không đổi tới 5,0). Nhạc ở mức -50 đến -55 dBFS trong 2 s đầu. So với Vox/WSJ thì chưa có căng thẳng nào trước giây thứ 5.
- **Chỗ chùng**: 3,2–5,0 (khoảng 1,8 s hình đứng yên). 14,4–15,5 (giữ nhãn "about 8 years" khoảng 1 s, chấp nhận được vì là chỗ thở sau cú đấm). 19,0–21,0 (bó đường đã vẽ xong, tick còn chạy, rồi "on paper," và nghỉ tới 21,5). 32,2–34,0 (khung tĩnh sau lời cuối, nhạc tắt; chấp nhận được cho cú kết).
- **Chỗ dồn/rối**: 15,5–23,0. Trong 7,5 s người xem phải nhận đổi tiêu đề, đổi trục, thêm footer, 307 đường, đường điển hình, đường chậm và hai nhãn. Riêng bó đường đã là một khối lưới trắng dày, trên điện thoại trông như một mảng nhiễu. Ý quan trọng nhất của đoạn này (đường điển hình chạm 80 % sớm hơn nhiều so với 8 năm theo lịch) chỉ thấy được nếu dừng hình, vì nhãn "typical" nhỏ và nằm sát trục.
- Đoạn 24–29 (hai chồng) có nhịp tốt: số 88→85→82→80 đếm lùi theo lời rồi chốt đúng chữ "eighty".

## 4. Lớp bắt buộc

- **ILLUSTRATIVE** (từ 10,5): góc trên phải, nền vàng, đọc được, không đè dữ liệu. Tốt.
- **"US only · history, not a forecast"** (từ 15,5) và **"A measurement, not a next step"** (từ 10,5): góc dưới trái. Không đè dữ liệu, nhưng ở cDef (24–29) chân hai chồng tiền gần chạm dòng footer. Chữ cao khoảng 3–3,5 % chiều cao khung: trên điện thoại cầm ngang vẫn đọc được nhưng sát ngưỡng.
- **Nguồn "Source: FHFA · Freddie Mac via FRED"**: có. Hai điều cần sửa. (a) Ở đồ thị lịch trả nợ 10,5–15 (một phép tính khấu hao) mà gắn FHFA là gây hiểu lầm; nên ghi nguồn lãi suất kèm "computed". (b) Ở cảnh thế giới 30–34 (không có dữ liệu) cả ba lớp vẫn đè lên cảnh, làm khung cuối rối.
- **Đối trọng**: đường "slow cases" có mặt và đúng giờ. Nhưng nhãn vàng nằm đè trên lưới trắng nên tương phản kém. Nhãn "typical" màu trắng nằm ngay dưới vạch 80 % sát hàng số trục, khó đọc.
- **Chữ chồng / cắt mép**: tiêu đề chồng nhau ở 15,5. Nhãn đè khiên ở 5,5. Căn hộ bị cắt mép phải ở 0,0–2,0. Tiêu đề bó đường ("loan ÷ home value by a national index · one line per purchase month, 1991–2016") dài và cỡ khoảng 2,5 % chiều cao khung, **không đọc được trên điện thoại**. Số trên trục (0…10 years, 80/90/100 %) cũng ở cỡ này.

## 5. Âm

- **Lời luôn rõ**: giọng có đỉnh khoảng -7 đến -12 dBFS. Nhạc chủ yếu ở -35 đến -45, sfx và data có đỉnh khoảng -28 đến -33, đều nằm trong khoảng nghỉ hoặc dưới giọng 15 dB trở lên. Đạt.
- **Nhạc theo căng–chùng**: trên audio.png nhạc gần như phẳng (-35 đến -45) từ 4 tới 29 s. Đường tension (0,3 → 0,65 → 0,35) không nghe ra được: không thấy bước nâng ở 10,4 hay 15,6. Hai accent ở 13,75 và 26,05 không nổi rõ trên đường nhạc. Phần nhả từ 29,9 (xuống -50) và cú dừng ở 31,82 đúng chữ "removed" thì có.
- **Kết thúc**: nhạc dừng ở "removed" kèm thud, rồi fade tới 34 s. Đúng ý "chưa", có cảm giác bỏ lửng hợp với cold open. Nhạc dừng giữa chữ "removed" (31,72–32,24) là chủ ý, chấp nhận được.
- **Âm dữ liệu**: 10,6–14 có nghĩa (nốt theo năm, rồi chime khi chạm 80 %). Nhưng chime trễ hơn lúc hình chạm ≥ 0,25 s (xem mục 1).
- **Hiệu ứng thừa/khó chịu**: 11 tick đều nhịp từ 15,7 tới 20,35 chạy dưới giọng nói, đè lên cụm "real US prices and rates month by month". Chúng không gắn với từng đường vẽ ra và còn kéo dài sau khi hình đã xong. Đây là âm trang trí, dễ gây mệt. Âm "rise" ở 8,46 không có đích hình để chạm vào. Bốn whoosh ở mức vừa phải, không chói.

## 6. 3D: làm ý rõ hơn hay chỉ trang trí

- **cDef (24–29) là chỗ 3D làm ý rõ nhất**. Hai chồng nhìn chính diện, đáy chung. Đo trên khung: tỉ lệ cao chồng vay / chồng giá trị khoảng 0,89 ở 24,0 và khoảng 0,81 ở 28,0, **khớp 88 % → 80 %**. Chồng giá trị lớn lên còn chồng vay gần như đứng yên, cho thấy đúng rằng "on paper" chủ yếu nhờ giá nhà tăng. Đạt.
- **c0/c1 (0–9) chỉ là trang trí**. Phối cảnh và hướng đặt (một chồng đứng, một thếp nằm ngang, gần máy hơn) làm **không đọc được tỉ lệ 10 % so với giá nhà**. Vì thiếu chồng MỜ và vạch 20 %, ý "10 % → 20 %" không có hình.
- **c2/c3 (10–23) không dùng 3D**: đó là đồ thị phẳng. Trục 80–90 % (sau đó tới 100 %) bị cắt gốc nhưng nhất quán và vạch 80 % là ngưỡng thật, nên **không làm sai tỉ lệ 90 % → 80 %**. Có điều độ dốc rất nông và vùng dữ liệu chỉ chiếm khoảng 15 % chiều cao khung, nên cú "đi xuống chậm" thiếu sức nặng.
- **c5 (30–34)**: khiên vàng trên mái là một biểu tượng rõ. Nhưng không có chồng vay thấp bên cạnh nên không có tương phản "đã thấp mà vẫn còn".

## 7. Chấm điểm (so với Vox / 3Blue1Brown / WSJ)

| Tiêu chí | Điểm | Lý do chính |
|---|---|---|
| Hình mang nghĩa | **3** | cDef và lịch 8 năm rõ. Mở đầu và c1 chỉ trang trí, thiếu chồng mờ và vạch 20 %. Bó đường là một mảng lưới khó đọc. |
| Liền mạch hình–lời–âm | **3** | Phần lớn khớp trong ±0,2 s. Lệch chứng minh được: nhãn "You" (≥ 0,5 s), chime 13,75 (≥ 0,25 s), "rise" (≥ 0,96 s). Chuyển sang CHART ở 9–10 gãy về nghĩa. |
| Nhịp | **2** | Không móc được trong 5 s đầu. Chùng 3,2–5,0 và 19–21,5. Dồn quá tải 15,5–23. |
| Âm | **3** | Lời luôn rõ, kết đúng chữ. Nhạc phẳng, không theo tension. Tick đều nhịp thừa. Chime lệch hình. |

### Năm sửa quan trọng nhất (xếp theo mức ảnh hưởng tới điểm)

1. **0,0–5,0: dựng lại móc.** Nhãn "You" phải có từ 0,0. Thêm chồng giá nhà MỜ đứng cạnh, đặt thếp 10 % **đứng** ngay sát chân nó ở chữ "ten" (1,04) kèm tick, để mắt tự đo 1/10. Khoảng 2,9–4,1 dùng để đẩy căng thẳng: máy lùi đúng lúc vào "Do you buy now" (4,1) chứ không phải ở 2,2, hoặc cho khiên lơ lửng phía trên mái từ cuối câu 1. Khung không được đứng yên quá 0,5 s trong 5 s đầu. (Ảnh hưởng: Nhịp, Hình.)
2. **9,0–10,5: chuyển sang CHART phải mọc ra từ thế giới.** Máy lao tới chồng nợ của người xem; đỉnh chồng là điểm 90 % đầu tiên; các chồng của từng năm tạo thành đường (đúng design note). Bỏ khung trống ở 9,5. (Ảnh hưởng: Liền mạch, Hình.)
3. **15,5–23,0: làm sạch bó đường.** Hạ độ đậm của 307 đường (xám mờ, khoảng 15–20 %). Giữ đường lịch 8 năm sáng làm mốc so. Đổi tiêu đề bằng cắt chứ không crossfade, và rút gọn tiêu đề để đọc được trên điện thoại. Cho "typical" và "slow cases" nền tối, đặt ở chỗ trống. Thay 11 tick đều nhịp bằng âm gắn với lúc nét vẽ chạy và dừng ở khoảng 19,0. (Ảnh hưởng: Nhịp, Hình, Âm.)
4. **7,2–8,5: đích 20 %.** Vẽ vạch 20 % mờ phía căn hộ. Chồng tiền lớn theo chiều đứng và chạm vạch đúng ở "20" (8,38) cùng lúc với âm "rise". Bỏ nhãn đè khiên ở 5,5. (Ảnh hưởng: Hình, Liền mạch.)
5. **13,5 và nhạc tổng: chốt đồng bộ và căng–chùng.** Đo lại onset của "eight" (13,54 theo ASR, 13,753 theo intent) rồi đặt chime, quầng sáng và lúc đường chạm vạch vào cùng một mốc. Nâng nhạc theo tension thật (+3 đến 4 dB ở 10,4 và 15,6) và làm accent 13,75 / 26,05 nghe ra được. Đồng thời dọn khung kết 30–34: bỏ footer và nguồn ở cảnh không có dữ liệu, thêm chồng vay thấp cạnh căn nhà, bỏ hai vệt đường lạc ở 29,5. (Ảnh hưởng: Âm, Liền mạch.)
