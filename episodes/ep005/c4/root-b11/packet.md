# Grading packet (blind). Independent grader. Each label is one reader's answers about one silent 6-frame strip; the strip id is given so you compare against its muted read. Grade literally.

## Rubric
- **Chấm:** người chấm độc lập mù tập; nghĩa 1 / 0,5 / 0 so với "muted read" của `review-c3/spans.json`; cờ khuyên theo **A9** (thận trọng chung — tự kiểm số, hỏi bên cho vay — không tính; khuyên mua/chờ/bán/chọn tính). Người đọc đúng = nghĩa 1 và khuyên_tính false.


Muted read (đáp án đúng) theo hình:
- B11-S11: Most purchase months have short bars; a horizontal median line sits low at 23 months, far below a faint ridge of the schedule's own months; nearly every bar ends below its schedule mark.

Output JSON only: {"R1": {"score": 1|0.5|0, "advice": true|false, "caution_only": true|false, "why": "<one line>"}, ...}

### R1 (strip B11-S11)
1. **The idea.** The animation shows how long past US home buyers took to get to 80% loan-to-value. That means owning 20% of the home on paper, through price gains and loan paydown. There is one bar per purchase month, from 1991 to about 2016. The source is FHFA and Freddie Mac data via FRED.

2. **What changes across the frames.**
   - Frame 1 shows only the bars. They run low and steady at roughly 20 months or more through the 1990s and early 2000s. They jump sharply for people who bought around 2005–2007, then fall back down after 2010.
   - Frame 2 adds a median line, "23 months on paper," and dims the bars so the line stands out.
   - Frame 3 adds a label saying 90.6% of buyers reached 80% no later than the standard amortization schedule would have. A jagged line also appears, sloping downward over time.
   - Frames 4 and 5 relabel that line as "schedule at each month's rate." It is the time it would take on the normal loan payoff schedule at that month's mortgage rate, and it falls as rates fall.
   - Frame 6 marks the distance between that schedule line and the bars as the "gap."

3. **What it means.**
   - For most buyers, reaching 80% took less time than the schedule alone predicted. Price appreciation sped it up, and that is the gap.
   - The typical wait was about two years.
   - Buyers from the mid-2000s peak took much longer. Prices fell after they bought, so they were stuck far longer before reaching 80%.
   - The outcome depended heavily on when someone bought.

4. **What advice a viewer would take.** The footer says outright: "Past buyers, measured · not a reason to buy, rent or wait," and "US only · history, not a forecast." So the animation gives no buy-or-rent advice. A viewer could reasonably conclude two things:
   - Reaching 20% equity often takes about two years, and usually less than the loan schedule alone implies.
   - Timing risk is real, because buyers near a market peak waited much longer.

   For someone with about 10% saved, that means 20% equity, which is the point where private mortgage insurance can typically be dropped, is plausible within a few years. It isn't guaranteed, and past results don't predict future prices.

### R2 (strip B11-S11)
**1. The idea.** The animation shows how long past US home buyers took to get their loan down to 80% of the purchase price, which is 20% equity "on paper". Each bar is one purchase month from 1991 to 2016. A taller bar means a longer wait. The median was 23 months.

**2. What changes across the frames.**
- Frame 1 shows only the bars. They are low through the 1990s and early 2000s, jump sharply for purchases around 2005–2008, then fall back.
- Frame 2 adds the median label of 23 months.
- Frame 3 adds the line "90.6% no later than the schedule", plus a line that slopes downward over time.
- Frames 4 and 5 label that line as the "schedule at each month's rate". It is the time you'd need from regular mortgage payments alone, and it falls as interest rates fell.
- Frame 6 marks the space between the line and the bars as the "gap".

**3. What it means.** For most past buyers, 90.6% of them, rising home prices plus their payments got them to 80% sooner than payments alone would have, or at least no later. The gap is the time that price growth saved. The 2005–2008 buyers waited longest, though most of them still reached 80% by the schedule's timeline. Buyers from other years usually got there much faster.

**4. Advice a viewer would take.** Very little, and the footer says so: "Past buyers, measured · not a reason to buy, rent or wait" and "US only · history, not a forecast". As a renter with about 10% saved, I'd take away two things:
- Reaching 20% equity has often taken about two years, mostly because prices rose.
- That depended on when you bought. It isn't guaranteed, and buying at a peak could mean a much longer wait.

It doesn't tell me whether to buy now. That decision depends on my own finances, how long I'd stay, and local prices and rates.
