# Đánh giá đạo diễn: V3d, ep004 (đoạn 0–70 s, bản xem trước 540p)

Nguồn đã xem: sheet-1/2 (khung cách 0,5 s), audio.png, transcript.txt, events.txt, intent.txt. Khung cách nhau 0,5 s nên mọi mốc hình có sai số ±0,25 s. Một sự kiện chỉ bị coi là LỆCH khi khoảng cách tới lời vượt 0,2 s cộng sai số khung, tức là lệch chắc chắn trên khoảng 0,45 s. Mức độ trên audio.png đọc bằng mắt, sai số khoảng ±0,1 s và ±3 dB.

---

## 1. Hình, lời, âm: chỗ lệch và chỗ khác ý đồ

### 1a. Đồng bộ (đối chiếu với lời nói trong ASR)

| Mốc lời | Sự kiện hình/âm | Thấy trên khung | Đánh giá |
|---|---|---|---|
| "Has" 2.08 | xà trần hiện | 2.0 có xà mờ | Khớp |
| "cap?" 3.20 | dấu hỏi | 3.0 đã có "?" | Có thể sớm 0–0,45 s, trong ngưỡng nghi ngờ |
| "can't see" 4.74–5.04 | sương, nhà mờ | 5.0 đang mờ, 5.5 mờ hẳn | Khớp |
| "rise" 7.04 | mũi tên lên | 7.0 đã có | Khớp |
| "Federal" 11.32 | nguồn "Source: FHFA via FRED" | 11.0 mờ, 11.5 rõ | Khớp |
| "many" 14.12 / "average" 13.60 | "many sales → one average", nhà bay vào chồng | 14.0 nhãn, 14.5 nhà bay | Khớp |
| "quarter" 16.36 | "2000 Q1" | 16.0 đã có Q1, 16.5 Q2, 17.0 Q3 | Q1 có thể sớm 0,1–0,6 s. Ba bước quý rõ, tốt. |
| **"2026" 19.76** | đường giá trị tới 2026 | 19.5 mới ở "2020", 20.0 "2025", 20.5 "2026 Q2" | **LỆCH: đường tới đích muộn khoảng 0,3–0,7 s so với chữ "2026".** Không khớp với con số đo pixel ±0,2 s. |
| "cap" 23.40 / thud 23.96 | đường + nhà tắt, xà rơi | 23.5 đường đã tắt, xà ngắn ở trên; 24.5 xà đủ dài | Khớp |
| "$500" 25.40 | nhãn "$500,000 cap" | 25.0 chưa có, 25.5 có | Khớp |
| "same" 27.20 | vạch từng quý + nhịp sáng chạy | 27.0 bắt đầu, 28.5 đủ | Khớp, có nghĩa |
| "gain" 30.00 | "their gain on paper = ?" | 30.0 | Khớp |
| "$200" 33.96 | khối đáy đổi teal + "what they paid" | 33.5 chưa, 34.0 có | Khớp |
| "grown" 35.72 | chồng lớn | 35.5 chưa, 36.0 cao | Khớp |
| "less" 37.28 | khối teal trượt, chồng hạ | 37.5 | Khớp |
| "paid" 39.58 | ngoặc + "their gain on paper" | 39.5 | Khớp |
| "under" 43.18 | ngoặc "well under" | 43.0 mờ, 43.5 rõ | Khớp |
| **"crosses" 47.94** | chạm và xuyên xà, loé, "Over: Q2 2022" | Loé và nhãn đúng ở 48.0, **nhưng từ 47.0 khối NHÀ đã nằm trên xà** (xem 1b) | Số liệu khớp, hình đọc sai sớm khoảng 0,9 s |
| "slips" 49.30 | "Back under" | 49.5 | Khớp |
| **"2023" 52.38 / "stayed above" 54.08–54.38** | "Stayed over since Q2 2023" | đã có ở 51.5 | **Nhãn đi trước lời: sớm khoảng 0,9 s so với "2023" và khoảng 2,6 s so với "stayed above".** Đúng mốc kế hoạch (51.53, chữ "From") nhưng sai với chữ mà nhãn lặp lại. Kết luận lộ ra trước khi người kể nói. |
| "So" 56.04 | Rosa & Frank hiện ở đầu đường | 56.5 mờ, 57.0 rõ | Khớp |
| "rose" 58.04 | mũi tên | 58.0 | Khớp |
| "this" 59.62 / fly 59.76 / land 60.73 | "≈ $558,100" bay lên biển trên mái | 59.5 số đã nằm ở đỉnh chồng, 60.0 đang bay, 60.5 đã đậu | Khớp, số có thể hiện sớm khoảng 0,1–0,3 s |
| "past" 62.06 | ngoặc "past the cap" | 62.0 | Khớp |
| "cap" 62.44 | nhà nảy qua xà, chạm lại; tiếng land 62.58 | 62.0–62.5 nhà và số chỉ nhích lên vài px | Cú nảy gần như không thấy ở mẫu 0,5 s; không kết luận được |
| "3" 65.36 | "×1" và "×3.8" | 65.5 | Khớp |

Âm thanh, đối chiếu events.txt với audio.png:
- Riser 2.06 đến "cap?", tick SOLD 8.98–13.80, chime 47.88 đều đúng mốc. Chime thấy rõ trên phổ ở khoảng 48 s, có các hài cao 4–7 kHz.
- Nhạc tắt sau "cap": đường nhạc rơi xuống dưới −80 dB ngay sau khoảng 62.4. Nhạc quay lại khoảng 63.6–63.8, trùng với "Phoenix" 63.62, sai số đọc ±0,2 s. Thời gian lặng thực tế khoảng 1,2 s. Đúng ý "lặng tới Phoenix".
- Kế hoạch ghi `release: 65.373` nhưng nhạc đã về từ khoảng 63.7, tức là trước mốc đó. Nếu "release" nghĩa là nhạc vào lại thì đây là lệch. Nếu nghĩa là bắt đầu lên dần thì không lệch. Cần thống nhất định nghĩa.
- Âm dữ liệu ở b5 (41–44) theo kế hoạch là "thưa, trầm". Trên audio.png lớp data đỏ lại dày từ khoảng 42.2 tới 47, ở mức −35 đến −25 dB. **Khác ý đồ.**

### 1b. Chỗ hình khác ý đồ hoặc dễ đọc sai

1. **47.0–47.5, ở khung phóng: nhà nằm trên đầu chồng nên thân nhà đã vượt xà** trong khi đầu đường lãi vẫn dưới xà. Mắt người xem đọc "đã vượt trần" trước "crosses" khoảng 0,9 s. Cùng vấn đề kéo dài suốt 56–64: điểm đánh dấu (nhà) cao hơn dữ liệu (đỉnh chồng) đúng bằng chiều cao một ngôi nhà. Đây là lỗi nghĩa nặng nhất của bản này.
2. **30.67–33.27, push "đẩy chậm vào nhà": trên khung không thấy.** Nhà ở 30.5, 31.0, 31.5, 32.0, 33.0 giữ nguyên cỡ và vị trí trong khoảng ±5 px ở lưới. Máy có lệnh di chuyển và có tiếng `whoosh_air` nhưng không có hình đi kèm.
3. **55.0–55.5:** hai nhãn "Over: Q2 2022" và "Back under" tắt ngay khi push bắt đầu. Ý đồ là giữ ba nhãn tới khi số bay (59.76).
4. **55.5–57.0:** nhãn "$500,000 cap" biến mất khoảng 2 s, rồi hiện lại dưới xà ở 57.5.
5. **9.0–14.0:** biển SOLD ở 540p chỉ là chấm đỏ trắng vài pixel, không đọc ra chữ "SOLD". Ý "mỗi nhà là một giao dịch" hiện chỉ nhờ tiếng tick truyền tải.
6. **64.5:** khung gần như trống, chỉ còn một phần chồng 2026 ở mép phải, giữa câu "Phoenix area prices". Ý đồ "khối teal về lại đáy chồng" ở 65.0 không thấy rõ ở 540p.

---

## 2. Chuyển cảnh và chuyển chế độ

| Mốc | Lệnh | Lý do | Liền mạch? |
|---|---|---|---|
| 4.96 | sương (không phải lệnh máy) | "can't see their house" | Liền mạch. Rosa & Frank biến mất cùng nhà; chấp nhận được. |
| 7.53–8.63 | pull, nhà → khu phố | "rise like the index", nhiều giao dịch | Liền mạch. Lý do tốt, có ý nghĩa. |
| 14.82–15.87 | mode, khu phố → đồ thị | "many sales → one average" | **Tốt nhất phim.** Nhà bay vào một chồng (14.5), máy về chính diện (15.0), chồng đứng ở mốc 2000 (15.5). Đúng tinh thần "một thế giới, máy đi". |
| 23.4 | không có lệnh máy: đường giá trị và nhà **tắt hẳn trong 0,5 s** | tránh đọc "giá vượt trần" | Hơi GÃY: đường vừa vẽ xong 3 s đã bị xoá phẳng, người xem mất vật đang theo dõi. Lý do hợp lý, nhưng nên mờ dần hoặc để lại bóng. |
| 28.76–29.76 | mode, đồ thị → thế giới | "And here's THEIR gain" | Liền mạch. Khung 29.0 cho thấy máy đi qua xà tới nhà, đúng kiểu cùng một thế giới. |
| 30.67–33.27 | push | "a home that rose like the average" | **Không thấy được** (mục 1b.2). Hoặc bỏ cả lệnh lẫn âm, hoặc đẩy thật (≥ 15–20 % cỡ khung). |
| 34.47–35.37 | pull | chồng sắp cao gấp 4 | Liền mạch, đúng lý do. Ở 36.5–37.0 mái nhà vẫn sát mép trên (khoảng 1 % khung): kéo lùi chưa đủ. |
| 41.14–42.14 | mode, thế giới → đồ thị, nhà tua về 2000 | "For most of these years" | Liền mạch về mặt máy. Ý "tua" đọc được vì chồng cao (41.0) co về nhỏ ở 2000 (42.0). |
| 46.06–47.26 | push, toàn cảnh → phóng | đoạn 2021–26 quá nhỏ | Lý do đúng. Mất trục năm: trong cZoom và cTip không còn nhãn năm, chỉ còn tiêu đề "2021 → 2026". Chấp nhận được. |
| 55.13–57.33 | push, phóng → đầu đường | "THEIR home" | Liền mạch. Phần đầu của đường bị đẩy ra mép trái và xuống sát dòng chữ dưới (56.0). |
| 64.12–65.12 | pull, đầu đường → toàn cảnh, đổi đại lượng lãi → giá | cần hai đầu 2000/2026 | **GÃY.** Ở 64.5 khung trống giữa câu. Đường lãi, xà, nhãn tắt cùng lúc trong khi máy đang bay, nên người xem không thấy "lãi + đã trả = giá" diễn ra. Đây là phép đổi đại lượng khó nhất phim mà lại ít được dàn dựng nhất. |

Tất cả 9 lệnh máy đều có lý do và có tiếng. Có 2 lệnh không đạt: push 30.67 (không thấy) và pull 64.12 (khung trống). Ngoài ra lần tắt đường ở 23.4 hơi gãy.

---

## 3. Nhịp

Chỗ chùng (lời chạy mà hình gần như đứng yên):
- **9.0–14.0 (khoảng 5 s):** khu phố đứng yên, chỉ có chấm SOLD li ti trong khi lời đọc tên cơ quan. Trên điện thoại khung này coi như tĩnh. Chỗ chùng dài nhất.
- **52.0–55.0 (khoảng 3 s):** nhãn "Stayed over" đã hiện từ 51.5, đường đã lên xong. Lời "2023, it has stayed above" chạy trên khung tĩnh. Phần lời cuối nhắc lại điều hình đã nói, nên vừa chùng vừa thừa.
- **31.0–33.5 (khoảng 2,5 s):** chạm ngưỡng chùng, vì cú push không thấy được.
- **65.5–69.0 (khoảng 3,5 s hình tĩnh, lời chạy 2,6 s trong đó):** chấp nhận được vì là khung kết luận, nhưng có thể cho ngoặc ×3.8 "đo" dần theo "times their 2000 level".
- 20.5–23.0 (2,5 s, lời chỉ có "the latest data" rồi nghỉ): ổn.

Chỗ dồn hoặc rối:
- **47–55:** cùng lúc có tiêu đề, phụ đề "A measurement, not a next step", ba nhãn (Over, Back under, Stayed over), nhãn cap, hai dòng chữ dưới, nguồn và ILLUSTRATIVE, tức khoảng **10 mảng chữ**. Thêm chớp loé, nhạc ở mức căng 0,85 và âm dữ liệu dày. Đây là đoạn rối nhất.
- **8.98–13.80:** 12 tick đều 0,44 s chạy dưới cả câu tên cơ quan. Nhịp máy móc, át cảm giác đọc nguồn.

---

## 4. Các lớp bắt buộc

| Lớp | Có mặt | Đè hình hay cắt mép | Đọc trên điện thoại |
|---|---|---|---|
| ILLUSTRATIVE (góc trên phải) | 0–69 s, liên tục | **Ở 20.0–23.0 nhà và nhãn "2026 Q2" nằm ngay dưới và chạm sát badge.** Ở 2.0–4.5 đầu phải xà trần gần chạm badge. | Chữ hoa, có nền vàng: đọc được |
| "US only · history, not a forecast" | từ 14.5 tới hết | Ở 56.0 đầu đường lãi đâm xuống sát dòng chữ dưới | Cao khoảng 3,5 % khung (khoảng 19 px ở 540p): đọc được nhưng sát ngưỡng |
| Nguồn "Source: FHFA via FRED" | từ 11.0 (lúc lời nói tên cơ quan) | Không đè | Như trên, nhỏ |
| Đối trọng "A measurement, not a next step", sau đó "not a tax bill or a next step" | 42.5–59.5 ở trên, 60.0+ ở dòng dưới | Ở 47–59 nằm chồng ngay dưới tiêu đề "their gain on paper, 2021 → 2026" thành hai tầng chữ | Đọc được. Có hai biến thể câu đối trọng trong cùng một phút, nên chọn một. |
| "A home that rose like the Phoenix average" | 31.5–59.5 | Không | Đọc được |

Chữ chồng hoặc cắt mép:
- "Back under" nằm đè lên chồng tiền và đường (49.5–55.0).
- "Stayed over since Q2 2023" đè lên mái nhà và đường (52–59).
- "≈ $558,100" ở 59.5 đè lên thân nhà và chồng trước khi bay.
- Mái nhà sát mép trên ở 36.5–37.0.
- Đầu trái của đường lãi bị cắt mép trái ở 55.5–64.0. Có chủ ý, nhưng đầu đường thòng xuống gần chữ dưới.

---

## 5. Âm

- **Lời luôn rõ.** Đỉnh giọng khoảng −8 đến −12 dBFS. Nhạc khoảng −45 đến −40 ở 5–40 s, lên khoảng −30 đến −25 ở 44–62 s. Khoảng cách với giọng 15–30 dB. Phổ cho thấy dải formant của giọng luôn nổi rõ.
- **Nhạc theo độ căng:** có biên độ thật, khoảng 15 dB từ đoạn chùng (b1–b3) lên cao trào (b6–b10), đúng chiều với bản đồ căng 0,3 → 1,0. Sau nhịp lặng nhạc về thấp (khoảng −50 ở 64–68). Tốt.
- **Khoảng lặng sau "past the cap":** có thật, khoảng 1,2 s (62.44 tới khoảng 63.7), chỉ còn tiếng chạm mềm 62.58 và room tone khoảng −60. Đúng ý, đây là khoảnh khắc mạnh nhất về âm. Tiếng chạm hơi to nếu muốn một khoảng lặng "sạch", có thể hạ 6 dB.
- **Âm dữ liệu** (16.2–54.4): nghe thấy, khoảng −40 đến −30 ở b2, không lấn lời. Ở b5–b8 dày và to hơn (−35 đến −25), cộng với nhạc khoảng −28, nên dồn sát dưới lời trong lúc lời nói những câu quan trọng nhất ("crosses", "slips back under"). Nên giảm mật độ ở b5 cho đúng "thưa, trầm".
- **Hiệu ứng thừa hoặc khó chịu:**
  - 36 sự kiện SFX trong 70 s, cộng 71 nốt dữ liệu. Có 9 tiếng whoosh và 4 tiếng land cho các lệnh máy, nên mỗi lệnh máy thành một tiếng gió: nghe như hiệu ứng giao diện, không như Vox.
  - Thud ở 23.96 lên khoảng −17 dBFS trên dòng mix, gần ngang giọng. Có chủ ý, nhưng gắt.
  - Chuỗi 12 tick (8.98–13.80) đều tăm tắp chạy dưới tên cơ quan.
  - `whoosh_air` 30.67 cho một cú push không thấy được.
  - `rise` 35.89 ở khoảng −30 trùng "grown with the index".

---

## 6. 3D: làm ý rõ hơn hay chỉ để trang trí

Làm ý rõ hơn:
- Khu phố nhiều nhà bay vào một chồng (14.5) là ẩn dụ "trung bình của nhiều giao dịch" có nghĩa thật.
- Khối teal "what they paid" tách khỏi chồng (34–40) là phép trừ nhìn thấy được, mạnh nhất phim.
- Xà trần "same in every quarter" có các vạch từng quý (27–28.5).
- Ngôi nhà cưỡi đỉnh đường lãi.

Trang trí hoặc phản tác dụng:
- Cú push 30.67 không thấy.
- Mũi tên xanh lơ lửng trên khu phố (7–14) không gắn với trục nào.
- Rosa & Frank xuất hiện trong chế độ đồ thị (56–64) chỉ để trang trí, trong khi chuẩn thiết kế là nhân vật thuộc chế độ thế giới.

Phối cảnh và tỉ lệ dữ liệu:
- Chế độ đồ thị chính diện. Tỉ lệ xà/đường nhất quán giữa b3 (giá trị) và b5 (lãi), cùng thang và xà ở cùng độ cao: tốt.
- **Ngôi nhà đặt trên đỉnh chồng là một khoảng cộng thêm không phải dữ liệu.** Hệ quả 1: ở 47.0 và 56–64 phần nhìn thấy vượt xà lớn hơn phần vượt thật (vượt thật là $58,100, khoảng 11,6 % so với trần). Hệ quả 2: ở 65–69, nếu so cả nhà thì hai chồng 2000 và 2026 trông như khoảng ×2,9 thay vì ×3,8 (ước tính từ pixel 540p, sai số lớn). Ngoặc ×1/×3.8 cứu được phần nào, nhưng mắt vẫn so cả khối.
- Ở chế độ thế giới (b4) phối cảnh nghiêng nhẹ, không gây sai lệch vì không có số.

---

## 7. Chấm điểm (so với Vox / 3Blue1Brown / WSJ)

| Tiêu chí | Điểm | Lý do ngắn |
|---|---|---|
| Hình mang nghĩa | **3** | Ý tưởng mạnh: một thế giới, chồng tiền thành đồ thị, phép trừ bằng khối. Bị kéo xuống vì nhà nằm trên chồng nên đọc sai điểm cắt, SOLD không đọc được, push vô hình, khung 64.5 trống, chữ chồng chất ở 47–59. |
| Liền mạch hình–lời–âm | **3** | Khoảng 20/23 mốc khớp trong sai số khung. Lệch thấy được: "2026" muộn 0,3–0,7 s; "Stayed over" sớm 2,6 s so với "stayed above"; điểm cắt đọc sớm 0,9 s; xoá đường đột ngột ở 23.4; gãy ở 64.5. |
| Nhịp | **3** | Có cao trào và có lặng. Chùng ở 9–14 và 52–55; rối ở 47–55. |
| Âm | **3** | Giọng sạch, nhạc có biên độ, khoảng lặng sau "cap" đúng chỗ. Quá nhiều whoosh/land/tick, thud gắt, âm dữ liệu dày ở b5–b8 trái kế hoạch. |

### Năm sửa quan trọng nhất (xếp theo mức ảnh hưởng tới điểm)

1. **47.0–48.0 và 56–64: tách điểm dữ liệu khỏi ngôi nhà.** Đỉnh chồng hoặc đầu đường phải là thứ chạm xà; vẽ một vạch mảnh tại đúng mức dữ liệu. Nhà bán trong suốt hoặc lùi ra sau khi gần xà, hoặc bỏ nhà khỏi phép so ở 65–69 (×1/×3.8 chỉ đo chồng). Sửa ý nghĩa ở điểm cắt, ở "past the cap" và ở tỉ lệ ×3.8.
2. **51.5–55.0: dời nhãn "Stayed over since Q2 2023" về chữ "stayed" (54.08)** và dùng 51.4–54.4 để vẽ đoạn trên xà từ Q2 2023 chạy tới 2026 theo lời. Giữ "Over" và "Back under" tới 59.76 như ý đồ, nhưng đặt lệch khỏi đường và chồng. Bỏ một tầng chữ ở trên (tiêu đề hoặc đối trọng). Mục tiêu: không quá 6 mảng chữ cùng lúc.
3. **64.1–65.5: dàn dựng phép đổi lãi → giá trong khung, không để trống.** Giữ chồng lãi; khối teal trượt về đáy rõ ràng trước khi kéo lùi (hoặc trong lúc kéo); đường lãi và xà mờ dần sau khi khối đã về. Khung 64.5 không được trống.
4. **30.67–33.27 và 9.0–14.0: bỏ hoặc làm thật các chuyển động vô hình.** Push phải thấy được (≥ 15–20 % cỡ khung) hoặc bỏ luôn cả `whoosh_air`. Biển SOLD lớn hơn (≥ 3 % chiều cao khung) và mỗi nhà nảy hoặc sáng khi bật. Giảm chuỗi tick xuống 5–6 tiếng có cao độ tăng dần thay vì 12 tiếng đều.
5. **17.7–20.5 và âm tổng: cho đường giá trị tới 2026 đúng chữ "2026" (19.76)**, chạy nhanh hơn khoảng 0,5 s. Đồng thời giảm SFX máy: bỏ land sau mỗi whoosh, hạ thud 23.96 khoảng 6 dB, làm thưa âm dữ liệu ở 41–47 như kế hoạch b5.
