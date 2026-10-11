# Grading packet (blind). You are an independent grader. Each label is one reader's answers to fixed questions about a text. Grade each label literally with the rubric. You know nothing else.

## Rubric
## Chấm
Ba ý: (b) quyết định **mua nhà hay thuê** (hai người cùng xuất phát); (c) trả lời bằng **giá nhà, tiền thuê, lãi vay thật của Mỹ**, **mọi tháng bắt đầu 1991–2016**; (d) đáp án là **người mua hơn người thuê bao nhiêu lần sau 10 năm, và khi nào thua**. Đủ ba → 1; hai → 0,5; ≤ một → 0.
**Câu khuyên:** `advice: true` khi câu 4 "yes" vì tin video bảo mua/thuê hoặc dự báo giá nhà, hoặc câu 5 nêu hành động (mua đi, thuê đi…). "Hiểu lịch sử / thời điểm quan trọng" không tính. Đúng = 1 và không khuyên.


Output JSON only (no prose, no code fence): {"R1": {"score": 1|0.5|0, "advice": true|false, "why": "<one line>"}, ...}

### R1
1. The video is aimed at someone who can afford a 20% down payment and is weighing buying versus renting. It takes a $400,000 home and compares two people with identical savings, one buying with a 30-year mortgage and one renting a similar home. It replays every starting month from 1991 to 2016 using real national home prices, rents and mortgage rates, and counts how often the buyer was ahead after 10 years, and when buying lost.

2. I expect to know in what share of historical starting months buying beat renting over a 10-year span, and in which periods buying did worse.

3. Nothing is seriously confusing. Two small spots: "come out ahead" isn't defined (net worth? total cost?), and "when buying lost" doesn't say whether that means particular years or conditions. I'd also wonder why the start months end at 2016, though it's presumably so each has a full 10 years of data.

4. No. The description says outright that it is "History, not a forecast: it won't tell you whether to buy," so it won't give a buy-or-rent verdict or predict future prices. It only reports what happened in past periods.

5. A viewer might take away that the outcome has historically depended heavily on when you bought, so timing and starting conditions (prices, rents, rates) matter, and that a 10-year horizon is a meaningful test. They shouldn't take a direct instruction to buy or rent, and they'd need to check local prices, rents and their own situation, since the data is a national index and not their city or house.

### R2
1. The video is for people weighing whether to buy a home or keep renting. It looks at that decision using history: a buyer (20% down on a $400,000 home, 30-year mortgage) and a renter with the same savings start in the same month, and every start month from 1991 to 2016 is replayed with real US prices, rents and mortgage rates. It counts how often the buyer was ahead after 10 years and when buying lost.

2. I expect to know what share of historical start months left the buyer better off than the renter after 10 years, and in which periods buying did worse.

3. Nothing is really confusing. The one phrase I'd want clarified is "came out ahead", since it's not stated how that is measured (probably net wealth, including the renter investing their savings), and "real" could mean inflation-adjusted or simply actual data.

4. No. The description says outright that it is "history, not a forecast" and that it "won't tell you whether to buy," so it won't give a personal buy-or-rent verdict or predict future home prices. It also notes the prices are a national index, not any specific house or city.

5. Little direct advice. A viewer might take away a sense of how often and when buying has historically won or lost over a 10-year horizon, as one input to their own decision. They should not treat it as a recommendation, since local markets, their own finances, and future conditions may differ.

### R3
1. This video is for someone weighing whether to buy a home or keep renting, especially a person with enough saved for a 20% down payment. It looks at a $400,000 purchase with a 30-year mortgage versus renting a similar home, and it answers by replaying every starting month from 1991 to 2016 with real US prices, rents, and mortgage rates, then counting how often the buyer was ahead after 10 years and when buying lost.

2. I expect to know how often buying beat renting over 10-year periods in past US history, and in which starting periods buying did worse.

3. Mostly nothing. The one phrase I'd flag is "came out ahead," because it doesn't say what is being measured (net worth? total cost?) or whether the buyer's home equity counts as a gain. I'd also wonder why the range ends at 2016, though it likely reflects needing a full 10 years of data.

4. No. The description says outright that it is "History, not a forecast" and that it "won't tell you whether to buy," so it's neither a verdict nor a price prediction. It only shows what happened in past scenarios.

5. Not a direct buy-or-rent instruction. A viewer might take away that buying has often (or not often, depending on the results) paid off over 10-year holds, that timing of purchase has mattered, and that they should check their own city, house, and finances because the data is a national index. The takeaway is context for their own decision, not a recommendation.
