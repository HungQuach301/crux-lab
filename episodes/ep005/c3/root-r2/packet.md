# Grading packet (blind). Independent grader. Each label is one reader's answers about one silent 6-frame strip; the strip id is given so you compare against its muted read. Grade literally.

## Rubric
- **Chấm:** người chấm độc lập mù tập; nghĩa 1 / 0,5 / 0 so với "muted read" của `review-c3/spans.json`; cờ khuyên theo **A9** (thận trọng chung — tự kiểm số, hỏi bên cho vay — không tính; khuyên mua/chờ/bán/chọn tính). Người đọc đúng = nghĩa 1 và khuyên_tính false.


Muted read (đáp án đúng) theo hình:
- N1-calendar: Each page of the calendar is one monthly payment ($2,362/month, principal + interest, illustrative); as the pages flip, the loan stack slides along the payments and its top draws the balance: it falls slowly at first and faster later.
- N2-bars: Back on the grid, the bars over 60 months turn warn; they are few (about 1 in 7), and they sit together in one stretch of purchase months (2005–2009), under the part of the national price index that peaks and falls.

Output JSON only: {"R1": {"score": 1|0.5|0, "advice": true|false, "caution_only": true|false, "why": "<one line>"}, ...}

### R1 (strip N2-bars)
1. **The idea.** The animation shows that the time it takes to build an 80% stake in a home (a 20% down payment, "on paper") is usually short but sometimes much longer. The distribution has a "long tail." The chart uses US data from FHFA and Freddie Mac via FRED. It has one bar per month in which someone bought a home, covering roughly 1991 to 2016.

2. **What changes across the frames.**
   - Frames 1–2 show a 3D bar chart. A "typical" line runs along the low bars, and a tall gold block stands out as the long tail.
   - Frame 3 flattens the chart to a 2D view. It adds a 60-month threshold line and the label "more than 60 months: 14.7% (about 1 in 7)." The gold bars are the purchase months that crossed that line, which cluster around 2005–2009.
   - Frames 4–5 highlight that gold cluster as "one stretch of purchase months."
   - Frame 6 adds a blue line for the national home price index. It rises steadily and peaks around 2005–2007, which is the same period as the tall gold bars.

3. **What it means.** For most past buyers, reaching 80% on paper took well under 60 months. About 1 in 7 buyers needed more than five years. Those buyers weren't spread evenly across time. They were concentrated in a single stretch, the mid-2000s. The blue price line suggests why: people who bought near the price peak waited the longest to build equity. The long tail is mostly a timing effect, not a random one.

4. **Advice a viewer would take.** The video says outright that this is "not a reason to buy, rent or wait," and that it is "history, not a forecast." So it gives no instruction to buy or not. A first-time buyer in their late 20s or early 30s could still take a few things from it:
   - When you buy matters a lot. Buying at a price peak can leave you waiting years to build equity.
   - Don't assume a typical short timeline. Plan for the possibility that it takes more than five years, and only buy if you can stay in the home that long.
   - The data covers only the US, and only people who actually bought.

### R2 (strip N1-calendar)
1. **The idea:** The animation shows how a 30-year fixed mortgage is paid down. It uses an illustrative $360,000 loan at 6.86%, which it labels as the September 2026 average rate from Freddie Mac via FRED. The monthly payment is $2,362 for principal plus interest.

2. **What changes:** Frame 1 shows a house, a person, a calendar page and a tall stack of cash. In frame 2 the stack is labeled as the $360,000 loan. Frame 3 labels the calendar as the $2,362 monthly payment, and an axis appears running from 0 to 360 payments. In frames 4 to 6 the calendar flips through payments 43, 92 and 114. The stack of cash moves along a curve of the loan balance. The curve falls slowly at first and then more steeply, labeled "slowly at first" and "faster later."

3. **What it means:** Early payments go mostly to interest, so the balance barely drops. After about 10 years (120 payments) the balance is still high. As the balance shrinks, more of each fixed payment goes to principal, so the balance falls faster in the later years. The stack in frame 6 is still tall at payment 114.

4. **Advice a viewer would take:**
   - Don't expect to build equity quickly in the first several years.
   - Budget for a payment of about $2,362 a month, before taxes, insurance and upkeep, which the animation doesn't show.
   - Plan to stay in the home a long time. If you sell early, you will have paid down little of the loan.
   - The rate matters a lot, and the animation implies that extra principal payments early on would help.

   The animation doesn't give any explicit advice. It is labeled "illustrative," so I'd treat the numbers as an example and not as a quote for your own loan.

### R3 (strip N1-calendar)
1. **The idea:** The animation shows how a 30-year fixed mortgage gets paid down. The example is a $360,000 loan at a 6.86% rate, which it labels as the September 2026 average from Freddie Mac via FRED. It is marked "illustrative", so it is a model and not a real loan offer. The monthly payment is $2,362 for principal plus interest.

2. **What changes across the frames:**
   - Frame 1 sets the scene with a house, a person, a calendar (monthly payments) and a tall stack of cash (the loan).
   - Frames 2 and 3 label the loan amount, the rate and the monthly payment.
   - Frames 4 to 6 add a curve of the loan balance over 360 payments. The calendar flips through payments 43, 92 and 114, and the cash stack shrinks along the curve.
   - The curve starts out nearly flat, with the label "slowly at first". It steepens toward the end, with the label "faster later".

3. **What it means:** Early payments go mostly to interest, so the balance barely drops. Around payment 114, which is nearly 10 years in, the stack is still tall. More of each payment goes to principal as time passes, so the balance falls faster in the later years. That is how amortization works. The payment stays the same, but its makeup shifts from interest to principal.

4. **What a viewer would take away:**
   - Don't expect to build equity quickly in the first several years. A first-time buyer who plans to move within a few years may owe almost as much as they started with.
   - Budget for the full monthly payment, which is about $2,362 on this loan before taxes, insurance and maintenance.
   - The rate has a big effect on the total cost, and that's a reason to shop lenders. Extra principal payments early on can cut interest, because that's when the balance falls slowest.
   - The animation doesn't say whether to buy or rent. It only shows what the loan costs, so you'd want to weigh how long you plan to stay.

### R4 (strip N2-bars)
1. The animation shows how long it takes a home buyer to reach 80% equity "on paper". The bars are for the month someone bought a home, and the height of each bar is the number of months until they got there. Most bars are short. A small group of purchase months has a very long wait, which the animation calls "a long tail."

2. Frames 1 and 2 show a 3D view that turns until you face the bars flat-on. A "typical" line is marked, and the tall gold block stands out from the gray bars. Frames 3 to 6 show the flat chart for purchases from 1991 to 2016. They add a 60-month line, the label "more than 60 months: 14.7% (about 1 in 7)", and a bracket marking "one stretch of purchase months." Frame 6 adds a blue line for the national home price index. The gold bars are the purchases from about 2005 to 2009. Those buyers waited the longest, well over 60 months. The blue price line is rising over the whole period and dips after the mid-2000s peak.

3. It means most past buyers got to 80% fairly quickly, but about 1 in 7 waited more than five years. Those long waits were bunched into a single window, the years around the housing peak and crash. They weren't spread evenly across time. The price line suggests why. People who bought near the top saw prices fall, so their equity took much longer to build. The waits depended heavily on when you bought.

4. The video's own caption says this is "not a reason to buy, rent or wait," and calls it "history, not a forecast." With that caveat, a viewer could take away a few things:
   - Don't assume you'll hit 20% equity quickly. Plan for the possibility that it takes five years or more.
   - Buy only if you could stay put for a long time and could afford the payments through a price dip.
   - With about 10% down, you start further from 80%, so a bad stretch could hurt you more. It would be worth knowing how long a mortgage insurance (PMI) payment might last.
   - Don't try to time the market. The result depends on the purchase month, and nobody can predict that in advance.

The image only covers US data from 1991 to 2016. It can't say whether now is a good time to buy.

### R5 (strip N1-calendar)
1. **The idea.** The animation shows how a 30-year mortgage gets paid down. It uses a $360,000 loan at 6.86%, which is the September 2026 average rate from Freddie Mac via FRED. The $2,362 monthly payment covers principal plus interest. The "ILLUSTRATIVE" tag says these are example numbers, not a quote.

2. **What changes.**
   - Frame 1 shows a house, a person, a calendar pad and a stack of cash. These stand for the buyer, the monthly payment and the loan.
   - Frames 2 and 3 label the stack as the $360,000 loan and the calendar as the $2,362 monthly payment. A timeline from 0 to 360 payments appears.
   - Frames 4 to 6 step through payments 43, 92 and 114. The calendar page flips with each payment, and the cash stack slowly shrinks along a curve.
   - The curve is labeled "slowly at first" and later "faster later."

3. **What it means.** Early payments go mostly to interest, so the balance barely falls in the first several years. Even after about 114 payments (nearly 10 years), the stack is still tall. The principal falls faster only in the later years, because the interest portion shrinks as the balance drops. This is how amortization works.

4. **The advice.** I'd take away four things:
   - **Budget for the payment.** Buying means committing to about $2,362 a month for a long time, before taxes, insurance and upkeep.
   - **Expect slow equity early.** Don't assume you'll build much equity in the first few years. That matters if you might move or sell soon, since selling costs and slow paydown can leave you with little or nothing.
   - **Plan to stay a long time.** The payoff comes from holding the home for years.
   - **Consider the rate.** At 6.86%, a lot of each payment is interest. Shopping for a lower rate, making extra principal payments, or waiting for a better rate could save real money.

   The animation doesn't tell you outright to buy or not to buy. It only shows the shape of the debt.
