# Đánh giá đạo diễn – bản A (70 s, Phoenix / trần $500,000)

Nguồn xem: sheet-1/2 (khung mỗi 0,5 s → mọi mốc hình có sai số ±0,25 s), audio.png (mức theo lớp + phổ), transcript (ASR), events.txt, intent.txt. Chỉ ghi những gì thấy được trong các file này.

---

## 1. Lệch hình / lời / âm (chuẩn: hình đúng từ khoá ±0,2 s)

| Beat | Từ khoá (lời) | Hình xuất hiện | Lệch | Âm | Nhận xét / khác intent |
|---|---|---|---|---|---|
| b0 | "cap?" @3,20 | Vạch "the tax-free cap" mờ từ 1,5, rõ 2,0; dấu "?" 3,0 | "?" −0,2 s: **đạt** | riser 1,52 → tới "cap?" | Intent: vạch ghi **$500,000**; hình chỉ ghi "the tax-free cap" (chưa có số). Chấp nhận được vì b3 mới giới thiệu số. |
| b1 | "can't see their house" @4,74–5,32 | Nhà mờ thành mây "?" + cặp đôi mờ 5,0 | **đạt** | whoosh_soft 4,96 khớp | Rosa & Frank **biến mất từ 5,5 và không bao giờ quay lại** (intent b9 cần họ). |
| b1 | "let its value **rise**" @7,04 | 5,5–9,0 nhà mây đứng yên, không có gì "rise" | không có hình | – | Chùng 3,5 s (xem §3). |
| b1 | "Federal Housing Finance Agency" @11,32–12,48 | "Source: FHFA via FRED" 11,0 | −0,3 s: chấp nhận | – | Đạt. |
| b1 | nhiều giao dịch ("many sales" @14,12) | Nhà nhỏ "SOLD" bật lên từ **9,0** tới 13,5 | Hình đi trước lời ~5 s (hợp lý như dẫn dắt) | **tick 11,93–13,49**: nhà đầu tiên bật lúc 9,0 mà tick đầu ở 11,93 → **âm trễ ~2,9 s**; 12 tick đều nhau 0,12 s, không gắn với từng nhà | Intent "tick mềm mỗi nhà nhỏ" chưa đạt. |
| b1 | gom về **một đường** | 13,5–15,0 nhà nén vào chân; 15,0 chỉ còn 1 nhà trên cọc, **không có đường** (đường bắt đầu vẽ 16,5) | Khác intent | gather 14,45 khớp lúc nén | Phép "nhiều nhà → một đường chỉ số" không thấy được; đường chỉ là vệt sau nhà. |
| b2 | "from **2000**" @17,70 | Lịch "2000" ở 15,5; lúc 17,7 lịch đã 2006→2009 | **Hình sớm ~2,2 s** | Nốt dữ liệu từ 15,8 (khớp đầu câu) | Lịch quét không bám lời. |
| b2 | "**2026**" @19,76 | Lịch "2026 Q2" ở 21,0 (19,5 còn 2019) | **Hình trễ ~1,2 s** | – | |
| b3 | "Here's the cap" @23,40 | Vạch trần hiện 23,5 | +0,1 s **đạt** | thud + drone 23,71 (+0,3 s) | Intent "vạch rơi xuống và khoá": khung cho thấy vạch **hiện tại chỗ**, không thấy rơi. |
| b3 | "$500,000" @25,40 | Nhãn "$500,000 cap" 25,5 | +0,1 s **đạt** | – | Chấm trắng chạy dọc vạch 27,0–28,0 khớp "every quarter" @27,90: tốt. |
| b3 (ngữ nghĩa) | – | 23,5–29,0: đường **giá nhà** (home value) đã vượt vạch trần ở cuối | – | – | Đặt trần lãi cạnh **giá trị nhà** trong 6 s khiến người xem tưởng "đã vượt trần" trước khi khái niệm lãi được giải thích. |
| b4 | "gain on paper" @30,00 | Không đổi gì trên biểu đồ; chỉ dòng chân "A home that rose like the Phoenix average" mờ 30,0 | **không có hình** | – | |
| b4 | "the **$200,000**" @33,96 | Thanh "$200,000 paid" 35,5 | **Trễ ~1,5 s** | – | Intent: thẻ $200,000 **lớn theo đường** ("grown with the index" @35,7–36,5) – không có. |
| b4 | "**less** the $200,000" @37,28–38,6 | Nhãn "− $200,000 paid" 37,0; đường trượt xuống 37,5–39,5; nhãn "gain on paper" 39,5 | ~0 s **đạt** | slide_down 37,06 (−0,2 s) **đạt** | Khoảnh khắc tốt nhất: phép trừ thấy được. |
| b5 | "well **under** the line" @42,82–43,76 | Nhà chạy lại từ 2000 (40,5) trên đường lãi, ở 2007–2009 | – | Âm dữ liệu có (≈ −30…−20 dBFS) | Intent: **vùng dưới vạch tô nhạt + ngoặc khoảng cách** – **không có**. Thay bằng "chạy lại" toàn bộ. |
| b6 | "second quarter of **2022**" @46,26 | Lịch 2019 ở 46,0; 2022 ở 47,0 | **Trễ ~0,8 s** | – | |
| b6 | "**crosses**" @47,96 | Đầu đường chạm vạch ~47,0–47,5; nhãn "Over: Q2 2022" 48,0 | Chạm sớm ~0,5 s; nhãn +0,05 s | chime 47,88 **đạt** (phổ thấy chuỗi hài sáng 48–49 s) | Không thấy "tia sáng ở điểm cắt". |
| b7 | "slips back under" @49,30 | 49,0–50,5 nhà gần như đứng ở vạch, lịch kẹt "2022" | Không thấy rõ trượt xuống | Dữ liệu tắt/đứt quãng 48–50 | Intent "phần vượt tắt màu" – không thấy. |
| b8 | "Q2 **2023**" @52,38 / "stayed above" @54,08 | Lịch 2023 ở 51,0; nhãn "Stayed over since Q2 2023" 51,5 | **Sớm ~0,9 s** (so với "2023") / ~2,5 s (so với "stayed") | Nốt dữ liệu tới 54,4 | Đoạn trên vạch tô cam: đạt. |
| b9 | "this is the **gain**" @59,74–60,24 | Thẻ "≈$558,100" 59,5 → số lớn giữa trên 60,0 | **đạt** | swish 59,75, tick 60,73 | **Khác intent**: số bay lên tiêu đề, **không bay vào biển trên nhà Rosa & Frank** (họ đã mất từ 5,5). |
| b10 | "past the **cap**" @62,06–62,44 | Nhãn "past the cap" 62,0 | **đạt** | impact **61,96** — đè lên chữ "past", sớm 0,5 s so với "cap" | Intent "chồng lãi đẩy xuyên trần" – không thấy chuyển động đẩy, chỉ nhãn. |
| b11 | "**3.8** times" @65,36–65,72 | "×3.8" + nhà 2026 cao lên 65,0–66,5 | **đạt** | rise 65,37 **đạt** | Đúng intent (chiều cao ∝ chỉ số). Nhưng biểu đồ cũ (vạch "$500,000 cap") còn **bóng mờ** phía sau suốt 63,5–69. |

## 2. Chuyển cảnh (mọi lần đổi hình)

1. **1,0** nhãn "paid $200,000 in 2000" bật ra – có lý do (đặt số gốc). Liền.
2. **1,5–2,0** vạch trần trượt vào từ trên – liền, khớp ý.
3. **5,0–5,5** nhà → mây "?", cặp đôi mờ đi – biến đổi liên tục, khớp "can't see their house". Nhưng mất nhân vật vĩnh viễn.
4. **9,0–13,5** nhà nhỏ SOLD bật quanh nhà mây – có lý do (nhiều giao dịch).
5. **13,5–15,0** gom: nhà nhỏ thu nhỏ, nhà mây tụt thành nhà nhỏ trên cọc – liên tục nhưng **ý gãy**: không có "đường" để gom vào.
6. **15,5** lịch bật lên + bắt đầu vẽ đường 16,5 – liền.
7. **23,5** vạch trần xuất hiện tại chỗ – chấp nhận, nhưng mất ý "rơi và khoá".
8. **35,5–39,5** thanh $200k trồi lên, cả đường trượt xuống, nhãn "home value" → "gain on paper" – **chuyển cảnh tốt nhất**, biến đổi liên tục mang nghĩa.
9. **40,0–40,5** cọc/nhà ở 2026 biến mất, lịch nhảy về "2000" (xám), nhà xuất hiện lại góc trái – **GÃY**: tua lại không có dấu hiệu tua (không thấy playhead quay về, đường đã vẽ sẵn mà nhà chạy lại trên đó).
10. **56,5–59,5** đẩy camera vào nhẹ – có lý do (tập trung đầu đường), nhưng xén mép trái.
11. **59,5–60,0** thẻ nhỏ "≈$558,100" → số lớn trên đầu – liên tục, nhưng điểm đến sai ý đồ.
12. **62,5–63,5** hoà tan biểu đồ → hai nhà "2000 / 2026 Q2" – **GÃY**: chuyển từ đại lượng *lãi* sang *giá* không có cầu nối, cọc lãi không biến thành nhà 2026; bóng vạch trần còn lại gợi liên hệ sai giữa nhà ×3,8 và trần.
13. **65,0–66,5** nhà 2026 cao lên + tiêu đề – liền, khớp ý.

## 3. Nhịp

**Chùng (hình đứng yên khi lời chạy > 3 s):**
- **5,5–9,0 (3,5 s)**: nhà mây đứng yên đúng lúc lời nói "let its value rise exactly like the Phoenix Area Home Price Index". Chữ "rise" không có chuyển động nào.
- **28,5–35,0 (~6,5 s)**: biểu đồ đứng yên hoàn toàn trong "And here's their gain on paper. For a home that rose like the average, the $200,000" – chỗ chùng nặng nhất, đúng ngay lúc giới thiệu khái niệm chính (lãi).
- **54,5–59,0 (~4,5 s)**: gần như đứng yên (chỉ đẩy camera rất chậm 57–59) trong "So on paper, if their home rose like the Phoenix average".
- Nhẹ: 21,0–23,0 (2 s), 49,0–50,5 lịch kẹt "2022".

**Dồn / rối:**
- **13,0–14,5**: ~15 nhãn "SOLD" đỏ chen nhau (không đọc được), nhãn "many sales → one average", dòng chân "US only…" vừa hiện, đồng thời thu gom – quá nhiều thứ trong 1,5 s.
- **59,5–62,5**: số lớn, phụ đề "gain on paper · the number from the opening", "Over: Q2 2022", "Stayed over since Q2 2023" (tới 59,5), "past the cap", đổi dòng chân, + swish/tick/impact trong 2,2 s.
- **40,5–54,5**: phần "chạy lại" 14 s lặp lại cùng quãng 2000→2026 đã xem ở 15,5–21,0 – tổng thời lượng dành cho việc vẽ đường quá dài so với thông tin mới.

## 4. Lớp bắt buộc

| Lớp | Có/từ lúc | Vị trí | Đọc được ở 25 %? | Vấn đề |
|---|---|---|---|---|
| ILLUSTRATIVE | Mọi khung 0–69 | Góc trên phải, huy hiệu viền cam | Có (nhận ra được ngay cả ở khung thu nhỏ ~15 %) | Sát nhãn "Stayed over since Q2 2023" (51,5–59,5) và tiêu đề "Phoenix-area prices since 2000" (65,5–69) – gần chạm. |
| Nguồn "Source: FHFA via FRED" | 11,0–69 | Trên trái, chữ xám nhỏ | **Khó** – ở khung ~15 % phải căng mắt; ở 25 % ước tính sát ngưỡng | **65,0–66,0**: tiêu đề "Phoenix-area prices since 2000" dính liền ngay sau chữ "FRED" (chồng/chạm). Ở 65,0 có bóng tiêu đề mờ đè vùng nguồn. |
| History-not-forecast "US only · history, not a forecast" | 14,5–69 | Dưới trái, xám nhỏ | **Khó** (tương phản thấp) | 14,0–14,5: chồng sát nhãn "many sales → one average". |
| Đối trọng "A home that rose like the Phoenix average" → "A measurement, not a tax bill or a next step" | 30,0–61,5 → 62,0–69 | Dưới phải, xám nhỏ | **Khó** | Đổi câu lúc 61,5–62,0 đúng giữa đỉnh căng – mắt đang ở số lớn, không ai đọc. Dòng đầu xuất hiện 30,0 gần như là "hình" duy nhất cho "gain on paper". |

Không có lớp nào đè lên dữ liệu chính. Chữ chồng / cắt mép thấy được:
- **12,0–14,0**: nhà/nhãn "SOLD" tràn ra mép trái và phải ("SC" bị cắt ở 12,0; 14,0 nhà bị cắt mép trái).
- **16,5–18,0, 37,5**: nhãn "home value" nằm đè lên đường.
- **44,5–46,5**: cọc nhà che nhãn "gain on paper" → đọc thành "gain  paper", "gain on pap".
- **48,0–58,5**: "Over: Q2 2022" nằm đè lên vạch trần/đường cam sát nhà.
- **57,5–59,5**: camera đẩy vào làm nhãn "$500,000 cap" dạt sát mép trái, đầu đường cong bị xén.
- **62,0–62,5**: "past the cap" sát mép phải.
- **63,5–69**: bóng mờ "$500,000 cap" và đường cũ còn sau cảnh hai nhà.

## 5. Âm

- **Lời rõ?** Phần lớn có: lời đỉnh −10…−5 dBFS, nhạc −45…−30, room tone −60 phẳng. Hai chỗ lớp phụ lấn:
  - **impact 61,96** (đỉnh ~−8 dBFS, ngang lời) rơi đúng lên "past the cap" (62,06–62,44) → che câu quan trọng nhất.
  - Âm dữ liệu **41–47 s** đỉnh ~−20 dBFS, chỉ cách lời ~10 dB, chạy dưới "sits well under the line / Then in the second quarter of 2022" – nghe được nhưng bắt đầu cạnh tranh; nên duck thêm khi có lời.
- **thud 23,71**: đỉnh ~−7 dBFS, to ngang lời – rơi vào khe giữa "cap." và "A flat line" nên không che lời, nhưng quá nặng cho cảm xúc "chắc, cố định" (0,45); nên giảm ~6–8 dB.
- **Nhạc theo bản đồ căng–chùng?** Chỉ một phần. Mức nhạc ~−40 ở 0–40 s, nhích lên ~−33 ở ~41–62 s, rồi hạ ~−45 sau 63 s và tắt dần 68,5–69,6. Các bước trong bản đồ (0,8 ở 44,5; tụt 0,6 ở 48,8; 0,85→1,0 ở 56,5–61,3) **không nghe ra thành biến động mức**; đỉnh 1,0 ở 61,3 không cao hơn đoạn 44–48. (Có thể căng bằng phối khí – không xác định được từ file.)
- **Khoảng lặng sau "past the cap"**: lời dừng 62,7, nói lại 63,64 → ~0,9 s. SFX impact tắt dần 62–63,5, nhạc hạ sau ~63, room tone giữ sàn −60 → **có chuyển tiếp**, không có lỗ chết. Nhưng do impact sớm 0,5 s, "cú đánh" không rơi sau chữ "cap" mà trước nó; khoảng lặng vì thế bị impact lấp, không thấy được nhịp "nín thở".
- **Âm dữ liệu nghe được?** Có, ở 16–22 và 41–55 (−30…−20 dBFS), 90 nốt 15,8–54,4. Ở b1, tick chỉ 11,93–13,49 (đều 0,12 s) trong khi nhà bật từ 9,0 → không "đọc" được nhà. Sau 54,4 không còn "nốt giữ sáng" cho b8 (lời "stayed above" 54,08–54,38 vừa hết là âm dữ liệu tắt) – chấp nhận. Âm dữ liệu đứt quãng 48–50 (b7 "đi xuống" không nghe rõ là đi xuống).
- **Hiệu ứng thừa/khó chịu**: impact 61,96 (đè lời, quá to); thud 23,71 (quá to); 12 tick máy móc đều nhịp 11,93–13,49 (nghe như đồng hồ, không phải dữ liệu). Chime 47,88 sáng, rộng tới ~7 kHz trên phổ – đúng chỗ, mức vừa.

## 6. Chấm điểm (so Vox / 3Blue1Brown / WSJ)

| Tiêu chí | Điểm | Lý do ngắn |
|---|---|---|
| Hình mang nghĩa | **3/5** | Phép trừ $200k (35,5–39,5) và ×3,8 (65–66,5) là chuyển động mang nghĩa đúng chất 3B1B; nhưng không có "nhiều nhà → một đường", không ngoặc khoảng cách, không đẩy xuyên trần, mất nhân vật chính. |
| Liền mạch hình–lời–âm | **2/5** | Lịch lệch −2,2/+1,2 s (b2), $200k trễ 1,5 s, tick trễ 2,9 s, impact đè lời; hai chuyển cảnh gãy (40,0 và 62,5). |
| Nhịp | **3/5** | Ba đoạn chùng (5,5–9,0; 28,5–35,0; 54,5–59,0) và đoạn chạy lại 14 s; hai điểm dồn (13–14,5; 59,5–62,5). |
| Âm | **3/5** | Lời nhìn chung rõ, room tone sàn ổn, chime/swish/rise đúng chỗ; nhưng impact che "past the cap", thud quá to, nhạc không thể hiện bản đồ căng. |

### Năm sửa quan trọng nhất

1. **28,5–35,0 – lấp khoảng chết bằng hình "lãi"**: ở "gain on paper" @30,0 cho thẻ "$200,000" xuất hiện tại điểm 2000 của đường; đưa thanh "$200,000 paid" lên đúng @33,96 (đang 35,5); cho thẻ lớn dọc theo đường đúng "grown with the index" @35,7–36,5, rồi giữ phép trượt xuống hiện có (37,06–39,5).
2. **61,96 impact – dời và hạ**: đặt impact ở ~62,50 (ngay sau "cap" @62,44), giảm ≥10 dB so với hiện tại, để khoảng 62,7–63,6 là khoảng lặng thật; đồng thời giảm thud 23,71 khoảng 6–8 dB. Cho nhạc lên thực sự theo bản đồ 56,5→61,3 rồi nhả ở 62,5.
3. **Giữ nhân vật & sửa hai chuyển cảnh gãy**: đưa nhà Rosa & Frank trở lại ở 56–60, cho "$558,100" bay vào biển trên nhà ấy (b9); ở 62,5–63,5 biến *chính nhà ấy* thành nhà "2026 Q2" (thay vì hoà tan), xoá bóng vạch "$500,000 cap" khỏi cảnh ×3,8. Ở 40,0–40,5 cho tua ngược thấy được (đầu đường chạy lùi về 2000) hoặc bỏ phần chạy lại.
4. **15,5–21,0 – khoá lịch theo lời**: giữ lịch "2000" tới "2000" @17,70, rồi quét để chạm "2026 Q2" đúng "2026" @19,76 (đang 21,0); ở b6 cho lịch tới 2022 đúng @46,26 và đầu đường chạm vạch đúng "crosses" @47,96 (đang ~47,0–47,5). Thêm vùng tô + ngoặc khoảng cách ở "well under the line" @42,8–43,8 như intent b5.
5. **5,5–14,5 – "rise" và dữ liệu nghe được**: cho cọc/giá trị nhà mây bắt đầu nhích lên ở "rise" @7,04; tick một nốt cho **mỗi** nhà SOLD từ 9,0 (không phải chuỗi đều 11,93–13,49); gom các nhà nhỏ thành **một đường** thấy được ở 14,45 (âm gather đã đúng mốc). Đồng thời giảm số nhãn SOLD ở 13–14,5 và tách "many sales → one average" khỏi dòng chân "US only…", sửa va chạm nhãn ở 44,5–46,5 và 65,0–66,0.
