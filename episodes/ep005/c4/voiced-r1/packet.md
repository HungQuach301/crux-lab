# Grading packet (blind). Independent grader. Each label is one reader's answers about one silent 6-frame strip; the strip id is given so you compare against its muted read. Grade literally.

## Rubric
- **Chấm:** người chấm độc lập mù tập; nghĩa 1 / 0,5 / 0 so với "muted read" của `review-c3/spans.json`; cờ khuyên theo **A9** (thận trọng chung — tự kiểm số, hỏi bên cho vay — không tính; khuyên mua/chờ/bán/chọn tính). Người đọc đúng = nghĩa 1 và khuyên_tính false.


Muted read (đáp án đúng) theo hình:
- N1-S06: Each page of the calendar is one monthly payment ($2,362/month, principal + interest, illustrative); as the pages flip, the loan stack slides along the payments and its top draws the balance: it falls slowly at first and faster later.
- B13-S13-N2: Back on the grid, the bars over 60 months turn `warn`; they are few, and they sit together in one stretch of purchase months.

Output JSON only: {"R1": {"score": 1|0.5|0, "advice": true|false, "caution_only": true|false, "why": "<one line>"}, ...}

### R1 (strip N1-S06)
1. **The idea.** The segment shows what a mortgage costs each month at a given rate. It uses a $360,000 loan at September 2026's average rate of 6.86% (Freddie Mac, via FRED). The principal-and-interest payment is $2,362 a month. The frames also show that this figure isn't the full housing cost, and that the loan balance falls on a schedule fixed on day one.

2. **What changes across the frames.**
   - Frames 1–2: the $360,000 loan appears, then the 6.86% rate label.
   - Frame 3: the $2,362/month principal-and-interest payment is added.
   - Frame 4: a note says taxes, home insurance and PMI come on top of that payment.
   - Frames 5–6: a curve plots the loan balance against payment number (0 to 360). A counter moves from payment 35 to payment 114. The curve starts out flat ("slowly at first") and steepens toward the end ("faster later").

3. **What it means.** At this rate, the base payment on a $360,000 loan is about $2,362 a month. The real monthly cost is higher once property taxes, homeowners insurance and mortgage insurance are added. PMI applies because the buyer put down less than 20%. Early payments are mostly interest, so the balance barely drops. Over time more of each payment goes to principal, and the balance falls faster. The schedule is fixed when the loan starts.

4. **What a viewer would take from it.** The video doesn't tell viewers to do anything. The "A measurement, not a next step" caption and the "Illustrative" tag say the same. The practical takeaways are:
   - Budget for more than the $2,362 quoted.
   - Expect to build equity slowly in the first years.
   - Treat the numbers as an example, since actual payments depend on the viewer's own loan size, rate and costs.

### R2 (strip B13-S13-N2)
1. **The idea.** The typical wait to save enough hides a minority of bad cases. Each bar is one month when someone could have bought. Its height is how many months it took to reach 80% on paper, which I read as a 20% down payment. Most bars are short. A cluster of tall ones, the "long tail," rises far above the 60-month (5-year) line.

2. **What changes across the frames.**
   - The view starts as a tilted 3D wall of bars with a "typical" level marked.
   - The tall stretch is then highlighted in blue and labeled "a long tail."
   - The view flattens into a 2D chart running from 1991 to 2016, with a 60-month line drawn across it.
   - A label appears saying 14.7% of purchase months, about 1 in 7, took more than 60 months.
   - The blue block is bracketed as "one stretch of purchase months," covering roughly 2005 to 2009.
   - A national home price index line fades in underneath. It rises through the mid-2000s, peaks around then, and dips afterward. That links the tall bars to the price run-up and slump.

3. **What it means.** Most past buyers got to their target in well under 5 years. The slow cases weren't scattered at random. They were concentrated in months just before and during the national price slump. Buying near the peak, when prices were high and about to fall, meant the paper-equity target took much longer. The averages hide that timing risk.

4. **Advice a viewer would take.** The video says outright that this is "past buyers, measured, not a reason to buy, rent or wait," and that it's US-only history, not a forecast. So it isn't a signal to act. For someone like me, renting with about 10% saved, the takeaway is that when you buy can matter a lot. A typical timeline is a poor guide to your own, so plan for the chance that yours runs long. Keep a cushion and don't assume the median outcome.

### R3 (strip B13-S13-N2)
1. **Idea:** Most past buyers reached a 20% down payment (80% loan-to-value) in a reasonable time, but a minority had to wait much longer. The chart has one bar per purchase month from 1991 to 2016. Each bar's height is the number of months it took to get to 80% on paper. Most bars sit below the 60-month line. A tall cluster of bars forms the "long tail."

2. **What changes across the frames:**
   - The view starts as a 3D ridge of bars. A "typical" band runs along the low bars, and a tall block stands out on the right.
   - The tall block turns blue and is labeled "a long tail."
   - The view flattens to a 2D chart with a 60-month line. The labels read "one bar per purchase month" and "each bar's height: months to 80% on paper."
   - The label "more than 60 months: 14.7% (about 1 in 7)" appears, with a bracket marking "one stretch of purchase months" over the blue bars. The blue bars fall roughly between 2005 and 2009.
   - A national home price index line is added underneath. It rises, peaks around 2006–07, then dips and recovers. The tall bars line up with that peak and the drop after it.

3. **Meaning:** The typical wait looks fine, but about 14.7% of purchase months took more than 5 years. Those months were not scattered. They were bunched together among people who bought just before and during the national price slump. Prices fell after they bought, so their equity was erased and they needed years to get back to 80%. Timing relative to the market drove the long waits, not how carefully people saved.

4. **Advice:** There is little direct advice, and the on-screen text says so: "Past buyers, measured · not a reason to buy, rent or wait," and "US only · history, not a forecast." A viewer should come away knowing that the typical outcome can hide a bad tail. If you buy with a small down payment, a price drop could leave you waiting many years to build equity. That is a reason to plan for the risk, such as keeping a cash cushion and not assuming you'll hit 20% equity soon. It is not a signal to buy now or to wait.

### R4 (strip B13-S13-N2)
1. **The idea:** The "typical" wait to save enough hides a minority of cases where the wait was far longer. Each bar is one purchase month. Its height is how many months a buyer needed to reach 80% on paper (a 20% down payment). Most bars are low. A tall block of them sits together, and that block is the "long tail."

2. **What changes across the frames:** The animation starts with a 3D view, where a "typical" line runs along the low bars and one tall wall stands out. The wall is then highlighted in blue and labeled "a long tail." The view flattens into a timeline from 1991 to 2016, with a 60-month (5-year) line drawn across it. The blue bars are the ones above that line. They're labeled "more than 60 months: 14.7% (about 1 in 7)" and "one stretch of purchase months," covering roughly 2005 to 2009. Last, a national home price index line appears underneath. It rises, peaks around the blue stretch, and then dips. That ties the long waits to the price slump.

3. **What it means:** Most people who bought in this data finished saving in under 5 years. About 14.7% of purchase months needed more than 5 years. Those months bunch together just before and during the national price slump, not scattered randomly. The likely reason is that prices had climbed so far that a buyer's savings couldn't keep up. When you started saving mattered a lot.

4. **Advice a viewer might take:** The video doesn't tell anyone to buy, rent, or wait. The on-screen text says "Past buyers, measured · not a reason to buy, rent or wait" and "history, not a forecast." As a renter with about 10% saved, I'd take two things from it. The typical timeline may be too optimistic, because the timing of a price run-up can stretch it well past 5 years. And I should plan for that possibility rather than assume the average. It doesn't give a signal about what to do now.

### R5 (strip N1-S06)
1. This part shows what a mortgage payment looks like at a given rate. The example is a $360,000 loan at September 2026's average rate of 6.86% (Freddie Mac, via FRED). The principal-and-interest payment is $2,362 a month. Other costs come on top of that, and the loan balance falls on a fixed schedule.

2. Frames 1 and 2 show the $360,000 loan as a tall stack beside a small payment block, and the 6.86% rate label appears. In frame 3 the $2,362/month label attaches to the payment block. In frame 4 an orange note adds "taxes, home insurance and PMI on top." Frames 5 and 6 switch to a balance curve over 360 payments. The payment counter runs from 35 to 114, and the loan stack shrinks as the curve falls. The curve is labeled "slowly at first" on the early, flatter part and "faster later" on the steeper part.

3. The $2,362 is only part of the real monthly cost, because taxes, insurance and PMI (private mortgage insurance) are extra. Early payments are mostly interest, so the balance barely drops at first. Over time more of each payment goes to principal, so the balance falls faster. The curve is "set on day one," meaning the schedule is fixed by the loan terms. The "ILLUSTRATIVE" tag and the "A measurement, not a next step" caption mean this is an example and not a recommendation.

4. The video gives no direct instruction. A viewer in my position, renting with about 10% saved, could take away a few things:
   - Budget for more than the $2,362 principal-and-interest figure. With roughly 10% down, PMI is likely.
   - Don't expect to build equity quickly in the first years.
   - Treat the numbers as an example, and check them against your own loan quote.

### R6 (strip N1-S06)
1. This part shows what a mortgage costs each month at the current average rate, and how the loan balance falls over the life of the loan. The example is a $360,000 loan at September 2026's average rate of 6.86% (Freddie Mac data via FRED). The monthly principal-and-interest payment is $2,362. The frames are labeled "illustrative," and the caption "A measurement, not a next step" says this is not a recommendation.

2. In frames 1–3, the loan and the rate appear first. Then the $2,362 monthly payment is attached to a small payment block beside the tall loan stack. In frame 4, a note is added: taxes, home insurance and PMI (mortgage insurance) come on top of that figure. In frames 5 and 6, the view changes to a balance curve over 360 payments. The payment counter moves from 35 to 114, and the loan stack shrinks as it does. The curve is labeled "slowly at first" on the left and "faster later" on the right.

3. The $2,362 is only part of the real monthly cost, since taxes, insurance and PMI are extra. PMI is likely here because a buyer with about 10% down is typically under the 20% threshold. Early payments go mostly to interest, so the balance barely drops in the first several years. Equity builds much faster in the later years. The schedule is "set on day one," so the pace of paydown is fixed by the loan terms and the rate.

4. The video doesn't tell viewers to do anything. A viewer could still take away a few points. Budget for the full monthly cost, not just principal and interest. Expect equity to build slowly at first. Don't count on a quick payoff if you plan to sell or refinance within a few years. As a renter with about 10% saved, I'd take this as a reason to price out the all-in payment, including PMI, taxes and insurance, before deciding I can afford a home. I wouldn't treat it as a signal to buy or wait.
