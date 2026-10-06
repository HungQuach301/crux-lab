# Đánh giá đạo diễn — E5f / ep005 — cold open 34 s (bản xem trước 540p)

Nguồn đã xem: sheet-1/2 (khung 0,5 s), audio.png, transcript.txt, events.txt, intent.txt.
Quy ước: sự kiện thấy lần đầu ở khung t thì đã xảy ra trong khoảng (t−0,5; t]. Sai số đo bằng mắt chỉ chính xác tới ±0,5 s. Ngưỡng chấp nhận: ±0,2 s.
Chỗ không thấy được ở bước 0,5 s thì ghi "không kiểm được", tôi không suy đoán.

## 1. Chỗ LỆCH hình / lời / âm và chỗ hình KHÁC ý đồ

### 1a. Đồng bộ theo từ khóa

| Mốc lời (sóng âm) | Hình dự kiến | Thấy lần đầu | Âm | Kết luận |
|---|---|---|---|---|
| "saved" 0,71 | chồng teal đặt xuống | 1,0 (có trong khoảng 0,5–1,0, nằm cạnh nhà) | tick 0,71 | Khớp được (sai số ≤ ±0,3, chưa phân giải được) |
| "ten" 1,13 | chồng trượt vào dưới nhà | 1,5 (nhà được nâng lên, teal nằm dưới) | land 1,13 | Khớp (khoảng 1,0–1,5) |
| "price" 2,55 | tháp giá mọc lên, nâng nhà | 3,0 | rise 2,55 | Khớp (2,5–3,0) |
| "insurance" 5,66 | khiên rơi lên mái + nhãn "buy now + mortgage insurance" | 6,0 | land 5,66 | Khớp (5,5–6,0) |
| "renting" 7,26 | căn hộ + nhãn "keep renting, keep saving" + chồng teal thứ hai | 7,5 | — | Khớp (7,0–7,5) |
| **"twenty" 8,46** | **chồng tiết kiệm lớn dần tới vạch 20 %** | **Không thấy. Ở 7,5, 8,0, 8,5 và 9,0 chồng có cùng độ cao, vạch vàng đã có sẵn từ 7,5** | rise 8,46 | **LỆCH / KHÁC ý đồ.** Có âm "rise" nhưng hình không đổi. Nếu có lớn thì quá nhỏ, không đọc được ở 540p |
| "schedule" 10,64 | đường lịch trả nợ bắt đầu vẽ từ 90 % | 11,0 (đoạn ngắn) | land 10,10 | Khớp. Riêng "land" 10,10 không có vật nào hạ cánh |
| "eight" 13,75 | đường chạm vạch 80 % ở năm 8, ánh sáng + nhãn "about 8 years" | 14,0 | chime 13,75 | Khớp (13,5–14,0). Đây là nhịp tốt nhất của đoạn |
| "replayed" 15,70 / "month" 17,59 | bó đường hiện dần từ trái sang phải | 16,0 (đã có mép trái), 17,5–19,5 lan dần | nốt dữ liệu | Khớp |
| "paper" 20,35 | — (không có sự kiện) | không có gì mới từ 19,5 tới 21,0 | — | Không lệch, nhưng hình chết khoảng 2 s (xem mục 3) |
| "typically" 21,51 | đường điển hình sáng lên | 21,5 nhãn "typical ≈ 2 years" mờ, đang hiện; 22,0 nhãn và đường trắng rõ | (không có nốt riêng trong events) | Khớp (21,0–21,5, chuyển động bắt đầu ngay quanh từ khóa) |
| "slow" 22,34 | đường chậm chuyển màu cảnh báo | 22,5 có đường vàng + "slow cases" | — | Khớp |
| "paper" 24,39 | nhãn "loan 90%" | 24,5 | — | Khớp |
| "eighty" 26,05 | chồng vay chạm vạch, hiện "80% on paper" | 26,0 vẫn là "81%"; 26,5 thấy "80% on paper" | chime 26,05 | Khớp (26,0–26,5; trường hợp xấu nhất +0,45, không phân giải được) |
| "value" 27,19 | nhãn "home value / by a national price index" | **27,0 đã hiện mờ** | — | **Sớm ≥ 0,19 s** (nhãn bắt đầu trong khoảng 26,5–27,0), ở mép ngưỡng. Phần chữ "by a national price index" xuất hiện trước từ "index" (28,72) khoảng 1,7 s |
| "removed" 31,82 | khiên rung rồi đứng yên + nhãn "insurance still on" | nhãn ở 32,0; không thấy khiên rung (khung 31,5 và 32,0 giống nhau) | impact 31,82 | Nhãn khớp. Rung: không kiểm được. Âm khác ý đồ: intent yêu cầu "tick trầm", bản dựng dùng "impact" |

Chuyển động máy so với lời:
- whoosh_mode 9,00 đè lên đuôi "percent?" (8,88–9,22).
- whoosh_mode 29,14 đè lên đuôi "index." (28,66–29,18).
- Hai chỗ này nhỏ nhưng trái quy tắc "máy chỉ chạy giữa các từ khóa". Nên lùi mỗi chỗ khoảng 0,2 s.

### 1b. Hình KHÁC ý đồ / thiết kế
1. **Con số 20 % không có hình** (8,46): xem bảng trên. Lối "thuê" chỉ còn một chồng tiền đứng yên.
2. **Mốc 0–2,5 s:** intent ghi nhà đứng trên chồng tiền mờ bằng giá nhà ngay từ đầu. Bản dựng không có chồng mờ, tháp giá chỉ mọc lên ở "price". Cách này khớp với brief mới (tháp mọc lên) nên chấp nhận được, nhưng intent.txt cần cập nhật cho khớp.
3. **cDef 24,0–29,0: căn nhà nằm CẠNH chồng giá trị**, lơ lửng ở mép trên bên trái, chứ không ở trên đỉnh. Điều này trái với ghi chú thiết kế "nhà luôn ở TRÊN chồng, đỉnh mái là điểm dữ liệu". Ở chế độ world (30,0 trở đi) nhà lại nằm trên tháp, nên cùng một vật có hai quy ước khác nhau.
4. **"about 8 years" thành nhãn mồ côi từ 16,5 đến 23,0.** Đường lịch trả nợ đã biến mất từ 16,5 nhưng nhãn vẫn nằm trên trục, nên người xem dễ hiểu nhầm rằng nó gắn với bó dữ liệu thật.
5. **Khung 29,5 gần như đen hoàn toàn**, chỉ còn một mẩu nhà ở mép phải. Hai chồng cDef biến mất thay vì để máy đi tới chúng như vật cùng một thế giới (xem mục 2).
6. Chồng vay xám đậm xuất hiện mới ở 30,0, có một mảnh đang rơi hoặc nằm dưới đất. Brief cho phép điều này ("at the end"), nhưng chồng không được giới thiệu bằng lời.

## 2. Chuyển cảnh và chuyển chế độ

| Mốc | Loại | Lý do (theo intent) | Đánh giá |
|---|---|---|---|
| 2,96–3,96 | lùi máy wYou→wFork | cần thấy cả hai lối | **Liền mạch.** Máy chạy đúng trong khoảng lặng 2,88–4,10, có whoosh nhẹ. Hợp lý |
| 9,00–10,10 | world→chart (cSched) | lịch trả nợ là một đường theo thời gian | **Liền mạch về chuyển động**: ở 9,5 thế giới trượt sang trái, trục đồ thị vào từ phải, đúng tinh thần "cùng một thế giới". **Yếu về nghĩa**: không có vật nào của thế giới (nhà, chồng teal) biến thành điểm 90 % của đường. Kiểu 3Blue1Brown sẽ cho đỉnh chồng vay hoặc giá trượt thành điểm xuất phát của đường |
| 15,5–16,0 | đổi nội dung trong chart (lịch → dữ liệu thật) | — | **Tốt**: thang trục giữ nguyên (80/90 không đổi vị trí, chỉ thêm 100 %), nhãn ILLUSTRATIVE tắt đúng lúc dữ liệu thật vào. **Lỗi**: nhãn 8 năm còn sót lại |
| 23,13–24,13 | lia máy cSched→cDef | định nghĩa cần hai chồng cạnh nhau | **Tạm liền**: ở 23,5 bó đường trượt trái. Nhưng chồng trong cDef là vật mới, vì nhà nhỏ đứng cạnh chồng chứ không phải tháp giá của world |
| 29,14–30,04 | chart→world (wHouse) | bảo hiểm gắn với căn nhà | **GÃY.** Khung 29,5 gần như đen trống. Hai chồng cDef (giá trị, vay) không được máy "đi tới" để lộ ra là tháp giá và chồng vay của world; chúng mất đi rồi world trôi vào từ mép phải. Ở 30,0 quy ước hình học đổi (nhà ở trên tháp, chồng vay đứng cạnh) |

## 3. Nhịp
- **5 s đầu: móc ở mức trung bình–yếu.**
  - Lời vào ngay ở 0,0 là tốt.
  - Khung 0–2,5 s tĩnh và xa: nhà, hình nhân, căn hộ đều nhỏ, nửa trên khung đen trống. Chồng 10 % chỉ còn vài pixel.
  - Hình mạnh đầu tiên là tháp giá vọt lên ở khoảng 2,6–3,0. Hình này tốt nhưng đến muộn và nhỏ.
  - Câu hỏi gây tò mò ("buy now… or keep renting") phải tới 4,1 mới vào, và nhãn hai lối tới 6,0 / 7,5 mới hiện.
  - So với Vox: chưa có "điều lạ" nào trong 3 s đầu.
- **Chỗ chùng:**
  - 14,0–15,5: nhãn 8 năm đã hiện, sau đó đứng yên 1,5 s trong khoảng lặng của lời. Chấp nhận được vì đây là chỗ thở sau một ý đắt.
  - **19,5–21,4**: bó đường đã vẽ xong, "on paper" (20,35) không có hình, cộng khoảng lặng 1,06 s của lời. Hình chết khoảng 2 s đúng lúc tension nhạc lên cao nhất (0,8).
  - 32,0–34,0: đứng yên 2 s, nhạc nhả rồi tắt. Đoạn kết chùng, không có cú cắt sang tiêu đề.
- **Chỗ dồn / rối:**
  - 21,5–22,5: "typical ≈ 2 years" và "slow cases" vào cách nhau 0,8 s, trên nền bó 300 đường, cạnh nhãn mồ côi 8 năm.
  - Phát hiện quan trọng nhất của đoạn là "thực tế thường chỉ khoảng 2 năm, so với 8 năm theo lịch". Nó lại là chữ nhỏ nhất, chen giữa các chữ khác.

## 4. Lớp bắt buộc (nguồn, ILLUSTRATIVE, dòng miễn trừ)
- **Có đè hình không:**
  - Hai dòng miễn trừ ở chân hình ("Past buyers, measured… / US only…") nằm sát trục x (16,0–29,0). Ở cSched chúng bám ngay dưới nhãn năm, nên chân hình chật.
  - Nhãn nguồn và ILLUSTRATIVE ở góc trên không đè lên dữ liệu.
  - Đỉnh bó đường (khoảng 110 %) lên sát dòng tiêu đề, cách khoảng 15 px ở 540p.
  - "slow cases" nằm chồng lên lưới đường trắng.
- **Đọc trên điện thoại** (đo trên crop gần độ phân giải gốc 540p):
  - Số trục khoảng 10 px (≈ 1,9 % chiều cao).
  - Miễn trừ, nguồn, tiêu đề khoảng 13–14 px (≈ 2,5 %).
  - "about 8 years", "typical ≈ 2 years", "80% on paper" khoảng 16–18 px (≈ 3 %).
  - Trên điện thoại cầm dọc, các cỡ này còn lần lượt khoảng 4 px, 5 px, 6–7 px, nên **phần lớn không đọc được**. Chỉ "80% on paper" và "insurance still on" là tạm đọc được.
  - Nhãn "You" và nhãn hai lối (≈ 12 px) cũng nhỏ.
- **Chữ chồng / cắt mép:**
  - "typical ≈ 2 years" và "about 8 years" nằm trên cùng một đường nền, cách nhau khoảng 45 px. Đọc thành hai con số song song, dễ nhầm.
  - Không thấy chữ bị cắt mép.
  - Khung 9,5 và 29,5 có vật bị cắt ở mép, nhưng đó là do chuyển cảnh nên chấp nhận được.

## 5. Âm
- **Lời rõ:**
  - Giọng đỉnh khoảng −10 đến −6 dBFS.
  - Nhạc nằm khoảng −45 đến −33 dBFS, tức thấp hơn giọng 25–30 dB.
  - Không có gì che lời.
- **Nhạc theo căng–chùng: yếu.**
  - Bản đồ tension đi từ 0,15 lên 0,8 (15,6), rồi xuống 0,1.
  - Mức nhạc thực tế chỉ dao động khoảng 5–8 dB, gần như phẳng, và quá thấp nên tai không nhận ra cao trào ở 15,6–23.
  - Các accent 13,75 và 26,05 nghe được chủ yếu nhờ chime, không nhờ nhạc.
- **Kết thúc:**
  - Nhạc dừng hoặc nhả từ 31,82 tới khoảng 34 thì tắt dần.
  - Về kỹ thuật là gọn. Về kịch thì sai chức năng: cold open nên kết bằng một nốt treo hoặc cú cắt vào tiêu đề, không nên fade nhẹ.
- **Âm dữ liệu:**
  - 17 nốt trong khoảng 10,6–22,3, đỉnh khoảng −20 đến −25 dBFS, to hơn nhạc khoảng 15 dB và chạy đè lên lời suốt 11 s.
  - Ở cSched có ý nghĩa (mỗi năm một nốt, chạm 80 % thì chime).
  - Ở bó dữ liệu, nhịp nốt gần như không đổi. Không nghe ra "nốt sáng" cho đường điển hình và "nốt trầm" cho đường chậm như intent yêu cầu (events không ghi hai nốt này).
- **Hiệu ứng thừa / sai:**
  - "land" 10,10 (không có vật nào hạ cánh).
  - "rise" 8,46 (không có hình lớn lên).
  - "impact" 31,82 quá nặng so với ý đồ "tick trầm, chưa". Nó cũng chồng lên chữ "removed".
  - Bốn whoosh trong 34 s ở mức chấp nhận được.

## 6. 3D: làm ý rõ hơn hay chỉ trang trí
- **Làm ý rõ hơn:**
  - Tháp giá nâng nhà (3,0): 10 % nằm ở đáy là một ẩn dụ tốt.
  - Hai chồng cDef: giá trị lớn lên, vạch 80 % của giá trị hạ xuống gặp đỉnh chồng vay. Hình học đúng: ở 24,5 vay/giá trị ≈ 150/170 px ≈ 88 %; ở 27,5 ≈ 150/183 px ≈ 82 %, vạch nằm ở khoảng 80 % chiều cao. Hình nói đúng điều "on paper": giá tăng chứ không phải nợ giảm.
- **Trang trí hoặc làm rối:**
  - Hình nhân "You" không làm gì.
  - Chồng 20 % đứng yên.
  - Khiên vàng nhỏ (≈ 15 px) khó thấy.
- **Tỉ lệ 10 % so với giá:**
  - Ở 3,0, teal ≈ 18 px so với phần tháp dưới nhà ≈ 175 px, tức khoảng 10 %. Con số này đúng nếu chỉ tính chồng tiền.
  - Theo quy ước "đỉnh mái = giá" (tổng ≈ 310 px), teal chỉ còn khoảng 6 %. Nghĩa là bản dựng tự trái quy ước của mình.
- **90 % → 80 %:**
  - Ở cDef: đúng (xem trên).
  - Ở world 30,0–33,5: chồng vay xám ≈ 90 px so với tháp giá ≈ 100 px dưới nhà (≈ 90 %), hoặc ≈ 220 px tới đỉnh mái (≈ 40 %). Cả hai đều **không ra 80 %** ngay sau khi vừa nói "eighty percent". Đây là mâu thuẫn dữ liệu giữa hai chế độ (đo trên hình phối cảnh nên chỉ gần đúng).

## 7. Chấm điểm (so với Vox / 3Blue1Brown / WSJ)

| Tiêu chí | Điểm | Lý do ngắn |
|---|---|---|
| Hình mang nghĩa | **3** | Tháp giá, đường 8 năm và hai chồng "on paper" đều tốt. 20 % không có hình, phát hiện "2 năm" bị chìm, nhà và chồng không giữ cùng quy ước giữa hai chế độ |
| Liền mạch hình–lời–âm | **3** | 10/11 điểm khớp, nhưng có nhãn mồ côi, khung đen ở 29,5 và âm thanh không có hình ("rise", "land") |
| Nhịp | **3** | Móc 5 s đầu yếu, hình chết khoảng 2 s ở 19,5–21,4, kết chùng |
| Âm | **2** | Lời rõ, nhưng nhạc quá thấp và phẳng nên không mang căng–chùng. Nốt dữ liệu lấn nhạc và đè lời, hiệu ứng sai loại |

### Năm sửa quan trọng nhất
1. **8,46–9,0:** cho chồng tiết kiệm bên căn hộ lớn gấp đôi (10 → 20 %) bắt đầu đúng "twenty", rồi giữ tới 9,1 trước khi máy chạy. Lùi whoosh_mode sang khoảng 9,25 để không đè "percent".
2. **16,5–23,0:** tắt "about 8 years" khi đường lịch biến mất, hoặc giữ đường lịch dưới dạng bóng mờ làm mốc so sánh. Ở 21,5 đưa "typical ≈ 2 years" thành chữ lớn nhất khung (≥ 22 px ở 540p), tách xa nhãn 8 năm. Lấp chỗ chết 19,5–21,4 bằng một nhịp sáng của vạch 80 % đúng chữ "paper" (20,35).
3. **24,0–30,0:** đặt nhà lên đỉnh chồng giá trị ở cDef (giống world). Ở lần chuyển 29,14, máy phải đi tới chính hai chồng này rồi lộ ra chúng là tháp giá và chồng vay của world, không để khung trống như 29,5. Chồng vay ở world phải bằng 80 % theo cùng quy ước với cDef.
4. **Mix âm 10,1–34:**
   - Nâng nhạc khoảng 8–10 dB và cho nhạc lên thật sự ở 15,6–23.
   - Hạ nốt dữ liệu xuống dưới nhạc khi đè lời, thêm nốt sáng ở 21,51 và nốt trầm ở 22,34.
   - Bỏ "land" 10,10 và "rise" 8,46 (hoặc để "rise" khớp với sửa số 1).
   - Đổi "impact" 31,82 thành tick trầm.
   - Kết ở 32,8 bằng nốt treo hoặc cú cắt sang tiêu đề, thay cho fade 2 s.
5. **0–5 s và chữ:**
   - Mở máy gần hơn: "You" và chồng teal chiếm ≥ 1/4 khung, để tháp giá vọt lên ở 2,55 thành hình chính.
   - Nâng mọi chữ bắt buộc lên ≥ 3,5–4 % chiều cao khung (khoảng 20 px ở 540p).
   - Gộp hai dòng miễn trừ (16,0–29,0) thành một dòng.
