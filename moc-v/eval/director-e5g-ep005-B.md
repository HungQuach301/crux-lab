# Đánh giá đạo diễn: E5g ep005, cold open 34 s (bản xem trước 540p)

Nguồn đã xem: sheet-1/2 (khung cách nhau 0,5 s), audio.png, transcript.txt, events.txt, intent.txt. Khung cách nhau 0,5 s, nên một sự kiện thấy lần đầu ở khung t đã xảy ra trong khoảng (t−0,5; t]. Chuẩn lệch là ±0,2 s; sai số khung ±0,5 s. Mốc lời lấy theo sóng âm (intent).

## 1. Chỗ lệch hình / lời / âm; chỗ hình khác ý đồ

| Mốc lời (sóng âm) | Hình quan sát | Âm (events) | Kết luận |
|---|---|---|---|
| "saved" 0,707 | Ở 0,5 chỉ có nhãn "You", chưa thấy tiền | tick 0,71 | Ở 0,5 chưa có hình gắn với "saved". Tick 0,71 không có hình đi kèm, đến 1,0 mới thấy (khoảng 0,3–0,8 s sau). Không vượt chuẩn với "ten". |
| "ten" 1,13 | Chồng teal đã nằm cạnh nhà ở 1,0, đã nằm dưới nhà ở 1,5 | land 1,13 | Khớp trong sai số khung |
| "price" 2,55 | 2,5 chưa có, 3,0 tháp giá đã nâng nhà | rise 2,55 | Khớp (2,5; 3,0] |
| "insurance" 5,656 | Khiên vàng và nhãn "buy now + mortgage insurance" có ở 6,0, chưa có ở 5,5 | land 5,66 | Khớp. Nhãn tên lối "buy now" ra trễ ~1,4 s so với "buy" 4,22, chấp nhận được vì nhãn đi cùng khiên. |
| "renting" 7,26 | Nhãn "keep renting, keep saving" và chồng teal ở căn hộ có ở 7,5 | (không) | Khớp |
| "twenty" 8,457 | Mũi tên xanh bắt đầu ở 8,5, rõ ở 9,0 | rise 8,46 | Khớp |
| "schedule" 10,644 | **Tiêu đề, trục 90 %/80 % và nhãn 0–10 years đã có ở 10,0** | land 10,10 | **Chữ đồ thị ra sớm ≥ 0,64 s.** Theo luật "số chỉ hiện ở CHART" thì không sai, nhưng nó đi trước keyword. Đường bắt đầu vẽ trong (10,5; 11,0], khớp. |
| (không keyword) | Dòng nguồn, nhãn ILLUSTRATIVE và chân "A measurement, not a next step" bật cùng lúc ở 11,0 | — | Ba lớp chữ đổ vào giữa câu "you can't even ask", không gắn từ nào |
| "eight" 13,753 | 13,5 đường mới ở ~6,5 năm; 14,0 chạm vạch 80 % có chớp sáng và nhãn "about 8 years" | chime 13,75 | Khớp |
| "replayed" 15,697 | Bó đường bắt đầu ở 16,0, đổi tiêu đề, ILLUSTRATIVE tắt | (data notes) | Khớp |
| "month" 17,587 | Bó quét liên tục, đến ~19,5–20,0 thì xong | data notes | Khớp về ý. **Nghi vấn:** trên audio.png các nốt dữ liệu (đỏ) có vẻ còn kéo đến ~22,3, trong khi bó đã quét xong ở ~20 s. Đoạn 20–21,5 có thể có nốt mà không có hình đi kèm. Từ ảnh không xác định chắc. |
| "paper" 20,347 | Không có thay đổi nhìn thấy | — | Intent không gán hình nên không tính lỗi |
| "typically" 21,508 | Nhãn "typical ≈ 2 years" mờ ở 21,5, đường trắng sáng rõ ở 22,0 | (nốt sáng) | Khớp |
| "slow" 22,344 | Đường vàng và nhãn "slow cases" có ở 22,5 | (nốt trầm) | Khớp |
| "paper" 24,387 | Ở 24,5 có "loan" và số đếm "90 %" | — | Khớp |
| "eighty" 26,046 | 26,0 ghi 81 %; 26,5 có vạch ngang và "80% on paper" | chime 26,05 | Khớp |
| "value" 27,187 | "home value / by a national price index" có ở 27,5 | — | Khớp với "value". Phần "by a national price index" ra trước chữ "index" (28,72) ~1,2 s. |
| "removed" 31,82 | "insurance still on" có ở 32,0. Từ ảnh tĩnh không thấy khiên rung. | impact 31,82 | Khớp về thời điểm. Không xác nhận được hiệu ứng rung. |

Tất cả cue đều nằm trong sai số một khung, phù hợp với số đo pixel 11/11. Phần lệch thực sự là chữ không gắn keyword (10,0 và 11,0).

**Chỗ hình khác ý đồ:**
- **0,0–2,5:** intent c0 muốn nhà đứng trên chồng mờ = giá ngay từ đầu, để thấy ngay khoảng cách 10 % so với giá. Hình thật mở bằng một căn nhà đặt trên đất, không có chồng mờ, nên phải đến 3,0 mới thấy tỉ lệ.
- **9,5 (WORLD→CHART):** ghi chú thiết kế yêu cầu nhà co vào đỉnh chồng của nó (morph). Hình thật là một cú trượt: cảnh thế giới trôi sang trái, nhà vẫn nằm nguyên trên tháp, còn đường đáy của đồ thị thò vào từ bên phải. Có một khung nhà và đường đồ thị cùng hình, nên điểm 90 % của đồ thị không sinh ra từ tháp.
- **29,5 (CHART→WORLD):** bó 307 đường của c3 hiện lại mờ ở mép trái. Máy quay lùi qua cảnh cũ, đi ngược chiều kể chuyện.
- **24,0–27,5:** chồng sáng (giá trị nhà) không có nhãn suốt ~3,5 s, trong khi số của chồng vay đang đếm 90→80 %. Người xem không biết 80 % là "của cái gì" cho tới 27,5.
- **7,5–9,0:** vạch 20 % mờ và chồng lớn dần chỉ cao vài pixel. Khó thấy chồng có thực sự chạm vạch 20 % không.

## 2. Chuyển cảnh và chuyển chế độ

| Thời điểm | Loại | Lý do | Đánh giá |
|---|---|---|---|
| 2,96–3,96 | Lùi máy wYou→wFork | Cần thấy cả hai lối | **Liền mạch.** Lấp đúng khoảng lặng 2,88–4,10. Điểm trừ nhỏ: lùi máy bắt đầu ngay khi tháp đang nâng (3,0), hai chuyển động chồng nhau. Lối "rẽ" không có đường hay ngã ba hiện ra, chỉ là một khung rộng hơn. |
| 9,0–10,1 | WORLD→CHART | Lịch trả nợ là đường theo thời gian | **GÃY về nghĩa.** Thời điểm thì đúng (khoảng lặng 9,18–10,34), nhưng morph không xảy ra. Ở khung 9,5 nhà bị cắt mép trái và nằm cạnh đường đồ thị. Dữ liệu không được "chở" từ tháp sang điểm 90 %. |
| 15,0–16,0 | Đổi đồ thị (lịch → bó lịch sử) | — | **Liền mạch.** Thang 80/90 giữ nguyên, chỉ thêm 100 %. Đường lịch còn lại làm mốc so sánh. Tốt. |
| 23,13–24,13 | Lia trong CHART sang hai chồng | Định nghĩa cần hai chồng cạnh nhau | **Liền mạch vừa phải.** Đường vàng "slow" trượt ra trái (khung 23,5) trông tự nhiên. Hai chồng hiện ra không nối với đường nào. |
| 29,14–30,04 | CHART→WORLD | Bảo hiểm gắn với căn nhà | **GÃY.** Ở 29,5 bó đường cũ quay lại. Ở 30,0 có một tấm xám nằm trên đất và một mẩu vật ở mép phải. Chồng vay xám đậm dựng cạnh nhà mà không rõ nó là chồng "loan" vừa thấy trên đồ thị. |

## 3. Nhịp

- **5 s đầu (móc):** yếu-trung bình. Từ 0,0 đến 1,0 khung tối, vật nhỏ, đứng yên; chỉ có nhãn "You" hiện lên. Hình mạnh đầu tiên (tháp giá cao vọt so với 10 %) đến ở 3,0, gần như là thứ duy nhất có thể móc người xem. Câu hỏi "buy now … or keep renting" ở 4,1 không có hình căng thẳng nào đi kèm cho tới khiên ở 6,0. Cần có xung đột trên hình ngay từ 0–1 s.
- **Chùng:**
  - 14,4–15,5: đường đã chạm 80 %, khung đứng yên, tiêu đề mờ dần. Chấp nhận được vì là khoảng thở sau ý "8 năm".
  - 32,2–34,0: khung tĩnh ~1,8 s ở cuối. Chấp nhận được với nhạc nhả.
  - 0,0–1,0: không có gì xảy ra.
- **Dồn/rối:** c3 (21,5–23,0). Bó dày đặc, đường trắng "typical", đường vàng "slow", ba nhãn và hai dòng chân trang cùng đổ vào trong 1,5 s; nhãn "typical" đè lên nhãn "schedule" (xem mục 4). Phát hiện lớn nhất của đoạn mở (2 năm so với 8 năm) chìm trong mớ đường.
- **Đều:** các khoảng lặng của giọng (2,9–4,1; 9,2–10,3; 23,1–23,9; 29,2–30,0) đều được lấp bằng chuyển động máy. Đó là cấu trúc đúng.

## 4. Lớp bắt buộc (chữ, nhãn, nguồn)

- **Chữ chồng:** 22,0–23,0, "typical ≈ 2 years" dính vào "schedule ≈ 8 years", đọc thành "typical ≈ 2 yearschedule ≈ 8 years". Đây là lỗi rõ nhất. Ở 26,5–29,0 vạch 80 % đâm thẳng vào đầu chữ "80% on paper" (lỗi nhẹ).
- **Đè hình:** ở 16,0–23,0 đỉnh bó vượt 100 %, sát dòng tiêu đề nhưng chưa đè. Hai dòng chân trang nằm sát trục x.
- **Quá tải lớp:** mỗi khung CHART có 5–6 lớp chữ: nguồn, ILLUSTRATIVE, tiêu đề, trục, nhãn và 1–2 dòng chân trang. ILLUSTRATIVE bật/tắt ba lần (11,0 bật, 16,0 tắt, 24,5 bật). Chân trang "A measurement, not a next step" (11–15,5) khó hiểu ở chỗ đó.
- **Đọc trên điện thoại (quy về 1080p):**
  - Tiêu đề và chân trang khoảng 30–36 px: đọc được nhưng nhỏ.
  - Số trục 0/2/4…/10 years khoảng 24 px: **quá nhỏ cho điện thoại**.
  - Nhãn "about 8 years" và "80% on paper" khoảng 40–45 px: được.
  - Nhãn WORLD ("buy now + mortgage insurance", "keep renting, keep saving") khoảng 36 px: hơi nhỏ.
- **Khoảng trống:** c2 dùng chưa đến 1/4 chiều cao khung cho dữ liệu, phía trên là một khoảng đen lớn. Ở c4 hai chồng chỉ chiếm ~1/3 chiều cao khung.
- **Cắt mép:** 9,5 nhà và tháp bị cắt mép trái; 29,5 và 30,0 có mảnh vật ở mép phải. Cả hai đều là khung chuyển cảnh.

## 5. Âm

- **Lời:** rõ. Giọng đỉnh khoảng −8 đến −15 dBFS, nhạc khoảng −30 đến −45 (thấp hơn ≥ 15–20 dB). Chime ở "eight" (13,75) thấp hơn giọng ~12 dB, không che chữ.
- **Nhạc theo căng–chùng:** mức nhạc trên audio.png gần như phẳng (−30 đến −45) suốt 4–30 s. Không thấy nhạc dâng ở 15,6 (tension 0,8) hay nhả ở 24,3 bằng mức âm lượng. Nếu căng–chùng nằm ở phối khí thì ảnh không thể hiện; ít nhất là mức không theo bản đồ căng thẳng. Nhạc nhô lên trong các khoảng lặng (~−25 ở 9,8–10,4), đúng kiểu ducking.
- **Kết thúc:** nhạc không tắt dứt ở 31,82. Nó suy dần từ −40 xuống −55 tới 34 s, không thấy rõ một hợp âm chốt. Kết hơi mềm cho một cold open, nên có một điểm nhấn để cắt sang tiêu đề.
- **Âm dữ liệu:** có (17 nốt, 10,6–22,3), khoảng −25 đến −30 dBFS, rải đều, nghe được giữa các chữ. Nghi vấn ở mục 1: nốt có thể còn kéo dài khi bó đã quét xong (20–21,5 s).
- **Hiệu ứng thừa:** 12 SFX, 17 nốt dữ liệu và 3 accent trong 34 s là dày.
  - Cụm rise 8,46 + whoosh_mode 9,00 + land 10,10 rơi trong 1,6 s.
  - Cụm rise 2,55 + whoosh_soft 2,96 cách nhau 0,4 s.
  - "land" ở 10,10 và 30,04 không có vật nào "đáp" trên hình: thừa.

## 6. 3D: làm rõ ý hay trang trí

- **Làm rõ ý:** c0 tốt. Tháp giá nâng nhà, chồng teal là phần đáy, thấy ngay 10 % là nhỏ. Ở 3,0 phần teal ≈ 7/57 px ≈ 12 % chiều cao tháp, đúng ~10 % trong giới hạn đo thumbnail. Khiên trên mái (c1, c5) là một biểu tượng rõ, và "vẫn ở đó" ở cuối là một hình kết có nghĩa.
- **Trang trí / yếu:**
  - Lối thuê ở c1: chồng teal tăng tới 20 % nhỏ đến mức gần như vô hình.
  - Căn hộ là khối lớn nhất cảnh nhưng không mang dữ liệu.
  - Cuối cảnh (30–34) có hai chồng teal (dưới nhà và ở căn hộ) cùng lúc, nên tiết kiệm như bị đếm hai lần. Hai lối song song chưa được tách bằng hình.
- **Tỉ lệ 90 %→80 %:**
  - c2 cắt trục còn 80–90 % (sau đó 80–100 %). Mức giảm 10 điểm phần trăm trông như một cú rơi lớn, nhưng có nhãn trục nên chấp nhận được.
  - c4 có hai chồng từ đáy 0, trung thực hơn: đo khoảng 54/65 px ≈ 83 % khi ghi 80 %, trong sai số đo.
  - Ở c4 khó thấy cái gì đang đổi (vay giảm hay giá trị tăng): chồng sáng chỉ cao thêm ~5 px.
  - Chồng vay ở WORLD (30,5+) có vẻ ≈ 75–80 % tháp, khớp ý nhưng không có gì nối nó với chồng "loan" trên đồ thị.

## 7. Điểm (1–5, so với Vox / 3Blue1Brown / WSJ)

| Tiêu chí | Điểm | Lý do ngắn |
|---|---|---|
| Hình mang nghĩa | **3** | c0, c2, c4 có nghĩa. Morph WORLD↔CHART không có. Phát hiện "2 năm" bị chìm. Lối thuê quá nhỏ. |
| Liền mạch hình–lời–âm | **3** | Cue đều trong sai số khung. Hai chuyển chế độ gãy (9,5; 29,5). Chữ ra trước keyword (10,0; 11,0). Nhãn đè nhau ở 22–23. |
| Nhịp | **3** | Khoảng lặng được lấp tốt. Móc 0–1 s yếu. c3 dồn. |
| Âm | **3** | Lời sạch, mix an toàn. Nhạc không theo bản đồ căng thẳng. Kết mềm. SFX dày, có "land" thừa. |

### Năm sửa quan trọng nhất

1. **22,0–23,0:** tách nhãn "typical ≈ 2 years" khỏi "schedule ≈ 8 years" (đặt nhãn typical phía trên, tại x≈2 năm, có đường dẫn) và làm mờ bó khi đường điển hình sáng lên, để 2 so với 8 năm là thứ duy nhất nổi bật.
2. **9,0–10,1 và 29,14–30,04:** làm đúng morph. Nhà co vào đỉnh tháp, tháp thành chồng 100 %, phần nợ 90 % thành điểm đầu đường ở (0; 90 %). Không để nhà và đường đồ thị cùng khung. Ở chiều về, không lia ngược qua bó c3; chồng "loan" của c4 biến thành chồng vay cạnh nhà.
3. **0,0–2,5 (móc):** mở bằng nhà trên chồng giá mờ (đúng intent) và người xem cầm 10 % ngay từ khung 0. Đẩy máy gần hơn để vật chiếm ~1/2 chiều cao khung. Có thể cho chồng mờ "đập" xuống ở 0,0 để có chuyển động ngay giây đầu.
4. **10,0–29,0 (chữ):**
   - Chữ đồ thị ra theo "schedule" (10,64), không phải ở 10,0.
   - Bỏ chân "A measurement, not a next step".
   - Gộp hai dòng disclaimer thành một; giữ ILLUSTRATIVE nhất quán.
   - Số trục ≥ 40 px ở 1080p.
   - Phóng vùng dữ liệu c2 và c4 cho lấp khung.
   - Gắn nhãn "home value" ngay khi lia tới (24,1), không đợi đến 27,5.
5. **Âm và 7,5–9,0:** bỏ "land" 10,10 và 30,04, giãn whoosh_soft khỏi rise 2,55, dừng nốt dữ liệu khi bó quét xong. Cho nhạc dâng thật ở 15,6, tắt dứt và có hợp âm chốt ở 31,82. Ở lối thuê, đẩy máy gần hoặc phóng chồng 20 % và vạch 20 % để lối này đọc được trên điện thoại.
