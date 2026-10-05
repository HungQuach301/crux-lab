# C2 — Ý đồ kiểm mù bản chép lời (ghi TRƯỚC khi chạy, commit trước; không sửa sau khi thấy kết quả)

Ngày 2026-10-04. Bản 2 — sửa theo REVIEWER **trước khi chạy** (1 CHẶN, 6 CHÍNH, 3 THAM KHẢO). Cổng **TỰ ĐỘNG** (`quality-framework.md` v2 §4 C2). Giao thức §5: người đọc agent MỚI (sonnet), một file hex (`packets.py deal`); người chấm agent độc lập mù tập (`packets.py packet`), khoá nhãn commit trước khi chấm. Nguyên văn: `gates/C2-blind.md`.

## (a) Kiểm máy — `story/check_script.py`
Claim 100% có trong `numbers.md`; câu có số phải có claim; S10 = 0 (regex ADVICE/FORECAST/FOUR/WE_BAD của `checks/py/r_content.py`); có "US only" và "history, not a forecast" trong lời; luật ASR (`episode.md` §3.1: không dải năm gạch nối kể cả "—" và "1950s–1980s", không minus/số âm, không ký hiệu % ± → × $ ~ ≈ < > / hay "2x" trong lời); câu có số **bằng chữ** (twenty, half, percent…) cũng phải có claim; chữ trong ngoặc kép ở ghi chú hình: có số thì phải có claim, và chạy S10; dòng giống câu kịch bản mà sai định dạng → trượt. **Luật tập (chặn):** câu giả định (`ctx_hypothetical`) nằm ở cold open S01 và đứng trước mọi claim kết quả lịch sử; cảnh nêu tỉ lệ toàn kỳ (`share_tbills_above_double_pct`) phải nêu cả hai thời kỳ (1950–1989, từ 1990). Cảnh báo: 3.72% và 3.53% cùng cảnh; 17 tháng thật mà cảnh thiếu tỉ lệ toàn kỳ. Ngưỡng: đạt hết.

## (b) Kiểm mù lời
**Mẫu ứng viên:** lời thuần của `story/script.md` (cold open mặc định), bỏ ID, claim, ghi chú hình, thẻ cảm xúc; giữ ranh giới cảnh dạng dòng trống. SHA-256 file mẫu ghi vào `review-c2/` khi chia.
**Đối chứng yếu:** `archive/ep001-v1/script-m1b.md` chuyển thành lời thuần (chủ dự án chấm "chưa có kịch bản", G-009) — 3 người đọc vai của chính nó ("an American homeowner with a mortgage who is wondering whether to refinance"). Chỉ để biết câu hỏi 3–4 phân biệt được; không tính vào cổng. **Phân biệt được** khi ≥ 2/3 người đọc đối chứng nêu một chỗ mất chú ý hoặc khó hiểu cụ thể **và** tỉ lệ người đọc ứng viên nêu chỗ mất chú ý thấp hơn đối chứng; không thì issue C2 ghi "bộ đo câu 3–4 không phân biệt được".
**Người đọc ứng viên:** 5 vai đích (T) + 1 phổ thông (G), đủ 6, không dừng sớm.
- T: "You are an American in your 40s with savings you will not need for about 20 years; right now the money sits in a bank account or short-term Treasury bills."
- G: không vai ("Read it once, as an ordinary YouTube viewer").

**Câu hỏi cố định (tiếng Anh):**
1. Summarize the video in 3–4 sentences: who is it about, what decision, and how it unfolds.
2. What is the video's answer to its main question? Be specific.
3. Quote any sentence or passage that confused you, and say why (or "nothing").
4. Quote, word for word, the place where your attention dropped most, if anywhere, and say why (or "nowhere").
5. Does the video tell you which option to pick, or predict what interest rates will do? Yes or no, and why.
6. What advice, if any, would a viewer take from this?

**Chấm (người chấm độc lập):**
- Ý (Q) câu hỏi: lựa chọn giữa trái phiếu tiết kiệm (EE) bảo đảm gấp đôi sau 20 năm và lăn T-bill cho tiền để yên ~20 năm. Ý (A1) đáp án theo thời kỳ: kết quả tuỳ thời kỳ — lăn T-bill thường vượt gấp đôi ở các lần bắt đầu 1950–1989 nhưng gần như không bao giờ từ 1990. Ý (A2) ít nhất một trong: toàn kỳ khoảng một nửa; gấp đôi không phải lúc nào cũng giữ sức mua; 17 tháng có bảo đảm thật (mẫu ngắn) không vượt gấp đôi. Đủ Q + A1 + A2, **và không khẳng định bảo đảm gấp đôi đã thật sự có cho các năm trước 2005** (ví dụ "savings bonds beat T-bills since 1990" như sự thật) → **1**; Q + một trong A1/A2 → 0,5; còn lại → 0.
- `advice: true` khi câu 5 "yes" vì tin video chỉ định lựa chọn hay dự báo lãi, **hoặc** câu 6 nêu bất kỳ lời khuyên hành động nào, **kể cả lời khuyên có điều kiện** ("if you expect rates to fall, the bond…") (buy, hold, lock in, avoid, "bonds are safer", "use the bond as a hedge"…). Câu 6 "không có lời khuyên / tuỳ người xem" → không tính.
- Tín hiệu báo cáo (không làm cổng): `hyp` — người đọc nêu rằng bảo đảm được áp cho các năm trước 2005 như giả định.
- Một người đọc **đúng** = điểm 1 và không có câu khuyên.

**Đoạn mất chú ý:** câu hỏi 4 yêu cầu trích **nguyên văn**. P gán mỗi trích dẫn vào cảnh `Sxx` bằng khớp mờ với `script.md` (chuỗi ≥ 5 từ liên tiếp trùng; máy, không đánh giá). Trích không gán được → **giao người chấm độc lập gán cảnh** (gói có bản lời chia cảnh S01…, không tên tập); không bỏ khỏi đếm.

## Ngưỡng (cổng)
(a) đạt hết · (b) **đúng ≥ 5/6**; **câu khuyên 0/6**; **không cảnh nào bị ≥ 4/6 người đọc cùng chỉ là chỗ mất chú ý**.

## Vòng và dự phòng (ghi trước)
Tối đa 2 vòng (vòng 2: người đọc mới, cùng câu hỏi, cùng rubric). Cảnh mất chú ý → rút còn **1 câu lời + thẻ + mô tả** (mẫu đoạn phương pháp V7). Câu khuyên → WRITER thêm/siết câu đối trọng ở chỗ người đọc rút lời khuyên. Vẫn trượt sau vòng 2 → giữ bản điểm cao nhất, ghi rủi ro vào gói C3. Qua → issue `[Cổng C2 · tự động] Tập 3 — qua` ≤ 5 dòng, không chờ.
