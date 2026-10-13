# REVIEWER C2 Tập 7 (headless Opus, khoá Console, $1,06; đầu bài briefs/reviewer-c2.md)

**Kết luận: ĐẠT có sửa.** Kịch bản đi được tới G1, nhưng `C2-blind.md` phải ghi lại cờ khuyên trước khi gửi gói, và cần sửa 6 lỗi CHÍNH bên dưới. Checker chạy lại cho exit 0. Số trong lời và chữ trên hình đều có claim đúng tuần và đúng thời kỳ (S03.1, S20.1, S29–S30, S33.3 đã đối chiếu với `numbers.md`).

**CHẶN (sửa gói, không phải sửa lời)**
- **C2-blind, cờ khuyên:** kết luận "mơ hồ rubric" không đứng vững. `c2/rubric.md` có trước kết quả (13:26:32, sớm hơn r1 lúc 13:26:53), giống hệt ở packet r1 và r2, và ghi rõ "trả theo tháng thay vì năm" là câu khuyên. Câu 6 ở r1 có 5/6 người nêu "monthly beats/cheaper than yearly" (trừ 4bba6150), r2 có 6/6. Vậy theo đúng rubric thì **cả hai vòng đều trượt ngưỡng khuyên 0/6**. Người chấm vòng 1 nới tay, rubric không mơ hồ. Ý đồ thì không bị sửa: `C2-intent.md` đã commit ở da54b61 và chưa đổi. Sửa: ghi vào gói G1 "câu khuyên trượt cả 2 vòng theo rubric ghi trước (r1 5/6 nếu chấm đúng rubric, r2 6/6); nguồn là S23–S24", rồi áp sửa S24.2 bên dưới. Hết 2 vòng nên bản sửa này **chưa kiểm mù**; G1 phải nói rõ điều đó.

**CHÍNH**
- **S24.2:** câu đối trọng yếu, người đọc rút ra "monthly beats yearly", và đó chính là nguồn cờ khuyên. Thay bằng: *"That isn't a verdict on paying yearly: the money stays in her account longer, and what it earns there isn't counted."*
- **S25.4–S25.5:** câu "has to clear it to come out ahead" overclaim. Nó bỏ qua rủi ro, thuế ở vế kia và thanh khoản (S31.3 tới muộn 6 cảnh). Hậu quả đã thấy: người đọc viết "with no risk" (r2 75d5e71f), "guaranteed" (r2 1f7eb3c5), "with certainty" (r1 beb52945). Thay S25.4: *"That rate is the bar any other use of that dollar gets measured against, before taxes."* Thay S25.5: *"Whether any investment clears it, once risk and taxes count, isn't tested here."* Ở B25 đổi "has to climb over the beam" thành "is held up against the beam".
- **S30.1, "And it was bigger":** câu này làm 12/12 người đọc khựng ở câu 3 của cả hai vòng. Thay bằng: *"And it left him more room: his required payment sat about $793 a month below the 15-year's."*
- **S15.3, câu dài ngay sau đỉnh** (25 từ, hai ý). Người đọc hỏi "not a mistake" từ đâu ra (r1 beb52945, r2 01da6d90 và afe74066). Thay bằng hai câu: *"That makes Tessa's fallback expensive by history."* và *"What a lower payment is worth in a bad month, this replay can't measure."*
- **S11–S18, S26–S27, số dày:** 3/6 người r2 mất chú ý ở S17. Đưa ngày và lãi theo thập kỷ lên hình, lời chỉ giữ số đô la:
  - S13.2 *"The smallest was $6,097."*
  - S14.1 *"The tallest was $29,502."*
  - S16.2 *"In the 1990s, the typical fallback cost $15,118."*
  - S17.1 *"In the 2000s, with lower rates, it cost about the same: $14,210."*
  - S18.1 *"In the 2010s, rates were far lower, yet the fallback cost more: $20,374."*
  - S26.2 *"Since 1991, it has stood as high as 9.25 percent."*
  - S27.1 *"And as low as 2.65 percent."*
  - S29.1 *"Leo, also illustrative, took a 30-year loan of the same size in January 2021, the lowest week, at 2.65 percent, and paid it like a 15-year too."*
- **Hồ sơ cầu (§7 mục 10):** chỉ vừa đủ 3/5. Q2 trả ở S21, Q3 ở S23–S24. Q1 ở S25 chỉ trả một nửa (có mốc, không có vế đầu tư; kiểm mù T 0/5 cả hai vòng). Q5 ở S22 trả lệch: câu hỏi là "lãi tháng sau", còn kịch bản trả lời "khoản trả", và không nhắc recast. Q4 không trả. Vì sát ngưỡng nên phải nêu tên ở G1. Nhịp điểm yếu đối thủ (S10.1, S31.3) và khoảng trống của video neo (S10.2–S10.3) đều ĐẠT, không nêu tên kênh. Sửa Q5, thêm sau S22.1: *"Each extra dollar does cut the next month's interest; the payment just stays fixed, so more of it goes to principal."*

**PHỤ**
- **S15.2 `{peak}`:** câu có **15 từ viết**, không phải 14 như `script.md` và `beats.md` ghi. Vẫn ĐẠT nhưng nằm đúng ngưỡng, phải nêu tên. Một ý một câu: ĐẠT.
- **Năm luật nhân vật:** (a) Tessa xuất hiện ở 0:00, đi qua phương pháp ở S10.4, câu kết S33.3 là của cô: ĐẠT. (b) M6 0 s: ĐẠT. (c) vật cụ thể là "the stack", có claim: ĐẠT. (e) câu kết quay về đúng câu hỏi S02.1: ĐẠT. Riêng S33.3 "Her answer:" bị 2 người đọc thấy lạ vì Tessa không chọn gì. Đề xuất: *"What she now knows: the 30-year paid in 15 is the 15-year plus a fallback, and this week, that fallback costs her $120 a month."*
- **S01.1:** "fallback" xuất hiện trước khi được định nghĩa (≥ 4 người đọc ở mỗi vòng). Chấp nhận được vì S02.1 giải thích ngay sau đó, nhưng cân nhắc thay bằng *"Keeping a lower mortgage payment for a bad month would cost Tessa $120 a month."*
- **M2 28,2 s** chỉ là số ước; bản đọc thử (mục d) phải xác nhận dưới 30 s. **Độ dài** ước 10:05, trục mốc giây 9:37: có thể rơi dưới 10 phút, tức ra ngoài dải hồ sơ (10–24 phút). Khi đó theo `format` và ghi một vế ở dòng Độ dài của G1.
- **Lệch sổ sách:** header `script.md` ghi 1273/1454 từ, checker hôm nay ra 1274/1452. `C2-blind.md` ghi MR2 "≈ 6:4x", script ghi 7:00. Tiêu đề `beats.md` vẫn là "C2 v1".
- **Thumbnail "$21,622":** cần kèm "this week's rates" hoặc chú trong mô tả.

**Ba móc (story §1 + M1–M6; cả ba ĐẠT M1–M6)**
1. **HB (đang dùng), giữ.** Nhân vật, cái được–mất (số hiện tại có claim) và vật trung tâm đều có trong 4 s đầu. Câu kết S33.3 trả lời đúng bằng chữ của HB.3. Yếu: "fallback" chưa định nghĩa ở 0 s.
2. **HA.** Câu hỏi của người xem ở 0 s, khớp từ khoá của video neo. Nhưng chưa có người và cái được–mất trước khoảng 12 s; phẳng.
3. **HC.** Mở bằng 7.40 % cạnh "obvious win", tức mời so với đầu tư đúng lúc tập đang trượt cờ khuyên. Tessa tới muộn nhất (khoảng 0:30), và "tested" dễ đọc thành "refuted".

REVIEWER tách được ba móc nên không cần so cặp.