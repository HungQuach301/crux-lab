# Đạo diễn duyệt V3f — ep004 (đoạn 0–70 s, bản xem trước 540p)

Nguồn đã xem: sheet-1/2 (khung 0,5 s), audio.png, transcript.txt, events.txt, intent.txt.
Quy ước: sự kiện thấy lần đầu ở khung t thì xảy ra trong (t−0,5; t]. "Lệch" chỉ được ghi khi khung chứng minh vượt ±0,2 s.

## 1. Đồng bộ hình / lời / âm

| Mốc lời (ASR) | Ý đồ | Thấy ở khung | Kết luận |
|---|---|---|---|
| "Has" 2,08 | xà trần hiện | 2,0 (không có ở 1,5) | Khớp (sai số khung 0–0,5 s) |
| "cap?" 3,20 | dấu hỏi | 3,0 (không có ở 2,5) | Sớm 0,2–0,7 s, ở ngưỡng, **không chứng minh được** là lệch |
| sương 4,96 | nhà mờ | 5,0 | Khớp |
| "rise" 7,04 | mũi tên đi lên | 7,0 | Khớp (mũi tên ra đúng chữ) |
| pull 7,53–8,63 | lùi máy ra khu phố | 7,5→8,5 | Khớp, máy đi giữa hai từ khoá |
| pop0 8,98 | biển SOLD đầu tiên | 9,0 | Khớp. Lưu ý: tới 9,0 đã có ≥2 nhà có biển, tick thì 0,88 s một cái, nên "một tick cho một nhà" khó thấy |
| "Federal" 11,32 | Source | 11,0 mờ, 11,5 rõ | Khớp |
| "many" 14,12 | nhãn "many sales → one average" | 14,0 | Khớp |
| "average/sales" 14,45 | nhà bay vào chồng | 14,5 | Khớp |
| "quarter by quarter" 16,34–16,76 | 2000 Q1/Q2/Q3 nhảy từng bước | 16,0 / 16,5 / 17,0 | Khớp, đây là chỗ đẹp nhất phần đầu |
| "2026" 19,76 | nhãn 2026 Q2 | 20,0 | Khớp |
| "cap" 23,40 | xà xuất hiện, đường giá trị tắt | 23,5 | Khớp. Không thấy xà **rơi** (23,5 và 24,0 cùng độ cao), nên tiếng thud 23,96 không có hình "khoá" tương ứng |
| "$500,000" 25,40 | nhãn "$500,000 cap" | 25,5 | Khớp |
| "same" 27,20 | nhịp sáng chạy dọc xà | 27,0 (không có ở 26,5) | Sớm 0–0,7 s, ở ngưỡng |
| "their gain" 30,00 | "their gain on paper = ?" | 30,0 | Khớp |
| "$200,000" 33,96 | khối đáy đổi teal | 34,0 | Khớp |
| "grown" 35,72 | chồng lớn lên | 36,0 | Khớp |
| "less" 37,30 | khối trượt sang phải, chồng hạ | 37,5 | Khớp |
| "paid" 39,58 | ngoặc "their gain on paper" (bỏ "= ?") | 39,5 | Khớp |
| "under" 43,18 | ngoặc "well under" | 43,5 | Khớp |
| "crosses" 47,94 | loé + "Over: Q2 2022" | 48,0 | Khớp; chime 47,88 trùng |
| "slips" 49,30 | "Back under" | 49,5 | Khớp |
| "From…" 51,34 (nhưng "2023" ở 52,38) | "Stayed over since Q2 2023" | 51,5 | Đúng cue, nhưng chữ "Q2 2023" lên **trước lời ~0,9 s**: mắt đọc trước tai |
| "rose" 58,04 | mũi tên cạnh nhà | 58,0 | Khớp |
| "this" 59,60 | số ≈ $558,100 bay | 60,0 | Khớp |
| "past" 62,06 | ngoặc "past the cap" | 62,0 | Khớp (có thể lên trước chữ "past" vài chục ms) |
| "cap" 62,44 → "Phoenix" 63,62 | nhạc tắt, lặng | audio: nhạc hết ≈62,6, lời lại 63,62 | Khớp, lặng ≈0,9–1,0 s |
| pull 64,12 | đổi đại lượng lãi → giá | 64,5 | Khớp |
| "3" 65,36 | ×1 / ×3,8 | 65,5 | Khớp |

**Âm có phản ứng đúng lúc không:** có. Mỗi sự kiện trong events.txt rơi vào đúng khung có thay đổi hình (tick SOLD, gather 14,45, chime 47,88, swish 59,76, land 62,58). Ngoại lệ: thud 23,96 không có hình xà rơi/khoá để bám vào.

**Hình khác ý đồ:**
- b0 (2–4,5 s): xà trần vẽ **nghiêng** vài độ do phối cảnh. 20 s sau lời nói "a flat line", nên hình đầu tiên của xà mâu thuẫn với định nghĩa của chính nó.
- b3 (23,5–29): không thấy xà "rơi và khoá"; xà được vẽ dần từ trái sang. Đường giá trị, chồng và nhà biến mất bằng **mờ dần** (23,5 còn mờ), trái nguyên tắc "không cross-fade".
- b4 (36,5–37,0): đỉnh chồng và **mái nhà bị cắt ở mép trên khung**. Lần lùi máy 34,47 nói là "để thấy trọn" nhưng chưa lùi đủ.
- b8: ý đồ là "ba nhãn giữ tới khi số bay" (59,76), nhưng "Over"/"Back under" tắt ở 55,5 (lúc bắt đầu đẩy máy) và "Stayed over" tắt ở 59,5. Trạng thái kết luận không được giữ.
- b9: ý đồ có "Rosa & Frank đứng cạnh nhà", nhưng từ 56 đến 64 s không thấy người. Số không đáp lên "biển trên mái": ô số dừng phía trên-trái đỉnh chồng, không thấy biển.
- b10: không thấy nhà "nảy qua xà" (61,5–63,0 nhà đứng yên). Có thể cú nảy ngắn hơn 0,5 s nên rơi giữa hai khung, nhưng không chứng minh được là nó có.
- b11: chưa thấy rõ khối teal "what they paid" trở về đáy chồng 2026 (ý "lãi + đã trả = giá"), nên bước nối giữa hai đại lượng không được trình bày.

## 2. Chuyển cảnh và chuyển chế độ

| Mốc | Chuyển | Lý do | Đánh giá |
|---|---|---|---|
| 7,53 | pull wHome→wHood | "index" = nhiều giao dịch | Liền, có lý do. Tốt |
| 14,82 | WORLD→CHART | nhiều nhà → một đường | Liền: nhà bay vào chồng (14,5), máy đi tới, chồng thành điểm 2000 (15,5). Tốt nhất phim |
| 23,4 | trong CHART: giá trị → trần | tránh đọc nhầm | **Gãy nhẹ**: mọi vật thể mờ đi, còn lại khung trống chỉ có một xà. Thế giới "biến mất" chứ máy không đi |
| 28,76 | CHART→WORLD | "their gain" | Liền: 29,0 thấy xà thành đường chân trời, nhà ở xa. Tốt |
| 30,67 push / 34,47 pull | đẩy vào nhà rồi lùi | ẩn dụ đo, chồng cao lên | Có lý do, nhưng lùi chưa đủ nên mép trên bị cắt (36,5–37,0), rồi 37,5 khung lại "nhảy" xuống. **Gãy** |
| 41,14 | WORLD→CHART | tua về 2000 | Liền ở 41,5 nhưng người và khối teal biến mất không có lời giải thích; chấp nhận được |
| 46,06 | push cFull→cZoom | sắp tới điểm cắt | Đúng lý do; ở 46,5 mọi nhãn tắt rồi lên lại ở 47,0, gây nháy nhãn |
| 55,13 | push cZoom→cTip | con số của họ | Có lý do; làm rơi nhãn kết luận (xem trên) |
| 64,12 | pull cTip→cFull, lãi→giá | cần hai đầu 2000/2026 | **Gãy**: trong một khung (64,0→64,5) đường lãi, xà, số $558,100 và "past the cap" biến mất cùng lúc, chồng 2000 mọc lên sau đó. Đổi đại lượng mà không có cầu nối hình |

## 3. Nhịp

**Chỗ chùng** (hình đứng yên khi lời chạy):
- 20,0–23,0: đồ thị đứng yên ~3 s ("the latest data" và 1,4 s nghỉ). Ở ngưỡng.
- 51,5–55,0: ba nhãn đứng yên khoảng 3,5 s trong lúc nói "…2023, it has stayed above". Đường đã chạm 2026 từ 52,0, không có chuyển động mang nghĩa. **Chùng**.
- 66,0–69,0: cảnh kết đứng yên. Có thể chấp nhận vì là khung giữ ở cuối.

**Chỗ dồn/rối:**
- 14,0–15,5: nhãn "many sales → one average", nhà bay, đổi chế độ và dòng "US only" lên cùng lúc trong 1,5 s.
- 48,0–55,0: "Over: Q2 2022", "$500,000 cap", "Back under" chồng sát nhau trong vùng khoảng 60 px quanh đỉnh, cạnh nhà và chồng. Trên điện thoại đây là một cụm chữ.
- 59,5–62,5: số bay, nhãn "their gain on paper", ngoặc "past the cap" và dòng đối trọng đổi ("…tax bill or a next step") ở 60,0, trong 3 s. Mắt bị kéo xuống chân khung đúng lúc cần nhìn con số.

## 4. Lớp bắt buộc

- **ILLUSTRATIVE**: có ở mọi khung, góc phải trên, không đè hình. Nhưng chữ rất nhỏ (cao khoảng 7–8 px ở 540p), trên điện thoại chỉ đọc được như một vệt vàng.
- **Nguồn** "Source: FHFA via FRED": từ 11,0 tới hết, góc trái trên, chữ nhỏ và mảnh, xám trên nền tối. Khó đọc trên điện thoại.
- **History-not-forecast** "US only · history, not a forecast": từ 14,5, chân trái. Cùng vấn đề cỡ chữ.
- **Đối trọng** "A measurement, not a (tax bill or a) next step": từ 42,5. Tốt về nội dung. Câu đổi ở 60,0 đúng lúc cao trào nên gây phân tán.
- Từ 31,5 chân khung có hai dòng chồng nhau ("A home that rose…" + "US only…"). Không đè nhau nhưng sát.
- **Chữ chồng / cắt mép:**
  - 36,5–37,0: mái nhà bị cắt mép trên.
  - 49,0–55,0: "Back under" sát "$500,000 cap".
  - 55,0–58,0: "$500,000 cap" trôi vào sát chồng tiền và nằm dưới đường lãi.
  - 65,5–69,0: "×1" chỉ cách mép trái khoảng 15–20 px.
  - Ở chế độ zoom (47–64) đường lãi và xà chạy ra khỏi mép trái. Có chủ ý, không lỗi.
- "what they paid" (teal trên nền tối, chữ nhỏ): tương phản thấp.

## 5. Âm

- **Lời luôn rõ**: đỉnh lời khoảng −5…−10 dBFS. Nhạc ở −40…−45 tới khoảng 40 s rồi lên −25…−30 ở 44–62 s. Lời vẫn trội 15–20 dB, phổ không thấy lời bị che.
- **Nhạc theo căng–chùng**: có hướng đúng. Đoạn đầu thấp, 44–62 cao hơn khoảng 12 dB, tắt ở "cap", trở lại khoảng −45 ở 65. Tuy vậy, đoạn 15–40 s (tension 0,35→0,55) gần như phẳng trên biểu đồ mức, nên biên độ chưa thể hiện được hai lần nhấn 23,86 và 47,88 ngoài tiếng sfx.
- **Khoảng lặng sau "past the cap"**: có, khoảng 0,9–1,0 s (62,6–63,6), giữ room tone, có tiếng "land" mềm 62,58. Làm đúng ý đồ, đây là điểm mạnh.
- **Âm dữ liệu**: nghe thấy ở 16–21 s (đỉnh khoảng −25…−30) và 43–54 s (−30…−45). Không lấn lời; ở 17–20 nó gần nhất (cách lời khoảng 15 dB). Đạt.
- **Hiệu ứng thừa/khó chịu**:
  - Thud 23,96 đạt khoảng −20 dBFS trên mix, ngang mức lời, và không có hình xà khoá đi kèm. Nên hạ 6 dB hoặc gắn với hình.
  - Riser 46,28 chạy dưới câu "in the second quarter of 2022, it crosses" ở khoảng −25…−30. Chấp nhận được nhưng dày.
  - Có 8 lần whoosh trong 70 s, hơi nhiều so với phong cách Vox/3B1B.

## 6. 3D

- **Làm ý rõ hơn**:
  - Khu phố → các nhà bay vào một chồng (14,5): 3D có nghĩa thật.
  - Phép trừ "grown − paid" bằng khối teal trượt ra (34–39,5) là ẩn dụ thể tích dễ hiểu.
  - Nhà đi theo đường lãi (42–46) gắn người với dữ liệu.
- **Trang trí / gây nhiễu**:
  - Nhà đứng cạnh chồng ở chế độ CHART (48–64) có mái **chạm/vượt qua xà $500,000**. Chính b3 tắt nhà để "tránh đọc nhầm 'giá nhà vượt trần'", nhưng từ 48 s trở đi hình lại gợi đúng cách đọc nhầm đó.
  - Sương ở 5–7 s làm mất người. Chấp nhận được.
- **Phối cảnh và tỉ lệ dữ liệu**:
  - Xà nghiêng ở b0 (sai hình học của "flat").
  - Ở WORLD (34–41) chồng và khối teal ở gần cùng độ sâu nên tỉ lệ đọc được (lãi ≈ 2,8 lần khối đã trả, nhìn xấp xỉ).
  - Ở CHART, ×3,8 nhìn ra khoảng 4 lần (đo thô). Không thấy méo đáng kể.
  - Đáy chồng ở zoom (47–64) chìm xuống dưới khung và mờ đi, nên không thấy gốc 0. Người xem không tự kiểm được "$558,100 > $500,000" bằng chiều cao; chỉ nhờ xà.

## 7. Chấm điểm (so Vox / 3Blue1Brown / WSJ)

| Tiêu chí | Điểm | Lý do chính |
|---|---|---|
| Hình mang nghĩa | **3** | Ẩn dụ chồng tiền, gom nhà và phép trừ tốt. Trừ điểm vì: xà nghiêng, nhà vượt xà gây hiểu nhầm, bước lãi→giá không có cầu nối, nhãn kết luận rơi sớm |
| Liền mạch hình–lời–âm | **3** | Đồng bộ theo từ rất tốt (gần như mọi cue trong ±0,2 s/khung). Trừ điểm vì 3 chỗ gãy: 23,4 mờ trắng, 36,5 cắt mép rồi khung nhảy, 64,0→64,5 xoá sạch |
| Nhịp | **3** | Chùng ở 51,5–55; dồn ở 14–15,5, 48–55 và 59,5–62,5; mở đầu 0–2 s đứng yên |
| Âm | **3** | Lời rõ, lặng sau "cap" đúng, âm dữ liệu vừa. Nhạc phẳng ở 15–40, thud 24 to, whoosh hơi dày |

### Năm sửa quan trọng nhất (theo mức ảnh hưởng tới điểm)

1. **64,0–65,5, cầu nối lãi → giá.** Không xoá sạch trong một khung. Giữ "$558,100/past the cap" khoảng 0,5 s khi lùi máy, cho khối teal "what they paid" rơi về đáy chồng 2026 rồi mới tắt xà. (Ảnh hưởng: hình mang nghĩa, liền mạch.)
2. **48–64, nhà cạnh chồng ở CHART.** Hạ nhà cho mái luôn nằm dưới xà, hoặc đẩy nhà ra xa xà, để không vẽ "nhà vượt trần". Đồng thời làm "past the cap" là phần chồng nhô trên xà chứ không phải nhà. (Hình mang nghĩa.)
3. **48–58, cụm nhãn.** Tách "Over/Back under/$500,000 cap" ra khỏi nhau (khoảng ≥24 px ở 540p), giữ chúng tới 59,76 như ý đồ, và lấp chỗ chùng 51,5–55 bằng một chuyển động mang nghĩa (vệt warn chạy dần tới 2026 theo "has stayed", đặt ở 53,9–54,4). (Nhịp, hình.)
4. **34,47–37,5, lùi máy chưa đủ.** Lùi tới khung chứa trọn chồng ×3,8 trước "grown" 35,72 để không cắt mái ở 36,5–37,0 và không phải nhảy khung ở 37,5. (Liền mạch.)
5. **2,0–4,5 và 23,4–24,0, xà trần.**
   - Ở b0 đặt máy ngang cho xà phẳng thật.
   - Ở b3 cho xà rơi và khoá đúng thud 23,96 thay vì vẽ dần.
   - Thay việc làm mờ đường giá trị bằng một chuyển động máy hoặc vật thể có lý do.
   - Hạ thud khoảng 6 dB.
   - Kèm theo: tăng cỡ chữ ILLUSTRATIVE, nguồn và dòng history-not-forecast lên khoảng 1,5 lần để đọc được trên điện thoại.

   (Liền mạch, âm, lớp bắt buộc.)
