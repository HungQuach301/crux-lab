# Grading packet (blind). Independent grader. Each label is one reader's answers about one silent 6-frame strip; the strip id is given so you compare against its muted read. Grade literally.

## Rubric
- **Chấm:** người chấm độc lập mù tập; nghĩa 1 / 0,5 / 0 so với "muted read" của `review-c3/spans.json`; cờ khuyên theo **A9** (thận trọng chung — tự kiểm số, hỏi bên cho vay — không tính; khuyên mua/chờ/bán/chọn tính). Người đọc đúng = nghĩa 1 và khuyên_tính false.


Muted read (đáp án đúng) theo hình:
- N1-calendar: Each page of the calendar is one monthly payment ($2,362/month, principal + interest, illustrative); as the pages flip, the loan stack slides along the payments and its top draws the balance: it falls slowly at first and faster later.

Output JSON only: {"R1": {"score": 1|0.5|0, "advice": true|false, "caution_only": true|false, "why": "<one line>"}, ...}

### R1 (strip N1-calendar)
1. **The idea:** The animation shows how a 30-year fixed mortgage gets paid down. It uses a $360,000 loan at the September 2026 average rate of 6.86% (Freddie Mac, via FRED). The monthly payment for principal and interest is about $2,362. The label says the loan balance schedule is "set on day one." The whole payoff path is fixed when you sign the loan.

2. **What changes across the frames:**
   - Frame 1 sets the scene. There's a house, a person, a calendar page standing for monthly payments, and a tall stack of cash standing for the loan.
   - Frames 2 and 3 label the loan amount, the rate, and the $2,362 payment. A payment-count axis appears, running 0 to 120 to 240 to 360.
   - Frames 4 to 6 step through payments 43, 92, and 114. The calendar page flips with each payment, and the cash stack shrinks slowly along a curve. The curve is labeled "slowly at first" and then "faster later."

3. **What it means:** Each payment is the same size, but its makeup changes. Early on, most of the payment goes to interest, so the balance barely drops. Even after about 114 payments, roughly 9.5 years in, a large share of the loan is still owed. Later, as the balance falls, more of each payment goes to principal and the balance drops faster. The "ILLUSTRATIVE" tag means the numbers are an example and not a quote.

4. **What a viewer would take from it:**
   - Early on in a mortgage, you build equity slowly. A first-time buyer who sells or refinances within a few years shouldn't expect much of the loan to be paid off.
   - At a rate near 6.86%, the interest cost is large. The rate and the loan size matter a lot.
   - Because the schedule is set up front, extra principal payments early on would have the biggest effect on shortening the curve. The image doesn't state that directly, so it's my inference.
   - The $2,362 figure covers only principal and interest. It leaves out taxes, insurance, and upkeep, so the real monthly cost would be higher. The image doesn't show those costs.
   - With only about 10% saved, you should budget for the full payment, plan to stay a while, and not count on fast equity.
