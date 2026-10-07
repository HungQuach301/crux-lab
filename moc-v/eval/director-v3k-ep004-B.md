# Đánh giá đạo diễn — V3k, ep004, đoạn B (0–69 s, bản xem trước 540p)

Nguồn đã xem: sheet-1/2 (khung 0,5 s), audio.png, transcript.txt, events.txt, intent.txt. Một khung thấy ở t nghĩa là sự kiện xảy ra trong (t−0,5; t]. Mình chỉ gọi là "lệch" khi khung chứng minh được lệch vượt quá sai số đó. Kích thước chữ quy về 1080p theo hệ số 6.

## 1. Lệch hình / lời / âm, và chỗ hình khác ý đồ

### 1a. Đồng bộ theo từ khoá (chuẩn ±0,2 s, sai số khung 0,5 s)

| Cue | Lời (onset) | Khung đầu tiên thấy | Kết luận |
|---|---|---|---|
| has → xà trần | 2,06 | 2,5 (2,0 chưa có) | trong sai số |
| q → "?" | 3,18 | 3,5 (3,0 chưa có) | trong sai số |
| blur → sương | 4,96 | 5,5 (5,0 còn nét) | trong sai số. Nếu sương dâng dần thì có thể trễ 0,2–0,5 s, khung không chứng minh được |
| rise → mũi tên | 7,18 | 7,5 | khớp |
| pull 7,53–8,63 | — | 8,0 giữa chừng, 8,5 thấy khu phố | khớp |
| pop0 + 6 tick SOLD | 8,98 → 13,37 | biển SOLD tăng dần 9,5→13,5; biển lớn ở 13,5 | khớp. Biển quá nhỏ nên không đếm được từng tick bằng mắt |
| src → "Source: FHFA via FRED" | 11,21 | 11,5 | khớp |
| avg/gather | 14,45 | 14,5 có chữ "many sales → one average", 15,0 các nhà gom lên trên | khớp |
| mode → chart | 14,82–15,87 | 15,5 còn một chồng, 16,0 có trục | khớp |
| quarter (3 bước quý) | 16,24 | 2000 Q1 / Q2 / Q3 lần lượt ở 16,5 / 17,0 / 17,5 | khớp, nhịp từng bước đúng ý |
| y2026 | 19,69 | 19,5 nhãn "2022", 20,0 nhãn "2026 Q2" | khớp |
| cap → xà rơi + thud | 23,36 / 23,66 | 23,5 xà đang rơi, 24,0 xà đã khoá | khớp |
| flat → vệt sáng | 24,58 | 25,0 | khớp |
| five → "$500,000 cap" | 25,37 | 25,5 | khớp |
| same → cột mốc | 27,18 | 27,5 (mọc dần tới 28,5) | khớp |
| gain → "their gain on paper = ?" | 30,01 | 30,5 | khớp |
| two → khối teal | 33,94 | 34,0 nhạt, 34,5 rõ | khớp |
| grow | 35,89 | 36,0 bắt đầu, 36,5 cao hẳn | khớp |
| less → khối trượt | 37,30 | 37,5 | khớp |
| paid → ngoặc | 39,58 | 40,0 | khớp |
| under → "well under" | 43,23 | 43,5 | khớp |
| push cZoom | 46,06–47,26 | 46,5 / 47,0 đang đẩy | khớp |
| cross → loé + "Over: Q2 2022" + chime | 47,88 | 48,0 | khớp |
| slips → "Back under" | 49,28 | 49,5 | khớp |
| stay/lbl → "Stayed over since Q2 2023" | 51,38 / 51,53 | 52,0 (51,5 chưa có) | trong sai số, nhưng ở mép trễ: cue 51,53, thấy ở 52,0. Nên kiểm lại ở 30 fps |
| rose → mũi tên | 58,02 | 58,0 mờ, 58,5 rõ | khớp |
| fly / land → "≈ $558,100" | 59,76 / 60,73 | 60,0 ở đầu đường, 60,5 đang bay, 61,0 đã đậu | khớp |
| past/cap → ngoặc "past the cap" | 62,01 / 62,44 | 62,5 đủ ngoặc (62,0 chưa có) | khớp |
| Phoenix → đổi đại lượng + pull | 63,62 | 64,0 đường đang nâng, xà và nhãn tắt | khớp |
| x → "×1 / ×3.8" | 65,37 | 65,5 | khớp |

Âm: riser kéo từ 2,06 tới "cap?" (đỉnh khoảng 3,2), tick, thud, chime ở 47,88, land ở 62,58 và nốt dữ liệu ở 65,4 đều thấy trên lớp sfx/data đúng mốc. **Không có chỗ lệch hình–lời–âm nào mà khung chứng minh được.** Đây là điểm mạnh nhất của bản này.

### 1b. Chỗ hình khác ý đồ

1. **23,5 s: đọc nhầm "giá nhà vượt trần".** Xà trần đã ở trong khung nhưng đường giá trị và chồng 2026 vẫn còn. Đỉnh đường giá trị (khoảng $760k) nằm rõ phía trên xà. Đây đúng là cách đọc mà intent b3 muốn tránh. Đường giá trị chỉ tắt ở 24,0, tức là có ≥ 1 khung sai nghĩa. Cần tắt đường giá trị **trước** khi xà vào khung, ở khoảng 22,9 s lúc nói "Here's".
2. **66,0–69,0 s: chồng giá 2000 sai chiều cao.** Ngoặc "×1" cao khoảng 72 px (đo trên khung phóng) và khớp với điểm đầu đường giá. Nhưng chồng teal năm 2000 chỉ cao khoảng 40 px, bằng 0,55 lần giá trị đúng. Chồng 2026 thì khớp: đỉnh trùng đầu đường, phần teal đáy cũng 72 px. Ghi chú thiết kế yêu cầu "đỉnh chồng là điểm dữ liệu", nên ở đây ai so hai chồng sẽ thấy ×6,8 thay vì ×3,8 (xem mục 6).
3. **0–5 s và 29,5–35 s: cùng $200,000 mà hai tỉ lệ.** Ở 0 s chồng $200k dưới nhà chỉ cao khoảng 0,37 lần chiều cao nhà. Từ 29,5 s, khối $200k ("what they paid") cao khoảng 1,1–1,2 lần nhà. Cùng một đại lượng trong cùng một thế giới nhưng tỉ lệ khác nhau. Intent b0 cũng ghi "chồng tiền $200,000" mà hình mở đầu chỉ là một bệ thấp, không đọc ra là tiền.
4. **14,5–15,0 s: các nhà không bay "vào" chồng.** Intent muốn các nhà bay vào chồng tiền của nhà chính (= trung bình). Trên hình, chúng gom thành một dải nổi **phía trên** mái nhà chính rồi biến mất ở 15,5. Ý "trung bình" không thành hình.
5. **41,5–42,0 s: "tua nhà về 2000" thành cross-fade.** Ở 42,0 vẫn thấy bóng mờ của chồng 2026 cao, đang tan, cạnh chồng nhỏ ở 2000. Ghi chú thiết kế cấm cross-fade vật thể thế giới và yêu cầu morph nhà vào đỉnh chồng. Ở đây nhà biến mất giữa 41,5 và 42,0, không thấy co vào đỉnh chồng.
6. **58,0–59,5 s: mũi tên "rose" lơ lửng.** Intent viết "mũi tên cạnh nhà, cùng mũi tên của b1", nhưng ở chế độ đồ thị không còn nhà. Mũi tên xanh đứng một mình giữa khoảng trống phía trên-phải đầu đường, nên không còn gắn với vật nào và không mang nghĩa.
7. **55–57 s: lý do đẩy máy "vào nhà ở đầu đường" mâu thuẫn với ghi chú thiết kế** (đồ thị không có nhà). Hình thực tế đẩy vào đỉnh chồng, vậy là đúng. Chỉ có lời giải thích trong intent là sai.
8. **Badge "ILLUSTRATIVE" nằm suốt cả các cảnh đồ thị dữ liệu thật FHFA** (15,5–69 s). Badge này đúng cho Rosa & Frank, nhưng đặt trên chuỗi chỉ số thật thì làm người xem nghi ngờ số liệu. Nên chỉ để badge ở chế độ WORLD, hoặc đổi thành "Hypothetical couple".

## 2. Chuyển cảnh và chuyển chế độ

| Mốc | Chuyển | Lý do có hợp với lời không | Liền / gãy |
|---|---|---|---|
| 7,53–8,63 | pull nhà → khu phố | hợp: "exactly like the index" mở sang nhiều nhà | **Liền** |
| 14,82–15,87 | WORLD → CHART | hợp: "an average of many sales" | **Gần liền**: chồng mảnh có nhà tí hon trên đỉnh (15,5) rồi thành điểm dữ liệu (16,0). Nhưng khu phố và Rosa & Frank chỉ tối/biến mất chứ không thấy đi đâu |
| 28,76–29,76 | CHART → WORLD | hợp: "And here's THEIR gain" | **Liền nhờ xà trần**: xà nằm trong cả hai chế độ, ở 29,0 vẫn là cùng một đường. Đây là mối nối tốt nhất đoạn. Nhưng các cột mốc "same in every quarter" và nhãn trục chỉ tắt chứ không chuyển |
| 30,67–33,27 | push vào nhà | yếu: chỉ để "nhìn kỹ", không lộ thêm thông tin gì | liền, hơi thừa |
| 34,47–35,37 | pull để thấy trọn chồng sắp cao gấp 4 | hợp, có lý do tốt | liền. Có điều push rồi pull cách nhau 1,2 s nên máy "thở" hai lần cho một ý |
| 41,14–42,14 | WORLD → CHART, tua về 2000 | hợp | **GÃY nhẹ**: cross-fade (bóng chồng 2026 ở 42,0), người và nhà biến mất chứ không morph |
| 46,06–47,26 | push cFull → cZoom | rất hợp: đoạn 2021–26 quá nhỏ, đẩy **trước** điểm cắt | liền. Có thước $600k/$400k. Lưu ý ở 47,0 khoảng $600k→cap (110 px) khác cap→$400k (86 px), nên thước không đều khi máy đang di chuyển. Nếu máy nghiêng chứ không thuần dolly thì đây là lỗi chế độ CHART "front-on" |
| 55,13–57,33 | push cZoom → cTip | hợp: con số sắp nói | liền. Nhãn "$500,000 cap" nhảy chỗ (56,0) |
| 63,56–65,01 | pull cTip → cFull và đổi lãi→giá | hợp: cần cả hai đầu 2000/2026 | **Liền nhưng dồn**: đổi đại lượng, đổi màu (vàng→trắng→xanh), tắt xà, hiện tiêu đề và lùi máy cùng lúc trong 1,5 s. Đường "nâng đúng $200,000" không đọc ra được vì máy đang lùi, nên phép nâng bị chìm vào chuyển động máy |

Tóm lại logic máy rất rõ: chỉ di chuyển giữa các từ khoá, mỗi lần có lý do và có âm. Xà trần là sợi chỉ nối hai chế độ, làm tốt. Chỗ gãy nằm ở hai lần vào CHART (15 s, 42 s): vật thể thế giới biến mất hoặc mờ đi thay vì morph như ghi chú thiết kế cam kết.

## 3. Nhịp

**Chỗ chùng** (hình gần đứng yên trong khi lời chạy):
- **9,5–14,0 s, khoảng 4,5 s.** Lời đọc tên dài "Phoenix Area Home Price Index from the Federal Housing Finance Agency". Hình chỉ thay đổi bằng những biển SOLD rất nhỏ; các khung 10,0–13,0 gần như giống hệt nhau. Theo tiêu chí ">3 s" thì đây là **chỗ chùng duy nhất đạt ngưỡng**. Nên cho máy trôi chậm dọc khu phố, hoặc cho biển SOLD to và rõ (mỗi tick một nhà sáng lên).
- 20,0–23,0 s: đường giá trị đã vẽ xong và đứng 3 s. Lời chỉ chạy khoảng 1,8 s ("the latest data") rồi nghỉ, nên chưa vượt ngưỡng nhưng cảm giác hơi đứng.
- 66,0–69,0 s: đứng 3 s, lời 66,0–68,0. Đây là khung kết luận nên chấp nhận được.

**Chỗ dồn / rối:**
- **41–48 s:** về chế độ đồ thị, tua, "well under", push rồi cắt, tất cả trong 7 s. Từng sự kiện đều có lý do nhưng không có nhịp thở trước điểm cắt. Riser ở 44,9 bắt đầu lúc máy chưa đẩy.
- **56–66 s:** push, mũi tên, nhãn lịch sử rời khung, số bay, ngoặc, lặng, đổi đại lượng + pull + tiêu đề + ×1/×3.8. Đây là vùng nặng nhất. Đặc biệt 63,6–65,5 s có năm thay đổi đồng thời (xem mục 2).
- 52,0–56,0 s: bốn nhãn ("$500,000 cap", "Over", "Back under", "Stayed over") cùng nằm ở 60% bên trái khung zoom, rối mắt.

## 4. Lớp bắt buộc (nguồn, nhãn, chú thích) và chữ

- **Đọc được trên điện thoại:** "Source: FHFA via FRED", chú thích đáy và các nhãn vàng (Over / Back under / Stayed over / "past the cap") khoảng 40–50 px ở 1080p, đọc tốt. **Yếu:** "$600k/$400k" (khoảng 30 px, xám mờ), năm trên trục (khoảng 34 px, xám), "what they paid" (teal trên nền tối, tương phản thấp), "many sales → one average" (xám, mờ dần), "Rosa & Frank · Phoenix" (khoảng 36 px).
- **Chữ chồng:**
  - 18,0–19,0 s: nhãn năm chạy theo đầu đường đè lên nhãn "home value" ("home 2004", "home value 2010", "home value 2016"). Lỗi rõ nhất.
  - 30,0–32,0 s: xà trần thế giới chạy sát hoặc gạch ngang dòng "Source: FHFA via FRED" (rõ ở 31,5).
  - 40,0–41,0 s: "their gain on paper" và "Rosa & Frank" xếp sát nhau, chữ chạm ngoặc.
  - 52,0–56,0 s: đường lãi cắt qua nhãn "Back under".
  - 56,0 s: nhãn "$500,000 cap" chạm đường vàng.
  - 59,5 s: "Stayed over since Q2 2023" bị đường vàng chạy xuyên và bị chồng che mất phần "Q2 2023".
  - 60,5–63,5 s: hộp "≈ $558,100" nằm đúng trên vạch $600k nên dễ hiểu nhầm là con số ở mức $600k.
- **Đè hình:** chú thích đáy ("A measurement, not a tax bill or a next step") đè lên chân chồng tiền ở 47,0 s và 60–63,5 s. Có gradient nhưng chân chồng bị cắt.
- **Cắt mép:** đường lãi tràn mép trái khung zoom (48–63 s). Chấp nhận được vì là zoom. "2026 Q2" ở 20,0–23,5 sát mép trên vùng đồ thị nhưng không bị cắt.
- Chú thích đáy đổi từ "not a next step" sang "not a tax bill or a next step" ở 60,0 mà không gắn với từ khoá nào. Nên đổi sau một nhịp lời.

## 5. Âm

- **Lời rõ.** Đỉnh giọng khoảng −10…−5 dBFS, nhạc −45…−30, dữ liệu −35…−22: cách nhau ≥ 15–20 dB. Phổ không thấy dải nào lấn vùng formant giọng.
- **Nhạc theo căng–chùng: tốt.** Mức nhạc tăng từ khoảng −45 (0–15 s) lên khoảng −30…−25 (44–62 s), bám bản đồ 0,3 → 1,0. Thấy accent quanh 23,8 và 47,9.
- **Khoảng lặng sau "past the cap": có, và đúng chỗ.** Nhạc tắt khoảng 62,45–62,7 (stop 62,44, tau 0,08). Lặng thật (không giọng, không nhạc) khoảng 62,8–63,56, khoảng 0,8 s, chỉ có room tone và đuôi "land" (62,58). Nhạc quay lại khoảng 65,3, tức là giọng nói "Phoenix area prices are now almost" (khoảng 1,7 s) không có nhạc. Đây là quyết định hợp lý và đúng music plan (release 65,373), dù intent b10 viết "lặng ~1 s tới Phoenix". Có một lỗi: whoosh_air ở 63,56 trùng đúng onset "Phoenix", nên khoảng lặng kết bằng một tiếng gió chứ không bằng giọng. Nên bỏ whoosh này hoặc lùi nó sau 64,0.
- **Âm dữ liệu:** 16–21 s nốt theo giá trị, hợp. 43–62 s nốt dày, có lúc to ngang nhạc (−22 dB). 65,4 có đúng một nốt lên một quãng, rất đẹp. Tuy vậy 51 nốt trong khoảng 49 s là dày, khó nghe ra "đường". Nên thưa hơn và chỉ nhấn ở điểm cắt.
- **Hiệu ứng thừa:** 29 sự kiện sfx trong 68 s; lần di chuyển máy nào cũng có whoosh, mỗi lần đổi chế độ là cặp whoosh_mode + land. Thừa cụ thể: whoosh_air 30,67 (push không mang thông tin), whoosh_air 34,47 (pull ngay sau push), whoosh_air 63,56 (phá lặng). Vox và 3Blue1Brown dùng ít hơn nhiều; ở đây tai bắt đầu đoán trước được tiếng gió.

## 6. 3D: làm ý rõ hơn hay chỉ trang trí

**Làm ý rõ hơn:**
- Chồng tiền là đại lượng. Khối teal "what they paid" đổi màu, chồng lớn, khối đáy trượt ra và ngoặc "their gain on paper" (33,9–40,0 s) là một phép trừ trực quan thật, đúng tinh thần 3Blue1Brown. Đã kiểm tỉ lệ ở 36,5 s: chồng / teal ≈ 3,7 (đúng ×3,8). Ở 40,5 s: lãi / teal ≈ 2,9 (đúng 558/200 ≈ 2,8). Xà trần ở thế giới nằm đúng mức $500k so với chồng.
- Xà trần nối hai chế độ: giữ nghĩa xuyên cảnh.
- Ở 61,0 s, đỉnh chồng trên xà (khoảng 30 px so với 52 px/$100k) đúng bằng $58k. Phần vượt trần tô vàng, đọc ngay ra "past the cap".

**Chỉ trang trí hoặc làm yếu ý:**
- Khu phố low-poly (9–14 s) chỉ để minh hoạ "many sales", biển SOLD quá nhỏ để mang nghĩa.
- Mũi tên xanh ở 58–59,5 s lơ lửng.
- Push 30,7–33,3 s.

**Phối cảnh làm sai tỉ lệ dữ liệu, có ở ba chỗ:**
1. 66–69 s: chồng 2000 chỉ cao khoảng 0,55 lần mức đúng. Đây là lỗi nghiêm trọng nhất: chính khung kết luận "×3.8" lại hiện hai chồng chênh khoảng ×6,8. Có thể do chồng 2000 nằm sâu hơn trong không gian 3D hoặc bị thu nhỏ. Phải đặt nó cùng mặt phẳng và cùng thang với chồng 2026.
2. 0 s so với 30 s: cùng $200k nhưng hai chiều cao (so với nhà).
3. 47,0 s: thước $600k/$400k không cách đều quanh cap (110 so với 86 px) trong lúc đẩy máy. Nếu do máy nghiêng thì vi phạm "CHART = front-on".

## 7. Chấm điểm (so với Vox / 3Blue1Brown / WSJ)

| Tiêu chí | Điểm | Lý do ngắn |
|---|---|---|
| Hình mang nghĩa | **3** | Phép trừ bằng chồng tiền và xà trần là ý tốt. Nhưng chồng 2000 sai thang ở khung kết luận, khung 23,5 s đọc nhầm, mũi tên lơ lửng, khu phố chỉ trang trí, badge ILLUSTRATIVE đặt trên dữ liệu thật |
| Liền mạch hình–lời–âm | **3,5** | Đồng bộ từ khoá gần như hoàn hảo (không lệch nào chứng minh được). Bị trừ vì cross-fade 42 s, vật thế giới biến mất ở 15 s, nhãn đè nhau (18–19 s, 52–59 s) và whoosh phá lặng ở 63,56 |
| Nhịp | **3** | Chùng 9,5–14 s. Dồn 41–48 s và đặc biệt 63,6–65,5 s (năm thay đổi cùng lúc). Push rồi pull liền nhau ở 30–35 s |
| Âm | **3,5** | Lời rõ, nhạc bám căng–chùng, lặng sau "cap" đúng chỗ. Nhưng sfx quá dày (whoosh mỗi lần di chuyển), nốt dữ liệu dày tới mức không nghe ra đường, whoosh 63,56 cắt khoảng lặng |

### Năm sửa quan trọng nhất
1. **66,0–69,0 s:** đặt chồng 2000 cùng mặt phẳng và cùng thang với chồng 2026, sao cho đỉnh của nó = điểm đầu đường = ngoặc ×1. Đây là con số kết luận của cả đoạn.
2. **22,9–23,5 s:** tắt đường giá trị và chồng 2026 trên chữ "Here's" (22,94), **trước** khi xà vào khung, để không có khung nào gợi "giá nhà vượt trần".
3. **63,56–65,5 s:** tách hai động tác. Lùi máy trước (63,6–64,4), sau đó mới nâng đường lãi lên $200k có ngoặc "+ what they paid" (64,4–65,3), rồi ×1/×3.8 ở 65,37. Bỏ whoosh_air ở 63,56 để khoảng lặng kết bằng chữ "Phoenix".
4. **18,0–19,5 s và 52–60 s:** xử lý va chạm nhãn. Nhãn năm đặt dưới đầu đường hoặc ẩn "home value" khi nhãn năm chạy. Dời "Back under" ra dưới đường. Rút "Stayed over…" trước 59,0 hoặc đặt nó trên cao tránh chồng. Dời hộp "≈ $558,100" khỏi vạch $600k.
5. **9,5–14,0 s và 41,1–42,1 s:** ở khu phố, cho mỗi tick một nhà sáng lên và biển SOLD đủ to (hoặc máy trôi chậm) để hết chùng. Khi vào chế độ đồ thị, làm đúng morph nhà→đỉnh chồng và chồng 2026 tua co về 2000 bằng chuyển động thay vì cross-fade.
