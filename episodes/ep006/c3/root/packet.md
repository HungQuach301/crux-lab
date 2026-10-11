# Grading packet (blind). Independent grader. Each label is one reader's answers about one silent 6-frame strip; the strip id is given so you compare against its muted read. Grade literally.

## Rubric
- **Chấm:** người chấm độc lập mù tập; nghĩa 1 / 0,5 / 0 so với "muted read" = câu "ý người xem phải đọc ra" của nhịp chép **nguyên văn** từ `beats.md` (`spans.json`); cờ khuyên theo **A9** (thận trọng chung — tự kiểm số, hỏi công ty bảo hiểm/báo giá — không tính; khuyên chọn khoản đều/khoản tăng/phương án gắn CPI, mua/không mua niên kim — tính). Người đọc đúng = nghĩa 1 và khuyên_tính false.


Muted read (đáp án đúng) theo hình:
- N1-s07-ruth: "Back to the crate row: of 10 crates her first check bought, 9 stay lit today."
- N1-s24-carl: "A second faceless figure over the 1966 tile with his row of 10 crates; a year counter ticks 1 to 20 and the row dims a little at every tick, never brightening, until about 4 are lit; a small inset of Ruth's line dipping and recovering early sits beside it."
- N1-s27-edna: "A third figure over the last `cushion` tile; her crate row ends fully lit. Her 20-year bar and Carl's on one time axis overlap at the end of hers / start of his; the shared years are shaded."
- N1-s29-three: "Three figures side by side, each over a crate row: Edna all lit, Ruth 9 lit, Carl fewer than half; each labelled with a start month only."

Output JSON only: {"R1": {"score": 1|0.5|0, "advice": true|false, "caution_only": true|false, "why": "<one line>"}, ...}

### R1 (strip N1-s07-ruth)
**1. The idea.** The animation shows inflation wearing down a fixed payment. Ruth stands beside a row of crates. The row stands for what her first check could buy, and the label says "first check: 10 crates." The labels say it is US consumer price (CPI-U) history, illustrative, and not a forecast.

**2. What changes.** In frames 1 and 2 the camera looks along the row from an angle. By frames 3 to 5 it has moved to a flat side view, and the last crate in the row has turned dark and faded out. That leaves nine bright crates. In frame 6 a new label appears: "today: about 9 in 10 crates (90.4%)."

**3. What it means.** A check that stays the same in dollars buys less as prices rise. The same check that once bought 10 crates now buys only about 9, or roughly 90% of the original amount. The dark crate is the purchasing power lost to rising prices. The image doesn't say how long this took, so the 90.4% figure shouldn't be read as a rate per year.

**4. What a viewer would take from it.** If you're choosing between two income annuity payouts, such as a higher level payment and a lower payment that rises with inflation, the animation suggests that a level payment loses buying power over time. A payment that adjusts for inflation would keep up better, though it usually starts lower. The image doesn't say which option is better for any one person. It also doesn't show future inflation, and it only covers the US. The practical step is to compare how much each option pays now against what that payment would buy in 10, 20 or 30 years. Because retirement can last decades, you'd want to weigh that against your other income and your health.

### R2 (strip N1-s24-carl)
1. **The idea:** A fixed income payment loses buying power when prices rise. The animation uses Carl, a retiree who starts in January 1966. His first check buys 10 crates of goods, and prices then rise 6.38% a year, which the frames call the fastest stretch of US consumer-price history. The labels say it is illustrative, US only, and history rather than a forecast.

2. **What changes:** The first two frames introduce the figures, Ruth and Carl, with a row of crates. In frames 3 and 4 Carl stands at the start with all 10 crates. By year 11 (frame 5), three of the 10 crates have faded, so the same check buys about 7. By year 20 (frame 6), only about 4 of the 10 crates are left, or 43.1% of the original buying power. Frame 6 also says Carl had less buying power on 20 of 20 anniversaries. A small line chart shows Ruth's path, labelled "back above in early years." That line stays near the "first check" level for a while and then drops below it.

3. **What it means:** The check stays the same in dollars, but each dollar buys less as prices climb. In a bad inflation stretch, a fixed payment can lose more than half its real value over 20 years, and Carl was behind every single year. Ruth's line seems to show a different experience, with buying power holding up early and slipping later. The image doesn't explain why her path differs.

4. **Advice a viewer might take:** Don't judge an income quote only by the size of the first check. Ask what that check will buy 10 or 20 years from now. If one payout option rises with inflation and the other is flat, the flat one may start higher but could lose a lot of real value. At 64, with a possible 20 to 30 years of retirement ahead, that matters. The frames don't say which option is better, and they warn that this is history, not a forecast. The takeaway is to weigh inflation risk against the higher starting payment, not to pick one option automatically.

### R3 (strip N1-s27-edna)
**1. The idea.** The animation shows that the real value of a fixed income payment depends on when you start collecting. It follows two illustrative retirees: Edna, who starts in January 1949, and Carl, who starts in January 1966. Each has 10 "crates" of spending power, and the frames track how many stay lit as US consumer prices (CPI-U) change.

**2. What changes across the frames.**
- Frames 1–3: Edna starts with 10 crates. At year 20, all 10 are still lit, which the caption describes as "kept up: the last start month that did."
- Frames 4–5: Carl is added beside her. The timeline bars show that Edna's last years of prices (around 1969) are the same years as Carl's first (from 1966), and the caption says "her last, his first."
- Frame 6: At year 20, Edna still has all 10 crates. At year 3, Carl's last crate has already started to dim, so his purchasing power is eroding.

**3. What it means.** The same price years hit the two retirees at different points in their retirements. Edna's income kept up with prices over her whole 20 years. Carl started just before a stretch of rising prices, so his fixed payment began losing buying power almost at once. Whether a fixed payment holds its value depends on the inflation that follows your start date, which you can't know in advance. The labels say "ILLUSTRATIVE" and "US only · history, not a forecast," so this is a historical example and not a prediction.

**4. Advice a viewer might take.** The image doesn't state a recommendation, but the implication is clear:
- A level, non-inflation-adjusted annuity payout can lose real purchasing power. Edna's outcome was the exception that the video calls the last start month that kept up.
- For your quote, the takeaway is to compare the two payout options with inflation in mind. A payout that rises with inflation usually starts lower but protects buying power. A level payout starts higher but is exposed to the risk Carl faced.
- Don't assume that past stretches where prices stayed tame will repeat. The animation is a caution, not a forecast, so test the choice against your own expected lifespan and other income sources.

### R4 (strip N1-s24-carl)
1. **The idea.** The animation shows inflation eroding a fixed income. A retiree's first payment buys 10 "crates" of goods. The example is an illustrative retiree, Carl, who starts in January 1966, a period of fast US price growth. A second illustrative retiree, Ruth, appears as a comparison.

2. **What changes.** Frames 1 and 2 introduce Ruth and Carl, each standing at the start of a row of 10 crates. In frame 3 the camera moves overhead and a caption says prices rose 6.38% a year, "the fastest stretch." In frame 5, at year 11, the crates start to fade from the right, and only about 7 are still bright. By frame 6, at year 20, only about 4 of the 10 crates remain bright. The caption says "about 4 of 10 crates (43.1%)." It also says Carl had less buying power on 20 of 20 anniversaries. A small line chart in the corner shows Ruth's line. It drifts around the "first check" level and then falls, and the label says she is "back above in early years."

3. **What it means.** A payment that stays the same in dollars buys less each year as prices rise. In this historical stretch, Carl's check bought less than his first check every year for 20 years. By year 20 it bought less than half as much. The "history, not a forecast" and "US only" labels say this is a past example. It does not predict what will happen to you.

4. **Advice for a 64-year-old.** The animation doesn't tell the viewer what to buy. The implied takeaway is to look at whether the annuity's payments adjust for inflation. A level payout starts higher but loses buying power over time. A payout that rises with inflation starts lower but keeps its value. Someone about to retire should compare the two options with that in mind and think about how long they might live. A 64-year-old could easily need income for 25 to 30 years. They should also keep in mind that this was a worst-case-style stretch, not a typical one. Inflation has been milder in other periods, so the real loss would likely be smaller in those.

### R5 (strip N1-s07-ruth)
1. **The idea.** The animation shows inflation eroding the buying power of a fixed income. A figure named Ruth stands beside a row of crates. The first check buys 10 crates, and the label says "US consumer prices (CPI-U)". Everything is marked "ILLUSTRATIVE" and "US only · history, not a forecast".

2. **What changes.** In frames 1 and 2 the row of crates is drawn in perspective and looks long. By frame 3 the camera has moved to a flat side view, and the last crate on the right has turned dark grey. In frames 4 and 5 the row is shown as 10 crates under the label "first check: 10 crates", with the final one dark. Frame 6 adds a second bracket and the caption "today: about 9 in 10 crates (90.4%)". Nine crates stay white and one is greyed out.

3. **What it means.** Ruth's check is a fixed dollar amount, and it bought 10 crates' worth of goods when she first received it. After prices rise, the same check buys only about 90.4% as much, roughly 9 crates. The dark crate is the buying power lost to inflation. The "today" label implies this is measured against US history, so the loss is a past figure and not a prediction.

4. **Advice a viewer would take.** A payout that stays the same each month loses real purchasing power over time. For you, at 64 and looking at an annuity quote with two payout options, the point is to compare a level payout with one that adjusts for inflation, such as a cost-of-living adjustment. The image doesn't recommend either option. It also doesn't show that the loss will be 10% for you, because it is only an illustration and not a forecast. It also doesn't show the trade-off. Inflation-adjusted annuities usually start with a lower first payment, so you would need to weigh that against the loss of buying power. The image also doesn't say over what period the 9.6% loss happened.

### R6 (strip N1-s29-three)
1. **The idea.** The animation shows how inflation erodes the buying power of a fixed income over time. Three illustrative retirees (Edna, Ruth and Carl) each get the same 2% annual raise. Each starts retirement in a different year (Jan 1949, Aug 2006 and Jan 1966). The label says "US only · history, not a forecast", so it uses real US consumer price (CPI-U) history and doesn't predict the future.

2. **What changes.** In frames 1–2, each person stands at the start of a row of crates, which stand for what their income buys. By frame 3 the rows are marked "crates at year 20 · same 2% raise." Edna's row stays full, Ruth's loses about one crate, and Carl's loses about half. Frames 4–6 add the totals: Edna still has 10 crates, Ruth about 9 and Carl about 4.

3. **What it means.** A 2% raise is not enough to keep your lifestyle if prices rise faster than that. Edna retired in 1949, and her 2% raises kept pace with prices over her 20 years. Ruth retired in 2006, and her raises nearly kept pace. Carl retired in 1966, just before the high inflation of the late 1960s and 1970s, and by year 20 his income bought less than half of what it did at the start. The result depends heavily on which decade you retire into, and you can't know that in advance.

4. **Advice a viewer might take.** As someone about to retire and weighing two annuity payout options, I'd take away these points:
   - Be wary of a fixed payment, or one with a small fixed escalator. Inflation can cut its real value sharply, and the animation shows the worst case (Carl) losing more than half.
   - When comparing the two quotes, check whether either one adjusts for inflation, such as a COLA or CPI-linked option. Compare that against the lower starting payment it usually comes with.
   - Don't count on a fixed 2% raise being enough.
   - The animation doesn't say which option is better and doesn't forecast inflation. It is a caution about inflation risk, not a recommendation to buy or avoid any product. I'd weigh it alongside my other income (such as Social Security, which has inflation adjustments), my health and my life expectancy, and I'd consider talking to a fee-only adviser.

### R7 (strip N1-s29-three)
**1. The idea.** The animation shows that a payment rising 2% a year can keep up with prices in some eras and fall far behind in others. Three illustrative retirees, Edna, Ruth and Carl, each start a 20-year retirement in a different period of US history: Edna in Jan 1949, Ruth in Aug 2006 and Carl in Jan 1966. Each has a row of crates standing for what their income can buy. The caption says "same 2% raise" for all three. The labels say US consumer prices (CPI-U), "illustrative", and "history, not a forecast".

**2. What changes.** In frames 1 and 2, the three rows of crates appear and start to run. By frame 3, the caption reads "crates at year 20 · same 2% raise". Edna's row is still full. Ruth's row has lost a little, with one dark slot at the end. Carl's row has lost more than half, with most slots dark. Frames 4 to 6 add the totals: Edna 10, Ruth about 9, Carl about 4. Frames 5 and 6 repeat those numbers.

**3. What it means.** Each person got the same 2% annual raise, but prices rose at different speeds in their different 20-year windows. In Edna's window, 2% roughly matched inflation, so she kept her full buying power. Ruth's window was slightly worse, so she kept about nine-tenths. Carl's window had much faster price increases, so by year 20 his income bought only about four crates' worth. A fixed raise doesn't protect you if inflation turns out higher than the raise. Starting date matters a great deal.

**4. What a viewer would take away.** As someone about to retire and weighing two payout options, I'd take these points from it:
- Don't judge an income stream by its dollar amount alone. What it can buy in 10 to 20 years is what counts.
- A payout that rises by a flat 2% is not the same as one that tracks inflation. It might do fine, as for Edna, or badly, as for Carl, and you can't know in advance.
- If one option is level and the other has a built-in raise or an inflation adjustment, compare what each would buy under both mild and high inflation. Don't compare only the first-year payment.
- The animation doesn't tell me which option to pick. It uses only US history, and it says it isn't a forecast. It is a warning about inflation risk, not a recommendation of one product.

### R8 (strip N1-s27-edna)
**1. The idea.** The animation shows that a fixed income's buying power depends on when you start. Each figure has a row of 10 crates standing for the purchasing power of a steady payment. Edna starts in Jan 1949 and Carl starts in Jan 1966. Both are measured against US consumer prices (CPI-U).

**2. What changes across the frames.**
- Frames 1–3 follow Edna. Her row of crates stays fully lit through year 20, and the caption reads "kept up: the last start month that did."
- Frame 4 resets to Edna alone.
- Frame 5 sets Edna and Carl side by side. The bars show that Carl's first years of prices overlap Edna's last years.
- In frame 6, Edna still has "all 10 crates still lit" at year 20. By only year 3, Carl's last crate is already fading.

**3. What it means.** The same flat payment can keep its buying power or lose it, depending on the inflation that follows the start date. Edna's 20 years held up. Carl's payment began losing value within about 3 years. The "ILLUSTRATIVE" tags and the "US only · history, not a forecast" note say these are historical examples, not predictions.

**4. Advice a viewer would take.** Inflation risk is real for a payout that stays the same. Before locking in an annuity, a viewer would want to weigh a level payout, which is bigger at first but can erode, against an inflation-adjusted payout, which starts lower but keeps pace. The animation doesn't say which to choose and doesn't predict future inflation. For someone retiring at 64, it points to considering how long the income must last and whether it could lose buying power along the way.
