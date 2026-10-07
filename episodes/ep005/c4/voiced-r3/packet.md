# Grading packet (blind). Independent grader. Each label is one reader's answers about one silent 6-frame strip; the strip id is given so you compare against its muted read. Grade literally.

## Rubric
- **Chấm:** người chấm độc lập mù tập; nghĩa 1 / 0,5 / 0 so với "muted read" của `review-c3/spans.json`; cờ khuyên theo **A9** (thận trọng chung — tự kiểm số, hỏi bên cho vay — không tính; khuyên mua/chờ/bán/chọn tính). Người đọc đúng = nghĩa 1 và khuyên_tính false.


Muted read (đáp án đúng) theo hình:
- N1-S06: Each page of the calendar is one monthly payment ($2,362/month, principal + interest, illustrative); as the pages flip, the loan stack slides along the payments and its top draws the balance: it falls slowly at first and faster later.
- B13-S13-N2: Back on the grid, the bars over 60 months turn `warn`; they are few, and they sit together in one stretch of purchase months.

Output JSON only: {"R1": {"score": 1|0.5|0, "advice": true|false, "caution_only": true|false, "why": "<one line>"}, ...}

### R1 (strip N1-S06)
1. This part shows what a mortgage costs each month and how the loan balance shrinks. It uses a $360,000 loan at September 2026's average rate of 6.86% (Freddie Mac data via FRED). The principal-and-interest payment is $2,362 a month. Taxes, home insurance and PMI (mortgage insurance) are added on top of that. The balance then falls along a schedule that is fixed on day one.

2. Across the frames, the labels build up. First the $360,000 loan appears. Then the rate is added, then the $2,362 payment, then a note that taxes, insurance and PMI come on top. In frames 5 and 6 the view switches to a balance curve over 360 payments. The payment counter goes from 35 to 114, and the curve drops slowly at first and faster later. Every frame carries an "ILLUSTRATIVE" tag and the caption "A measurement, not a next step."

3. The $2,362 is only part of what you would pay each month. Your real monthly cost would be higher. Early on, most of each payment goes to interest, so the balance barely falls. Only in the later years does most of the payment reduce the principal. The frames suggest that payoff speeds up as the loan ages. The example is illustrative, so it isn't a quote for any particular buyer.

4. The video gives no direct advice, and its caption says this is a measurement, not a next step. A viewer could still take away three things:
   - Budget for the full monthly cost, not just principal and interest.
   - Expect to build equity slowly in the first years.
   - Treat the rate and payment as a snapshot, since they change with the market and with your own loan terms.

   As a renter with about 10% saved, I would work out my own numbers before deciding anything. That means getting real quotes for taxes, insurance and PMI.

### R2 (strip N1-S06)
1. **The idea.** This part shows what a mortgage costs each month and how the loan gets paid off. The example is a $360,000 loan at September 2026's average rate of 6.86% (Freddie Mac data via FRED). The principal-and-interest payment is $2,362 a month. Taxes, home insurance and PMI (mortgage insurance) are extra. The balance follows a schedule that is fixed on day one.

2. **What changes.**
   - Frames 1–3: the $360,000 loan stack appears, then the rate, then the $2,362 payment label.
   - Frame 4: a "taxes, home insurance and PMI on top" note is added to the payment.
   - Frames 5–6: the view switches to a balance curve over 360 payments. The payment counter moves from 35 to 114, and the stack of the loan shrinks as the counter rises.
   - The curve starts out flat and then drops more steeply. It is labeled "slowly at first" and "faster later."

3. **What it means.**
   - The $2,362 is only part of the real monthly cost. The full payment is higher once taxes, insurance and PMI are added.
   - Early payments go mostly to interest, so the balance barely falls. Over time more of each payment goes to principal, and the balance falls faster.
   - The schedule is set when the loan starts, and the graphic is marked "illustrative."

4. **Advice for a viewer.** The video gives no direct advice. The footer says "A measurement, not a next step." A viewer could still take away three points:
   - Budget for the full monthly cost, not just principal and interest.
   - Expect to build equity slowly in the first years.
   - Treat the numbers as an example, since your own rate, loan size and extra costs will differ.

   As a renter with about 10% saved, I would take this as a reason to get real quotes before deciding. The $2,362 figure is not enough to decide on.

### R3 (strip B13-S13-N2)
1. **The idea.** The usual wait to save up isn't the whole story. A minority of buyers waited much longer than the rest. The chart has one bar per month in which someone could have bought. Each bar's height is how many months it took to reach 80% on paper. Most bars are short. A cluster of tall bars forms the "long tail." About 14.7% of purchase months, roughly 1 in 7, took more than 60 months (5 years).

2. **What changes across the frames.**
   - Frames 1–2: The view starts as a 3D wall of bars. The "typical" low stretch is marked first, and then the tall block is highlighted in blue as "a long tail."
   - Frame 3: The view flattens to a 2D bar chart from 1991 to 2016, with the source and axes labeled. The blue block sits around 2005 to 2009.
   - Frame 4: The 60-month line and the "14.7% (about 1 in 7)" label appear.
   - Frames 5–6: The blue block is labeled "one stretch of purchase months." A national home price index line is added underneath. It rises through the mid-2000s, peaks, then dips, which lines up with the tall bars.

3. **What it means.** The long waits aren't scattered at random. They're concentrated in the months just before and during the national price slump. Buyers in those months waited the longest, and buyers outside that window mostly waited much less. The slump drove the tail, so "the typical wait" hides how bad the worst stretch was. This is also history from US data, not a forecast.

4. **The advice.** The video gives no instruction. Its on-screen note says this is "not a reason to buy, rent or wait." A viewer could take away a few things:
   - Don't plan around the typical timeline alone. Allow for the chance that it takes much longer.
   - Timing relative to the price cycle matters a lot, and it's hard to predict.
   - Treat the numbers as a picture of what has happened to past buyers, not a signal about what to do now.

### R4 (strip N1-S06)
1. This part shows what a mortgage payment looks like at the current average rate. It uses a $360,000 loan at 6.86%. The principal-and-interest payment is only part of the monthly cost, and the loan balance falls on a schedule fixed on day one.

2. The frames build up in steps. First the $360,000 loan appears as a stack next to a payment slip. Then the September 2026 rate of 6.86% is added. Then the payment is labeled at $2,362 a month for principal and interest. Then a note says taxes, home insurance and PMI come on top of that. In the last two frames a curve shows the balance falling over 360 payments. The payment marker moves from payment 35 to payment 114. The curve is labeled "slowly at first" and "faster later." Each frame also carries an "illustrative" tag and the caption "A measurement, not a next step."

3. The $2,362 is not the full monthly housing cost. Taxes, insurance and mortgage insurance add to it. Early payments go mostly to interest, so the balance barely moves at first. The paydown speeds up in the later years. The loan's whole path is set when you sign.

4. The video doesn't tell viewers to do anything, and the caption says so directly. A first-time buyer could still take a few points from it:
   - Budget for the full monthly cost, not just the principal-and-interest figure.
   - Expect to build equity slowly in the early years.
   - Treat the numbers as an example, since they are illustrative and your own rate and loan size will differ.

### R5 (strip B13-S13-N2)
1. **The idea:** The typical wait to build 20% equity (80% on paper, in the chart's wording) is short. But some buyers waited much longer, and those long waits are bunched together in one period. Each bar is a purchase month. Its height is the number of months it took that buyer to reach 80% on paper.

2. **What changes across the frames:**
   - Frames 1–2 show a 3D wall of bars. A flat "typical" band runs along most of it, and one tall block stands out and turns blue as "a long tail."
   - Frame 3 flattens this into a 2D chart, with years from 1991 to 2016 along the bottom.
   - Frame 4 adds a label: more than 60 months happened for 14.7% of purchase months, about 1 in 7.
   - Frame 5 marks the blue block as "one stretch of purchase months." A faint line starts to appear underneath.
   - Frame 6 completes that line as the national home price index. The blue stretch sits around 2005–2009, when prices peaked and then fell.

3. **What it means:** The long waits were not spread evenly across history. They came from buying in the years just before and during the national price slump, when prices dropped after those purchases. People who bought in other years mostly got there much faster. Roughly 1 in 7 purchase months fell into the long-wait group, so the typical case doesn't describe everyone.

4. **Advice for a viewer:** The video gives no direct advice. The on-screen text says this is "Past buyers, measured · not a reason to buy, rent or wait," and "history, not a forecast." As a renter with about 10% saved, I'd take away that the usual timeline is encouraging but not guaranteed. If I bought near a market peak, I could be waiting more than 5 years to reach 20% equity. So I should plan to stay put for a long time and keep a cash cushion. I shouldn't count on a quick payoff, and I shouldn't treat this chart as a signal to buy now or hold off.

### R6 (strip B13-S13-N2)
1. **The idea:** The typical home buyer reached a 20% down payment (80% "on paper", meaning loan-to-value) fairly quickly. But the average hides a minority of buyers who waited much longer. Each bar is one purchase month. Its height is how many months it took buyers from that month to reach 80% on paper. About 14.7% of purchase months, roughly 1 in 7, took more than 60 months.

2. **What changes across the frames:**
   - Frames 1–2 show a 3D bar chart. A low "typical" ridge runs along most of it, and a tall block sticks up on one side. That block gets highlighted in blue and labeled "a long tail."
   - Frames 3–4 flatten the chart into a 2D view. A horizontal line marks the 60-month cutoff, and the blue bars poking above it are labeled "more than 60 months: 14.7% (about 1 in 7)."
   - Frames 5–6 bracket that blue section as "one stretch of purchase months," about 2005 to 2009. A national home price index line is then added underneath. It rises, peaks around 2006–2007, then falls and recovers, so the slow months line up with the price slump.

3. **What it means:** The long waits were not spread evenly across time. They were concentrated among people who bought just before and during the national price crash. Prices fell after they bought, so it took many years to build 20% equity on paper. Buyers in most other periods got there much faster. The risk is tied to when you buy relative to a national downturn, not to a steady share of buyers.

4. **What a viewer would take away:** There is no instruction to buy, rent, or wait. The on-screen text says "Past buyers, measured · not a reason to buy, rent or wait" and "history, not a forecast." The practical lesson is to avoid relying only on the typical case. Buying a home carries a small but real chance of a very long wait to build equity if prices fall soon after you buy. You'd want a financial cushion and a plan to stay put for years, because a downturn can stretch that wait well past the typical timeline. This is US-only data and doesn't predict what will happen next.
