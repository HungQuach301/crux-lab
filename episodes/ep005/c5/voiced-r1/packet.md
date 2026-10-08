# Grading packet (blind). Independent grader. Each label is one reader's answers about one silent 6-frame strip; the strip id is given so you compare against its muted read. Grade literally.

## Rubric
- **Chấm:** người chấm độc lập mù tập; nghĩa 1 / 0,5 / 0 so với "muted read" của `review-c3/spans.json`; cờ khuyên theo **A9** (thận trọng chung — tự kiểm số, hỏi bên cho vay — không tính; khuyên mua/chờ/bán/chọn tính). Người đọc đúng = nghĩa 1 và khuyên_tính false.


Muted read (đáp án đúng) theo hình:
- N1-S06: Each page of the calendar is one monthly payment ($2,362/month, principal + interest, illustrative); as the pages flip, the loan stack slides along the payments and its top draws the balance: it falls slowly at first and faster later.
- B13-S13-N2: Back on the grid, the bars over 60 months turn `warn`; they are few, and they sit together in one stretch of purchase months.

Output JSON only: {"R1": {"score": 1|0.5|0, "advice": true|false, "caution_only": true|false, "why": "<one line>"}, ...}

### R1 (strip N1-S06)
1. **Idea:** The segment shows what a mortgage costs each month at today's rate, and how the loan balance shrinks over its life. The example is a $360,000 loan at September 2026's average rate of 6.86% (Freddie Mac via FRED). The principal-and-interest payment is $2,362 a month. The frames are labeled "illustrative," so they're an example and not a quote for any particular buyer.

2. **What changes:** Frames 1–3 add the rate and then the $2,362 payment next to the $360,000 loan. Frame 4 adds a note that taxes, home insurance and PMI come on top of that payment. Frames 5–6 switch to a balance schedule over 360 payments (30 years). A curve starts high and slopes down, and it's labeled "slowly at first" on the left and "faster later" on the right.

3. **What it means:** The $2,362 covers only principal and interest, so the real monthly housing cost is higher. In the early years most of each payment goes to interest, so the balance barely falls. The balance drops faster in later years as the interest share shrinks. The schedule is fixed on day one.

4. **Advice:** The video doesn't give explicit advice, and its footer says "a measurement, not a next step." A viewer could still take a few things from it:
   - Budget for the full monthly cost, not just principal and interest. Taxes, insurance and PMI add to it, and PMI is likely if you put down about 10%.
   - Don't expect to build equity quickly in the first several years.
   - Use the current rate when you run your own numbers.

   As a renter who has saved about 10%, I'd take this as a reminder to get a full monthly estimate that includes all those costs before deciding I can afford a home.

### R2 (strip N1-S06)
1. This part shows what a mortgage costs each month and how the loan gets paid off. The example is a $360,000 loan at September 2026's average rate of 6.86% (Freddie Mac data via FRED). The monthly principal-and-interest payment is $2,362. Taxes, home insurance and PMI come on top of that. The frames are labeled "illustrative" and "a measurement, not a next step."

2. Frames 1 to 3 add the rate and then the $2,362 payment next to the $360,000 loan. Frame 4 adds a note that taxes, insurance and PMI are extra. Frames 5 and 6 switch to a balance schedule over 360 payments, which is 30 years. A curve shows the balance falling. It falls slowly at first, around payment 0 to 120, and faster later, toward payment 360.

3. The $2,362 is only part of the real monthly cost. Early payments go mostly to interest, so the balance barely drops at first. Later, more of each payment goes to principal, and the balance falls faster. The payment amount stays fixed from day one, which is why the schedule is "set on day one."

4. The video doesn't tell the viewer what to do, and it says so itself. A viewer could still take away a few things:
   - Budget for more than principal and interest, because taxes, insurance and PMI add to it.
   - Expect to build equity slowly in the early years.
   - Don't treat $2,362 as a quote for their own loan. It depends on their loan size, rate and costs.

   For someone who has saved about 10% of a home's price, as I have, PMI is likely to apply, since the down payment is under 20%. That makes the "on top" costs matter even more.

### R3 (strip B13-S13-N2)
1. **The idea.** The typical wait is short, but a minority of cases took much longer. The chart has one bar per purchase month from 1991 to 2016. Each bar's height is the number of months a buyer needed to reach 80% on paper. That's likely a loan-to-value measure, but the frames don't spell it out. About 14.7% of purchase months, roughly 1 in 7, took more than 60 months. Those months are bunched together in a single stretch, not scattered.

2. **What changes across the frames.**
   - Frame 1 is a 3D view of the bars. A low "typical" band runs along most of the grid, with one tall spike near the right.
   - Frame 2 colors the spike blue and labels it "a long tail."
   - Frame 3 flattens the view into a 2D bar chart with a 60-month line. The blue bars sit well above that line, around 2005 to 2009.
   - Frames 4 and 5 add the "more than 60 months: 14.7% (about 1 in 7)" label and a bracket marking "one stretch of purchase months."
   - Frame 6 adds a national home price index line underneath. The blue stretch lines up with the run-up and the peak, just before and during the price slump.

3. **What it means.** The average case hides a risk. How long it took to build 80% equity depended heavily on when someone bought. People who bought just before or during the national price drop waited the longest, often more than 5 years. Most other purchase months were well under that. The delay came from the timing of the market, not from how the buyers behaved.

4. **Advice for a viewer.** The video doesn't tell you to buy, rent, or wait. The on-screen text says "Past buyers, measured · not a reason to buy, rent or wait" and "history, not a forecast." As someone with about 10% saved, I'd take away three things:
   - Plan for the possibility that reaching real equity could take longer than the typical case suggests.
   - Make sure I could stay in the home through a downturn, with a stable job, an emergency fund, and a payment I can afford.
   - Don't treat the typical number as a promise, because roughly 1 in 7 past purchase months went well past 5 years.

   This is US-only historical data, so it doesn't predict what will happen next.

### R4 (strip B13-S13-N2)
1. **The idea.** The "typical" wait for a buyer to reach 80% equity on paper is short, but some purchase months had a much longer wait. The chart shows one bar for each month a person could have bought. Each bar's height is the number of months it took that buyer to reach 80% on paper. Most bars are low, and one tall block of bars is the long tail.

2. **What changes across the frames.**
   - Frames 1–2 show a 3D row of bars. The "typical" level is marked first. Then the tall stretch on the right turns blue and gets the label "a long tail."
   - Frame 3 flattens the view into a standard chart. The x-axis runs from 1991 to 2016, and a 60-month line (5 years) is drawn across it.
   - Frame 4 adds the figure for the blue bars that rise above that line: 14.7%, or about 1 in 7 purchase months, took more than 60 months.
   - Frame 5 labels the blue bars as one stretch of purchase months. A faint line begins to appear underneath.
   - Frame 6 completes that line as the national home price index. The blue stretch sits around the 2005–2009 peak and the slump that followed.

3. **What it means.** About 1 in 7 of the historical purchase months took more than 5 years to reach 80%. Those months are bunched together, not spread out. They are the months just before and during the national price slump. Someone who bought near the peak, then watched prices fall, waited much longer. Buyers in most other periods got there faster. So the typical result hides a bad stretch that depended on when the person bought.

4. **Advice a viewer would take.** The slide says outright that this is "not a reason to buy, rent or wait," and that it is US-only history and not a forecast. A first-time buyer shouldn't read it as a signal about timing. The takeaway is that the average wait understates the risk. Purchase timing can stretch the wait past 5 years, so it's worth planning for the case where you stay in the home longer or prices fall after you buy. With roughly 10% saved, that means keeping a cushion and not counting on a quick payoff.

### R5 (strip N1-S06)
1. This part shows what a mortgage costs each month at today's rate, and how the loan balance shrinks over the life of the loan. The example is a $360,000 loan at September 2026's average rate of 6.86% (Freddie Mac data via FRED). The principal-and-interest payment is $2,362 a month. The frames are labeled "illustrative," so this is an example and not a quote for anyone.

2. Frames 1 to 3 add information in steps. First comes the loan, drawn as a tall stack. Then the 6.86% rate appears. Then the $2,362 monthly payment, shown as a small block next to the loan. In frame 4, a note says taxes, home insurance and PMI (mortgage insurance) are added on top of that payment. Frames 5 and 6 switch to a curve of the loan balance across 360 payments (30 years). The curve falls slowly at the start and then drops faster toward the end. The labels "slowly at first" and "faster later" mark those two stretches.

3. The $2,362 covers only principal and interest. Your real monthly cost will be higher once taxes, insurance and PMI are added. Early on, most of each payment goes to interest, so the balance barely moves. Later, more of each payment goes to principal and the balance falls faster. A fixed payment doesn't mean the balance falls at a steady pace.

4. The video doesn't tell viewers to do anything. Its footer says "A measurement, not a next step." Still, a few points follow from what it shows:
   - Budget for more than the headline payment, since taxes, insurance and PMI come on top.
   - Don't expect to build equity quickly in the first several years. That matters if you might sell or refinance early.
   - Treat the numbers as an example and run your own with a real quote, because your price, down payment, rate and local taxes will differ.

   As a renter who has saved about 10%, I'd take away that PMI probably applies to me. I'd also compare $2,362 plus the extras against my current rent before deciding anything.

### R6 (strip B13-S13-N2)
1. **The idea:** The typical case hides a long tail of bad outcomes. Each bar is one month when someone could have bought a home. Its height is how many months it took that buyer to reach 80% "on paper" (80% of the original down payment, as the chart labels it). Most bars are short, but one cluster is very tall. The takeaway is that the typical wait isn't the whole story.

2. **What changes across the frames:**
   - Frame 1 shows a 3D wall of bars with a "typical" line running along the low part and one tall spike on the right.
   - Frame 2 highlights the spike in blue and labels it "a long tail."
   - Frame 3 flattens the view into a 2D chart. The x-axis runs from 1991 to 2016 and a 60-month line is drawn across it.
   - Frame 4 adds the statistic: more than 60 months for 14.7% of purchase months, about 1 in 7.
   - Frame 5 labels the blue bars as "one stretch of purchase months," clustered around 2005 to 2009.
   - Frame 6 overlays a national home price index line, which rises, peaks near 2006 to 2007, and then falls. This links the tall bars to the price slump.

3. **What it means:** About 1 in 7 of the months when someone could have bought needed more than 5 years to get there. Those bad months aren't spread evenly. They sit together around the peak of the market and the national price decline that followed. Buyers who bought just before or during the slump waited much longer. Buyers in most other periods waited far less.

4. **Advice for a viewer:** The video gives no buy, rent, or wait advice. The on-screen text says so directly: "Past buyers, measured · not a reason to buy, rent or wait," and "US only · history, not a forecast." A viewer in my position, renting with about 10% saved, could take away two points:
   - The typical timeline is a good guide, but a buy-in-a-bad-stretch case could take much longer.
   - If I buy, I should have a cushion and a plan for staying put for many years, in case prices fall right after I buy.

   The video can't tell me whether now is one of those stretches.
