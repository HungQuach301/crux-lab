# C1 — Ý đồ kiểm mù kể lại logline (ghi TRƯỚC khi chạy; không sửa sau khi thấy kết quả)

Ngày 2026-10-06. Giao thức Tập 5 (`episode.md` §2, lessons H2–H3): **headless** (`episodes/ep005/blind.py`, `toolkit/blind/headless.sh`), mỗi logline **3 người đọc (2 T + 1 G)**, không đối chứng, không so cặp tiêu đề. Dừng một logline khi đã 2 người đọc sai. Người chấm: 1 lượt headless độc lập, mù tập, gói nhãn ngẫu nhiên. Dự kiến 6 + 1 = 7 lượt (≈ 60 nghìn token).

## Vai
- **T:** "You are an American in your late 20s or early 30s, renting, who has saved about 10% of a home's price and is thinking about buying your first home."
- **G:** không vai.

## Câu hỏi cố định
1. In 2–3 sentences, retell what this video will be about: who it is for, what decision it looks at, and how it will answer it.
2. What do you expect to know by the end? (one sentence)
3. Was anything confusing or hard to follow? Quote the exact words, or say "nothing".
4. Does it sound like the video will tell you whether to buy now or keep renting, or predict home prices or mortgage rates? Answer yes or no, then why.
5. What advice, if any, would a viewer take from this?

## Chấm (rubric, người chấm độc lập)
Ba ý: (b) với 10 % trả trước có **bảo hiểm thế chấp (PMI) cho tới khi khoản vay xuống 80 %** giá trị nhà; theo lịch trả nợ riêng thì mất **khoảng 8 năm / gần một thập kỷ**; (c) trả lời bằng **lịch sử thật giá nhà + lãi vay Mỹ**, phát lại theo nhiều tháng mua; (d) đáp án là **thời gian thực tế để chạm 80 % "trên giấy"** (mức thường gặp và những trường hợp xấu / khác nhau giữa người mua), để người xem tự so với kế hoạch của mình. Đủ ba → 1; đủ hai → 0,5; ≤ một → 0.
**Cờ `overclaim`** (báo riêng, không tính ngưỡng): người đọc kể thành "video cho biết khi nào PMI của tôi được gỡ" / "PMI sẽ hết sau X năm" / dự báo.
**Câu khuyên:** `advice: true` khi câu 4 "yes" vì tin video sẽ bảo mua/chờ hoặc dự báo, **hoặc** câu 5 nêu lời khuyên hành động (mua ngay, chờ đủ 20 %, rút tiền…). Câu 5 kiểu "so kế hoạch của mình với dải lịch sử / đừng chỉ tin lịch trả nợ" là hiểu lời hứa, **không** tính. Người đọc **đúng** = điểm 1 và không câu khuyên.

## Ngưỡng
Logline **qua** khi **2/2 người đọc T đúng**. G báo riêng (cờ khuyên của G nêu tên). Cả hai qua → khuyến nghị bản ít cờ hơn, hoà thì L2 (câu hỏi người xem, story §1.1). Cả hai trượt → vòng 2 (sửa theo câu 3, người đọc mới), tối đa 2 vòng; vẫn trượt → đưa bản tốt nhất kèm điểm vào G1.
