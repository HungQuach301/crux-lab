# REVIEWER — mục bắt buộc riêng của Tập 5

Áp cho **mọi** lượt REVIEWER của Tập 5 (gói C4, G2, Shorts, mô tả, thumbnail), cùng với soát thường lệ (`quality-framework.md` §7). Chủ dự án, 2026-10-06. Luật máy đề xuất: `checks-appeal.md` A20 (lô K sau).

## R1 — Không nêu số tiền phí PMI (CHẶN)
Không câu lời đọc, chữ trên hình, nhãn, thẻ phương pháp, Shorts, thumbnail, tiêu đề hay mô tả nào nêu **số tiền phí bảo hiểm thế chấp (PMI)** — theo tháng, theo năm, tổng, hay % khoản vay — vì không có nguồn (claim `pmi_premium` = không có giá trị; S04.3 "this video puts no dollar figure on it").
- **Rà:** toàn bộ `story/script.md` (cột lời) và mọi chữ hiện trên hình ở `story/beats.md` (nhãn, thẻ, chú thích); ở G2: `out/script.json`, khung bản cuối, `out/package/*`.
- **Tính là vi phạm:** một số tiền hay tỉ lệ phí đặt cạnh "PMI", "mortgage insurance", "insurance", "premium" mà người xem có thể đọc là cái giá của bảo hiểm (kể cả "about $X a month", "X% of the loan a year", "costs thousands").
- **Không tính:** giá nhà, khoản vay, trả trước, khoản trả gốc + lãi (`ex_*`, có claim), câu nói rõ là không nêu số ("no dollar figure").
- **Báo:** mỗi chỗ một dòng (id câu / id nhịp, nguyên văn, kết luận). 0 chỗ → ghi "R1: 0".
