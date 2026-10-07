# Đánh giá đạo diễn — V3i, ep004, đoạn 0–70 s (bản xem trước 540p)

Nguồn đã xem: sheet-1/2 (khung hình cách nhau 0,5 s), audio.png (mức âm từng lớp theo 50 ms + phổ), transcript.txt, events.txt, intent.txt.
Quy ước: một sự kiện thấy lần đầu ở khung t thì đã xảy ra trong khoảng (t−0,5; t]. Chỉ gọi là "sớm" hoặc "trễ" khi khung hình chứng minh được điều đó vượt quá dung sai ±0,2 s.

---

## 1. Chỗ lệch hình / lời / âm, và chỗ hình khác ý đồ

### 1a. Đồng bộ theo mốc (dung sai ±0,2 s, sai số khung 0,5 s)

| Mốc (cue) | Thấy lần đầu | Khoảng thực | Nhận định |
|---|---|---|---|
| xà trần `has` 2,06 | 2,0 | ≤2,0 | Khớp. Nằm ở biên −0,06, trong dung sai. |
| dấu "?" `q` 3,18 | 3,0 (còn mờ) | (2,5; 3,0] | Sớm ít nhất 0,18 s. Trong dung sai nhưng sát biên. |
| tối nhà `blur` 4,96 | 5,0 | (4,5; 5,0] | Khớp. |
| mũi tên `rise` 7,176 | 7,0 | (6,5; 7,0] | Sớm ít nhất 0,18 s, sát biên. |
| biển SOLD `pop0` 8,98 | 9,0 | (8,5; 9,0] | Khớp. |
| "Source" `src` 11,21 | 11,0 (mờ), 11,5 (rõ) | — | Khớp. |
| nhà bay vào chồng `avg` 14,45 | 14,5 | — | Khớp. |
| nhãn "2000 Q1" `quarter` 16,24 | **16,0** | ≤16,0 | **Sớm ít nhất 0,24 s, vượt dung sai.** Ở khung 15,5 chưa có nhãn, nên nhãn hiện trong (15,5; 16,0]. Nếu "Q1" được tính là trạng thái lúc đáp chế độ (land 15,87) thì không lỗi, nhưng khi đó bước nhảy đầu tiên lại không rơi vào chữ "quarter". |
| chạy tới 2026 `y2026` 19,686 | 20,0 ("2026 Q2") | — | Khớp. |
| xà `cap` 23,36 | 23,5 | — | Khớp. Tiếng thud ở 23,66 (+0,3 s) đúng như kế hoạch. Không thấy chuyển động "rơi rồi khoá": ở 23,5 xà đã nằm đúng vị trí. |
| vệt sáng `flat` 24,58 | 24,5 | — | Khớp. |
| "$500,000 cap" `five` 25,37 | 25,5 | — | Khớp. |
| cột mốc `same` 27,18 | 27,0 | (26,5; 27,0] | Sớm ít nhất 0,18 s, sát biên. |
| "their gain on paper = ?" `gain` 30,01 | 30,0 | — | Khớp. |
| khối đổi teal `two` 33,94 | 34,0 | — | Khớp. |
| chồng lớn lên `grow` 35,89 | 36,0 | — | Khớp. |
| khối trượt `less` 37,30 | 37,5 | — | Khớp. |
| ngoặc lãi `paid` 39,58 | 39,5 | — | Khớp. |
| ngoặc "well under" `under` 43,23 | 43,5 | — | Khớp. |
| cắt xà + loé `cross` 47,88 | 48,0 | — | Khớp, đúng nhịp chime. Đây là khoảnh khắc tốt nhất của đoạn. |
| "Back under" `slips` 49,28 | 49,5 | — | Khớp. |
| "Stayed over…" `lbl` 51,53 | 51,5 | — | Khớp. |
| mũi tên `rose` 58,02 | 58,0 | — | Khớp. |
| số bay `fly` 59,76 / đáp `land` 60,73 | 60,0 / 60,5–61,0 | — | Khớp. |
| ngoặc "past the cap" `past` 62,01 / `cap` 62,44 | 62,0 (ngoặc đã cao khoảng 80%), chữ hiện ở 62,5 | — | Không chứng minh được sớm. |
| đổi lãi → giá, từ chữ "Phoenix" 63,62 | 63,5 bắt đầu mờ, 64,0 đổi | — | Khớp. |
| ×1 / ×3,8 `x` 65,37 | 65,5 | — | Khớp. |
| `lvl` 67,69 | — | — | **Không thấy thay đổi nào** giữa khung 67,5 và 68,0. Mốc này không có hình tương ứng. |

Tổng kết đồng bộ: gần như mọi mốc đều khớp. Có bốn mốc lệch sớm khoảng −0,2 s một cách có hệ thống (q, rise, same, Q1). Riêng nhãn Q1 được khung hình chứng minh là vượt dung sai.

### 1b. Chỗ hình khác ý đồ

- **b1, 4,96 ("nhà mờ trong sương"):** ý đồ là sương mù, nhưng hình chỉ làm tối nhà và tắt nhãn. Khán giả đọc thành "tắt đèn" chứ không phải "không nhìn thấy". Không có sương hay độ nhoè nào.
- **b1, 7,0–14,0 ("let its value rise"):** chỉ có một mũi tên xanh trôi cạnh mái nhà. Chồng tiền đứng yên, không có gì thực sự "lên giá".
- **b1, tick theo SOLD:** ý đồ là "tick mỗi nhà SOLD". Trên hình có khoảng 8 hoặc hơn biển SOLD bật dần từ 9,0 đến 13,5, nhưng events.txt chỉ có 3 tick (8,98 · 10,73 · 12,49). Lỗi lệch hình–âm do đếm sai.
- **b3, 24,0–28,5:** ý đồ chỉ tắt "đường giá trị + nhà", nhưng chồng tiền 2026 cũng biến mất. Đồ thị còn trống trơn, chỉ có xà và trục.
- **b4, 34,0:** nhãn "what they paid" hiện ngay khi nói "the $200,000", tức trước chữ "paid" (39,58) 5,6 s. Ý đồ không nêu nhãn này. Nó nói trước lời.
- **b8 → b9 (55,0–55,5):** ý đồ b8 là "ba nhãn giữ tới khi số bay". Thực tế nhãn "Over: Q2 2022" và "Back under" **mờ đi tại chỗ** ở 55,0 rồi mất ở 55,5. Chúng không "rời khung" theo cú đẩy máy như b9 mô tả. Chỉ còn "Stayed over…" giữ tới khoảng 59,5.
- **b9, 55,1–59,8 ("đẩy chậm vào NHÀ ở đầu đường"): lệch nặng nhất.** Ở cTip **không có nhà nào trong khung**. Chân chồng tiền chìm xuống mép dưới, và nhà (đứng trên mặt đất cạnh chồng) nằm ngoài khung. Mũi tên "rose" ở 58,0 trôi lơ lửng giữa nền đen, cách xa chồng tiền chứ không "cạnh nhà". Lý do của cú máy ("con số là của Rosa & Frank") không hiện ra trên hình.
- **b10, ngoặc "past the cap" (62,0–63,5):** ý đồ đặt ngoặc "bên phải chồng". Thực tế ngoặc cách chồng khoảng 20% chiều rộng khung, đứng lẻ ở vùng trống bên phải. Mắt phải tự nối ngoặc với đoạn chồng vượt xà.
- **b11 ("cả đường lãi NÂNG đúng $200,000"):** ở 64,0 vẫn là đường lãi trắng trong khung zoom, đến 64,5 đã là đường giá xanh toàn cảnh. Với khung 0,5 s thì không thấy được chuyển động "nâng". Không kết luận là sai, nhưng nếu có thì nó quá nhanh để đọc.
- **b11, âm "dữ liệu lên một quãng":** lớp data (đỏ) tắt hẳn sau 54,4 s, nên **không có âm dữ liệu ở 65,4**.

---

## 2. Chuyển cảnh và chuyển chế độ

| Thời điểm | Cú máy | Lý do có đúng không | Liền hay gãy |
|---|---|---|---|
| 7,5–8,6 | pull wHome→wHood | Đúng: "index" nghĩa là nhiều giao dịch. | Liền. |
| 14,8–15,9 | mode → chart | Đúng: "average of many sales". Các nhà bay vào chồng ở 14,5 là hình có nghĩa. | **Gãy nhẹ.** Nhà chính đang **đứng trên đỉnh chồng** (thế giới, 14,5) thì nhảy xuống **đứng cạnh chồng** (đồ thị, 15,5). Cùng một vật thể nhưng đổi chỗ khi đổi chế độ. Ở 15,5 còn thấy bóng người mờ ở hai mép khung. |
| 23,5–24,0 | (trong chế độ đồ thị) tắt đường, nhà, chồng | Ý đồ hợp lý (tránh đọc nhầm). | Gãy về nội dung: đồ thị bị dọn sạch, mất điểm neo. |
| 28,8–29,8 | mode → world | Đúng: "THEIR gain". | Khung 29,0 là một cú hoà hình: xà đồ thị còn treo ở góc trái trong khi nhà xuất hiện ở bên phải. Hai cảnh chồng lên nhau trông giống crossfade chứ không phải "máy đi giữa các nơi của cùng một thế giới". Gãy nhẹ. |
| 30,7–33,3 | push vào nhà | Đúng. | Liền, chậm, đẹp. |
| 34,5–35,4 | pull để thấy chồng | Đúng. | Liền. Tuy vậy ở 36,5 mái nhà gần chạm dải Source/ILLUSTRATIVE (khoảng đầu khung gần như không còn). Cú lùi chưa đủ. |
| 41,1–42,1 | mode → chart (tua về 2000) | Đúng. | Gần liền. Nhà lại nhảy từ đỉnh chồng (41,5) xuống mặt đất (42,0), cùng lỗi như ở 15 s. |
| 46,1–47,3 | push → cZoom | Lý do tốt (đoạn 2021–26 quá nhỏ). Đẩy **trước** mốc cắt là đúng. | Liền. Nhưng sau cú đẩy **mất trục năm và chân chồng**, xem mục 6. |
| 55,1–57,3 | push → cTip | Lý do nói về "nhà", nhưng khung không có nhà. | **Gãy về nghĩa.** Thêm nữa, nhãn "$500,000 cap" **nhảy chỗ** từ trái (55,0) sang sát chồng (55,5). |
| 64,1–65,1 | pull → cFull | Đúng: cần cả 2000 và 2026. | Liền. Đổi đại lượng ở 63,5–64,5 rõ ràng, tiêu đề mới đặt đúng lúc. |

Tóm lại, các chuyển động máy đều có lý do bằng lời và đúng mốc. Hai điểm gãy có hệ thống là **nhà đổi vị trí (trên chồng ↔ cạnh chồng) mỗi lần đổi chế độ** và **cú đẩy vào nhà ở 55 s mà không có nhà**.

---

## 3. Nhịp

**Chỗ chùng** (hình đứng yên trong khi lời chạy, hoặc khoảng tĩnh dài):
- **20,0–23,3 (khoảng 3,3 s):** đường đã tới 2026 và đứng yên. Lời "the latest data" (21,1–21,5), rồi 1,4 s im, rồi "Here's the". Lời chạy không quá 3 s, nhưng hình chết khoảng 3,3 s. Chùng nhẹ.
- **24,0–27,0:** cả màn hình chỉ có một đường ngang, ba giây gần như trống (chỉ có vệt sáng ở 24,5 và nhãn ở 25,5). Chùng về thị giác.
- **57,0–59,7 (khoảng 2,7 s):** khung tĩnh, chỉ có mũi tên ở 58,0. Lời "on paper, if their home rose like the Phoenix average" chạy suốt. Gần ngưỡng.
- **65,5–69,0 (3,5 s tĩnh, lời chạy khoảng 2,5 s):** chấp nhận được vì đây là khung kết luận. Tuy vậy mốc `lvl` 67,69 không có gì xảy ra.
- Không có đoạn nào hình đứng yên quá 3 s trong khi lời chạy liên tục.

**Chỗ dồn hoặc rối:**
- **47,5–55,0:** ba nhãn cam, nhãn xà, tiêu đề, đường hai màu, loé và chồng tiền dồn trong khoảng 40% khung. Nhãn đè lên đường (xem mục 4). Thông tin đúng nhưng đọc trên điện thoại thì nặng.
- **59,7–62,5:** số bay, bảng đáp, nhãn "their gain on paper" đổi chỗ, ngoặc mọc, nhãn "past the cap", tất cả trong khoảng 2,8 s. Chấp nhận được vì đây là cao trào, và có khoảng lặng ngay sau đó để thở.
- **8,9–14,5:** khoảng 8 biển SOLD cộng mũi tên cộng nhãn Source cùng chạy. Hơi ồn nhưng hợp với "many sales".

---

## 4. Lớp bắt buộc (54 px trên 1080p)

- **Cỡ chữ:** đo trên khung 66,0 phóng to, chữ "US only · history, not a forecast" cao khoảng 38–40 px quy về 1080p (từ cap tới descender). Con số này khớp với cỡ 54 px. Đọc được trên điện thoại. ILLUSTRATIVE (badge vàng) và Source rõ.
- **Đè hình:**
  - Ở cZoom và cTip (47–63 s), chân chồng tiền tan dần ngay trên hai dòng bắt buộc. Không chồng chữ, nhưng dải đáy khung thành vùng chết.
  - Ở b4 (31,5–41), dòng "A home that rose like the Phoenix average" cộng "US only…" chiếm hai dòng đáy. Không đè lên nhân vật.
  - Ở 66,0, tiêu đề "Phoenix-area prices since 2000" sát đỉnh đường 2022 (cách khoảng 2–3 px ở 540p). Gần chạm.
- **Chữ chồng chữ / chữ chồng đường (không thuộc lớp bắt buộc, nhưng là lỗi đọc):**
  - 19,5–23,0: đường xanh **cắt qua** nhãn "home value"; nhãn "2026 Q2" chạm đường.
  - 49,5–55,0: đường trắng cắt qua hộp "Back under". "$500,000 cap" sát đường dốc.
  - 56,0–59,0: hộp "Stayed over since Q2 2023" chạm hoặc đè mép trái chồng tiền. Nhãn "$500,000 cap" kẹp giữa đường vàng và xà.
- **Cắt mép:**
  - 36,5: mái nhà gần chạm mép trên, ngay dưới dải Source.
  - 60,5–63,5: bảng "≈ $558,100" nằm sát dải Source/ILLUSTRATIVE. Chưa đè nhưng không còn khoảng an toàn.
  - Các vạch năm ở trục (2005… 2020) màu xám tối trên nền gần đen, tương phản thấp trên điện thoại.

---

## 5. Âm

- **Lời:** rõ. Đỉnh voice từ −8 đến −10 dBFS. Nhạc nằm ở −35 đến −45 trong đa số đoạn, chừa khoảng 25 dB. Ở cao trào 56–62 nhạc lên khoảng −25, vẫn chừa khoảng 15 dB. Phổ không có dải nào che dải tiếng nói.
- **Nhạc theo căng–chùng:** mức nhạc đi lên đúng hướng, từ khoảng −45 (0–4 s) lên khoảng −37 (5–40 s) rồi −30 đến −25 (44–62 s). Accent ở 47,88 có thể thấy như một đỉnh nhỏ. Tuy vậy các bậc nhỏ của bản đồ tension (0,45 → 0,55 → 0,45 ở 23–41 s) không thể hiện ra mức âm, đoạn đó phẳng.
- **Khoảng lặng sau "past the cap":** nhạc bắt đầu tắt ở 62,44 và chạm đáy ở khoảng 62,7. Khoảng lặng thật (không lời, không nhạc) kéo dài **khoảng 62,7–63,6, tức khoảng 0,9 s**, chỉ còn tiếng "land" mềm (khoảng −45 dB) và room tone. Đúng ý đồ "lặng ~1 s", và đây là điểm mạnh. Lưu ý: nhạc chỉ trở lại ở **khoảng 65,3** (theo music plan release 65,373), không phải ở "Phoenix" như beat b10 ghi. Hai tài liệu ý đồ mâu thuẫn nhau. Bản dựng theo music plan nên câu "Phoenix area prices are now almost" (63,6–65,3) chạy trên nền không nhạc. Hiệu quả vẫn tốt, nhưng cần thống nhất lại.
- **Âm dữ liệu:** có ở 16,3–20,2 s (b2) và khoảng 42,4–54,4 s (b5–b8), mức −25 đến −40, không lấn lời. **Thiếu ở b11** (65,4 "lên một quãng"): lớp data tắt từ 54,4. Từ hình mức âm không kiểm chứng được cao độ "đi xuống" ở b7 hay "trầm, thưa" ở b5.
- **Hiệu ứng thừa hoặc thiếu:**
  - Khoảng 10 tiếng whoosh và 3 tiếng land trong 70 s, gần như mỗi cú máy một whoosh. So với 3Blue1Brown và Vox thì dày, và tiếng whoosh mất giá trị báo hiệu. Nên bỏ whoosh ở các cú push/pull nhỏ (30,7 · 34,5 · 55,1 · 64,1), chỉ giữ whoosh_mode.
  - Riser 2,06–3,1 là một khối mức phẳng khoảng −42 dB, ổn.
  - 3 tick cho khoảng 8 biển SOLD (đã nêu ở mục 1b).

---

## 6. 3D: làm ý rõ hơn hay chỉ trang trí; phối cảnh có làm sai tỉ lệ không

**3D làm ý rõ hơn:**
- Chồng tiền trở thành đường đồ thị. Đỉnh chồng xuyên xà ở 48,0 có loé và chime: hình mang nghĩa đúng tinh thần 3Blue1Brown.
- Khối teal "what they paid" trượt ra và chồng hạ xuống ở 37,5 là phép trừ nhìn thấy được.
- Các nhà bay vào chồng ở 14,5 diễn đạt ý "trung bình".
- Ở 65,5–69,0, chồng teal 2000 và đáy teal 2026 cho thấy "cái đã trả" ở cả hai đầu.

**Kiểm tra tỉ lệ:**
- Ở 66,0: chồng 2000 cao khoảng 97 px, chồng 2026 cao khoảng 362 px (ảnh phóng 4×). Tỉ lệ khoảng 3,7, khớp ×3,8. Đáy teal 2026 cao bằng chồng 2000. **Phối cảnh không làm sai dữ liệu** ở chế độ đồ thị toàn cảnh.

**Chỉ trang trí hoặc gây hiểu sai:**
- Mũi tên xanh ở b1 và b9 lơ lửng, không gắn với đại lượng nào.
- "Sương" ở b1 thực ra chỉ là làm tối.
- Ở b0 (0–4,5 s), **nhà đặt trên đỉnh chồng giá trị $200k, ngay dưới xà trần**. Hình ảnh này gợi đúng cách đọc nhầm "giá nhà vượt trần" mà b3 phải tắt nhà để tránh. Ý đồ tự mâu thuẫn ngay cảnh mở.

**Sai cảm nhận tỉ lệ (truncation):**
- Ở cZoom và cTip (47–63 s), chồng tiền bị cắt chân và không có trục năm hay trục giá. Phần vượt xà ($58k trên $500k, khoảng 12%) chiếm khoảng 1/3 phần chồng nhìn thấy. Mắt người xem sẽ phóng đại mức vượt. WSJ sẽ đánh dấu ngắt trục hoặc giữ lại một mẩu chân chồng.
- Thang hai chế độ không đồng nhất: thế giới đặt nhà trên chồng, đồ thị đặt nhà cạnh chồng (đã nêu ở mục 2).

---

## 7. Chấm điểm (so với Vox, 3Blue1Brown, WSJ)

| Tiêu chí | Điểm | Lý do ngắn |
|---|---|---|
| Hình mang nghĩa | **3** | Ý tưởng chồng-tiền-là-đồ-thị mạnh. Điểm cắt 48 s, phép trừ 37,5 s và ×3,8 đúng tỉ lệ. Kéo điểm xuống: cú đẩy vào nhà không có nhà (55–60), sương giả, mũi tên trang trí, zoom cắt chân chồng, và cảnh mở gợi đọc nhầm. |
| Liền mạch hình–lời–âm | **3** | Đồng bộ mốc rất tốt (lệch rõ nhất chỉ ở Q1, khoảng −0,24 s). Kéo điểm xuống: nhà nhảy chỗ mỗi lần đổi chế độ, crossfade ở 29,0, nhãn nhảy chỗ ở 55,5, 3 tick cho khoảng 8 SOLD, mốc `lvl` không có hình, và b11 thiếu âm dữ liệu. |
| Nhịp | **3** | Không có đoạn chết trên 3 s khi lời chạy liên tục. Khoảng lặng ở 62,7 thở tốt. Kéo điểm xuống: 20–27 s gần như trống, 47–55 s dồn nhãn. |
| Âm | **3** | Lời sạch, nhạc đi đúng hướng, khoảng lặng sau "cap" đạt. Kéo điểm xuống: whoosh dày, tick đếm sai, thiếu âm dữ liệu cuối, tension tầng giữa phẳng, và music plan mâu thuẫn với beat b10. |

### Năm sửa quan trọng nhất

1. **55,1–59,8, cTip không có nhà.** Khung lại cTip để thấy mặt đất, nhà cạnh chân chồng và một mẩu chân chồng. Gắn mũi tên "rose" ngay cạnh nhà. Nếu không làm được thì đổi lý do cú máy, vì hiện tại cú đẩy hứa một thứ không có trên hình.
2. **47–63 s, zoom cắt chân chồng và mất trục.** Thêm dấu ngắt trục hoặc giữ chân chồng trong khung. Thêm 2–3 vạch năm (2022, 2024, 2026). Kéo ngoặc "past the cap" (62,0) **sát mép phải chồng** thay vì cách khoảng 20% khung.
3. **Nhãn đè đường:** "home value" và "2026 Q2" (19,5–23), "Back under" (49,5–55), "Stayed over…" đè chồng (56–59). Thêm luật né đường cho nhãn, cố định "$500,000 cap" ở một chỗ (bỏ cú nhảy ở 55,5), và để hai nhãn lịch sử rời khung theo cú đẩy thay vì mờ ở 55,0.
4. **Tính liên tục giữa hai chế độ (15,0→15,5; 41,5→42,0; 29,0) và cảnh mở 0–4,5.** Ở chế độ thế giới cũng đặt nhà **cạnh** chồng như ở chế độ đồ thị. Như vậy nhà không nhảy chỗ, và cảnh mở không gợi "giá nhà vượt trần". Bỏ crossfade ở 29,0.
5. **Âm và hình b1 + b11:**
   - Một tick cho mỗi biển SOLD (khoảng 8), hoặc giảm số biển xuống 3.
   - Thay "làm tối" ở 4,96 bằng sương hoặc nhoè thật.
   - Thêm âm dữ liệu "lên một quãng" ở 65,4 và một hành động hình cho `lvl` 67,7 (ví dụ nhấn ngoặc ×1).
   - Bỏ whoosh ở các cú push/pull nhỏ (30,7 · 34,5 · 55,1 · 64,1).
   - Thống nhất music plan với b10 (nhạc trở lại ở "Phoenix" hay ở "three").
