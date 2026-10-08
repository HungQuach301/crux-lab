# Grading packet (blind). You are an independent grader. Each label is one reader's answers to fixed questions about a text. Grade each label literally with the rubric. You know nothing else.

## Rubric
**Chấm (người chấm độc lập headless, mù tập):**
- (Q) câu hỏi: với 10 % trả trước, bảo hiểm thế chấp (PMI) kéo dài bao lâu / mua ngay trả PMI hay thuê tiếp tới 20 %.
- (A1) đáp án: theo lịch trả nợ ≈ 8 năm tới 80 %; theo lịch sử giá nhà Mỹ, thường (trung vị) ≈ **23 tháng / khoảng 2 năm** để chạm 80 % "trên giấy".
- (A2) ít nhất một: "trên giấy" ≠ được gỡ bảo hiểm (quy định bên cho vay: yêu cầu, thẩm định, thời gian tối thiểu, mốc 75 %); khoảng 1/7 mất hơn 5 năm / trường hợp chậm (10/2005, 112 tháng); ba người mua khác nhau theo năm mua.
- Đủ Q + A1 + A2 → 1; thiếu một → 0,5; ≤ một → 0. Khẳng định sai nghĩa ("PMI của bạn sẽ hết sau 2 năm", "luật gỡ PMI ở 80 % giá trị hiện tại") → 0.
- `advice: true` khi câu 5 "yes" vì tin video bảo mua/chờ hay dự báo, **hoặc** câu 6 nêu lời khuyên hành động như chỉ thị (mua ngay, chờ 20 %, xin gỡ PMI sau 2 năm…). Câu 6 "so kế hoạch với dải lịch sử / đừng chỉ dựa vào lịch trả nợ / hỏi bên cho vay quy định của họ" nói như hiểu biết, không mệnh lệnh mua/chờ → không tính.
- Người đọc **đúng** = điểm 1 và không câu khuyên.



Output JSON only (no prose, no code fence): {"R1": {"score": 1|0.5|0, "advice": true|false, "why": "<one line>"}, ...}

### R1
1. The video is about someone with 10% saved for a home, weighing buying now with mortgage insurance (PMI) against waiting for 20% down. It sets up a $400,000 home with a $360,000 loan and shows that, by the legal schedule alone, you can request cancellation at about 8 years, and it ends automatically at about 9.5 years. It then replays US prices and rates from 1991 to 2016 to see how fast rising prices got the loan to 80% "on paper." It closes with three example buyers (Grace, Owen, Victor) whose results differed because of when they bought, and it says outright that it won't tell you whether to buy or wait.

2. The video's answer is that it depends on the benchmark. On the schedule, it's set on day one: request at payment 99 (about 8 years) and automatic end at 78% (about 9.5 years). On paper in the replay, the typical case reached 80% in 23 months, and 90.6% of purchase months got there no later than the schedule would have. The range ran from 13 months (Owen, January 2004) to 112 months (Victor, October 2005). About 1 in 7 months took more than 5 years. It also says that reaching 80% on paper isn't the same as getting the insurance removed, since lenders add requests, appraisals, minimum times, and often a 75% bar early on. Only 15.6% of purchases were at or below 75% two years in.

3. Nothing was truly confusing, but a couple of things were slippery:
   - "He got there by paying the loan down, and his own schedule, at his lower rate of 6.07 percent, reached 80 percent of the original price first, at payment 90." I had to stop and work out that the on-paper date (112 months) and his schedule date (90 payments) are different measures, and that the schedule came first. It's also odd that "lower rate" comes right after the 6.86% example rate, so I wasn't sure what it was lower than.
   - The example uses "September's average rate" with no year, while the replay ends in 2016. That left me unsure how current the example is.

4. "The other is history on paper: a plan that counts on about two years matched the typical month, not the slow ones, and not the lender's step." My attention dropped here. It packs three comparisons into one sentence, with "history on paper" and "the lender's step" as jargon I had to decode. It arrives after a lot of numbers, so I was already tired.

5. No. The video says it "won't say whether to buy or wait" and that it's "history, not a forecast." It never predicts home prices or rates, and it never weighs the extra $40,000 for 20% down against renting or waiting. It only measures how long the insurance math took.

6. The video gives no explicit advice, but a viewer would probably take away these points:
   - Don't assume PMI will be gone in about 2 years. That was typical on paper, but it depended on prices rising, and it wasn't a safe bet.
   - The only firm timeline is the schedule: about 8 years to request cancellation and about 9.5 years for automatic removal.
   - "80% on paper" isn't removal. Ask a lender about its removal rules, such as appraisal, minimum time, and any 75% bar.
   - Buying right before a price slump can stretch things well past 5 years.

### R2
1. The video is about a first-time buyer with 10% saved who is deciding between buying now with private mortgage insurance (PMI) or renting until 20% down. It doesn't try to settle that choice. It measures how long PMI lasts on an example $360,000 loan, first by the legal schedule (about 8 years to request cancellation, about 9.5 to automatic termination). It then replays 1991-2016 purchase months against a national price index, to see when the loan hit 80% of the home's value "on paper." Three example buyers (Grace, Owen, Victor) show how the start month changed the answer.

2. The answer depends on which clock you use. On the schedule, cancellation can be requested at payment 99 (about 8 years) and is automatic at 78% (about 9.5 years). On paper with rising prices, the typical wait was 23 months, and the range ran from 13 months (January 2004) to 112 months (October 2005). About 1 in 7 purchase months took more than 5 years, and prices got there no later than the schedule in 90.6% of months. "On paper" still isn't removal: lenders require a request, an appraisal, a minimum time, and early on a 75% bar. Only 15.6% of purchase months were at or below 75% two years in.

3. The passage that confused me most: "Her loan reached 80 percent on paper right at the middle of the replay: she is the typical case from before. Her own schedule would have taken several years longer." "The middle of the replay" is vague, and I had to work out that it means the median, 23 months. I also stumbled on "That's the gap between the schedule's long road and the replay's typical one." It's clear in the end, but "on paper" and "the schedule" are easy to mix up at first.

4. My attention dropped most here: "Every month after that, we compare the balance with the value, and stop the clock the first time the loan is 80 percent or less." It's a run of method steps with no number or example to hold onto. It comes right after the more concrete payment and schedule section.

5. No. The video says outright that it "won't say whether to buy or wait," and that it is "history, not a forecast." It doesn't weigh PMI against renting, and it gives no dollar figure for PMI. It mentions $40,000 more up front for 20% down but explicitly declines to weigh it.

6. The video gives no explicit advice, but a viewer could reasonably take away a few things:
   - Don't assume PMI will be gone in about 2 years. That matched the typical month, not the slow ones, and not a lender's early bar.
   - Treat the legal schedule (roughly 8 to 9.5 years) as the safe baseline, and anything faster as a bonus that depends on prices.
   - Ask a lender about its rules for removing PMI based on value, including the appraisal, minimum time, and 75% bar.
   - Remember that this is national-average history, and a local market could do much better or worse.

### R3
1. The video is about a first-time buyer, in my position, with 10% saved who is deciding whether to buy now with mortgage insurance (PMI) or keep renting until they have 20%. It works through a $400,000 home with a $360,000 loan at 6.86%. The law-based schedule lets you request cancellation at payment 99 (about 8 years) and forces it to end at about 9.5 years. It then replays every purchase month from 1991 to 2016 against a national price index to see how fast rising prices got the loan to 80% "on paper". Three example buyers (Grace, Owen and Victor) show why the answers ranged so widely.

2. The video's answer is that it depends on the schedule versus price history. On the schedule alone, you can ask to cancel at about 8 years (payment 99) and it ends automatically at about 9.5 years. With prices counted, the typical purchase month reached 80% on paper in 23 months, and 90.6% got there no later than the schedule. The range ran from 13 months (the fastest, January 2004) to 112 months (the slowest, October 2005), and about 1 in 7 months took more than 5 years. Reaching 80% on paper is not the same as getting the insurance removed. Only 15.6% were at or below 75%, the bar lenders often use early on, after two years.

3. I was confused by this passage: "The slowest was October 2005: 112 months on paper. That's longer than the schedule itself took at that month's rate." Victor's schedule hit 80% at payment 90, but the on-paper figure is 112 months. It took me a moment to see that falling prices pushed the value-based clock past the schedule, because the schedule uses the original value. Also, Grace gets no month count, only "right at the middle", so I had to connect that to the 23 months myself.

4. My attention dropped most here: "So a plan can be measured against two benchmarks from this history." It's abstract, it comes right after the three stories, and it restates things I already had, so it felt like a recap in jargon rather than something new.

5. No. The video says outright that it won't say whether to buy or wait, and that it's "history, not a forecast". It doesn't predict prices or rates. It only notes that 20% down on the example home means $40,000 more up front, and it explicitly doesn't weigh that against renting or waiting.

6. The video gives no direct advice, but a viewer could take these points:
- Don't assume the insurance will be gone in about 2 years just because that was the typical case. It was typical, not guaranteed, and a bad start month can take many years.
- Treat the legal schedule (request at about 8 years, automatic at about 9.5) as the dependable baseline.
- Price-based removal depends on lender policy (request, appraisal, minimum time, often a 75% bar early on), so ask the lender about those rules before buying.
- Remember that "on paper" is not "removed", and that a national average doesn't describe a local market.

### R4
1. The video is for someone like me, a renter with 10 percent saved who is deciding whether to buy now with mortgage insurance (PMI) or keep renting until 20 percent. It doesn't answer that. It asks how long the insurance lasts. It uses a $400,000 home with a $360,000 loan to show that the legal schedule lets you request cancellation at payment 99 (about 8 years) and forces it to end at about 9.5 years. Then it replays real prices and rates from 1991 to 2016 to see how fast rising prices got buyers to 80 percent "on paper", and it uses three buyers (Grace, Owen, Victor) to show how much the starting month mattered.

2. The video doesn't give a single answer. On the schedule, cancellation can be requested at about 8 years (payment 99) and is automatic at 78 percent, about 9.5 years in. On paper, the typical purchase month reached 80 percent in 23 months, the fastest took 13 (Owen, January 2004), and the slowest took 112 (Victor, October 2005). About 1 in 7 took more than 5 years. On paper isn't the same as the insurance actually being removed, since lenders require a request, an appraisal and a minimum time, and early on a 75 percent bar. Only 15.6 percent of purchase months were at or below that bar after two years.

3. "On this loan, that's payment 99, the date this video opened with." I had to think back to "about 8 years" in the opening, and the video never says that 99 payments is about 8.25 years. I was also briefly confused by "That's longer than the schedule itself took at that month's rate." It took me a moment to see how a value-based measure could be slower than the schedule. The Victor section explains it (prices fell, so the loan had to reach 80 percent of a lower value), but the earlier line lands without that explanation.

4. "The other is history on paper: a plan that counts on about two years matched the typical month, not the slow ones, and not the lender's step." This is where my attention dropped. It's a dense, abstract sentence in the wrap-up, and it packs three comparisons (typical month, slow months, lender's step) into one clause. Earlier, the "we compare the balance with the value, and stop the clock" methodology stretch was also dry, but I could follow it.

5. No. The video says it won't say whether to buy or wait, and it says "This video doesn't weigh that against renting or waiting." It also says repeatedly that it's history, not a forecast, so it predicts neither home prices nor mortgage rates. It even avoids a dollar figure for PMI, so I can't compare PMI against waiting to reach 20 percent.

6. A viewer would take away a few cautions:
   - Don't count on a quick PMI exit just because prices might rise. The two-year outcome was typical but not guaranteed, and some buyers waited most of a decade.
   - Treat the legal schedule (about 8 to 9.5 years here) as the baseline, and treat faster removal as a bonus.
   - Reaching 80 percent on paper isn't removal, so ask a lender about its value-based removal rules (appraisal, minimum time, the 75 percent early bar) before relying on it.
   - Compare the extra up-front cost of 20 percent down ($40,000 on the example) with the length of time you'd pay PMI. The video leaves that comparison to me.

### R5
1. The video is about a first-time buyer with 10 percent saved who is deciding whether to buy now and pay mortgage insurance (PMI) or rent until reaching 20 percent. It doesn't pick a side. It measures how long the insurance lasts on a $400,000 example home with a $360,000 loan. First it shows the legal schedule: you can request cancellation at payment 99 (about 8 years), and it ends automatically at about 9.5 years. Then it replays US prices and rates from 1991 to 2016 to see how fast rising prices got the loan to 80 percent "on paper." Three buyers (Grace, Owen, Victor) show how much the start month mattered.

2. The answer depends on which benchmark you use. On the schedule, it's about 8 years to request cancellation and about 9.5 to automatic termination, set the day the loan starts. On paper in the history replay, the typical case was 23 months, the fastest was 13 months, and the slowest (October 2005) was 112 months, a bit over 9 years. About 1 in 7 purchase months took more than 5 years. Reaching 80 percent on paper is not the same as getting the insurance removed. Lenders add requests, appraisals, minimum time, and early on a 75 percent bar. Only 15.6 percent of purchase months hit that bar within two years.

3. "Her loan reached 80 percent on paper right at the middle of the replay: she is the typical case from before." It's a little confusing because the typical case was 23 months, and the video never says Grace's month count, so I had to infer it. Also: "He got there by paying the loan down, and his own schedule, at his lower rate of 6.07 percent, reached 80 percent of the original price first, at payment 90." That's a lot of ideas in one sentence. Why "lower rate" matters, and how it fits with "112 months," took me a second.

4. "We also checked a larger set: every purchase month since January 1991 with two years of prices after it." My attention dropped here because the video switches to a different group of months (a different denominator) right after the headline number. I wasn't sure how it related to the 90.6 percent figure, and the numbers felt like they were piling up.

5. No. The video says outright that it won't say whether to buy or wait, and that it's history, not a forecast. It puts no dollar figure on PMI and doesn't weigh the extra $40,000 for 20 percent down against renting. It only measures how long the insurance math took.

6. The video gives no explicit advice, but a viewer would probably take away a few points:
   - Plan around the schedule (roughly 8 to 9.5 years) rather than assuming prices will remove PMI quickly.
   - A plan that counts on about two years matched the typical month in this history, not the slow ones, and not a lender's stricter early rule.
   - "On paper" doesn't mean removed, so ask your own lender about its removal policy, appraisal, and waiting period.
   - Local markets and your start month can change the outcome a lot.

### R6
1. The video is about a would-be buyer with 10 percent saved, deciding whether to buy now and pay mortgage insurance (PMI) or rent until reaching 20 percent. It doesn't try to settle that decision. It measures how long PMI lasts on an example $400,000 home with a $360,000 loan. First it walks through the legal schedule: you can ask to cancel at payment 99, and it ends automatically at about 9.5 years. Then it replays every purchase month from 1991 to 2016 against a national price index to see when the loan reached 80 percent of value "on paper." Three illustrative buyers, Grace, Owen and Victor, show why the answers varied so much.

2. The answer depends on which clock you use.
   - **Schedule:** the earliest you can ask to cancel is about 8 years (payment 99), and automatic removal comes at about 9.5 years. This is fixed when the loan starts.
   - **History on paper:** the typical purchase month reached 80 percent in 23 months, and the range ran from 13 months (Owen) to 112 months (Victor, October 2005).
   - **Tail and caveats:** about 1 in 7 months took over 5 years, and 90.6 percent reached 80 percent no later than the schedule would have. Reaching 80 percent on paper is not the same as the insurance being removed. Only 15.6 percent of months were at or below 75 percent after two years, a bar lenders often use early on.

3. The passage that confused me is: "He got there by paying the loan down, and his own schedule, at his lower rate of 6.07 percent, reached 80 percent of the original price first, at payment 90."
   - It mixes two clocks, the schedule on original value and the on-paper test against the index.
   - It sits next to the earlier line that his on-paper time was 112 months, so I had to work out that 90 is the schedule and 112 is the index-based result.
   - "Lower rate" is also relative to the 6.86 percent example, which I'd half forgotten.

   Smaller stumbles: "payment 99, the date this video opened with" (the opening said "about 8 years"), and the 75 percent bar being mentioned early and only explained much later.

4. My attention dropped most at: "We also checked a larger set: every purchase month since January 1991 with two years of prices after it. Two years after purchase, only 15.6 percent of them were at or below the 75 percent bar that lenders often use early on." It switches to a different data set and a new threshold right after the headline 23-month result. It also adds another percentage to a stretch that already had several. The methodology paragraph just before it ("We took every purchase month...") was a close second.

5. No. The video says outright that it won't say whether to buy or wait, and that it's "history, not a forecast." It also puts no dollar figure on PMI cost, so it can't compare buying with renting. It mentions the $40,000 extra for 20 percent down but says it doesn't weigh that against renting or waiting. It doesn't predict prices or rates either. The replay uses past index movements and rates, and the video repeatedly stresses that one national average doesn't predict any single home or market.

6. The video gives no explicit advice, but a viewer could take away these points:
   - Don't assume PMI will vanish in about two years. That matched the typical historical month, not the slow ones, and not a lender's actual removal rules.
   - The legal schedule on a 10-percent-down loan means roughly 8 to 9.5 years, so a plan should hold up on that benchmark.
   - Rising prices can speed things up, but falling or flat prices can leave you waiting a long time.
   - Ask your lender about its removal policy (request, appraisal, minimum time, any 75 percent early bar), because "on paper" isn't "removed."
