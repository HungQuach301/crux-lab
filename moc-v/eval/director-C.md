# Đánh giá đạo diễn: bản C (đoạn 0–69 s)

Nguồn đã xem: sheet-1/2 (khung hình mỗi 0,5 s), audio.png (mức từng lớp và phổ), transcript.txt (mốc từ theo ASR), events.txt, intent.txt.
Lưu ý: hình chỉ lấy mẫu mỗi 0,5 s, nên độ lệch hình ghi bên dưới có sai số ±0,25 s. Mức âm đọc bằng mắt từ biểu đồ, nên là ước lượng.

---

## 1. Các chỗ LỆCH giữa hình, lời và âm

Chuẩn: hình xuất hiện đúng lúc từ khoá ±0,2 s. ✔ = đạt; ✖ = lệch.

| Beat | Từ khoá (mốc lời) | Hình xuất hiện | Lệch | Âm phản ứng | Khác ý đồ intent |
|---|---|---|---|---|---|
| b0 | "cap?" 3,20 | Vạch trần mờ dần hiện từ 1,5; dấu "?" lúc 3,0 | vạch sớm khoảng 1,7 s (chấp nhận được vì là câu hỏi mở); "?" ✔ | riser 1,52, dâng tới "cap?" ✔ | Vạch không "hạ xuống trên mái" mà chỉ mờ dần hiện ra, đứng yên ở mép trên. Nhãn "the cap" mờ, dính sát dưới badge ILLUSTRATIVE |
| b1 | "can't see their house" 4,74–5,32 | Nhà và Rosa & Frank tan thành bóng nét đứt lúc 5,0–5,5 | ✔ | whoosh_soft 4,96 ✔ | Vạch trần và dấu "?" biến mất lúc 5,5 mà không có lý do |
| b1 | "Phoenix… Home Price Index" 9,08–10,34 | Nhà nhỏ bật lên từ 9,0 đến 11,5 | ✔ (bắt đầu đúng "Phoenix") | **tick 11,93–13,49: trễ khoảng 3 s** so với lúc nhà bật (9,0–11,5); lúc tick vang thì nhà đã bắt đầu co lại | Intent: mỗi nhà một tick. Thực tế các tick không gắn với nhà nào |
| b1 | "Federal Housing Finance Agency" 11,32 | Thẻ "Source: FHFA via FRED" lúc 11,0 | sớm khoảng 0,3 s, ✔ gần đạt | – | – |
| b1 | "average of many sales" 13,60–14,40 | Nhà co lại về gốc trục 13,0–14,5; một nhà ở gốc lúc 15,0 | ✔ | gather 14,45 đúng "sales" ✔ | **Không thấy nhiều nhà gom thành một ĐƯỜNG.** Chúng gom về một ĐIỂM, nên ý "chỉ số = trung bình nhiều giao dịch" chưa hiện thành hình |
| b2 | "from 2000" 17,70 | Đường bắt đầu vẽ từ 15,5; tới 17,0 đã ở năm 2006 | **hình đi trước lời khoảng 2 s** (khi lời nói "2000" thì hình đã ở 2006–2009) | nốt dữ liệu từ 15,8 ✔ | – |
| b2 | "2026" 19,76 | Thẻ năm "2026 Q2" lúc 21,0 (lúc 20,0 thẻ còn ghi 2021) | **trễ khoảng 1,2 s** | – | Intent muốn giá hiện trên nhà tăng dần. Thực tế chỉ có thẻ năm, không có giá |
| b3 | "Here's the cap" 23,40 | Vạch ngang hiện lúc 23,5 | ✔ (+0,1) | thud 23,71 (+0,3) ✔ | Vạch mờ dần hiện ra chứ không "rơi xuống rồi khoá" |
| b3 | "$500,000" 25,40 | Nhãn "$500,000 cap" lúc 25,5 | ✔ | drone_on 23,71 ✔ | – |
| b3 | "same in every quarter" 27,20–28,34 | Vạch tick nhỏ chạy dọc vạch trần 27,0–28,0 | ✔ | – | Có ý nghĩa, tốt |
| b4 | "their gain on paper" 30,00 | **Không có gì xảy ra.** Chỉ có chú thích nhỏ góc phải dưới hiện ra | ✖ (thiếu hình) | – | Lời đã giới thiệu "gain" mà đường vẫn tên "home value" |
| b4 | "a home that rose like the average" 31,64–32,74 | Chú thích "A home that rose like the Phoenix average" lúc 30,0–30,5 | sớm khoảng 1,5 s | – | – |
| b4 | "the $200,000, grown with the index" 33,96–36,50 | Cột và nhãn "$200,000 paid" lúc 35,5 | **trễ khoảng 1,5 s, và SAI NGHĨA.** Lời đang nói 200k *lớn theo chỉ số* (giá trị nhà), hình lại ghi "paid" (khoản đã trả, thuộc vế "less… they paid") | – | Intent: thẻ $200,000 *lớn theo đường*. Thực tế không có thẻ nào lớn theo đường |
| b4 | "less" 37,28; "$200,000 they paid" 38,18–39,60 | Dải xanh trải ngang 37,0; nhãn "− $200,000" 37,0–38,0; đường trượt xuống 37,5–38,5; nhãn "gain on paper" 39,5 | dải ✔; "−$200,000" sớm khoảng 1 s; "gain on paper" ✔ | slide_down 37,06 (sớm khoảng 0,2) ✔ | Phép trừ đã thấy được. Đây là đoạn mang nghĩa tốt nhất, tuy chữ còn chồng nhau (mục 4) |
| b5 | "most of these years… under the line" 41,10–43,76 | Ngôi nhà đánh dấu NHẢY từ 2026 về 2000 lúc 40,5 rồi chạy lại; ô tối tô vùng 2000–2011 lúc 43,0 | ô tô ✔ ("under" 43,18) | âm dữ liệu khá to (khoảng −20 đến −30 dBFS) trong 41–47 | Intent: tô vùng dưới vạch trên *phần lớn* số năm và có ngoặc lớn chỉ khoảng cách. Thực tế chỉ tô 2000–2011, không có ngoặc |
| b6 | "2022" 46,26; "crosses" 47,96 | Nhà chạm và vượt vạch khoảng 47,0–47,5; nhãn "Over: Q2 2022" lúc 48,0 | điểm cắt sớm khoảng 0,5–0,9 s so với "crosses"; nhãn ✔ | chime 47,88, **trễ khoảng 0,4–0,6 s so với khung cắt**. Intent đòi ±1 khung | **Không thấy tia sáng ở điểm cắt** |
| b7 | "slips back under" 49,30–49,80 | Nhà đi qua chỗ trũng nhỏ 49,0–50,0; khó thấy phần vượt "tắt màu" | ~ | **Âm dữ liệu gần như tắt** (rơi về −80 trong khoảng 47,5–50) thay vì "đi xuống" | Đoạn trượt xuống quá nhỏ trên hình, gần như không đọc được |
| b8 | "Q2 2023" 51,64–52,38 | Nhãn "Stayed over since Q2 2023" lúc 51,5; đoạn cam kéo dài 52–55 | ✔ | nốt dữ liệu kết thúc 54,4 | ✔ |
| b9 | "So on paper" 56,04 | Camera đẩy vào (zoom) 56,5–59,0 | ✔ | – | Zoom cắt mép trái: mất nhãn trục năm |
| b9 | "this is the gain" 59,74–60,24 | "$558,100" nhỏ cạnh nhà lúc 59,5; số lớn "≈ $558,100" lúc 60,0; phụ đề "from the opening" lúc 61,0 ("opening" 60,82) | ✔ | swish 59,75 ✔; tick 60,73 ✔ | **Số KHÔNG bay vào biển trên nhà Rosa & Frank.** Rosa & Frank đã biến mất từ 5,5 và không quay lại; số chỉ hiện ở đầu khung |
| b10 | "past the cap" 62,06–62,44 | Ngoặc và nhãn "past the cap" lúc 62,0 | ✔ | impact 61,96 ✔ (nhưng to, xem mục 5) | **Không có chồng tiền đẩy xuyên vạch trần.** Cú đỉnh căng chỉ là một nhãn chữ |
| b11 | "Phoenix area prices" 63,64 | Tiêu đề "Phoenix-area prices since 2000" lúc 65,5 (mờ từ 65,0) | **trễ khoảng 1,9 s** | – | – |
| b11 | "3.8" 65,36–65,72 | Cột 2026 cao lên 65,0–66,0; nhãn "×3,8" lúc 65,5 | ✔ | rise 65,37 ✔ | Từ 64,0 đến 64,5 hai cột cao BẰNG nhau, nên khoảng 1 s hình nói sai rằng 2026 bằng 2000. Intent: chiều cao ∝ chỉ số; khi đứng yên thì đạt |

**Tóm lại:** các mốc "chốt" khớp đúng: 23,4 / 25,4 / 37,3 / 48,0 / 51,5 / 60,0 / 62,0 / 65,4. Lệch nặng ở b2 (17,7 và 19,8), b4 (30,0; 33,96 sai nghĩa), b1 (tick trễ 3 s) và b11 (tiêu đề trễ 1,9 s). Ba hành động mang nghĩa của intent bị thay bằng nhãn chữ hoặc bị bỏ: gom nhiều nhà thành một đường (b1); số bay vào nhà Rosa & Frank (b9); chồng tiền xuyên vạch trần (b10).

---

## 2. Chuyển cảnh

| # | Mốc | Đổi gì | Đánh giá |
|---|---|---|---|
| 1 | 5,0–5,5 | Nhà và Rosa & Frank tan thành bóng nét đứt | **Có lý do**, khớp "can't see their house". Nhưng vạch trần và "?" biến mất cùng lúc, mất mạch câu hỏi "has it passed the cap?" (**gãy nhẹ**) |
| 2 | 9,0–11,5 | Nhà nhỏ bật lên quanh bóng nhà | Có lý do (nhiều giao dịch) |
| 3 | 13,0–15,0 | Đám nhà co lại về gốc trục; bóng nhà biến mất; trục năm hiện | Biến đổi liên tục, nhưng về một **điểm** chứ không về một **đường**. Đạt một nửa |
| 4 | 15,5–21,0 | Nhà cưỡi đầu đường, vẽ quý theo quý | Liên tục, tốt |
| 5 | 23,5 | Vạch trần hiện, đường giá mờ đi | Có lý do. Mờ dần thay vì rơi xuống, nên thiếu lực |
| 6 | 37,0–38,5 | Dải $200k, đường trượt xuống, đổi màu xanh → trắng | **Liên tục, mang nghĩa**. Là chuyển hình tốt nhất đoạn này |
| 7 | 40,5 | Ngôi nhà đánh dấu **nhảy tức thời** từ 2026 về 2000 | **GÃY.** Không có tua ngược hay chuyển hình nào; người xem không biết vì sao đi lại từ đầu |
| 8 | 56,5–59,0 | Camera đẩy vào | Có lý do (tập trung), nhưng cắt mép trái và mất trục năm |
| 9 | 63,0–64,0 | Biểu đồ đường **hoà tan chồng** sang hai cột nhà | **GÃY / chồng hình.** Khung 63,5 có hai lớp cùng lúc: cột đè lên đường cũ, "gain on paper" nằm dưới cột. Đường không biến thành cột |
| — | toàn đoạn | Rosa & Frank (hero) biến mất từ 5,5 tới hết | **Gãy câu chuyện.** Lời liên tục nói "their gain", "their home" mà hình không còn nhân vật |

---

## 3. Nhịp

**Chùng** (hình đứng yên khi lời chạy quá 3 s):
- **5,5–9,0 (khoảng 3,5 s):** chỉ có bóng nhà nét đứt đứng yên, trong lúc lời nói "so we let its value rise, exactly like the Phoenix…". Chữ "rise" (7,04) không có hình nào tăng.
- **25,5–35,0 (khoảng 9,5 s): chùng nặng nhất.** Biểu đồ gần như đứng yên. Chỉ có tick chạy dọc vạch (27–28) và chú thích mờ hiện ra (30). Trong lúc đó lời giới thiệu khái niệm chính "gain on paper".
- 66,0–69,0 (3 s): giữ khung kết. Chấp nhận được vì là nhịp thả.
- 21,0–23,5 (2,5 s): đứng yên dưới ngưỡng 3 s. Ổn.

**Dồn / rối:**
- **37,0–38,5:** dải xanh, nhãn "−$200,000", nhãn "$200,000 paid", đường trượt xuống và đổi màu, tất cả trong 1,5 s và chữ chồng nhau. Nên giãn ra theo hai vế lời: "grown with the index" (35,7) và "less… they paid" (37,3–39,6).
- **47,5–49,0:** nhà, điểm cắt và nhãn "Over: Q2 2022" dính vào nhau tại cùng một điểm.
- **52–59:** hai nhãn cam xếp chồng ("Over: Q2 2022" và "Stayed over since Q2 2023"), thêm icon nhà, đều nằm ở góc phải trên.
- **63,5:** hai cảnh chồng nhau (xem chuyển cảnh #9).

---

## 4. Lớp bắt buộc

| Lớp | Có không, từ lúc nào | Đè lên hình? | Đọc được ở 25 %? |
|---|---|---|---|
| ILLUSTRATIVE | Có, góc phải trên, suốt 0–69 | Không đè lên dữ liệu. Nhưng 1,5–5,0 nhãn "the cap" nằm sát ngay dưới badge, gần dính | **Không đọc được.** Badge rất nhỏ (chiều cao chữ chỉ khoảng 1 % khung) |
| history-not-forecast ("US only · history, not a forecast") | Từ 14,5 tới hết, góc trái dưới | Không đè | **Không đọc được.** Chữ xám nhỏ trên nền đen |
| Nguồn ("Source: FHFA via FRED") | Từ 11,0 tới hết, góc trái trên | Từ 65,5 nằm sát tiêu đề "Phoenix-area prices since 2000"; hai chuỗi gần như chạm nhau | **Không đọc được.** Chữ xám rất nhỏ |
| Đối trọng ("A home that rose like the Phoenix average", từ 62,0 là "A measurement, not a tax bill or a next step") | 30,0–61,5, rồi 62,0–69 | Không đè | **Không đọc được.** Chữ nhỏ và mờ, sát mép dưới phải |

**Chữ chồng nhau:**
- 37,0: "home value" × "−$200,000" (đọc thành "home-v$200,000").
- 36,5–39,0: "$200,000 paid" bị chính đường giá cắt ngang.
- 17,5–18,0: "home value" bị đường và icon nhà đè.
- 48,0–48,5: "Over: Q2 2022" chạm icon nhà.
- 63,5: "gain on paper" nằm dưới cột 2026.

**Cắt mép:**
- 14,0–14,5: trục năm bị mờ hoặc tràn trái.
- 56,5–63,0: đường giá và nhãn năm bị cắt ở mép trái sau khi zoom; trục năm mất hẳn từ khoảng 57,0.

---

## 5. Âm

- **Lời rõ:** đỉnh lời khoảng −5 đến −10 dBFS. Nhạc đều ở khoảng −35 đến −45, không lấn lời. **Ngoại lệ là hiệu ứng (sfx):**
  - thud 23,71 lên khoảng −8 dBFS, ngang lời. Nó rơi vào khe giữa "cap." và "A flat" nên chưa che từ, nhưng quá to.
  - **impact 61,96 lên khoảng −10 dBFS, đè trúng "past the cap" (62,06–62,44)**, đúng câu đỉnh của đoạn.
  - chime 47,88 trùng "crosses" (47,96).
  - slide_down khoảng 37,06 có đỉnh khoảng −15, sát "less" (37,28).
- **Nhạc theo bản đồ căng–chùng:** chỉ theo yếu. Đường nhạc gần như phẳng (−35 đến −45) trong khi bản đồ đi từ 0,35 lên 0,8 (44,5) và 1,0 (61,3). Chỉ thấy nhạc nhích lên khoảng −30 trong 44–56, rồi rơi sau 62. Nghe không ra cao trào ở 61,3.
- **Khoảng lặng sau "past the cap":** lời ngắt từ 62,70 đến 63,64 (khoảng 0,9 s). Nhạc nhả xuống khoảng −50 và room tone giữ sàn khoảng −60 đúng ý đồ. Nhưng đuôi impact phủ phần đầu khoảng lặng. Hình dissolve 63,0–64,0 trôi qua khoảng lặng thay vì đánh dấu nó. Nhạc tụt về khoảng −80 quanh 67–68, nên kết bị hụt sàn.
- **Âm dữ liệu:**
  - Nghe được trong 16–22 (khoảng −30) và 41–47 (khoảng −20 đến −30). Trong 41–47 nó to hơn nhạc và chỉ thấp hơn lời khoảng 10–15 dB. Intent ở đây muốn "trầm, thưa", nên nên hạ 6 dB.
  - Tắt hẳn quanh 47,5–50, đúng lúc "slips back under", trong khi intent muốn nó đi xuống.
  - Phổ cho thấy dải vạch đều ở 15,3–15,6, có thể là khởi động chuỗi nốt.
- **Hiệu ứng thừa hoặc khó chịu:**
  - 14 tick liên tiếp 11,93–13,49 (cách nhau 0,12 s) không gắn với hình nào và nghe như máy đếm.
  - thud và impact quá to.
  - riser 1,52 và whoosh 4,96 ổn.

---

## 6. Chấm điểm (1–5, so với Vox / 3Blue1Brown / WSJ)

| Tiêu chí | Điểm | Lý do ngắn |
|---|---|---|
| Hình mang nghĩa | **3** | Phép trừ 200k (37–39), tick dọc vạch trần, ×3,8 có ý nghĩa. Nhưng ba hành động then chốt (gom thành đường, số bay về nhà, chồng tiền xuyên trần) bị thay bằng nhãn; hero biến mất |
| Liền mạch hình–lời–âm | **3** | Phần lớn mốc chốt khớp ±0,2. Lệch 1–3 s ở b1, b2, b4, b11; "$200,000 paid" sai nghĩa lúc 35,5 |
| Nhịp | **2** | Đứng yên khoảng 9,5 s ở 25,5–35 và 3,5 s ở 5,5–9; dồn chữ ở 37–38,5; nhảy tức thời ở 40,5 |
| Âm | **3** | Lời sạch, nhạc thấp hợp lý. Nhưng nhạc không theo bản đồ căng, impact che "past the cap", tick lệch 3 s, âm dữ liệu tắt ở b7 |

### Năm sửa quan trọng nhất

1. **25,5–35,0, lấp đoạn chùng và sửa nghĩa b4:**
   - Lúc "their gain on paper" (30,0): làm đường nhấp sáng.
   - Lúc "$200,000" (33,96): gắn thẻ "$200,000" vào gốc đường năm 2000 và cho thẻ lớn theo đường tới 2026 trong "grown with the index" (35,7–36,5).
   - Chỉ hiện "paid" và dải trừ ở "less" (37,28).
   - Tách nhãn "−$200,000" khỏi "home value".
2. **59,7–62,5, đưa hero trở lại:**
   - Rosa & Frank cùng ngôi nhà vào khung từ khoảng 56,0.
   - "$558,100" bay vào biển trên nhà (swish 59,75, tick 60,73 giữ nguyên).
   - Lúc "past the cap" (62,06): chồng tiền dưới nhà đẩy xuyên vạch trần.
   - Hạ impact khoảng 8–10 dB, hoặc đặt nó ở 62,50, sau chữ "cap".
3. **15,5–21,0, khoá thẻ năm theo lời:** bắt đầu vẽ ở 17,70 ("2000") hoặc kéo dài nét vẽ để thẻ "2026 Q2" chạm đúng 19,76. Thêm giá trên nhà tăng dần.
4. **9,0–15,0:**
   - Gắn mỗi tick với một nhà bật lên (9,0–11,5) thay vì loạt tick 11,93–13,49.
   - Ở 13,6–14,4 gom các nhà thành **một đường** (không phải một điểm).
   - Lấp 5,5–9,0 bằng chữ "rise" (7,04): bóng nhà nhích lên.
5. **Chuyển cảnh và lớp bắt buộc:**
   - 40,5: tua ngược có thấy được thay vì nhảy tức thời.
   - 63,0–64,0: cho hai đầu đường (2000, 2026) dựng thành hai cột, thay cho dissolve chồng; cột 2026 không được bằng cột 2000 lúc 64,0.
   - Tiêu đề b11 hiện ở 63,64.
   - Phóng ILLUSTRATIVE, nguồn, history-not-forecast và đối trọng lên khoảng 2× để đọc được ở 25 %.
   - Bỏ zoom cắt mép 56,5–63; tách tiêu đề khỏi dòng nguồn ở 65,5.
