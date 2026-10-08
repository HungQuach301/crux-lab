# Grading packet (blind). Independent grader. Each label is one reader's answers about one silent 6-frame strip; the strip id is given so you compare against its muted read. Grade literally.

## Rubric
- **Chấm:** người chấm độc lập mù tập; nghĩa 1 / 0,5 / 0 so với "muted read" của `review-c3/spans.json`; cờ khuyên theo **A9** (thận trọng chung — tự kiểm số, hỏi bên cho vay — không tính; khuyên mua/chờ/bán/chọn tính). Người đọc đúng = nghĩa 1 và khuyên_tính false.


Muted read (đáp án đúng) theo hình:
- B02-S02: The loan, as a share of the price, starts at 90 % and drifts down slowly; it only touches the 80 % line after about 8 years.
- B18-S18: Three panels side by side, aligned at purchase: one fixed schedule band and a fan of on-paper lines from fast to slow; a vertical 'your plan' marker stands between the schedule band and the fan; the 75 % line stays visible under all of them.

Output JSON only: {"R1": {"score": 1|0.5|0, "advice": true|false, "caution_only": true|false, "why": "<one line>"}, ...}

### R1 (strip B18-S18)
1. **The idea.** The animation compares how fast past US home buyers actually reached 80% loan-to-value (20% equity) with the schedule on paper. That is the point where mortgage insurance can come off. It uses FHFA and Freddie Mac data. Three example buyers, Owen (fast), Grace (typical) and Victor (slow), all follow the same rule and the same price index, lined up at their purchase date. The labels say "ILLUSTRATIVE", "history, not a forecast" and "not a reason to buy, rent or wait."

2. **What changes across the frames.**
   - Frame 1 shows three separate panels, one per buyer. Each has a straight "on paper" schedule line and a wobbly real line of the loan balance relative to home value.
   - Frames 2 and 3 overlay the three buyers on one shared 0–10 year axis, with a "plan" marker at the start. The paths spread out around the 80% line, and the background shows many other past buyers as a band.
   - Frame 4 adds numbers. The paper schedule is fixed at the start, with a typical 23 months. About 1 in 7 buyers took more than 60 months. About 2 years matched the typical month, "not the slow ones, not the lender's step."
   - Frame 5 switches to a $400,000 home shown as a stack of green blocks. It is labeled "a measurement, not a next step," in dollars of the day.
   - Frame 6 ends with a person between two options. One is "buying now + mortgage insurance" and the other is "still renting, still saving."

3. **What it means.** The paper schedule says when you should reach 80%, but real timing depends on home prices, so it varies. Most buyers got there in around two years, a few quickly and some very slowly. About 1 in 7 took more than five years. Mortgage insurance on a roughly 10%-down purchase is therefore usually temporary, but its length is uncertain. Frame 6 frames the choice as buying with that insurance versus renting and saving.

4. **Advice a viewer would take.** The video explicitly gives no buy, rent or wait recommendation. A viewer, like me with about 10% saved, would take away three things:
   - Don't assume the paper schedule will tell you when the insurance ends. Plan for a typical 2 years or so, and budget for the chance it takes 5 or more.
   - Check whether your monthly budget could handle the insurance for that long, since the data is historical and US-only.
   - Treat this as one input to the buy-or-rent decision. Other factors matter too, such as local prices, how long you'll stay, and your savings.

### R2 (strip B18-S18)
1. **The idea.** The animation looks at how long mortgage insurance lasts for someone who buys with a small down payment. It compares the loan balance against the home's value, using one rule and one price index, with every past buyer lined up at their purchase date. It appears to track when the loan falls to about 80% of the home's value, the usual point where insurance can come off. The 75% line is a lower reference mark. The image doesn't say "mortgage insurance" until the last frame, so that reading is my inference from the final frame and the 80% and 75% marks.

2. **What changes.** Frame 1 shows a few lines over 0 to 10 years. Frame 2 expands that into a ribbon of many past buyers, with three example buyers (Owen, Grace and Victor) and a marker near year 2. Frame 3 adds that the repayment schedule is fixed at the start. Frame 4 adds the numbers: on paper, the typical buyer reached the threshold in 23 months, and about 1 in 7 took more than 60 months. It also says two years matched the typical month, not the slow cases or the lender's step. Frame 5 switches to a $400,000 home next to a stacked bar, with a small highlighted slice at the bottom. Frame 6 shows a house, a person and an apartment building, labeled "buy now + mortgage insurance" and "keep renting, keep saving."

3. **What it means.** Mortgage insurance often doesn't last long, and for the typical past buyer it ended in about two years. That depended on how home prices moved, so some buyers waited much longer. The "on paper" line is the loan's actual standing, which moves with home prices. The "schedule" line is the fixed repayment plan, which doesn't. The repeated captions say this is US history, not a forecast, and that it is "a measurement, not a next step."

4. **Advice a viewer would take.** The video avoids telling you what to do. Its captions say the data is "not a reason to buy, rent or wait," and frame 6 shows both paths without favoring either. A viewer could take away that mortgage insurance isn't necessarily a long-term cost, but that how long it lasts is uncertain and depends on the housing market. In your position, with about 10% saved, it's one input to weigh against your own budget, how long you plan to stay, and local prices. It isn't a signal to act.

### R3 (strip B02-S02)
1. **The idea.** The animation shows how long it takes a home buyer's loan to fall to 80% of the home's value. That is the point where you could drop private mortgage insurance. It compares the fixed payment schedule with what happened to real buyers. The schedule assumes the loan starts at about 90% of the price and reaches 80% in roughly 8 years, from paying down the loan alone. The real-world lines use FHFA and Freddie Mac data from FRED. They show loan divided by the home's value on paper, with one line per purchase month from 1991 to 2016.

2. **What changes across the frames.**
   - Frames 1–2: A single illustrative line, marked "ILLUSTRATIVE", slopes down from 90% to the 80% line. It gets there at about year 8.
   - Frame 3: The label "schedule ≈ 8 years" appears. Real purchase-month lines begin to fan out from the starting point.
   - Frames 4–5: Many more lines fill in. They spread widely. Some drop below the schedule quickly, and others rise well above 90% before coming back down.
   - Frame 6: Two real cases are highlighted. A typical buyer reaches 80% in about 2 years. The slowest case, in blue, rises well above the starting level and takes about 9 years.

3. **What it means.** The schedule is a rough guide, and actual experience varies a lot because home values moved. When prices rose, the loan share fell fast, and a typical buyer got to 80% in about 2 years. When prices fell, the loan share went up and the wait stretched out. Even the slowest case came in only slightly after the schedule's 8 years. The chart's own caption says this is a measurement of past buyers. It is US-only history and not a forecast.

4. **Advice a viewer would take.** The animation gives no direct advice. It says outright that it is "not a reason to buy, rent or wait." A careful viewer would take away a few points:
   - Don't count on home price growth to get you out of mortgage insurance quickly.
   - Don't assume the 8-year schedule will hold either, because it can run slower or faster.
   - If you put down about 10%, plan for a range of outcomes, from about 2 years to 9 years or more, rather than a single date.
   - The past isn't a promise, so this should inform your planning and not decide whether you buy.

### R4 (strip B18-S18)
**1. The idea.** The animation shows how long it takes past US home buyers with small down payments to reach 80% loan-to-value. That is the point where mortgage insurance can normally come off. The data source is labeled FHFA and Freddie Mac via FRED. The whole thing is marked "illustrative."

**2. What changes across the frames.**
- **Frame 1:** Three buyers appear side by side: Owen (fast), Grace, and Victor (slow). Each has a straight "on paper" payoff schedule, and a wiggly line shows what actually happened, which depends on home prices.
- **Frames 2–3:** The three paths are lined up at the purchase date and overlaid on a 0–10 year axis. A "plan" marker sits at the start, and the note says the schedule is fixed at the start.
- **Frame 4:** Numbers appear. On paper, the typical buyer reaches the 80% mark in about 23 months, and about 1 in 7 take more than 60 months. A callout says roughly 2 years matched the typical month, not the slow ones and not the lender's step.
- **Frame 5:** The view switches to a $400,000 home drawn as a stack of equity, with "all $ in dollars of the day."
- **Frame 6:** It ends on two icons. One is a house with the label "buying now + mortgage insurance." The other is an apartment building with the label "still renting, still saving."

**3. What it means.**
- How fast you get below 80% loan-to-value depends on when you buy and what home prices do afterward, not only on the payment schedule.
- Most buyers reach it in about two years, but some take five years or more.
- The animation says it is a measurement of past buyers. It is not a forecast and not a reason to buy, rent, or wait.

**4. Advice a viewer would take.**
- The animation gives no direct advice, and it says so on every frame.
- A viewer could take away that mortgage insurance is usually temporary but its length is uncertain, so they shouldn't assume the typical 2 years.
- They might also see that buying with a small down payment and continuing to rent and save are both real options, with different trade-offs.
- Because I read the frames only, I can't say what the narration recommends. The image doesn't show whether the 23-month figure assumes price growth or only paying down the loan.

### R5 (strip B02-S02)
1. The animation shows how long it takes a buyer who puts 10% down to get their loan down to 80% of the home's value. It starts with a made-up "illustrative" line for a standard payment schedule. Then it swaps in real historical data from FHFA and Freddie Mac, pulled through FRED. The frames label the 80% line only as a level, not what it is for. I'd guess it's the point where mortgage insurance usually comes off, but the image doesn't say that.

2. In frames 1 and 2, a single line slides from 90% down to 80% over about 8 years. That is the schedule alone, and the frames call it "a measurement, not a next step." In frames 3 to 5, many thin gray lines fan out, one for each purchase month from 1991 to 2016. Some drop fast. Many rise first, because home values fell, and then come down slowly. In frame 6, two lines are highlighted. The typical buyer got to 80% in about 2 years, and the slowest case took about 9 years, which is longer than the 8-year schedule.

3. The time it takes to reach 80% depends heavily on what home prices do after you buy, not just on your payments. The schedule says about 8 years. Most past buyers got there much sooner, because rising prices cut the loan's share of the value. Some bought at a bad time, watched prices fall, and waited longer than the schedule, up to about 9 years.

4. The animation gives no buy, rent or wait advice. It says outright that it covers past buyers, is "not a reason to buy, rent or wait," and covers the US only, as "history, not a forecast." The most a viewer can take from it is to expect a wide range of outcomes. If I'm putting 10% down, I shouldn't count on reaching 80% in exactly 8 years or in 2. I should plan for the slow case, so I'd want to know I could afford the costs of staying under 80% for as long as 9 years.

### R6 (strip B02-S02)
**1. The idea.** The animation shows how long it takes a buyer who put down about 10% to get their loan down to 80% of the home's value. The loan starts at about 90% of the price. The animation measures how long past buyers took to reach 80%.

**2. What changes across the frames.**
- Frames 1–2: A single illustrative line slopes down from 90% toward the 80% line. This is the loan paid down on the normal schedule, and it reaches 80% at about 8 years.
- Frames 3–5: Many thin lines are added, one for each month someone bought between 1991 and 2016. They measure the loan divided by the home's value on paper, so they move with home prices as well as with payments. The lines spread out. Many drop faster than the schedule line, and many rise well above 90% before they come down.
- Frame 6: Two cases are highlighted. The typical buyer reached 80% in about 2 years. The slowest case (blue) took about 9 years, and its line climbed well above 90% along the way.

**3. What it means.** The schedule alone gets you to 80% in roughly 8 years. In practice the timing depended mostly on what home prices did after purchase. When prices rose, buyers got to 80% much sooner. When prices fell, their loan was a larger share of the home's value for years, and the slowest case took longer than the schedule. The footnotes say this is a measurement of past US buyers. It is history, not a forecast, and not a reason to buy, rent or wait.

**4. What a viewer would take away.** The video isn't telling you to buy or not buy. For someone like me with about 10% saved, the takeaways are:
- Don't count on a fixed number of years to reach 80%. The typical case was about 2 years, but 8 or 9 years is possible.
- Home prices, which I can't control, drive the timing as much as my payments do.
- If I buy, I should be able to afford the loan even if my equity grows slowly or my loan stays above 90% of the home's value for a while.
- The past isn't a promise. The data only covers the US from 1991 to 2016.

### R7 (strip B02-S02)
1. **The idea.** The animation is about how long it takes a buyer with a small down payment (about 10%) to get their loan down to 80% of the home's value. At 80% the buyer has 20% equity, which is the usual point where you can drop mortgage insurance. It compares the textbook payment schedule with what happened to real buyers.

2. **What changes across the frames.**
   - Frames 1–2: A single illustrative line starts at 90% loan-to-value and slowly falls to the 80% line. It gets there at about 8 years, which is "on the schedule." The label says this is a measurement, not a next step.
   - Frames 3–5: Many thin lines are added, one for each purchase month from 1991 to 2016. Each shows loan divided by the home's value on paper. They spread out a lot. Some drop quickly, and others rise well above 90% before they come down.
   - Frame 6: Two cases are highlighted. The typical buyer reached 80% in about 2 years, much faster than the 8-year schedule. The slowest case, in blue, rose and took about 9 years, which is longer than the schedule.

3. **What it means.** The schedule only counts loan paydown, so it gives one tidy number. Real buyers' ratios also move with home prices. In most cases, rising prices got people to 80% far sooner than the schedule says. For people who bought just before prices fell, the ratio went up and it took longer than the schedule. So the real timeline varied a lot, from about 2 years to about 9, depending on when someone bought and what the market did.

4. **Advice a viewer would take.** The animation gives no buy, rent or wait advice. It says outright that this is past buyers, measured, US only, and "history, not a forecast." The sensible takeaway is not to count on a fixed 8-year path to 20% equity. With a 10% down payment, expect the path to depend on the market. It could be quick, or it could be slow if prices drop. If you're thinking about buying, plan for the slow case. That means keeping a cash cushion and not stretching your budget, so a longer stretch of mortgage insurance and thin equity wouldn't hurt you. Don't treat the typical 2-year result as a promise.

### R8 (strip B18-S18)
1. **The idea:** The animation looks at how long it takes a new buyer with a small down payment to get their loan down to about 80% of the home's value. The 80% line is usually where mortgage insurance can come off. I'm inferring that from the "80%" label and the "mortgage insurance" caption in frame 6, because the frames never say it outright. It compares the lender's fixed paydown schedule ("on paper") with what actually happened to past US buyers. It uses real home-price history (FHFA index, via Freddie Mac and FRED), with every buyer lined up at their purchase date.

2. **What changes across the frames:**
   - **Frame 1:** Three example buyers appear: Owen (fast), Grace, and Victor (slow). Each has a line that falls toward the 80% mark, and the paths differ a lot.
   - **Frames 2–3:** The view zooms out to a spread of many past buyers over 10 years, with a "plan" line fixed at the start.
   - **Frame 4:** Numbers appear. The typical buyer took 23 months, and about 1 in 7 took more than 60 months. Two years matched the typical month, but not the slow cases and not the lender's step.
   - **Frame 5:** It shows a $400,000 home as a stack of money, in dollars of the day.
   - **Frame 6:** It contrasts "buying now + mortgage insurance" with "still renting, still saving."

3. **What it means:** Home prices drive how fast you build enough equity, not just your payments. The fixed schedule is only part of the story. In the past, most buyers got there in about two years, but some waited five years or more, and you can't know which group you'd land in. The captions say this is history, not a forecast, and US only.

4. **Advice a viewer would take:** Strictly, none. The video says, "Past buyers, measured · not a reason to buy, rent or wait," and "A measurement, not a next step." As a renter with about 10% saved, I'd take away three things:
   - Mortgage insurance might go away in around two years, but it could take much longer.
   - I shouldn't count on the optimistic timeline.
   - Buying and renting-and-saving are both left as open choices that depend on my own situation.

### R9 (strip B18-S18)
**1. What idea is this animation showing?**
It shows how long past home buyers who put down less than 20% paid for mortgage insurance. The chart tracks the loan against the home's value, with 80% and 75% marked on the left. Mortgage insurance seems to end once the loan falls to about 80% of the home's value. Each buyer's path comes from real price history (FHFA and Freddie Mac data via FRED). It is labeled "illustrative," and it is US only.

**2. What changes over time across the frames?**
- **Frame 1:** There is one wiggly line for how home prices actually moved. Next to it are flat or gently sloping lines for the scheduled paydown, and the axis runs 0 to 10 years.
- **Frames 2–3:** Many past buyers are layered on as a gray mesh, with three named examples (Owen, Grace and Victor). A vertical marker sits near year 2, and a note says the schedule is fixed at the start.
- **Frame 4:** Text says the typical buyer took about 23 months to get there, and about 1 in 7 took more than 60 months. Another note says about 2 years matched the typical month, not the slow cases and not the lender's own step.
- **Frame 5:** The picture shifts to a $400,000 home, shown as a stack of blocks with the bottom portion filled in, like a down payment or equity.
- **Frame 6:** Two choices appear, "buy now + mortgage insurance" and "keep renting, keep saving."

**3. What does it mean?**
The paper schedule says when the insurance should end, but real timing depends on what home prices did after each person bought. Most past buyers got out of mortgage insurance in about two years. A minority waited five years or more, because prices were flat or fell. So the cost of a small down payment varies a lot depending on when you buy.

**4. What advice, if any, would a viewer take from this?**
The video gives no direct advice. The captions say "not a reason to buy, rent or wait" and "a measurement, not a next step." As a renter with about 10% saved, I'd take a few things from it:
- Buying with 10% down and paying mortgage insurance is not a long-term trap. Typically it was short, but I shouldn't count on that.
- I should plan for the slow case, where the insurance lasts 5+ years, and check that I could afford that.
- The choice between buying now and renting while I save is still mine. The animation doesn't say which is better, and it isn't a forecast.

### R10 (strip B02-S02)
1. **The idea.** The animation shows how long it takes a buyer who puts down about 10% to get their loan down to 80% of the home's value. That is the point where private mortgage insurance (PMI) usually ends, though the frames never mention PMI. It compares the textbook payment schedule with what actually happened to past buyers.

2. **What changes across the frames.**
   - Frames 1–2 are labeled "illustrative." One line starts at 90% and slopes down to the 80% line at about 8 years. That is the schedule.
   - Frame 3 swaps the title to real data: loan as a percent of home value, one line per purchase month from 1991 to 2016. The data comes from FHFA and Freddie Mac via FRED.
   - Frames 4–5 fill in hundreds of gray lines, one for each purchase month. Many dip below 80% quickly. Others rise first, because home prices fell, and then come down slowly.
   - Frame 6 highlights two lines. The typical buyer reached 80% in about 2 years. The slowest case, shown in blue, took about 9 years, which is longer than the 8-year schedule.

3. **What it means.** The schedule is only a baseline. Home price changes mostly decide how fast your loan-to-value ratio falls, and paying down principal matters less. Most past buyers got to 80% much faster than the schedule says, because prices rose. Buyers who bought before a price drop waited longer than the schedule, since their loan was a larger share of a home worth less. The captions say this is a measurement of past US buyers. It is not a forecast.

4. **Advice a viewer would take.** The captions say plainly that this is "not a reason to buy, rent or wait." The only takeaway is to expect a wide range. With 10% down, reaching 80% could take anywhere from about 2 to 9 years, depending on prices after you buy. So I wouldn't count on a specific date for dropping the extra costs. I'd also leave some room in my budget in case it takes longer than 8 years.

### R11 (strip B18-S18)
**1. What idea is this animation showing?**
It looks at how long a buyer with a small down payment (about 10%) pays mortgage insurance. Mortgage insurance seems to end once the loan falls to about 80% of the home's value. The animation compares the fixed paper payoff schedule with what actually happened to past US buyers. It uses the FHFA/Freddie Mac house price index, with every buyer lined up at their purchase date. It is labeled "illustrative," and it says it is history, not a forecast.

**2. What changes over time across the frames?**
- **Frame 1:** Three past buyers appear side by side: Owen (fast), Grace (in between) and Victor (slow). Each has a line that starts near 80% and moves against a straight "on paper" schedule line. Victor's line wanders up and down with home prices before it finally drops.
- **Frames 2–3:** The three are stacked on one 0–10 year timeline, with many faint lines behind them for other past buyers. The note "schedule: fixed at the start" appears. The label "a plan" marks the starting point.
- **Frame 4:** Numbers are added. On paper, the typical time is 23 months, and about 1 in 7 buyers took more than 60 months. A callout says roughly 2 years matched the typical month, not the slow cases and not the lender's step.
- **Frame 5:** The view shifts to a $400,000 home with a stacked bar, probably showing the down payment and equity. The caption reads "A measurement, not a next step."
- **Frame 6:** Two options appear: a house and a person, labeled "buying now + mortgage insurance," and an apartment building labeled "still renting, still saving."

**3. What does it mean?**
The paper schedule says when you should reach 80%. In real life, home prices move, so the actual timing can be faster or much slower. For most past buyers it took about two years. For a minority, about 1 in 7, it took five years or more. The two-year figure is a historical typical case, not a promise.

**4. What advice, if any, would a viewer take from this?**
The video doesn't tell you what to do. The footer says the data is "not a reason to buy, rent or wait," and Frame 5 says it's "a measurement, not a next step." As a renter with about 10% saved, I'd take away three things:
- Buying with a small down payment can mean mortgage insurance for about two years, and sometimes much longer.
- I shouldn't count on the paper schedule when planning my budget.
- Buying and renting while saving are both presented as live options, and the decision is mine.

### R12 (strip B18-S18)
**1. The idea.** The animation shows how long a buyer with a small down payment might pay mortgage insurance. It follows past US buyers who all bought under the same rule, using the same house-price index (FHFA/Freddie Mac via FRED), lined up at their purchase date. The loan balance is measured against the home's value, with markers at 80% and 75%. The on-paper schedule says the balance should reach those lines on a fixed timetable. Real home prices moved the actual path faster or slower than that. The whole thing is labeled "illustrative."

**2. What changes across the frames.**
- Frame 1 shows three separate buyers, Owen (fast), Grace (in between) and Victor (slow). Each has a different wobbly line for their loan-to-value path, set against the straight on-paper schedule.
- Frames 2 and 3 stack many past buyers into one ridge-like chart over 0–10 years. Owen, Grace and Victor are marked along it, and the schedule is described as "fixed at the start."
- Frame 4 adds numbers. On paper the typical wait is 23 months, and about 1 in 7 buyers waited more than 60 months. A callout says roughly 2 years matched the typical month, "not the slow ones, not the lender's step."
- Frame 5 switches to a $400,000 home drawn as a stack of money, with a small slice (about the bottom tenth) in a different color. The note says "A measurement, not a next step" and that all dollars are in dollars of the day.
- Frame 6 shows a house with an insurance-style marker labeled "buying now + mortgage insurance" next to an apartment building labeled "still renting, still saving."

**3. What it means.** With about 10% down, you normally pay mortgage insurance until you build enough equity to reach the 80% mark, or 75% on the other line. How long that takes depends on both your payments and what home prices do. Most past buyers got there in around two years. A minority waited five years or more, mostly when prices were flat or fell. The schedule on paper is a best case, and real outcomes spread widely around it. Frames 5 and 6 compare that cost and timeline with continuing to rent while saving more.

**4. The advice a viewer would take.** The video gives no verdict. The captions say it is "not a reason to buy, rent or wait," that it covers the US only, and that it is "history, not a forecast." Someone like me, renting with about 10% saved, would take away three things:
- Expect mortgage insurance to last about two years in a typical case.
- Plan for it to last much longer, because about 1 in 7 past buyers waited more than five years.
- Don't treat the lender's payment schedule as a promise of when it ends.

The decision to buy now or keep saving is left to the viewer.

### R13 (strip B18-S18)
**1. The idea.** The animation looks at how long it takes a new homebuyer to get their loan down to a target loan-to-value level, shown as the 80% and 75% lines. It uses real US house-price history (FHFA and Freddie Mac data via FRED). The label says "illustrative," so the specific lines aren't a forecast. I'm inferring that the 80% line is where mortgage insurance can come off, but the image never says so outright. The point seems to be that the same payment schedule gives very different timelines depending on when you bought.

**2. What changes across the frames.**
- Frame 1 shows three example buyers, Owen (fast), Grace and Victor (slow). Each has the same fixed paydown schedule on paper, but their actual paths differ because house prices moved differently after each purchase.
- Frames 2 and 3 line up many past purchase dates on one 0–10 year axis. Each buyer's path starts at 80% and drifts toward 75%. Some get there quickly and some take years, so the paths spread out.
- Frame 4 adds numbers: on paper the typical case takes 23 months, but about 1 in 7 buyers took more than 60 months. It also notes that about 2 years matched the typical month, "not the slow ones, not the lender's step."
- Frame 5 switches to a $400,000 home shown as a stack of dollars, with the caption "a measurement, not a next step."
- Frame 6 compares "buying now + mortgage insurance" with "still renting, still saving."

**3. What it means.** The schedule on paper says one thing, but what happens depends on home prices after you buy. A typical buyer gets there in around two years. A meaningful minority, roughly one in seven, waited five years or more. The footer says this is past data for the US only, "history, not a forecast," and "not a reason to buy, rent or wait."

**4. The advice a viewer would take.** The video explicitly avoids telling you to buy, rent or wait. As a renter with about 10% saved, I'd take away three things:
- If I buy with a small down payment, I should expect to pay mortgage insurance for about two years, and plan for it possibly lasting much longer.
- The "typical" timeline isn't guaranteed, so I shouldn't budget as if it were.
- Buying now with insurance and renting while I keep saving are both legitimate options. The decision depends on my own finances and how long I plan to stay, not on this chart.

I'm reading these frames without audio or narration, so the details above are my best interpretation of the labels.

### R14 (strip B02-S02)
1. **The idea.** The animation shows how long it took past US home buyers who put down about 10% to get their loan down to 80% of their home's value. That is the point where a buyer typically no longer has to pay mortgage insurance. It compares the scheduled paydown with what actually happened, using FHFA and Freddie Mac data from FRED.

2. **What changes across the frames.**
   - Frames 1–2 show an illustrative line. It starts at a 90% loan-to-value ratio and slopes down to 80% at about 8 years, which is the "schedule." The label says this is a measurement, not a next step.
   - Frame 3 swaps in real data. It plots one line per purchase month from 1991 to 2016, and the lines start to fan out from the 90% starting point.
   - Frames 4–5 fill in the whole bundle of lines. Many drop to 80% quickly. Others rise first, because home values fell or the loan balance outpaced the home's value, and only come down much later.
   - Frame 6 highlights two lines. The typical buyer reached 80% in about 2 years, much faster than the 8-year schedule. The slowest case took about 9 years, and its loan share climbed well above 90% before it came down.

3. **What it means.** Paying down the loan on schedule is slow. In practice, home price changes mattered much more for how fast buyers built equity. In most cases rising prices got buyers to 80% far sooner than the schedule predicted. In a few cases falling prices left them underwater for years. The outcomes varied widely, and the 8-year schedule was neither typical nor a worst case.

4. **What a viewer would take from it.** The video gives no buy, rent or wait advice. The frames say it is "not a reason to buy, rent or wait," and that it covers the US only and is "history, not a forecast." A viewer with a 10% down payment could take away three things:
   - Expect to carry mortgage insurance for somewhere between about 2 and 9 years. The past range is wide, and the future could differ.
   - Don't count on price gains to get you to 80% quickly.
   - Plan for the slow case by keeping a cushion, and by not buying a home you might have to sell within a few years.

### R15 (strip B02-S02)
1. **The idea:** The animation shows how long it took past buyers who put 10% down to get their loan down to 80% of the home's value. The 80% line is probably the point where extra costs like mortgage insurance usually end, but the image doesn't say so. Frames 1 and 2 show an illustrative schedule. The loan starts at 90% of the price and falls to 80% by about 8 years from regular payments alone. Frames 3 to 6 swap that for real data: one line for each purchase month from 1991 to 2016, from FHFA and Freddie Mac data via FRED.

2. **What changes:** The single schedule line is replaced by a bundle of many gray lines. All of them start at 90%. Some drop quickly to 80%. Others rise well above 90% before they come back down. In frame 6 two lines are highlighted. The "typical" one reaches 80% in about 2 years, and the "slowest case" one takes about 9 years. That is slower than the 8-year schedule.

3. **What it means:** Paying down the loan on schedule is only part of the story, because the loan's share of the home's value also moves with the home's price. In most past cases, rising prices got buyers to 80% much faster than the schedule, about 2 years. In the worst case, prices fell and it took longer than the schedule, about 9 years. So the time it takes is uncertain and depends on the market.

4. **Advice a viewer would take:** The video gives no instruction to buy, rent or wait. The frames say this is "a measurement, not a next step," "not a reason to buy, rent or wait," and "US only · history, not a forecast." A viewer would take away that, with 10% down, you can plan around the 8-year schedule. Past buyers were often much faster, but some were slower, so you shouldn't count on a quick drop to 80%. As a renter with about 10% saved, I'd read this as a way to budget for the range of outcomes, from about 2 to 9 years. I wouldn't treat it as a signal to act now.

### R16 (strip B18-S18)
1. **The idea.** The animation looks at how long a first-time buyer with a small down payment would pay mortgage insurance. It lines up many past home-price histories (FHFA and Freddie Mac data via FRED) at the month of purchase. It compares them with a fixed paydown schedule, and the schedule is labeled "on paper." The lines at 80% and 75% appear to be loan-to-value thresholds, where mortgage insurance can come off. The labels are small, so that reading is my inference.

2. **What changes.**
   - Frame 1 shows a few lines over 10 years: the schedule falling toward the thresholds and a price line rising and then falling.
   - Frame 2 adds a dense bundle of past price paths and a vertical marker labeled "a plan." Three example buyers, Owen, Grace and Victor, sit along the way.
   - Frame 3 adds the note that the schedule is "fixed at the start."
   - Frame 4 adds the numbers: on paper, the typical case takes 23 months, and about 1 in 7 buyers takes more than 60 months. It also says that about 2 years matched the typical month, "not the slow ones, not the lender's step."
   - Frame 5 switches to a $400,000 home drawn as a stack of blocks, with the bottom portion shaded as the owner's share.
   - Frame 6 shows a house, a person and an apartment building, labeled "buy now + mortgage insurance" and "keep renting, keep saving."

3. **What it means.** The date mortgage insurance ends is not fixed. It depends on the schedule and on what home prices do after you buy. In the typical past case it ended in about two years. In roughly one in seven cases it took more than five years. Every frame is marked "illustrative," "history, not a forecast," and "US only."

4. **What a viewer would take away.** The animation gives no buy, rent or wait advice, and it says so: "not a reason to buy, rent or wait" and "a measurement, not a next step." The takeaway is to treat mortgage insurance as a cost with an uncertain end date. If you're buying with about 10% down, the typical past case was around two years, but plan for the chance that it takes much longer. Frame 6 sets "buy now with mortgage insurance" beside "keep renting and saving" as two real options, and the choice is left to you.

### R17 (strip B02-S02)
1. **The idea.** The animation shows how long it takes a buyer who puts down about 10% to get their loan down to 80% of the home's value. At that point the buyer has 20% equity, which is the usual threshold for dropping private mortgage insurance. The scheduled paydown takes about 8 years. The animation then compares that schedule with what actually happened to past US buyers.

2. **What changes over time.**
   - Frames 1 and 2 are labeled "illustrative." A single line starts near 90% loan-to-price and slopes down to the 80% line. It reaches 80% at about 8 years, which is the "schedule."
   - Frame 3 switches to real data (FHFA and Freddie Mac, via FRED). It shows one line for each purchase month from 1991 to 2016. The lines start to fan out from the starting point.
   - Frames 4 and 5 fill in the whole bundle of lines. Many drop below the schedule quickly. Others rise well above 90% before coming back down.
   - Frame 6 highlights two cases. The typical buyer reached 80% in about 2 years, much faster than the schedule. The slowest case, in blue, took about 9 years. Its loan-to-value ratio went up first, which would happen if the home's value fell.

3. **What it means.** Loan-to-value depends on home prices as well as on paying down the loan. In most of the historical cases, rising prices got buyers to 80% much sooner than the schedule predicts. In the worst cases, falling prices pushed the ratio above where it started and delayed reaching 80% past the schedule. The real range was wide, from roughly 2 years to 9 years or more.

4. **What a viewer would take from it.** The animation doesn't tell anyone to buy, rent or wait. Its captions say "Past buyers, measured · not a reason to buy, rent or wait" and "US only · history, not a forecast." A viewer should come away with a few points:
   - Don't assume the 8-year schedule is exact.
   - The typical outcome was faster, but a bad stretch for prices could make it slower.
   - Equity and the date you can drop PMI depend on the housing market as well as on your payments.
   - Plan for a range of outcomes, and don't treat the past as a promise.

As a renter with about 10% saved, I'd read this as a reason to keep a cushion and not count on price gains to build equity.

### R18 (strip B02-S02)
1. **The idea.** The animation shows how long it takes a buyer who starts with a small down payment to get their loan down to 80% of the home's value. The 80% line is the usual point where private mortgage insurance can come off. The sources are FHFA and Freddie Mac data via FRED. The early frames are labeled "illustrative," and the later ones use real data. The animation compares the loan's fixed paydown schedule with what actually happened to past buyers.

2. **What changes across the frames.**
   - Frames 1–2: A single smooth line starts near 90% and falls toward the 80% line. It reaches 80% at about 8 years, which is the amortization schedule.
   - Frame 3: The label changes to "Loan ÷ home value on paper." Many faint lines start to appear at the left. Each line is one purchase month, from 1991 to 2016.
   - Frames 4–5: The faint lines fan out into a large cloud. Some drop below the schedule line quickly. Others rise well above it, to roughly 90% or more, before they fall.
   - Frame 6: Two cases are highlighted. The typical buyer reached 80% in about 2 years, faster than the schedule. The slowest case took about 9 years and rose a long way above 90% on the way. That buyer's home value fell, so their loan was a bigger share of it.

3. **What it means.** The schedule is only a baseline. In practice, the loan-to-value ratio depends mostly on what home prices do. Rising prices got most past buyers to 80% much sooner than 8 years. Falling prices pushed some buyers up and kept them there longer. The spread shows the range of outcomes, and the schedule is only one point inside it.

4. **Advice a viewer would take.** The frames give no buy, rent, or wait advice. The captions say "Past buyers, measured · not a reason to buy, rent or wait" and "US only · history, not a forecast." A viewer should come away with a few cautions:
   - Don't count on price gains to remove mortgage insurance quickly.
   - Plan for the 8-year schedule or longer as the safer assumption.
   - Know that a down payment around 10% can leave you exposed if prices fall.

   For you, as a renter with about 10% saved, the takeaway is to budget for mortgage insurance lasting years, not months. Past results don't predict what happens next.

### R19 (strip B02-S02)
1. **The idea:** The animation shows how long it takes a buyer who put 10% down to get their loan down to 80% of the home's value. The loan starts at 90% of the price. At 80%, I'd guess, you'd typically stop paying mortgage insurance. The first two frames are an illustrative schedule: if you only pay down the loan on the normal payment schedule, you get there in about 8 years.

2. **What changes:** Frames 1 and 2 draw a single line sloping down from 90% toward the 80% line. It reaches 80% at about 8 years. Frames 3 to 5 swap that for many thin gray lines, one for each month someone bought a home between 1991 and 2016. The lines fan out. Many drop to 80% much faster than the schedule, and many rise above 90% first before coming back down. Frame 6 highlights two cases. The typical buyer reached 80% in about 2 years. The slowest case took about 9 years, and its line climbed well above 90% along the way.

3. **What it means:** The 8-year schedule is only a baseline. In real life, the loan as a share of the home's value also depends on what happens to the home's price. When prices rose, past buyers hit 80% quickly, and the typical buyer did it in about 2 years. When prices fell or stalled, the loan was a bigger share of the home's value and it took longer. Even the slowest buyer took only about a year longer than the schedule. The captions say this is measured history, for the US only. It is not a forecast, and it is not a reason to buy, rent or wait.

4. **Advice a viewer would take:** The video gives no buy-or-wait advice, and it says so directly. As a renter with about 10% saved, I'd take away three things:
   - Putting 10% down doesn't mean I'd be stuck with mortgage insurance for the full 8 years. Past buyers usually got out much sooner.
   - How fast I get out depends on home prices, which I can't control or predict, and the past isn't a promise.
   - The timeline for dropping to 80% varies a lot, so I shouldn't count on the fast case in my budget. I'd plan for the possibility that it takes the full 8 years or longer.

### R20 (strip B18-S18)
I read this as a chart about how long mortgage insurance lasts for someone who buys with a small down payment. This is my interpretation of the image, because it has no narration.

**1. What idea is this animation showing?**
It shows how long a buyer with a small down payment might pay mortgage insurance. Insurance usually ends once the loan falls to about 80% of the home's value. The chart uses real past US home-price data (FHFA and Freddie Mac, via FRED). It lines up many past buyers at the moment of purchase and applies the same rule to each. The "ILLUSTRATIVE" tag tells me the specific figures are examples.

**2. What changes over time across the frames?**
- **Frame 1:** There is one wiggly line for the price history, plus a few flat or sloping lines for the loan schedule. The axis runs from 0 to 10 years, with 75% and 80% marked on the side.
- **Frames 2 and 3:** Many faint lines pile up to show lots of past buyers. Three named examples (Owen, Grace and Victor) stand out. A vertical bar marks "a plan", and the label "schedule: fixed at the start" appears.
- **Frame 4:** The chart gets numbers. On paper, the typical buyer reached the 80% mark in about 23 months, and about 1 in 7 buyers took more than 60 months. A note says roughly 2 years matched the typical month. It was not the slow cases, and it was not the lender's own step.
- **Frame 5:** The chart gives way to a $400,000 home drawn as a stack of green slices. The bottom slice is the buyer's down payment, and a small house sits next to it. The caption reads "A measurement, not a next step."
- **Frame 6:** A person stands between two options. One is "buy now + mortgage insurance" and the other is "keep renting, keep saving."

**3. What does it mean?**
The loan schedule is fixed on day one, but how fast a buyer actually gets out of mortgage insurance depends on what home prices do. Owen, Grace and Victor are past buyers whose timing ranged from quick to very slow. A typical buyer got there in under 2 years. A meaningful minority waited 5 years or more, and a few waited close to 10. The repeated footers ("Past buyers, measured · not a reason to buy, rent or wait" and "history, not a forecast") say the chart describes the past and doesn't predict anything.

**4. What advice, if any, would a viewer take from this?**
There is no direct advice, and the video says so on purpose. The takeaway for someone like me is to expect that mortgage insurance might last about 2 years or might last much longer. I'd budget for the slow case instead of counting on the typical one. The last frame lays out the choice between buying now with insurance and renting while saving more, and it doesn't pick one. The decision is still mine, and the chart only tells me what past buyers experienced.

### R21 (strip B02-S02)
1. **The idea:** The animation shows how long it takes a first-time buyer with a small down payment to get their loan down to 80% of the home's value. It starts with a textbook case, where you put 10% down and the loan is 90% of the price. On the regular payment schedule, the loan falls to 80% in about 8 years. That 80% mark is the usual point where extra costs for a small down payment, such as mortgage insurance, can come off. The animation then checks that schedule against real data.

2. **What changes across the frames:**
   - Frames 1 and 2 draw one illustrative line, labeled "ILLUSTRATIVE." It starts at 90% and slopes down until it meets the 80% line at about 8 years.
   - Frame 3 swaps in real data. The chart is now "loan as % of home value, one line per purchase month, 1991–2016," from FHFA and Freddie Mac data via FRED. A bunch of lines start fanning out from 90%.
   - Frames 4 and 5 fill in the full set of lines. Some drop quickly. Many rise first, because home prices fell or loans grew relative to value, and then come down much later.
   - Frame 6 highlights two cases. The typical buyer reached 80% in about 2 years, much faster than the schedule's 8. The slowest case took about 9 years, longer than the schedule.

3. **What it means:** The 8-year schedule is only a baseline that assumes the home's value doesn't change. In real life, home price changes mattered more than paydown. Most past buyers got to 80% much sooner because their homes appreciated. A few were stuck for longer than the schedule says because prices fell. So the time to reach 80% varied widely, from about 2 years to about 9 years or more.

4. **What a viewer would take away:** The captions say this is "a measurement, not a next step" and "not a reason to buy, rent or wait." It also says "US only · history, not a forecast." So there's no instruction to buy or not buy. The takeaway is about expectations. Don't count on reaching 80% in exactly 8 years, and don't assume it will be fast. It depends heavily on what home prices do, which nobody can predict. If I were buying with about 10% down, I'd plan for the slow end of the range and treat an early drop to 80% as a bonus.

### R22 (strip B02-S02)
1. **The idea.** The animation shows how long it takes a buyer who put down 10% to get their loan down to 80% of the home's value. That is the 20%-equity mark, which is where people usually think of private mortgage insurance coming off. The loan starts at about 90% of the price. The straight "schedule" line shows how fast regular payments alone would get it to 80%. The animation then compares that line with what actually happened to real US buyers.

2. **What changes across frames.**
   - Frames 1 and 2 draw the illustrative schedule line. It slopes down from 90% and reaches the 80% line at about 8 years.
   - Frame 3 adds a thin line for each purchase month from 1991 to 2016. Each line is the loan divided by the home's value on paper.
   - Frames 4 and 5 fill in the full bundle of lines. Many drop below the schedule line quickly. Others rise well above 90% before they come back down.
   - Frame 6 highlights two cases. The typical buyer got to 80% in about 2 years. The slowest buyer took about 9 years, and their line rose a long way first.

3. **What it means.** The 8-year schedule is only what payments alone would do. In practice, home values moving up or down matter as much as the payments. Most past buyers reached 80% much faster than the schedule, probably because prices rose. Some bought at a bad time and sat above 90% for years, so they ended up slower than the schedule. The result depends a lot on when you buy, and that is outside your control.

4. **What a viewer would take from it.** There isn't a buy, rent or wait instruction, and the video says so. The caption reads "Past buyers, measured · not a reason to buy, rent or wait," and adds "history, not a forecast." It is also US-only. The useful takeaway is to plan for a range. With 10% down, reaching 80% could take about 2 years or about 9, so don't count on dropping mortgage insurance by a certain date. I'd keep a cushion in case the slow case happens.

### R23 (strip B18-S18)
1. **The idea.** The animation shows how long a buyer with a small down payment would pay mortgage insurance. It compares the fixed paydown schedule "on paper" with what happened to real past buyers. The same rule and the same home price index (FHFA/Freddie Mac data via FRED) were applied to every buyer, lined up at their purchase date. The vertical axis seems to show the loan as a share of the home's value, running from about 80% down to 75%. The horizontal axis runs 0 to 10 years. I'm inferring that this is the point where mortgage insurance can be dropped, and the image doesn't say so outright.

2. **What changes across the frames.**
   - Frame 1 shows a few lines, including the schedule and one real path.
   - Frames 2 and 3 add a dense fan of many past buyers' paths. Three example buyers are labeled Grace, Owen and Victor, and "a plan" marks the schedule fixed at the start.
   - Frame 4 adds numbers: on paper the typical case takes 23 months, and about 1 in 7 buyers were still not there after 60 months. A note says a two-year wait matched the typical month, not the slow cases and not the lender's step.
   - Frame 5 switches to a $400,000 home next to a tall stack of green blocks, with the bottom blocks highlighted.
   - Frame 6 shows a house with "buy now + mortgage insurance" and an apartment building with "keep renting, keep saving," with a person standing between them.

3. **What it means.** How long you pay mortgage insurance depends partly on the plan and partly on what home prices do after you buy. Most past buyers got out in roughly two years, but some took much longer, and the spread was wide. The repeated captions say this is history and not a forecast, applies to the US only, and is not a reason to buy, rent or wait. Frame 5 is labeled "A measurement, not a next step."

4. **What a viewer would take from it.** The video avoids telling you what to do. The only takeaway is to understand the choice. Buying with a small down payment means paying mortgage insurance for an uncertain length of time, and the typical case is about two years with a real chance of much longer. Renting and saving is the other path. As a renter with about 10% saved, I'd use this to plan for the slow case. I'd budget for the insurance lasting longer than two years instead of treating the typical number as a promise. The animation doesn't say which path is better.

### R24 (strip B18-S18)
1. **The idea:** The animation looks at how long past US home buyers with a small down payment took to get their loan down to 80% of the home's value. That's the point where mortgage insurance can usually come off. It lines up many past buyers by their purchase date and uses one rule and one price index (FHFA/Freddie Mac data via FRED). Three example buyers, Grace, Owen and Victor, show different paths. The labels say the figures are illustrative, US-only and "history, not a forecast."

2. **What changes across the frames:**
   - Frame 1 shows a single price-history line against flat and sloping lines at 80% and 75%.
   - Frames 2 and 3 add a dense bundle of lines for many past buyers. A vertical marker labeled "a plan" appears, and the schedule is "fixed at the start."
   - Frame 4 adds numbers. On paper, the typical buyer took about 23 months, and about 1 in 7 took over 60 months. It also notes that about 2 years matched the typical month, not the slow cases and not the lender's step.
   - Frame 5 switches to a $400,000 home next to a tall stack of segments, mostly filled in at the bottom. I can't tell exactly what the stack measures, but it seems to be the down payment or equity share. The caption reads "A measurement, not a next step."
   - Frame 6 shows a house, a person and an apartment building. The labels are "buy now + mortgage insurance" and "keep renting, keep saving."

3. **What it means:** The schedule on paper, which is how long it should take to reach 80%, can differ from what actually happened to past buyers, because home prices moved. Most buyers got there in roughly two years, but a minority waited much longer. The animation is measuring that spread. It is not predicting what will happen to me.

4. **Advice a viewer would take:** There's no direct advice, and the video says so: "not a reason to buy, rent or wait." Frame 6 sets out the two choices without picking one. As a renter with about 10% saved, I'd take away three things:
   - Buying with under 20% down means paying mortgage insurance for a while.
   - It would probably last about two years, but it could last much longer.
   - I should plan for the slower case instead of assuming the typical one.

   I'd still have to decide for myself, using my own budget and how long I plan to stay.
