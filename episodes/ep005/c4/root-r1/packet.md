# Grading packet (blind). Independent grader. Each label is one reader's answers about one silent 6-frame strip; the strip id is given so you compare against its muted read. Grade literally.

## Rubric
- **Chấm:** người chấm độc lập mù tập; nghĩa 1 / 0,5 / 0 so với "muted read" của `review-c3/spans.json`; cờ khuyên theo **A9** (thận trọng chung — tự kiểm số, hỏi bên cho vay — không tính; khuyên mua/chờ/bán/chọn tính). Người đọc đúng = nghĩa 1 và khuyên_tính false.


Muted read (đáp án đúng) theo hình:
- B02-S02: The loan, as a share of the price, starts at 90 % and drifts down slowly; it only touches the 80 % line after about 8 years.
- B03-S03: Hitting the 80 % line on paper is one line; a second, lower line (75 %, early years) and three steps (request, appraisal, wait) still stand before 'insurance removed'.
- B07-S07: On the same falling line, a first marker sits where the loan reaches 80 % of the original price, at payment 99: 'you may ask'.
- B08-S08: A second marker a little later, at 78 %: 'ends automatically'. Both markers sit on the payment line; the house's value is nowhere on the chart.
- B11-S11: Most purchase months have short bars; a horizontal median line sits low at 23 months, far below a faint ridge of the schedule's own months; nearly every bar ends below its schedule mark.
- B12-S12: Two years in, a little more than half the months are under the 80 % line, but only a thin slice is under the 75 % line lenders often use early.
- B13-S13-N2: Back on the grid, the bars over 60 months turn `warn`; they are few, and they sit together in one stretch of purchase months.
- B14-S14: The zoom frame lands on the tallest bar: bought October 2005, 112 months on paper, taller than that month's schedule mark.
- B16-S16: Owen's panel: the index line climbs steeply, and his on-paper line drops through 80 % almost at once, while his schedule line has barely moved.
- B17-S17: Victor's panel: the index line rises a little, then falls for years; his on-paper line stays above 80 % long after his schedule line has crossed it at payment 90.
- B18-S18: Three panels side by side, aligned at purchase: one fixed schedule band and a fan of on-paper lines from fast to slow; a blank card labelled 'your plan' slides between the schedule band and the fan; the 75 % line stays visible under all of them.
- N1-S06: Each page of the calendar is one monthly payment ($2,362/month, principal + interest, illustrative); as the pages flip, the loan stack slides along the payments and its top draws the balance: it falls slowly at first and faster later.

Output JSON only: {"R1": {"score": 1|0.5|0, "advice": true|false, "caution_only": true|false, "why": "<one line>"}, ...}

### R1 (strip B14-S14)
1. **The idea.** The animation shows how long past home buyers actually took to pay off their mortgages, using buyers from different starting months. The October 2005 buyers are the example. Their payoff took 112 months (9 years 4 months). A mortgage on paper at that rate would take 90 payments. The source is FHFA and Freddie Mac data via FRED. The animation says repeatedly that this is US-only history and not a forecast.

2. **What changes over time.**
   - In frames 1–3, a bar chart of many thin bars is already drawn. One bar is highlighted with a white marker at October 2005. The label "on paper" appears in frame 2. In frame 3, a note appears, "schedule at that rate: 90 payments", along with an "ILLUSTRATIVE" tag.
   - In frames 4–6, the scene changes to a row of small houses with a blue line running through them. The caption reads "national average, not one home". The houses' heights shift from frame to frame. Some grow taller and some shrink, while the line stays roughly flat. This suggests individual homes vary around the national average.

3. **What it means.** The chart looks like the time it took past buyers to reach some milestone, probably break-even or recovering their costs. The time varies a lot depending on when someone bought. Buyers near the 2005 peak waited much longer than a simple schedule would suggest. The "on paper" and "schedule" labels point to a gap between the theoretical payoff or break-even and what happened in practice. The house scene adds that these are national averages. A single home can do much better or worse than the average.

4. **What a viewer would take from it.**
   - Timing and local conditions matter a lot, so don't assume a simple schedule will play out.
   - Buying should be planned around a long holding period, since the 2005 buyers needed more than nine years.
   - The on-screen text says outright that this is not a reason to buy, rent or wait. The animation isn't telling anyone to act. It tells them to be realistic about how long it can take and to remember that their own house may differ from the average.

I can't tell from the image alone exactly what the bars measure. My reading of them as time to break even is an inference.

### R2 (strip N1-S06)
1. **The idea.** The animation shows how a $360,000 mortgage works at the September 2026 average rate of 6.86% (Freddie Mac, via FRED). The monthly principal-and-interest payment is $2,362. That payment doesn't include taxes, home insurance and PMI. The loan balance then follows a schedule that is fixed on day one. A badge marks the whole thing as "illustrative."

2. **What changes across the frames.**
   - Frame 1 shows only a small building and a tall tower labeled "$360,000 loan."
   - Frame 2 adds the 6.86% rate.
   - Frame 3 adds the $2,362/month principal-and-interest figure, with a line pointing to the small building.
   - Frame 4 adds a warning that taxes, home insurance and PMI come on top of that payment.
   - Frames 5 and 6 switch to a curve of the loan balance over 360 payments. In frame 5 the tower is still near its starting height at payment 35. By payment 114 in frame 6, the curve has only started to fall, and the labels say "slowly at first" and "faster later."

3. **What it means.** A big loan at today's rate gives a payment of over $2,300 a month before any extras, so the real monthly cost is higher. Early on, most of each payment goes to interest. The balance barely shrinks in the first several years, and the pace picks up only in the later years of the 30-year term. The schedule is set when you sign. The footer, "A measurement, not a next step," says the video is showing a calculation and isn't telling you to buy.

4. **What a viewer would take away.**
   - Budget for the full monthly cost: principal and interest plus taxes, insurance and PMI. Don't budget for just the $2,362.
   - Don't expect to build equity quickly. Early payments mostly cover interest, so you'd be building equity slowly for years. That matters if you might move within 5 to 10 years.
   - The rate drives the payment. Today's 6.86% is a snapshot, and it affects what you can afford.
   - The video gives no explicit instruction. The advice is to understand the real cost and the slow payoff before deciding.

For me in particular, with about 10% saved, a down payment that small probably means PMI. That puts my real monthly cost above $2,362, so I'd want to run the full numbers before treating this as affordable.

### R3 (strip B13-S13-N2)
1. **The idea.** The animation shows that for most US home buyers, the home's price was "paid back" in a fairly typical amount of time. A minority who bought in one particular stretch waited far longer. The measure is how many months it took for a buyer's equity to reach 80% of the home's value on paper, using only the scheduled mortgage payments and the price at purchase. Each bar is one purchase month, and its height is the months that purchase took to reach that mark.

2. **What changes across the frames.**
   - Frames 1–2 show the bars as a 3D wall. Most months sit low, labeled "typical," and then one tall spike rises. It is highlighted in blue and labeled "a long tail."
   - Frame 3 flattens the wall into a 2D chart from 1991 to 2016. A "60 months" line is drawn across it, and the blue spike is the purchase months from about 2005 to 2009. These sit well above the line.
   - Frames 4–5 add a label saying that more than 60 months applied to 14.7% of buyers, about 1 in 7. They also bracket the blue region as "one stretch of purchase months."
   - Frames 5–6 draw a national home price index line underneath. It rises, peaks around the blue stretch, dips, and then climbs again.

3. **What it means.** Most buyers reached 80% within about five years or less. Buyers who bought near the mid-2000s peak, right before prices fell, had to wait much longer. The price index suggests the cause. Prices dropped after they bought, so it took years for them to recover. The long tail therefore comes from *when* people bought, not from anything about the buyers themselves. The footers say this is "past buyers, measured," US only, "history, not a forecast," and "not a reason to buy, rent or wait."

4. **Advice a viewer would take.** The animation gives no direct buy, rent or wait advice, and it says so. A viewer would take away a few points about risk:
   - Buying carries timing risk. The typical outcome was fine, but about 1 in 7 buyers in this history waited more than five years.
   - Don't count on a quick payback. Plan to stay put for a long time, and keep an emergency fund so you aren't forced to sell during a downturn.
   - Don't read this as a prediction. It's one historical pattern, not a signal about today's market.

### R4 (strip B14-S14)
**1. What idea is this animation showing?**
It shows how long someone who bought a home at a particular past moment, October 2005, had to wait for the purchase to look okay on paper. The label says 112 months, or 9 years 4 months. The source is FHFA and Freddie Mac data via FRED. The image doesn't define the measure, so I'm reading it as the time for the home's value to get back to what the buyer paid. The second half shows houses of different heights around a flat blue line. The caption says the line is a national average, not one home.

**2. What changes over time across the frames?**
- **Frames 1 to 3:** The chart stays the same. It's a set of thin bars that peak just after the highlighted October 2005 line and then taper off to the right. The text is what changes. Frame 2 adds "on paper" under the 112-month label. Frame 3 adds an "ILLUSTRATIVE" tag and a note: "schedule at that rate: 90 payments."
- **Frames 4 to 6:** The blue average line stays roughly level. The individual houses change height from frame to frame. Some grow taller, some shrink, and they swap places.

**3. What does it mean?**
- **Waiting time:** For people who bought near the 2005 peak, getting back to even took nearly a decade. Buyers from other months waited much less, which is why the bars shrink toward the right.
- **Averages hide variation:** The national average can stay steady while individual homes do much better or worse than it. A buyer's own home won't track the average.
- **Not a prediction:** The repeated footers say "Past buyers, measured," "history, not a forecast," and "not a reason to buy, rent or wait."
- **Unclear point:** I can't tell exactly what the "90 payments" note is meant to show. It looks like a loan-schedule comparison, and the image doesn't explain it.

**4. What advice, if any, would a viewer take from this?**
The video deliberately gives no buy, rent or wait advice. A first-time buyer with about 10% down could still take away a few cautions:
- **Timing matters:** Buying at a peak can mean a long stretch where the home is worth no more than you paid.
- **Plan to stay a long time:** Expect to hold the home for many years, not just a few.
- **Keep a cushion:** Don't stretch so far that you'd be forced to sell during a downturn.
- **Local and individual factors matter:** The national average doesn't tell you what will happen to a specific home or town.

### R5 (strip B12-S12)
1. The animation shows how much of a home's value was still owed as a loan two years after purchase, for people who bought between January 1991 and July 2024. Each bar is one purchase month. Its height is the loan divided by the home's value on paper two years later. Two horizontal lines mark 80% and 75%, and the blue highlights mark the months that got under 75%.

2. Frame 1 shows only the gray bars and the 80% and 75% lines. Frame 2 adds the first result: 58.6% of the 403 purchase months were at or under 80% two years in. Frames 3 to 6 add the second result in blue: 15.6% were at or under 75%. They also highlight two stretches of blue bars, one around 2002 to 2004 and one around 2019 to 2021. Frames 4 to 6 add the label "Fannie Mae's early bar", which links the 75% line to a Fannie Mae rule. I can't tell what that rule is from the image alone.

3. In most periods, home values rose or loans were paid down enough to bring the loan below 80% of the value within two years. That happened for about 6 in 10 purchase months. Getting down to 75% was much rarer, at about 1 in 6. The bars also swell to a big peak in the middle of the chart, roughly the 2006 to 2010 era. For those buyers the loan was still near or above the home's value after two years, so they had little or no equity on paper. Two years in, the outcome depended heavily on when someone bought.

4. The footer says it plainly: this is "not a reason to buy, rent or wait," and it's "history, not a forecast." As a renter with about 10% saved, I would take away three points:
   - Reaching 80% after two years has often happened, but it isn't guaranteed. Buying with 10% down means starting at about 90%, so I'd need price gains or paydown to get there.
   - I shouldn't plan around hitting 75% quickly, since that was uncommon.
   - I should make sure I could handle the case where my equity stays thin or goes negative for a while. For example, I'd want a cushion and a plan to stay in the home for several years.

### R6 (strip B11-S11)
**1. The idea.** The animation shows how long past home buyers waited before their loan was down to 80% of the home's value "on paper". That is the usual point where mortgage insurance could come off. It has one bar for each month a home was bought, from about 1991 to 2016. The data come from FHFA house-price data and Freddie Mac rates, via FRED.

**2. What changes across the frames.**
- Frame 1 shows only the bars. They are low and fairly steady through the 1990s and early 2000s. They spike sharply for purchases around 2005 to 2008, then fall back to a low level after about 2010.
- Frame 2 dims the bars and adds a line and label for the median, which is 23 months on paper.
- Frame 3 adds a wavy line that slopes down over time. It also adds the headline "90.6% no later than the schedule".
- Frames 4 and 5 rearrange the layout and label the line "schedule at each month's rate".
- Frame 6 adds a bracket marked "gap" between the schedule line and the bars.

**3. What it means.**
- The schedule line appears to show how long it would take to reach 80% by making regular mortgage payments alone. It falls over time because mortgage rates fell, so more of each payment goes to principal.
- For about 90.6% of purchase months, buyers reached 80% no later than that schedule. Rising home prices usually sped things up, which is the gap in frame 6. The typical wait was about 23 months.
- The exception is the 2005 to 2008 group. Prices fell after they bought, so they waited much longer.
- The image has no y-axis numbers, so I can't read exact month counts for the bars or the line. It also doesn't state the down payment, so I'm assuming it's roughly 10%.

**4. Advice a viewer would take.** The footers say this is "Past buyers, measured · not a reason to buy, rent or wait" and "history, not a forecast". So it gives no instruction to buy or to wait. A viewer could reasonably take away four points:
- With a small down payment, you have often reached 80% sooner than the payment schedule alone would suggest, because price growth helped.
- That help is not guaranteed. If you buy near a market peak, you could wait years.
- Gains "on paper" aren't cash, and the data cover the US only.
- Plan so you could handle a long wait for 80% instead of counting on a short one.

### R7 (strip B03-S03)
1. **The idea:** The animation shows the 80% loan-to-value line on a mortgage. A buyer who puts down less than 20% usually pays mortgage insurance. It stays on until the loan falls to about 80% of the home's value "on paper." The labels cite Fannie Mae's servicing guide and say it is "the loan owner's rule." They also cite FHFA and Freddie Mac data on past buyers.

2. **What changes:**
   - Frames 1 and 3 show a tall stack for the home's value next to a shorter, darker stack for the loan. A line marks 80% of the value, and the loan stack sits at or near it.
   - In frame 2, a house has a yellow cap on its roof labeled "insurance still on."
   - By frames 5 and 6, there are three houses, each with a green stack and a person beside it, and the yellow insurance cap is gone.

   I'm inferring that the green stacks stand for the owner's equity, and that the three houses stand for the past buyers who were measured.

3. **What it means:** Insurance doesn't drop off until your balance falls to that 80% mark. Paying down the loan, or the home gaining value, moves you toward it. The captions say this is "history, not a forecast," "US only," and "a measurement, not a next step." It describes what happened to earlier buyers, and it doesn't predict what will happen to me.

4. **What I'd take from it:** With about 10% saved, I'd expect to pay mortgage insurance for a while after buying. I'd also know the goal is to get my loan down to 80% of the home's value. The video says outright that this is "not a reason to buy, rent or wait," so it isn't telling me what to do. I'd use it to understand one cost of a small down payment. For my own timeline, I'd check the actual rules on my own loan.

### R8 (strip B07-S07)
1. **The idea.** The animation shows a mortgage balance falling over time until it reaches a threshold: 80% of the home's original value, or $320,000. That implies an original value of $400,000. The citation, 12 U.S.C. 4902, is the federal Homeowners Protection Act. The image never says "mortgage insurance," so I'm inferring that from the law. That act lets you ask to drop private mortgage insurance once you reach this point. The "ILLUSTRATIVE" tag means the numbers are an example, not your numbers.

2. **What changes across the frames.**
   - Frames 1 and 2 show only the white balance curve sloping down toward a stack of blocks on the right.
   - Frame 3 adds a horizontal line labeled "80% of original value = $320,000."
   - Frame 4 moves that line lower in the frame, and the curve gets closer to it.
   - Frame 5 marks the spot where the curve crosses the line, labeled "payment 99: may request."
   - Frame 6 adds a note at the top: "conditions: written request · current on payments."

3. **What it means.**
   - In this example, after about 99 monthly payments the loan balance falls to 80% of the home's original value.
   - At that point the borrower may ask the lender to cancel the extra insurance. It isn't automatic.
   - The borrower has to make the request in writing and be current on payments.
   - The caption "A measurement, not a next step" says that crossing the line only tells you where you stand. You still have to act.

4. **Advice a viewer would take.**
   - Track your loan balance against 80% of the original home value.
   - When you cross it, send a written request to your lender, and keep your payments current.
   - As a renter planning to buy with about 10% down, this means mortgage insurance would likely be part of your costs at first. It isn't permanent, and you can get rid of it.
   - The animation doesn't give a rule for when to buy, how much to save, or what the insurance costs. Those details would have to come from somewhere else.

### R9 (strip B03-S03)
1. **The idea:** I think this is about mortgage insurance (PMI) and the 80% loan-to-value line. A buyer's loan can reach 80% of the home's value on paper, but the insurance stays on until the loan owner's rules say it can come off. The labels cite Fannie Mae's servicing guide and FHFA/Freddie Mac data, and the loan owner is probably Fannie Mae or Freddie Mac. The text on the frames doesn't say "PMI" or "mortgage insurance" outright, so this part is my reading.

2. **What changes:** Frame 1 shows two stacks, the home value (tall) and the loan (shorter), with the loan touching a line labeled "80% on paper." Frame 2 shows a house with a yellow cap and the words "insurance still on." A person stands nearby with a cash bundle and a building. Frame 3 repeats the stacks and adds "loan owner's rule." Frame 4 shows the stacks and the line sliding to the side. Frames 5 and 6 show three similar houses, each with a green stack and a person, which stands for many past buyers.

3. **What it means:** Hitting 80% on paper doesn't automatically end the insurance cost. The loan owner's rule decides when it ends. The animation also stresses that this is a measurement of what past US buyers experienced. The captions say "history, not a forecast" and "a measurement, not a next step." The three houses suggest it describes a typical pattern across buyers rather than one person's case.

4. **Advice a viewer would take:** There's no direct instruction to buy, rent, or wait. The caption says outright that this is "not a reason to buy, rent or wait." The practical takeaway for someone with about 10% down is that you'd likely pay mortgage insurance at first. Getting the loan to 80% is a milestone, but you'd need to check the loan owner's rules for removing the insurance. It's worth asking a lender how and when it comes off.

### R10 (strip B02-S02)
1. **The idea.** The animation is about how long it takes a buyer who puts down about 10% to get the loan down to 80% of the home's value. At 80%, the buyer would have 20% equity. That is the usual point where private mortgage insurance can come off. It compares the scheduled paydown with what actually happened to past buyers.

2. **What changes across the frames.**
   - Frames 1–2: An illustrative line starts at 90% of the price and slopes down to the 80% line. It reaches 80% at about 8 years, which is labeled the "schedule." The caption says this is "a measurement, not a next step."
   - Frame 3: Real data appears. The chart is labeled "one line per purchase month, 1991–2016," and the first lines begin to fan out from the 90% starting point.
   - Frames 4–5: More lines fill in. Many climb above 90% before they fall. The loan grew as a share of home value, which means home prices fell. Others drop quickly. The bundle spreads across the whole 0–10 year range.
   - Frame 6: Two lines are highlighted. The typical buyer reached 80% in about 2 years. The slowest case, in blue, took about 9 years. That is longer than the 8-year schedule, and the line went well above 90% along the way.

3. **What it means.** Home price changes affect how fast you reach 20% equity much more than the loan payments do. In the data, the typical buyer got there in about 2 years, mostly because prices rose. Buyers who bought at the wrong time had home values fall, and they waited much longer than the schedule suggests. The 8-year schedule is a middle reference point, not a prediction. The timing varied widely from one buyer to the next.

4. **The advice a viewer would take.** The animation gives no buy, rent or wait advice. Its captions say these are past buyers, measured, "not a reason to buy, rent or wait," and "history, not a forecast." I'd take away three points:
   - Don't count on reaching 20% equity in a fixed number of years.
   - Plan for the slow case, which could be 9 years or more, in case prices stall or fall.
   - Be ready to hold the home long enough to ride out a bad stretch, and keep a cash cushion so you aren't forced to sell during one.

   The data covers the US only.

### R11 (strip B16-S16)
**1. The idea.** The animation follows one past buyer, Owen, who got a 5.71% mortgage in January 2004. It compares two ways of reaching the 80% line. That line is probably loan-to-value, the point where you owe 80% of the home's value, meaning 20% equity. The image doesn't say why 80% matters. A common reason is that it's where mortgage insurance can usually be dropped, but that's my inference.

**2. What changes across the frames.**
- The x-axis runs from 0 to 10 years.
- Two white lines start at 80% and move rightward.
- The "schedule" line slopes down very slowly. It follows only the planned loan paydown and doesn't reach the 80% line until about year 7 (86 months).
- The "on paper" line drops quickly and crosses the 80% line after about 13 months.
- The blue price index line rises, ending at +11.2%. That rise in home prices is what pulls the "on paper" line down so fast.

**3. What it means.** In Owen's case, rising home prices built equity much faster than the loan payments alone would have. The "on paper" crossing came at 13 months, against 86 months on the normal payment schedule. The picture is a gap between equity from price growth and equity from paying down the loan.

**4. What advice a viewer would take.** Very little that's directive, and the video says so itself. The footer reads "Past buyers, measured · not a reason to buy, rent or wait," and also "US only · history, not a forecast." The chart is also labeled "Illustrative."

The reasonable takeaways for someone with about 10% down are:
- Equity can come from price changes as well as payments. That is not guaranteed, and prices can also fall.
- If the 80% mark matters for your loan, check how your lender defines it and whether it uses the original value or a new appraisal.
- Don't treat one buyer's 2004 experience as a forecast.

### R12 (strip B17-S17)
1. **The idea:** The animation follows one past buyer, Victor, who bought in October 2005 with a 6.07% rate. It shows how long it took before his loan fell to the 80% line. The 80% label isn't explained in the image. I read it as the point where he owes 80% of the home's value, meaning 20% equity. That's an inference. The source line says the data is from FHFA and Freddie Mac via FRED, and a tag marks the chart as illustrative.

2. **What changes:** The time axis runs from 0 to 10 years, and the lines draw in from left to right. There are three lines:
   - A straight gray "schedule" line drifts slowly downward.
   - A white "on paper" line wiggles. It rises in the middle years, peaks at about year 5, then falls past the 80% line near the end.
   - A blue price index line stays below the others and dips in the middle years.

   Labels then appear: "on paper: 112 months" and "index still 3.3% below purchase." The last frame swaps the chart for a small house and a person.

3. **What it means:** The straight schedule line shows what he'd expect from paying the loan down. His real position moved around with home prices, and it got worse when prices fell. By the 112-month mark, nearly 9.5 years, he had reached the 80% line on paper. Even then, the price index was still 3.3% below what he paid. After about a decade, he had barely gotten past the equity line, and the home's market price hadn't recovered.

4. **Advice a viewer would take:** The image says outright that this is "not a reason to buy, rent or wait," that it covers the US only, and that it is history, not a forecast. So it gives no buy-or-rent instruction. A viewer with a small down payment would take a cautious point. Reaching 20% equity can take close to ten years, and falling prices can make it take longer. If you buy, plan to stay a long time and keep a cushion. Don't count on quick equity.

### R13 (strip B08-S08)
1. **The idea.** The animation shows when private mortgage insurance (PMI) can end under the Homeowners Protection Act (12 U.S.C. 4902). As the loan balance falls, it crosses two thresholds. At 80% of the home's original value ($320,000, which implies a $400,000 home), you may ask to have PMI removed. At 78% ($312,000), it ends automatically. The "Illustrative" tag means the numbers are examples.

2. **What changes over time.**
   - In frames 1–4, a sloping band (the loan balance) falls toward two horizontal lines.
   - In frame 1 it reaches the 80% line, around payment 99. The label says you "may request" cancellation, if you made a written request and are current on payments.
   - In frames 2–3 the 78% line ($312,000) appears.
   - In frame 4 the balance reaches that line at payment 114, about 9.5 years in. The label says PMI "ends automatically."
   - In frames 5–6 the view zooms out to the full 360-payment (30-year) curve. Payments 99 and 114 sit early on it, well before the house is paid off. The final label says this is "based on the schedule only."

3. **What it means.** PMI is not permanent. It is tied to how much of the original value you still owe. Under the scheduled payments alone, you could ask to drop it around payment 99 and it would stop automatically around payment 114. That is roughly 8 to 9.5 years into a 30-year loan. The caption "A measurement, not a next step" suggests the video is only showing where these points fall, not telling you what to do.

4. **Advice a viewer would take.**
   - The video gives no explicit advice. A viewer could still infer that a low down payment, with PMI, is a cost that fades.
   - They might also infer that they can ask to cancel PMI at 80% rather than wait for the automatic end at 78%.
   - The conditions matter. You need a written request and current payments.
   - The timing assumes you only make scheduled payments. Extra principal payments or a home value change could change when you hit the thresholds. The video doesn't cover that, and the lender's own rules may differ.

For you, with about 10% saved, you'd likely pay PMI. This suggests it would be temporary, not a reason to rule out buying. A 10% down payment would start the loan at 90% of the price, not the 80% shown here. So your own dates would differ from the ones in the animation.

### R14 (strip B07-S07)
1. **The idea:** The animation shows when you can ask to cancel private mortgage insurance (PMI). The law cited, 12 U.S.C. 4902, is the Homeowners Protection Act. A falling line, which I read as the loan balance, drops toward a threshold line labeled "80% of original value = $320,000." That figure implies a $400,000 home.

2. **What changes:** In frames 1 and 2, the balance curve just slopes downward as payments are made, and there is no threshold yet. In frames 3 and 4, the 80% line appears, and the curve gets closer to it. In frame 5, the curve crosses the line at a marked point labeled "payment 99: may request." In frame 6, a note appears: "conditions: written request · current on payments." The caption throughout reads "A measurement, not a next step," and the "ILLUSTRATIVE" tag means the numbers are an example.

3. **What it means:** As you pay down the mortgage, your balance eventually falls to 80% of the home's original value. In this example that happens around payment 99, roughly 8 years in. At that point you earn the right to ask the lender to drop PMI. Reaching 80% doesn't end PMI by itself. The caption says it's a measurement, not an automatic action. You have to make a written request, and you have to be current on your payments.

4. **Advice a viewer would take:**
   - If you put down less than 20%, as I'd be doing with about 10%, PMI is a cost you should expect. It isn't permanent.
   - Track when your balance will reach 80% of the original value, and don't wait for the lender to remove PMI for you.
   - When you hit that point, send a written request and keep your payments current.
   - Extra principal payments would get you to the threshold sooner.
   - The video doesn't say this, but I'd also check my loan's specific terms, because the law has other rules and automatic-termination points that this animation doesn't show.

### R15 (strip B16-S16)
**1. The idea.** The animation follows one past buyer, "Owen," who bought in January 2004 with a 5.71% mortgage rate. It compares two ways he could have reached the 80% mark, which I read as 80% loan-to-value, or 20% equity. The "schedule" line is the slow path from paying down the loan on its normal amortization schedule. The "on paper" line is the faster path when rising home prices (the blue price index) are counted. The image doesn't define the 80% line, so that reading is my inference. The chart is labeled "Illustrative," with data from FHFA and Freddie Mac via FRED.

**2. What changes across the frames.** The time axis runs from 0 to 10 years, and the lines are drawn out gradually from left to right.
- The blue price index climbs, ending at +11.2%.
- The "on paper" line drops quickly and crosses the 80% line at about 13 months.
- The "schedule" line slopes down very gently and doesn't reach 80% until about month 86, roughly 7 years.
- The text labels fill in over the frames: "on paper: 13 months · schedule: 86," then "index +11.2%."

**3. What it means.** For this buyer, rising prices got them to 80% about 6 years sooner than loan paydown alone would have. Home price movement can matter more than the monthly payments in the early years. That only works if prices rise. The footer says this is "Past buyers, measured," "history, not a forecast," and "US only."

**4. Advice a viewer would take.** The video explicitly says this is not a reason to buy, rent, or wait. A viewer with about 10% down could take away three things:
- Early equity depends heavily on what home prices do, not just on payments.
- The 80% threshold is worth tracking.
- One buyer's good timing isn't something to count on, because prices can also fall and delay or reverse the progress.

### R16 (strip N1-S06)
1. **The idea:** The animation shows what a mortgage looks like in numbers. A $360,000 loan at the September 2026 average rate of 6.86% (Freddie Mac, via FRED) comes to a fixed payment of $2,362 a month for principal and interest. It also shows that the loan balance falls on a schedule fixed on day one.

2. **What changes across the frames:**
   - **Frames 1–2:** A $360,000 loan, drawn as a tall tower beside a small house block, appears. Then the 6.86% rate label is added.
   - **Frame 3:** The $2,362/month payment is attached to the house block.
   - **Frame 4:** A warning appears that taxes, home insurance and PMI come on top of that payment.
   - **Frames 5–6:** The view switches to a balance curve over 360 payments. The tower shrinks as payments go by, at payment 35 and then payment 114. The curve is labeled "slowly at first" and "faster later."

3. **What it means:**
   - **Monthly cost:** The $2,362 covers only the loan itself. The real monthly cost is higher once taxes, insurance and PMI are added. PMI is typically charged when the down payment is under 20%, which would apply to someone who has saved about 10%.
   - **Slow early paydown:** In the early years most of each payment goes to interest. The balance barely drops at first and then speeds up over the 30-year term.
   - **Fixed schedule:** The payoff path is set when you sign.
   - **Illustrative figures:** The "ILLUSTRATIVE" tag and the "A measurement, not a next step" caption say these numbers are an example. They are not a recommendation or a prediction.

4. **Advice a viewer would take:**
   - **Budget for the full payment:** Plan around the whole monthly cost, not just the $2,362. Taxes, insurance and PMI could add a lot.
   - **Expect slow equity early:** Equity builds slowly in the first years. If you might move within a few years, that matters a lot.
   - **Check your own numbers:** Run your own price, rate and down payment. The video doesn't tell you to buy or to wait.

### R17 (strip B02-S02)
1. **The idea.** The animation is about how long it takes a buyer who puts down about 10% to get their loan down to 80% of the home's value. That point matters because it's roughly where private mortgage insurance (PMI) can come off. It compares the scheduled path with what actually happened to past US buyers.

2. **What changes across the frames.**
   - Frames 1–2 are labeled "illustrative." A single line starts at 90% of the price and slides down to the 80% line. On the standard payment schedule that takes about 8 years.
   - Frame 3 switches to real data (FHA/FHFA and Freddie Mac, via FRED). It draws one line for each purchase month from 1991 to 2016.
   - Frames 4–5 fill in a large tangle of lines. Many drop to 80% much sooner than the schedule. Others rise above 90% first and take much longer to come down.
   - Frame 6 highlights two cases. The typical buyer got to 80% in about 2 years. The slowest case took about 9 years, which is longer than the schedule.

3. **What it means.** Loan-to-value depends on more than paying down the principal. It also depends on what home prices do. If prices rose, the loan fell as a share of the home's value much faster than the schedule predicts. If prices fell, the loan stayed high or even grew as a share of value, and the buyer stayed above 80% for years. The 8-year schedule is therefore a middle-of-the-road benchmark. Real outcomes ranged from about 2 years to about 9 years, depending on when someone bought.

4. **What a viewer would take from it.** Not much about whether to act. The animation says outright that it is "not a reason to buy, rent or wait," that it covers the US only, and that it is "history, not a forecast." The practical points are about expectations. Don't assume PMI will end on the scheduled date, since it could be much sooner or later. Budget for the possibility that PMI lasts longer if prices stall or fall. As a buyer with 10% down, I'd read it as a reminder that my timeline depends partly on the market, not just on my payments.

### R18 (strip B11-S11)
1. **The idea:** The animation looks at how long past US home buyers took to get to 80% on paper, one bar per purchase month from about 1991 to 2016. I'm assuming "80% on paper" means owing 80% of the home's value, or 20% equity. A line shows how long the plain payment schedule would take at that month's mortgage rate. The point is that, for most past buyers, getting to 80% didn't take longer than the schedule said.

2. **What changes across the frames:**
   - Frame 1 shows only the bars. They are low and steady through the 1990s and early 2000s, jump sharply for people who bought around 2005 to 2008, then fall back.
   - Frame 2 adds a median line, 23 months on paper, and dims the bars.
   - Frame 3 adds the headline "90.6% no later than the schedule" and the schedule line.
   - Frames 4 and 5 re-align the chart and label the line "schedule at each month's rate."
   - Frame 6 marks the "gap" between the schedule line and most of the bars.

3. **What it means:**
   - A typical buyer got to 80% in about 23 months.
   - Roughly 9 in 10 buyers got there on or ahead of the schedule. The gap in frame 6 suggests they were usually well ahead, probably because home prices rose along with their payments.
   - The exception is the 2005–2008 group. They bought near the peak, prices fell, and they took much longer.
   - The schedule line drifts down over time, which fits falling mortgage rates.

4. **What a viewer would take away:**
   - The video says outright that this is "not a reason to buy, rent or wait," and that it is US-only history, not a forecast. So it gives no buy-or-wait advice.
   - The takeaway is more modest. Building equity has usually been faster than the schedule alone suggests, but timing matters. Buying at a peak can stretch it out a lot.
   - For me, saving about 10% and renting, that means I shouldn't count on fast equity. I'd want a cushion in case prices fall, and I'd plan to stay put for years.

I'm inferring the exact definitions from the labels. The image doesn't spell them out.

### R19 (strip B12-S12)
**1. The idea.** The animation shows how much of a home's value was still owed as a loan two years after purchase, for buyers who bought in each month from January 1991 to July 2024. Each bar is one purchase month. Bar height is loan divided by the home's value on paper two years later. The sources are FHFA, Freddie Mac via FRED, and Fannie Mae's guideline B-8.1-04. Two horizontal lines mark 80% and 75%.

**2. What changes across the frames.**
- Frame 1 shows only the grey bars and the two threshold lines.
- Frame 2 adds the first statistic: in 58.6% of the 403 purchase months, the loan was at or under 80% of value after 24 months.
- Frame 3 adds a second statistic and highlights the matching bars in blue. In 15.6% of months, the loan was at or under 75%. The blue bars form two clusters, one in the early-to-mid 2000s and one around 2020–2022.
- Frames 4 to 6 add a "Fannie Mae's early bar" label and keep the highlights. The blue patches get a little more emphasis, but the data doesn't change.

**3. What it means.** Most buyers owed less than 80% of the home's value two years in, but only a small share owed 75% or less. Buyers who bought just before the mid-2000s price drop had the tallest bars, so they owed the most relative to value. Buyers who bought just before the 2020–2022 price run-up had the shortest bars. Putting 10% down starts you well above these thresholds. Whether you cross 80% or 75% within two years depends heavily on when you buy and what home prices do afterward, which you don't control.

I'm not sure what "Fannie Mae's early bar" refers to. It probably means the loan-to-value level at which Fannie Mae's rules let a borrower get out of mortgage insurance early. The image doesn't say so, so treat that as a guess.

**4. The advice a viewer would take.** The footer says it directly: this is past buyers, measured. It is not a reason to buy, rent, or wait, and it is US-only history, not a forecast. A viewer shouldn't treat it as a signal to time the market. As someone with about 10% saved, I'd take away three points:
- Reaching 80% loan-to-value, where private mortgage insurance typically becomes removable, is common but not guaranteed within two years.
- Reaching 75% is rare, so don't count on price gains to build equity quickly.
- If I buy, I should plan for paying down the loan and for possibly carrying mortgage insurance for a while.

### R20 (strip B18-S18)
**1. The idea.** The animation shows how long past US home buyers with small down payments took to reach 80% loan-to-value, the point where mortgage insurance usually can come off. It draws each buyer's path from the same starting point, "lined up at purchase," using the same rule and the same house-price index (FHFA and Freddie Mac data via FRED). The slide labels it "illustrative." It also says it is history, not a forecast, and not a reason to buy, rent or wait.

**2. What changes across the frames.**
- Frame 1 shows one white line ("on paper") wandering above and below the flat "schedule" lines, between about 75% and 80%, over 0 to 10 years.
- Frames 2 and 3 add many thin lines, one per past buyer, which form a cloud. Three example buyers, Grace, Owen and Victor, are labeled at different points. Frame 3 notes that the schedule is fixed at the start.
- Frame 4 adds a marker at about 2 years. It says the typical buyer took 23 months and that about 1 in 7 took more than 60 months. About 2 years matched the typical month, "not the slow ones, not the lender's step."
- Frame 5 shows a $400,000 home next to a tall stack that is green and mostly filled in, captioned "A measurement, not a next step."
- Frame 6 shows two choices side by side: "buy now + mortgage insurance" with a house, and "keep renting, keep saving" with an apartment building. A person stands between them.

**3. What it means.** Mortgage insurance does not end on a fixed date. The schedule set at purchase is slow, but home prices often rise and push the loan below 80% sooner. For a typical past buyer that happened in about 2 years, while for roughly 1 in 7 it took over 5 years. The spread between buyers is wide, and the typical case is not a promise.

**4. What a viewer would take from it.** The slides themselves say the animation is not advice to buy, rent or wait. A viewer would take away that putting down less than 20% and paying mortgage insurance is often temporary and has historically ended in about 2 years. They would also see it can last much longer, so they should not count on a quick exit. The last frame leaves the choice open: buy now with insurance, or keep renting and saving. As a renter with about 10% saved, I'd read it as "insurance cost is a real but time-limited factor to plan for, and I shouldn't assume I'm in the fast group."

### R21 (strip B13-S13-N2)
1. **The idea.** The animation shows how long past US home buyers took to build enough equity to reach 80% loan-to-value. That is the point where they'd have 20% equity and could drop private mortgage insurance (PMI). Each bar is one purchase month, from 1991 to 2016. Its height is the number of months it took to get to 80% on the original payment schedule alone. The data come from FHFA and Freddie Mac via FRED.

2. **What changes over time.**
   - **Frames 1–2:** A 3D view shows a "typical" low run of bars. Then a tall spike appears, labeled "a long tail," and is highlighted in blue.
   - **Frame 3:** The view flattens into a 2D chart with a 60-month line. The blue bars, which are the purchase months from about 2005 to 2009, sit above that line.
   - **Frame 4:** A label says 14.7% of buyers (about 1 in 7) took more than 60 months.
   - **Frame 5:** The blue stretch is bracketed as "one stretch of purchase months." A thin line begins to appear along the bottom.
   - **Frame 6:** That line is now fully drawn and labeled "national home price index." It rose through the mid-2000s, peaked, then fell and recovered.

3. **What it means.** For most buyers, reaching 80% "on paper" took under five years. A minority took much longer. They were clustered in one stretch, those who bought near the 2005–2009 price peak. Prices then fell, so their equity didn't build the way the schedule suggested. The wait wasn't spread evenly across buyers. It depended heavily on when you bought relative to the housing cycle.

4. **Advice a viewer might take.**
   - The video says outright that this is "not a reason to buy, rent or wait," and it is "history, not a forecast." So it gives no buy-or-rent instruction.
   - A viewer could reasonably take away that a roughly 10% down payment usually means a few years of PMI, and that timing risk is real. A bad purchase window can stretch that period a lot, so it's worth keeping a cash cushion and not assuming equity will build on schedule.
   - It also suggests planning to stay put long enough to ride out a price dip.
   - Past buyers' experience is only a guide to what could happen, not a prediction.

### R22 (strip B08-S08)
1. **The idea:** The animation shows when private mortgage insurance (PMI) can be removed, under the federal Homeowners Protection Act (12 U.S.C. 4902). The loan balance falls along a declining line toward two thresholds. At 80% of the home's original value ($320,000, which implies a $400,000 home), you may ask to cancel PMI. At 78% ($312,000), it ends automatically. It's labeled "illustrative."

2. **What changes:** Frame 1 shows the balance line sinking to the 80% line at payment 99. That's the point where you "may request" cancellation, and it comes with conditions: a written request and being current on payments. Frames 2 and 3 add the 78% line. Frame 4 marks payment 114 (9.5 years in) as the point where PMI "ends automatically." Frames 5 and 6 zoom out to the full 360-payment (30-year) schedule. Payments 99 and 114 sit early on the curve, well before the house is paid off. Frame 6 adds the note "based on the schedule only."

3. **What it means:** PMI isn't permanent. On a 30-year loan with a small down payment, the balance reaches 80% of the original value around payment 99, so you can ask to drop PMI then. If you don't ask, it ends automatically at 78%, around payment 114. Both dates come from the original amortization schedule, not from what the home is worth now. The caption "A measurement, not a next step" means the video is describing the timeline and isn't telling you to do anything.

4. **Advice a viewer would take:** If you buy with about 10% down, you'll probably pay PMI at first, and it has an end date. Don't treat it as a reason never to buy. Know the payment number where you hit 80% (about year 8 in this example). Be current on payments, and send a written request then instead of waiting for the automatic cutoff about 15 payments later. Making extra principal payments would reach the 80% mark sooner. The animation doesn't give an explicit recommendation beyond that. It also doesn't cover other ways PMI can end, such as a new appraisal after the home gains value.

### R23 (strip B18-S18)
**1. The idea.** The animation looks at how long a first-time buyer with a small down payment (about 80% loan-to-value or higher) typically takes to get their loan balance down to roughly 80% of the home's value. That is usually the point where mortgage insurance can come off. It uses past US buyers' histories (FHFA and Freddie Mac data via FRED), all lined up at their purchase date. The labels say it is illustrative, history and not a forecast.

**2. What changes across the frames.**
- Frame 1 shows a few lines starting near 80% and moving toward 75% over 10 years. The straight, steady lines are the fixed payoff schedule. The wavy white line is what happened "on paper" once home prices moved.
- Frames 2 and 3 add many more past buyers as a dense bundle of wavy lines. The labeled examples (Owen, Grace, Victor) fall at different speeds. Frame 3 stresses that the schedule is fixed at the start.
- Frame 4 zooms in on year 2 with a marker. The typical buyer got there in about 23 months, and about 1 in 7 took more than 60 months. The note says about 2 years matched the typical month, not the slow cases and not the lender's scheduled step.
- Frame 5 switches to a $400,000 home with a stack of green blocks. It is labeled "a measurement, not a next step."
- Frame 6 shows two paths for the buyer: "buy now + mortgage insurance" (a house) and "keep renting, keep saving" (an apartment building), with a person between them.

**3. What it means.** Mortgage insurance on a small down payment doesn't last as long as it would if only the lender's schedule counted. Rising home prices can get a buyer to the cutoff sooner, often in about 2 years. That isn't guaranteed. Some buyers wait 5 years or more, especially if prices stall or fall. The spread between buyers is wide, and the typical case isn't the only one.

**4. Advice a viewer would take.** The video avoids telling anyone what to do. Its caption says this is "not a reason to buy, rent or wait." A viewer would come away with these points:
- Mortgage insurance with a small down payment may be temporary, and about 2 years is typical.
- It could take much longer, so plan for the slow case and not only the typical one.
- Buying now with insurance and renting while saving more are both presented as legitimate choices.
- The decision should rest on personal finances, such as budget, how long they'd stay, and how much cushion they'd have. A past average shouldn't drive it.

I can't confirm details beyond what is printed in the frames, such as exactly how "on paper" is calculated.

### R24 (strip B17-S17)
1. **The idea:** The animation follows one past buyer, "Victor," who bought in October 2005 with a 6.07% mortgage. It shows how long it took him to build real equity after home prices fell. The white line looks like his loan as a share of the home's value. The 80% line looks like the point where he owes 80% or less, which means 20% equity. That reading is my inference, because the chart doesn't label the vertical axis. The gray "schedule" line is the paydown he would have had if prices stayed flat. The blue line is a national home price index. The footer says this is past data, labeled "illustrative," and "not a reason to buy, rent or wait."

2. **What changes across the frames:**
   - **Frame 1:** There's only the 80% line and a 0–10 year axis.
   - **Frame 2:** The first few years are drawn. The white line drifts slightly with the schedule line, and the blue price index dips.
   - **Frames 3–5:** The white line climbs well above the schedule line in the middle years as prices sag. It then falls and finally crosses below 80% at the end. The text reads "on paper: 112 months" and "index still 3.3% below purchase."
   - **Frame 6:** The chart is replaced by a small house with a person beside it.

3. **What it means:** On paper, Victor reached 20% equity after about 112 months, or roughly 9 years. That happened even though home prices were still 3.3% below what he paid. So his equity came from paying down the loan, not from the home gaining value. For years the price drop pushed him away from the 80% line, so he was likely underwater or close to it.

4. **Advice a viewer might take:**
   - A small down payment, like my roughly 10%, can leave you with thin or negative equity for a long time if prices fall.
   - Don't count on appreciation to build equity. Plan to stay many years, and keep cash reserves so you aren't forced to sell during a dip.
   - The video says outright that this is one historical case, US only. It isn't a forecast or a signal about whether to buy, rent or wait now.

For me, the practical lesson is to buy only if I can hold the home for a decade and absorb a price drop. I shouldn't treat a home as a guaranteed gain.
