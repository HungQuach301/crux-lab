# Grading packet (blind). Independent grader. Each label is one reader's answers about one silent 6-frame strip; the strip id is given so you compare against its muted read. Grade literally.

## Rubric
- **Chấm:** người chấm độc lập mù tập; nghĩa 1 / 0,5 / 0 so với "muted read" của `review-c3/spans.json`; cờ khuyên theo **A9** (thận trọng chung — tự kiểm số, hỏi bên cho vay — không tính; khuyên mua/chờ/bán/chọn tính). Người đọc đúng = nghĩa 1 và khuyên_tính false.


Muted read (đáp án đúng) theo hình — mỗi nhãn ghi hình nào ở mục 'sample':
- N1-calendar: Each page of the calendar is one monthly payment ($2,362/month, principal + interest, illustrative); as the pages flip, the loan stack slides along the payments and its top draws the balance: it falls slowly at first and faster later.
- N3-fold: One buyer's calendar stops when the loan stack reaches the 80% mark on the home's value; then every purchase month's line folds into a bar standing at its purchase month, and the bar's height is how many months that month took to reach 80% on paper.
- N2-bars: Back on the grid, the bars over 60 months turn warn; they are few (about 1 in 7), and they sit together in one stretch of purchase months (2005–2009), under the part of the national price index that peaks and falls.

Output JSON only: {"R1": {"score": 1|0.5|0, "advice": true|false, "caution_only": true|false, "why": "<one line>"}, ...}

### R1 (strip N1-calendar)
1. **The idea:** The animation shows how a 30-year fixed mortgage is paid off. The example is a $360,000 loan at 6.86%, which the frames label as the September 2026 average rate from Freddie Mac via FRED. The monthly payment is $2,362, covering principal and interest. The frames are marked "illustrative," so they show a general pattern and not a prediction for any one loan.

2. **What changes:** Frame 1 shows a house, a person, a calendar page and a tall stack of cash. Frame 2 shrinks the scene and labels the stack as the $360,000 loan. Frame 3 adds the $2,362 monthly payment and a timeline running from 0 to 360 payments. In frames 4 to 6, the calendar page flips as payments are made (payment 75, then 181, then 346). The stack of cash shrinks as this happens. A curve traces the loan balance. It falls slowly at first and then drops faster later. By payment 346 the stack is nearly gone.

3. **What it means:** Early payments are mostly interest, so the balance barely falls for the first several years. Each payment is the same size, but the share going to principal grows over time. That is why the balance falls faster in the later years. By payment 75, about 6 years in, the stack has shrunk only a little.

4. **Advice a viewer would take:**
   - Don't expect to build equity quickly in the first years of a mortgage. Selling or refinancing early leaves you with little principal paid down.
   - Budget for the full $2,362 a month, and stay in the home long enough for the principal paydown to speed up.
   - Extra payments made early cut the principal sooner, so they save more interest than extra payments made late.
   - The video doesn't state any of this advice, so these takeaways are my inference from the shape of the curve.

I've assumed that a viewer like me, a renter with about 10% saved, would see this as a reminder that the monthly cost and slow early equity matter as much as the down payment.

### R2 (strip N1-calendar)
1. **The idea.** The animation shows how a 30-year fixed mortgage gets paid off. The example is a $360,000 loan at 6.86%, which the frames give as the September 2026 average rate from Freddie Mac via FRED. The monthly payment is $2,362, covering principal plus interest. The frames are labeled "illustrative," so this is a worked example and not a quote for any real person.

2. **What changes.** Frame 1 shows a house, a person, a calendar page, and a tall stack of cash. The stack stands for the loan. In frame 2 the picture shrinks to the calendar and the $360,000 stack. Frame 3 adds the $2,362 monthly payment. In frames 4 to 6 a timeline runs from 0 to 360 payments, and the calendar page flips as payments go by (payment 75, then 181, then 346). The stack shrinks along a curve labeled "loan balance · on the schedule." The curve falls slowly at first and then drops steeply, labeled "faster later." By payment 346 only a small stub of cash is left.

3. **What it means.** The monthly payment stays the same, but its makeup changes. Early on, most of each payment goes to interest, so the balance barely falls. Later, most of it goes to principal, and the balance falls quickly. After 75 payments, about 6 years, the balance has only dropped a modest amount. Most of the paydown comes in the last stretch of the loan.

4. **Advice a viewer would take.**
   - The video doesn't give explicit advice, but the implied lessons are practical. Don't expect to build equity quickly in the first several years.
   - Selling or refinancing early means you've mostly paid interest and owe most of the loan.
   - Budget for the full $2,362 a month, and remember that taxes, insurance, and upkeep come on top of it.
   - As a renter who has saved about 10%, I'd take away that a home is a long-term commitment. It makes the most sense if I expect to stay many years.
   - Extra principal payments early would help more than later ones, though the animation doesn't say that directly.

### R3 (strip N3-fold)
1. **The idea.** The animation shows how long it took past US homebuyers to get their loan down to 80% of their home's value. That is the point where a buyer with a small down payment has built about 20% equity "on paper." It uses a house, a loan tower, and a notepad as an illustration. It then switches to real data from FHFA and Freddie Mac via FRED.

2. **What changes across the frames.**
   - Frames 1–2 are labeled "illustrative." A tall "home value" tower sits next to a shorter "loan" tower, and the loan tower gets a glow.
   - Frame 3 is a 3D ridge of lines. Each line is one purchase month from 1991 to 2016. It plots loan as a percentage of home value over 10 years, with 80% as the reference line.
   - Frames 4–6 flatten that into a bar chart. Each bar is a purchase month, and its height is the number of months it took to reach 80%. The bars are low (quick) for 1990s buyers and shrink further toward the early 2000s. They jump sharply for buyers around 2005–2007, then fall back through the 2010s. Frame 6 adds a bracket marking that bar height as "months to 80% on paper."

3. **What it means.** Time to reach 80% loan-to-value varies a lot depending on when you bought. Buyers in the late 1990s and early 2000s got there fast, mostly because prices rose. Buyers near the mid-2000s peak waited much longer because prices fell and their equity stalled. The timing of your purchase and the housing market's path affected equity as much as your own payments did.

4. **What a viewer would take from it.** The slide's own captions say it is "past buyers, measured," "not a reason to buy, rent or wait," and "history, not a forecast," and that it covers the US only. So the animation gives no buy-or-wait advice. A viewer might take away two things:
   - Don't assume a small down payment will reach 20% equity on a set schedule. It could take a few months or many years.
   - Expect that building equity depends partly on market timing you can't control. A first-time buyer with about 10% down should plan for the slow case, for example by keeping a cash cushion and not counting on price gains. They should also check what removing mortgage insurance would take in their own situation.

### R4 (strip N3-fold)
1. **The idea:** The animation shows how long past US home buyers took to get their loan down to 80% of their home's value. It measures this "on paper", meaning by the numbers, using home value and loan balance. The first two frames are an illustration, marked "ILLUSTRATIVE". They show a house with a "home value" tower, a smaller "loan" tower and a ledger pad. The later frames use real data, sourced to FHFA and Freddie Mac via FRED.

2. **What changes across the frames:**
   - Frames 1 and 2 are the same cartoon, with the loan tower highlighted in frame 2.
   - Frame 3 is a 3D ridge chart. It has one line per purchase month from 1991 to 2016, showing loan as a percentage of home value over 0 to 10 years.
   - Frames 4 to 6 flatten that into a bar chart, with one bar per purchase month. Each bar's height is the months it took to reach 80%.
   - Frame 6 adds labels for the years and for what bar height means.

3. **What it means:** The wait to reach 80% varied a lot depending on when someone bought.
   - Buyers from the early 1990s through the early 2000s mostly had short bars.
   - Buyers from roughly 2005 to 2007 have the tallest bars. Their waits were much longer, most likely because home prices fell after they bought.
   - Bars drop back down for later purchase months.
   - The takeaway is that timing and the market affected how quickly buyers built a cushion. It was not only a matter of how fast they paid down the loan.

4. **Advice a viewer would take:** Very little that is direct, and that seems intentional. The captions say "Past buyers, measured · not a reason to buy, rent or wait" and "US only · history, not a forecast." A viewer would take away that building equity isn't guaranteed or steady, and that the wait could be short or very long. As someone with about 10% saved, I'd read it as a reason to leave room in my budget for a long wait. The chart doesn't tell me whether to buy now or hold off.

### R5 (strip N2-bars)
1. The animation shows that the time it takes a home buyer to get back to 80% loan-to-value ("80% on paper") has a long tail. For most purchase months the wait is short, under the 60-month line. For people who bought in one stretch, it took much longer. The data come from FHFA and Freddie Mac via FRED. The label says 14.7% of purchase months, about 1 in 7, took more than 60 months.

2. The first two frames are a 3D view. The bars start out all gray, with a "typical" line running along them. The camera then turns, and a tall orange block of bars stands far above the line, labeled "a long tail." Frames 3 and 4 flatten this into a 2D chart. Each bar is a purchase month from 1991 to 2016. The orange bars are the months that took more than 60 months, and they cluster around 2005 to 2008. Frame 5 labels that cluster "one stretch" and adds a blue line at the top. Frame 6 fills in that line as the national home price index. It rises through the mid-2000s, dips, then recovers.

3. For most buyers across these years, the wait was well under five years. But people who bought near the peak of the mid-2000s market, just before prices fell, waited much longer. The long wait was concentrated in that one stretch. It wasn't spread evenly across all buyers. The blue price line suggests why. Prices rose, then fell, and buyers who got in near the top had their equity wiped out. Timing and the price cycle drove the outcome far more than anything the individual buyer did.

4. The video says outright that this is not a reason to buy, rent, or wait. The footer reads "Past buyers, measured · not a reason to buy, rent or wait," and "US only · history, not a forecast." As someone with about 10% saved, I'd take away a few things:
   - Buying with a small down payment can leave you with little equity for years if prices fall. So don't count on being able to sell or refinance on a short timeline.
   - Most past buyers did fine, but a meaningful minority (about 1 in 7) didn't. Plan to stay put long enough to ride out a bad stretch, and keep an emergency fund so you aren't forced to sell.
   - The data can't tell me whether now is a good time. It only describes how past buyers fared.

### R6 (strip N2-bars)
1. **The idea.** The animation shows how long it took past US home buyers to get from their small down payment to 80% ownership "on paper", meaning 20% equity. Each bar is one purchase month from 1991 to 2016. Most bars are short, but one cluster is very tall. That cluster is the "long tail", a stretch of buyers who waited much longer than usual.

2. **What changes across the frames.**
   - Frames 1 and 2 show the bars as a 3D wall with a "typical" line running along it. The camera turns until the tall orange block stands out.
   - Frames 3 and 4 flatten the chart into a 2D bar chart with a year axis. A 60-month line is added, along with the label "more than 60 months: 14.7% (about 1 in 7)".
   - Frame 5 adds a blue line above the chart and labels the orange bars "one stretch".
   - Frame 6 completes the blue line. It is labeled as a national home price index, and it is flat to slightly rising up to the mid-2000s, then dips and recovers.

3. **What it means.** Most buyers reached 80% equity fairly quickly, but about 1 in 7 needed more than five years. Those slow buyers are not spread randomly through the period. They are mostly people who bought in a single stretch, roughly 2004 to 2008. The price-index line suggests why: prices peaked and fell around then, so those buyers' equity stalled or went backwards. The wait depended heavily on when you bought, not just on how much you put down.

4. **What a viewer would take from it.**
   - The animation gives no explicit advice. The footer says it is "Past buyers, measured · not a reason to buy, rent or wait," and "history, not a forecast."
   - With about 10% down, I'd take away that building equity can take much longer than expected if prices stall right after you buy.
   - So I'd plan to stay put for many years and keep a cash cushion. I wouldn't count on a quick path to 20% equity.
   - I wouldn't treat it as a signal to buy now or to wait. It describes US buyers in the past and doesn't predict anything.
