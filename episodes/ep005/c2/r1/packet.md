# Grading packet (blind). You are an independent grader. Each label is one reader's answers to fixed questions about a text. Grade each label literally with the rubric. You know nothing else.

## Rubric
**Chấm (người chấm độc lập headless, mù tập):**
- (Q) câu hỏi: với 10 % trả trước, bảo hiểm thế chấp (PMI) kéo dài bao lâu / mua ngay trả PMI hay thuê tiếp tới 20 %.
- (A1) đáp án: theo lịch trả nợ ≈ 8 năm tới 80 %; theo lịch sử giá nhà Mỹ, thường (trung vị) ≈ **23 tháng / khoảng 2 năm** để chạm 80 % "trên giấy".
- (A2) ít nhất một: "trên giấy" ≠ được gỡ bảo hiểm (quy định bên cho vay: yêu cầu, thẩm định, thời gian tối thiểu, mốc 75 %); khoảng 1/7 mất hơn 5 năm / trường hợp chậm (10/2005, 112 tháng); ba người mua khác nhau theo năm mua.
- Đủ Q + A1 + A2 → 1; thiếu một → 0,5; ≤ một → 0. Khẳng định sai nghĩa ("PMI của bạn sẽ hết sau 2 năm", "luật gỡ PMI ở 80 % giá trị hiện tại") → 0.
- `advice: true` khi câu 5 "yes" vì tin video bảo mua/chờ hay dự báo, **hoặc** câu 6 nêu lời khuyên hành động như chỉ thị (mua ngay, chờ 20 %, xin gỡ PMI sau 2 năm…). Câu 6 "so kế hoạch với dải lịch sử / đừng chỉ dựa vào lịch trả nợ / hỏi bên cho vay quy định của họ" nói như hiểu biết, không mệnh lệnh mua/chờ → không tính.
- Người đọc **đúng** = điểm 1 và không câu khuyên.



Output JSON only (no prose, no code fence): {"R1": {"score": 1|0.5|0, "advice": true|false, "attention_quote": "<reader Q4 quote, first 12 words, or nowhere>", "why": "<one line>"}, ...}

### R1
1. The video follows someone with 10 percent saved for a home who has to decide whether to buy now and pay private mortgage insurance (PMI) or keep renting until they hit 20 percent. It uses a $400,000 example home and a $360,000 loan to show how long PMI lasts. It first gives the legal schedule (request cancellation at payment 99, automatic termination around 9.5 years). Then it replays every purchase month from 1991 to 2016 against a national price index, and ends with three buyers (Grace, Owen, Victor) who got very different timelines.

2. The answer depends on which clock you use. On the legal schedule, you can request cancellation at payment 99 (about 8 years) and it ends automatically at about 9.5 years. On paper, using price growth, the typical replay got the loan to 80 percent in 23 months, and the range ran from 13 months (fastest) to 112 months (slowest, October 2005). About 1 in 7 months took more than 5 years. Only 15.6 percent were at or below the 75 percent bar two years in. Reaching 80 percent on paper is not the same as the insurance actually being removed.

3. "On the schedule alone, you can't even ask to cancel it for about 8 years." It's the very first claim and arrives before I know what "the schedule" is or what "ask to cancel" means. Later I learn it means payment 99, but for the first minute it floats unexplained. Also: "Her own schedule would have taken several years longer." Several years longer than what? It's unclear if that's compared to her 80-percent-on-paper date or something else, and I have no number to anchor it. And "That's the road behind the words on paper, with the lender's rules from the opening still in the way." This one is hard to follow. "Road" is used metaphorically in several places and I can't tell what exactly it refers to.

4. "Not modeled here: what the insurance costs, appraisal fees, rent, local prices, or how fast savings grow." It's a list of everything left out, read quickly right after the personal stories, and it's the part where I most want to know the stuff that matters for my decision (cost, rent). It feels like a disclaimer block, so my attention drifts, even though the omissions are the very things I'd need to decide.

5. No. The video says outright that it "won't say whether to buy or wait," that it's "history, not a forecast," and that it doesn't weigh 20 percent down against renting or waiting. It only measures how long the insurance math took, using past data, and makes no prediction about prices or rates.

6. A viewer would take away a few cautions rather than a recommendation. Don't assume the insurance disappears when you reach 80 percent on paper, since removal on value depends on the lender's policy (request, appraisal, minimum time, a 75 percent bar early on). Don't count on price growth: a plan that assumes about two years matches the typical month but not the slow ones. And know the fallback is the legal schedule, which runs most of a decade on the example loan. The viewer should check their own lender's removal rules and local market, and find out the actual insurance cost, since the video leaves that out.

### R2
1. The video is about a first-time buyer with 10% saved, weighing whether to buy now and pay mortgage insurance (PMI) or keep renting until reaching 20%. It uses a $400,000 example home and a $360,000 loan to show the legal schedule: you can ask to cancel at payment 99 and it ends automatically at about 9.5 years. It then replays US prices and rates from 1991 to 2016 to see how fast rising prices got the loan to 80% on paper. Three illustrative buyers, Grace, Owen, and Victor, show how much the start month mattered.

2. It doesn't give one number. On the schedule alone, the answer is fixed at the start: you can request cancellation at about 8 years (payment 99) and it ends automatically around 9.5 years. On paper, using price history, the typical case was 23 months. In 90.6% of purchase months, prices got there no later than the schedule would have. The range ran from 13 months (fastest, January 2004) to 112 months (slowest, October 2005), and about 1 in 7 months took more than 5 years. Also, "on paper" is not the same as removal: lenders require a request, an appraisal, a minimum time, and early on a 75% bar. Only 15.6% of months had hit 75% by two years.

3. "Here, that's about 9.5 years in." Earlier the video says you can't even ask to cancel for "about 8 years," and payment 99 is about 8.25 years. The numbers are fine, but the 78% auto-termination point is not explained, and I had to work out that it's a separate, later date.

   I also stumbled on "On this loan, that's payment 99: the schedule's road from the opening." The phrase "the schedule's road from the opening" is vague and callback-heavy, so I wasn't sure what it referred to on first hearing.

   Related: "Victor... his own schedule reached 80 percent of the original price first, at payment 90." That seems to conflict with the 112 months on paper and the claim that 112 is longer than the schedule. It makes sense once you note his rate was different from the example's 6.86%, but the video never says so.

4. "Not modeled here: what the insurance costs, appraisal fees, rent, local prices, or how fast savings grow."

   My attention dropped there because it's a list of omissions delivered right when I wanted help with my own decision. It shifts from the story to disclaimers. The earlier stretch, "We took every purchase month from January 1991 to July 2016. For each one, we set up the same 10 percent down loan..." was also dense methodology.

5. No. It says outright that it "won't say whether to buy or wait," and it closes with "history, not a forecast." It doesn't predict prices or rates. It only replays past data and says it doesn't weigh $40,000 more down against renting or waiting. The reason is that it measures how long the insurance lasted, not whether buying is right.

6. A viewer would take away the following:
   - Don't assume PMI ends in about two years just because that was typical. That matched the median month, not the slow ones, and not the lender's rules.
   - The legal schedule is the dependable baseline, roughly 8 to 9.5 years on the example loan. Anything faster depends on prices rising.
   - Removal on value depends on lender policy: a request, an appraisal, a minimum holding time, and possibly a 75% bar.
   - Timing and local prices matter a lot, and a bad stretch can leave you well past five years.
   - A plan should be tested against both the slow and the typical case, and the viewer still has to weigh insurance cost, rent, and savings on their own.

### R3
1. The video follows a first-time buyer with 10% saved who is deciding whether to buy now with mortgage insurance (PMI) or keep renting until 20% down. It uses a $400,000 example home and a $360,000 loan at 6.86%, then compares two clocks: the legal schedule, and a replay of US history from 1991 to 2016 using a national price index. It finishes with three buyers (Grace, Owen, Victor) who got very different timelines depending on when they bought. It deliberately doesn't say whether to buy or wait.

2. The answer is that it depends on which clock you use, and "on paper" isn't "removed." On the schedule, you can request cancellation at payment 99 (about 8 years) and it ends automatically at about 9.5 years. In the historical replay, the typical purchase reached 80% loan-to-value on paper in 23 months, and 90.6% of months got there no later than the schedule. About 1 in 7 took over 5 years, the slowest was 112 months (October 2005), and the range was roughly 13 months to more than 9 years. Only 15.6% were at or below a 75% bar at two years.

3. "That's the road behind the words on paper, with the lender's rules from the opening still in the way." It's vague: it points back to earlier material without saying clearly what "the road" is. Also, "That's longer than the schedule itself took at that month's rate" is hard to follow, because I'm comparing 112 months to a schedule figure I was never given for that month. Later, Victor's schedule hitting 80% "at payment 90" confused me too, since the example schedule was 99 payments at a different rate. I had to work out that it's a different loan.

4. "Here, that's about 9.5 years in." followed by the stretch from "Both dates come from the schedule alone..." through the methodology block ("We took every purchase month from January 1991 to July 2016. For each one, we set up the same 10 percent down loan at that month's average rate...") is where I drifted. It's a dense run of process description with no payoff until the bars appear. The line "Each bar here is one purchase month, and its height shows how long that took" helped, but I'd already lost some attention by then.

5. No. It states outright that it is history, not a forecast, and that it "won't say whether to buy or wait." It also excludes insurance cost, rent, local prices, and savings growth, so it couldn't make a buy-vs-rent case anyway. It only measures how long the insurance math took.

6. A viewer would probably take away these points:
   - Don't assume the insurance will drop quickly just because prices might rise. Two years matched the typical historical month, not the slow ones, and not a lender's stricter early rules.
   - Treat the legal schedule (about 8 to 9.5 years here) as the dependable worst case, and check your lender's actual removal policy: appraisal, minimum time, and the 75% bar early on.
   - Know that timing and local prices matter a lot, and a national average may not match your market.
   - The video also puts $40,000 more up front for 20% down next to this, but it doesn't tell the viewer which way to go.

### R4
1. The video is for first-time US buyers like me who have saved 10% down. The choice is whether to buy now and pay private mortgage insurance (PMI) or keep renting until I have 20%. It starts with an example: a $400,000 home with a $360,000 loan at 6.86%. On that loan's schedule I could ask to cancel PMI at payment 99, about 8 years in, and it ends on its own at about 9.5 years. Then it replays US home prices for every purchase month from 1991 to 2016 to see how fast rising prices brought the loan to 80% of the home's value "on paper." It finishes with three example buyers (Grace, Owen and Victor) whose results were very different.

2. On the schedule, PMI lasts most of a decade: you can ask to cancel at about 8 years, and it drops off automatically at about 9.5. On paper, the typical purchase month reached 80% loan-to-value in 23 months. 90.6% of months got there no later than the schedule would have. About 1 in 7 took more than 5 years, and the slowest (October 2005) took 112 months. But "on paper" is not the same as having PMI removed. Only 15.6% of months were at or below the 75% bar lenders often use early on, two years after purchase. So the honest answer is "anywhere from about a year to more than 9 years on paper, and actual removal depends on your lender."

3. "On this loan, that's payment 99: the schedule's road from the opening." I couldn't tell what "the schedule's road from the opening" means. It sounds like it points to an on-screen visual I can't see. Also: "That's the road behind the words on paper, with the lender's rules from the opening still in the way." Same problem: the "road" wording is vague, and I had to work out what it was referring back to. And "In a wider set of months, two years after purchase..." made me ask: wider than what? Why is this number from a different set of months than the 23-month figure?

4. "We took every purchase month from January 1991 to July 2016. For each one, we set up the same 10 percent down loan at that month's average rate. And we let the home's value move exactly like the Federal Housing Finance Agency's national index of home purchase prices." This is where my attention dropped. It's method detail, packed in right before the answer I was waiting for, and the agency name is a mouthful.

5. No. It says plainly that it "won't say whether to buy or wait," that it's "history, not a forecast," and that it doesn't weigh the extra $40,000 for 20% down against renting. It doesn't predict prices or rates either. It only measures how long PMI lasted in past data.

6. Don't count on PMI going away in about two years. That only happened in a typical month, and the slow cases took 5 to 9+ years. Removing it based on home value is up to the lender (a request, an appraisal, a minimum time, and possibly a 75% bar), so check your lender's rules before you buy. To be safe, plan your budget assuming PMI lasts until the schedule date (about 8 to 9.5 years). Keep in mind that national averages may not match your local market.

### R5
1. The video is for someone like me, a first-time US buyer with about 10% saved, who is choosing between buying now and paying PMI or renting until I have 20%. It walks through a $400,000 example loan at 6.86% and shows that, going by the payment schedule alone, I could ask to cancel PMI at about 8 years (payment 99), and it would end automatically at about 9.5 years. Then it replays every purchase month from 1991 to 2016 against a national home price index to see how fast rising prices brought the loan to 80% of the home's value on paper. It finishes with three example buyers (Grace, Owen, Victor) who got very different results depending on when they bought.

2. On the schedule, PMI lasts most of a decade: about 8 years until you can ask to cancel and about 9.5 years until it ends automatically. With prices factored in, the typical purchase month reached 80% on paper in 23 months, and 90.6% of months got there no later than the schedule would have. The range was 13 months (Jan 2004) to 112 months (Oct 2005), and about 1 in 7 months took more than 5 years. But "on paper" is not the same as getting PMI removed. Only 15.6% of months were at or below the 75% bar lenders often use early on at the two-year mark, so a plan that counts on about two years matches the typical case, not the slow cases or the lender's actual rules.

3. "On this loan, that's payment 99: the schedule's road from the opening." I didn't know what "the schedule's road from the opening" meant. It sounds like it refers to a visual I can't see. "That's the road behind the words on paper, with the lender's rules from the opening still in the way." This one confused me too: it's abstract and leans on a metaphor and a callback I had to puzzle out. "In a wider set of months, two years after purchase, only 15.6 percent..." Wider than what? I couldn't tell why the set of months changed or what it was. "So a plan of your own has a pair of lines to sit against." Awkward wording, and it took a second to see this was about two comparison benchmarks. I was also briefly thrown by Victor's schedule hitting 80% at payment 90 when the example loan said 99, until I figured his rate was different.

4. "We took every purchase month from January 1991 to July 2016. For each one, we set up the same 10 percent down loan at that month's average rate. And we let the home's value move exactly like the Federal Housing Finance Agency's national index of home purchase prices." This is a dense stretch of method detail just as I wanted the answer, so I drifted until "The typical answer: 23 months."

5. No. It says outright that it "won't say whether to buy or wait" and that it's "history, not a forecast." It only measures how long PMI lasted in the past and leaves out costs, rent, and local prices.

6. Don't plan on PMI disappearing in about two years just because prices usually rise. Plan around the schedule (about 8 to 9.5 years on a loan like the example) as the realistic worst case, and treat early removal based on home value as possible but not guaranteed. It depends on your lender's rules, an appraisal, the 75% bar early on, and your local market. Find out your lender's PMI-removal policy and what PMI would actually cost you before deciding, and weigh that against the extra $40,000 needed for 20% down.

### R6
1. The video is about a hypothetical buyer with 10 percent down on a $400,000 home, facing the choice of buying now with mortgage insurance (PMI) or renting until reaching 20 percent down. It explains the legal schedule for ending PMI (can request at 80 percent of original value, automatic at 78 percent), then replays US history from 1991 to 2016 with the same loan to see how long it took the loan to hit 80 percent of home value on paper. Three buyers (Grace, Owen, Victor) show how timing and price movement changed the outcome. It closes by noting that on paper is not the same as removed.

2. On the schedule alone, the example loan can be cancelled on request at payment 99 (about 8 years) and ends automatically around 9.5 years. In the historical replay, the typical purchase month reached 80 percent on paper in 23 months, 90.6 percent of months got there no later than the schedule would have, and about 1 in 7 took over 5 years. The range was about a year (13 months) to more than 9 years (112 months, October 2005). Lenders' value-based removal has its own rules, so on paper doesn't mean removed.

3. Two passages confused me:
   - "That's the road behind the words on paper, with the lender's rules from the opening still in the way." It's vague and refers back to earlier phrases rather than saying something plain.
   - "The slowest was October 2005: 112 months on paper. That's longer than the schedule itself took at that month's rate." It sits oddly with Victor's story, where his own schedule reached 80 percent at payment 90. The 112 months versus the schedule's 99 (at a different rate) isn't clearly reconciled, and "longer than the schedule" is easy to misread.

4. "Whether a lender would have dropped his insurance at that point, this data can't show." Attention dropped most in the stretch around the lender-rules caveats and the closing "pair of lines" paragraph, where the same caveats repeat. In that paragraph, "So a plan of your own has a pair of lines to sit against." is the most abstract line and the one where I drifted, because it speaks in metaphor instead of stating the takeaway.

5. No. The video says outright that it won't say whether to buy or wait, that it's history and not a forecast, and that it doesn't model PMI cost, rent, local prices, or savings growth. It only measures how long the insurance lasted.

6. Mainly cautionary: don't assume the schedule or a fast price rise will end PMI on a set date. Planning on about two years matched the typical historical month but not slow ones, and not a lender's stricter early bar (75 percent). A viewer would take away that they should check their own lender's removal rules (request, appraisal, minimum time), and that the 20 percent down alternative means $40,000 more up front on the example home.

### R7
1. The video is about someone like me, with 10% saved for a home, weighing whether to buy now and pay mortgage insurance (PMI) or keep renting until reaching 20% down. It uses a $400,000 example home and first shows the legal schedule: you can ask to cancel at about 8 years, and it ends automatically at about 9.5 years. Then it replays every purchase month from 1991 to mid-2016 against the national price index to see how fast the loan hit 80% of value "on paper." Three sample buyers (Grace, Owen, Victor) show how much the start month mattered. It closes by saying it measures how long the insurance lasts and doesn't tell you whether to buy.

2. It doesn't give one number. It gives a range, plus a warning.
- The schedule alone sets the dates when the loan starts. On the example loan, the loan reaches 80% at payment 99 (you can ask to cancel) and 78% at about 9.5 years (automatic).
- On paper, the typical purchase month got to 80% in 23 months. The fastest was 13 months (January 2004) and the slowest was 112 months (October 2005).
- 90.6% of months got there no later than the schedule would have, and about 1 in 7 took more than 5 years.
- Reaching 80% on paper isn't the same as getting the insurance removed. Lenders add their own rules, and only 15.6% of months were at or below 75% by two years.

3. Several passages confused me.
- "On this loan, that's payment 99: the schedule's road from the opening." I don't know what "the schedule's road from the opening" means. It sounds like a callback to the intro, but it reads as a garbled phrase.
- "That's the road behind the words on paper, with the lender's rules from the opening still in the way." This one is also vague. I had to reread it to realize it was just saying "on paper" ignores lender policy.
- "In a wider set of months, two years after purchase, only 15.6 percent were at or below the 75 percent bar." I don't know what the "wider set" is or why it differs from the earlier months.
- The replay only runs to July 2016, and the video never says why it stops there. I wondered whether recent years were excluded on purpose.

4. My attention dropped most here: "Not modeled here: what the insurance costs, appraisal fees, rent, local prices, or how fast savings grow. How we know this: public data from FRED, one loan replayed from every purchase month, and every rule and limit is on this card and in the description." It's a dense list of disclaimers and sourcing right near the end, just when I want the payoff. It also points me to a card and description I can't read while watching.

5. No. It says outright that it "won't say whether to buy or wait," and that it's "history, not a forecast." It doesn't predict home prices or rates. It also doesn't weigh the $40,000 extra down payment against renting or waiting. It only measures how long the insurance math took in the past.

6. The video gives no direct advice, but a viewer could take away a few things.
- Don't count on the fast outcome. About two years matched the typical month, but not the slow ones, and not a lender's stricter early rules.
- Treat the schedule as the dependable benchmark, which on the example is most of a decade.
- "On paper" doesn't mean the insurance is removed, so ask a lender about its removal rules, such as appraisal, minimum time, and the 75% bar.
- Whether you get a fast result depends on when you buy and what prices do next, and that part is mostly luck.
- The cost of the insurance itself still has to be worked out separately.

### R8
1. The video is about a first-time buyer with 10% saved, deciding whether to buy now and pay mortgage insurance (PMI) or rent until they reach 20%. It takes a $400,000 home with a $360,000 loan and shows that the legal schedule only lets you ask to cancel PMI at about 8 years, with automatic removal at about 9.5. It then replays every purchase month from 1991 to 2016 against a national price index to see how fast rising prices got the loan to 80% of the home's value "on paper". Three example buyers (Grace, Owen, Victor) show how much the start month mattered, and it ends by saying on paper is not the same as removed.

2. The answer depends on which measure you use. On the schedule, it's about 8 years (payment 99) to ask to cancel and about 9.5 years for automatic removal, and that's fixed on day one. On paper with price growth, the typical case was 23 months, the fastest was 13 months (Owen), and the slowest was 112 months (Victor, October 2005). About 1 in 7 purchase months took over 5 years. In 90.6% of months, prices got the loan to 80% no later than the schedule would have. Only 15.6% of months were at or below the 75% bar that lenders often use early on at the two-year mark.

3. Several passages confused me:
   - "On this loan, that's payment 99: the schedule's road from the opening." The "road from the opening" callback is vague. I had to guess it means the 8-year line from the intro.
   - "That's the road behind the words on paper, with the lender's rules from the opening still in the way." It's metaphor stacked on a callback, and I couldn't tell what it was telling me.
   - "He got there by paying the loan down, and his own schedule reached 80 percent of the original price first, at payment 90." If the schedule hit 80% at payment 90, why did his on-paper clock stop at 112 months? I eventually worked out that falling prices made the value-based measure slower, but it took effort.

4. "How we know this: public data from FRED, one loan replayed from every purchase month, and every rule and limit is on this card and in the description." My attention dropped here because it's fast, fine-print-style sourcing. It also points to a "card" I can't see in the narration, and by this point I just wanted the conclusion.

5. No. It says outright that it won't say whether to buy or wait, and that it's history, not a forecast. It mentions the $40,000 extra for 20% down but says it isn't weighing that against renting. It also says it doesn't model PMI cost, rent, local prices or savings growth, so I can't compare buying with renting from this alone.

6. The video gives no explicit advice, but I'd take away these points:
   - Don't assume PMI will be gone in about two years just because that was the typical case in the past. The slow cases ran past 9 years, and removal depends on the lender's rules, not the index.
   - Treat the 8 to 9.5 year schedule as the dependable baseline, and treat faster removal as a bonus that depends on prices rising.
   - Before buying, ask the lender how they handle value-based PMI removal: the appraisal, the minimum time, and the 75% bar early on.
   - The month you buy and what prices do next matter a lot, and nobody can control or predict them.

### R9
1. The video is for a US first-time buyer who has saved 10% of a home's price and is deciding whether to buy now and pay private mortgage insurance (PMI) or keep renting until they have 20%. It explains what PMI is and walks through a $400,000 example home with a $360,000 loan at 6.86%. On the standard payment schedule, you can ask to cancel PMI at payment 99, about 8 years in, and it ends automatically at about 9.5 years. It then replays real national home prices for every purchase month from 1991 to 2016 to show how fast rising prices got the loan to 80% of the home's value "on paper." It finishes with three example buyers (Grace, Owen, Victor) to show that the month you buy in drives the result.

2. It depends on which clock you use. On the schedule alone, you can ask to cancel at about 8 years and PMI ends automatically at about 9.5 years on the example loan. On paper, using the national price index, the typical purchase month reached 80% loan-to-value in 23 months, and 90.6% of months got there no later than the schedule. About 1 in 7 months took more than 5 years, and the worst, October 2005, took 112 months. The range ran from about a year (13 months) to more than 9 years. Reaching 80% on paper is not the same as getting PMI removed. Lenders need a request, an appraisal and a minimum time, and early on they often use a 75% bar. Only 15.6% of months were at or below 75% after two years.

3. Three things confused me.
- "On this loan, that's payment 99: the schedule's road from the opening." I couldn't tell what "the schedule's road from the opening" meant. I guess it points back to the "about 8 years" line, but it reads like a leftover script note.
- "That's the road behind the words on paper, with the lender's rules from the opening still in the way." Same problem: abstract wording that points back to earlier lines instead of saying something plainly.
- "In a wider set of months, two years after purchase..." Wider than what? Which months, and why is it a different set from the 23-month replay? I also wasn't sure why Victor's schedule hit 80% at payment 90 when the example loan took 99. I assume his rate was lower, but the video doesn't say so.

4. "We took every purchase month from January 1991 to July 2016. For each one, we set up the same 10 percent down loan at that month's average rate. And we let the home's value move exactly like the Federal Housing Finance Agency's national index of home purchase prices." This method description is dry, and I just wanted the result. The "Not modeled here..." list near the end also felt like fine print.

5. No. It says outright that it won't say whether to buy or wait, and that it's "history, not a forecast." It only measures how long PMI lasted in the past. It also doesn't weigh the extra $40,000 needed for 20% down against renting or waiting.

6. Don't count on dropping PMI in about two years. That matched the typical month in a rising market, not the slow cases, and it ignores the lender's appraisal and 75% rules. The safe baseline is the schedule, roughly 8 to 9.5 years at today's rates. Faster removal depends on local prices rising and on your lender's policy. Check that policy (request process, appraisal, minimum time, the loan-to-value bar) before relying on it, and budget for PMI possibly lasting most of a decade.
