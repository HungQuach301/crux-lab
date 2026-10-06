# Grading packet (blind). You are an independent grader. Each label is one reader's answers to fixed questions about a text. Grade each label literally with the rubric. You know nothing else.

## Rubric
## Chấm (rubric, người chấm độc lập)
Ba ý: (b) với 10 % trả trước có **bảo hiểm thế chấp (PMI) cho tới khi khoản vay xuống 80 %** giá trị nhà; theo lịch trả nợ riêng thì mất **khoảng 8 năm / gần một thập kỷ**; (c) trả lời bằng **lịch sử thật giá nhà + lãi vay Mỹ**, phát lại theo nhiều tháng mua; (d) đáp án là **thời gian thực tế để chạm 80 % "trên giấy"** (mức thường gặp và những trường hợp xấu / khác nhau giữa người mua), để người xem tự so với kế hoạch của mình. Đủ ba → 1; đủ hai → 0,5; ≤ một → 0.
**Cờ `overclaim`** (báo riêng, không tính ngưỡng): người đọc kể thành "video cho biết khi nào PMI của tôi được gỡ" / "PMI sẽ hết sau X năm" / dự báo.
**Câu khuyên:** `advice: true` khi câu 4 "yes" vì tin video sẽ bảo mua/chờ hoặc dự báo, **hoặc** câu 5 nêu lời khuyên hành động (mua ngay, chờ đủ 20 %, rút tiền…). Câu 5 kiểu "so kế hoạch của mình với dải lịch sử / đừng chỉ tin lịch trả nợ" là hiểu lời hứa, **không** tính. Người đọc **đúng** = điểm 1 và không câu khuyên.



Output JSON only (no prose, no code fence): {"R1": {"score": 1|0.5|0, "advice": true|false, "overclaim": true|false, "why": "<one line>"}, ...}

### R1
1. This video is for renters in their late 20s or early 30s who have about 10% saved and are weighing a first home purchase. It looks at how long it takes to get from 10% down to owing less than 80% of the home's value, which is the point where private mortgage insurance (PMI) is supposed to end. It answers by replaying 25 years of US home prices and mortgage rates, one purchase month at a time, and comparing three buyers who started in different years.

2. I'd know roughly how long 10%-down buyers historically took to reach 80% on paper, and why that time varied so much depending on when they bought.

3. Nothing is badly confusing, but a few phrases are slightly hard:
- "reaching 80% on paper is not the same as getting the insurance removed": it doesn't say what the gap is, so I'd want the video to explain it.
- "on the payment schedule alone": it's a bit jargony, though I can guess it means paying only the scheduled amounts with no price change or extra payments.
- "replay 25 years ... one purchase month at a time": it is clear enough, but it's not obvious how that gets boiled down into three buyers.

4. No. The description says outright that it "won't tell you whether to buy or wait," and it only measures past outcomes. It doesn't forecast prices or rates, and the 6.86% rate is used just as a starting point for the eight-year baseline.

5. Not much direct advice, and that seems intentional. A viewer might take away that the eight-year textbook figure is only a baseline, that the real timeline depends heavily on price movement after purchase, and that they should check their own lender's rules for removing PMI. It doesn't say to buy, wait, or put down more.

### R2
1. This video is for people like me who have saved about 10% for a first home and are wondering whether to buy now and pay mortgage insurance or keep renting until they hit 20%. It looks at how long buyers with 10% down actually take to reach 80% equity, which is the point where insurance is supposed to go away. To answer it, it replays every purchase month from 1991 to 2016 using real US home prices and mortgage rates, and shows the typical outcome and the bad ones.

2. I expect to know how long it historically took 10%-down buyers to reach 80% of their home's value on paper, and whether that was shorter than the roughly ten years the payment schedule alone suggests.

3. Nothing is badly confusing, but one phrase made me pause: "equity on paper isn't the same as getting the insurance removed." It's clear that there's a gap, but I don't know what the gap is (an appraisal? a lender request? a waiting period?), so I expect the video won't fully explain it. "No home tracks the national average exactly" is also a little abstract, though I get the point.

4. No. The video says outright that it won't tell me whether to buy or wait, and it only replays what already happened from 1991 to 2016 rather than forecasting prices or rates. It's a look at past outcomes, not a prediction or a recommendation.

5. Not much direct advice. A viewer would probably take away a realistic sense of how long mortgage insurance might last, including in bad cases, to plug into their own buy-or-wait thinking. They should also check with a lender about how insurance is actually removed, since paper equity doesn't guarantee that. And they shouldn't assume their own home will follow the national average.

### R3
1. The video is for homebuyers who can only put 10% down and will pay private mortgage insurance (PMI). It looks at how long it takes to reach 80% loan-to-value, the point where PMI is supposed to end. It answers this by replaying 25 years of US home prices and mortgage rates, one purchase month at a time, and comparing three buyers who started in different years.

2. By the end I'd know how long 10%-down buyers historically took to reach 80% on paper, and why that time varied so much depending on when they bought.

3. Nothing is seriously confusing. The one phrase that might trip a viewer is "on paper," which only becomes clear from the closing line ("reaching 80% on paper is not the same as getting the insurance removed"). Also, "a loan at September 2026's average rate of 6.86% takes about eight years" doesn't say whether that is the term-schedule-only estimate, though "on the payment schedule alone" implies it.

4. No. The description says outright that it won't tell you whether to buy or wait. It is a historical replay of past prices and rates, not a forecast, and it makes no claim about where prices or rates are headed.

5. Little direct advice. A viewer might take away that PMI removal depends on more than the payment schedule, since home price changes affect timing, and that lenders set their own removal rules, so they should check their own lender's terms. The video doesn't tell anyone what to do about buying.

### R4
1. This video is for renters around my age who've saved about 10% down and wonder whether to buy now with mortgage insurance or keep renting until they hit 20%. It replays every monthly purchase from 1991 to 2016 using actual US home prices and mortgage rates to see how long 10%-down buyers really took to reach 80% of their home's value on paper. It shows the typical timeline and the bad cases, not just the roughly ten-year schedule most people assume.

2. I expect to know how long it historically took 10%-down buyers to reach 80% equity on paper, in typical and bad scenarios, compared to the standard payment schedule.

3. Nothing is truly confusing. The one phrase I'd have to pause on is "equity on paper isn't the same as getting the insurance removed," since it's not explained here, though I get that it's a caveat: hitting 80% in theory doesn't automatically end the insurance.

4. No. The description says outright that it won't tell me whether to buy or wait. It's also looking backward at historical data from 1991 to 2016 rather than forecasting prices or rates, and it notes that no single home follows the national average.

5. Not much direct advice. A viewer would probably take away that the "about a decade of insurance" assumption may be too pessimistic or too optimistic depending on the market, and that they should check how their lender actually removes insurance. They'd still have to make the buy-or-wait call themselves based on their own situation.

### R5
1. This video is for people who have saved a 10% down payment on a first home and are deciding whether to buy now and pay mortgage insurance or keep renting until they reach 20%. It tests the common belief that insurance lasts about a decade. To do that, it replays every monthly purchase from 1991 to 2016 using US home prices and mortgage rates, and measures how long 10%-down buyers took to reach 80% of their home's value on paper, in typical and bad cases.

2. I expect to know how long it really took 10%-down buyers to reach 80% loan-to-value on paper, compared with the roughly ten-year schedule-based expectation, including the typical and worst outcomes.

3. Nothing is seriously confusing. The one phrase that may trip some viewers is "equity on paper isn't the same as getting the insurance removed," since it doesn't say why (for example, lender rules or appraisals). It reads as a deliberate caveat, though, not a gap in the video's point.

4. No. The description says outright that it "won't tell you whether to buy or wait," and it only looks backward at historical outcomes from 1991 to 2016. It makes no forecasts of prices or rates, and it cautions that no individual home tracks the national average.

5. Little direct advice, by design. A viewer might take away that the ten-year assumption is worth questioning, and that the timeline depends on price and rate conditions. They should also remember that reaching 80% on paper doesn't automatically end the insurance, and that their own home may differ from the national average. The decision itself is left to them.

### R6
1. This video is for renters who have saved around 10% down and are considering a first home purchase. It looks at how long you'd pay private mortgage insurance (PMI), meaning how long it takes to owe less than 80% of the home's value. It answers this by replaying 25 years of US home prices and mortgage rates, one purchase month at a time, and comparing how long 10%-down buyers actually took to reach 80% with the roughly eight years the payment schedule alone predicts today.

2. I'd know how long 10%-down buyers historically took to reach 80% on paper, and why that varied so much depending on the year they bought.

3. Mostly nothing, but a few phrases are slightly fuzzy. "On paper" is only loosely explained (I infer it means by the schedule or by the home's value, not by the lender actually removing PMI). "Three buyers who started in different years" doesn't say which years or why they differ. "Lenders set their own rules" is vague about what those rules are.

4. No. The description says outright that it won't tell you whether to buy or wait. It's a look back at historical data, not a forecast, and it doesn't claim to predict home prices or mortgage rates.

5. Little direct advice. A viewer might take away that the roughly eight-year schedule estimate isn't a fixed answer, since it could be shorter or longer depending on how home prices move. They might also take away that hitting 80% on paper doesn't automatically end PMI, so they should ask a lender how removal works. The video doesn't say whether to buy.
