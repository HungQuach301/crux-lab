# Director review: bản C v2 (đoạn trích 70 s)

Nguồn đã xem: sheet-1/2 (khung 0,5 s), audio.png (mức 50 ms theo lớp, phổ), transcript.txt (ASR theo từ), events.txt, intent.txt.
**Độ bất định:** hình chỉ lấy mẫu 0,5 s, nên mọi thời điểm "hình xuất hiện" có sai số ±0,25 s. Một sự kiện "xuất hiện ở khung t" nghĩa là nó có mặt trong khoảng (t−0,5, t]. Mốc lời lấy theo ASR, không theo cue trong intent (hai bên lệch nhau tới 0,6 s, ví dụ "many" 13,53 trong intent so với 14,12 theo ASR).

## 1. Lệch giữa hình, lời và âm

| # | Mốc | Lời (ASR) | Hình (khung) | Âm (events / audio) | Lệch | Đánh giá |
|---|---|---|---|---|---|---|
| 1 | b0 cap | "cap?" 3,20 | vạch đứt "the cap" mờ ở 1,5, rõ ở 2,0; "?" ở 3,0 | riser 1,52 | "?" khớp (≤0,2). Vạch đến sớm, ứng với cue cap_hint 1,52 chứ không với từ | Đạt. Vạch chỉ **hiện tại chỗ** (cùng y ở 1,5 và 2,0), không "hạ xuống" như intent; có thể chuyển động nằm giữa hai khung nhưng không thấy được |
| 2 | b1 blur | "can't see" 4,74–5,04 | nhà thành viền đứt + "?" ở 5,0–5,5 | whoosh 4,96 | ≈0 | Đạt |
| 3 | b1 rise | "rise" 7,04 | mũi tên xanh mờ ở 7,0, rõ ở 7,5 | (không có âm) | ≈0 | Đạt. Riêng "rise" không có âm nào đỡ |
| 4 | b1 nguồn | "Federal…" 11,32 | "Source: FHFA via FRED" ở 11,0 | — | −0,3 | Chấp nhận được |
| 5 | b1 many/avg | "many" 14,12, "sales" 14,40 | nhà nhỏ gom lại ở 14,0–14,5; còn một nhà ở 15,0 | 12 tick từ 8,98 đến 13,23; gather 14,45 | tick dừng 0,9 s **trước** "many" | Tick đi theo nhà bật lên chứ không theo từ: chấp nhận được. Nhưng intent ghi "gom về một ĐƯỜNG", hình lại gom về **một nhà**, đường chỉ được vẽ sau đó |
| 6 | b2 2000 | "2000" 17,70 | nhãn "2000" đứng từ 16,0; 17,5 đã sang "2001" | nốt dữ liệu chạy từ 15,8 | nhãn sớm 1,7 s | Từ 15,8 đến 17,5 nhà đứng yên ở năm 2000, rồi chạy 2001→2026 chỉ trong khoảng 2 s (17,5→19,5). Nhịp vẽ không đều. Intent muốn trục năm lật như lịch; hình làm bằng bộ đếm năm cạnh nhà |
| 7 | b2 2026 | "2026" 19,76 | "2026 Q2" ở 19,5 | — | ≈−0,26 | Đạt. Ở 20,5 nhãn "2026 Q2" bị **cắt mép phải** |
| 8 | b3 cap | "cap" 23,40 | vạch trần liền nét có ở 23,5 (chưa có ở 23,0) | thud + drone_on 23,71 | thud trễ +0,31 so với từ, +0,2 đến 0,7 so với hình | Lệch nhẹ: thud nên đặt ở 23,40 |
| 9 | b3 nhãn | "$500,000" 25,40–25,86 | "$500,000 cap" ở 25,5 | — | ≈0 | Đạt |
| 10 | b3 flat | "same in every quarter" 26,96–28,34 | 3 vạch tick nhỏ chạy trên trần, 27,0–28,0 | không có âm riêng | — | Ý thì đúng, nhưng tick quá nhỏ và mờ, ở 25 % gần như không thấy |
| 11 | b4 gain | "gain" 30,00 | "their gain on paper = ?" ở 30,0 | — | ≈0 | Đạt |
| 12 | b4 $200k | "$200" 33,96 | cột xanh lá "$200,000" ở 34,0 | — | ≈0 | Đạt |
| 13 | b4 grow | "grown" 35,70 | đường sáng xanh, nhãn "…grown with the index" mờ ở 35,5, rõ ở 36,0 | — | ≈0 | Đạt |
| 14 | b4 less/paid | "less" 37,30; "paid" 39,58 | dải "−$200,000 paid" đã có ở 37,0; đường trượt xuống ở 37,5–38,0, xong trước 38,5; nhãn "paid" mờ đi ở 39,0; "gain on paper" ở 39,5 | slide_down 37,06 | dải sớm ≥0,3 so với "less"; phép trừ **xong trước "paid" khoảng 1–1,5 s** | Lệch rõ. Phép trừ phải "chốt" đúng chữ "paid" |
| 15 | chuyển ý | (lặng 39,6–41,1) | nhà nhảy ngược từ 2026 về 2000 trong 39,5–40,5 | không có âm | — | Đi ngược thời gian mà không có lời, không có âm. Người xem dễ đọc thành lỗi |
| 16 | b5 under | "under" 43,18 | vùng tô + ngoặc "well under" mờ ở 43,0, rõ 43,5–44,5 | dữ liệu thưa (lớp đỏ có ở 41–46) | ≈0 | Đúng giờ. Nhưng vùng tô chỉ phủ 2000–2009, trong khi lời nói "most of these years". Nhãn "well under" xanh đậm trên nền đen nên **không đọc được** |
| 17 | b6 Q2 2022 | "second quarter of 2022" 45,54–46,26 | ở 45,5–46,0 nhà mới đến khoảng 2015–2018; nhãn "Over: Q2 2022" ở 48,0 | riser 46,28 | nhãn **trễ khoảng 1,7 s** (intent cue q 45,45) | Lệch: tai nghe "2022" trong khi mắt thấy khoảng 2016 |
| 18 | b6 cross | "crosses" 47,96 | nhà chạm trần ở 47,5; tia sáng + nhãn ở 48,0 | chime 47,88 | ≈0 | **Tốt nhất đoạn**: hình, lời, âm trùng nhau |
| 19 | b7 slip | "slips" 49,30 | nhà xuống chỗ trũng ở 49,5–50,0 | dữ liệu đi xuống (không xác minh được cao độ) | ≈0 | Đúng giờ nhưng chỗ trũng dưới trần rất nông, ở 25 % gần như không thấy. Không thấy "phần vượt tắt màu" |
| 20 | b8 stay | "2023" 52,38; "above" 54,38 | "Stayed over since Q2 2023" ở 51,5; đoạn cam kéo dài 51,5–54,5 | — | nhãn sớm khoảng 0,9 so với "2023" | Đạt, vì "From the second quarter" đã bắt đầu ở 51,34 |
| 21 | b9 fly/land | "gain" 60,24 | "$558,100" nhỏ cạnh nhà ở 59,5, đã to ở giữa trên cùng từ 60,0 | swish 59,75; tick 60,73 | tick chạm trễ ≥0,7 so với hình | **Khác ý đồ**: intent cho số bay **vào biển trên nhà**; hình cho số bay **ra khỏi nhà** lên làm tít. Tick "chạm" rơi vào lúc không có gì chạm |
| 22 | b10 past the cap | "cap" 62,44 | ngoặc cam + "past the cap" ở 62,0 | impact 62,76 | impact trễ +0,32 | **Khác ý đồ**: không có "chồng tiền lãi đẩy xuyên trần". Đoạn vượt đã cam từ 51,5, nên ở đỉnh căng (tension 1,0) hình chỉ thêm một nhãn |
| 23 | b11 ×3,8 | "3.8" 65,36–65,72 | cột lớn dần 63,5–65,0; "×3.8" ở 65,5 | rise 65,37 | ≈0 | Đạt. Tỉ lệ cột (phần xanh) khoảng 3,7–3,8, đúng |

**Âm có phản ứng với biến động hình không?** Có ở 4,96, 9–13, 47,88, 65,37. Thiếu ở: nhà đi ngược (39,5–40,5), lúc số bay lên tít (60,0, tick rơi sai chỗ), vạch trần xuất hiện ở b0 (riser ổn), mũi tên "rise" 7,0.

## 2. Chuyển cảnh

| Mốc | Chuyển | Có lý do? |
|---|---|---|
| 4,5–5,5 | nhà thật → viền đứt "?" | **Có lý do** ("can't see"). Vạch trần mở màn biến mất ở 5,5 mà không có lời giải thích. Chấp nhận được |
| 13,5–15,0 | đám nhà nhỏ co về góc trái dưới, trục năm hiện ra | **Gãy nhẹ**. Ở 14,0 trục đang phóng to, các nhãn năm bên phải bị cắt ("2(") và đám nhà còn lơ lửng trên trục. Ý "nhiều giao dịch → một chỉ số" còn đọc được, nhưng gom về một nhà chứ không về một đường |
| 23,0–24,0 | đường giá mờ đi, trần hiện | Có lý do: lùi lớp cũ để nhấn trần |
| 37,0–38,5 | trừ $200k, đổi màu xanh → trắng, đổi nhãn | Có lý do nhưng **dồn**: 4 thay đổi trong 1,5 s |
| 39,5–41,0 | nhà tua ngược về 2000 | **Gãy**: không có lời, không có âm |
| 56,0–59,0 | đẩy máy vào vùng 2022–2026; trục năm mất, đường bị cắt mép trái | Có lý do (hội tụ về kết luận). Mất trục năm thì mất mốc thời gian, nhưng ở đây chấp nhận được |
| 63,0–64,0 | biểu đồ lãi hoà tan → hai cột giá | Có lý do (từ lãi sang bối cảnh giá). Khung 63,5 bị **chồng hai lớp rối**: nhãn trục "2000/2010" cũ đè "2000/2026 Q2" mới, "gain on paper" bị cột che. Đổi khái niệm từ *lãi* sang *giá* mà không có cầu nối bằng hình |

## 3. Nhịp

**Chùng** (hình đứng yên khi lời chạy, hoặc gần như đứng yên):
- **25,5–30,0**: chỉ có 3 tick nhỏ trên trần trong khi lời chạy 26,96–28,34. Khoảng 4,5 s gần như tĩnh.
- **30,0–33,9**: hoàn toàn tĩnh trong khi lời chạy 31,40–32,74 ("For a home that rose like the average"). Khoảng 3,9 s. Cộng với đoạn trên thành gần **8,5 s chùng liên tục**, đây là lỗ nhịp lớn nhất.
- 20,0–22,9: tĩnh khoảng 2,9 s, lời chỉ có "the latest data". Chấp nhận được.
- 65,5–69,0: tĩnh 3,5 s, lời chạy 65,7–68,0. Ở ngưỡng, nhưng đây là khung kết nên chấp nhận được.
- 54,5–56,0: lặng cả hình lẫn lời 1,5 s. Có thể là nhịp thở, nhưng nhạc ở đó không làm gì.

**Dồn/rối:**
- 37,0–40,5: trừ, đổi màu, đổi nhãn, nhà tua ngược. Quá nhiều trong 3,5 s.
- 17,5–19,5: 25 năm dữ liệu vẽ trong 2 s, sau 1,7 s đứng chờ.
- 9,0–14,0: đám nhà nhỏ đủ để thấy "nhiều", không rối.

## 4. Lớp bắt buộc

| Lớp | Có mặt | Đè hình | Đọc được ở 25 % (ước lượng từ sheet, mỗi khung khoảng 15 % kích thước) |
|---|---|---|---|
| ILLUSTRATIVE (huy hiệu vàng, góc phải trên) | 0,0–69,0, liên tục | Ở 1,5–5,0 nhãn "the cap" nằm **sát dưới, gần chạm** huy hiệu, vạch đứt chạy ngay dưới: **chồng chữ** | Có (huy hiệu có viền, tương phản tốt) |
| Nguồn "Source: FHFA via FRED" | 11,0–69,0 | Không | Chỉ vừa đủ. Chữ nhỏ, xám nhạt, có thể không đọc được trên điện thoại |
| "US only · history, not a forecast" | 14,5–69,0 | Không | Chỉ vừa đủ, giống dòng nguồn. Trước 14,5 chưa có, nhưng khi đó cũng chưa có dữ liệu nên không sao |
| Đối trọng: "A home that rose like the Phoenix average" (30,0–61,5), "A measurement, not a tax bill or a next step" (62,0–69) | Có | Không | Xám mờ, cỡ nhỏ, ở 25 % **khó đọc**. Lúc đổi câu (61,5–62,0) chữ mờ hẳn trong khoảnh khắc ngay trước đỉnh căng. Nếu đây là lớp đối trọng bắt buộc thì phải sáng và to hơn |

**Chữ chồng / cắt mép:**
- 14,0: nhãn trục năm bị cắt mép phải.
- 20,5: "2026 Q2" bị cắt mép phải.
- 35,5–36,0: đường đi xuyên qua nhãn "$200,000".
- 37,0–38,5: đường đi xuyên qua nhãn "−$200,000 paid", chồng chữ rõ.
- 43,0–44,5: "well under" gần như vô hình.
- 59,0: "Stayed over since Q2 2023" sát mép phải (khoảng 98 % bề ngang), ngoài vùng an toàn.
- 60,0–63,0: "past the cap" ở khoảng 91 % bề ngang, sát vùng an toàn.
- 56,5–63,0: Rosa & Frank tái xuất cạnh nhà nhưng quá nhỏ, ở 25 % không nhận ra. Callback bị phí.

## 5. Âm

- **Lời có luôn rõ không:** có. Lời đỉnh khoảng −7 đến −10 dBFS. Nhạc nằm khoảng −35 đến −45 trong phần lớn đoạn, và lên khoảng −25 đến −20 ở 56–62. Riêng 59–62 khoảng cách lời–nhạc chỉ còn khoảng 10 dB: vẫn rõ, nhưng đã sát.
- **Nhạc có theo căng–chùng không:** theo hướng thì đúng (nhích lên ở 44–50 và 56–62, rớt ở 63, tắt dần đến 69). Nhưng biên độ hẹp, khoảng 10–15 dB. Đỉnh 0,8 (44,5) và 1,0 (61,3) không tạo được khác biệt rõ so với 0,4–0,5, nên đường cong căng–chùng nghe phẳng.
- **Drone của trần:** lớp sfx giữ khoảng −35 dBFS liên tục từ 24 đến 40 (khoảng 16 s), ngang mức nhạc, làm đục nền đúng vào đoạn hình đang chùng. Nên giảm hoặc cho tắt dần sau khoảng 4 s.
- **Khoảng lặng sau "past the cap":** lời dừng ở 62,7, lời kế tiếp vào ở 63,62, tức khoảng lặng chừng 0,9 s. Nhạc rớt xuống khoảng −45 và room tone giữ sàn −60, đúng ý đồ. Nhưng impact (62,76) lên khoảng **−8 dBFS, ngang đỉnh lời**: quá to, trễ 0,32 s so với "cap", và lấp chính khoảng lặng. Chuyển tiếp hình hoà tan bắt đầu ngay trong khoảng lặng (63,0–63,5), nên có chuyển tiếp, nhưng khoảng lặng không được "thở" trọn.
- **Âm dữ liệu:** nghe thấy ở 17,5–21 và 41–55, đỉnh khoảng −18 đến −35, không lấn lời. Riêng 18–19 đỉnh chạm khoảng −18, ngay trong khe giữa các từ: đạt. Trong 22–40 gần như không thấy lớp dữ liệu, dù events ghi 90 nốt trải 15,8–54,4. Mình không xác minh được cao độ "theo giá trị" và "đi xuống ở slip".
- **Hiệu ứng thừa / khó chịu:**
  - Chime 47,88 có chuỗi hài lên tới 8 kHz, rất sáng trên phổ. Đúng chỗ, nhưng có thể chói; nên cắt bớt dải cao.
  - Impact 62,76 quá to (đã nêu ở trên).
  - Tick 60,73 rơi vào lúc không có gì chạm.
  - Đoạn nhà tua ngược (39,5–40,5) và mũi tên "rise" (7,0) lại không có âm nào.

## 6. Chấm điểm (so với Vox, 3Blue1Brown, WSJ)

| Tiêu chí | Điểm | Lý do ngắn |
|---|---|---|
| Hình mang nghĩa | **3/5** | Phép trừ trượt đường, điểm cắt và cột ×3,8 tỉ lệ đúng đều tốt kiểu 3B1B. Nhưng đỉnh căng (b10) và cú bay số (b9) yếu hoặc làm ngược ý đồ, và "well under"/"slip" khó thấy |
| Liền mạch hình–lời–âm | **3/5** | Đa số mốc khớp trong ±0,3 s. Lệch rõ ở: Q2 2022 (+1,7 s), phép trừ xong sớm hơn "paid" khoảng 1 s, thud +0,3, impact +0,3, tick chạm trễ khoảng 0,7 |
| Nhịp | **2,5/5** | Lỗ chùng khoảng 8,5 s ở 25,5–33,9; dồn ở 37–40,5; vẽ dữ liệu không đều ở 15,8–19,5 |
| Âm | **3/5** | Lời rõ và lớp âm có tổ chức, nhưng nhạc phẳng, drone kéo dài, impact quá to và lấp khoảng lặng |

### Năm sửa quan trọng nhất
1. **61,3–63,6 (đỉnh căng):**
   - Làm đúng hình trong intent: chồng lãi dưới nhà đẩy xuyên trần, phần vượt **đổi sang cam ngay lúc này**. Nếu muốn giữ cam từ 51,5 thì nâng độ sáng ở đây.
   - Dời impact về 62,44 và hạ xuống khoảng −20 dBFS.
   - Giữ khoảng lặng trọn khoảng 0,6 s rồi mới hoà tan ở khoảng 63,2.
2. **25,5–33,9 (lỗ chùng):**
   - Ở "same in every quarter" (26,96–28,34): cho tick quý chạy hết chiều dài trần, mỗi tick một nốt.
   - Ở "for a home that rose like the average" (31,4–32,7): cho nhà + Rosa & Frank lướt dọc đường hoặc làm đường "thở", để không còn quá 3 s đứng yên.
   - Tắt dần drone sau khoảng 27 s.
3. **37,3–41,1 (phép trừ):**
   - Bắt đầu trượt đúng "less" 37,30 và chốt đúng "paid" 39,58, với slide_down kéo dài theo.
   - Bỏ hoặc làm rõ cú tua ngược nhà 39,5–40,5 (vệt quét + âm rewind), hoặc cho nhà bắt đầu đi từ 2000 ngay sau khi trừ xong.
   - Không để nhãn "−$200,000 paid" bị đường cắt qua.
4. **45,5–48,0 (Q2 2022):**
   - Đưa vạch hoặc nhãn "Q2 2022" lên trục ngay ở 45,54–46,26 làm đích, rồi để nhà chạy tới đó ở "crosses" 47,96.
   - Hiện tại tai nghe "2022" khi mắt còn thấy khoảng 2016, nhãn trễ 1,7 s.
5. **59,5–61,0 và chữ/mép toàn đoạn:**
   - Cho "$558,100" bay **vào** biển trên nhà Rosa & Frank đúng intent, với tick chạm ở 60,73 khi thực sự chạm.
   - Sửa các chỗ cắt mép: 14,0, 20,5, 59,0 ("Stayed over…"), "past the cap" sát mép.
   - Sửa chồng chữ "the cap" và ILLUSTRATIVE (1,5–5,0).
   - Làm sáng "well under" (43–44,5) và các dòng đối trọng ở chân khung, để đọc được ở 25 %.
