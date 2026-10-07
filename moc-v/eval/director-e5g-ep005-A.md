# Đạo diễn duyệt E5g — ep005 cold open (34 s, bản xem trước 540p)

Nguồn đã xem: sheet-1/2 (khung 0,5 s), audio.png, transcript.txt, events.txt, intent.txt. Khung cách nhau 0,5 s, nên một sự kiện thấy lần đầu ở khung t đã xảy ra trong (t−0,5; t]. Mốc lời lấy theo sóng âm (intent), ASR chỉ để đối chiếu.

## 1. Lệch hình / lời / âm (chuẩn ±0,2 s)

| # | Từ khoá (mốc) | Hình dự định | Thấy lần đầu | Khoảng | Kết luận |
|---|---|---|---|---|---|
| 1 | saved 0,707 (tick) | chồng tiền teal xuất hiện | 1,0 (0,5 chưa có) | (0,5; 1,0] | khớp được |
| 2 | ten 1,13 (land) | chồng teal trượt vào dưới nhà | 1,5 | (1,0; 1,5] | khớp được |
| 3 | price 2,55 (rise) | tháp giá xám nhạt mọc lên, nhấc nhà | 3,0 (2,5 chưa có) | (2,5; 3,0] | khớp được |
| 4 | máy lùi 2,96–3,96 (whoosh_soft) | wYou→wFork | 3,5 rộng hơn, 4,0 đứng | — | đúng, nằm trong khoảng lặng 2,88–4,10 |
| 5 | buy 4,22 | (cue có trong danh sách) | không có sự kiện hình nào ở 4,0–5,5 | — | **cue không có hình**: nhãn "buy now + mortgage insurance" chỉ hiện ở 6,0, trễ khoảng 1,4–1,8 s so với "buy" (nếu nhãn được gắn với "insurance" thì khớp) |
| 6 | insurance 5,656 (land) | khiên rơi lên mái | 6,0 | (5,5; 6,0] | khớp được; không thấy được pha "rơi" ở 0,5 s/khung |
| 7 | renting 7,26 | nhãn "keep renting, keep saving" + chồng tiền ở căn hộ | 7,5 | (7,0; 7,5] | khớp được |
| 8 | twenty 8,457 (rise) | chồng lớn tới vạch 20 % + mũi tên lên | mũi tên mờ ở 8,5, rõ ở 9,0 | (8,0; 8,5] | thời điểm khớp được, nhưng **chồng gần như không lớn lên** (7,5 và 9,0 cao bằng nhau) → hình KHÁC ý đồ |
| 9 | chuyển chế độ 9,0–10,1 (whoosh_mode) | wFork→cSched, nhà co vào đỉnh chồng (morph) | 9,5: nhà còn nguyên mái, đường đồ thị đã vào từ phải; 10,0: đồ thị | — | đúng giờ; **không thấy morph** (xem mục 2) |
| 10 | schedule 10,644 | đường bắt đầu đi từ 90 % | 11,0 (10,5 chưa có) | (10,5; 11,0] | khớp được |
| 11 | cancel 12,559 | — | đường vẫn đang vẽ, không có nhấn | — | cue không có hình, chấp nhận được |
| 12 | eight 13,753 (chime) | chạm 80 % ở ~8 năm + "about 8 years" + điểm sáng | 14,0 (13,5 chưa có) | (13,5; 14,0] | khớp được |
| 13 | replayed 15,697 | bó đường hiện dần | 16,0 | (15,5; 16,0] | khớp được; quét tới 20,0 |
| 14 | typically 21,508 | đường điển hình sáng lên | 21,5 nhãn mờ đang hiện; 22,0 rõ | khoảng 21,5 | khớp được, **nhưng chữ đè chữ** (mục 4) |
| 15 | slow 22,344 | đường chậm nhất màu cảnh báo + "slow cases" | 22,5 | (22,0; 22,5] | khớp được |
| 16 | lia 23,13–24,13 (whoosh_push) | cSched→cDef | 23,5 đang trượt, 24,0 hai chồng | — | đúng |
| 17 | paper 24,387 | nhãn "loan 90%" | 24,5 | (24,0; 24,5] | khớp được |
| 18 | eighty 26,046 (chime) | chồng vay chạm vạch, "80% on paper" | 26,5; ở 26,0 còn ghi **81 %** | (26,0; 26,5] | chưa xác nhận được bằng khung; con số đếm 90→86→83→81 cho thấy chồng tới vạch sau 26,0 (đo pixel báo ±0,2) |
| 19 | value 27,187 | nhãn "home value by a national price index" | 27,5 | (27,0; 27,5] | khớp với "value", nhưng chữ "national price index" lên **trước lời "index" (28,72) khoảng 1,2 s** |
| 20 | chuyển chế độ 29,14–30,04 (whoosh_mode, land 30,04) | cDef→wHouse | 29,5 **bó đường cũ hiện lại**; 30,0 thế giới | — | đúng giờ, nhưng gãy (mục 2) |
| 21 | same 30,464 | (không có trong spec) | chồng vay xám đậm nằm ở 30,0, đứng lên ở 30,5 | — | trùng "same", tạm ổn |
| 22 | removed 31,82 (impact) | khiên rung rồi đứng; nhãn "insurance still on" | nhãn ở 32,0 (31,5 chưa có) | (31,5; 32,0] | khớp được; pha rung không thấy được ở 0,5 s/khung |

Tổng kết: không có sự kiện nào sai khung một cách chứng minh được. Những chỗ hình KHÁC ý đồ:
- 0–2,5 s: intent (c0) muốn có chồng MỜ = giá nhà ngay từ đầu, người xem cầm chồng nhỏ. Bản dựng thì không có chồng mờ; tháp giá chỉ mọc ở "price". Cách này hợp với thiết kế "tháp mọc lên nhấc nhà", nhưng 2,5 s đầu thiếu thước so sánh 10 %.
- 7,5–9,0 s: chồng thuê nhà không lớn từ 10 % lên 20 %. Chỉ thấy mũi tên. Điểm chính của lối thuê vì thế không được trình bày bằng hình.
- 9,5 s: nhà không co vào đỉnh chồng. Trông như một nhát chuyển hoặc trượt cảnh, chứ không phải morph.
- c3: "nốt sáng (điển hình) / nốt trầm (chậm)" chỉ đọc được trên ảnh âm thanh (sóng dữ liệu kết thúc ở 22,3). Mình không phân biệt được cao độ.

## 2. Chuyển cảnh và chuyển chế độ

- **2,96–3,96 lùi máy (wYou→wFork)**: lý do đúng (cần thấy cả hai lối). Cảnh liền mạch, nằm gọn trong khoảng lặng. Tốt.
- **9,0–10,1 thế giới→đồ thị**: lý do đúng ("on the schedule" là một đường theo thời gian). Tuy vậy ở 9,5 nhà vẫn còn đủ mái và tháp, trong khi đường đồ thị đã trượt vào bên phải. Không thấy được câu "nhà co thành đỉnh chồng = điểm dữ liệu". Thêm nữa, đồ thị cSched là một **đường** dư nợ/giá, không phải chồng, nên phép ẩn dụ "đỉnh chồng là điểm dữ liệu" bị đứt ngay ở lần chuyển đầu tiên. **Gãy nhẹ.**
- **11,0**: nguồn, nhãn ILLUSTRATIVE và chân "A measurement, not a next step" bật ra cùng lúc, thêm 3 khối chữ đúng lúc người xem cần nhìn đường. Hơi gắt.
- **15,5–16,0 đồ thị lịch→bó đường thật**: tiêu đề mờ đi rồi đổi, trục y được thêm 100 %, đường lịch thu lại thành "schedule ≈ 8 years". Đây là phép biến đổi có nghĩa (đường lý thuyết → dữ liệu thật). Liền mạch, cảnh hay nhất phim.
- **23,13–24,13 lia sang hai chồng**: lý do đúng. Ở 23,5 bó đường trượt ra khỏi khung, mọi nhãn tắt. Liền mạch.
- **29,14–30,04 đồ thị→thế giới**: ở 29,5 **bó đường của cảnh trước hiện lại** (máy đi ngược qua cSched), sau đó mới tới căn nhà. Người xem thấy một cảnh "quay lại quá khứ" chẳng mang nghĩa gì, vừa đúng lúc lời bắt đầu "That's not the same". Chồng vay (cDef) có thể đã thành chồng vay xám đậm cạnh nhà (30,0 nằm, 30,5 đứng), đó là ý hay nhưng không đọc được vì bị cảnh bó đường che mất. **GÃY.**

## 3. Nhịp

- **0–2,5 s**: khung 0,0 tĩnh. Ba vật nhỏ nằm ở dải giữa, khoảng 55–60 % khung là đen trống. Nhãn "You" chỉ hiện ở 0,5. Chồng tiền ở 1,0 và tháp giá ở 3,0 là hai nhịp thị giác tốt. **Móc 5 s đầu: trung bình.** Có câu hỏi ẩn ("10 %… rồi sao?"), nhưng chưa có cú nhìn mạnh hay cái giá phải trả trước 4,1 s, và nhạc gần như im (khoảng −50 dBFS) tới ~2,5 s.
- **4,1–9,2 s**: câu hỏi hai lối là móc thật. Hình chỉ có thêm 2 nhãn và 1 khiên, phần lớn tĩnh (4,0–5,5 không có gì chuyển động). **Hơi chùng ở 4,0–5,5.**
- **10–15,5 s**: đường đi chậm 90→80 hợp với "about eight years". Nhưng 14,4–15,5 là khoảng giữ tĩnh 1 s, chấp nhận được.
- **16–23 s**: chỗ **dồn/rối** nhất. Bó 307 đường thành một "dãy núi" lưới vượt quá 100 %, trong khi lời chỉ nói "typically / slow". Cái gù lớn (dư nợ > giá trị nhà) không hề được giải thích, rất gây phân tâm. Sau đó ba nhãn đè nhau ở 22,0–23,0.
- **24–29 s**: đếm 90→80 % rõ, tốt. 27,5–29 thêm khối nhãn "home value by a national price index", chấp nhận được.
- **30–34 s**: kết gọn. Giữ ~1,8 s sau lời với nhãn "insurance still on" là đủ.

## 4. Lớp bắt buộc (nguồn, ILLUSTRATIVE, chú thích)

- **Chữ chồng**: 22,0–23,0 nhãn "typical ≈ 2 years" đè lên "schedule ≈ 8 years" thành "typical ≈ 2 yea**rs**chedule ≈ 8 years". Đây là lỗi nặng nhất về chữ. Ở 21,5 nhãn mờ cũng đã chạm vào nhau.
- **Đè hình**: chân trang hai dòng ("Past buyers, measured · not a reason to buy, rent or wait / US only · history, not a forecast") nằm sát dưới trục x (16–23 s), dòng số năm và chân trang dính vào nhau. Ở 22,0–23,0, chân trang + nhãn typical/schedule + nhãn trục tạo thành ba lớp chữ trong khoảng ~40 px (thumbnail).
- **Cỡ chữ cho điện thoại** (quy đổi ×6): nguồn/ILLUSTRATIVE/chân trang ≈ 7 px → ~40 px ở 1080p, đọc được nhưng sát ngưỡng. Số trục x (0 2 4 6 8, "10 years") ≈ 5 px → ~30 px, **quá nhỏ cho điện thoại**. Tiêu đề "Loan as % of home value · one line per purchase month, 1991–2016" ≈ 6 px → ~36 px và quá dài. "You", "insurance still on", "80% on paper" ≈ 7–8 px → ~45 px, đạt.
- **Cắt mép**: không thấy chữ bị cắt. Tháp ở 3,0 có mái sát mép trên nhưng chưa bị cắt. Ở 29,5 chữ của lớp bắt buộc mờ dần cùng cảnh, chấp nhận được.
- 10,0–10,5: đồ thị chưa có nguồn/ILLUSTRATIVE (chỉ lên ở 11,0), nên trong 1 s đầu dữ liệu xuất hiện mà không có nguồn.
- Nhãn ILLUSTRATIVE vắng trên đồ thị bó đường (16–23 s). Đúng, vì đó là dữ liệu thật. Có mặt ở cSched và cDef. Nhất quán.

## 5. Âm

- **Lời rõ**: đỉnh giọng khoảng −10 dBFS, nhạc nền −30 đến −40, cách nhau ~20 dB. Rõ.
- **Nhạc theo căng–chùng**: bản đồ căng 0,3→0,45→0,6→**0,8 (15,6)**→0,65→0,4, nhưng mức nhạc trên ảnh gần như phẳng (−30 đến −38) từ 4 s tới 29 s. Cú dâng ở 15,6 s không thấy được. Phần chùng sau 29,9 thì có (nhạc giảm dần). Nhạc **không tắt ở "removed" (31,82)** như kế hoạch: vẫn còn khoảng −40 đến −45 dBFS ở 32,5–33 và tắt hẳn ~34,0. Cũng không thấy đỉnh "hợp âm cuối". Kết thúc là một lần fade, không phải một lần chốt.
- **Âm dữ liệu**: 17 nốt trong 10,6–22,3 s, đỉnh −22 đến −30 dBFS, vài nốt rơi vào giữa câu nói (12–14 s, 19–20 s). Cao độ = tỉ lệ trung vị là một mã hoá mà người xem không có chìa khoá để hiểu. Ở 10–14 s nốt theo năm hợp với đường đang vẽ, có ích. Ở 16–22 s chỉ là nhịp gõ.
- **Hiệu ứng thừa/lệch**: "land" ở 10,10 không có vật gì đáp xuống (đồ thị chỉ hiện ra). "chime" 13,75 trùng đúng chữ "eight", nghe như nhấn mạnh, chấp nhận được. Có 4 whoosh trong 34 s; whoosh_mode 9,0 đạt khoảng −24 dBFS ngay trước "On" (10,34), hơi to so với nền. Impact 31,82 yếu (khoảng −37 đến −40), không ra "tiếng trầm có thân".
- 0–2,5 s: nhạc gần như im (khoảng −50), chỉ có tick và land, nên cold open mở ra hơi trống.

## 6. 3D: làm rõ ý hay trang trí

- **Làm rõ ý**: tiền tiết kiệm (teal) trượt vào dưới nhà rồi tháp giá nhấc nhà lên (1,0–3,0) là hình mang nghĩa đúng tinh thần 3Blue1Brown. Lớp teal ở đáy so với cả tháp trông khoảng 1/10 (≈10/95 px ở 3,0), **tỉ lệ 10 % đạt** (ước lượng bằng mắt). Đếm chồng vay 90→80 % ở cDef cũng rõ. Vạch 80 % nằm ở khoảng 81 % chiều cao chồng giá trị (đo ở 29,0), đúng.
- **Trang trí/lệch**: chồng thuê nhà không lớn lên 20 % (7,5–9,0). Khiên chỉ là một khối vàng nhỏ trên mái, khó đọc là "bảo hiểm" nếu không có nhãn. Ở 30,5–33,5 chồng vay xám đậm cạnh nhà cao khoảng 60 % tháp giá (ước lượng thô, có phối cảnh), trong khi phải là ~80 % giá trị, nên **cần kiểm tra lại tỉ lệ**. Chồng teal ở căn hộ vẫn còn ở cảnh cuối, gây rối (hai chồng teal cho cùng một khoản tiết kiệm).
- **90 %→80 % (cSched 10–15 s)**: dải 80–90 % chỉ chiếm khoảng 24 px trên 205 px khung (≈12 %), nửa trên khung trống. Đường trông gần như nằm ngang, nên cảm giác "chậm 8 năm" bị nén lại. Trên điện thoại chỉ là một sợi chỉ.
- Bó đường dạng lưới (16–23 s) đọc như một mặt 3D hơn là 307 đường riêng. Đẹp, nhưng phần vượt 100 % không có nhãn hay lời giải thích.

## 7. Điểm (1–5, so với Vox / 3Blue1Brown / WSJ)

| Tiêu chí | Điểm | Lý do |
|---|---|---|
| Hình mang nghĩa | **3** | Mở 10 %/tháp giá và đếm 90→80 tốt. Chồng 20 % không lớn, morph không thấy, gù >100 % không giải thích. |
| Liền mạch hình–lời–âm | **3** | 22/22 mốc khớp trong khoảng khung, nhưng có chữ đè 22–23 s, cảnh bó đường flash lại ở 29,5 và cue "buy" không có hình. |
| Nhịp | **3** | Mở chậm và trống (0–2,5), chùng 4–5,5, dồn rối 16–23, kết ổn. |
| Âm | **3** | Lời rõ. Nhạc phẳng không theo căng, kết là fade chứ không chốt ở "removed", có "land" thừa, nốt dữ liệu khó giải mã. |

### Năm sửa quan trọng nhất

1. **21,5–23,0 s**: tách nhãn "typical ≈ 2 years" khỏi "schedule ≈ 8 years". Đặt typical phía trên đường trắng ở x≈2 năm, hoặc mờ schedule xuống khi typical lên. Đẩy chân trang xuống thấp hơn trục x ít nhất 1 dòng.
2. **29,14–30,04 s**: bỏ cảnh bó đường xuất hiện lại ở 29,5 (ẩn lớp cSched hoặc cho máy đi đường khác). Cho chồng vay của cDef bay/morph thẳng thành chồng vay xám đậm cạnh nhà, để "loan đã thấp mà khiên vẫn còn" đọc được bằng một chuyển động. Kiểm tra chiều cao chồng vay ≈ 80 % tháp giá trị (30,5–33,5).
3. **7,26–8,46 s**: cho chồng teal ở căn hộ **lớn gấp đôi thấy được** (10 %→20 %), chạm vạch 20 % mờ ngay ở "twenty", có nốt đi lên. Hiện tại chỉ có mũi tên.
4. **10,0–15,5 s**: phóng trục y (ví dụ 78–92 %) để đường 90→80 chiếm ≥40 % chiều cao khung. Ở 15,6 thì nới trục lên tới >100 % như một phép biến đổi có nghĩa ("dữ liệu thật vượt cả giá trị nhà"), và gắn nhãn hoặc tô vùng >100 %. Phóng số trục x lên ≥40 px@1080p.
5. **0,0–2,5 s và 31,82 s**: mở bằng chuyển động ngay từ khung 0 (máy đẩy nhẹ vào, hoặc chồng mờ = giá nhà có sẵn) và cho nhạc vào ngay (không để −50 dBFS). Ở "removed" cho nhạc tắt/chốt đúng kế hoạch (stop 31,82, release 32,82) với impact trầm to hơn. Bỏ "land" ở 10,10.
