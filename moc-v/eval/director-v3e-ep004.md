# Đạo diễn duyệt — V3e, ep004 (đoạn 0–70 s, bản xem trước 540p)

Nguồn đã xem: sheet-1.png, sheet-2.png (khung cách 0,5 s), audio.png, transcript.txt, events.txt, intent.txt.
Quy ước sai số: sự kiện thấy lần đầu ở khung t thì đã xảy ra trong khoảng (t−0,5; t]. Δ = (thời điểm hình) − (mốc lời). Chỉ gọi là "lệch" khi cả khoảng nằm ngoài ±0,2 s.

---

## 1. Lệch hình / lời / âm

### 1a. Bảng đồng bộ theo từng mốc

| Mốc (cue) | Lời (ASR) | Hình thấy lần đầu | Khoảng Δ | Kết luận |
|---|---|---|---|---|
| has 2,06 – xà trần hiện | Has@2,08 | 2,0 s | [−0,56; −0,06] | Đạt |
| q 3,18 – dấu "?" | cap?@3,20 | 3,0 s (đã rõ) | [−0,68; −0,18] | Sát biên; sớm ít nhất 0,18 s. Không chứng minh được là lệch |
| blur 4,96 – sương | can't see@4,74–5,04 | 5,0 s (nhà đang mờ) | [−0,46; +0,04] | Đạt |
| rise 7,18 – mũi tên | rise@7,04 | 7,0 s | [−0,68; −0,18] | Sát biên so với cue, nhưng khớp với chữ "rise" được nói lúc 7,04. Đạt |
| pop0 8,98 – biển SOLD đầu tiên | exactly@8,18 | 9,0 s | [−0,48; +0,02] | Đạt; các tick SOLD tiếp theo khớp với biển hiện dần |
| src 11,21 – "Source: FHFA via FRED" | Federal@11,34 | 11,0 s (mờ), 11,5 s (rõ) | bắt đầu ≤ 11,0 → Δ ≤ −0,21 | Fade bắt đầu sớm khoảng 0,2 s. Về nghĩa vẫn ổn: chữ "from the" nằm ở 10,72–11,16 |
| many 14,10 – "many sales → one average" | many@14,12 | 14,0 s | [−0,60; −0,10] | Đạt |
| avg 14,45 – các nhà gom vào chồng | sales@14,40 | 14,5 s | [−0,45; +0,05] | Đạt |
| quarter 16,24 – "2000 Q1" | quarter@16,36 | 16,0 s (15,5 s chưa có) | [−0,74; −0,24] | **Sớm ≥ 0,24 s.** Nhãn Q1 là trạng thái đầu nên hại ít; Q2 ở 16,5 và Q3 ở 17,0 vẫn khớp nhịp "quarter by quarter" |
| y2000 17,70 – đường bắt đầu chạy | 2000@17,70 | 17,5 s vẫn là Q3, 18,0 s đã tới 2007 | [−0,20; +0,30] | Đạt; chạy 7 năm trong < 0,5 s |
| y2026 19,69 – tới 2026 Q2 | 2026@19,76 | 20,0 s ("2025" ở 19,5 s) | [−0,19; +0,31] | Đạt |
| cap 23,36 – xà rơi | cap@23,40 | 23,5 s | [−0,36; +0,14] | Đạt; thud 23,96 rơi đúng lúc xà khoá (24,0 s) |
| flat 24,58 – xà đủ dài | flat@24,64 | 24,5 s | [−0,58; −0,08] | Đạt |
| five 25,37 – nhãn "$500,000 cap" | $500@25,40 | 25,5 s | [−0,37; +0,13] | Đạt |
| same 27,18 – nhịp sáng chạy dọc xà theo quý | same@27,20 | 27,0 s | [−0,68; −0,18] | Sát biên, không chứng minh được là lệch |
| gain 30,01 – "their gain on paper = ?" | gain@30,00 | 30,0 s | [−0,51; −0,01] | Đạt |
| two 33,94 – khối teal "what they paid" | $200@33,96 | 34,0 s | [−0,44; +0,06] | Đạt |
| grow 35,89 – chồng lớn | grown@35,72 | 36,0 s | [−0,39; +0,11] | Đạt |
| less 37,30 – khối trượt, chồng hạ | less@37,30 | 37,5 s | [−0,30; +0,20] | Đạt |
| paid 39,58 – ngoặc "their gain on paper" | paid@39,58 | 39,5 s | [−0,58; −0,08] | Đạt |
| under 43,23 – ngoặc "well under" | under@43,18 | mờ ở 43,0 s, rõ ở 43,5 s | bắt đầu ≤ 43,0 → Δ ≤ −0,23 | **Fade bắt đầu sớm ≥ 0,23 s**, nhưng phần rõ rơi đúng chữ. Lỗi nhẹ |
| cross 47,88 – chạm xà, loé, "Over: Q2 2022" | crosses@47,94 | 48,0 s | [−0,38; +0,12] | Đạt; chime khớp |
| slips 49,28 – "Back under" | slips@49,30 | 49,5 s | [−0,28; +0,22] | Đạt |
| lbl 51,53 – "since Q2 2023" | From@51,36 | 51,5 s | [−0,53; −0,03] | Đạt (nhãn hiện trước khi nói "2023"@52,38, đúng như spec) |
| above 54,43 – "Stayed over since Q2 2023" | above@54,38 | 54,5 s | [−0,43; +0,07] | Đạt |
| rose 58,02 – mũi tên cạnh nhà | rose@58,04 | 58,0 s | [−0,52; −0,02] | Đạt |
| fly 59,76 – số "≈ $558,100" | this@59,74 | **59,5 s** (59,0 s chưa có) | [−0,76; −0,26] | **Sớm ≥ 0,26 s**: con số hiện trước chữ "this" |
| land 60,73 – số đáp lên biển | opening@60,82 | Vị trí và cỡ đã cố định ở 60,5 s, giống 61,0 s | đáp ≤ 60,5 → Δ ≤ −0,23 | **Có thể sớm.** Tiếng tick ở 60,73 đến sau khi hình đã đứng yên. Quãng bay quá ngắn nên khó đo |
| past 62,01 – ngoặc "past the cap" | passed@62,06 | 62,0 s | [−0,51; −0,01] | Đạt |
| cap 62,44 – nhà nảy qua xà, chạm mềm | cap@62,44 | **Không thấy**: nhà đứng yên ở 62,0, 62,5 và 63,0 s | — | Cú nảy có thể đã rơi giữa hai khung, không xác nhận được. Tiếng "land" ở 62,58 vẫn kêu, nên có nguy cơ **có âm mà không có hình** |
| x 65,37 – "×1" / "×3.8" | 3@65,36 | 65,5 s | [−0,37; +0,13] | Đạt |
| lvl 67,69 | level@67,60 | Không có thay đổi nào thấy được | — | Không có sự kiện hình |

Tóm lại: 27 mốc kiểm được. 23 mốc nằm trong ±0,2 s hoặc không chứng minh được là lệch. Có 3 chỗ sớm vượt biên một chút: 16,0 s (Q1), 43,0 s (bắt đầu fade "well under") và 59,5 s (số $558,100). Có 1 sự kiện không thấy trên hình: cú nảy lúc 62,44 s.

### 1b. Âm có phản ứng đúng lúc không
- Whoosh nằm đúng các khoảng di chuyển máy (7,53 / 14,82 / 28,76 / 30,67 / 34,47 / 41,14 / 46,06 / 55,12 / 64,12). Tiếng tick khi biển SOLD hiện cách nhau khoảng 0,88 s, khớp với biển hiện dần từ 9,0 đến 13,5 s. Thud 23,96 khớp lúc xà khoá. Chime 47,88 khớp khung loé 48,0.
- Tiếng tick 60,73 ("đáp") đến muộn hơn hình, vì số đã đứng yên ở 60,5.
- Tiếng land 62,58 không có hình đi kèm (xem trên).
- Whoosh_air 30,67 phục vụ một cú đẩy máy gần như không thấy được (xem mục 2). Đó là âm cho một chuyển động không tồn tại về mặt cảm nhận.

### 1c. Chỗ hình KHÁC ý đồ
1. **b8 → b9 (55,0–59,5 s).** Spec yêu cầu "ba nhãn giữ tới khi số bay". Thực tế "Over: Q2 2022" và "Back under" mờ đi ở 55,0 và mất hẳn ở 55,5. "Stayed over since Q2 2023" mất ở 59,5. Nhãn "$500,000 cap" cũng vắng từ 55,5 đến 57,0. Kết quả là trong 2 s cái xà không có tên.
2. **b9: không thấy Rosa & Frank** đứng cạnh nhà ở đầu đường (56–61 s), dù spec ghi rõ. Câu "if THEIR home…" vì thế mất người, chỉ còn nhà.
3. **b9: số "bay" gần như không di chuyển.** Từ 59,5 đến 60,5 hộp số chỉ dịch vài pixel sang phải và to lên một chút. Đó không phải đường bay từ đỉnh chồng lên biển trên mái. Số hiện ở phía trên bên trái mái nhà, chưa thành "biển trên mái".
4. **b10: cú nảy qua xà không thấy** (62,0 / 62,5 / 63,0 giống nhau).
5. **b11 (64,5 s): xà và nhãn "$500,000 cap" còn nguyên giữa cú lùi máy**, kèm một đường cong trắng (đường lãi đổi màu?) đang dâng lên. Spec ghi "đường lãi, xà, nhãn trần tắt ngay khi lùi máy". Ở 65,0 s vẫn còn bóng mờ của xà, của nhãn và của một đường giá.
6. **b4: cú đẩy chậm 30,67–33,27** gần như không đọc được (nhà ở 30,0 và 33,5 to gần bằng nhau).
7. **b1 (5,5–14 s):** nhà chính chỉ còn một mái mờ lơ lửng trên chồng tiền. Đúng ý "không thấy nhà", nhưng hình trông như lỗi render (mái tách khỏi thân).

---

## 2. Chuyển cảnh và chuyển chế độ

| Thời điểm | Bước chuyển | Lý do | Liền mạch? |
|---|---|---|---|
| 7,53–8,63 | pull wHome → wHood | "rise like the … index" → nhiều nhà | **Liền**: 7,5 → 8,0 → 8,5 lùi đều, các nhà hiện vào khung |
| 14,82–15,87 | mode World → Chart | "average of many sales" → một đường | **Liền**: nhà gom vào chồng (14,5), còn một nhà một chồng (15,0), trục hiện (15,5). Đây là cú chuyển tốt nhất đoạn: cùng một vật thể trở thành điểm dữ liệu |
| 28,76–29,76 | mode Chart → World | "And here's THEIR gain" | **Liền**: ở 29,0 vẫn thấy xà và hình người ở xa, máy bay tới. Xà thì biến mất ở 29,5 mà không có lý do |
| 30,67–33,27 | push | "a home that rose like the average" | **Không thấy được.** Có lý do nhưng không có hiệu quả; nên bỏ hoặc đẩy mạnh hơn |
| 34,47–35,37 | pull | để thấy trọn chồng cao gấp ~4 | Có lý do. **Lùi chưa đủ**: ở 36,0–37,0 mái nhà chạm sát mép trên khung |
| 41,14–42,14 | mode World → Chart | tua về 2000 rồi phát theo năm | **Liền**: nhà nhỏ lại trên chồng ngắn (41,5) rồi đứng ở 2000 (42,0). Rõ ý |
| 46,06–47,26 | push cFull → cZoom | đoạn 2021–26 quá nhỏ | **Liền và có lý do**. Đẩy xong trước khi đường cắt xà (47,88), rất đúng nghề |
| 55,12–57,33 | push cZoom → cTip | "THEIR home" | Liền nhưng nhẹ. Thiếu Rosa & Frank nên lý do "của họ" không hiện ra hình |
| 64,12–65,12 | pull cTip → cFull, đổi đại lượng lãi → giá | cần cả 2000 và 2026 | **GÃY.** Ở 64,5 lãi, xà, nhãn trần và một đường trắng còn chồng lên nhau. Ở 65,0 tiêu đề mới, bóng đường giá, bóng xà. Ở 65,5 chỉ còn hai chồng. Đổi đại lượng ngay giữa lúc máy chạy, lại bằng cross-fade, nên trái với quy tắc "không cross-fade". Người xem không biết trục dọc vừa đổi nghĩa |

---

## 3. Nhịp

**Chỗ chùng** (hình gần như đứng yên trong khi lời chạy):
- **30,0–33,5 s (≈ 3,5 s):** lời "on paper. For a home that rose like the average" đi kèm một cú đẩy không thấy được. Thực chất là hình đứng yên.
- **55,5–58,0 s (≈ 2,5–3 s):** lời "So, on paper, if their home…", chỉ có cú đẩy rất nhẹ và các nhãn tắt dần. Chưa quá 3 s, nhưng là đoạn trước cao trào nên càng thấy chùng.
- **65,5–69,0 s:** khung đứng yên, chỉ có hai chồng và hai ngoặc ×1 / ×3,8. Lời "times their 2000 level" chạy khoảng 2,5 s. Chưa quá 3 s, nhưng khung trống: tiêu đề là "prices since 2000" mà không có đường giá.
- 20,0–23,0 s đứng yên khoảng 3 s, nhưng lời chỉ chiếm 0,5 s. Chấp nhận được, đó là một khoảng thở.

**Chỗ dồn hoặc rối:**
- **17,5–20,0 s:** đường chạy 26 năm trong khoảng 2 s (2000 → 2007 trong < 0,5 s). Dồn nhưng có chủ ý, đúng với "from 2000 to 2026".
- **47,0–55,0 s:** cùng lúc có "Over: Q2 2022", "Back under", "$500,000 cap", "since Q2 2023", tiêu đề, nhà và chồng, tất cả dồn trong nửa trái và giữa khung. "Back under" dính sát dưới "$500,000 cap".
- **61,0–64,0 s:** "their gain on paper" (đè lên đường vàng), "≈ $558,100", "$500,000 cap", "past the cap" và nhà trong cùng một vùng. Cao trào bị rối chữ.

---

## 4. Lớp bắt buộc

- **ILLUSTRATIVE:** có suốt từ 0 đến 69 s ở góc trên phải. Không bị đè, đọc được.
- **history-not-forecast** ("US only · history, not a forecast"): chỉ có từ 14,5 s. **Đoạn 0–14 s không có.** Có thể chấp nhận vì chưa có số liệu, nhưng biển SOLD và mũi tên đi lên đã hiện từ 7,0 s.
- **Nguồn** ("Source: FHFA via FRED"): có từ 11,0 s, đúng lúc nói tên cơ quan. Tốt.
- **Đối trọng** ("A measurement, not a next step", từ 60,0 s thành "not a tax bill or a next step"): có từ 42,5 s.
- **Bị đè hình:** **có.** Từ 47,0 đến 64,0 s, cột chồng tiền xanh ở chế độ zoom chạy xuyên xuống đáy khung và đi qua cụm chữ "…not a next step" / "…tax bill or a next step" (thấy rõ ở 47,0–55,0 và 60,5–64,0). Đây là lỗi nặng nhất về lớp bắt buộc: dòng miễn trừ bị khối 3D cắt ngang.
- **Đọc trên điện thoại:** lower-third cao khoảng 2,5–3 % chiều cao khung, đọc được nhưng nhỏ. Nhãn năm trên trục (2000…2025), "×1", "2000 Q1" và "past the cap" (cam, nhỏ) **quá nhỏ cho màn hình điện thoại**. "×3.8" và "≈ $558,100" thì đọc tốt.
- **Chữ chồng nhau:**
  - 47,0: "$500,000 cap" bị đường lãi và chồng cắt qua.
  - 49,5–55,0: "Back under" sát dưới "$500,000 cap".
  - 61,0–64,0: "their gain on paper" đè lên đường vàng.
  - 64,5: "$500,000 cap" đè lên đỉnh chồng 2026.
  - 65,0: bóng "$500,000 cap" nằm sau chồng.
- **Cắt mép:** ở 36,0–37,0 mái nhà chạm sát mép trên. Ở 47–64 đường dữ liệu bị cắt ở mép trái; khung đang zoom nên chấp nhận được.

---

## 5. Âm

- **Lời luôn rõ:** có. Đỉnh lời khoảng −8 đến −10 dBFS. Nhạc khoảng −40 dB ở 4–40 s và khoảng −25 đến −32 dB ở 44–62 s. Ở 52–62 s, các âm tiết thấp của lời (−20 đến −30) bắt đầu ngang với nhạc. Vẫn rõ, nhưng nên hạ nhạc thêm 2–3 dB khi có lời ở đoạn cao trào.
- **Nhạc theo căng–chùng:** chỉ đúng một nửa. Đoạn 4–40 s gần như phẳng (khoảng −40 ± 3 dB), dù bản đồ căng tăng từ 0,35 lên 0,55. Đoạn 44–62 s dâng rõ, khoảng +10 dB, đúng với 0,85–1,0. Biên độ tổng khoảng 12–15 dB là đủ. Accent 23,86 có một đỉnh nhỏ trong mix; accent 47,88 khớp chime.
- **Khoảng lặng sau "past the cap":** **đạt.** Nhạc tắt khoảng 62,6 s. Từ khoảng 62,7 đến 63,6 s chỉ còn room tone (khoảng −60 dB), quãng tối thấy rõ trên spectrogram, rồi lời "Phoenix" vào lúc 63,62. Nhạc quay lại khoảng 64,5 s ở mức thấp (−45 đến −50 dB), đúng "release". Đây là khoảnh khắc âm thanh tốt nhất của đoạn.
- **Âm dữ liệu:** nghe được. Đỉnh khoảng −25 đến −30 dB ở 16–21 s và 41–54 s, thấp hơn đỉnh lời khoảng 15 dB, rơi vào các khe giữa câu nên không lấn lời. Ở 17–19 s âm dữ liệu cao hơn nhạc, hợp lý vì là lúc đường chạy.
- **Hiệu ứng thừa hoặc khó chịu:**
  - Chime 47,9 có các họa âm kéo thành vạch ngang tới khoảng 7 kHz trên spectrogram, có nguy cơ chói trên loa điện thoại.
  - Thud 23,96 lên tới khoảng −20 dB trong mix, hơi to so với một "khoá".
  - Whoosh_soft 55,12 kéo khoảng 2 s ở −45 dB cho một cú đẩy rất nhẹ.
  - Whoosh_air 30,67 không có chuyển động tương ứng.
  - Land 62,58 không có hình.

---

## 6. 3D: làm rõ ý hay trang trí

**Làm rõ ý:**
- Chồng tiền là giá trị và đỉnh chồng là điểm dữ liệu. Đây là ý tưởng mạnh.
- Các nhà SOLD bay vào một chồng (14,5) tức là "trung bình của nhiều giao dịch". Hình ảnh hoá rất đúng tinh thần 3Blue1Brown.
- Khối "what they paid" đổi màu teal, trượt ra, chồng hạ xuống (34,0–39,5) tức là phép trừ. Rõ và đáng nhớ.
- Xà trần là vật thể thật, nên "crosses" thành một va chạm (48,0).

**Trang trí hoặc gây nhiễu:**
- Mái nhà mờ lơ lửng ở 5,5–14 s.
- Thân nhà to đứng cạnh chồng ở chế độ CHART. **Từ 56 đến 64 s mái nhà nhô cao hơn xà trần**, đúng kiểu đọc nhầm "giá nhà vượt trần" mà b3 đã cố tránh. Spec chỉ bảo mái nằm dưới điểm dữ liệu; điều đó đúng nhưng chưa đủ, mái còn phải nằm dưới xà, hoặc nhà phải đứng xa xà hơn.

**Tỉ lệ dữ liệu:**
- Ở chế độ CHART nhìn thẳng, tỉ lệ có vẻ đúng. Ở 65,5 s chồng 2000 so với chồng 2026 khoảng 1 : 4, khớp ×3,8. Ở 38,0 s phần lãi so với phần đã trả khoảng 2,5 : 1, gần với 558 / 200 ≈ 2,8.
- Ở chế độ WORLD, khi máy đổi khoảng cách thì không so được chiều cao trước và sau ("grown" 3,8 lần). Pull ở 34,5 xảy ra trước grow ở 35,9 nên tạm ổn.
- Ở chế độ zoom, chồng kéo dài xuống quá đáy khung. Không sai tỉ lệ, nhưng mất mốc 0, nên người xem chỉ còn so được với xà.
- Đoạn 64,5–65,0 (lãi và giá cùng trên một trục) là chỗ duy nhất có nguy cơ đọc sai đại lượng.

---

## 7. Chấm điểm (so với Vox / 3Blue1Brown / WSJ)

| Tiêu chí | Điểm | Lý do ngắn |
|---|---|---|
| Hình mang nghĩa | **3,5 / 5** | Có những ẩn dụ chuyển động thật sự mang nghĩa: gom nhà thành trung bình, phép trừ bằng khối, cú chạm xà. Bị kéo xuống vì cao trào b9–b11 yếu (số không bay, không có cú nảy, thiếu Rosa & Frank, mái nhô qua xà) và cảnh kết 65–69 s không có đường giá |
| Liền mạch hình–lời–âm | **3,5 / 5** | Đồng bộ theo chữ rất tốt (23/27 mốc trong biên). Có 3 chỗ sớm khoảng 0,25 s, 1 âm thiếu hình (62,58) và cú chuyển 64–65 s bị gãy bằng cross-fade |
| Nhịp | **3 / 5** | Có hai khoảng gần đứng yên khoảng 3 s (30–33,5 và 55,5–58). Cao trào 47–64 s bị dồn chữ |
| Âm | **3,5 / 5** | Khoảng lặng sau "cap" rất đẹp, lời luôn rõ, âm dữ liệu có chỗ đứng. Bị trừ vì nhạc phẳng ở 4–40 s, chime chói, có âm không có hình hoặc chuyển động tương ứng |

### Năm sửa quan trọng nhất (xếp theo mức ảnh hưởng tới điểm)

1. **64,1–65,5 s: làm lại cú đổi đại lượng lãi → giá** (ảnh hưởng tới Hình, Liền mạch và Nhịp).
   - Tắt đường lãi, xà và nhãn trần trong khoảng lặng 62,7–63,6, **trước** khi máy lùi. Không để còn ở 64,5.
   - Đổi đại lượng bằng hành động vật thể, ví dụ khối teal trở về đáy chồng như spec, thay vì cross-fade.
   - Vẽ lại đường giá từ 2000 tới 2026 trong 65,5–68 s để có cái nhìn trong lúc lời "almost 3.8 times" chạy.
2. **59,5–63,0 s: sửa cao trào.**
   - Số "≈ $558,100" phải hiện đúng ở "this" (59,74), không sớm hơn.
   - Cho số bay một quãng thấy được (đỉnh chồng → biển trên mái), đáp đúng 60,73 cùng tiếng tick.
   - Làm cú nảy qua xà thấy được trong ít nhất 2 khung quanh 62,44–62,6, nếu không thì bỏ tiếng land.
   - Đưa Rosa & Frank vào khung từ 56,0.
   - Hạ nhà để mái nằm dưới xà.
3. **47,0–64,0 s: dọn chữ và lớp bắt buộc.**
   - Cắt chồng tiền phía trên lower-third, hoặc đặt nền cho dòng miễn trừ, để khối 3D không xuyên qua "…not a next step".
   - Tách "Back under" khỏi "$500,000 cap" (49,5–55).
   - Đưa "their gain on paper" ra khỏi đường vàng (61–64).
   - Phóng to nhãn năm, "×1" và "past the cap" cho điện thoại.
4. **55,0–59,5 s: giữ nguyên ba nhãn và nhãn "$500,000 cap"** đến khi số bay như spec, để có "trạng thái kết luận". Đồng thời làm cú đẩy 55,1–57,3 rõ hơn hoặc thêm một hành động nhỏ, để hết đoạn chùng.
5. **30,0–37,0 s: sửa máy ở b4.**
   - Cú đẩy 30,67–33,27 hoặc làm cho thấy được (đẩy gấp khoảng 1,3 lần) hoặc bỏ cả máy lẫn whoosh_air.
   - Lùi máy ở 34,5 thêm để mái nhà không chạm mép trên ở 36,0–37,0.
   - Kèm theo: cho nhạc 4–40 s dâng nhẹ theo bản đồ căng (0,35 → 0,55), và lọc bớt họa âm cao của chime 47,9.
