# C2 — Ý đồ kiểm máy + kiểm mù lời (ghi TRƯỚC khi chạy kiểm mù; không sửa sau khi thấy kết quả)

Ngày 2026-10-06. Cổng **TỰ ĐỘNG** (`quality-framework.md` §4 C2; `episode.md` §2, §3.9).

## (a) Kiểm máy
`story/check_script.py` (WRITER viết, REVIEWER soát): claim ↔ `numbers.md`, "US only", "history, not a forecast", từ khuyên/dự báo (regex `checks/py/r_content.py` + danh sách riêng), luật ASR, ≤ 2 số mới/cảnh, số cốt lõi quay lại, khuôn tỉ lệ `101`, MR1. **Móc M1–M5 đo trên bản đọc thử thật** (`story/table_read.py`: ElevenLabs Eric `eleven_v3`, mốc ký tự; cảnh nối như nhà máy, đuôi 1,0 s, ident 3 s): M1 ≤ 5,0 s · M2 ≤ 30 s · M3 ≤ 30 s · M4 ≤ 10 s · M5 ≤ 45 s. Trượt → WRITER mới sửa (≤ 2 vòng); vẫn trượt → nêu ở G1.

## (b) Kiểm mù lời (headless)
**Mẫu:** lời thuần `story/script.md` (móc đã chọn), bỏ ID, vai, claim, thẻ cảm xúc, ghi chú; ranh giới cảnh = dòng trống; dòng `[on screen: …]` chỉ khi lời nói "on screen".
**Người đọc:** 5 T + 1 G, headless (`blind.py`), đủ 6; dừng sớm chỉ khi gặp câu khuyên đầu tiên (A9) hoặc 2 sai.
- T: "You are an American in your late 20s or early 30s, renting, who has saved about 10% of a home's price and is thinking about buying your first home."
- G: "Read it once, as an ordinary YouTube viewer."

**Câu hỏi cố định:**
1. Summarize the video in 3–4 sentences: who is it about, what decision, and how it unfolds.
2. What is the video's answer to its main question? Be specific.
3. Quote any sentence or passage that confused you, and say why (or "nothing").
4. Quote, word for word, the place where your attention dropped most, if anywhere, and say why (or "nowhere").
5. Does the video tell you whether to buy now or keep renting, or predict home prices or mortgage rates? Yes or no, and why.
6. What advice, if any, would a viewer take from this?

**Chấm (người chấm độc lập headless, mù tập):**
- (Q) câu hỏi: với 10 % trả trước, bảo hiểm thế chấp (PMI) kéo dài bao lâu / mua ngay trả PMI hay thuê tiếp tới 20 %.
- (A1) đáp án: theo lịch trả nợ ≈ 8 năm tới 80 %; theo lịch sử giá nhà Mỹ, thường (trung vị) ≈ **23 tháng / khoảng 2 năm** để chạm 80 % "trên giấy".
- (A2) ít nhất một: "trên giấy" ≠ được gỡ bảo hiểm (quy định bên cho vay: yêu cầu, thẩm định, thời gian tối thiểu, mốc 75 %); khoảng 1/7 mất hơn 5 năm / trường hợp chậm (10/2005, 112 tháng); ba người mua khác nhau theo năm mua.
- Đủ Q + A1 + A2 → 1; thiếu một → 0,5; ≤ một → 0. Khẳng định sai nghĩa ("PMI của bạn sẽ hết sau 2 năm", "luật gỡ PMI ở 80 % giá trị hiện tại") → 0.
- `advice: true` khi câu 5 "yes" vì tin video bảo mua/chờ hay dự báo, **hoặc** câu 6 nêu lời khuyên hành động như chỉ thị (mua ngay, chờ 20 %, xin gỡ PMI sau 2 năm…). Câu 6 "so kế hoạch với dải lịch sử / đừng chỉ dựa vào lịch trả nợ / hỏi bên cho vay quy định của họ" nói như hiểu biết, không mệnh lệnh mua/chờ → không tính.
- Người đọc **đúng** = điểm 1 và không câu khuyên.

**Đoạn mất chú ý:** câu 4 trích nguyên văn; gán cảnh `Sxx` bằng khớp ≥ 5 từ liên tiếp với lời (máy).

## Ngưỡng
(a) đạt hết · (b) **đúng ≥ 5/6**; **câu khuyên 0/6**; **không cảnh nào bị ≥ 4/6 cùng chỉ là chỗ mất chú ý**. Đúng bằng 5/6 → nêu tên.

## Vòng và dự phòng
≤ 2 vòng (người đọc mới). Cảnh mất chú ý ≥ 4/6 → rút còn 1 câu lời + thẻ V7 + mô tả. Câu khuyên → WRITER mới siết câu đối trọng. Vẫn trượt → giữ bản điểm cao nhất, nêu ở G1.

## (c) So song song headless ↔ `Explore` (một lần, `episode.md` §2; tongket-t4 §2a)
Cùng mẫu, cùng đầu bài, thêm **3 người đọc agent con `Explore`** (vai T), chỉ để so; không tính vào ngưỡng. Một người chấm chấm cả 9 nhãn trộn ngẫu nhiên. **Giữ headless** nếu: kết luận đạt/trượt của 3 `Explore` (chiếu theo cùng ngưỡng tỉ lệ) trùng với 6 headless **và** cảnh mất chú ý nhiều nhất trùng (hoặc cả hai nhóm "nowhere" đa số). Ghi token mỗi lượt hai cách.
