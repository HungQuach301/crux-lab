# Grading packet (blind). Independent grader. Each label is one reader's answers about one silent 6-frame strip; the strip id is given so you compare against its muted read. Grade literally.

## Rubric
- **Chấm:** người chấm độc lập mù tập; nghĩa 1 / 0,5 / 0 so với "muted read" của `review-c3/spans.json`; cờ khuyên theo **A9** (thận trọng chung — tự kiểm số, hỏi bên cho vay — không tính; khuyên mua/chờ/bán/chọn tính). Người đọc đúng = nghĩa 1 và khuyên_tính false.


Muted read (đáp án đúng) theo hình:
- N1-calendar: Each page of the calendar is one monthly payment ($2,362/month, principal + interest, illustrative); as the pages flip, the loan stack slides along the payments and its top draws the balance: it falls slowly at first and faster later.
- N2-bars: Back on the grid, the bars over 60 months are set apart in their own colour; they are few (about 1 in 7), and they sit together in one stretch of purchase months (2005–2009), under the part of the national price index that peaks and falls.

Output JSON only: {"R1": {"score": 1|0.5|0, "advice": true|false, "caution_only": true|false, "why": "<one line>"}, ...}

### R1 (strip N1-calendar)
1. **The idea:** The animation shows how a 30-year mortgage gets paid down. It uses an illustrative $360,000 loan at 6.86%, the September 2026 average rate from Freddie Mac via FRED. The monthly payment is $2,362 for principal plus interest. The balance follows a schedule that is fixed on day one.

2. **What changes:**
   - Frame 1 shows a house, a person, a calendar page and a tall stack of cash.
   - Frame 2 shrinks the scene and labels the stack as the $360,000 loan.
   - Frame 3 adds the $2,362/month payment and a 0–360 payments axis.
   - Frames 4 to 6 count payments (43, 92, 114) as the calendar flips forward. The stack shrinks a little at a time. A curve labeled "loan balance schedule · set on day one" starts nearly flat ("slowly at first") and steepens toward 360 ("faster later").

3. **What it means:** Early payments go mostly to interest, so the balance barely falls for the first several years. Even after about 114 payments, roughly 9.5 years, the stack is still tall. Most of the principal gets paid off in the later years. The "set on day one" label says the payment schedule is locked in when you sign the loan. The "illustrative" tag says these are example numbers, not a quote.

4. **Advice a viewer would take:**
   - The video doesn't give explicit advice, but the implied lesson is not to expect fast equity from your payments early on.
   - The real cost of a mortgage is mostly interest up front, so the rate and the loan size matter a lot.
   - If you might move within 5 to 10 years, you'd have paid down little principal. Any equity would then come mostly from the home's price rising or from your down payment.
   - For me, with about 10% saved, I'd take away two things. Budget for the full $2,362-type payment, and don't count on the balance dropping quickly. I'd also check the numbers against my own loan amount and rate.

### R2 (strip N2-bars)
1. **The idea.** The animation shows that the time it takes a home buyer to build up 80% equity on paper has a "long tail." For most buyers the time is fairly typical. For a minority it runs much longer. The bars are labeled "months to 80% on paper." I read that as how long it took past buyers to reach 80% loan-to-value, though the image doesn't spell that out. The chart shows one bar for each month a home was purchased, from 1991 to 2016. Its sources are FHFA and Freddie Mac data via FRED.

2. **What changes across the frames.**
   - Frames 1–2 show a 3D ridge of bars. The camera swings from an angle to a flat view, and a "typical" line sits across the lower part of the ridge. A tall blue block stands out near the right side.
   - Frame 3 flattens the view into a 2D bar chart. A 60-month line is added, along with the label "more than 60 months: 14.7% (about 1 in 7)."
   - Frame 4 adds a bracket and shading around the blue stretch of purchase months, which sit around 2005–2009.
   - Frame 5 labels that stretch "one stretch of purchase months." A thin line begins to draw along the bottom.
   - Frame 6 completes that line and labels it "national home price index." The index rises, peaks around 2005–2007, dips, and then recovers.

3. **What it means.**
   - Most purchase months had bars below the 60-month line, so those buyers reached 80% in under five years.
   - About 1 in 7 buyers needed more than five years. Nearly all of them bought in the blue stretch, roughly 2005–2009.
   - Those buyers bought near the top of the price index. Prices then fell, so their paper equity took much longer to build.
   - The long tail comes from when people bought, not from how they behaved. A buyer's timing relative to the price cycle can matter more than the average suggests.

4. **What a viewer would take from it.**
   - The on-screen text says this is "Past buyers, measured · not a reason to buy, rent or wait," and "history, not a forecast." So the animation doesn't tell anyone to buy or to wait.
   - As a renter with about 10% saved, I'd take away a few cautions:
     - Don't assume you'll be at 80% equity in a few years.
     - Plan to stay in the home for a long time, because a bad stretch can take more than 5 years to recover from.
     - Keep a cushion so you aren't forced to sell during a downturn.
     - A small down payment makes equity more sensitive to price drops.

### R3 (strip N1-calendar)
1. **The idea:** The animation shows how a 30-year fixed mortgage gets paid down. It uses an illustrative $360,000 loan at 6.86%, the September 2026 average rate from Freddie Mac via FRED. The monthly payment is $2,362 for principal plus interest. The balance is a stack of cash, and the payment is a calendar page.

2. **What changes:**
   - Frame 1 sets the scene: a house, a person, a calendar, and a tall stack of cash.
   - Frames 2 and 3 label the loan and the monthly payment, and a payment-count axis appears (0, 120, 240, 360).
   - Frames 4 to 6 step through payments 43, 92, and 114. The calendar flips each month, and the stack of cash slides along a curve showing the balance falling.
   - The curve is labeled "set on day one." It drops slowly at first and faster later.

3. **What it means:** The payment is the same every month, but the balance doesn't fall at a steady pace. In the early years most of each payment goes to interest, so the balance barely moves. Later, more of each payment goes to principal, and the balance drops faster. The whole schedule is fixed when you sign the loan. The "illustrative" tag means these are example numbers, not a quote.

4. **Advice a viewer might take:**
   - Expect to build equity slowly in the first several years. After about 10 years (120 payments), a large share of the loan is still owed.
   - Look at the total cost of the loan, not just whether the monthly payment fits your budget.
   - Rate and loan length matter a lot, so compare lenders and think about how long you'll stay in the home.
   - If you sell or refinance early, you will have paid off less than you might expect.
   - Extra principal payments early on would help the most. The animation implies this but doesn't say it.

   The video gives no explicit recommendation, so these are my inferences from the picture. As a renter with about 10% saved, I'd take this as a reason to run the real numbers. I'd include taxes, insurance, and maintenance, which aren't shown here.

### R4 (strip N2-bars)
1. **The idea:** The animation shows that the time it takes a new home buyer to build equity is usually short but has a long tail. Each bar is one month in which people bought a home. Its height is how many months it took that group to reach 80% of the home's value owed, which is 20% equity "on paper." Most bars are low, meaning a typical wait. A tall cluster sticks up far above that.

2. **What changes across the frames:**
   - Frames 1 and 2 show a 3D ribbon of bars. A "typical" line runs along the low part, and a blue block of tall bars is labeled "a long tail."
   - Frame 3 flattens this into a 2D chart from 1991 to 2016. A 60-month line is added, along with the label "more than 60 months: 14.7% (about 1 in 7)."
   - Frames 4 and 5 highlight the blue bars as "one stretch of purchase months," which falls around 2005 to 2009.
   - Frame 6 adds a thin line for the national home price index along the bottom. It rises, peaks around the mid-2000s, dips, then climbs again.

3. **What it means:**
   - **Most buyers:** Most people who bought in this period reached 80% in well under five years.
   - **The long tail:** About 1 in 7 buyers needed more than five years. Almost all of them bought in the mid-2000s, near the peak of home prices. Prices then fell, which wiped out their equity and delayed the wait.
   - **Timing risk:** The risk was concentrated in when someone bought, not spread evenly across all buyers.

4. **Advice a viewer would take:** The animation gives no explicit instruction, and the on-screen text says so: "not a reason to buy, rent or wait," "history, not a forecast," and "US only." As a renter with about 10% saved, I would take away two cautions:
   - **Don't assume quick equity.** If you buy with a small down payment, you could be underwater or stuck for years if prices fall soon after.
   - **Plan to stay longer.** Have a cushion and expect to hold the home well beyond five years.

   Most buyers in this data did fine, so it isn't a warning against buying.
