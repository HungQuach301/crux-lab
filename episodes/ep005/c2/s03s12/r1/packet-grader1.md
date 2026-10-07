# Grading packet (blind). You are an independent grader. Each label is one reader's answers to fixed questions about a text. Grade each label literally with the rubric. You know nothing else.

## Rubric
**Chấm:** (a) luật: xin huỷ ở 80 % / tự hết ở 78 % theo lịch gốc (giá trị lúc mua) — đủ một trong hai và gắn với "lịch/schedule"; (b) gỡ theo giá trị hôm nay là quy định của chủ khoản vay — với khoản vay Fannie Mae: **chờ ít nhất 2 năm và khoản vay ≤ 75 %** giá trị hiện tại (cả hai ý, kể cả 2 năm đọc từ nhãn); (c) 15,6 % = tỉ lệ tháng mua (lịch sử) ở/dưới 75 % sau 2 năm. Đủ 3 → 1; đủ 2 → 0,5; ≤ 1 → 0. Khẳng định sai nghĩa (75 % là luật liên bang / áp mọi khoản vay; 15,6 % là xác suất của người xem) → 0. `advice` như C2.


Output JSON only (no prose, no code fence): {"R1": {"score": 1|0.5|0, "advice": true|false, "two_years_from_label": true|false, "why": "<one line>"}, ...}

### R1
1. This part explains how long private mortgage insurance (PMI) lasts on a 10%-down loan, and whether rising home prices can end it sooner than the legal payoff schedule. It replays 1991 to July 2016 purchase months using a national price index. The typical loan reached 80% of the home's value "on paper" in 23 months, but only 15.6% of purchases cleared Fannie Mae's stricter 75% bar by the two-year mark.

2. Under the law's schedule, you can ask to cancel once the loan is scheduled to reach 80% of the original value ($320,000 in the example), which is payment 99. You also have to be current on payments, among other conditions. The insurance must end automatically at 78% of the original value, about 9.5 years in, if you're current. Both dates ignore what the house is worth. Removal based on today's value is different. It's the rules of the lender or loan owner, not the law's schedule. It uses the home's current value, so price gains can get you there sooner. You have to ask, and an appraisal and a minimum waiting time still apply.

3. It requires a waiting period (the screen says at least 2 years) and a loan at or below 75% of the home's current value. You also have to be the one to ask.

4. It's the share of purchase months since January 1991 (with two years of later price data) in which the loan was at or below 75% of the index-adjusted home value two years after purchase. In other words, in about 84% of cases the Fannie Mae value-based removal wouldn't have been available yet at two years.

5. Confusing bits:
- "On this loan, that's payment 99, the date this video opened with." This excerpt never mentions payment 99 at the start, and "payment 99" isn't translated into years.
- "At September's average mortgage rate, 6.86 percent" doesn't say which year. The loan term (30 years?) is never stated either, though I assume it.
- "You'll also meet three illustrative buyers who got very different answers." They don't appear in this section.
- "for Fannie Mae loans, that's a waiting period and a 75 percent bar." The length of the wait appears only on screen, not in the narration.
- The 23-month result covers purchases from 1991 to July 2016, while the 15.6% covers a larger set of months. I had to work out that these are different groups and not directly comparable.
- "Common" for reaching 80% on paper in about two years sits oddly next to a median of 23 months, since half took longer.

6. The video says it isn't advice on whether to buy or wait, so the takeaways are limited:
- Don't count on price gains to drop PMI quickly, and don't assume the schedule dates are your only options.
- Find out who owns your loan and what their value-based removal rules are (waiting period, LTV threshold, appraisal).
- Know that the law gives a request right at 80% and automatic cancellation at 78% of the original value.
- Past price growth doesn't predict the future. This is history, not a forecast, and it gives no PMI cost, so I'd still need real quotes.

### R2
1. This part explains how long PMI lasts for a buyer putting 10% down. It compares the legal schedule, which ends PMI at about 8 years (request) or 9.5 years (automatic), with a historical replay in which rising home prices got the loan to 80% of value "on paper" in a typical 23 months. It then notes that actually having PMI removed on current value is a separate, stricter process, and that few buyers would have met Fannie Mae's early bar.

2. Under the law's schedule, the borrower can ask to cancel once the scheduled balance reaches 80% of the original value ($320,000 in the example, payment 99), if they are current on payments and meet other conditions. PMI must end automatically when the schedule reaches 78%, about 9.5 years in, if payments are current. Both dates ignore what the house is worth. Removal based on today's value is different. A lender or loan owner can choose to allow it, so if prices rise the same balance is a smaller share of the home and 80% can arrive sooner. But it depends on the loan owner's rules, and you must request it, usually with an appraisal and a minimum time.

3. For Fannie Mae loans, it requires a waiting period (the screen says at least 2 years) and a loan of 75% or less of the home's current value. I assume the 75% is measured against current value, though the narration doesn't spell that out.

4. It is the share of purchase months, among all those since January 1991 with two years of later price data, where the loan was at or below 75% of the home's value two years after purchase. In other words, only about 1 in 6 would have cleared Fannie Mae's bar at the two-year mark.

5. Confusing parts:
- "On paper means the loan is 80 percent of the home's value by a national price index." The term is introduced up front, but the explanation is spread out and I had to piece it together.
- "On this loan, that's payment 99, the date this video opened with." The excerpt doesn't state payment 99 at the start, so I can't tell what "opened with" refers to.
- "You'll also meet three illustrative buyers who got very different answers." They never appear in this section.
- "The typical answer: 23 months" versus "15.6 percent" uses two different samples (1991 to July 2016 purchases, versus all months with two years of data) and two different thresholds (80% versus 75%). I could easily mix them up.
- "That's the gap between the schedule's long road and the replay's typical one." It's unclear whether the schedule's long road means 99 payments or 9.5 years.
- "Taxes, home insurance and the mortgage insurance all come on top of it" is clear, but the video gives no PMI cost, so I can't tell how much is at stake.

6. The video explicitly gives no buy-or-wait advice. A viewer could take away that PMI won't necessarily last the full 8 to 9.5 years if prices rise, but that you shouldn't count on early removal. It depends on your loan owner's rules, an appraisal and a waiting period, and meeting an early bar like Fannie Mae's 75% was uncommon in this history. A sensible step would be to ask a lender what their PMI removal rules are before buying.

### R3
1. This part explains how long PMI lasts on a 10%-down loan. It compares the legal schedule (request at 80%, automatic end at 78%, here roughly 8 and 9.5 years) with a historical replay in which rising home prices got the loan to 80% of value "on paper" in a typical 23 months. It then warns that clearing Fannie Mae's stricter bar for removal on today's value after two years was uncommon (15.6%).

2. Under the law's schedule, on the $360,000 loan, I can ask to cancel when the scheduled balance reaches 80% of the original value ($320,000). That is payment 99, with conditions like being current on payments. The insurance must end automatically at 78%, about 9.5 years in, if payments are current. Both dates ignore what the house is worth. Removal based on today's value is different. The lender or loan owner can drop PMI because prices rose and the same balance is now a smaller share of the home. That route runs on the loan owner's rules, not the law's schedule, and it involves a request, an appraisal and a minimum time.

3. It requires a waiting period (the on-screen text says at least 2 years) and a loan of 75% or less of the home's current value.

4. It is the share of purchase months, among every month since January 1991 with two years of prices after it, in which the replayed loan was at or below 75% of the home's value two years after purchase. In other words, 15.6% of buyers would have met Fannie Mae's bar at the two-year mark.

5. Confusing bits:
- "That's payment 99, the date this video opened with." I haven't seen the opening in this clip, so I don't know what date that refers to.
- "At September's average mortgage rate, 6.86 percent." It doesn't say which September. It also never says the loan is 30 years, though the $2,362 only works out that way.
- "We took every purchase month from January 1991 to July 2016" versus "every purchase month since January 1991 with two years of prices after it." These are two different sets of months. I can't tell why the first stops in 2016, or whether the 23-month figure and the 15.6% figure can be compared directly.
- "Reaching 80% in about two years was common" sits next to "23 months" and "90.6%." I had to work out that 23 months is the typical time to 80% and 90.6% is the share beating the schedule, which is a different thing.
- The narration mentions "a waiting period" for Fannie Mae without giving the length. The 2 years appears only on screen.

6. The video gives no buy-or-wait advice, and says so. What I'd take from it:
- Don't assume PMI will fall off in two years just because prices are rising, since the early bar is hard to clear.
- Know the legal dates (80% to request, 78% automatic) as a backstop.
- Find out who owns my loan and what its value-based removal rules are before I buy.
- Treat the history as history, not a forecast.

### R4
1. This part explains how long PMI (private mortgage insurance) lasts on a 10%-down loan. It compares the legal schedule-based end dates with the earlier date you might reach if home prices rise. It then replays 1991-2016 history to show that reaching 80% "on paper" within about two years was typical, but clearing Fannie Mae's stricter bar by then was not.

2. Under the law's schedule, you can ask to cancel once the loan is scheduled to reach 80% of the original value ($320,000 on the example loan, at payment 99), if you're current on payments and meet other conditions. The insurance must end automatically at 78% of the original value (about 9.5 years in on the example), if you're current. Both dates depend only on the payment schedule and ignore what the house is worth. Removal on today's value is different. It uses the home's current value, so rising prices can get you under 80% sooner. It's up to the loan owner's rules, and it comes with a request, an appraisal and a minimum time.

3. For Fannie Mae loans, you have to wait at least 2 years, and the loan has to be 75% or less of the home's current value.

4. It's the share of purchase months (from a larger set since January 1991 with two years of later prices) in which the loan was at or below 75% of value two years after purchase, following the national price index. So only about 1 in 6 would have cleared Fannie Mae's bar on today's value by then.

5. Confusing bits:
- "On paper means the loan is 80 percent of the home's value by a national price index." The opening is abstract, and I only half understood it until later.
- "On this loan, that's payment 99, the date this video opened with." This refers to something not in this section, so I can't tell what date it means.
- The 30-year term is never stated, though the $2,362 and "9.5 years" depend on it.
- It mixes 80% (on paper, the replay) with 75% (Fannie Mae), and it uses two different sets of purchase months (the 23-month replay and the larger set for the 15.6%). It's easy to lose track of which number answers which question.
- "Waiting period" in the opening isn't specified until the on-screen text, and the narration never says "2 years" there.

6. Don't assume PMI will go away quickly just because prices rise. The automatic and request dates are slow (about 8 to 9.5 years here), and the faster route depends on the loan owner's rules. Before buying, I'd ask the lender who will own or service the loan and what their PMI removal rules are, including the waiting period, the value threshold and whether an appraisal is needed. The video explicitly doesn't say whether to buy or wait, and past price growth isn't a forecast.

### R5
1. This part explains that PMI is insurance a borrower pays to protect the lender when they put down less than 20% on a conventional loan, and it looks at how long it lasts. It walks through a $400,000 home with 10% down and shows that the law's schedule ends PMI well after a replay of historical home prices would have gotten the loan to 80% "on paper." It then cautions that reaching 80% on paper isn't the same as getting PMI removed, since lenders and loan owners like Fannie Mae have their own rules.

2. Under the law's schedule, you can ask to cancel once the schedule says the loan is down to 80% of the original value ($320,000 here), which is payment 99, if you're current on payments and meet other conditions. PMI must end automatically at 78% on the schedule, about 9.5 years in here, if payments are current. Both dates ignore what the house is worth. Removal based on today's value is different: it depends on the lender's or loan owner's rules, not the law's schedule, and it involves a request, an appraisal, and a minimum time. If prices rise, the same balance is a smaller share of the home, so you could get there sooner.

3. For Fannie Mae loans, it requires a waiting period of at least 2 years and a loan of 75% or less of today's value.

4. It's the share of purchase months in the larger set (every month since January 1991 with two years of prices after it) in which the loan was at or below 75% of the home's value two years after purchase. So only about 1 in 6 would have cleared Fannie Mae's early 75% bar by then.

5. Possibly confusing:
- "On paper means the loan is 80 percent of the home's value by a national price index." This is abstract at the start, before PMI is explained.
- "payment 99, the date this video opened with." The video as narrated here never states that date up front, so a viewer might not recall it.
- "The typical answer: 23 months," versus "about two years," versus the 15.6% figure. Someone could mix up the 80% on-paper measure with the 75% Fannie Mae measure.
- "Three illustrative buyers" is promised but doesn't appear in this section.
- "At September's average mortgage rate" and "April through June" don't name a year, which is unclear.
- "Half got there sooner, half took longer" and "90.6 percent... no later than the schedule" are two different statistics close together.
- The window "January 1991 to July 2016" for the replay versus "since January 1991" for the larger set isn't explained.

6. A viewer might take away that the schedule dates (80% and 78%) are a floor they can count on, while removal sooner based on rising home values is not automatic. It depends on the loan owner's rules, such as Fannie Mae's wait and 75% bar, and possibly an appraisal. They should find out who owns their loan and what its removal rules are. The video explicitly doesn't say whether to buy or wait, and it gives no PMI cost, so it offers no advice on those. It also shouldn't be read as a forecast, because it's historical.

### R6
1. This part explains how long private mortgage insurance lasts on a 10%-down loan and compares two ways it can end: the legal schedule versus rising home prices. Using a $400,000 example and a replay of US price history from 1991 to 2016, it finds that prices typically got the loan to 80% of value "on paper" in about 23 months. Getting insurance actually removed under a stricter lender rule, like Fannie Mae's, was much less common by two years.

2. Under the law's schedule, the borrower can request cancellation when the scheduled balance reaches 80% of the original value (payment 99 in the example, $320,000), if payments are current and other conditions are met. The insurance must end automatically at 78% of original value (about 9.5 years in), if payments are current. Both dates depend only on the payment schedule and ignore what the house is worth. Removal based on today's value is different: it's a lender or loan-owner rule, not the law's schedule. If prices rise, the same balance is a smaller share of the current value, so 80% can come sooner. But the lender's request process, appraisal, and minimum waiting time still apply.

3. It requires waiting at least 2 years and having a loan at or below 75% of the home's current value. The video also mentions a request and appraisal as part of the lender process.

4. It's the share of purchase months, among all those since January 1991 with two years of subsequent prices, where the loan was at or below 75% of value two years after purchase. In other words, only about 1 in 6 of those buyers would have cleared Fannie Mae's early 75% bar by the two-year mark.

5. Some things were confusing:
- "You'll also meet three illustrative buyers who got very different answers." The video never shows those three buyers in this section.
- "On this loan, that's payment 99, the date this video opened with." The opening here doesn't mention payment 99, so the reference doesn't land.
- "The typical answer: 23 months." Then "90.6 percent ... no later than the schedule would have." These are different measures, and the jump between them is quick.
- The "75 percent bar" is described as measured against current value, but it's never stated plainly. The 15.6% figure is compared with the 80%-on-paper result, which are different thresholds, so the comparison takes effort to follow.
- The video says the 2-year Fannie Mae figure comes from a "larger set" than the 1991–July 2016 set, without explaining why the sets differ.

6. A viewer might take away that PMI doesn't automatically end when home prices rise. The legal schedule dates (80% request, 78% automatic) are fixed by the loan's amortization. Ending it sooner based on current value depends on the loan owner's rules, such as Fannie Mae's wait and 75% bar. The video explicitly says it doesn't advise on whether to buy or wait, so the practical suggestion is to check the specific lender's or loan owner's rules and not assume rising prices alone will remove the insurance.
