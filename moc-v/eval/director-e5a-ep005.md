# Đạo diễn duyệt — E5a / ep005, cold open 34 s (bản xem trước 540p)

Nguồn đã xem: sheet-1/2 (khung cách 0,5 s), audio.png (mức theo lớp + phổ), transcript.txt (ASR), events.txt, intent.txt.
Quy ước: sự kiện thấy lần đầu ở khung t thì đã xảy ra trong khoảng (t−0,5; t]. Chỉ gọi là "sớm/trễ" khi khung chứng minh được vượt quá sai số đó.

---

## 1. Lệch hình / lời / âm (chuẩn ±0,2 s)

| # | Mốc | Lời (ASR) | Hình (khung) | Âm (events) | Kết luận |
|---|---|---|---|---|---|
| 1 | c0 chồng 10 % | "10" @1,04 (cue 1,13) | chưa có ở 0,5; có ở 1,0 → xuất hiện trong (0,5; 1,0] | tick 1,13 | Không chứng minh được lệch: hợp lệ nếu chồng xuất hiện trong [0,93; 1,0]. Tick nằm ở mép sau. Đạt. |
| 2 | c1 khiên rơi | "insurance" @5,64 | khung 5,5 đã có khiên trên không + nhãn "buy now + mortgage insurance"; 6,0 khiên đã nằm trên mái | land 5,66 | Khiên xuất hiện sớm nhất 0,16 s trước từ khoá, có thể sớm hơn. Ở biên, chấp nhận được. Nhãn hiện cùng lúc với "mortgage" là hợp lý. |
| 3 | c1 nhãn thuê + chồng lớn | "renting" @7,22; "20" @8,38 | nhãn "keep renting, keep saving" có ở 7,5; chồng cao gấp đôi ở 8,5 (khung 8,0 chưa có) | rise 8,46 | Đạt. |
| 4 | c2 đường chạm 80 % | "8" @13,54 (cue 13,753) | khung 13,5: đường **đã chạm** vạch 80 % ở ~8 năm, nhãn "about 8 years" mờ; 14,0: nhãn rõ + chấm sáng | chime 13,75 | Hình chạm vạch ≤ 13,5, chime 13,75 → **âm trễ so với hình ≥ 0,25 s** (khớp với ASR "8" nhưng lệch cue 0,21). Lệch nhẹ, thấy được. |
| 5 | c3 bó đường | "replayed" @15,70; "month" @17,58 | 15,5–18,0 chỉ vài đường ở góc dưới trái; **toàn bộ "núi" đường hiện bung trong (18,0; 18,5]**, sau "month, by month"; từ 18,5 tới 21,0 gần như đứng yên | 11 tick đều 15,70→20,35 | Hình không "dần dần trái→phải" theo tick: bó hiện gần như một lần. Các tick 19,42 / 19,88 / 20,35 (ít nhất 2–3 tick) **kêu trên ảnh đứng yên** → âm không còn gắn với dữ liệu. |
| 6 | c3 "typical" | "typically" @21,48 | có ở 21,5 | nốt sáng | Đạt. |
| 7 | c3 "slow cases" | "slow" @22,42 | đường vàng + nhãn có ở 22,5 | nốt trầm | Đạt, nhưng chỉ còn ≤ 0,6 s trước khi máy lia đi (khung 23,0 đã trượt) — xem §3. |
| 8 | c4 chồng vay về 80 % | "80" @26,10 (cue 26,046) | bộ đếm: 90 % (24,0) → 85 % → 81 % → **"80%" ở 25,5**; đường nối + "80% on paper" ở 26,0 | chime 26,05 | **Sớm thật sự**: con số 80 % trên màn ≤ 25,5, tức **≥ 0,55 s trước** khi nói "eighty" và trước chime. Lỗi đồng bộ rõ nhất của bản này (phép đo pixel 11/11 chỉ bắt nhãn "on paper", không bắt bộ đếm). |
| 9 | c4 "index" | "national" @28,00, "index" @28,66 | phụ đề "by a national price index" mờ ở 28,5, rõ ở 29,0 | — | Đạt. |
| 10 | c5 "removed" | "removed" @31,72 | "insurance still on" có ở 32,0, chưa có ở 31,5 | thud 31,82 | Đạt về thời điểm. Khiên "rung nhẹ rồi đứng yên" thì khung 0,5 s không cho thấy, nên không đánh giá được. |

**Hình KHÁC ý đồ**
- c0: chồng tiền dưới nhà theo ý đồ là "MỜ = giá nhà", nhưng trên khung là chồng xanh **đặc**, cùng chất liệu với chồng của người xem. Vì vậy ý "phần còn thiếu" không đọc ra.
- c0: chồng 10 % **nằm ngang** sát chân người xem, ở tiền cảnh, trong khi chồng giá nhà **dựng đứng** ở hậu cảnh. Không so được tỉ lệ (xem §6).
- c1: "vạch 20 % mờ" gần như không thấy ở 540p (chỉ một nét mảnh trên chồng ở 7,5–8,5).
- c3: ý đồ là "hiện dần trái → phải"; thực tế bó đường bung ra một lần ở ~18,3 (mục 5).
- c4: ý đồ là "KHOẢN VAY nhỏ dần". Thực tế cột vay **không đổi chiều cao**: đỉnh xám giữ y≈463 px từ 24,0 đến 26,0, chỉ cột giá trị cao thêm ~7 px/61 px. Như vậy là đúng dữ liệu (tỉ lệ đổi chủ yếu do giá tăng), nhưng khác ý đồ, và chuyển động quá nhỏ để thấy trên điện thoại. Con số làm hết việc.
- c5: ý đồ là "khiên VẪN ở trên mái **dù chồng vay đã thấp**". Cảnh thế giới ở 30,0–33,5 giống hệt cảnh 3,5 s: không có chồng vay nào thấp đi. Vế "dù… đã thấp" không có hình, chỉ còn chữ.

## 2. Chuyển cảnh / chuyển chế độ

| Mốc | Loại | Lý do | Liền mạch? |
|---|---|---|---|
| 2,175–3,175 pull wYou→wFork | camera lùi | "cần thấy cả hai lối" | Chuyển động mượt (2,5 → 3,0 → 3,5). Nhưng **lý do yếu**: căn hộ và nhà đã cùng trong khung từ 0,0, nên lùi máy không lộ ra thông tin mới, chỉ làm vật nhỏ đi. Máy cũng chạy trong lúc đang nói "a home's price". |
| 9,0–10,1 mode wFork→cSched | thế giới → đồ thị | "schedule là một đường theo thời gian" | **GÃY.** Khung 9,0 cả cảnh tối dần, nhãn mờ; 9,5 gần đen, vật lệch trái; 10,0 trục đồ thị trên nền khác hẳn. Đây là **dip-to-black / cross-fade**, trái nguyên tắc "không cross-fade, máy đi trong cùng một thế giới". Người xem không thấy đồ thị nằm ở đâu so với căn nhà. Thời điểm thì đúng: rơi vào khoảng lặng 9,20–10,34. |
| 15,5 đổi tiêu đề c2→c3 | trong đồ thị | — | Hai tiêu đề **chồng lên nhau** trong khung 15,5 (cross-fade chữ). Trục thêm vạch 100 %, giữ nguyên thang, tốt. Đường lịch "about 8 years" được giữ lại làm mốc so sánh: có lý do, liền. |
| 22,866–23,866 pan cSched→cDef | lia trong đồ thị | "định nghĩa cần hai chồng" | **Liền** nhất trong cả đoạn: 23,0 thấy bó đường trượt sang trái, 23,5 là hai chồng. Nằm đúng khoảng lặng 23,06–23,86. Nhược điểm: lia ngay sau khi "slow cases" vừa hiện (mục 7). |
| 29,142–30,042 mode cDef→wHouse | đồ thị → thế giới | "bảo hiểm gắn với căn nhà" | **GÃY.** Khung 29,5 cho thấy cảnh thế giới mờ bên trái **cùng lúc** với đường 80 % của đồ thị kéo ngang qua: hai chế độ chồng hình lên nhau (cross-fade/wipe), không phải máy di chuyển. Lý do thì đúng, thời điểm nằm trong khoảng lặng 29,18–30,04. |

Tóm lại: lý do của cả 4 lần di chuyển đều đúng về nội dung và đều rơi vào khoảng lặng. Nhưng cả **2/2 lần đổi chế độ là fade**, nên lời hứa thiết kế lớn nhất ("một thế giới, hai chế độ camera") chưa được thực hiện trên màn hình.

## 3. Nhịp

**Chỗ chùng** (hình đứng yên trong khi lời chạy):
- 3,5–5,0: ảnh rộng đứng yên, cộng thêm khoảng **lặng 1,2 s (2,88–4,08)** ngay giây thứ 3. Đây là chỗ chết đúng trong cửa sổ móc người xem.
- 18,5–21,0: bó đường đứng yên ~2,5 s trong lúc đọc "so you'll see how long it took on paper". Gần ngưỡng 3 s, và tick vẫn kêu đều làm lộ sự đứng yên.
- 26,0–28,5: hai chồng đứng yên ~2,5 s ("of the home's value by a national"). Gần ngưỡng.
- 32,0–33,5+: đứng yên ~2 s sau lời cuối. Cold open không kết bằng một nhát cắt hay một nốt chốt.

**Chỗ dồn/rối:**
- 21,5–23,0: "typical" (21,5), "slow cases" (22,5), rồi lia đi (22,87). Đường chậm — chi tiết đắt nhất của đoạn — chỉ ở trên màn ≤ 0,6–1 s.
- 18,5: "núi" ~307 đường vượt quá vạch 100 % mà không có nhãn trục. Ở 540p nó đọc như nhiễu, chưa đọc ra là "nhiều kịch bản". Ý "LTV > 100 % (âm vốn)" chưa được giải thích nên gây rối.

**5 s đầu có móc không? Yếu.**
- Câu mở "You've saved ten percent…" là một tiền đề, chưa phải câu hỏi hay xung đột.
- Hình là một diorama tối, vật nhỏ, ít tương phản, chuyển động duy nhất là một lần lùi máy.
- Câu hỏi thật ("buy now… or keep renting") tới lúc 4,1 s, sau khoảng lặng.
- Cú móc mạnh nhất ("you can't even ask to cancel it for about **eight years**") mãi tới **13,5 s** mới có.

So với Vox/WSJ, khoảng 0–5 s này chưa tạo được câu hỏi. Mặt tốt: giọng vào ngay khung 0, không có intro rỗng.

## 4. Lớp bắt buộc

- **Nguồn** "Source: FHFA · Freddie Mac via FRED": góc trên trái từ 10,5 tới hết, không cắt mép (~5 % lề).
  - Ở **32,0–33,5 nhãn "insurance still on" CHỒNG lên dòng nguồn**: hai dòng chữ đè nhau, không đọc được cả hai. Đây là lỗi chữ chồng rõ nhất.
  - Nguồn vẫn nằm trên cảnh WORLD (30,0–33,5). Chấp nhận được với một lớp bắt buộc, nhưng nên tách khỏi vùng nhãn.
- **"US only · history, not a forecast"**: góc dưới trái từ 15,5–16,0 (đúng lúc bắt đầu dữ liệu lịch sử). Không đè hình, không cắt mép.
- **ILLUSTRATIVE**: không thấy nhãn nào, trong khi hai chỗ cần có:
  - c2 "on the schedule": đường lịch trả nợ cho một khoản vay giả định. Không ghi lãi suất hay kỳ hạn, nên "about 8 years" không kiểm chứng được.
  - c0/c1: chồng tiền tượng trưng.
- **Đọc trên điện thoại**: chữ nhãn và lớp bắt buộc cao khoảng 3 % chiều cao khung (ước lượng từ khung thu nhỏ). Đọc được nhưng sát ngưỡng trên màn 6".
  - Nhãn trục "100 %/90 %/80 %" và số năm còn nhỏ hơn.
  - Tiêu đề c3 ("loan + home value by a national index · one line per purchase month, 1991–2016") quá dài, quá nhỏ.
- **Chữ chồng khác:**
  - 15,5: hai tiêu đề đè nhau (chuyển tiếp).
  - 14,0–22,5: "about 8 years" sát/chạm dãy số trục x quanh "6"–"8".
  - 22,5: nhãn "slow cases" nằm đè lên đỉnh đường vàng.
  - 18,5–22,5: đỉnh bó đường lên sát dòng tiêu đề.

## 5. Âm

- **Lời luôn rõ**: giọng −7…−12 dBFS, nhạc thường −35…−45, nên tách ≥ 20 dB. Ở 10–14 s (nhạc + data + sfx dâng lên ~−25…−30) vẫn còn ~15 dB. Phổ không thấy che formant. Đạt.
- **Nhạc theo căng–chùng**: nhạc gần như vắng 0–1,5 s, dâng dần, cao nhất quanh 10–15 s và 18–22 s, nhả từ ~29 s, tắt sau "removed" (31,8). Hướng đi khớp bản đồ căng 0,3→0,65→0,35. Ý dừng nhạc đúng từ "removed" là một nhát đúng kiểu Vox.
- **Kết thúc**: sau 32,2 chỉ còn room tone (−55…−60) trên ảnh đứng yên ~2 s. Không có nốt chốt, không cắt vào tiêu đề. Cold open "xì hơi" thay vì treo câu hỏi.
- **Âm dữ liệu**: 11 nốt 10,6–22,3 có mặt (lớp đỏ). Ở c2, nốt đi theo đường là hợp lý. Ở c3 thì sai: chuỗi tick đều 2,15 Hz không ăn với hình (bó bung một lần ở ~18,3, sau đó đứng yên), nghe như máy đếm nhịp chứ không phải dữ liệu.
- **Hiệu ứng thừa/khó chịu:**
  - "land" 10,10 là đỉnh sfx to nhất (~−21 dBFS), ngay trước giọng 10,34, hơi giật.
  - Chime 13,75 và 26,05 có hoạ âm sáng tới ~7 kHz (thấy rõ trên phổ), chói nhẹ trên loa điện thoại, và chime 13,75 đè ngay lên từ "eight".
  - 11 tick ở c3 là thừa.
  - whoosh_soft 2,17 nằm dưới lời, vô hại nhưng không cần.

## 6. 3D: làm rõ ý hay trang trí

- **Làm rõ:**
  - c4: hai chồng đặt cạnh nhau, chính diện. Tỉ lệ chiều cao đúng dữ liệu (đo trên khung: 55/61 ≈ 0,90 ở 24,0; 55/68 ≈ 0,81 ở 26,0).
  - c2: đường xuống chậm tới vạch 80 % ở ~8 năm, rất rõ.
- **Trang trí / làm sai tỉ lệ:**
  - c0: chồng 10 % ở **tiền cảnh** nên phối cảnh phóng to nó. Nó lại **nằm ngang**, còn chồng giá nhà dựng đứng. Người xem không thể ước "10 % của giá nhà" bằng mắt.
  - Chồng giá nhà không mờ, nên cũng không đọc ra "phần thiếu".
  - c1: chồng 20 % (gấp đôi) đúng về số lượng, nhưng vạch đích quá mờ.
- **90 % → 80 %:**
  - c2: trục cắt từ ~75 % (có nhãn 80/90 %). Chấp nhận được theo chuẩn WSJ.
  - c3: thang kéo lên trên 100 % mà không có nhãn phía trên, nên đỉnh "núi" không đọc được giá trị.
  - c4: chuyển động 90→80 gần như vô hình (+7 px trên cột giá trị), toàn bộ ý nằm ở con số.
- **c5**: 3D không chở được ý "vay đã thấp mà khiên vẫn còn": không có chồng vay. Khiên — vật thể then chốt — chỉ cỡ ~20 px trên 540p, trên điện thoại khó nhận ra là cái khiên.
- Thế giới tối, vật nhỏ, chiếm < ½ khung. Không gian 3D chưa được dùng (máy chỉ lùi một lần). So với 3Blue1Brown, chuyển động ở đây chưa "mang nghĩa" trừ c2 và pan c3→c4.

## 7. Chấm điểm (1–5, so với Vox / 3Blue1Brown / WSJ)

| Tiêu chí | Điểm | Lý do ngắn |
|---|---|---|
| Hình mang nghĩa | **3** | c2 và c4 mạch lạc. Thế giới c0/c1/c5 tỉ lệ không đọc được, khiên quá nhỏ, c5 thiếu hình "vay đã thấp", c3 bó đường thành nhiễu. |
| Liền mạch hình–lời–âm | **2** | 8/10 mốc trong sai số, nhưng bộ đếm 80 % sớm ≥ 0,55 s, chime 13,75 trễ ≥ 0,25 s so với chỗ chạm vạch, tick c3 kêu trên ảnh đứng. Cả hai lần đổi chế độ là fade/chồng hình, trái thiết kế. |
| Nhịp | **2** | 5 s đầu không móc (lặng 1,2 s ở giây 3, cú móc 8 năm ở 13,5 s). Ba khoảng đứng ~2,5 s. "slow cases" bị lia đi sau < 1 s. Kết thúc là một hình đứng không chốt. |
| Âm | **3** | Lời rõ, nhạc theo căng–chùng và dừng đúng "removed". Âm dữ liệu c3 lệch hình, chime chói, land 10,1 hơi to, kết thúc rỗng. |

### Năm sửa quan trọng nhất (xếp theo ảnh hưởng tới điểm)

1. **9,0–10,1 và 29,1–30,0: bỏ fade, làm máy đi thật.** Đồ thị phải là một mặt phẳng trong cùng thế giới (ví dụ máy bay lên/quay chính diện vào mặt tường cạnh nhà), không dip-to-black. Ở 29,5 không được có đường 80 % đè lên cảnh nhà. Tác động: liền mạch +1.
2. **0–5 s: dựng lại cú móc.**
   - Cắt khoảng lặng 2,88–4,08 xuống ≤ 0,4 s.
   - Cho câu hỏi "buy now… or keep renting" hoặc một câu treo về "8 năm" lên trước.
   - Khung mở gần hơn, sáng hơn, tách rõ nhân vật.
   - Làm chồng giá nhà mờ thật, và đặt chồng 10 % **dựng đứng cạnh, cùng mặt phẳng sâu** với chồng giá nhà để mắt so được 1/10.

   Tác động: nhịp và hình mang nghĩa.
3. **24,0–26,1: neo bộ đếm 90→80 % vào từ "eighty".** Đếm từ ~"loan" @25,5 và chạm 80 % đúng 26,05 cùng chime. Cho cột vay/giá trị chuyển động đủ lớn để thấy. Đồng thời đặt chime 13,75 đúng khung đường chạm vạch, hoặc làm đường chạm muộn hơn ~0,25 s.
4. **15,7–23,0 (c3):**
   - Cho bó đường hiện thật sự dần dần, từng nhóm theo năm mua, khớp với tick (hoặc bỏ tick đều, chỉ giữ nốt khi có nhóm mới).
   - Ghi nhãn vùng > 100 % hoặc cắt thang.
   - Rút tiêu đề.
   - Giữ "slow cases" trên màn ≥ 1,5 s trước khi lia: dời pan sang sau 23,5, hoặc đưa "slow" sớm hơn trong lời.
5. **30,0–34,0 (c5) và lớp chữ:**
   - Thêm chồng vay thấp cạnh nhà để hình nói được "đã thấp mà khiên vẫn còn".
   - Phóng to khiên (máy đẩy vào mái lúc "insurance").
   - Dời "insurance still on" khỏi dòng nguồn (đang chồng chữ ở 32,0–33,5).
   - Thêm nhãn ILLUSTRATIVE + giả định (lãi suất, kỳ hạn) cho đường lịch c2.
   - Kết bằng một nốt chốt hoặc nhát cắt thay vì 2 s room tone.
