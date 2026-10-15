# Grading packet (blind). You are an independent grader. Each label is one reader's answers to fixed questions about a text. Grade each label literally with the rubric. You know nothing else.

## Rubric
## Chấm (rubric, người chấm độc lập)
Ba ý: (b) quyết định là **mua nhà, hay thuê và đầu tư phần tiền không dùng cho nhà** (cọc + chênh hằng tháng) vào cổ phiếu; (c) trả lời bằng **phát lại lịch sử thật của Mỹ** (giá nhà, tiền thuê, lãi vay, lợi nhuận cổ phiếu thật) **từ nhiều tháng/năm bắt đầu từ 1991**; (d) đáp án là **người mua còn hơn bao thường xuyên khi người thuê đầu tư** (tỉ lệ sau 10/15 năm, so với khi để tiền mặt, hoặc khi không đầu tư phần chênh). Đủ ba → 1; đủ hai → 0,5; ≤ một → 0.
**Cờ `overclaim`** (báo riêng, không tính ngưỡng): người đọc kể thành "video bảo mua, thuê hay đầu tư" / "video dự báo giá nhà, tiền thuê hay cổ phiếu".
**Câu khuyên:** `advice: true` khi câu 4 "yes" vì tin video sẽ bảo mua/thuê/đầu tư hoặc dự báo, **hoặc** câu 5 nêu lời khuyên hành động (mua, thuê, đầu tư, chờ…). Câu 5 kiểu "biết trong lịch sử ai hơn bao thường xuyên / tính đủ chi phí trước khi quyết" là hiểu lời hứa hoặc thận trọng chung, **không** tính. Người đọc **đúng** = điểm 1 và không câu khuyên.


Output JSON only (no prose, no code fence): {"R1": {"score": 1|0.5|0, "advice": true|false, "overclaim": true|false, "why": "<one line>"}, ...}

### R1
1. This video is for someone like me, a renter with a 20% down payment saved who has heard "rent and invest the difference." It looks at whether renting and investing in the stock market beats buying a $400,000 home. It answers by replaying two identical people through 307 real start months since 1991, using actual home prices, rents, mortgage rates and stock returns, and checking how often the buyer was ahead after 10 and 15 years.

2. By the end I expect to know how often, in past data, the buyer versus the rent-and-invest person came out ahead, and how that changes if the renter stops investing the monthly savings or if the assumed rent is different.

3. Nothing really, though two small things: "the whole US stock market" doesn't say which index or whether dividends and fees are included, and "307 real start months" overlap heavily, so they aren't 307 independent tests. Neither is confusing enough to lose me.

4. No. The description says "History, not a forecast: no advice to buy, rent or invest," so it will show what happened in the past rather than tell me what to do or predict future prices, rents or returns.

5. No direct advice. A viewer might take away that the "rent and invest the difference" claim depends on assumptions: whether the renter actually keeps investing every month, what rent is compared to the mortgage, and the period you start in. They would likely be more skeptical of the slogan and check those assumptions against their own local rent and prices, but the video doesn't tell them which choice to make.

### R2
1. The video is for people weighing the "rent and invest the difference" idea against buying a home. It looks at whether a renter who invests a down payment and monthly savings in the US stock market ends up ahead of a buyer of a $400,000 home. It answers by replaying two identical people through 307 real start months since 1991, using historical home prices, rents, mortgage rates and stock returns.

2. By the end I expect to know how often the buyer was still ahead after ten and fifteen years in the historical record, and how that changes if the renter stops investing or if the assumed rent differs.

3. Mostly nothing, but a few phrases could trip a viewer up: "the whole US stock market" (is it a total-market index, and are dividends and fees included?) and "the difference" (it isn't defined until you read "every month's savings"). "Same savings" and "identical people" also leave open whether the buyer's costs (taxes, maintenance, insurance) are counted. These are small gaps, not real confusion.

4. No. The description says "History, not a forecast: no advice to buy, rent or invest." It frames the video as a replay of past outcomes, not a prediction of future home prices, rents or stock returns, and not a recommendation.

5. Ideally none that is directly actionable. A viewer might take away that the claim "renting and investing always wins" didn't hold uniformly in the past, and that the result depends on how long you hold, whether you keep investing, and what rent you assume. A careless viewer could still read the historical frequencies as a hint about what to do, even though the video says it isn't advice.

### R3
1. The video is for someone who rents and has saved enough for a 20% down payment plus closing costs, using Nina as the example. It looks at whether buying a home beats renting while investing the leftover money in the US stock market. It answers by replaying all 307 start months since 1991 with real home prices, rents, mortgage rates, stock returns and all ownership costs, then counting how often the buyer is still ahead after ten and fifteen years, and what changes if the renter doesn't invest the monthly difference.

2. I expect to know the share of historical start months in which buying beat renting-and-investing at 10 and 15 years, and how much that share shifts if the renter skips investing the monthly difference.

3. Nothing is seriously confusing. The one small snag is "her renting twin" and "Last time", which assume you saw the previous video, though the 3-in-4 cash result is explained enough to follow. "Invests every dollar she doesn't spend on housing" is also slightly abstract until you see it worked out.

4. No. The description says "History, not a forecast: no advice to buy, rent or invest." It presents past outcomes of a replay, not a recommendation or a prediction of future prices, rents or returns.

5. None directly, since the video explicitly gives no advice. A viewer might take away that how the renter handles the monthly difference matters a lot to the comparison, and that past outcomes varied by start month. Any decision would be their own.

### R4
1. This video is for a renter like Nina who has enough saved for a 20% down payment on a median-priced home (about $400,000) and wonders if "rent and invest the difference" really beats buying. It looks at buying versus renting when the renter puts her down payment and her monthly savings into the total US stock market, instead of leaving them in cash. It answers by replaying 307 historical start months since 1991 with real home prices, rents, mortgage rates, stock returns and all ownership costs, and counting how often the buyer is still ahead after 10 and 15 years.

2. I expect to know in what share of historical start months buying beat renting-and-investing at 10 and 15 years, and how that share changes if the renter doesn't invest the monthly difference.

3. Nothing is clearly confusing. Two small points: "invests every dollar she doesn't spend on housing" is a bit ambiguous about whether it includes the down payment, though "keeps that money" in the earlier sentence suggests it does. "Her renting twin" assumes you saw the last video, but the recap of the 3-in-4 result is enough to follow along.

4. No. The description says outright "History, not a forecast: no advice to buy, rent or invest." It frames the video as a replay of past outcomes, so it reports how often each side came out ahead and does not claim to know what prices, rents or stocks will do next.

5. Little or none, and that is by design. A viewer could take away that the "rent and invest" claim can be checked against history, and that the answer depends on the horizon and on whether the renter actually invests the monthly difference. But they shouldn't take away a recommendation to buy, rent or invest, since the video says it isn't giving one.

### R5
1. The video is for a renter with enough saved for a down payment who wonders whether "rent and invest the difference" really beats buying. It takes two identical people, one buying a $400,000 home and one renting and investing the down payment plus the monthly savings in the total US stock market, and replays them through 307 historical start months since 1991 using real home prices, rents, mortgage rates and stock returns. It answers by showing how often the buyer was still ahead after 10 and 15 years, what happens if the renter stops investing, and how the result shifts with the rent assumed.

2. I expect to know how often, in past US data, the buyer or the renter-investor came out ahead after 10 and 15 years, and how sensitive that is to investing discipline and rent level.

3. Nothing really blocks understanding. The only mildly fuzzy bits are "307 real start months" (I'd want a quick note that these are overlapping windows, not 307 independent trials) and "the difference" (I assume it means monthly ownership cost minus rent, but the video should say so). Neither is confusing enough to lose me.

4. No. The description says outright that it is "History, not a forecast: no advice to buy, rent or invest." It is framed as a replay of past outcomes, so it won't tell me what to do or predict future prices, rents or returns.

5. Essentially none, and that's by design. A viewer might take away that the answer depends on assumptions, especially whether the renter keeps investing and what rent is, so "rent and invest the difference" isn't automatically a win. They'd have to apply that to their own situation, since the video doesn't tell them what to do.

### R6
1. This video is for a renter like Nina who has enough saved for a 20% down payment on a median-priced home and wonders if "rent and invest the difference" really beats buying. It looks at buying versus renting when the renter puts all her non-housing money into the total US stock market. It answers by replaying 307 historical start months since 1991, using real home prices, rents, mortgage rates, stock returns and all ownership costs, and counting how often the buyer is ahead after 10 and 15 years.

2. I expect to know in what share of historical start months the buyer still came out ahead at 10 and 15 years when the renter invests, and how that changes if the renter doesn't invest the monthly difference.

3. Nothing. The one phrase that needs a moment is "invests every dollar she doesn't spend on housing," meaning the down payment plus any monthly savings from renting being cheaper than owning, but the next sentences make that clear enough.

4. No. The description says "History, not a forecast: no advice to buy, rent or invest," and the video replays past data rather than projecting future prices, rents or returns.

5. No direct advice. A viewer might take away that "rent and invest the difference" isn't automatically a winner, or that it depends on the period, but only as a description of how past periods turned out. They would still need to weigh their own situation, local market and risk tolerance, since the past results aren't a prediction.
