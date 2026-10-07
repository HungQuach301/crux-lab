# Đánh giá đạo diễn: V3a / ep004 (bản xem trước 540p, 0–69,6 s)

Nguồn: sheet-1/2 (khung hình cách nhau 0,5 s), audio.png, transcript.txt (mốc ASR), events.txt, intent.txt.
Sai số: khung hình cách nhau 0,5 s nên mọi mốc "hình" chỉ chính xác trong khoảng ±0,25 s. Một độ lệch nhỏ hơn 0,5 s chỉ được coi là *có thể* lệch. Mốc âm lấy từ events.txt và làn sfx/data trên audio.png (độ phân giải 50 ms, đọc bằng mắt nên sai khoảng ±0,1 s).

---

## 1. Chỗ lệch hình / lời / âm, và chỗ hình khác ý đồ

| # | Mốc (s) | Lời (ASR) | Hình (khung) | Âm | Đánh giá |
|---|---|---|---|---|---|
| 1 | 0,8–3,6 | "Has their gain past the cap?" (cap 3,20) | Chỉ có nhà, chồng tiền và hai người. **Không thấy xà trần mờ** ở khung nào từ 0–4,5. Dấu "?" nhỏ màu nâu, xuất hiện lần đầu ở 3,0, **sát mép trên và bị cắt một nửa**. | riser 1,52 → khoảng 3,5 | **KHÁC Ý ĐỒ.** Câu hỏi nói về "cap" mà trên hình không có trần. Hook mất đối tượng. "?" khớp thời điểm (3,0 so với 3,20, trong sai số) nhưng gần như không nhìn thấy. |
| 2 | 4,96 | "We can't see their house" (4,74–5,32) | 5,0: nhà tối lại, người biến mất, nhãn mờ dần | whoosh_soft 4,96 | Khớp. |
| 3 | 7,04 | "rise" | Mũi tên ↑ có ở 7,0 | – | Khớp (±0,25). |
| 4 | 8,98–13,23 | "exactly like … Agency" | Mỗi khoảng 0,39 s thêm một căn nhà (9,0 → 13,5, khoảng 12 nhà) | 12 tick | Nhịp tick khớp với số nhà (với khung 0,5 s thì không kiểm tra được từng tick). **Biển SOLD chỉ là chấm đỏ trắng, không đọc được ở 540p.** |
| 5 | 11,32 | "Federal Housing Finance Agency" | "Source: FHFA via FRED" mờ ở 11,0, rõ ở 11,5 | – | Khớp. |
| 6 | 14,45 | "average of many sales" (14,12–14,40) | 14,0: đủ các nhà. 14,5: **các nhà đã biến mất**, không thấy lúc chúng bay vào chồng. | gather 14,45 | **KHÁC Ý ĐỒ, có thể lệch.** Cú "gom" diễn ra trọn trong một khoảng 0,5 s nên người xem thấy một lần biến mất chứ không thấy "nhiều thành một". Âm "gom" có, nhưng hình không cho thấy chuyển động gom. |
| 7 | 16,36–17,0 | "quarter by quarter" | 16,0: nhãn 2000 Q1, 16,5: Q2, 17,0: Q3 | nốt dữ liệu từ 15,8 | Khớp, đây là chỗ đẹp. |
| 8 | 19,76 | "2026" | Đầu đường tới 2026 Q2 ở 20,0 | – | Có thể trễ khoảng 0,25 s, chấp nhận được. |
| 9 | 23,40 / 23,71 | "Here's the cap." | 23,5: đường giá trị và nhà đã tắt, chỉ còn một vạch xám mờ đã nằm sẵn đúng chỗ. **Không thấy xà rơi.** | thud 23,71 (đỉnh sfx khoảng −15 dBFS, ngang lời) | Thud trễ khoảng 0,31 s sau "cap", **ngoài ±0,2 s**. Thud cũng **quá to** (làn sfx gần bằng đỉnh lời). Ý đồ "xà rơi rồi khoá" không đọc ra được. |
| 10 | 25,40 | "$500,000" | Nhãn "$500,000 cap" xuất hiện ở 25,5 | – | Khớp. |
| 11 | 27,20 | "the same in every quarter" | Nhịp sáng: 27,0 ở mép trái, 27,5 ở giữa | (không có trong events) | Khớp về thời điểm, nhưng nhịp sáng chỉ là một vạch trắng vài px. **Không có âm** dù intent ghi "nhịp chạy dọc xà". |
| 12 | 30,00 | "their gain" | "their gain on paper = ?" xuất hiện ở 30,0 | – | Khớp. Có điều đây là **nhãn chữ trong WORLD mode**, trái với quy tắc "nhãn chỉ có ở CHART". |
| 13 | 33,96 | "$200,000" | 34,0: khối đáy chuyển xanh ngọc, có nhãn "what they paid" | **Không có tick** trong events | Hình khớp, **thiếu âm** so với intent. |
| 14 | 35,68 | "grown" | 35,5 chồng bắt đầu cao lên, 36,0 đã cao hết | data note (nằm trong dải 15,8–54,4) | Khớp. |
| 15 | 37,30 | "less" | 37,5–38,0 chồng hạ xuống, 38,5 "what they paid" dạt sang trái | slide_down 37,06 | Âm **sớm 0,24 s** so với chữ "less", ngoài ±0,2 s. Lệch nhẹ. |
| 16 | 43,18 | "under" | Ngoặc "well under" mờ ở 43,0, rõ ở 43,5 | data thưa? | Khớp. **Âm dữ liệu không thưa**: làn data 41–46 s dày, đỉnh khoảng −20 dBFS, ngược với intent "thưa, trầm". |
| 17 | 47,94 | "crosses" | 47,5: đỉnh chạm xà. 48,0: loé + "Over: Q2 2022" | riser 46,28 → chime 47,88 (thấy vạch tần cao khoảng 6–7 kHz trên spectrogram) | **Khớp tốt.** Đây là khoảnh khắc mạnh nhất của đoạn. |
| 18 | 49,30 | "slips" | "Back under" xuất hiện ở 49,5 | data đi xuống | Khớp. **KHÁC Ý ĐỒ:** đoạn dưới xà vẫn có màu vàng/warn (49,5–52), chưa "đổi về ink" (mức tin cậy vừa phải vì 540p). |
| 19 | 51,36–52,38 | "From Q2 2023" | "Stayed over since Q2 2023" xuất hiện ở 51,5, trước khi lời nói tới "2023" | – | Chấp nhận được, vì nhãn đến cùng lúc với "From". |
| 20 | 56,5 | "So, on paper…" | Rosa & Frank hiện lên cạnh nhà ở 56,5 | – | Khớp. |
| 21 | 59,58–60,82 | "this is the gain from the opening" | 59,5: "≈$558,100" nhỏ ở đỉnh. 60,0: đã lớn và nằm trên biển mái | swish 59,75, tick 60,73 | Chuyến bay kết thúc trước 60,0, nên tick 60,73 có thể **trễ khoảng 0,5–0,7 s so với lúc số chạm biển**. Nhãn phụ "their gain on paper" (61,0) **bị hộp số đè lên** và dính vào mái. |
| 22 | 62,06 | "past" | 62,0: nhà nảy lên, có ngoặc "past the cap", câu đối trọng đổi | impact 62,76 (sau "cap" 62,44 là +0,32) | Khớp với ý đồ "impact SAU cap". |
| 23 | 63,4–64,4 | (lặng, rồi "Phoenix" 63,62) | 63,5: **hộp số mờ còn lại một hình chữ nhật xám rỗng** (lỗi fade). Cột tiền xanh lộ ra dưới xà và chạy ra khỏi mép dưới. | whoosh_soft (không có trong events) | **Lỗi render** trong lúc lùi máy. |
| 24 | 65,36 | "3" | "×3.8" xuất hiện ở 65,5 | rise 65,37 | Khớp. Tuy vậy ngoặc **không biểu diễn 3,8 lần** (xem mục 6). |

**Âm có phản ứng với biến động hình không?** Phần lớn có: riser→chime ở 47,9, tick theo nhà, swish số bay, impact sau "cap". Có các ngoại lệ sau:
- (a) Các whoosh chuyển máy/chế độ ghi trong intent (7,5 / 14,8 / 28,1 / 40,9 / 48,2 / 63,4) **không có dòng nào trong events.txt**. Làn sfx có gồ ở khoảng 15–16,5 và khoảng 41, nhưng tôi không xác nhận được đủ cả sáu.
- (b) Thiếu tick lúc khối đổi màu (34,0) và thiếu âm cho nhịp sáng chạy dọc xà (27).
- (c) Thud 23,71 trễ và to.

## 2. Chuyển cảnh và chuyển chế độ

| Mốc | Chuyển | Lý do | Liền mạch? |
|---|---|---|---|
| 7,5–8,6 | pull wHome→wHood | "rise exactly like the index" | **Liền.** Lùi máy mượt, mũi tên giữ chỗ. Có điều lúc lùi khu phố vẫn còn trống, các nhà chỉ hiện sau 9,0, nên ở thời điểm chuyển động thì lý do "thấy khu phố" chưa có trên hình. |
| 14,8–15,9 | mode wHood→cFull | "many sales → one average" | **Gãy nhẹ.** Các nhà biến mất trong một khung (14,0→14,5), rồi 15,0 là một nhà tí hon giữa màn đen, rồi 15,5 là trục đồ thị. Người xem không thấy chồng tiền *trở thành* điểm đầu đường. Lý do đúng, nhưng thiếu cầu nối hình. |
| 28,1–29,1 | mode cFull→wDemo | "And here's their gain" | **Gãy/hoà tan.** 28,0–28,5 là dissolve kép: nhãn "Rosa & Frank" bóng ma nằm giữa đồ thị, xà trần còn vắt ngang cảnh thế giới. Đây là crossfade chứ không phải một máy quay di chuyển trong một thế giới. Chuyển động cũng bắt đầu khoảng 1,2 s trước khi lời nói "their gain" (29,88), tức là lý do đến sau hành động. |
| 40,9–41,9 | mode wDemo→cFull | lãi vừa tách ra | **Gãy/hoà tan**, cùng kiểu với lần trước: 41,0–41,5 có nhãn "their gain on paper / what they paid" mờ chồng lên xà. Lý do là "sự kiện dữ liệu", nhưng hình không cho thấy chồng lãi đi đâu, nên khó hiểu vì sao đường lãi bắt đầu lại từ 2000. |
| 48,2–49,0 | push cFull→cZoom | "slips back under": đoạn 2022–23 quá nhỏ | **Lý do tốt, nhưng gắt.** 48,0 → 48,5 → 49,0 là ba khung bố cục khác hẳn nhau. Nhãn "$500,000 cap" nhảy từ trái sang phải, đường cong biến dạng mạnh, có thể do phối cảnh trong lúc đẩy. Với 0,85 s và khung 0,5 s thì không loại trừ được một cú giật thật sự. |
| 63,4–64,4 | pull cZoom→cFull | cần thấy cả 2000 và 2026 | **Lý do tốt, có lỗi render** (hộp xám rỗng, cột tiền lộ dưới xà ở 63,5). Đồng thời đường lãi đổi sang đường giá mà không có báo hiệu (xem mục 6). |

Kết luận: các cú **push/pull** có lý do rõ và khá liền. Các cú **mode** (3 lần) đều là crossfade có bóng ma chồng hình, không đạt mức "một thế giới, hai chế độ máy". Người xem sẽ cảm nhận là cắt cảnh slide.

## 3. Nhịp

- **Chùng:**
  - **54,5–59,5 s.** Hình gần như đứng yên khoảng 5 s. Lời chạy liên tục 56,04–59,5 (3,5 s) và thay đổi duy nhất là hai người hiện ra ở 56,5. Trước đó còn có khoảng lặng lời 54,4–56,0. Đây là chỗ chùng rõ nhất.
  - **23,5–25,4 s.** Màn hình gần như trống: chỉ có một vạch xám mờ và trục, trong khi lời "Here's the cap. A flat line…". Không đứng yên tới 3 s, nhưng trống ý.
  - **38,5–40,5 s.** Chồng tiền đứng yên trong lúc "less the $200,000 they paid" (2 s). Chấp nhận được.
  - **21,0–22,9 s.** Đồ thị đứng yên, "the latest data" rồi lặng. Chấp nhận được, vì cần chỗ thở.
- **Dồn/rối:**
  - **14,0–15,5.** Gom nhà, chuyển chế độ và hiện trục diễn ra trong khoảng 1,5 s, đúng lúc lời đã qua câu khác.
  - **48,0–49,5.** Chớp "Over", đẩy máy, đổi bố cục và nhãn "Back under" dồn trong khoảng 1,5 s.
  - **59,5–62,5.** Số bay, nhãn phụ, ngoặc "past the cap", đổi câu đối trọng và nhà nảy lên dồn vào 3 s. Đây là cao trào nên dồn là đúng, nhưng chữ thì quá nhiều (xem mục 4).
- Tổng thể: nửa đầu (0–23) đi đều. Đoạn thế giới 29–40 có hành động đúng nhịp lời nhưng nhân vật quá nhỏ nên năng lượng thấp.

## 4. Các lớp bắt buộc

- **ILLUSTRATIVE** (huy hiệu vàng, góc trên phải): có mặt liên tục 0–69. Không đè lên nội dung, ngoại trừ ở 65–69: cột 2026 vươn tới dải trên, sát huy hiệu và tiêu đề.
- **"US only · history, not a forecast"**: có từ 14,5 tới hết. "Source: FHFA via FRED" có từ 11,0 tới hết. Từ 29,0: "A home that rose like the Phoenix average". Từ 62,0, câu đối trọng "A measurement, not a tax bill or a next step": đúng chỗ, xuất hiện ngay khi nói "past the cap".
- **Cỡ chữ:** tôi ước lượng chiều cao chữ của các lớp này vào khoảng 2,5–3 % chiều cao khung (đo trên thumbnail, sai số lớn). Trên điện thoại cầm dọc xem video ngang thì **khó đọc**. Nên nâng lên khoảng ≥ 3,5–4 % và tăng tương phản; hiện chữ trắng xám nằm trên nền gần đen.
- **Chồng chữ / cắt mép:**
  - 30,0–40,5: chữ "Phoenix" trong caption **chạy xuyên qua chân chồng tiền và hai người**.
  - **49,5–59,5: nhãn "Back under" nằm đè lên caption "A home that rose like the Phoenix average"**, cả hai cùng không đọc được.
  - 48,5–63,0: **đường cong trắng của dữ liệu chạy xuyên qua caption** ("the Ph|oenix", "not a|forecast") và ra khỏi mép dưới.
  - 61,0–63,0: nhãn phụ "their gain on paper" bị hộp "≈$558,100" che mất nửa trên.
  - 62,0–63,0: "past the cap" nằm đè lên đường vàng.
  - 64,5–69: nhãn trục "2025" dính vào "2026 Q2" và đọc thành "22026 Q2".
  - 3,0–4,5: dấu "?" bị cắt ở mép trên.

## 5. Âm

- **Lời:** luôn rõ. Đỉnh lời khoảng −8 đến −10 dBFS. Nhạc chủ yếu ở −45 đến −35 (0–44 s) và −30 đến −25 (44–62 s), nên dưới lời khoảng 15–25 dB. Spectrogram cho thấy formant lời không bị phủ.
- **Nhạc theo căng–chùng:** có, ở mức thô. Mức nhạc tăng rõ từ khoảng 44 s ("crosses", tension 0,8), đạt đỉnh khoảng 62 s (1,0), rồi rơi mạnh xuống khoảng −48 ở 63 s (0,45). Tuy vậy, đoạn 0–40 dao động trong khoảng 10 dB, phẳng hơn tension map (0,3→0,55), và không nghe ra bậc ở 23 s (cap) hay 29 s.
- **Khoảng lặng sau "past the cap":** lời dừng 62,6 → 63,62 (khoảng 1,0 s). Nhạc rút từ khoảng 62,9 và impact ở 62,76 lấp phần đầu khoảng lặng. Có "lặng" nhưng ngắn và bị tiếng đuôi của impact làm vơi đi, phần thật sự lặng chỉ khoảng 0,6 s. Nên dời impact sát "cap" (62,5) hoặc bỏ đuôi, để nhạc về sát mức nền phòng khoảng 0,8–1 s.
- **Âm dữ liệu:**
  - 15,8–21 s: nghe được, ở khoảng −30 đến −25, không lấn lời. Tốt.
  - 41–54 s: dày và có đỉnh khoảng −20, sát lời trong những khoảng lời ngắt. Có nguy cơ lấn lời và **trái intent "thưa, trầm"** ở b5.
- **Hiệu ứng thừa/khó chịu:**
  - Thud 23,7 quá to (khoảng −15).
  - 12 tick liên tiếp 9–13 s có nguy cơ lắt nhắt, nên giảm dần biên độ.
  - Nền phòng khoảng −60 ổn.
  - Thiếu âm ở các chỗ intent yêu cầu: tick 34 s, nhịp xà 27 s, và các whoosh chế độ không có trong events.

## 6. 3D: làm ý rõ hơn hay trang trí; phối cảnh có làm sai tỉ lệ dữ liệu không

- **Làm ý rõ hơn:**
  - Chồng tiền dưới nhà (giá trị = chiều cao).
  - Khối đáy đổi màu "what they paid" rồi bị trừ ra (34–38 s). Đây là ý tốt, kiểu 3B1B.
  - Nhà cưỡi đường lãi và xuyên xà (44–48 s). Mạnh.
- **Trang trí hoặc làm yếu ý:**
  - Cảnh WORLD (29–40, 0–14) để nhân vật và chồng tiền chiếm khoảng 10–20 % khung, phía trên là khoảng tối rỗng. Trên điện thoại, hai người chỉ còn vài pixel.
  - Bóng đổ của chồng tiền là một **mảng đen tách rời** trôi bên phải (0–14,5; 29–40), trông như lỗ đen.
  - Mái nhà lơ lửng không thân trong sương (5,5–14,5) khó hiểu.
  - Biển SOLD không đọc được.
- **Sai tỉ lệ / đọc nhầm dữ liệu:**
  1. **×3.8 (65,5–69):** ngoặc trái cao khoảng 47 px, ngoặc phải khoảng 118 px (đo trên khung phóng 66,5), tỉ lệ khoảng 2,5. Chiều cao hai cột tiền cũng chỉ khoảng 3,2 lần. Ngoặc phải còn không chạm đáy. **Hình không biểu diễn đúng 3,8×.** Cột 3D nhìn hơi chếch nên đỉnh và đáy có phối cảnh. Tôi cần đo lại trên bản gốc, nhưng ở 540p con số và hình đang mâu thuẫn.
  2. **64–69 s:** đường GIÁ hiện cùng vạch "$500,000 cap" (mờ), và cuối đường giá chạm đúng mức vạch cap quanh 2025–26. Chính b3 đã tắt nhà để *tránh* đọc nhầm "giá nhà vượt trần", vậy mà b11 lại tạo ra đúng cách đọc nhầm đó. Thêm vào đó, đỉnh cột 2026 cao hơn hẳn điểm cuối của đường giá, nên phá bất biến "vệt đỉnh chồng = đường".
  3. **48,5–63 (cZoom):** đây là phối cảnh chứ không phải chính diện. Xà nằm nghiêng nhẹ, đường cong trắng phía trái chạy xuống dưới khung. Nếu máy đã khoá chính diện đúng như design thì không được có phối cảnh. Cần kiểm tra lại camera cZoom.
  4. 41–42: chuyển từ đường giá trị sang đường LÃI (cùng hình dáng, cùng trục năm), nhưng không có tiêu đề hay nhãn trục y báo "gain", nên người xem dễ tưởng vẫn là giá nhà.

## 7. Chấm điểm (1–5, so với Vox / 3Blue1Brown / WSJ)

| Tiêu chí | Điểm | Lý do chính |
|---|---|---|
| Hình mang nghĩa | **3** | Ý chồng tiền = giá trị, phép trừ, cú xuyên xà đều có nghĩa thật. Nhưng hook thiếu xà, phép gom nhà không thấy, ×3.8 vẽ sai tỉ lệ, cap nằm trên đồ thị giá gây đọc nhầm. |
| Liền mạch hình–lời–âm | **3** | Phần lớn mốc khớp trong khoảng ±0,25, có những khoảnh khắc đẹp (16–17, 47,9, 62). Nhưng cả 3 lần đổi chế độ đều là dissolve có bóng ma, thud trễ và to, slide sớm, tick 60,7 trễ, lỗi hộp xám ở 63,5. |
| Nhịp | **3** | Chùng ở 54,5–59,5 và trống ở 23,5–25,4. Dồn ở 14–15,5 và 48–49,5. Nửa đầu đều nhịp. |
| Âm | **3** | Lời luôn rõ, nhạc có đường lên–rút, khoảng lặng có nhưng ngắn. Âm dữ liệu b5 dày trái ý đồ, thud quá to, thiếu nhiều âm theo intent (whoosh chế độ, tick đổi màu). |

### Năm sửa quan trọng nhất (xếp theo mức ảnh hưởng tới điểm)

1. **64–69 s: sửa đồ thị ×3.8.**
   - Bỏ hẳn vạch "$500,000 cap" khỏi đồ thị giá, hoặc chuyển sang trục y riêng có nhãn.
   - Ngoặc phải đo từ đáy, tỉ lệ đúng 3,8 so với ngoặc trái.
   - Cột phải dùng phép chiếu chính diện (orthographic) và đỉnh cột trùng điểm cuối của đường.
   - Tách "2025" khỏi "2026 Q2".

   Ảnh hưởng: hình mang nghĩa, độ tin cậy.
2. **28,1 / 40,9 / 14,8 s: thay dissolve chế độ bằng một chuyển động máy liên tục.**
   - Máy xoay hoặc nâng về chính diện. Chồng tiền ở vị trí cũ trở thành điểm của đường.
   - Bỏ bóng ma nhãn (28,0; 41,0–41,5).
   - Ở 14,0–14,5, kéo các nhà bay vào chồng trong khoảng ≥ 0,8 s.

   Ảnh hưởng: liền mạch, hình mang nghĩa.
3. **49,5–63 s: dọn chữ.**
   - Dời "Back under" lên trên đường, hoặc đẩy khung lên để đường cong không chui qua caption.
   - Tách nhãn phụ "their gain on paper" ra khỏi hộp số.
   - Nâng các lớp bắt buộc lên khoảng ≥ 3,5–4 % chiều cao khung, đặt trên dải nền tối bán trong suốt.

   Ảnh hưởng: đọc trên điện thoại, mục 4.
4. **0,8–3,6 s và 23,4 s: hiện xà trần ngay ở hook.**
   - Hook: xà trần mờ phía trên nhà, dấu "?" lớn đặt giữa mái và xà, không bị cắt mép.
   - 23,4 s: cho xà rơi thật, khoá đúng chữ "cap" (23,40). Thud dời về khoảng 23,45 và giảm khoảng 8–10 dB.

   Ảnh hưởng: hình mang nghĩa, liền mạch.
5. **54,5–59,5 s (chùng) và âm dữ liệu 41–54 s.**
   - Trong "So, on paper, if their home rose like the Phoenix average…", cho máy đẩy nhẹ hoặc trượt dọc đường lãi về nhà, hoặc cho con số bắt đầu "đếm" từ đỉnh chồng.
   - Làm âm dữ liệu b5 thưa và trầm, hạ khoảng 6 dB khi có lời.
   - Sau "cap" (62,44), đặt impact sát chữ, rồi cho nhạc về gần mức nền phòng trong khoảng 1 s.

   Ảnh hưởng: nhịp, âm.
