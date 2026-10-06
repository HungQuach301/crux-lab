# Đánh giá đạo diễn: bản A, v2 (đoạn trích 0–69 s)

Nguồn đã xem: sheet-1 và sheet-2 (khung cách nhau 0,5 s; tôi cắt và phóng từng hàng để xem), audio.png (mức theo 50 ms và phổ), transcript.txt (mốc thời gian từng từ do ASR tạo), events.txt, intent.txt.
Sai số: hình chỉ biết tới ±0,25 s (một khung là 0,5 s). Những điều tôi không thấy được ở độ phân giải này đều ghi rõ là "không xác nhận được".

## 1. Chỗ lệch giữa hình, lời và âm

| # | Mốc (s) | Lời (ASR) | Hình thấy được | Âm | Đánh giá |
|---|---|---|---|---|---|
| 1 | 1,0 | "Is it?" (0,72–1,02) | Thẻ "paid $200,000 in 2000" bật lên lúc 1,0 | — | Lời không nhắc tới con số này. Thông tin thừa đặt ngay trên câu hỏi, làm loãng chữ "cap". Phải tới 34 s con số $200k mới được nói ra. |
| 2 | 1,5 | "cap?" lúc 3,20 | Vạch trần mờ cùng nhãn "the tax-free cap" hiện lúc 1,5. Không thấy vạch "hạ xuống": nó hiện tại chỗ | riser 1,52 | Khớp với cue cap_hint 1,52 (tức là cố ý vào sớm 1,7 s so với từ). Đạt yêu cầu. Nhãn chỉ cao khoảng 6 px trên thumbnail và tương phản thấp. |
| 3 | 3,0 | "cap?" 3,20 | Dấu "?" hiện lúc 3,0 (khoảng 2,75–3,0) | — | Đạt (cue 3,18, nằm trong ±0,25 s). |
| 4 | 5,0 | "can't see" 4,74–5,04 | Nhà mờ thành mây "?" lúc 5,0–5,5 | whoosh_soft 4,96 | Khớp. Nhưng Rosa & Frank **biến mất** lúc 5,5 và 51 s sau mới quay lại (khoảng 56,5). Ý đồ không yêu cầu điều này. |
| 5 | 7,0–7,5 | "rise" 7,04 | Mũi tên xanh đi lên | — | Khớp. Không có âm nào cho mũi tên. |
| 6 | 9,0–13,5 | "Phoenix Area Home Price Index… Federal Housing…" | Các nhà nhỏ "SOLD" bật lên từ 9,0 | 12 tick, mỗi tick cách nhau khoảng 0,39 s, từ 8,98 tới 13,23 | Tick khớp với nhịp nhà bật lên (cue pop0 8,98). Về nghĩa, hình "nhiều giao dịch" xuất hiện sớm khoảng 5 s so với "many sales" (14,12). Chấp nhận được vì chúng minh hoạ cho "index". |
| 7 | 11,0 | "Federal" 11,32 | Thẻ "Source: FHFA via FRED" | — | Khớp (cue 11,21). |
| 8 | 14,0–15,0 | "average of many sales" 13,60–14,40 | Có chữ "many sales → one average". Lúc 14,5 các nhà nhỏ dẹt lại, lúc 15,0 thì **biến mất hết** | gather 14,45 | **Hình làm khác ý đồ.** Không có cảnh các nhà "gom về một ĐƯỜNG": đường chỉ số chỉ bắt đầu hiện khoảng 16,5–17,0. Hợp âm "gom" vang lên nhưng trên hình không có gì được gom lại. |
| 9 | 15,5–17,5 | "We follow it…from 2000" (15,78–17,70) | Lịch "2000" hiện lúc 15,5. Nhãn "home value" mờ dần vào lúc 16,5–17,0. Đường bắt đầu vẽ khoảng 17,0–17,5 | Có nốt dữ liệu từ 15,8 | Lịch khớp với lời. Đường vẽ trễ khoảng 1,2 s so với cue draw0 15,85. Như vậy khoảng 1–1,5 s đầu, nốt dữ liệu kêu khi chưa có nét nào. |
| 10 | 18,0–19,5 | "to the second quarter of 2026" (18,24–19,76) | Lịch lật 2007→2013→2020→2026 Q2 lúc 19,5 | Nốt tăng cao độ | Khớp (±0,25 s). Đường vẽ 26 năm trong khoảng 2,5 s nên rất nhanh. Tuy vậy, lời đã cho thời lượng đúng bằng ngần ấy. |
| 11 | 15–37 | (cả đoạn) | **Không có trục y và không có giá trên nhà** | — | Ý đồ yêu cầu "giá trên nhà tăng", nhưng tôi không thấy con số nào. Người xem không biết đường đang đo đơn vị gì. |
| 12 | 23,5 | "cap" 23,40 | Vạch trần hiện lúc 23,5 (khoảng 23,25–23,5) | thud 23,71 | Hình khớp. Thud **trễ khoảng 0,3 s** so với từ và so với cue 23,36. Lúc 24,0, đường "home value" tối gần hết rồi sáng lại ở 24,5. Có thể đây là hiệu ứng nhấn, nhưng tôi không xác nhận được ý đồ. |
| 13 | 23,5–37 | "Here's the cap…" | Vạch $500k đặt **trên đường GIÁ NHÀ**, và đường này vượt vạch quanh 2021–22 | — | **Sai nghĩa nguy hiểm nhất.** Suốt khoảng 13 s, người xem thấy *giá nhà* chạm trần trước khi khái niệm *lãi* được đưa ra. Rất dễ hiểu nhầm "giá vượt trần". |
| 14 | 25,5 | "$500" 25,40 / ",000" 25,86 | Nhãn "$500,000 cap" hiện lúc 25,5 | — | Khớp. |
| 15 | 27,0–28,0 | "same in every quarter" 27,20–28,34 | Một vạch trắng nhỏ trượt dọc trần | drone (giữ) | Ý tưởng đúng (thể hiện "mọi quý"), nhưng vạch quá nhỏ: khó thấy ngay cả ở cỡ 100 %. |
| 16 | 30,0 | "gain" 30,00 | "their gain on paper = ?" | — | Khớp. |
| 17 | 30,5–31,0 | "rose like the average" 32,06–32,74 | Chân trang "A home that rose like the Phoenix average" | — | Sớm khoảng 1,5 s, nhưng nó là chân trang nên chấp nhận được. |
| 18 | 34,0 | "$200" 33,96 | Thẻ "$200,000" xanh ngọc ở chân cột nhà | — | Khớp. Tuy nhiên ý đồ là "thẻ giá lớn lên theo đường". Trên hình nó chỉ là một khúc ở chân cột và **không lớn lên**. |
| 19 | 35,5–36,0 | "grown" 35,70 | Chữ "$200,000, grown with the index" | — | Khớp. |
| 20 | 37,0–38,0 | "less" 37,30 / "paid" 39,58 | Lúc 37,0 nhãn đổi thành "$200,000 paid". Đường trượt xuống và đổi sang màu trắng trong khoảng 37,5–38,0 | slide_down 37,06 | Âm vào sớm khoảng 0,24 s so với "less", sát mép chuẩn. Hình trượt khoảng 37,25–38,0, coi là khớp. Lúc 37,0 có **chữ chồng**: "their gain on paper = ?" đè lên "$200,000 paid". Ngoài ra, sau khi trượt, biên độ đường trông lớn hơn, như thể đổi tỉ lệ. Tôi không xác nhận được vì thiếu trục. |
| 21 | 39,5–40,5 | "paid" 39,58, sau đó im lặng tới 41,10 | Lịch nhảy 2026→2009→2000. Nhà "tua lại" về năm 2000 | không có âm | **Gãy.** Xem mục 2. |
| 22 | 43,0–44,5 | "under" 43,18 | Ngoặc "well under" xuất hiện | Nốt dữ liệu trầm | Khớp. Không thấy "vùng dưới vạch tô nhạt" như ý đồ. |
| 23 | 45,5–48,0 | "second quarter of 2022" 45,42–46,26; "crosses" 47,96 | Nhà chạm vạch khoảng 47,0. Nhãn "Over: Q2 2022" và tia sáng hiện lúc 48,0 | riser 46,28, chime 47,88 | Chime khớp với lời. Nhưng nhà đã **chạm vạch khoảng 0,5–0,9 s trước "crosses"**, nên tia sáng và chime đến sau khi hình đã cắt. Nhãn "Q2 2022" trễ khoảng 1,7 s so với từ "2022" (cue q 45,446 muốn nhãn hiện cùng lời). |
| 24 | 49,0–50,5 | "slips back under" 49,30 | Vạch đổi từ vàng sang xám lúc 49,5. **Không thấy nhà trượt xuống** | Nốt dữ liệu đi xuống (đường đỏ) | Việc tắt màu thì đúng lúc. Còn cú "trượt xuống", thứ người xem cần thấy, thì quá nhỏ để nhìn ra. |
| 25 | 51,0–51,5 | "From the second quarter of 2023" 51,34–52,38 | Lịch "2023" hiện lúc 51,0, nhãn "Stayed over since Q2 2023" lúc 51,5 | — | Nhãn khớp với cue lbl 51,53 nhưng **sớm khoảng 0,9 s so với từ "2023"** và sớm khoảng 2,5 s so với "stayed above" (54,08). Đoạn vàng kéo tới 2026 lúc 54,5 thì khớp với "above" 54,38. |
| 26 | 56,5–59,0 | "their home" 57,64–57,82 | Máy đẩy vào, Rosa & Frank xuất hiện lại cạnh nhà | — | Khớp và có lý do. |
| 27 | 59,5–60,0 | "this is the gain" 59,72–60,24 | Thẻ "≈ $558,100" nhỏ ở 59,5, phóng lớn lên trên ở 60,0 | swish 59,75, tick 60,73 | Âm khớp. Hình **khác ý đồ**: số bay lên ô ở giữa phía trên, chứ không "vào biển trên nhà" như dự định. |
| 28 | 62,0 | "past" 62,06 / "cap" 62,44 | Nhãn "past the cap" màu cam | impact 62,76 | Nhãn khớp. Impact **trễ khoảng 0,3 s** so với "cap". Không thấy "chồng tiền đẩy xuyên trần" như ý đồ, chỉ có một khúc cam trên cột vốn đã có từ 59,5. |
| 29 | 63,5 | "Phoenix" 63,62 | Tiêu đề "Phoenix-area prices since 2000" và hai nhà | — | Khớp. |
| 30 | 65,5 | "3" 65,36 / ".8" 65,72 | "×3.8" hiện ra, nhà 2026 cao lên trong khoảng 64,0–65,5 | rise 65,37 | Khớp. Tôi đo thô chiều cao cột (tính cả mái) thì tỉ lệ chỉ khoảng 2,8×, chưa tới 3,8×. Cần kiểm lại xem chiều cao có thật sự tỉ lệ với chỉ số không. |

## 2. Chuyển cảnh

| Mốc | Chuyển | Có lý do? |
|---|---|---|
| 5,0 | Nhà rõ → mây "?" | **Có**, vì "can't see their house". Nhưng việc bỏ hai nhân vật khỏi khung là **gãy mạch nhân vật**: người xem mất "ai" suốt 51 s. |
| 14,5 → 15,0 | Đám nhà SOLD biến mất, mây tan, nhà co lại rất nhỏ | **Gãy nhẹ.** Phép "gom" không cho ra kết quả nhìn thấy được, đường chỉ số không xuất hiện. Trong khoảng 15,0–16,5 chỉ có một ngôi nhà tí hon giữa khung đen. |
| 23,5 | Vạch trần hiện ra | Có lý do. |
| 24,0 | Đường giá tối đi rồi sáng lại (24,0 → 24,5) | Không rõ lý do. Trông như nhấp nháy. |
| 37,5 | Đường giá trượt xuống thành đường lãi | **Tốt nhất phim**: phép trừ hiện ra bằng chuyển động, đúng tinh thần 3Blue1Brown. |
| 39,5–40,5 | Nhà và lịch tua từ 2026 về 2000 (có một khung trung gian "2009" lúc 40,0, và "2000" mờ ở 40,5) | **Gãy.** Không có âm, không có chữ báo, người xem không biết vì sao thời gian chạy lùi. Lời cũng ngưng (39,6–41,1), nên đây chính là lúc phải có một cue. |
| 56–59 | Đẩy máy, nhân vật quay lại | Có lý do ("their home"). Nhưng phần khung trái bị cắt: đường cong và vạch chạm mép trái. |
| 63,0–63,5 | Hoà tan biểu đồ sang cảnh hai nhà | Có lý do (đổi ý sang ×3,8). Nhưng lúc 63,5 hai lớp chồng lên nhau rất đục (đường cũ, vạch $500k mờ, nhà mới) nên trông bẩn. Cả câu chuyện về trần bị bỏ ngang, không có cảnh khép lại. |

## 3. Nhịp

**Chỗ chùng** (hình gần như đứng yên trong khi lời chạy, hoặc đứng yên quá 3 s):
- **5,5–9,0 (khoảng 3,5 s):** mây "?" đứng yên. Chỉ có mũi tên nhỏ hiện lúc 7,0 trong khi lời đọc "so we let its value rise exactly like…".
- **19,5–23,3 (khoảng 3,8 s):** biểu đồ đứng yên ở 2026 Q2. Lời "the latest data" kết thúc lúc 21,52, sau đó im 1,4 s.
- **30,5–34,0 (khoảng 3,5 s):** "their gain on paper = ?" đứng yên trong khi lời chạy "on paper. For a home that rose like the average". Chùng rõ.
- **54,5–56,0:** đứng yên khoảng 1,5 s, chấp nhận được.
- **66,0–69,0 (khoảng 3 s):** ×3.8 đứng yên. Lời chạy tới 67,6, sau đó hết đoạn.

**Chỗ dồn hoặc rối:**
- **37,0–40,5:** đổi nhãn, đường trượt, chữ chồng, rồi tua lại về 2000, tất cả trong khoảng 3,5 s. Người xem chưa kịp "đọc" đường lãi thì nó đã bị tua.
- **47,0–48,5:** nhà chạm vạch, nhãn, tia sáng và vạch đổi vàng dồn vào nhau. Tình huống này có chủ ý, nên chấp nhận được.
- **51,5–56:** ba nhãn chen ở góc trên phải ("Over: Q2 2022", "Stayed over since Q2 2023", "$500,000 cap") cùng với huy hiệu ILLUSTRATIVE. Góc này quá chật.

## 4. Lớp bắt buộc

| Lớp | Có mặt | Đè hình? | Đọc được ở 25 %? |
|---|---|---|---|
| ILLUSTRATIVE (huy hiệu vàng, góc trên phải) | Suốt 0–69 s | Không | **Không.** Chữ cao khoảng 5–6 px trên thumbnail, nên ở 25 % sẽ dưới 3 px. |
| "US only · history, not a forecast" (chân trái) | 15,0 → hết | Không | **Không.** Chữ nhỏ và xám trên nền tối. |
| "Source: FHFA via FRED" (trên trái) | 11,0 → hết, **nhưng mất lúc 63,0–63,5** (bị ô $558,100 đang mờ dần che, sau đó hiện lại lúc 64,0) | Không | Không, vì chữ quá nhỏ. Việc nó **chớp tắt** lúc chuyển cảnh là lỗi. |
| Đối trọng "A measurement, not a tax bill or a next step" (chân phải) | Khoảng 62,0 → hết | Không | **Không.** Đây lại là lớp quan trọng nhất về mặt pháp lý và nội dung. |
| "A home that rose like the Phoenix average" | 30,5 → 62 | Không | Không. |

**Chữ chồng và cắt mép:**
- 37,0: "their gain on paper = ?" đè lên "$200,000 paid".
- 45,5–46,5: nhãn "gain on paper" bị cột nhà che giữa chữ ("gai… paper").
- 61,0–62,5: dòng "gain on paper · the number from the opening" chồng lên mái nhà và hai nhân vật.
- 14,0: nhà SOLD bị cắt ở mép trái.
- 58,5–63,0: đường cong và vạch trần chạy ra mép trái. Nhãn "$500,000 cap" chỉ cách mép khoảng 1 %.

## 5. Âm

- **Lời luôn rõ:** có. Đỉnh giọng khoảng −5 đến −10 dBFS, nhạc khoảng −35 đến −40, room tone khoảng −60. Riêng hai hiệu ứng thud (23,71) và impact (62,76) đạt đỉnh khoảng −8 dBFS, **to ngang giọng**. Ý đồ là "thud trầm" và "va chạm mềm", nên hiện tại quá mạnh.
- **Nhạc theo căng–chùng:** yếu. Bản đồ tension đi từ 0,35 tới 1,0, nhưng mức nhạc chỉ dao động khoảng ±5–8 dB quanh −37. Có nhích lên ở 44–48 và 56–62 (khoảng −30 đến −25) rồi rơi xuống khoảng −45 sau 63. Hướng đi đúng, nhưng quá kín: đỉnh 1,0 lúc 61,3 không thành cao trào nghe được.
- **Khoảng lặng sau "past the cap":** lời dừng lúc 62,68 và quay lại lúc 63,62, tức khoảng 0,94 s. Impact rơi vào 62,76. Nhạc nhả xuống khoảng −45 nhưng không tắt hẳn, room tone vẫn giữ sàn khoảng −60, nên **có chuyển tiếp** và không bị hụt. Tuy vậy, khoảng lặng bị impact chiếm mất và không có "hơi thở" trước câu ×3,8.
- **Âm dữ liệu:** nghe thấy được. Đường đỏ ở 17,5–20 và 41–54 nằm khoảng −20 đến −35, thấp hơn đỉnh giọng khoảng 10–15 dB, nên **không lấn lời**. Lỗi duy nhất: nốt kêu từ 15,8 khi đường chưa vẽ (khoảng 17,0).
- **Hiệu ứng thừa hoặc khó chịu:**
  - Thud và impact quá to, cả hai đều trễ khoảng 0,3 s.
  - Chime lúc 47,88 có dải hài rất sáng tới 8 kHz, kéo dài khoảng 1,5 s trên phổ. Hơi chói, nên cắt ngắn đuôi.
  - Đoạn tua lại ở 40 s thì thiếu âm.
  - Mười hai tick ở 9–13 s thì đạt yêu cầu.

## 6. Chấm điểm (so với Vox / 3Blue1Brown / WSJ)

| Tiêu chí | Điểm | Lý do ngắn |
|---|---|---|
| Hình mang nghĩa | **3/5** | Phép trừ trượt đường ở 37,5 rất tốt. Nhưng vạch trần đặt trên đường *giá* suốt 13 s gây hiểu sai, thiếu trục và đơn vị, cú "gom" không ra đường, cú "slip" không nhìn thấy được. |
| Liền mạch hình–lời–âm | **3/5** | Phần lớn khớp trong ±0,25 s. Các điểm lệch: chạm vạch sớm khoảng 0,7 s so với "crosses", nhãn Q2 2022 trễ khoảng 1,7 s, thud và impact trễ khoảng 0,3 s, nhân vật biến mất 51 s. |
| Nhịp | **3/5** | Có ba chỗ chùng 3,5–3,8 s, và cụm 37–40,5 bị dồn rồi tua ngược. |
| Âm | **3/5** | Lời luôn sạch, âm dữ liệu cân tốt. Nhưng nhạc không thở theo căng–chùng, hai hiệu ứng nặng thì to quá và trễ. |

### Năm sửa quan trọng nhất

1. **23,4–37,0: không để vạch trần $500k đứng cạnh đường GIÁ.** Có hai cách. Cách thứ nhất là làm phép trừ (37,3) trước rồi mới hạ trần. Cách thứ hai là giữ đường giá thật mờ và chỉ hiện trần khi đường lãi đã có. Dù chọn cách nào, cũng phải thêm trục $ (ít nhất các mốc $0, $250k, $500k, $750k) và giá trên nhà như ý đồ.
2. **39,6–41,1: thay cú tua 2026→2000.** Hoặc dùng một kim quét (playhead) có whoosh ngược kèm nhãn "replay from 2000", hoặc giữ nhà ở 2026 và cho một điểm sáng chạy dọc đường lãi. Đồng thời gỡ chữ chồng lúc 37,0 và giữ đường lãi đứng yên khoảng 1 s sau "paid" (39,58) để người xem đọc.
3. **45,4–49,5: đồng bộ cú cắt.** Nhãn "Q2 2022" phải hiện lúc 46,26 ("2022"). Nhà chỉ được chạm vạch đúng lúc 47,96 ("crosses"), cùng tia sáng và chime trong ±1 khung. Lúc 49,3, phóng to hoặc nhấn để cú "slips back under" nhìn thấy được.
4. **13,5–17,0: cho các nhà SOLD gom thành ĐƯỜNG chỉ số đúng lúc 14,45**, khớp với hợp âm gather. Đường đó sẽ là điểm bắt đầu vẽ ở 15,85, xoá được 2 s nhà tí hon đứng một mình. Đồng thời giữ Rosa & Frank (dưới dạng bóng) ở góc khung từ 5,5 tới 56.
5. **Âm và chữ bắt buộc:**
   - Kéo thud về 23,40 và impact về 62,44, hạ cả hai 8–10 dB.
   - Đẩy nhạc thêm khoảng 6 dB ở 44,5–48 và 56,5–62,4, rồi cắt hẳn trong khoảng 0,5 s sau "cap" (chỉ còn room tone).
   - Phóng các lớp bắt buộc lên cỡ đọc được ở 25 %, tối thiểu khoảng 2,5 % chiều cao khung, đặc biệt là đối trọng xuất hiện từ khoảng 62 s.
   - Sửa chỗ Source mất ở 63,0–63,5 và chỗ chữ chồng ở 61–62,5.
