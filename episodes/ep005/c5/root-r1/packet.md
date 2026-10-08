# Grading packet (blind). Independent grader. Each label is one reader's answers about one silent 6-frame strip; the strip id is given so you compare against its muted read. Grade literally.

## Rubric
- **Chấm:** người chấm độc lập mù tập; nghĩa 1 / 0,5 / 0 so với "muted read" của `review-c3/spans.json`; cờ khuyên theo **A9** (thận trọng chung — tự kiểm số, hỏi bên cho vay — không tính; khuyên mua/chờ/bán/chọn tính). Người đọc đúng = nghĩa 1 và khuyên_tính false.


Muted read (đáp án đúng) theo hình:
- B02-S02: The loan, as a share of the price, starts at 90 % and drifts down slowly; it only touches the 80 % line after about 8 years.
- B03-S03: Hitting the 80 % line on paper is one line; a second, lower line (75 %, early years) and three steps (request, appraisal, wait) still stand before 'insurance removed'.
- B11-S11: Most purchase months have short bars; a horizontal median line sits low at 23 months, far below a faint ridge of the schedule's own months; nearly every bar ends below its schedule mark.
- B13-S13-N2: Back on the grid, the bars over 60 months turn `warn`; they are few, and they sit together in one stretch of purchase months.
- B14-S14: The zoom frame lands on the tallest bar: bought October 2005, 112 months on paper, taller than that month's schedule mark.
- B16-S16: Owen's panel: the index line climbs steeply, and his on-paper line drops through 80 % almost at once, while his schedule line has barely moved.
- B17-S17: Victor's panel: the index line rises a little, then falls for years; his on-paper line stays above 80 % long after his schedule line has crossed it at payment 90.
- B18-S18: Three panels side by side, aligned at purchase: one fixed schedule band and a fan of on-paper lines from fast to slow; a vertical 'your plan' marker stands between the schedule band and the fan; the 75 % line stays visible under all of them.

Output JSON only: {"R1": {"score": 1|0.5|0, "advice": true|false, "caution_only": true|false, "why": "<one line>"}, ...}

### R1 (strip B02-S02)
1. **The idea.** The animation shows how long it takes a buyer who put down about 10% to owe 80% or less of their home's value. That is the 80% line. Frames 1 and 2 are an illustrative case: the loan starts near 90% of the price and shrinks on the normal payment schedule, reaching 80% in about 8 years. Frames 3 to 6 swap in real history from FHFA and Freddie Mac data via FRED. Each thin line is one purchase month between 1991 and 2016.

2. **What changes over time.**
   - The single schedule line is replaced by a growing bundle of real lines.
   - Many real lines drop to 80% much faster than the schedule, because home values rose.
   - Other lines climb well above 90% before they come down, because home values fell.
   - Frame 6 highlights two of them. The typical buyer got to 80% in about 2 years. The slowest case, in blue, took about 9 years. That is even longer than the 8-year schedule, and it spent years with a loan share above where it started.

3. **What it means.** The time it takes to build a cushion of equity depends on more than your payments. It also depends on what home prices do after you buy. Usually prices help and the cushion arrives early. For some buyers prices hurt, and the wait runs longer than the payment schedule says. The caption in the image says this is "a measurement, not a next step."

4. **What a viewer would take from it.** The video seems to be saying not to treat this as a signal to buy, rent, or wait. The captions say it is past buyers, US only, "history, not a forecast." If I were a renter with 10% saved, I'd take away three things:
   - Putting 10% down is normal, and most past buyers got to 80% quickly.
   - I shouldn't count on that, because the bad cases took many years.
   - I should only buy if I can hold the home for a long time and cover the payments if prices dip.

   The image doesn't say why 80% matters. My guess is that it's the point where extra loan costs like mortgage insurance can come off, but that is my inference and not something the frames state.

### R2 (strip B16-S16)
**1. The idea.** The animation follows one past buyer, Owen, who bought in January 2004 with a 5.71% mortgage. It compares two ways of reaching the 80% line. The image doesn't label that line, but I read it as the loan being 80% of the home's value, which is the point where a small-down-payment buyer usually stops paying mortgage insurance. One way is the loan's scheduled paydown. The other is the "on paper" path, which also counts home prices rising.

**2. What changes across the frames.**
- The time axis fills in from 0 toward 10 years.
- The blue price-index line climbs, ending at +11.2%.
- The white "on paper" line starts above 80% and falls to the 80% line fast, at about 13 months.
- In the last frame, the grey "schedule" line is drawn. It slopes down slowly and doesn't reach 80% until about 86 months, or roughly 7 years.

**3. What it means.** Rising prices got Owen to 80% about six years sooner than the scheduled payments alone would have. The faster result came from price appreciation, not from paying the loan down faster. The footer says this is "illustrative" and "history, not a forecast."

**4. What a viewer would take from it.** The video gives no buy, rent or wait advice, and it says so on every frame. The takeaways I'd draw as a renter with about 10% saved are:
- With a small down payment, the scheduled path is the only one you can count on. That could be several years of extra insurance cost.
- Price gains can shorten that wait, as they did for Owen, but they aren't guaranteed. This is one US buyer in one period, and prices can also fall.
- Don't build a plan that only works if prices rise.

### R3 (strip B11-S11)
**1. What idea is this animation showing?**
It shows how long past home buyers with a small down payment took to reach 80% of their home's value "on paper". Reaching 80% means owing no more than 80% of the home's value, or having 20% equity. That is the point where private mortgage insurance usually can come off. Each bar is one month of purchase, from 1991 to 2016. The data come from FHFA and Freddie Mac via FRED.

**2. What changes over time across the frames?**
- **Frame 1:** There are just the bars. They are low and steady in the 1990s, jump sharply for purchases around 2005 to 2007, then fall back.
- **Frame 2:** The chart is redrawn around a baseline, and a label appears saying the median is 23 months.
- **Frame 3:** A line is added, with the headline "90.6% no later than the schedule."
- **Frames 4 and 5:** The line is labeled "schedule at each month's rate." It sits high in the early 1990s and drifts lower over the years.
- **Frame 6:** A bracket marks the "gap" between that schedule line and the bars.

**3. What does it mean?**
The schedule line seems to show how long it would take to reach 80% by paying down the loan alone, at the mortgage rate of that month. The bars show how long it actually took. For about 90.6% of purchase months, buyers got there no later than the schedule predicted. The usual reason is that home prices rose, so equity grew faster than payments alone would build it. The median wait was about 23 months. The exception was buyers near the 2005 to 2007 peak, whose bars are far taller. Falling prices made them wait much longer, and their bars reach or pass the schedule line. I'm inferring some of this from the labels, because the frames don't spell out the method.

**4. What advice, if any, would a viewer take from this?**
The video says outright that this is "not a reason to buy, rent or wait," that it covers the US only, and that it is "history, not a forecast." So there is no instruction to buy.

As a renter with about 10% saved, I'd take away three things:
- Historically, a small down payment often got to 20% equity faster than the payment schedule alone suggested. That is mostly thanks to price growth.
- That isn't guaranteed. If I bought at a market peak, it could take many years.
- I should budget for mortgage insurance lasting longer than two years, and not count on appreciation to remove it.

### R4 (strip B03-S03)
1. **The idea:** The animation is about getting rid of mortgage insurance (the "insurance still on" label looks like PMI). When a home's value rises while the loan stays the same, the loan drops below 80% of the value "on paper". That doesn't turn the insurance off automatically. The lender or loan owner has a process you have to follow.

2. **What changes across the frames:**
   - In frames 1 to 3, the home-value stack grows taller while the loan stack stays about the same. The loan sinks below the 80% line.
   - Frame 2 shows a house with a banner reading "insurance still on", even though the loan is now under 80%.
   - Frames 3 and 4 add the rule: request removal, get an appraisal, and wait.
   - Frame 4 then tightens the bar. Fannie Mae wants you to wait at least 2 years, and the loan must be 75% or less of the value. The 80% label is greyed out and 75% becomes the line that counts.
   - Frames 5 and 6 show three homeowners, Grace, Owen and Victor, each with their own house and loan stack. Their situations seem to differ, but the image doesn't make clear how.

3. **What it means:** Hitting 80% "on paper" isn't enough. If your home has gone up in value, you usually have to ask for the insurance to be removed and pay for an appraisal. The loan owner may also apply stricter tests, such as 2 or more years of waiting and a loan of 75% or less. The different homeowners suggest outcomes vary from person to person. The captions say this is "history, not a forecast", US only, and "a measurement, not a next step". The "ILLUSTRATIVE" tags mean the pictures aren't real data.

4. **What a viewer would take away:**
   - The video says outright that this is not a reason to buy, rent or wait.
   - If I buy with about 10% down, I'd probably pay mortgage insurance. I shouldn't assume it disappears on its own when I reach 80%.
   - I'd need to find out who owns my loan, what their removal rules are, and how long I'd have to wait.
   - I'd also need to budget for an appraisal.
   - I shouldn't count on home prices rising to get me out of the insurance. Appreciation is history, not a promise.

### R5 (strip B13-S13-N2)
1. **The idea:** The animation shows how long past home buyers had to wait before they had 20% equity, meaning their loan was down to 80% of the home's value "on paper." Each bar is one purchase month, and its height is the number of months that buyer needed to get there. Most bars are fairly short. A small group of purchase months has a very tall "long tail."

2. **What changes across the frames:**
   - Frames 1 and 2 show a 3D ridge of bars. A "typical" level is marked, then the tall block is highlighted in blue as "a long tail."
   - Frame 3 flattens the ridge into a 2D chart from 1991 to 2016, with a 60-month line drawn across it.
   - Frames 4 and 5 add the statistic that 14.7% of purchase months (about 1 in 7) took more than 60 months. They also label the blue block as "one stretch of purchase months," running from about 2005 to 2009.
   - Frame 6 adds a thin line for the national home price index along the bottom. It rises, peaks around the blue stretch, then dips and recovers.

3. **What it means:** For most buyers, building 20% equity took well under five years. People who bought in the mid-2000s, near the price peak, often waited much longer, because prices fell right after they bought. So how long it takes to build equity depends heavily on when you buy. The small print says this is measured history for US buyers only. It is not a forecast and not a reason to buy, rent, or wait.

4. **What a viewer would take from it:** The video doesn't tell you to buy or to wait, and it says so outright. As a renter with about 10% saved, I'd take away three points:
   - With a small down payment, I shouldn't assume I'll hit 20% equity quickly. About 1 in 7 past buyers waited more than five years.
   - I should plan to stay put for a long time and keep a cash cushion, because a bad stretch can last years.
   - Trying to time the market isn't the lesson. The takeaway is to buy only if I could handle a long wait for equity.

### R6 (strip B18-S18)
1. **The idea:** The animation seems to compare two ways a home buyer with a small down payment gets to 80% loan-to-value. That is the point where mortgage insurance can usually come off. The first way is the fixed payoff schedule set at purchase (the gray lines). The second is "on paper" (the wavy white line), meaning actual home prices as measured by FHFA and Freddie Mac data. Past buyers who all started at the same time and followed the same rule ended up in very different places. The frames name three of them: Owen, Grace and Victor.

2. **What changes:**
   - Frame 1 shows the lines, the 80% and 75% levels, and a 0–10 year axis.
   - Frames 2 and 3 add a "a plan" marker at about 2 years. They also label Owen, Grace and Victor at different points along the timeline.
   - Frame 4 adds numbers. On paper, the typical buyer reached 80% in 23 months, and about 1 in 7 took more than 60 months. It also notes that about 2 years matched the typical month, "not the slow ones, not the lender's step."
   - Frame 5 switches to a $400,000 home with a stack of money beside it. It is labeled "A measurement, not a next step."
   - Frame 6 shows a house with "buying now + mortgage insurance" next to an apartment building with "still renting, still saving."

3. **What it means:** How long it takes to reach 80% depends heavily on when you buy and what home prices do afterward. A typical past buyer got there in about two years. A meaningful minority (about 1 in 7) waited five years or more. The fixed schedule is slower and more predictable, and the real path can be faster or slower. The captions say this is US-only history, not a forecast, and that it is "not a reason to buy, rent or wait." The frames are also marked "illustrative."

4. **Advice a viewer would take:** The video avoids telling you to buy or to keep renting. It shows that either path is a real option, and the frame 6 pairing shows no winner. The takeaway I'd draw is to not assume mortgage insurance will be gone in two years. I'd plan for the slow case, and the "typical" case is only a possibility. That means checking whether I could afford the payments, including insurance, for five years or more. I'd also keep saving whichever way I go.

### R7 (strip B14-S14)
1. **The idea.** The animation shows how long past US home buyers would have needed to pay a mortgage on schedule before owing 80% or less of the home's value. The caption calls this "months to 80% on paper." The chart is a bar series, with one bar for each month. A bar's height is the number of months to reach 80% on paper. The sources are FHFA and Freddie Mac data via FRED.

2. **What changes across the frames.**
   - Frame 1 shows the bar series with one month highlighted: October 2005, at 112 months (9 years 4 months).
   - Frame 2 adds the label "height = months to 80% on paper" and a bracket marking that bar's height.
   - Frame 3 adds a line labeled "schedule at that rate: 90 payments," marked ILLUSTRATIVE. It wanders across the top of the chart.
   - Frames 4 to 6 add the note "national average, not one home." The marked bar and the line stay the same.
   - Early bars are low. They jump sharply around the 2005 mark, then decline gradually afterward.

3. **What it means.**
   - A buyer in the mid-2000s, near the peak, had to wait far longer than usual to reach 80% on paper.
   - The scheduled payments alone would have taken 90 payments, but the line suggests the real wait ran longer, to 112 months. The most likely reason is falling home prices.
   - The time to reach 80% depends on the purchase price, the interest rate and what home prices did afterward.
   - The footers add limits. This is a national average rather than one home. It covers the US only. It is history, not a forecast.

4. **Advice a viewer would take.**
   - The footer says outright that this is "not a reason to buy, rent or wait," so it gives no direct buy or rent instruction.
   - As a renter with about 10% saved, I'd take away that equity isn't guaranteed to build quickly. Timing, prices and rates can stretch the wait to nearly ten years.
   - If I did buy, I'd plan to stay a long time, keep a cash cushion, and not count on quick equity.
   - I'd also remember that one national average doesn't describe my local market.

### R8 (strip B18-S18)
**1. What idea is the animation showing?**

I think it shows how long a buyer with a small down payment (about 10%) might pay mortgage insurance. The 80% and 75% marks look like loan-to-value levels. 80% is usually where mortgage insurance can come off. The chart doesn't say "mortgage insurance" until the last frame, so that part is my inference. It follows past US buyers, using FHFA and Freddie Mac house-price data from FRED, with each buyer lined up at their purchase date. It's labeled "illustrative."

**2. What changes over time across the frames?**

- **Frame 1:** There's a white line that rises and falls over 10 years. That looks like the path of home prices. Below it are flat or sloping gray lines for the loan schedule.
- **Frames 2 and 3:** The picture fills in with many faint lines, one for each past buyer. Three named examples (Owen, Grace and Victor) show different outcomes. Owen gets to 80% very early, Grace later, and Victor only near year 10. A marker labeled "a plan" sits near year 2. The schedule is "fixed at the start."
- **Frame 4:** Numbers appear. The typical buyer got there in 23 months, and about 1 in 7 took more than 60 months. The note says "≈2 years matched the typical month — not the slow ones, not the lender's step."
- **Frame 5:** It switches to a $400,000 home with a stack of money beside it, and the bottom slice is highlighted. That is probably the down payment. A caption reads "A measurement, not a next step."
- **Frame 6:** It compares two people. One is "buying now + mortgage insurance," shown with a house. The other is "still renting, still saving," shown with an apartment building.

**3. What does it mean?**

Mortgage insurance doesn't end on a fixed date for everyone. On paper, the loan schedule gets you to 80% at one point. In real life, home prices moved and buyers' timelines varied. Most past buyers got there in about two years, but some took five years or more. Planning on two years would have worked for a typical buyer but not for the slow ones.

**4. What advice would a viewer take from this?**

The video avoids telling anyone what to do. The text says "not a reason to buy, rent or wait," "history, not a forecast," and "US only." The takeaway I'd draw is to not assume mortgage insurance will be gone in two years. A cautious buyer would budget for it lasting longer, and past the typical case. They would also see that buying with 10% down and paying insurance is a real option, and so is renting while saving more. Which one is better depends on the person's own situation.

As a renter with about 10% saved, I'd take this as a reminder to plan for the slow case, not the average one. It doesn't tell me whether to buy now.

### R9 (strip B17-S17)
1. **The idea:** The animation follows one past buyer, "Victor," who bought in October 2005 with a 6.07% mortgage. It shows how long it took him to reach 80% loan-to-value, the point where you owe 80% of the home's value and could stop paying mortgage insurance. It compares two ways of getting there: the original payment schedule, and what actually happened to his loan balance relative to the home's value given the local price index. The "ILLUSTRATIVE" tag and the footer say this is one historical example. The footer reads "Past buyers, measured · not a reason to buy, rent or wait. US only · history, not a forecast."

2. **What changes across the frames:**
   - A line for the loan "on paper" and a line for the "price index" are drawn out over a 10-year axis.
   - In the early frames, the on-paper line rises above the 80% line, then falls back toward it. Meanwhile the blue price index line dips well below its starting level, bottoming out around years 5–7, then partly recovers.
   - By frame 3, the on-paper line reaches 80% at 112 months, which is about 9⅓ years.
   - Frames 4 and 5 add a marker showing the original schedule would have hit 80% at 90 payments, about 7.5 years. They also add the note "index still 3.3% below purchase" for the price index.
   - Frame 6 switches to a house with a question mark.

3. **What it means:** Victor bought at the 2005 peak, and prices then fell. Because of that, he reached 80% about 22 months later than the schedule predicted: 112 months instead of 90. Even after ten years, home prices in his area were still 3.3% below what he paid. Paying down the loan alone wasn't enough, because falling prices pushed the 80% milestone back. The house is a risky and uncertain purchase, and the outcome depended on timing and local prices.

4. **Advice a viewer would take:** The animation gives no direct advice. It says outright that this is "not a reason to buy, rent or wait." A viewer could still take away a few cautions:
   - Don't assume your equity will grow on schedule. Prices can fall, and a small down payment (about 10%) leaves little cushion.
   - Plan to stay a long time, since recovery can take a decade.
   - Keep a financial buffer, because you may be paying mortgage insurance for longer than the schedule says.
   - Treat this as one historical case, not a forecast. It doesn't tell you whether buying now is right or wrong.

### R10 (strip B14-S14)
**1. The idea.** The animation shows how long past home buyers had to wait before their loan fell to 80% of their home's value, which is 20% equity. The bars are tall for people who bought around 2005–2007. Frame 1 marks October 2005 as one example: 112 months, or 9 years 4 months. Before that peak the bars are short, and they get short again for later buyers.

**2. What changes across the frames.**
- Frame 1 shows only the bars and the October 2005 marker.
- Frame 2 adds the label "height = months to 80% on paper".
- Frames 3 to 6 add a line tagged "ILLUSTRATIVE". It shows the wait you'd expect from the loan schedule alone at that month's interest rate, and for October 2005 that is 90 payments.
- Frames 4 to 6 add a note that this is a national average, not one home.

For that buyer, the actual wait of 112 months is longer than the 90 payments the schedule alone implies. That is about 22 extra months.

**3. What it means.** Paying down the loan is only part of building equity. If home prices fall or stall after you buy, the gap between the schedule and reality can add years to reaching 20% equity. People who bought near the 2005–2006 peak waited much longer than people who bought at other times. The rest of the 2005 wait comes from the loan's amortization pace, which at the start is mostly interest. The footer says this is measured history for past buyers, US only, and not a forecast.

**4. Advice a viewer would take.** The on-screen text says outright that this is not a reason to buy, rent or wait. The takeaway I'd draw as a renter with about 10% saved is limited:
- Don't assume your equity will build on the loan's schedule. With 10% down, reaching 80% could take a lot longer if prices drop right after you buy.
- Plan to stay long enough, and keep enough cash cushion, to ride out a slow stretch.
- Timing matters, but nobody can predict it. This chart describes the past and says nothing about where prices are going.

### R11 (strip B02-S02)
**1. The idea.** The animation shows how long it takes a buyer who put about 10% down to owe only 80% of the home's value. That means a loan of 90% of the price falling to 80%. The image doesn't say why 80% matters. I'd guess it's the usual point where extra costs like mortgage insurance can come off, but that's my inference.

**2. What changes across the frames.**
- Frames 1 and 2 show an illustrative line. It starts at 90% and slowly slides down to the 80% line by about year 8, just from making the scheduled payments.
- Frame 3 switches to real data: loan divided by home value, with one line for each month someone bought between 1991 and 2016. The lines start fanning out.
- Frames 4 and 5 fill in more of those lines. They spread widely. Some drop fast, and others climb well above 90% before they come back down.
- Frame 6 highlights two cases. The typical buyer got to 80% in about 2 years. The slowest buyer took about 9 years, which is longer than the 8-year schedule.

**3. What it means.** Paying down the loan on schedule takes about 8 years to reach 80%. In real life, home values moved the ratio too. When prices rose, buyers got there much faster, in about 2 years for the typical buyer. When prices fell after purchase, the ratio went up instead of down, and some buyers waited around 9 years. So the timeline depended heavily on when you bought and what the market did.

**4. The advice a viewer would take.** The video itself says this is a measurement and not a reason to buy, rent, or wait. It is US-only, and it is history, not a forecast. As a viewer with a 10% down payment, I'd take away three things:
- Don't assume quick price gains will get me to 80% soon, even though that was typical in the past.
- Plan for roughly 8 years, and know it could take longer if prices drop.
- Treat the time it takes to reach 80% as a real range of outcomes, not a single number.

### R12 (strip B03-S03)
**1. What idea is this animation showing?**
It shows that a mortgage can reach 80% loan-to-value "on paper" without the mortgage insurance coming off automatically. The insurance usually comes off only if the owner asks for it, and the lender has to approve. The first frame cites FHFA/Freddie Mac data on past buyers. The rule frames cite Fannie Mae's Servicing Guide.

**2. What changes over time across the frames?**
- **Frame 1:** The home-value bar and the loan bar sit side by side, with the loan at the 80% line.
- **Frame 2:** A house icon is labeled "insurance still on," even though the loan has hit 80%.
- **Frame 3:** The value bar grows taller, so the loan is a smaller share of it. The text says the loan owner's rule is to request, get an appraisal, and wait.
- **Frame 4:** The stricter Fannie Mae conditions appear: wait at least 2 years and get the loan to 75% or less. The line moves from "80% on paper" down to 75%, and the loan bar gets an orange highlight for the gap.
- **Frames 5 and 6:** Three illustrative buyers, Grace, Owen and Victor, each have a house and a loan stack. The footers say "US only · history, not a forecast."

**3. What does it mean?**
Reaching 80% on paper is not the same as getting rid of the insurance. You usually have to request removal and pay for an appraisal. If you're relying on the home's value rising rather than paying down the loan, the rules can be stricter: a waiting period of at least 2 years and a loan of 75% or less. The three named buyers show that different people can end up in different places. I can't tell from the image what each one's outcome was. The "ILLUSTRATIVE" tags and the footers say this is a measurement of past buyers, not a prediction.

**4. What advice, if any, would a viewer take from this?**
The video says outright that it isn't a reason to buy, rent or wait. As someone with about 10% saved, the practical takeaways for me are:
- A 10% down payment likely means paying mortgage insurance for a while.
- Ask the lender or servicer how removal works. I'd ask what the request process is, whether an appraisal is required, and what the waiting period and loan-to-value thresholds are.
- Don't assume the insurance will disappear on its own at 80%.
- Keep in mind that removal can depend on home value rising, which nobody can promise.

### R13 (strip B13-S13-N2)
1. **The idea.** The animation shows how long it took past home buyers to get to "80% on paper." The label doesn't define that. I'm guessing it means owing 80% or less of the home's value, so the buyer has 20% equity. Each bar is one month when someone bought, and its height is the number of months that buyer needed. The data is US only, from FHFA and Freddie Mac via FRED. Most buyers needed a moderate amount of time, but a few purchase months had a very long wait. That is the "long tail."

2. **What changes across the frames.**
   - Frame 1 is a 3D ribbon of bars. Most are low and marked "typical," with one tall spike on the right.
   - Frame 2 colors the spike blue and calls it "a long tail."
   - Frame 3 flattens the view into a timeline from 1991 to 2016. It adds a 60-month line, and the blue bars sit well above it. They fall around 2005 to 2009.
   - Frames 4 and 5 add the statistic that 14.7% of purchase months (about 1 in 7) took more than 60 months. They label the blue block as "one stretch of purchase months."
   - Frames 5 and 6 add a thin line for the national home price index along the bottom. In frame 6 it is fully drawn and rises over the whole period, with a bump near the blue stretch.

3. **What it means.** Most buyers got to 80% on paper in well under five years. People who bought in the mid-2000s, near the price peak, often waited much longer than five years. The wait depended heavily on when you bought. About 1 in 7 purchase months in this history took more than five years. The footer says this is past buyers, measured, and "not a reason to buy, rent or wait." It also says "history, not a forecast."

4. **What a viewer would take from it.** There's no instruction to buy or not to buy, and the video says so. What I'd take from it:
   - Timing risk is real. If I buy and prices fall or stall soon after, building equity could take much longer than usual.
   - With about 10% down, I should plan to stay put for a long time and keep a cushion for the bad-timing case, rather than assume I'll be at 20% equity in a few years.
   - I shouldn't try to predict the perfect month. The data doesn't tell me whether to rent, buy, or wait, so my own finances, job stability, and how long I'd stay should drive the decision.

### R14 (strip B17-S17)
1. **The idea:** The animation follows one past buyer, Victor, who bought in October 2005 with a 6.07% mortgage. It shows how the housing market after his purchase changed how long it took him to reach 80% of his home's value owed. The image doesn't define the 80% line, but it's probably the loan-to-value level where private mortgage insurance usually comes off. That would fit a buyer who started with about 10% down. The caption says this is "history, not a forecast" and "not a reason to buy, rent or wait."

2. **What changes:** The lines draw out left to right across a 0 to 10 year axis.
   - The gray "schedule" line slopes steadily down toward 80%. This is the payoff path if prices never mattered.
   - The white "on paper" line starts above 80%, then rises above the schedule as the blue price index falls. It peaks around year 5 or 6, then comes back down and meets 80% late.
   - The blue "price index" line dips well below its starting level, bottoms out around years 6 to 7, then recovers only partway. Even at year 10 it is still 3.3% below Victor's purchase price.
   - The labels fill in as it goes: the schedule hits 80% after 90 payments, while "on paper" gets there at 112 months.
   - The last frame is just a house with a question mark.

3. **What it means:** Paying the loan down on schedule wasn't enough for Victor. Home prices fell after he bought, so what he owed stayed high relative to what the home was worth. Reaching 80% took about 22 months longer than the schedule promised (112 months versus 90). A small down payment leaves little cushion, and a price drop can delay equity, and the things that depend on it, for years. Ten years later his home was still worth less than he paid.

4. **Advice a viewer might take:** The video doesn't tell anyone to buy, rent or wait. A viewer would more likely take away a few cautions.
   - Don't assume equity builds on the loan's schedule alone.
   - Expect that a thin down payment could leave you stuck for longer if prices fall.
   - Plan to stay put for a long time, and keep a cash buffer.
   - Treat this as one historical example, since it's US-only and marked illustrative. The question mark house suggests the decision is still open and depends on your own situation.

### R15 (strip B16-S16)
1. **The idea.** The animation follows one past buyer, "Owen," who bought in January 2004 with a 5.71% mortgage. It shows how fast his equity built up in two different ways. One is "on paper," meaning his loan balance against the home's value. The other is the fixed amortization "schedule." The 80% line is probably the loan-to-value mark where a buyer reaches 20% equity. That is usually when private mortgage insurance can come off, though the image doesn't say so. The data comes from FHFA and Freddie Mac via FRED. It is labeled "illustrative."

2. **What changes across the frames.** Three lines are drawn from left to right along a 0–10 year axis.
   - The white "on paper" line starts above 80% and drops to meet the 80% line at about 13 months (frame 4).
   - The thin white "schedule" line barely slopes down. In frame 6 it reaches 80% at about year 7, which is 86 months.
   - The blue house price index line climbs the whole time, up 11.2% by the point where the on-paper line crosses 80% (frames 5–6).

3. **What it means.** Owen reached 80% in about 13 months instead of 86. The reason wasn't mostly his mortgage payments. Rising home prices pushed his loan-to-value down much faster than the payment schedule would have. His quick progress came from price appreciation, which is outside a buyer's control. It is also a single example from one time and place, and the footer says so: "Past buyers, measured · not a reason to buy, rent or wait. US only · history, not a forecast."

4. **Advice a viewer would take.** The video isn't telling anyone to buy, rent, or wait. A viewer would take away these points:
   - Don't count on price gains to build equity quickly. The schedule alone took about 7 years to reach 80%.
   - If you buy with a small down payment, as I would at about 10%, the time to reach 20% equity and drop mortgage insurance could be much shorter or much longer than the schedule says, depending on the market.
   - Plan around the slower schedule and treat any appreciation as a bonus.
   - One buyer's 2004 outcome isn't a forecast. Prices can also fall, which would slow equity growth or reverse it.

### R16 (strip B11-S11)
1. **The idea.** The animation shows how long past home buyers took to get to 80% of their home's value still owed. That's the point where you have 20% equity. Each bar is one purchase month from 1991 to 2016. The chart comes from FHFA and Freddie Mac data via FRED. It uses a buyer who put down about 10%, which is close to my situation. I'm inferring that from the labels, since the frames never say what the 80% threshold is for.

2. **What changes across the frames.**
   - Frame 1 shows only the bars. They are low and flat through the 1990s and early 2000s, jump sharply for buyers around 2005 to 2007, then fall back down.
   - Frame 2 dims the bars and adds a baseline marked "median: 23 months on paper."
   - Frame 3 adds a headline, "90.6% no later than the schedule," and a thin line that drifts downward over the years.
   - Frames 4 and 5 flip the layout and label the line "schedule at each month's rate."
   - Frame 6 brackets the distance between that line and the bars and labels it "gap."

3. **What it means.** The "schedule" line seems to be how many months it would take to reach 80% by making regular payments alone, given the mortgage rate in that month. The bars show how long it actually took once home price changes are included. For about 90.6% of buyers, the actual time was no longer than the schedule. For most buyers, rising prices sped things up. The typical wait was about 23 months. The gap is the time that price gains saved compared with paying down the loan alone. It shrinks and then widens as rates fall. The tall bars for 2005 to 2007 buyers show the minority who bought near the peak and waited much longer.

4. **Advice a viewer would take.** The frames give almost no direct advice. The footer says in every frame: "Past buyers, measured · not a reason to buy, rent or wait," and "US only · history, not a forecast." As a renter with about 10% saved, I'd take away three things:
   - Historically, reaching 20% equity often took only a couple of years, mostly because prices rose.
   - That depended on when you bought, and buyers near a market peak could wait far longer.
   - I shouldn't count on price gains. I should plan on the slower, payment-only schedule and treat anything faster as a bonus.

   It doesn't tell me to buy now or to wait.
