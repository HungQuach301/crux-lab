# Grading packet (blind). Independent grader. Each label is one reader's answers about one silent 6-frame strip; the strip id is given so you compare against its muted read. Grade literally.

## Rubric
- **Chấm:** người chấm độc lập mù tập; nghĩa 1 / 0,5 / 0 so với "muted read" của `review-c3/spans.json`; cờ khuyên theo **A9** (thận trọng chung — tự kiểm số, hỏi bên cho vay — không tính; khuyên mua/chờ/bán/chọn tính). Người đọc đúng = nghĩa 1 và khuyên_tính false.


Muted read (đáp án đúng) theo hình:
- B02-S02: The loan, as a share of the price, starts at 90 % and drifts down slowly; it only touches the 80 % line after about 8 years.
- B03-S03: Hitting the 80 % line on paper is one line; a second, lower line (75 %, early years) and three steps (request, appraisal, wait) still stand before 'insurance removed'.
- N1-S06: Each page of the calendar is one monthly payment ($2,362/month, principal + interest, illustrative); as the pages flip, the loan stack slides along the payments and its top draws the balance: it falls slowly at first and faster later.
- B07-S07: On the same falling line, a first marker sits where the loan reaches 80 % of the original price, at payment 99: 'you may ask'.
- B08-S08: A second marker a little later, at 78 %: 'ends automatically'. Both markers sit on the payment line; the house's value is nowhere on the chart.
- B12-S12: Two years in, a little more than half the months are under the 80 % line, but only a thin slice is under the 75 % line lenders often use early.
- B13-S13-N2: Back on the grid, the bars over 60 months turn `warn`; they are few, and they sit together in one stretch of purchase months.
- B16-S16: Owen's panel: the index line climbs steeply, and his on-paper line drops through 80 % almost at once, while his schedule line has barely moved.
- B17-S17: Victor's panel: the index line rises a little, then falls for years; his on-paper line stays above 80 % long after his schedule line has crossed it at payment 90.
- B18-S18: Three panels side by side, aligned at purchase: one fixed schedule band and a fan of on-paper lines from fast to slow; a vertical 'your plan' marker stands between the schedule band and the fan; the 75 % line stays visible under all of them.

Output JSON only: {"R1": {"score": 1|0.5|0, "advice": true|false, "caution_only": true|false, "why": "<one line>"}, ...}

### R1 (strip B07-S07)
1. The animation shows a 30-year mortgage balance falling over 360 monthly payments. It marks the point where the balance reaches 80% of the home's original value, which is $320,000 on what looks like a $400,000 home. The title cites 12 U.S.C. 4902, and the label says "the law's two dates on this schedule." The image never says "mortgage insurance," but that statute is the Homeowners Protection Act, which covers cancelling private mortgage insurance (PMI). I'm inferring that part from the citation.

2. Frames 1 and 2 show only the downward-curving balance line and the payment axis (0, 120, 240, 360). Frame 3 adds a marker near the start of the curve, labeled "80% of original value = $320,000." Frame 4 zooms in and draws a horizontal line at that level. Frame 5 adds a dotted vertical line down to the axis and the label "payment 99 may request." Frame 6 adds a small note: "conditions: e.g. payments current." Throughout, a caption reads "A measurement, not a next step," and a tag marks the chart as illustrative.

3. In this example, once the balance has fallen to 80% of the original value, around payment 99 or about 8 years in, the borrower gains the right to ask the lender to drop the extra insurance. The right isn't automatic, and it depends on conditions such as being current on payments. The caption suggests the chart only marks where you stand on the schedule. It doesn't tell you to do anything. The title mentions two dates, but only the first one, the 80% request date, appears in these six frames.

4. As a renter who has saved about 10% and is thinking of buying, I'd take away these points:
   - With less than 20% down, I'd probably pay PMI, but it isn't permanent. I can request removal at about 80% of the original value.
   - I should keep my payments current, because that is a stated condition.
   - I should ask any lender what their cancellation conditions are.
   - Payment 99 is only an example. Real timing depends on my loan size, rate, and any extra principal payments, and extra payments would get me to 80% sooner.
   - The frames don't say whether the law also has an automatic cutoff. I'd have to look that up rather than assume it from this image.

### R2 (strip B17-S17)
**1. The idea.** The animation follows one past buyer, Victor, who bought in October 2005 with a 6.07% mortgage. It shows how long it took his loan to fall to 80% of the home's value, which is the usual equity milestone. The labels say it is illustrative, uses US data (FHFA and Freddie Mac via FRED), and is history rather than a forecast.

**2. What changes across the frames.** The lines get drawn out over a 10-year axis.
- **Price index (blue line):** It first rises a little, then falls for years, and then partly recovers. By year 10 it is still 3.3% below Victor's purchase price.
- **"On paper" line (white):** This is his actual position given home prices. It drifts above the 80% line while prices fall, then comes back down and touches 80% at 112 months.
- **Schedule line (thin gray):** This is what the loan alone would do. It slopes steadily down and would have hit 80% at 90 payments.

The last frame is just a house with a question mark.

**3. What it means.** Paying down a mortgage on schedule would have given Victor 80% in about 7.5 years. Because home prices fell after he bought, it took about 9 years and 4 months, roughly 22 months longer. Home values can sit below the purchase price for a long time, and that delays the point where you have meaningful equity. I'm inferring that the 80% line is the loan-to-value threshold, since the image doesn't say so outright.

**4. Advice a viewer would take.** The video gives no direct advice. Its caption says this is "not a reason to buy, rent or wait." As a renter with about 10% saved, I'd take away a few cautions:
- Don't count on prices rising to build my equity.
- Expect that I may have to stay in the home many years.
- Keep a cash cushion so I'm not forced to sell during a downturn.

It doesn't tell me whether to buy now, and it doesn't predict where prices are going.

### R3 (strip B13-S13-N2)
1. **The idea.** The animation shows how long past US home buyers took to reach 80% loan-to-value, which is 20% equity. It uses one bar per purchase month, from 1991 to 2016. For most purchase months the wait was short, which the video calls "typical". For a stretch of purchase months the wait was much longer, which the video calls "a long tail".

2. **What changes across the frames.**
   - Frames 1–2 show a 3D ridge of bars. Most are low, and one cluster towers up. In frame 2 that cluster is colored blue and labeled "a long tail".
   - Frame 3 flattens the view into a 2D chart. A horizontal line marks the 60-month threshold, and the axis shows years. The blue bars sit around 2005–2009.
   - Frame 4 adds a label: more than 60 months for 14.7% of buyers, about 1 in 7. It also marks the blue stretch.
   - Frame 5 labels the blue bars "one stretch of purchase months". A thin line starts to appear along the bottom.
   - Frame 6 completes that line as the national home price index. It rises through the mid-2000s, peaks around 2006–2007, then dips and recovers.

3. **What it means.** Most past buyers got to 20% equity on paper in well under 5 years. About 1 in 7 waited more than 5 years, and nearly all of them bought during one window, roughly 2005 to 2009. Their wait was long because home prices peaked and then fell soon after they bought. That is a timing effect, not a sign that those buyers did something wrong. The chart's footnotes say it is history, US only, and not a forecast.

4. **Advice a viewer would take.** The video doesn't tell anyone to buy, rent, or wait. Its own caption says so: "not a reason to buy, rent or wait." A viewer would take away three points:
   - Building equity on paper usually takes a few years, but it isn't guaranteed.
   - Some buyers face a much longer wait if prices fall after they buy.
   - You should plan for the possibility of being in that 1-in-7 group. For example, only buy if you could stay put and cover payments for 5 or more years, and keep an emergency cushion beyond your down payment.

   With only about 10% saved, I'd read this as a caution to think about how long you'd stay in the home and how much slack your budget has. It doesn't say whether to buy now.

### R4 (strip B08-S08)
**1. The idea.** The animation shows when private mortgage insurance (PMI) can end under a federal law, 12 U.S.C. 4902. It plots a loan balance falling along its payment schedule. It marks two thresholds on that curve. At 80% of the home's original value, which is $320,000 in the example, the borrower may ask to drop it, and that happens at payment 99. At 78%, which is $312,000, it ends automatically, and that happens at payment 114, or about 9.5 years in.

**2. What changes.**
- Frames 1 to 4 follow the balance curve down. First the 80% point is marked, then the 78% point appears slightly further along. Frame 4 adds the labels "payment 114 (9.5 years)" and "ends automatically."
- Frames 5 and 6 zoom out to the full 360-payment (30-year) schedule. A home-value block sits beside the loan block, and the 99 and 114 markers show up early in the loan, before payment 120.
- Frame 6 adds the caption "based on the schedule only."
- Every frame is tagged "ILLUSTRATIVE," and the footer reads "A measurement, not a next step."

**3. What it means.** There are two dates, and they are only about 15 payments apart. The first is when you are allowed to ask. The second is when the lender must drop it without being asked. Both come early in a 30-year loan, not at the end. The numbers assume you simply follow the scheduled payments. The footer and the "illustrative" tag say the animation is showing a measurement, not telling you what to do.

**4. What a viewer would take from it.**
- With a down payment of around 10%, PMI is a temporary cost that should end in roughly 8 to 10 years if you only make the regular payments.
- You don't have to wait for the automatic date. You can request removal at the 80% point, which could save about 15 months of premiums.
- The animation doesn't give exact rules, such as payment history or other conditions. It also doesn't say whether extra payments or a rise in home value would change the timing. Before relying on those dates, I'd check them against my own loan terms and ask my lender.

### R5 (strip B02-S02)
1. **The idea.** The animation shows how long it takes a home buyer's loan to fall to 80% of the home's value. That is the usual point where you can drop private mortgage insurance and have a real equity cushion. It starts with one illustrative line, then adds real historical data from FHFA and Freddie Mac (via FRED). Each line is one purchase month from 1991 to 2016.

2. **What changes across the frames.**
   - Frames 1–2: a single "on the schedule" line starts at about 90% loan-to-value and slopes down. It reaches 80% at about 8 years.
   - Frames 3–5: lines for hundreds of purchase months pile up, building a mountain-shaped bundle. Many lines rise above 90% before they come down, and some take much longer than the schedule says.
   - Frame 6: two lines are highlighted. The typical buyer got to 80% in about 2 years, much faster than the 8-year schedule. The slowest case, shown in blue, took about 9 years. Its line climbed first and then fell.

3. **What it means.** The loan balance alone doesn't decide how fast you build equity. Home prices matter too. When prices rose, buyers hit 80% quickly, in about 2 years for the typical buyer. When prices fell, the loan's share of the home's value went up, and buyers took longer than the schedule's 8 years. The range is wide, from about 2 to 9 years.

4. **What a viewer would take from it.** The animation says outright that it gives no advice: "Past buyers, measured · not a reason to buy, rent or wait," and "US only · history, not a forecast." The practical takeaways are modest.
   - With about 10% down, expect to reach 80% loan-to-value in years rather than months. Plan for the slow case of roughly 9 years, not the fast one.
   - Don't count on price gains to build equity. They helped past buyers, but they aren't guaranteed.
   - Buy only if you expect to stay long enough, and have enough cash reserve, to get through a slow stretch.

### R6 (strip B18-S18)
1. **The idea.** The animation shows how long it has taken past US home buyers with a small down payment to pay their mortgage down, or let their home's value rise, until they owe 80% or 75% of the home's value. Around 80% is when mortgage insurance can typically come off. The lines are based on FHFA and Freddie Mac data from FRED, with every buyer starting under the same rule and the same price index. It ends by setting "buy now and pay mortgage insurance" against "keep renting and keep saving."

2. **What changes.**
   - Frame 1 shows the lines for the percent of the home's value still owed, running over 10 years. The loan balance falls on a fixed schedule, and the home's price moves along a historical path.
   - Frames 2 and 3 add a faint cloud of many past buyers and label three example buyers: Owen, Grace and Victor. Owen and Grace reach the threshold quickly. Victor's line rises first and only gets to 80% and 75% after about 9 or 10 years. Frame 3 also notes that the schedule is fixed at the start.
   - Frame 4 adds the numbers. On paper, the typical buyer reaches the threshold in about 23 months, but about 1 in 7 take more than 60 months. About 2 years matches the typical case, not the slow ones.
   - Frame 5 switches to an illustrative $400,000 home shown as a stack of layers, with a small house beside it.
   - Frame 6 shows a house labeled "buy now + mortgage insurance," a person, and an apartment building labeled "keep renting, keep saving."

3. **What it means.** For buyers with a small down payment, the mortgage insurance period is usually short, around 2 years, but it varies a lot. If home prices fall or stay flat, it can last 5 years or more, and for some it takes nearly a decade. The "past buyers" cloud shows the typical outcome and the range around it. The small print says this is history, not a forecast, and it applies to the US only.

4. **Advice a viewer would take.** The video gives no direct advice. The captions say "not a reason to buy, rent or wait" and "a measurement, not a next step." A viewer could take away the following:
   - Expect mortgage insurance to last about 2 years, but plan for the chance it lasts much longer.
   - Buying with a small down payment and renting while you save are both reasonable paths.
   - Decide based on your own budget, how long you plan to stay, and how much risk you can handle, not on this chart alone.

### R7 (strip N1-S06)
1. **The idea:** The animation shows what a 30-year mortgage looks like at today's rate. The loan is $360,000 at a 6.86% average rate (September 2026, Freddie Mac via FRED). That gives a principal-and-interest payment of $2,362 a month. It also shows how the loan balance falls over the 360 payments. Every frame is labeled "illustrative," and the caption says "A measurement, not a next step."

2. **What changes across the frames:**
   - Frame 1 shows a small document or payment icon next to a tall stack that stands for the $360,000 loan.
   - Frame 2 adds the 6.86% rate.
   - Frame 3 adds the $2,362 monthly principal-and-interest payment, tied to the payment icon.
   - Frame 4 adds a note that taxes, homeowners insurance and PMI come on top of that payment.
   - Frame 5 switches to a loan-balance curve over 0 to 360 payments. The stack shrinks only a little by payment 35.
   - Frame 6 shows the stack at payment 114, still well above zero. The curve is labeled "slowly at first" and "faster later," and it is described as "set on day one."

3. **What it means:** The monthly payment is a fixed number, but the true monthly cost is higher once taxes, insurance and PMI are added. PMI is likely here because a buyer with about 10% down is under 20%. Early in the loan, most of each payment goes to interest. The balance falls slowly for roughly the first third of the loan, and the paydown speeds up in later years. That schedule is locked in from the start.

4. **Advice a viewer might take:**
   - Don't judge affordability by the $2,362 alone. Budget for the full payment, including taxes, insurance and PMI.
   - Expect to build equity slowly in the early years. That matters if you might sell or move within a few years.
   - The video doesn't tell you to buy, wait or refinance. Its caption frames the numbers as information, not a recommendation. A viewer would mainly come away better able to run their own numbers.

### R8 (strip B12-S12)
1. **The idea.** The animation shows how much equity past US home buyers had two years after they bought. Each bar is one purchase month, from January 1991 to July 2024, which makes 403 months. Bar height is loan divided by value on paper at the two-year mark. A shorter bar means a smaller loan relative to the home's value. Two lines mark 80% and 75%. The data comes from FHFA, Freddie Mac via FRED, and a Fannie Mae guideline (B-8.1-04).

2. **What changes across the frames.**
   - Frame 1 shows only the gray bars and the two threshold lines.
   - Frame 2 adds a header and the statistic that 58.6% of purchase months ended up at or under 80%.
   - Frames 3 to 6 highlight in blue the months that ended up at or under 75%, and the share is 15.6%. There are two blue clusters, one around 2002 to 2004 and one around 2021 to 2023.
   - Frames 4 to 6 add the label "Fannie Mae's early bar" and keep both statistics on screen.

3. **What it means.** For most of the period, buyers had a loan above 75% of the home's value two years in. Fewer than one in six purchase months got under 75%, and a bit more than half got under 80%. The bars rise sharply for purchases around the mid-2000s, so those buyers ended up with the least equity. Buyers in the blue stretches, when prices rose quickly, got under 75% fastest. The 80% and 75% lines matter because lenders and Fannie Mae use cutoffs like these. I can't tell exactly what "early bar" refers to from the image alone.

4. **The advice.** The footer says this is "not a reason to buy, rent or wait." It also says the data is US only and is "history, not a forecast." A viewer shouldn't treat it as a signal to act. They could take away that building equity quickly depends heavily on when you buy and on price trends, which nobody controls. They could also take away that a small down payment, like my roughly 10%, usually means a loan above 80% of the home's value for a while. So I shouldn't count on reaching 80% or 75% quickly.

### R9 (strip B12-S12)
1. **The idea.** The animation shows how much of a home buyers still owed compared with what the home was worth, measured two years after they bought. It does this for every purchase month from January 1991 to July 2024, which is 403 months. Each bar is one purchase month, and its height is loan divided by value on paper. Two reference lines mark 80% and 75%.

2. **What changes across the frames.**
   - Frame 1 shows only the bars and the two lines.
   - Frame 2 adds a label: for 58.6% of purchase months, buyers were at or under 80% loan-to-value two years later.
   - Frame 3 highlights a few stretches of bars in blue and adds a second label: 15.6% of months were at or under 75%.
   - Frames 4 to 6 add a "Fannie Mae's early bar" tag and hold the same picture. Frame 4 is the same chart with the tags moved around.

   The blue stretches fall in the early 2000s and around 2020 to 2022, where the bars dip below the 75% line.

3. **What it means.**
   - Over this history, buyers usually owed less than 80% of the home's value after two years in a little over half of purchase months. That is the point where private mortgage insurance can typically come off.
   - Getting down to 75% or lower happened rarely, in about one month in six. It happened mainly when prices rose quickly, and only for people who bought just before those rises.
   - The tall hump around the mid-2000s to 2010 shows buyers who owed close to or more than their home was worth. That is the bust period.
   - Who ends up in good shape depends heavily on when they bought, which no buyer controls.

4. **What a viewer would take from it.**
   - The on-screen text says this is "not a reason to buy, rent or wait." It is past data for the US only, "history, not a forecast."
   - So the animation gives no instruction to buy or to hold off.
   - The practical takeaway for someone with about 10% down is to not count on fast price gains to build equity. Start with a thin cushion and expect a good chance of still being above 80% loan-to-value after two years.
   - Plan for that with room in the budget for mortgage insurance and an emergency fund. Plan to stay long enough to ride out a dip. The bars show timing luck swinging outcomes a lot.

### R10 (strip B18-S18)
1. **The idea:** The animation is about how long mortgage insurance lasts on a low-down-payment loan. Mortgage insurance usually ends once the loan falls to about 80% of the home's value, or 75% in some cases. The chart compares the schedule printed on paper with what happened to past buyers, using home-price data from FHFA and Freddie Mac. Every buyer follows the same rule and the same price index, lined up at the purchase date.

2. **What changes across the frames:**
   - Frame 1 starts with one price-driven line and the 80% and 75% thresholds.
   - Frames 2 and 3 add a faint spread of many past buyers' paths. They also add three named examples: Owen, Grace and Victor. A vertical bar marks "a plan" and a note says the schedule is fixed at the start.
   - Frame 4 adds the numbers. On paper, the typical buyer reaches the threshold in about 23 months, and about 1 in 7 take more than 60 months. Owen and Grace reach the threshold in roughly 2 years or less. Victor's line rises first and only reaches the threshold near year 10.
   - Frame 5 switches to an illustrative $400,000 home as a stack of green bars beside a house, labeled "A measurement, not a next step."
   - Frame 6 shows a house, a person and an apartment building. The labels are "buy now + mortgage insurance" and "keep renting, keep saving."

3. **What it means:** The schedule on paper is fixed, but how long you actually pay mortgage insurance depends on what home prices do after you buy. Many past buyers got out in about 2 years. A minority were stuck for 5 years or more, and the slowest took about 10. The chart describes US history, not a forecast, and it doesn't say whether buying or renting is better.

4. **What a viewer would take away:** The video doesn't tell you to buy, rent or wait. A viewer with about 10% saved would learn to plan for mortgage insurance lasting longer than the typical 2 years. They should check whether they could afford the payments if it lasted 5 years or more. Both options in frame 6 stay open, and the choice is theirs.

### R11 (strip B16-S16)
1. **The idea:** The animation follows one past buyer, Owen, who bought in January 2004 with a 5.71% mortgage rate. It shows how long it took Owen's loan to fall to 80% of the home's value. That is the usual point where a buyer who put down less than 20% can stop paying mortgage insurance. The chart marks 80% with a horizontal line.

2. **What changes:** The time axis runs from 0 to 10 years, and the lines extend further right in each frame.
   - The blue price index line rises early on.
   - The "on paper" line starts near the top and falls quickly to the 80% line.
   - The "schedule" line, which reflects only regular loan paydown, slopes down slowly. By frame 6 it reaches 80% at roughly 7 years.
   - The text labels appear in stages. They end with "on paper: 13 months · schedule: 86" and "index +11.2%".

3. **What it means:** Because home prices rose 11.2%, Owen's loan was down to 80% of the home's value after about 13 months. Paying down the loan on the normal schedule alone would have taken 86 months, or about 7 years. So price growth shortened the wait a lot for this buyer. The labels say this is illustrative, uses US data only, and is history, not a forecast.

4. **What a viewer would take from it:** The video explicitly says it is not a reason to buy, rent, or wait. The practical lesson is limited:
   - If you put down less than 20%, you may be able to drop mortgage insurance earlier than the schedule says if your home gains value. Ask your lender how that works.
   - Don't plan around price gains happening. Prices could be flat or fall, and then you'd be on the slow schedule.
   - For me, with about 10% saved, the safe assumption is that I'd pay that insurance for years. I'd only treat early removal as a bonus.

### R12 (strip B07-S07)
1. **The idea:** The animation shows a mortgage balance falling over a 30-year loan (360 payments). It marks the point where you can ask to drop private mortgage insurance. The citation, 12 U.S.C. 4902, is the federal law on cancelling that insurance. That's from my own background knowledge, not the image. The image only says "the law's two dates on this schedule" and shows one of them.

2. **What changes across the frames:**
   - Frames 1 and 2 show only the downward curve of the balance, from payment 0 to payment 360. The early stretch is highlighted.
   - Frame 3 adds a dot on the curve, labeled "80% of original value = $320,000."
   - Frame 4 zooms in on that dot.
   - Frame 5 adds a dotted line down to payment 99, labeled "may request."
   - Frame 6 adds a caveat: "conditions: e.g. payments current."

3. **What it means:**
   - On the example schedule, the balance reaches 80% of the home's original value (a $400,000 home) after about 99 payments, roughly 8 years.
   - At that point the borrower may ask the lender to cancel the insurance, but only if they meet conditions such as being current on payments.
   - The labels "ILLUSTRATIVE" and "A measurement, not a next step" say the numbers are an example. The chart shows where the threshold falls. It doesn't tell you to do anything.
   - Only one of the law's two dates is visible here. I'd guess the other is an automatic cancellation point, but the frames don't show it.

4. **What I'd take from it as a renter with about 10% saved:**
   - If I put down less than 20%, I'd likely pay mortgage insurance, and it wouldn't last forever.
   - The balance falls slowly at first, so reaching 80% could take years. Paying extra principal, or the home gaining value, might get me there sooner. The animation doesn't say that, so I'd have to check it.
   - I'd need to stay current on payments and probably make the request myself.
   - The animation gives no instruction beyond that. Since the numbers are illustrative, I'd check my own loan terms before relying on any of them.

### R13 (strip B13-S13-N2)
1. The animation shows how long it took past US home buyers to reach 80% equity, which is the point where private mortgage insurance (PMI) can usually be dropped. It shows that the wait is usually short but sometimes very long. The data comes from FHFA and Freddie Mac via FRED. Each bar is one purchase month, from 1991 to 2016. A bar's height is the number of months that buyer needed to reach 80% "on paper."

2. In frames 1 and 2 the chart is a 3D ridge. Most bars are low and labeled "typical." One raised block of bars sticks up, and in frame 2 it turns blue and is labeled "a long tail." In frame 3 the view flattens into a 2D bar chart with a year axis and a horizontal threshold line. Frames 4 to 6 add labels. The blue bars are buyers from roughly 2005 to 2009, and they waited more than 60 months. The label says 14.7%, or about 1 in 7 buyers, fell into that group. Frame 6 adds a national home price index line underneath. It rises through the mid-2000s, peaks around 2006 to 2007, then dips and recovers.

3. Most buyers got to 80% fairly quickly. Buyers who bought near the price peak, just before the crash, had a much longer wait because prices fell after they bought. Timing and price changes beyond your control can stretch the wait a lot. The bottom text says this is measured history for the US only. It is not a forecast and not a reason to buy, rent, or wait.

4. The video's own caveat says the chart isn't a signal to buy, rent, or wait. A viewer could still take away a few things:
   - Don't assume you'll build equity quickly. About 1 in 7 past buyers waited more than five years.
   - A 10% down payment with PMI could last longer than planned if prices fall.
   - Keep a cash buffer and plan to stay a long time, so a bad-timing stretch doesn't force a sale.
   - Don't try to time the market. The chart only shows that the downside risk exists.

### R14 (strip B17-S17)
1. **The idea.** The animation follows one past buyer, "Victor," who bought in October 2005 with a 6.07% mortgage. It tracks how his home equity and the local price index moved over the next 10 years. The source is FHFA and Freddie Mac data via FRED. It's labeled "illustrative," US-only, and "history, not a forecast."

2. **What changes across the frames.**
   - Frames 1–3: Two lines are drawn from left to right across a 0–10 year axis. A white line shows Victor's position "on paper" against a grey 80% line. A thin grey line shows the scheduled paydown. A blue line shows the price index.
   - The white line rises above 80% for a while, then falls back down to it.
   - The blue price index dips for years, bottoming out around year 6. It then recovers but ends about 3.3% below his purchase price.
   - Frames 3–5: Labels appear that read "on paper: 112 months" and "schedule: 90 payments." The caption "index still 3.3% below purchase" also appears.
   - Frame 6: The charts disappear and a house with a question mark on it takes their place.

3. **What it means.** I read the 80% line as the point where his loan balance falls to 80% of the home's value. That's the usual threshold for dropping mortgage insurance, though the image doesn't say so. Under the original payment schedule he'd reach it after 90 payments, about 7.5 years. Because prices fell, he didn't reach it on paper until month 112, about 9.3 years. So a price slump delayed his progress by about 22 months. After 10 years the index was still below what he paid. A buyer with a small down payment, like my roughly 10%, is exposed to this. Falling prices can wipe out equity and delay milestones, even when every payment is made on time.

4. **Advice a viewer would take.** The caption says this isn't a reason to buy, rent or wait. So the animation gives no instruction. The takeaway is about risk. A home bought with a small down payment can spend years with little or no equity if prices fall, and the timing of the purchase matters. I'd take it as a reason to plan to stay a long time and keep a cash buffer. I'd also avoid stretching the budget, and I wouldn't count on quick appreciation. It's one example, and it doesn't predict what will happen to me.

### R15 (strip B02-S02)
1. **The idea:** The animation shows how long it takes a first-time buyer with a small down payment to get their loan down to 80% of the home's value. That is the usual point where you can drop private mortgage insurance. Someone who puts down 10% starts at a 90% loan-to-value ratio. The animation compares the "on the schedule" path with what actually happened to real past buyers.

2. **What changes across the frames:**
   - Frames 1 and 2 show an illustrative line sloping down from 90% toward the 80% line. It reaches 80% at about 8 years, which is the scheduled payoff pace.
   - Frame 3 swaps in real data: one line for each purchase month from 1991 to 2016. They start bunched at the left.
   - Frames 4 and 5 fill in the full set of lines. Many of them don't fall. They rise well above 90% for years, then come back down.
   - Frame 6 highlights two cases. The typical buyer reached 80% in about 2 years. The slowest case, in blue, took about 9 years, which is longer than the 8-year schedule.

3. **What it means:** The 8-year schedule is only a baseline. In practice, the time to reach 80% depends mostly on what home prices did after you bought. Most buyers got there much faster than scheduled because prices rose. Buyers who bought before price drops saw their loan-to-value ratio rise first. Those buyers took longer than the schedule, in the worst case about 9 years. The outcomes varied a lot.

4. **What a viewer would take from it:** There's no instruction to buy, rent or wait. The frames say so directly: "Past buyers, measured · not a reason to buy, rent or wait" and "history, not a forecast." A viewer should come away with a few points:
   - With about 10% down, expect to carry mortgage insurance for some time. A reasonable plan is a couple of years, but it could take much longer.
   - Don't count on rising prices to remove it quickly.
   - Keep a financial cushion in case it takes longer.

   The data covers only the US, and past results don't predict future ones.

### R16 (strip B03-S03)
1. **The idea:** The animation is about private mortgage insurance (PMI) and how a buyer who put down less than 20% can get rid of it. A house is bought with a loan, and the loan balance sits next to the home's value. At 80% loan-to-value, the point where PMI would normally end, the loan is still insured "on paper." Dropping the insurance isn't automatic. The loan owner has a process.

2. **What changes:** In frames 1 and 3, the home-value stack gets taller while the loan stack stays about the same. That means the buyer's equity is growing. Frame 2 shows the insurance still on, even though the loan is near the 80% line. In frame 4 the target line drops from 80% to 75%. A new label says Fannie Mae wants a wait of at least 2 years and a loan of 75% or less. Frames 5 and 6 show three example buyers, Grace, Owen and Victor, each with a house and a loan stack. They show that this plays out across different people.

3. **What it means:** Reaching 80% doesn't end the insurance by itself. You have to ask the loan owner, get an appraisal and wait. When the removal is based on an appraisal showing the home has gained value, Fannie Mae's rule is stricter: at least 2 years, and a loan of 75% or less of the value. The repeated "illustrative" tags and the notes "past buyers, measured," "US only," "history, not a forecast," and "not a reason to buy, rent or wait" say the visuals are examples. They are not predictions.

4. **Advice a viewer would take:** If I put down about 10%, I should expect to pay PMI, and I shouldn't assume it will go away on its own. I'd need to find out who owns my loan and what their removal rules are. I'd plan for requesting removal, paying for an appraisal and waiting, and I wouldn't count on a quick exit. The video doesn't tell me whether to buy, rent or wait. It only says what the process and the past numbers look like.

### R17 (strip B03-S03)
**1. What idea is this animation showing?**
It looks like it's about getting mortgage insurance (PMI) taken off a home loan. A loan that reaches 80% of the home's value "on paper" doesn't automatically end the insurance. Frame 2 shows "insurance still on" even though the loan looks small enough. Frames 3 and 4 show the loan owner's process: you request removal, get an appraisal, and wait. Fannie Mae's rule shown in frame 4 is to wait at least 2 years, with the loan at 75% or less of value.

**2. What changes over time across the frames?**
- **Frame 1:** A tall stack (home value) sits next to a shorter stack (the loan). The loan reaches the 80% line, with a note that this is measured from past buyers' data (FHFA/Freddie Mac).
- **Frame 2:** A house with the insurance still attached, plus a person, cash and a building.
- **Frames 3–4:** The 80% line fades and a stricter 75% line appears, with an amber band showing the gap still to close.
- **Frames 5–6:** Three homeowners, Grace, Owen and Victor, each with their own house, loan stack and value stack. This suggests different people reach the goal in different ways or at different times.

**3. What does it mean?**
Hitting 80% on paper is not the same as getting the insurance removed. Depending on how you ask, the lender or loan owner may want a formal request, an appraisal, a minimum holding period and a lower loan-to-value ratio. The footnotes say it is illustrative, US-only, history and not a forecast. The data is a measurement of past buyers, not a prediction or a next step.

**4. What advice, if any, would a viewer take from this?**
The video seems to avoid telling you to buy, rent or wait. The labels say it's "not a reason to buy, rent or wait." As someone with about 10% saved, I'd take away three things:
- A 10% down payment likely means paying mortgage insurance, so I should budget for it.
- I should ask my lender how and when the insurance can come off, including the appraisal, the waiting period and the 75% or 80% thresholds.
- I shouldn't assume home prices will rise to help me get there. Past results are not a forecast.

I can only see the image, so I'm inferring the PMI topic from the labels and visuals. The narration might add details I can't see.

### R18 (strip N1-S06)
1. **The idea:** The animation shows what a typical mortgage costs and how the loan gets paid down. It uses a $360,000 loan at the September 2026 average rate of 6.86% (Freddie Mac, via FRED). It's labeled "illustrative," so it's an example and not a quote for anyone in particular.

2. **What changes across the frames:**
   - Frames 1–2 show a $360,000 loan, drawn as a tall stack, next to a small payment block. Frame 2 adds the 6.86% rate.
   - Frame 3 labels the monthly payment as $2,362 of principal plus interest.
   - Frame 4 adds a note that taxes, homeowners insurance, and PMI come on top of that payment.
   - Frames 5–6 switch to a curve of the loan balance over 360 payments, which is 30 years. The curve starts with the balance high and drops slowly, then falls faster later. The payment counter moves from 35 to 114 while the balance stays high.
   - The caption "A measurement, not a next step" stays the same in every frame.

3. **What it means:**
   - The $2,362 is only the principal-and-interest part of the monthly cost. The real monthly bill is higher once taxes, insurance, and PMI are added.
   - Early payments go mostly to interest, so the balance barely falls at first. Even after 114 payments, which is more than 9 years, a large share of the loan is still owed. Most of the principal gets paid off in the later years.
   - The schedule is fixed on day one. The pace of paydown is built into the loan and doesn't change.

4. **Advice a viewer might take away:**
   - The video doesn't tell anyone to buy or wait. The caption says it is a measurement and not a recommendation.
   - If you're a renter with about 10% saved, the practical takeaway is to budget for the full monthly cost, not just the $2,362 headline payment. That means adding taxes, insurance, and PMI, which a down payment under 20% usually triggers.
   - Don't expect to build equity quickly. If you might move within a few years, you would own very little of the home.
   - Compare your own numbers against this example, since your rate, price, and local taxes will differ.

### R19 (strip B16-S16)
**1. The idea.** The animation follows one past buyer, "Owen," who bought in January 2004 with a 5.71% mortgage rate. It tracks how fast his loan balance fell to 80% of the home's value. That 80% line is the usual point where a down payment under 20% stops needing extra costs like mortgage insurance. I'm inferring that last part, because the image only labels the line "80%."

**2. What changes across the frames.** The time axis runs from 0 to 10 years. Two white lines and a blue line are drawn in as time passes.
- The blue line is the home price index, and it climbs quickly at the start.
- The thin white "schedule" line is the planned paydown, and it slopes down slowly.
- The thick white "on paper" line drops fast and crosses 80% at about 13 months. By frame 6 the price index is up 11.2%, and the schedule line doesn't reach 80% until about month 86, or roughly 7 years.

**3. What it means.** Owen started with a small down payment, so his loan was well above 80% of the home's value. Rising prices cut that ratio much faster than his payments alone would have. On paper he reached 80% in about 13 months instead of 86. Most of the speedup came from price growth, not from paying down the loan.

**4. The advice a viewer would take.** The takeaway is limited. Price growth can shorten how long a small down payment costs extra, but that depended on prices rising in Owen's case. The footer says this is "past buyers, measured," "not a reason to buy, rent or wait," and "history, not a forecast." The tag also says "illustrative," and it's US-only. As a renter with about 10% saved, I wouldn't read this as a reason to buy now or to hold off. I'd read it as a reminder to plan for the cost of a small down payment and not count on prices rising to get me out of it quickly.

### R20 (strip B08-S08)
**1. The idea.** The animation shows the two points in the law (12 U.S.C. 4902) where private mortgage insurance (PMI) can end. The first is when the loan balance falls to 80% of the home's original value. The second is 78%. The "illustrative" tag and the "based on the schedule only" caption say these are example numbers, not a prediction for any one person.

**2. What changes across the frames.**
- Frames 1–3 show a loan-balance curve sloping down. A marker lands on the 80% line, which is $320,000 in the example. It is labeled "payment 99, may request."
- A second marker then appears a little further along, at 78%, or $312,000.
- Frame 4 labels that second point "payment 114 (9.5 years), ends automatically."
- Frames 5–6 zoom out to the full 360-payment (30-year) schedule. Points 99 and 114 sit early on the curve, well before the end. The home-value icon on the right stays fixed, which fits with the percentages being measured against the original value.

**3. What it means.** Paying the loan down on schedule eventually gets you out of PMI. At payment 99, which is about 8 years in, you can ask the lender to drop it. If you don't ask, it ends on its own at payment 114. The caption "A measurement, not a next step" says this is a milestone on the schedule. It isn't an action the video is telling you to take.

**4. Advice a viewer might take.**
- PMI isn't permanent. Know the dates, and remember that between 80% and 78% you have to ask for cancellation. It won't happen automatically until 78%.
- The video gives no explicit instruction. Its only implied advice is to track when you hit those thresholds.
- I'd put down about 10%, so my loan would start near 90% of the home's value. My dates would differ from the example's, and PMI would last longer than it does for someone who put 20% down. I'd check my own loan terms and amortization schedule.
- The example uses the schedule only. Extra payments would reach 80% sooner. Falling home prices wouldn't change the original-value math, but the lender may have its own rules for requesting cancellation.
