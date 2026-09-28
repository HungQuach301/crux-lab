# Tập 1 — CRITIC vòng 1 (story: treatment, beats, cold open A/B)

Người chấm: CRITIC (độc lập, chỉ đọc và chấm). Ngày: 2026-09-28.
Đã đọc: `taste-ledger.md` (G-007, G-008, G-009), `checks/RUBRIC.md` (H1, H3, H4), `genre-spec/data-explainer.md` §2–§3, `CHARTER.md` §5, `story/{treatment,beats,cold-open,context}.md`, `numbers.md`, `model/refi.py` (chỉ để kiểm nghĩa hai cách tính hoà vốn).
Không đọc: `script/`, `review-m1*/`, `out/script-draft.json`.

Ghi chú: đây là bản giấy, chưa có hình hay giọng, nên H1 chấm theo ý đồ hình ghi trong beat. H4 ở cột cold open chấm ở phạm vi cold open: cái giá đã cụ thể chưa.

---

## 1. Bảng điểm

| Câu | Treatment + beats | CO-A | CO-B |
|---|---|---|---|
| H1 (cold open, vòng mở) | **3** | **3** | **3** |
| H3 (cấu trúc hồi) | **4** | **3** | **4** |
| H4 (cái giá cụ thể) | **4** | **2** | **2** |
| G-007 (một người, một khoảnh khắc, liên quan đến tôi) | **4** | **4** | **3** |
| G-008 (số gắn với hoàn cảnh) | **3** | **4** | **2** |
| G-009 (câu chuyện liền mạch) | **3** | **4** | **2** |
| **Trung bình** | 3.50 | 3.33 | 2.67 |

**Điểm thấp nhất: 2** (CO-A H4; CO-B H4, G-008, G-009). Chưa đạt ngưỡng CHARTER §5: trung bình ≥ 4, không câu nào dưới 3.

So với bản M1b: bộ khung đã đúng trình tự bối cảnh → nhân vật → vấn đề → hành trình → đáp án, và đã có bước ngoặt thật (dư nợ). Phần còn tệ nằm ở hai chỗ. Hồi 1 kể lại bối cảnh hai lần. Hồi 3 lại trượt về kiểu liệt kê số.

### Bằng chứng cho từng điểm

**Treatment + beats**
- H1 = 3. Vòng mở tốt, đóng lại bằng cùng hình ở B23 ("thư đề nghị trên laptop của Nora, dòng 'new rate' giờ có thước bên cạnh") và cùng chữ. Nhưng beat tự ghi "COLD OPEN (≤ 0:25", vượt trần DX-S1 ≤ 15 s. Câu hỏi mở cũng không nói mốc thời gian (3 năm), trong khi đáp án "nửa điểm" chỉ đúng với mốc đó.
- H3 = 4. Hồi 1 có ngoặt: "The division looks airtight. It is missing one line." Hồi 2 có ngoặt, cao trào và payoff: B11 dư nợ → B14 "không bao giờ [be_bal_025]" → B16 "nửa điểm". Trừ một điểm vì hai lẽ. Hồi 3 có câu hỏi ("với người khác thì sao") nhưng bước ngoặt yếu: Walt và Anjali chỉ là hai phép tính nữa. Và B22 (lịch sử) chen vào sau khi bộ ba đã xong, làm loãng payoff.
- H4 = 4. Cái giá gọi bằng tháng và đô la ở mọi điểm quyết định: "Đến tháng 24, dư nợ khoản mới cao hơn khoản cũ $1,133 [gap24]", "anh lỗ $1,777 [net36_small]". Trừ một điểm vì lời chưa bao giờ nói "nominal dollars" (DX-H3), và B22 quay lại nói trừu tượng ("13 đợt… 3 đợt").
- G-007 = 4. "Nếu người xem là một trong số họ, câu chuyện này là của họ." Nhưng B5 hứa "giới thiệu nhân vật bằng đời thật" mà chỉ đưa khoản vay và lãi suất. Nora chưa có một chi tiết đời thường nào.
- G-008 = 3. Hồi 2 bám chặt Nora. Nhưng B3 "2.65% [low]", B6 "6.30% [r_year_ago]; 7.03% [r_today]" và B22 "13 đợt [n_eps]" là số đứng một mình: không gắn vào quyết định của ai. Riêng B22 còn dùng khoản vay $300,000 giả định mà người xem chưa từng gặp.
- G-009 = 3. Có chuyển ý ở mọi beat, tốt. Nhưng trình tự thực tế là bối cảnh (CO) → Nora (CO) → bối cảnh lại (B3–B4) → Nora lại (B5) → bối cảnh lại (B6). Hồi 3 cụt lủn đúng kiểu chủ dự án chê: "Anjali thì ngược lại: khoản $655,000, phí $5,514, mỗi tháng bớt $387, hoà vốn ở tháng 18; cô chỉ cần 0.32 điểm". Câu mở treatment còn sai thời gian: "Ba năm trước… Tháng 1/2021".

**CO-A**
- H1 = 3. Theo beat, hình đi trước lời (đường lãi leo lên đỉnh). Câu hỏi cụ thể: "How far does a rate have to fall before that bill pays itself back?", và được trả lời ở B23. Nhưng dài 69 từ, khoảng 26–28 s, gần gấp đôi trần 15 s.
- H3 = 3. Câu hỏi của CO khớp câu hỏi cả phim, nhưng không dựng câu hỏi hồi 1 (quy tắc một điểm đối đầu phép chia).
- H4 = 2. "a bill for loan costs, due up front": không có số tiền, không có mốc tháng.
- G-007 = 4. Có người, có khoảnh khắc: "Now a refinance offer is open on her laptop". Có cả lý do để người xem nhận ra mình: "Families still needed homes, so many of them signed anyway."
- G-008 = 4. Con số duy nhất ("highest level since 2000") được nối thẳng vào quyết định ký hợp đồng của các gia đình.
- G-009 = 4. Năm câu đi đúng trình tự bối cảnh → người → vấn đề → câu hỏi, có chuyển ý ("so many of them signed anyway", "Nora was one of them").

**CO-B**
- H1 = 3. Câu hỏi sắc hơn A ("Is half a point enough?"), nhưng "enough" cho việc gì thì chưa nói (3 năm? 7 năm?). Cũng dài 70 từ, khoảng 26–28 s.
- H3 = 4. Dựng đúng câu hỏi hồi 1: "The rule of thumb she keeps hearing says wait for a full point."
- H4 = 2. "cuts her rate by just over half a point": chỉ có mức giảm, không có cái giá.
- G-007 = 3. Nora xuất hiện ở câu 4, không có khoảnh khắc nhìn thấy được (không laptop, không thư).
- G-008 = 2. Hai câu đầu là đọc số thuần: "In the week ending September 24, 2026, the average US mortgage rate was back above seven percent. A year earlier, it had been 6.30."
- G-009 = 2. Logic đứt đoạn. Người xem vừa nghe lãi *tăng* từ 6.30 lên trên 7, rồi lại nghe "Her refinance offer cuts her rate". Lãi cũ 7.62% của Nora chưa được nói, nên "cắt" không có nghĩa. Câu "those weeks mattered" mơ hồ.

---

## 2. Ba người xem

**(a) Người Mỹ đang trả góp nhà, không rành tài chính.**
"CO-A chạm tôi ngay: tôi cũng vừa nhận email mời refinance. Nhưng sau đó phim lại kể lãi 2021, rồi đỉnh 2023, rồi lãi năm qua. Tôi đã nghe 'rates are high' ở mở đầu rồi, tới phút thứ hai vẫn chưa thấy tiền, nên muốn tua. 'Half a point', 'a full point': tôi tưởng là *points* ngân hàng bắt mua (discount points), không phải điểm phần trăm lãi. Đoạn hai đường dư nợ là lúc tôi hiểu ra điều mới, nhưng 'balance gap' phải nói bằng tiếng thường: 'khoản mới bắt bạn nợ lại từ đầu 30 năm'."

**(b) Biên tập viên phim tài liệu.**
"Xương sống tốt: có vật lặp lại (đồng hồ, thước 'rate drop'), dựng ở B2 và trả ở B16, B21, B23. Vòng mở đóng bằng cùng hình. Nhưng cold open 25 s là dài. Hồi 1 có bốn beat liền nhau dùng cùng một hình đường lãi (B1, B3, B4, B6), nhịp chết trước khi có tiền ở B7. Nora là một cái marker tròn, chưa phải một người: cho tôi một chi tiết (căn nhà, lý do mua tháng 10/2023). B22 là đoạn lạc đề ngay sau cao trào hồi 3: cắt, hoặc chuyển vào thẻ phương pháp."

**(c) Chuyên gia tín dụng nhà ở.**
"Sửa conforming/jumbo là đúng: $655,000 dưới hạn mức 2023 $726,200 [cll2023], nên dùng lãi PMMS được. Nhưng lời chưa bao giờ nói 'still under the conforming limit', và chữ 'large' dễ bị hiểu là jumbo. Có ba chỗ về PMMS. 'The average US mortgage rate' là nói quá rộng: đó là trung bình theo tuần của Freddie Mac cho vay 30 năm lãi cố định, loại conventional, dựa trên hồ sơ gửi Freddie Mac. PMMS chủ yếu là hồ sơ vay mua nhà, trong khi lãi vay lại thường khác. PMMS cũng giả định có trả points. `total_loan_costs` là mục D của Closing Disclosure: A (phí khởi tạo, **gồm cả discount points**) + B + C, chưa trừ lender credits (mục J), không gồm Other Costs (thuế, phí đăng ký, trả trước, ký quỹ). Beat B8 nói đúng phần 'không gồm', nhưng bỏ qua chuyện 'gồm points', tức là một phần hoá đơn đã mua lãi thấp hơn. Bộ lọc `total_loan_costs > 0` cũng loại các khoản no-closing-cost. Hai cách tính hoà vốn thì đúng: phép chia (phí ÷ số tiền trả tháng giảm được) so với cách tính dư nợ (tiết kiệm cộng dồn + [dư nợ cũ − dư nợ mới] ≥ phí), đúng `model/refi.py`. Nhưng 'never' ở 0.25 điểm thực ra là 'không trước kỳ trả cuối của khoản cũ'. Và phim không nhắc lựa chọn vay lại với kỳ hạn ngắn hơn, cũng không nhắc cộng phí vào khoản vay. Cuối cùng, $375,000 và $655,000 là số tiền của *khoản vay lại năm 2025* nhưng lại dùng làm khoản vay gốc năm 2023. Được, vì là ILLUSTRATIVE, nhưng phải nói ra."

---

## 3. Kiểm độ chính xác (số và nghĩa)

### 3a. Lỗi nghĩa (DX-H7)

1. **Walt "tức 3.4% khoản vay [share_small]" là sai nghĩa.** `share_small` là tỉ lệ phí trung vị của *cả nhóm* khoản < $150k. Phí của Walt chia khoản vay của Walt là $3,667 / $115,000 = 3.19%; chia dư nợ lúc vay lại còn khoảng 3.3%. Không phải 3.4%.
   - Sửa: "Loans this size typically pay about 3.4% of the loan in loan costs [share_small]." Nói ở cấp nhóm, không gán cho Walt.
2. **"Ba năm trước, người Mỹ mua nhà trong một thế giới lãi suất rất khác. Tháng 1/2021…"** sai thời gian. Ba năm trước là 2023, tức lãi *cao*; 2021 là gần 6 năm trước.
3. **"Rồi lãi leo lên không ngừng"** sai. Chuỗi 2022–2023 có những đợt giảm. Nên viết "climbed for most of the next three years" (không số), hoặc bỏ.
4. **"Tháng 1/2021, lãi… chỉ 2.65%"**: đây là mức của *một tuần* (tuần kết thúc January 7, 2021 [low_date]), không phải của tháng.
5. **CO-A và CO-B nói "the average US mortgage rate"**: nên nói "the average 30-year fixed rate", vì PMMS chỉ đo loại vay đó.
6. **"never [be_bal_025]"**: theo model nghĩa là không hoà vốn trước kỳ trả cuối của khoản cũ. Lời nên nói "not before her old loan would have been paid off", hoặc ít nhất ghi trong thẻ phương pháp.
7. **"cut_today" 0.59** so trung bình *tháng* 10/2023 với một *tuần* 2026. Được, nhưng thẻ phương pháp phải ghi.
8. **"Six extra months" (B13)** là số tự suy (30 − 24), không có claim.
9. **Chữ "point"** trong ngành vay nhà trước hết nghĩa là discount point. Lần đầu phải nói "percentage point", các lần sau mới rút gọn.

### 3b. Số thiếu claim ID

| Chỗ | Chữ | Cần |
|---|---|---|
| treatment ¶1 | "mức thấp nhất từ 1971" | [y1971] |
| treatment ¶4 | "khoản mới bắt đầu lại 30 năm" | [term30] |
| treatment ¶4 | "một phần tư điểm", "nửa điểm" | [s025], [s05] |
| treatment ¶4, ¶5; B2; B19 | "trong ba năm", "sau ba năm", "within three years" | [hold36] / [y3] |
| treatment ¶5 | "Cùng mức giảm như Nora" | [cut_today] |
| treatment ¶6 | "giảm ít nhất một điểm", "giảm thêm một điểm" | [s10] |
| treatment ¶7; B24 | "ở bảy năm" | [y7] |
| B13 | "Six extra months" | xin DATA cấp claim, hoặc bỏ |
| CO-A | "many of them signed anyway" | không bắt buộc (không có số); nếu muốn cụ thể thì dùng [purch23_n] |

### 3c. Đối chiếu với numbers.md

Mọi số có claim ID đều khớp numbers.md: 2.65, 7.79, 2000, 30%, 881,835, $375,000, 7.62%, 6.30%, 7.03%, 0.59, $221, $5,124, $3,443, $8,270, 24, 30, 35, $1,133, 38, never, 36, 18, 0.5, $115,000, $3,667, 3.4%, $68, 75, −$1,777, 1.12, $655,000, $5,514, 0.8%, $387, 18, 0.32, 13, 3, $1,039, $8,093, 4.38, 488,241, 6.00%, January 16, 2025.

Chỗ không khớp duy nhất là **nghĩa** của 3.4% (mục 3a.1). Dấu: `net36_small` là lỗ, và treatment nói "lỗ", đúng.

### 3d. Lỗi nhân dạng (DX-I1, DX-I2, DX-I4)

- **B2 "we start with how everyone got here"**: "we" ở đây gộp cả người xem. Sửa thành "The answer starts with how rates got here."
- **B6 "We cannot tell her where the line goes next. We can tell her what a given drop is worth."**: "we" là người phân tích, đúng luật. Câu này còn là câu chống dự báo tốt; giữ.
- **B22 "3 đợt lãi còn giảm thêm một điểm trước khi kịp hoà vốn"** dễ bị nghe thành "cứ chờ đi" (khuyên ngầm hoặc dự báo ngầm). Phải đóng khung: "In 3 of 13, a second drop came before the first refinance had paid back. That is history, not a forecast." Không kèm lời bình.
- **"US only" và "history, not a forecast"**: có ở B4 và B3, và ở treatment ¶1. Đạt DX-I2. Cold open không có, nhưng không bắt buộc.
- **Không thấy câu khuyên hay câu mệnh lệnh.** B24 dùng câu hỏi ("How long do you picture yourself there?"), đúng. "Để hoà vốn…, anh cần…" là câu mô tả, được.
- **"the way you watch a stock you own" (B5)**: không phạm luật, nhưng giả định người xem có cổ phiếu. Nên đổi thành "the way you check a price you care about".

---

## 4. Ba điểm yếu nhất

1. **Cold open dài gần gấp đôi trần**, và câu hỏi thiếu mốc thời gian. A và B đều 69–70 từ, khoảng 26–28 s, so với trần DX-S1 ≤ 15 s. Câu hỏi "how far must it fall" chưa nói "để hoà vốn trong bao lâu", nên đáp án "nửa điểm" ở B23 phải kèm điều kiện mà người xem chưa được hứa.
2. **Hồi 1 kể bối cảnh hai lần, trễ tiền.** CO đã nói đỉnh 2023 và Nora. Rồi B3 (2021) → B4 (đỉnh 2023, lại) → B5 (Nora, lại) → B6 (lãi năm qua) dùng bốn beat đường lãi liên tiếp. Số tiền đầu tiên của Nora ($221) đến ở B7, khoảng 2:00. Đây là G-009 "đưa nhân vật khi chưa có bối cảnh" bị lật ngược: bối cảnh cứ quay lại sau khi đã có nhân vật.
3. **Hồi 3 là danh sách số, không phải chuyện.** Walt và Anjali mỗi người 4 số trong 2 beat, không có đời sống, không có khoảnh khắc. B22 (13 đợt, khoản $300k giả định) là lạc đề sau cao trào. Kèm lỗi nghĩa 3.4%. Đây đúng là "thông tin cụt lủn" mà chủ dự án chê ở M1b.

## 5. Chỗ người xem bỏ đi

| Beat | Vì sao |
|---|---|
| **B3–B4** (~0:45–1:20) | Vừa nghe "highest since 2000" ở CO, giờ lại xem đường lãi từ 1971 và đỉnh 2023 lần hai. Câu hỏi của B3 ("Sao lãi lại cao thế?") không bao giờ được trả lời. |
| **B6** (~1:35) | Lần thứ tư thấy đường lãi. Hai số (6.30, 7.03) không đổi gì cho Nora, vì cô chỉ cần mức 7.03 của đề nghị. |
| **B11** | "Hai đường dư nợ" là trừu tượng với người (a). Nếu không có một câu đời thường ("the new loan starts the 30-year clock over"), người xem sẽ bỏ đúng ở bước ngoặt hay nhất. |
| **B22** | Đổi từ ba người sang 13 dải lịch sử, sau khi câu hỏi hồi 3 đã có đáp án. Người xem cảm thấy phim đã xong. |

## 6. Chỗ thiếu bối cảnh

- **"Refinance" là gì**: chưa có câu nào nói "a new loan pays off the old one, at today's rate, and it has fees".
- **Vì sao Nora được 7.03%**: phải nói đề nghị lấy theo lãi trung bình tuần kết thúc September 24, 2026, và lãi cũ của cô là 7.62%. CO-B mâu thuẫn chính vì thiếu câu này.
- **Vì sao phí gần như không đổi theo quy mô** (thẩm định, bảo hiểm quyền sở hữu, phí khởi tạo cố định): context.md có ý này, nhưng beat không giải thích cơ chế. Thiếu nó, Walt chỉ là một con số buồn.
- **Nora, Walt, Anjali "khoản vay và phí là trung vị thật của gần nửa triệu khoản vay lại năm 2025"**: chữ ILLUSTRATIVE và [n31] chưa vào lời. Đây là câu tạo lòng tin.
- **Anjali**: phải nói "still under the conforming limit" (một câu, không cần số). Cũng phải nói cô vay cùng tháng 10/2023, cùng mức giảm.
- **Giả định "phí trả tiền mặt, không cộng vào khoản vay"** và **"kỳ hạn mới 30 năm"**: có ở giới hạn B23, nhưng nên nói sớm, ở B8 hoặc B11, vì cả phép tính dựa vào hai giả định này.
- **"Nominal dollars"**: một lần trong lời hoặc trên thẻ.

## 7. Câu nghe như đọc số

- treatment ¶2: "6.30% một năm trước, rồi lại 7.03% trong tuần kết thúc 24/9/2026"
- treatment ¶5: "Anjali thì ngược lại: khoản $655,000, phí $5,514, mỗi tháng bớt $387, hoà vốn ở tháng 18; cô chỉ cần 0.32 điểm" (5 số một câu)
- treatment ¶5: "Walt vay $115,000, nhưng phí của anh vẫn $3,667, tức 3.4% khoản vay" (3 số một câu)
- treatment ¶1: "Tháng 1/2021, lãi vay 30 năm trung bình chỉ 2.65%, mức thấp nhất từ 1971"
- treatment ¶7: "Mức giảm cần thiết là 0.32, 0.5 hay 1.12 điểm tuỳ khoản vay" (được ở đáp án, nhưng cần gắn tên: "Anjali's line is a third of a point; Nora's, half; Walt's, more than one")
- CO-B: "A year earlier, it had been 6.30." (con số trần, không đơn vị, không người)
- B19: "lỗ $1,777; cần 1.12 điểm" (hai số quyết định trong một beat, không có khoảng thở giữa hai số)

---

## 8. Cold open và trần 15 s

- Trần DX-S1 là ≤ 15 s. Ở 150–160 wpm, 15 s tương đương 37–40 **từ nói**, chưa trừ 1–2 s hình đi trước lời. Như vậy lời nên ≤ 32–35 từ nói.
- CO-A có 69 từ viết, khoảng 26–28 s. CO-B có 70 từ, khoảng 26–28 s. Năm, ngày và số đọc thành nhiều từ ("twenty twenty-three"), nên thực tế còn dài hơn. **Cả hai trượt.**
- Không nên xin nới trần trước khi thử bản ngắn. Nếu chủ dự án hoặc K1 vẫn muốn 25 s thì phải sửa spec, không lách.

**Đề xuất: chọn A, rút gọn, và mượn câu hỏi của B vào hồi 1.** Khoảng 36 từ nói (14 s ở 155 wpm), cộng 1.5 s hình đi trước:

> October 2023. The average 30-year rate hit its highest since 2000 [oct2023][peak2023_since]. Nora signed anyway. Now a refinance offer sits on her laptop, bill due up front. How far must her rate fall before that bill pays itself back?

Bổ sung cho bản rút gọn:
- Cho hình mang số: nhãn "highest since 2000" trên đỉnh đường lãi, hoặc chuyển số này lên màn hình và bỏ khỏi lời. Hoá đơn **$5,124 [cost_median]** hiện trên màn hình laptop, không đọc. Như vậy H4 của CO có cái giá thật mà không thêm số vào lời.
- Mốc thời gian của câu hỏi ("within three years") để ở câu hứa B2: "By the end, you will see the exact drop that pays that bill back within three years [hold36], for three loan sizes." Không cần nhồi vào CO.
- Câu "Families still needed homes" bị cắt khỏi CO. Chuyển nó vào B4, nơi đặt lưới 10 nhà.

---

## 9. Chỉ dẫn sửa cho WRITER (theo thứ tự ưu tiên)

1. **Cold open**: dùng bản 36 từ ở mục 8. Bỏ CO-B, nhưng đưa câu "the rule of thumb… says wait for a full point" vào B9. Sửa đầu beats từ "≤ 0:25" thành "≤ 0:15".
2. **Gộp hồi 1, bỏ lặp bối cảnh.**
   - B3 và B4 thành **một** beat (~20 s): 2.65% tuần January 7, 2021 → 7.79% đỉnh → "3 in 10 home loans made in 2023 carried 7% or more [purch23_ge7]", kèm "history, not a forecast" và "US only". Bỏ câu hỏi "Sao lãi lại cao thế?", vì không trả lời được mà không dự báo hay suy đoán.
   - Bỏ B6 như một beat riêng. Đưa 7.03% [r_today] vào B7 thành lý do của đề nghị: "The offer is priced near the average for the week ending September 24, 2026: 7.03%. Her loan is at 7.62%." Nếu muốn giữ 6.30% thì chỉ để trên hình.
   - Mục tiêu: $221 đến trước 1:30.
3. **Cho Nora đời sống ở B5**: một chi tiết không số, ví dụ mua căn nhà đầu tiên tháng 10/2023 vì công việc mới. Ghi ILLUSTRATIVE trên màn hình cùng lúc. Nói một câu: "Her loan and her fees are the real 2025 medians from nearly half a million refinances [n31]."
4. **Định nghĩa từ, bằng lời thường**:
   - B7: "A refinance is a new loan that pays off the old one."
   - Lần đầu nói "percentage point", sau đó mới "point".
   - B11: "The new loan restarts the 30-year clock, so in the early years more of each payment goes to interest." Câu này phải đứng trước chữ "balance".
5. **Sửa lỗi nghĩa ở mục 3a**:
   - Câu 3.4% của Walt.
   - "Ba năm trước… 2021".
   - "leo lên không ngừng".
   - "average US mortgage rate" thành "average 30-year fixed rate".
   - "never" thành "not before the old loan would have been paid off".
   - Bỏ "Six extra months", hoặc xin DATA cấp claim.
6. **Viết lại hồi 3 thành chuyện, không phải bảng.**
   - Mỗi nhân vật một khoảnh khắc: Walt mở cùng loại thư, hoá đơn gần bằng của Nora.
   - Giải thích cơ chế phí gần như cố định.
   - Mỗi câu tối đa 1 số. Tách "lỗ $1,777" và "1.12" thành hai câu, có khoảng thở ≥ 1 s (DX-R3).
   - Anjali: "still under the conforming limit", "same month, same drop".
7. **B22**: hoặc chuyển sang thẻ phương pháp, hoặc đặt *trước* B23 với khung trung lập ở mục 3d, gắn vào Nora: "Nora's 30 months is long enough for rates to move again. In 3 of 13 past drops, they did." Không dùng khoản $300k mới trong lời.
8. **Gắn đủ claim ID** theo bảng 3b.
9. **Chuyên môn vào thẻ phương pháp B25**:
   - PMMS = trung bình tuần của Freddie Mac cho vay 30 năm cố định conventional, dựa trên hồ sơ; lãi của từng người khác.
   - `total_loan_costs` = mục D: gồm phí khởi tạo và discount points; chưa trừ lender credits; không gồm thuế, phí đăng ký, trả trước; bỏ các khoản phí bằng 0.
   - Khoản vay gốc lấy theo số tiền vay lại năm 2025 (ILLUSTRATIVE).
   - Tiền là danh nghĩa.
10. **B2**: "we start with how everyone got here" thành "The answer starts with how rates got here."

Mức cần đạt ở vòng 2: mọi ô ≥ 3, trung bình mỗi cột ≥ 4. Chấm lại trên bản có lời đọc đầy đủ (script) sau khi sửa.
