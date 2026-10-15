# Grading packet (blind). You are an independent grader. Each label is one reader's answers to fixed questions about a text. Grade each label literally with the rubric. You know nothing else.

## Rubric
## Chấm (rubric, người chấm độc lập)
Ba ý: (b) quyết định là **mua nhà hay tiếp tục thuê** (một người có tiền cọc); (c) trả lời bằng **phát lại lịch sử thật của Mỹ** (giá nhà, tiền thuê, lãi vay thật) **từ nhiều tháng/năm bắt đầu từ 1991**; (d) đáp án là **mua hơn thuê bao thường xuyên / khi nào thua** (tỉ lệ, dải kết quả, năm thua như 2006) **sau khi tính đủ chi phí sở hữu**. Đủ ba → 1; đủ hai → 0,5; ≤ một → 0.
**Cờ `overclaim`** (báo riêng, không tính ngưỡng): người đọc kể thành "video bảo mua hay thuê" / "video dự báo giá nhà hay tiền thuê".
**Câu khuyên:** `advice: true` khi câu 4 "yes" vì tin video sẽ bảo mua hay thuê hoặc dự báo, **hoặc** câu 5 nêu lời khuyên hành động (mua, thuê, chờ, mua trước khi…). Câu 5 kiểu "biết mua hơn thuê bao thường xuyên trong lịch sử / tính đủ chi phí trước khi quyết" là hiểu lời hứa hoặc thận trọng chung, **không** tính. Người đọc **đúng** = điểm 1 và không câu khuyên.


Output JSON only (no prose, no code fence): {"R1": {"score": 1|0.5|0, "advice": true|false, "overclaim": true|false, "why": "<one line>"}, ...}

### R1
1. The video is for people weighing whether owning a home beats renting a similar one. It looks at that choice by simulating two identical people with the same savings, one buying a $400,000 home and one renting, starting in each of 307 real months since 1991 and using actual US home prices, rents, and mortgage rates. It counts the buyer's costs (interest, property tax, insurance, repairs, selling) and compares both people after ten years.

2. I expect to know how often the buyer came out ahead after ten years in past US data, why 2006 buyers fell behind, and how sensitive the result is to the rent you assume.

3. Nothing is truly confusing. Two small spots are loose: "identical people with the same savings" doesn't say what the renter does with the money not spent on a down payment (presumably invests it), and "a similar one" doesn't say how similarity is defined. Neither blocks understanding.

4. No. The description says outright "History, not a forecast: no advice to buy or to rent." It frames the content as a replay of past outcomes, so it won't tell you what to do or predict future prices or rents.

5. Little direct advice. A viewer might take away that the rent-versus-buy result depends heavily on when you start and on the rent you assume, so a simple "renting wastes money" or "buying always wins" claim is too crude. They would still need to apply that to their own situation.

### R2
1. The video is for a renter like Maya who has saved enough for a 20% down payment on a roughly $400,000 home and wonders whether rent is money wasted. It looks at buying versus continuing to rent, by replaying that choice for every starting month since 1991 with two "twins" (one buys, one rents), using real US home prices, rents, and mortgage rates and counting all ownership costs, including the 6% cost of selling. It answers by showing how often buying came out ahead after ten years and when it lost.

2. By the end I expect to know in what share of historical starting months, and in which periods, buying beat renting over a ten-year span once all costs were counted.

3. Nothing is seriously confusing. The one phrase I'd want explained is "one twin who buys and one who keeps renting," since I'm not sure at first how the renting twin's money is treated (presumably the down payment is invested). Also "every cost of owning" isn't spelled out beyond the list, but the list is clear enough.

4. No. The description says explicitly "History, not a forecast: no advice to buy or to rent." It frames the video as a look back at what happened in past periods, not a prediction of future prices or rents and not a recommendation.

5. Little direct advice. A viewer would likely take away that "rent is wasted money" is too simple a claim, that owning has real costs beyond the mortgage, and that the outcome depended heavily on when you started and on how long you stayed. Any decision would still have to rest on their own situation, local prices, and how long they plan to stay.

### R3
1. This video is for a renter who has saved a 20% down payment and wonders whether renting costs more than buying once all ownership costs are counted. It looks at two identical people, one buying a $400,000 home and one renting a similar place, and replays them through 307 start months since 1991 using real home prices, rents and mortgage rates. It then shows how often the buyer came out ahead after ten years, why 2006 buyers did worse, and how the result shifts with the rent you assume.

2. I expect to know how often, historically, buying beat renting over ten years, and how sensitive that result is to the rent assumption.

3. Nothing. One small thing: "307 real start months" is clear enough in context, but I would not know until watching how the buyer's and renter's finances are compared at the end (for example, whether the renter invests the down payment). That is a detail the video will presumably explain, not a point of confusion in the wording.

4. No. The description says it is "history, not a forecast: no advice to buy or to rent," so it will report what happened in past periods rather than tell me what to do or predict future prices or rents.

5. Little direct advice, by design. A viewer might take away that the answer depends on when you buy and on the rent you compare against, so it is worth testing your own local rent and price numbers before deciding. That is a takeaway from the framing, not a recommendation the video makes.

### R4
1. The video is for renters like Maya who have saved enough for a 20% down payment and wonder whether continuing to rent is wasting money. It looks at the buy-versus-rent decision by replaying it for every month since 1991 with two "twins," one who buys and one who keeps renting, using real US home prices, rents, mortgage rates, and all ownership costs (interest, property tax, insurance, repairs, 6% selling cost). It then answers by counting how often buying came out ahead after ten years and when it lost.

2. By the end I expect to know in what share of historical start months buying beat renting over a ten-year hold, and which periods buying lost.

3. Mostly nothing. Two small points: "enough to put 20% down on a $400,000 home and pay the closing costs" is slightly unclear, because $80,000 is the down payment and it isn't obvious how the remaining $12,000 maps to closing costs. And "one twin who buys and one who keeps renting" doesn't say what the renting twin does with the saved money (for example, invests it), which matters for a fair comparison.

4. No. The description says explicitly "History, not a forecast: no advice to buy or to rent." It frames the video as a replay of past outcomes, so it won't recommend a choice or predict future prices or rents.

5. Little direct advice. A viewer would take away that "is rent wasted money?" can be tested against history, that ownership has costs beyond the mortgage, and that the outcome depended on when you bought and how long you held. Any decision would still have to be their own, based on their situation.

### R5
1. The video is for a renter like Maya who has saved enough for a 20% down payment on a median-priced home (about $400,000) and wonders if rent is money wasted. It looks at whether buying or continuing to rent leaves you better off after ten years. It answers by replaying her choice for every starting month since 1991 as two twins, one who buys and one who rents, using real home prices, rents, and mortgage rates and counting all the costs of owning.

2. I expect to know in what share of historical starting months buying beat renting after ten years, and in which periods buying lost.

3. Nothing is truly confusing. The one phrase I'd want clarified is "one twin who buys and one who keeps renting": I'd assume the renting twin invests the down payment and the monthly savings, but the description doesn't say so, and that assumption affects the outcome. "The 6% it costs to sell" is also slightly ambiguous, though I read it as agent and selling fees.

4. No. The description explicitly says "History, not a forecast: no advice to buy or to rent," so it will show what happened in past decades, not tell me what to do or predict future prices or rents.

5. Little direct advice. A viewer might take away that the answer depends on when you buy, that ownership has real costs beyond the mortgage payment (tax, insurance, repairs, selling), and that "rent is wasted money" is not automatically true. They would have to apply that to their own situation, since the video won't tell them what to do.

### R6
1. This video is for a renter with a down payment saved who wonders whether buying a median-priced home beats renting. It compares two identical people, one buying a $400,000 home and one renting a similar place, and replays them through 307 historical start months since 1991 using real prices, rents, and mortgage rates, counting all ownership costs including selling. It then shows how often the buyer came out ahead after ten years and how that changes with the rent assumed.

2. I expect to know how often, in past US history, buying beat renting over ten years, why 2006 buyers did badly, and how sensitive the result is to the rent figure.

3. Nothing. The one phrase I'd want clarified is "the same savings", since it's not obvious whether the renter invests the down payment, but it's a minor point and the description is otherwise clear.

4. No. The description says outright that this is "History, not a forecast: no advice to buy or to rent," so it only reports what happened in past periods and doesn't claim to know what prices or rents will do next.

5. No direct advice. A viewer might come away with a sense that the answer depends on timing and on the rent they compare against, so they should test their own local rent and price numbers. That is my inference, though, since the video says it won't tell anyone what to do.
