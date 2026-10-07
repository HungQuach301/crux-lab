# Đánh giá đạo diễn — bản B (hướng 3D, 0–69,6 s)

Nguồn đã xem: sheet-1/2 (khung 0,5 s), audio.png (mức từng lớp + phổ), transcript.txt, events.txt, intent.txt. Mọi mốc dưới đây đọc từ các file đó; độ phân giải hình là 0,5 s nên sai số hình ±0,25 s.

## 1. Chỗ LỆCH hình / lời / âm

Chuẩn: hình khớp từ khoá trong khoảng ±0,2 s.

| Beat | Lời (mốc) | Hình xuất hiện | Lệch | Âm | Ghi chú so với intent |
|---|---|---|---|---|---|
| b0 | "cap?" 3,22 | vạch trần trượt ngang vào từ 1,5 s; "?" hiện 3,0 s | "?" khớp (−0,2) | riser 1,52, khớp | Vạch **trượt ngang ở mép trên**, không "hạ xuống phía trên mái" như intent. |
| b1 | "can't see their house" 4,74–5,32 | nhà và Rosa & Frank mờ đi 5,0–5,5 | khớp | whoosh_soft 4,96, khớp | Tốt. |
| b1 | "let its value **rise**" 7,04 | không có gì tăng lên; nhà ma đứng yên 5,5–9,0 | **thiếu hình** | — | Intent không đòi chuyển động ở đây, nhưng lời nói "rise" mà hình không có gì đi lên. |
| b1 | "Phoenix" 9,08 | nhãn "Phoenix area" 9,0 | khớp | — | |
| b1 | "Federal" 11,32 | thẻ "Source: FHFA via FRED" 11,5 | +0,2, khớp | — | |
| b1 | ticks (âm dữ liệu) | events: **12 tick 8,98–13,23**; nhà nhỏ chỉ bật lên **12,0–13,5** | **8 tick đầu (8,98–11,69) vang khi chưa có nhà nào, sớm ~3 s** | lệch | Ghi chú nói tick định ở 11,9–13,5, nhưng events.txt cho thấy chúng thực tế chạy từ 8,98. |
| b1 | "many sales" 14,12–14,40 | nhãn "many sales" 13,5 | sớm 0,6 s | — | |
| b1 | gom về một đường | nhà nhỏ bay về một chấm sáng 14,5–15,0, có nhãn "Phoenix-area average"; **15,5 chấm biến mất**, đường bắt đầu mọc từ nhà ở 16,5 | ý "gom → thành một ĐƯỜNG" bị đứt | gather 14,45, khớp với lúc gom | Chấm không trở thành đường. Nhà ma lại thành nhà đặc ở 15,5, trái với câu "we can't see their house". |
| b2 | "**2000**" 17,70 | lịch hiện 2000 ở **15,5**; lúc nói "2000" lịch đang ở **~2008–2009** (2006 ở 17,0, 2009 ở 17,5) | **sớm ~2,2 s** | nốt dữ liệu bắt đầu 15,8 | Lịch quét tuyến tính, không bám theo lời. |
| b2 | "second quarter of **2026**" 18,84–19,76 | lịch 2016 ở 19,0, 2018 ở 19,5; **2026 Q2 ở 21,0** | **trễ ~1,3 s** | | |
| b3 | "**cap**" 23,40 | vạch ngang hiện 23,5 | khớp | thud 23,71 (+0,3) | Vạch chỉ **bật ra**, không "rơi xuống rồi khoá" như intent. |
| b3 | "$500,000" 25,40 | nhãn "$500,000 cap" 25,5 | khớp | — | Tốt. |
| b3 | "same" 27,20 | "same in every quarter" mờ 27,0 → rõ 27,5 | khớp | drone giữ | Tốt. |
| b4 | "for a home that rose like the average" 31,38–32,74 | dòng "A home that rose like the Phoenix average" mờ dần vào từ 29,0, rõ ở 29,5 | sớm ~2 s | — | Chấp nhận được vì đây là lớp đối trọng. |
| b4 | "$200,000" 33,96 | khối xanh lam "$200,000" ở chân tháp **2026** lúc 34,0 | khớp | — | Intent muốn thẻ $200k ở 2000 rồi **lớn dần theo đường**. Ở đây khối nằm ở 2026 và **không lớn lên** suốt "grown with the index" (35,70–36,50). |
| b4 | "**less**" 37,32 / "they **paid**" 39,60 | khối tách ra thành cột "$200,000 paid" lúc 37,0; nhãn đổi "home value" → "gain on paper" lúc 38,5; cột lam đổi sang lục và ngắn lại ở 39,0 | "paid" hiện sớm 2,6 s; phép trừ khó đọc | slide_down 37,06, khớp với lúc tách | Không thấy rõ "CẢ ĐƯỜNG trượt xuống đúng $200,000". Người xem không thấy được phép trừ. |
| b4→b5 | im lặng 40,0–41,14 | **TUA NGƯỢC**: đường xám đi, nhà chạy ngược 2018 (39,5) → 2003 (40,0) → 2000 (40,5) rồi vẽ lại | không có trong intent hay lời | không có âm báo | Gây bối rối, xem mục 2. |
| b5 | "under the line" 43,18 | vùng tô dưới vạch và một vạch đứng mảnh (ngoặc khoảng cách) hiện 43,0 | khớp | âm dữ liệu **to nhất đoạn** (~−20 dBFS) 42–47 s | Intent muốn âm "trầm, thưa"; thực tế ngược lại. Vạch ngoặc quá mảnh, không phải "ngoặc lớn". |
| b6 | "**2022**" 46,26 | lịch 2021 ở 46,5–47,0, 2022 ở 47,5 | trễ ~1,2 s | riser 46,28 | |
| b6 | "**crosses**" 47,96 | đỉnh tháp chạm vạch 47,5; tia sáng và nhãn "Over: Q2 2022" lúc 48,0 | khớp | chime 47,88, khớp | Khoảnh khắc khớp tốt nhất của bản này. |
| b7 | "slips back under" 49,30 | nhãn "Over" mờ đi 49,5, mất ở 50,0; đỉnh tháp hạ nhẹ về sát vạch 50,0 | khớp nhưng chuyển động **rất nhỏ** | không nghe tách được nốt đi xuống | Phần vượt "tắt màu" chỉ thể hiện bằng nhãn mờ đi. |
| b8 | "**2023**" 52,38 | lịch 2023 ở 51,0; nhãn "Stayed over since Q2 2023" ở 51,5 | sớm 0,9–1,4 s | | Đoạn cam trên vạch kéo dài tới 2026: đúng intent. |
| b9 | "**this is the gain**" 59,80–60,22 | nhãn nhỏ "≈ $558,100" cạnh vạch từ **57,0**; số lớn "≈ $558,100" ở góc trên trái lúc 60,0 | nhãn nhỏ sớm 2,8 s; số lớn khớp | swish 59,75, tick 60,73 | Intent: số **bay từ đầu đường vào biển trên nhà**. Ở đây số đổi chỗ sang góc trái, không bay vào nhà. |
| b10 | "**past** the cap" 62,06 | nhãn "past the cap", quầng sáng ở vạch, khúc cam trên tháp lúc 62,0 | khớp | impact 62,76 (+0,3 sau "cap" 62,46) | Không thấy "chồng tiền đẩy XUYÊN vạch" như một chuyển động; trạng thái chỉ bật sẵn. |
| b11 | "Phoenix area prices" 63,62 | tiêu đề "Phoenix-area prices since 2000" chỉ hiện **67,5–68,0** | **trễ ~4 s** | | |
| b11 | "**3**.8 times" 65,36 | nhà 2026 vọt cao, có "×3.8", lúc 65,5 | khớp | rise 65,37, khớp | Tốt. Nhưng 64,0–65,0 có **hai nhà bằng nhau** gắn nhãn 2000 / 2026 Q2, sai nghĩa trong 1 s. |

## 2. Chuyển cảnh (mọi lần đổi hình)

1. **1,5–2,5 s**: vạch trần trượt vào. *Có lý do* (đặt câu hỏi). Nhưng nó chạy ngang chứ không hạ xuống.
2. **5,0–7,0 s**: Rosa & Frank tắt, nhà hoá ma, máy quay lùi và cao lên, lộ lưới nền. *Liên tục, khớp lời* ("can't see their house").
3. **12,0–14,0 s**: nhà nhỏ bật lên quanh nhà ma. *Liên tục.*
4. **14,5–15,0 s**: nhà nhỏ bay gom thành một chấm sáng. *Có lý do.*
5. **15,0 → 15,5 s**: chấm và lưới biến mất, nhà ma thành nhà đặc, lịch "2000" bật ra. **GÃY**: chấm "trung bình" không biến thành đường, và đường chỉ xuất hiện ở 16,5 s, mọc ra từ nhà.
6. **15,5–21,0 s**: nhà cưỡi đầu đường, tháp cao dần. *Liên tục, đây là chuyển động mang nghĩa tốt nhất* (chiều cao tháp ∝ giá).
7. **23,5 s**: vạch trần bật ra. Bị cắt ngang thay vì rơi xuống, nhưng *chấp nhận được*.
8. **37,0–39,0 s**: khối $200k tách thành cột "paid", nhãn đổi thành "gain on paper", cột đổi màu. **Rối**: đổi nhãn mà hình đường gần như không đổi, nên người xem không thấy phép trừ.
9. **39,5–40,5 s**: tua ngược 2026 → 2000 trong khoảng 1 s, đường cũ xám đi. **GÃY**: không có lời hay âm báo, người xem tưởng phim lỗi.
10. **41,0–47,5 s**: vẽ lại đường lãi từ 2000. *Liên tục.*
11. **43,0 s**: vùng tô dưới vạch hiện ra. *Khớp lời.*
12. **55,5–58,5 s**: máy quay đẩy vào và hạ góc. Nhãn "$500,000 cap" mất, trục rơi xuống đè lớp chú thích, lịch trượt ra mép trái. *Liên tục nhưng luộm thuộm.*
13. **60,0 s**: số lớn hiện ở góc trái, nhãn nhỏ biến mất. *Gần như cắt*, không có đường bay.
14. **63,0 → 64,0 s**: số mờ đi, vạch trần và đường biến mất, tháp chìm xuống. Một nhà khác trồi lên ở mép trái dưới (bị cắt mép ở 63,5), rồi thành hai nhà bằng nhau. **GÃY**: đổi không gian, mất nhân vật, và trong 1 s hình còn nói sai rằng giá không đổi.
15. **65,0–65,5 s**: nhà 2026 vọt cao, nhà 2000 co nhỏ, "×3.8". *Mang nghĩa, khớp lời.*
16. **67,5–68,0 s**: tiêu đề hiện ra. Muộn.

## 3. Nhịp

**Chùng** (hình đứng yên trong khi lời chạy quá 3 s):
- **5,5–12,0 s** (~6,5 s): nhà ma đứng yên, chỉ thêm nhãn "Phoenix area" ở 9,0 trong khi lời đọc "so we let its value rise, exactly like the Phoenix Area Home Price Index from the Federal…". Đây là chỗ chùng nặng nhất.
- **27,5–33,5 s** (~6 s): biểu đồ đứng yên, chỉ có dòng chú thích mờ vào ở 29,0, trong khi lời đọc "And here's their gain on paper, for a home that rose like the average".
- **34,0–36,5 s** (2,5 s): khối $200k đứng yên trong lúc lời nói "grown with the index". Chưa quá 3 s nhưng sai nghĩa.
- **66,0–69,6 s**: hình đứng yên khoảng 3 s ở đoạn kết. Chấp nhận được vì là cảnh thả.

**Dồn / rối**:
- **37,0–41,0 s**: tách cột, đổi nhãn, đổi màu và tua ngược dồn vào khoảng 4 s.
- **55,5–58,5 s**: máy quay di chuyển, nhãn mất, số nhỏ hiện ra và lịch trượt, tất cả cùng lúc.
- **15,5–21,0 s**: quét năm nhanh (≈4,7 năm/giây) và không bám lời. Không rối, nhưng mắt không kịp đọc lịch.

## 4. Lớp bắt buộc

- **ILLUSTRATIVE**: viền vàng góc trên phải, có mặt từ 0,0 đến hết, không bị đè. Ở 25 % kích thước vẫn nhận ra là một badge, nhưng chữ gần như không đọc được.
- **"US only · history, not a forecast"**: góc dưới trái, chỉ có từ **4,5 s**, nên **vắng 0–4,0 s** trong lúc lời đã hỏi về khoản lãi. Chữ xám nhỏ, tương phản thấp; ở 25 % **không đọc được**.
- **Nguồn "Source: FHFA via FRED"**: góc trên trái từ 11,5 s, khớp lời. Chữ xám nhỏ; ở 25 % khó đọc.
- **Đối trọng**: "A home that rose like the Phoenix average" từ 29,0 s, rồi "A measurement, not a tax bill or a next step" từ 63,0 s, ở góc dưới phải. Cỡ chữ và tương phản giống lớp history, nên ở 25 % cũng không đọc được.

**Chồng chữ và cắt mép**:
- **56,0–56,5 s**: nhãn trục (2000, 2010, 2020, 2026 Q2) rơi xuống **đè lên dòng chú thích dưới** ("US only…" và "A home that rose…"). "2000" bị **cắt mép trái** ở 56,0.
- **56,0–58,5 s**: thẻ lịch "2026 Q2" **đè lên "Source: FHFA via FRED"**, rồi bị **cắt mép trái** ở 57,5–58,5 (chỉ còn "26").
- **40,5–41,5 s**: nhãn "gain on paper" bị nhà ở mốc 2000 đè lên.
- **63,5 s**: nhà mới bị cắt ở mép dưới trái.
- **3,0–4,5 s**: "?" đè lên vạch trần. Có lẽ là chủ ý, không sao.

## 5. Âm

- **Độ rõ của lời**: đỉnh lời khoảng −8 đến −15 dBFS. Nhạc thường ở −30 đến −45 nên luôn dưới lời; âm dữ liệu ở −40 đến −25 nên phần lớn thời gian dưới lời 10–20 dB. Có ba chỗ lấn:
  - **42–47 s**: âm dữ liệu lên khoảng **−20 dBFS**, chỉ thấp hơn đỉnh lời khoảng 5–10 dB, và rơi đúng câu "For most of these years… Then, in the second quarter of 2022". Intent ở đây lại muốn "trầm, thưa".
  - **thud 23,71**: lớp sfx vọt lên khoảng **−8 dBFS**, to ngang đỉnh lời, đúng giữa "cap, a flat line".
  - **impact quanh 62 s**: lớp sfx cũng chạm khoảng **−8 dBFS**, sát chữ "cap".
- **Nhạc so với bản đồ căng–chùng**: nhạc bị duck sâu (−45 đến −50) ở 5–14 s, khớp mức 0,4. Mức 0,5 lúc 15,4 có lên nhẹ (khoảng −30 ở khe 15–16 s). **Đỉnh 0,8 lúc 44,5 không nghe thấy**: nhạc ở 45–47 s chỉ khoảng −40 đến −45, thấp nhất đoạn, nên phần căng do riser và chime gánh. Đoạn 51–62 s nhạc nhích lên khoảng −25 đến −30, khớp 0,75 → 1,0. Sau 63,5 s nhạc nhỏ dần về −80 lúc khoảng 67,5 s, nên **cảnh kết 67,5–69,6 không còn nhạc**, trong khi bản đồ vẫn ghi 0,35 lúc 68,1.
- **Khoảng lặng sau "past the cap"**: lời có khe 62,70–63,62 (0,9 s). Khe này bị **impact và nhạc còn ở khoảng −30 lấp kín**, nên không có khoảnh khắc "nhả" rõ. Nhạc chỉ bắt đầu rút từ khoảng 63,5. Room tone giữ sàn −60 suốt bài: đúng intent.
- **Âm dữ liệu**: chạy 15,8–54,4 s (90 nốt), nghe được trên phổ và trên đường mức. Ở b1 tick vang trước khi có nhà nhỏ khoảng 3 s (xem bảng). Ở b7 không thấy nốt đi xuống tách khỏi nền. b11 có rise 65,37 khớp ×3.8.
- **Hiệu ứng thừa hoặc khó chịu**:
  - thud 23,71 và impact quanh 62 quá to.
  - chime 47,88 trên phổ là một dải sáng phủ tới 8 kHz, kéo dài khoảng 47,9–49,5. Âm này sắc và đè lên "it crosses".
  - Dải hoạ âm quanh 15,3–15,7 s (có vẻ là gather) cũng sáng.
  - Tick dày 8,98–13,23 khi chưa có hình dễ thành tiếng gõ vô nghĩa.

## 6. Hướng 3D

**Chỗ 3D làm ý rõ hơn**:
- Tháp-nhà "cưỡi" đầu đường ở 15,5–21,0 và 41–55 s. Chiều cao tháp đọc như giá, và việc nhà vượt vạch ở 47,5–48,0 rất trực quan.
- Cặp nhà ×3.8 ở 65,5–69,0 đúng tỉ lệ. Đo trên khung 68,0 s: nhà 2000 cao khoảng 27 px, nhà 2026 khoảng 104 px, tức ≈ 3,85.

**Chỗ 3D chỉ trang trí hoặc gây nhiễu**:
- Lưới nền và máy quay lùi ở 5,5–12 s không mang dữ liệu.
- Mái nhà đặt trên đỉnh tháp **cộng thêm chiều cao không phải dữ liệu**, nên khó biết giá trị nằm ở chân mái hay đỉnh mái.
- Nhà ×3.8 có **mái bị kéo thành chóp nhọn**: tỉ lệ đúng nhưng hình nhà méo.

**Chỗ phối cảnh làm sai tỉ lệ dữ liệu**:
- **56–63 s**: máy quay hạ góc và đẩy vào. Vạch trần nghiêng và chạy chéo, phần 2000–2010 của đường bị nén hoặc trôi ra khỏi khung, trục bị ép. Khúc cam "vượt cap" trên tháp ở 61,5–62,5 trông dày khoảng 1/4 phần tháp dưới vạch, trong khi lãi chỉ vượt 58.100/500.000 ≈ 12 %. **Rất có thể phần vượt bị phóng đại**; ở độ phân giải này tôi không đo chắc được.
- **64,0–65,0 s**: hai nhà bằng nhau gắn nhãn 2000 / 2026 Q2 là sai dữ liệu trong 1 s.

## 7. Chấm điểm (so với Vox / 3Blue1Brown / WSJ)

| Tiêu chí | Điểm | Lý do chính |
|---|---|---|
| Hình mang nghĩa | **3/5** | Tháp cưỡi đường, khoảnh khắc vượt vạch và ×3.8 tốt. Phép trừ $200k, chấm gom → đường, số bay vào nhà thì hỏng hoặc thiếu. |
| Liền mạch hình–lời–âm | **2/5** | Lịch năm lệch 1–2 s, tick sớm 3 s, đoạn tua ngược không lời, tiêu đề trễ 4 s. Chỉ "crosses", "cap", "×3.8" là khớp. |
| Nhịp | **2/5** | Hai đoạn chùng khoảng 6 s (5,5–12 và 27,5–33,5); hai đoạn dồn (37–41 và 55,5–58,5). |
| Âm | **3/5** | Lời luôn nghe được, room tone ổn. Nhưng thud và impact quá to, âm dữ liệu lấn lời ở 42–47, đỉnh căng 0,8 không nghe thấy, không có khoảng lặng sau "cap", nhạc tắt trước cảnh kết. |

### Năm sửa quan trọng nhất

1. **Khoá lịch năm vào lời ở 15,5–21,0**: giữ "2000" tới chữ "2000" ở 17,70, quét tới "2026 Q2" đúng lúc 19,76. Hiện lịch sớm 2,2 s rồi trễ 1,3 s. Làm tương tự cho "2022" (46,26, hiện trễ 1,2 s) và "2023" (52,38, hiện sớm 1,4 s).
2. **Sửa b1 (5,5–16,5)**:
   - Dời 12 tick về đúng lúc nhà nhỏ bật lên 12,0–13,5, thay vì 8,98–13,23.
   - Cho chỉ số bắt đầu nhích lên trên chữ "rise" (7,04) để lấp 6,5 s chùng.
   - Cho chấm "Phoenix-area average" (15,0) **kéo ra thành đường** thay vì biến mất ở 15,5.
3. **Làm lại phép trừ b4 (29–41)**:
   - Thẻ $200k bắt đầu ở 2000 và lớn theo đường trên "grown with the index" (35,7).
   - Cả đường trượt xuống đúng $200k trên "less" (37,32), kèm slide_down.
   - Bỏ đoạn tua ngược 39,5–40,5, hoặc thay bằng một chuyển cảnh có báo hiệu.
   - Lấp khoảng tĩnh 27,5–33,5.
4. **Dọn cảnh đẩy máy 55,5–63,5**:
   - Giữ nhãn "$500,000 cap".
   - Không để lịch đè lên "Source", không để trục đè lớp chú thích, không cắt mép (56,0–58,5).
   - Bỏ nhãn nhỏ $558,100 sớm ở 57,0; cho số **bay vào biển trên nhà** trên "this is the gain" (59,80).
   - Kiểm tra lại tỉ lệ khúc vượt cap ở góc máy thấp.
   - Ở 64,0–65,0 không để hai nhà bằng nhau; tiêu đề b11 phải hiện ở 63,6 chứ không phải 67,5.
5. **Mix âm**:
   - Hạ thud 23,71 và impact quanh 62 khoảng 8–10 dB.
   - Tạo khoảng lặng nhạc thật 0,6–0,8 s ngay sau "cap" (62,70).
   - Hạ âm dữ liệu ở 42–47 s khoảng 6–8 dB và làm thưa đi.
   - Cho nhạc nở theo mức 0,8 ở 44,5 và giữ nền nhạc tới 69,6.
   - Cắt bớt dải cao của chime 47,88 (low-pass dưới khoảng 5 kHz).
