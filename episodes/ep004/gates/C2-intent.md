# C2 — Ý đồ kiểm máy + kiểm mù lời (ghi TRƯỚC khi có kịch bản; không sửa sau khi thấy kết quả)

Ngày 2026-10-05. Cổng **TỰ ĐỘNG** (`quality-framework.md` §4 C2, §5). Số agent: **6 người đọc + 1 người chấm = 7** mỗi vòng.

## (a) Kiểm máy — `story/check_script.py` (viết trước kịch bản)
CHẶN: claim có trong `numbers.md`; câu có số (chữ số hay từ chỉ số) phải có claim; S10 = 0 (regex `checks/py/r_content.py`) trên lời và chữ trích trên hình; có "US only" và "history, not a forecast"; luật ASR (`episode.md` §3.1); **móc** (`story.md` §1): 5 s đầu có câu hỏi hoặc câu được–mất mang claim, lời hứa trước 0:30, không câu ràng buộc chen giữa câu hỏi và lời hứa — áp cho S01 của script **và** cho cả 3 phương án ở `hooks.md`. CẢNH BÁO (không chặn): mật độ số, câu ngưỡng thiếu "like/average", khuôn tỉ lệ ±5 điểm % (WRITER báo, P đối chiếu).

## (b) Kiểm mù lời
**Mẫu:** lời thuần của `story/script.md` (S01 = móc đã chọn), bỏ ID, claim, ghi chú hình, thẻ cảm xúc; ranh giới cảnh = dòng trống. Không đối chứng (lessons E12: đối chứng "hiểu" không phân biệt; F4: đối chứng phải cùng chủ đề — chỉ có ở hiệu chuẩn móc).
**Người đọc:** 5 vai đích (T) + 1 phổ thông (G), đủ 6, không dừng sớm.
- T: "You are an American in your late 50s or 60s, married, who bought your home around 2000 and has started thinking about selling it to downsize."
- G: "Read it once, as an ordinary YouTube viewer."

**Câu hỏi cố định (tiếng Anh):**
1. Summarize the video in 3–4 sentences: who is it about, what decision, and how it unfolds.
2. What is the video's answer to its main question? Be specific.
3. Quote any sentence or passage that confused you, and say why (or "nothing").
4. Quote, word for word, the place where your attention dropped most, if anywhere, and say why (or "nowhere").
5. Does the video tell you whether to sell or keep your home, or predict home prices or tax law? Yes or no, and why.
6. What advice, if any, would a viewer take from this?

**Chấm (người chấm độc lập, mù tập):**
- (Q) câu hỏi: lãi khi bán căn nhà mua năm 2000 có vượt giới hạn miễn thuế $500,000 (cặp vợ chồng), một giới hạn không đổi từ 1997, không.
- (A1) đáp án: có một **mức giá mua năm 2000 theo vùng** mà trên đó lãi của căn nhà tăng như trung bình vùng vượt giới hạn, và mức đó **thấp hơn người ta nghĩ / dưới $300,000 ở hầu hết các vùng được xét** (hoặc nêu đúng ít nhất hai ngưỡng vùng).
- (A2) ít nhất một: giới hạn 1997 theo giá hôm nay ≈ $1.05 triệu (không tăng theo lạm phát); ngưỡng chỉ là của căn nhà tăng như trung bình vùng (cải tạo, chi phí bán, căn nhà cụ thể khác); một căn nhà cụ thể ($200k/$300k minh hoạ) vượt giới hạn ở một thời điểm cụ thể.
- Đủ Q + A1 + A2 → 1; thiếu một → 0,5; ≤ một ý → 0. Khẳng định sai nghĩa (ví dụ "họ sẽ nợ thuế $X", "mọi người mua năm 2000 đều vượt") → 0.
- `advice: true` khi câu 5 "yes" vì tin video bảo bán/giữ hay dự báo, **hoặc** câu 6 nêu lời khuyên hành động, kể cả có điều kiện ("sell before…", "hold until death for the step-up", "keep receipts to avoid tax" nói như chỉ thị). Câu 6 "kiểm con số của chính mình / không có lời khuyên" → không tính.
- Người đọc **đúng** = điểm 1 và không câu khuyên.

**Đoạn mất chú ý:** câu 4 trích nguyên văn; P gán cảnh `Sxx` bằng khớp ≥ 5 từ liên tiếp với `script.md` (máy); không gán được → người chấm gán.

## Ngưỡng
(a) đạt hết · (b) **đúng ≥ 5/6**; **câu khuyên 0/6**; **không cảnh nào bị ≥ 4/6 cùng chỉ là chỗ mất chú ý**. Đúng bằng 5/6 → nêu tên.

## Vòng và dự phòng (ghi trước)
Tối đa 2 vòng (người đọc mới). Cảnh mất chú ý → rút còn 1 câu lời + thẻ + mô tả (V7). Câu khuyên → WRITER siết câu đối trọng đúng chỗ. Vẫn trượt → giữ bản điểm cao nhất, ghi rủi ro vào G1. Qua → issue `[Cổng C2 · tự động] Tập 4` ≤ 5 dòng, không chờ.
