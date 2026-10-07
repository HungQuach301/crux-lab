# Grading packet (blind). Independent grader. Each label is one reader's answers about one silent 6-frame strip; the strip id is given so you compare against its muted read. Grade literally.

## Rubric
- **Chấm:** người chấm độc lập mù tập; nghĩa 1 / 0,5 / 0 so với "muted read" của `review-c3/spans.json`; cờ khuyên theo **A9** (thận trọng chung — tự kiểm số, hỏi bên cho vay — không tính; khuyên mua/chờ/bán/chọn tính). Người đọc đúng = nghĩa 1 và khuyên_tính false.


Muted read (đáp án đúng) theo hình:
- B03-S03: Hitting the 80 % line on paper is one line; a second, lower line (75 %, early years) and three steps (request, appraisal, wait) still stand before 'insurance removed'.
- B08-S08: A second marker a little later, at 78 %: 'ends automatically'. Both markers sit on the payment line; the house's value is nowhere on the chart.
- B14-S14: The zoom frame lands on the tallest bar: bought October 2005, 112 months on paper, taller than that month's schedule mark.
- B17-S17: Victor's panel: the index line rises a little, then falls for years; his on-paper line stays above 80 % long after his schedule line has crossed it at payment 90.
- B18-S18: Three panels side by side, aligned at purchase: one fixed schedule band and a fan of on-paper lines from fast to slow; a vertical 'your plan' marker stands between the schedule band and the fan; the 75 % line stays visible under all of them.

Output JSON only: {"R1": {"score": 1|0.5|0, "advice": true|false, "caution_only": true|false, "why": "<one line>"}, ...}

### R1 (strip B18-S18)
I only opened the one image. Some labels are small, so parts of my reading are inferences.

**1. What idea is the animation showing?**
It shows how long a first-time buyer with a small down payment might pay mortgage insurance. Mortgage insurance can come off once the loan falls to about 80% of the home's value. The chart compares two ways of getting there. One is the lender's fixed paydown schedule. The other is what actually happened to past buyers, using US home price and mortgage rate data (FHFA, Freddie Mac, FRED). Every frame is labeled "illustrative" and "history, not a forecast."

**2. What changes over time across the frames?**
- Frame 1 shows a few lines drifting down from 80% toward 75% over 10 years. That includes one wiggly line for the "on paper" path and flatter lines for the schedule.
- Frame 2 adds a dense cloud of many past buyers' paths. Three example buyers, Grace, Owen and Victor, are marked at a "plan" point near the start.
- Frame 3 adds the note "schedule: fixed at the start."
- Frame 4 adds the numbers. The typical case took about 23 months, and about 1 in 7 buyers took more than 60 months. It also says roughly 2 years matched the typical month, "not the slow ones, not the lender's step."
- Frame 5 shows a $400,000 home next to a tall stack of blocks with the bottom ones highlighted. It is captioned "A measurement, not a next step."
- Frame 6 shows a house with mortgage insurance on one side and an apartment building on the other. The labels are "buy now + mortgage insurance" and "keep renting, keep saving," with a neutral figure in between.

**3. What does it mean?**
The schedule you're given at closing is only one possible path. Home prices move, so the real time to drop mortgage insurance varied a lot. Historically it was often about 2 years, but sometimes much longer, and for about 1 in 7 buyers it ran past 5 years. The video is measuring that spread. It is not predicting what will happen to you.

**4. What advice would a viewer take from this?**
The video avoids telling you to buy, rent, or wait. The closing frames present both options as legitimate. A viewer would likely take away three things:
- Don't assume mortgage insurance will end quickly. Budget as if it could last several years.
- Don't treat the typical case, about 2 years, as a promise.
- Make the buy-or-rent decision on your own finances. In my situation, that means checking whether I could afford the payment plus insurance if it lasted 5+ years.

### R2 (strip B03-S03)
**1. The idea:** Putting down less than 20% usually means paying mortgage insurance. Reaching 80% loan-to-value on paper doesn't automatically end it. The loan owner has rules for dropping it. The image never says "mortgage insurance" outright, so I'm inferring that from "insurance still on" and the 80% line.

**2. What changes across the frames:**
- Frame 1 shows two stacks, the home's value and the loan, with the loan sitting at the 80% line. The label says this is measured from past buyers (FHFA and Freddie Mac data).
- Frame 2 shows a house with a small gold roof marker and the words "insurance still on." The loan is at 80%, but the insurance hasn't gone away.
- Frame 3 shows the same stacks, now with the rule "request · appraisal · wait." You have to ask, pay for an appraisal, and wait.
- Frame 4 adds the Fannie Mae numbers: wait at least 2 years, and get the loan to 75% or less. The 80% label fades, and a gold band marks the gap between 80% and 75%.
- Frames 5 and 6 show three similar houses with three different people. The point seems to be that this plays out for many ordinary buyers, with the "US only, history, not a forecast" caveat.

**3. What it means:** Hitting 80% doesn't switch the insurance off by itself. If you're relying on the home's value having gone up, the loan owner can require a formal request, an appraisal, a waiting period, and a lower loan balance of 75%. The "illustrative" tags and the repeated "not a forecast" and "not a reason to buy, rent or wait" lines tell me the video is explaining a mechanism. It isn't predicting prices or telling anyone what to do.

**4. What I'd take from it as a first-time buyer with about 10% saved:**
- Expect to pay mortgage insurance, and don't assume it ends the day I reach 80%.
- Before choosing a lender, ask who owns or services the loan and what their rules are for removing insurance. I'd ask about the waiting period, the appraisal cost, and whether they use the 75% threshold.
- Paying the balance down, or having the home gain value, can shorten the time, but only through that request process.
- The video doesn't tell me whether to buy now or keep renting. I'd use it to add the cost of insurance and the timeline for removing it to my budget.

### R3 (strip B03-S03)
I'm going only by what the image shows, and some of it is my interpretation.

**1. What idea is this animation showing?**
It looks like it's about getting rid of mortgage insurance on a home loan. Frame 2 says "insurance still on," and the yellow marker on the house seems to stand for that. The loan sits at "80% on paper" of the home's value. The animation says that reaching 80% on paper doesn't automatically end the insurance. The loan's owner has its own process.

**2. What changes over time across the frames?**
- **Frames 1 and 3:** The home-value bar gets taller while the loan bar stays about the same. The loan is therefore a smaller share of the home's value.
- **Frame 3:** The text adds the loan owner's rule: request, get an appraisal, wait.
- **Frame 4:** The line for the Fannie Mae test moves from 80% down to 75%. The gold gap on the loan bar shows how much further the balance has to fall.
- **Frames 5 and 6:** Three similar homes with three different people appear. This seems to stand for many past buyers, not one person's case.

**3. What does it mean?**
Hitting 80% loan-to-value on paper isn't enough. The rules shown are:
- You have to ask for the insurance to be removed.
- You have to pay for an appraisal.
- You have to wait.

The Fannie Mae example adds two conditions: at least 2 years of waiting, and a loan at or below 75% of the value. The tags and captions say this is illustrative. They also say it's US-only history from FHFA and Freddie Mac data, and that it's a measurement, not a forecast.

**4. What advice, if any, would a viewer take from this?**
The animation says outright that it isn't a reason to buy, rent, or wait. The useful takeaway for me is practical. With about 10% down, I should expect mortgage insurance. Before buying, I should ask who will own my loan and what their removal rules are. If I buy, I shouldn't assume the insurance drops off on its own. I'd need to track my loan balance against my home's value, and then request removal and get an appraisal.

### R4 (strip B17-S17)
1. **The idea.** The animation follows one past buyer, "Victor," who bought in October 2005 with a 6.07% mortgage. It asks how the buyer's equity compares with the home's price over the next 10 years. The 80% line looks like the loan-to-value mark, where a down payment of about 20% gets you there. The chart uses FHFA and Freddie Mac data from FRED, and it is labeled "illustrative."

2. **What changes across the frames.**
   - Frame 1 shows only the empty chart with the 80% line.
   - In frame 2, two lines start to draw. One is the loan balance on its normal paydown schedule, which drifts slowly down. The other is the loan balance measured against the home's price index, and it wobbles. A blue price-index line draws below them.
   - In frame 3, the price index rises, then falls well below its starting level around years 5 to 7, then partly recovers. The loan-to-value line rises above 80% and then falls back.
   - Frames 4 and 5 are the finished chart. They show "on paper: 112 months," meaning the loan hit 80% on schedule after about 9 years and 4 months. They also show "index still 3.3% below purchase," meaning home prices were still below Victor's purchase price at that point.
   - Frame 6 drops the chart and shows a house with a question mark.

3. **What it means.** A loan's paydown schedule says one thing, and what the housing market does can say another. Victor's schedule looked fine on paper. The market pushed the loan above 80% of the home's value for years, and prices were still below the purchase price after nearly a decade. A buyer who put down about 10% would have been in a worse spot than the chart shows. The closing caption says this is history, not a forecast, and not a reason to buy, rent or wait.

4. **What a viewer would take away.** The video doesn't tell anyone what to do. A viewer would probably come away with these points:
   - Don't count on a home's price going up, especially over a short holding period.
   - Plan to stay long enough to ride out a dip.
   - Keep a cushion, so you can cover payments without having to sell at a bad time.
   - Know that a small down payment leaves you with little equity if prices drop.

   As a renter with about 10% saved, I'd read it as a caution about timing and risk, not a verdict on buying. This was one buyer at one bad moment, so it's a stress test and not a prediction.

### R5 (strip B18-S18)
**1. What idea is this animation showing?**
It looks like it's about how long a first-time buyer with a small down payment would pay mortgage insurance. The lines seem to track the loan as a share of the home's value, falling from about 80% toward 75%. The animation compares the fixed repayment schedule (the "on paper" path) with what actually happened to past buyers. It replays every past purchase date under the same rule and the same price index (FHFA and Freddie Mac data via FRED), lined up at the moment of purchase.

**2. What changes over time across the frames?**
- **Frame 1:** a few lines run across a 0–10 year axis. One wiggly line shows what actually happened, and the flatter lines show the schedule.
- **Frames 2–3:** a bundle of many thin lines appears, one per past buyer. Three example buyers are labeled: Owen at the quick end, Grace in the middle, and Victor at the slow end. A marker bar sits near year 2, with the note "schedule: fixed at the start."
- **Frame 4:** the labels get specific. It says the typical wait was 23 months, and about 1 in 7 buyers waited more than 60 months. It also says roughly 2 years matched the typical month, "not the slow ones, not the lender's step."
- **Frame 5:** the picture switches to a $400,000 home next to a stack of bars, with the bottom bars highlighted. That probably shows the share of the price that is equity, or the amount that has to be reached.
- **Frame 6:** a house labeled "buy now + mortgage insurance" and an apartment building labeled "keep renting, keep saving" sit on either side of a person.

**3. What does it mean?**
The apparent point is that mortgage insurance usually doesn't last forever. In past US data, buyers typically reached the cutoff in about 2 years, but the spread was wide. Some buyers took five years or more, and the written schedule alone didn't predict how long it took. The repeated captions say this is history, US-only, illustrative, and "not a forecast."

**4. What advice, if any, would a viewer take from this?**
The video avoids giving direct advice. Its own text says it is "not a reason to buy, rent or wait" and "a measurement, not a next step." As a viewer with about 10% saved, I would take away a few things:
- Paying mortgage insurance on a small down payment is probably temporary.
- I should plan for the slow case, not just the typical one.
- Buying now with insurance and renting while saving are both presented as legitimate choices. The decision is mine, and it should rest on my own budget and plans, not on this chart.

I'm reading the axes and labels from a small image, so the exact meaning of the lines and the stack of bars is my best interpretation.

### R6 (strip B14-S14)
1. **The idea.** The animation shows how long it took past US home buyers to reach 80% equity, which is the point where private mortgage insurance can come off. It is the "months to 80% on paper" figure. Each bar is a purchase month, and its height is how many months that cohort needed. Data is from FHFA and Freddie Mac via FRED. The bar for October 2005 is highlighted at 112 months (9 years 4 months). That is the tallest part of the chart. Buyers from the mid-2000s peak waited much longer than buyers before or after them.

2. **What changes across the frames.**
   - Frame 1 shows only the bars with the October 2005 bar marked.
   - Frame 2 adds a bracket and the label "height = months to 80% on paper."
   - Frame 3 adds an "ILLUSTRATIVE" tag and a line over the chart. Its label reads "schedule at that rate: 90 payments", meaning a normal payment schedule would reach 80% in about 90 payments. The line seems to be a mortgage-rate or price series.
   - Frames 4 to 6 add the caption "national average, not one home." The marked bar and the line stay in place.

   The bars are the same in every frame. Only the annotations are added.

3. **What it means.** On paper, the October 2005 buyer should have hit 80% in about 90 months. In practice it took 112, which is about 22 months longer. The likely reason is that prices fell after the 2005–2006 peak and wiped out early equity, so those buyers waited longer to drop PMI. Buyers whose purchase month fell outside that peak reached 80% much sooner, and the bars before and after it are much shorter. The caption says this is a national average, not a prediction for any one home.

4. **What a viewer would take away.** The video says outright that this is "not a reason to buy, rent or wait," and that it is "history, not a forecast." The only real advice is about risk:
   - Timing and local prices can add years to how long it takes to build equity.
   - With about 10% down, you shouldn't count on reaching 80% quickly.
   - You should have a cushion and plan to stay put for a long time.

   I'd treat it as a reminder not to rely on fast appreciation. It doesn't say whether to buy now.

### R7 (strip B17-S17)
1. **The idea:** The animation follows one past buyer, "Victor," who bought in October 2005 with a 6.07% mortgage. It tests what happens to a low-down-payment buyer when home prices fall. It plots his equity against the 80% loan-to-value line, the point where private mortgage insurance usually can be dropped. It also plots the price index (FHFA/Freddie Mac data via FRED) relative to what he paid.

2. **What changes:**
   - **Frame 1:** There is only the 80% line on a 0–10 year axis.
   - **Frame 2:** Two lines start to draw. The "on paper" schedule line and his actual loan-to-value line begin together near the 80% line. The blue price index sits below and starts to dip.
   - **Frame 3:** The price index falls well below its starting level, bottoming around year 6. His loan-to-value line rises well above 80% because the home is worth less. The scheduled paydown line drifts down alone.
   - **Frame 4:** The lines finish. His loan-to-value line only falls back to the 80% line around year 9 to 10. The schedule had it reaching 80% earlier. The caption says "on paper: 112 months" and "index still 3.3% below purchase."
   - **Frame 5:** Same as frame 4.
   - **Frame 6:** A house with a "?" over it, which poses the buy-or-not question.

3. **What it means:** On paper, paying down the loan on schedule would have gotten Victor to 80% in 112 months, about 9 years and 4 months. Falling prices made his real equity lag far behind that schedule. About 10 years after buying, the price index was still 3.3% below his purchase price. A buyer with a small down payment can be stuck with a high loan-to-value ratio, and the costs that come with it, much longer than the payment schedule implies. The chart is labeled "illustrative," and it says "history, not a forecast."

4. **Advice a viewer would take:** The video says plainly that this is "not a reason to buy, rent or wait," so it gives no direct instruction. The takeaways I'd draw are about risk:
   - Don't assume the amortization schedule alone will build equity. Prices matter, especially with about 10% down.
   - Plan to stay put for a long time, and keep an emergency cushion so you aren't forced to sell during a dip.
   - Treat the 80% date as uncertain, because insurance costs can last longer than expected.
   - It's one buyer in one period, so it shows what can happen, not what will happen.

### R8 (strip B08-S08)
1. **The idea:** The animation shows when private mortgage insurance (PMI) can be removed under the federal Homeowners Protection Act (12 U.S.C. 4902). As you pay down the loan balance, it falls to certain thresholds. At those thresholds you can ask to cancel PMI, or it ends on its own. The example is labeled "illustrative." The numbers appear to describe a $400,000 home, since 80% of the original value is $320,000.

2. **What changes over time:**
   - A sloping band, which I read as the loan balance, falls toward two horizontal lines.
   - The first line is 80% of the original value, or $320,000. The balance reaches it at payment 99, and the label there says "may request."
   - The second line is 78%, or $312,000. The balance reaches it at payment 114, about 9.5 years in, and the label says PMI "ends automatically."
   - Frames 5 and 6 zoom out to the whole 360-payment (30-year) schedule. They show the balance curve falling slowly at first and faster later. Payments 99 and 114 are marked on it, next to a "home value" icon.
   - Frame 1 adds the conditions: a written request, and payments current.
   - Frame 6 adds that this is "based on the schedule only."

3. **What it means:** The thresholds are measured against the original home value and the original payment schedule. They are not measured against what the home is worth today. The caption "A measurement, not a next step" suggests that reaching a threshold doesn't cancel PMI by itself. You can ask for cancellation at 80%. Automatic termination at 78% is the backstop if you never ask.

4. **Advice a viewer would take:**
   - If you put down less than 20%, as I would with about 10% saved, PMI is a temporary cost, not a permanent one.
   - Track when your balance will hit 80% of the original price. Then send your servicer a written request, and keep your payments current so you qualify.
   - Don't wait for the automatic cutoff at 78%, because asking at 80% saves you the payments in between.
   - The image only shows the schedule-based timeline. It says nothing about getting PMI removed sooner by paying extra or by reappraising a home that has gained value. Those routes may exist, but you'd need to check them with your lender.

### R9 (strip B14-S14)
1. **The idea.** The animation shows how long it took past US home buyers to build 80% equity "on paper", by month of purchase. That's the point where a mortgage balance falls to 80% of the home's original price. The data comes from FHFA and Freddie Mac via FRED. Each bar is a purchase month, and its height is the number of months until that buyer reached 80% on paper. The highlighted bar is October 2005, which took 112 months (9 years 4 months). A second line, marked "illustrative", shows that a plain payment schedule at that mortgage rate would reach 80% in about 90 payments.

2. **What changes.** Frame 1 shows only the bars, with October 2005 marked. The bars are low for early purchases, jump sharply around 2005, then decline and flatten. Frame 2 adds the label "height = months to 80% on paper". Frame 3 adds the wavy line and the "schedule at that rate: 90 payments" label. Frames 4 to 6 add "national average, not one home" and keep the same view. The chart itself doesn't change. Only the labels and annotations are added.

3. **What it means.** Buyers who bought near the 2005 peak waited much longer to reach 80% than the simple payment schedule predicts. The gap is about 112 months against 90 payments. The likely reason is that home prices fell after 2005, so paying down the loan wasn't enough on its own. Buyers at other times reached 80% much sooner. Timing of purchase changed the outcome a lot. The caveats are that these are national averages and not any one home, the data is US only, and the line is illustrative.

4. **Advice a viewer would take.** The image gives no instruction to buy, rent or wait. It says so directly: "Past buyers, measured · not a reason to buy, rent or wait" and "history, not a forecast". A viewer would mainly learn that building equity isn't guaranteed to follow the amortization schedule, because price moves can add years. It's also a reason not to assume equity arrives on a fixed timeline when planning a purchase with a small down payment, like the 10% in your case. Your own timeline could differ a lot from the average.

### R10 (strip B08-S08)
1. **The idea.** The animation shows when private mortgage insurance (PMI) can be removed under a federal law, 12 U.S.C. 4902. The loan balance falls along a set payment schedule. When it reaches 80% of the home's original value, which is $320,000 in this example, you may ask to cancel PMI. When it reaches 78%, or $312,000, PMI ends automatically. The "illustrative" tag means the numbers are an example, not a promise.

2. **What changes.** In frames 1 to 4, a descending band, which I read as the loan balance, crosses two horizontal lines. It crosses the 80% line at payment 99, labeled "may request." It crosses the 78% line at payment 114, about 9.5 years in, labeled "ends automatically." Frames 5 and 6 zoom out to the full 360-payment (30-year) curve. They mark payments 99 and 114 early on the curve, next to a "home value" icon. Frame 6 adds the note "based on the schedule only."

3. **What it means.** The two milestones depend on the original loan schedule and the original home value. They don't depend on what the house is worth now. Cancellation on request has conditions: you must ask in writing and be current on payments. Automatic termination at 78% needs no request. The caption "A measurement, not a next step" suggests the 80% and 78% lines are only markers. Reaching one doesn't cancel anything by itself.

4. **What a viewer would take away.** If you put down about 10%, you'll probably pay PMI at first. Don't wait for it to end on its own:
   - Track when your balance will hit 80% of the original value, which is around payment 99 in this example.
   - Send a written request at that point, and keep your payments current.
   - Know that PMI drops off automatically at 78% either way.
   - Making extra principal payments could get you to 80% sooner. The animation doesn't say that, so it's my inference.
   - A rise in home value doesn't change these dates on the schedule shown. The image doesn't cover other routes, such as a new appraisal.
