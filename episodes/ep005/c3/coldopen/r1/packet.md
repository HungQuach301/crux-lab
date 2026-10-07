# Grading packet (blind). Independent grader. Each label is one reader's answers about one silent 6-frame strip; the strip id is given so you compare against its muted read. Grade literally.

## Rubric
- **Chấm:** người chấm độc lập mù tập; nghĩa 1 / 0,5 / 0 so với "muted read" của `review-c3/spans.json`; cờ khuyên theo **A9** (thận trọng chung — tự kiểm số, hỏi bên cho vay — không tính; khuyên mua/chờ/bán/chọn tính). Người đọc đúng = nghĩa 1 và khuyên_tính false.


Muted read (đáp án đúng) theo hình:
- E1: Correct meaning (score 1) requires ALL of: on the loan's repayment schedule alone it takes about 8 years for the loan to fall to 80% of the price; when real history is replayed (many purchase months), the typical buyer reaches 80% on paper much sooner; slow cases take longer. Score 0.5: right direction but one element wrong or missing. Score 0: otherwise.
- E2: Correct meaning (score 1) requires BOTH: 'on paper' means the loan compared with the home's value by a (national) price index, reaching 80%; and reaching 80% on paper is NOT the same as the mortgage insurance being removed (it is still on). Score 0.5: only one of the two. Score 0: otherwise.

Output JSON only: {"R1": {"score": 1|0.5|0, "advice": true|false, "caution_only": true|false, "why": "<one line>"}, ...}

### R1 (strip E2)
**1. The idea.** The animation seems to show a first-time buyer with a small down payment. On paper, their loan falls to 80% of the home's value, which is the usual point where mortgage insurance can come off. The frames suggest the insurance may not actually come off at that point. The footer says this is "past buyers, measured," "illustrative," and "history, not a forecast." The source is listed as FHFA and Freddie Mac data via FRED.

**2. What changes across the frames.**
- In frame 1, the loan bar sits a bit below the home-value bar, and the label reads 88%.
- In frames 2 and 3, the loan bar lines up with a line across the home-value bar, and the label changes to "80% on paper." Frame 3 adds that the home value comes "by a national price index."
- Frames 4 to 6 switch to a 3D scene with a house, a person, a stack of cash, and an apartment building. In frame 4, a wireframe landscape that looks like a price history rises in the distance.
- By frame 5 the house sits on a stack of money with a gold piece on the roof.
- Frame 6 labels the scene "insurance still on."

**3. What it means.** As I read it, the loan looks like 80% of the home's value when you use a national price index. Your own lender and your own home might not agree. Mortgage insurance is still being charged in frame 6. The index shows 80%, but the real insurance depends on your actual loan and your home's actual value, and the animation doesn't explain how those are determined. The data is also from past buyers, so it describes what happened and doesn't predict what will.

**4. The advice a viewer might take.** The footer says outright that this is "not a reason to buy, rent or wait," so there is no buy-or-don't-buy advice. A viewer in my position, renting with about 10% saved, would probably take away three things:
- A national index hitting 80% doesn't mean my insurance ends.
- I should ask a lender exactly when and how mortgage insurance can be removed.
- I should count that insurance cost in what I'd really pay.

I'd treat that as a prompt to check the details, not as a rule.

### R2 (strip E1)
1. The animation shows how long it takes a buyer who puts 10% down to get their loan down to 80% of the home's value. The 90% and 80% levels are marked on the chart. The first two frames are an illustrative, scheduled paydown line. The later frames replace it with real US history, with one line for each purchase month from 1991 to 2016. The data source is credited to FHFA and Freddie Mac via FRED.

2. In frames 1 and 2, a single line slopes down from 90% toward 80% as the years pass. By frame 3 it reaches 80% at about 8 years, labeled "schedule ≈ 8 years." In frames 4 and 5, a tangle of historical lines fills in. Many of them drop to 80% much faster than the schedule. Others rise well above 90% before they come back down. In frame 6, two lines are highlighted. The "typical" line gets to 80% in about 2 years, and the slowest case, in blue, takes about 9 years.

3. The loan's share of the home's value depends on more than the payment schedule. It also depends on what happens to the home's price. For most past buyers, price rises pushed the loan share down much faster than the schedule would. For a few buyers, prices fell or stalled. Their loan share went up for years and ended up slower than the schedule. The message is that the schedule is only one possible path. The real range ran from about 2 to 9 years.

4. The video gives no direct advice to buy, rent or wait, and the captions say so. They read "A measurement, not a next step," "Past buyers, measured · not a reason to buy, rent or wait," and "US only · history, not a forecast." A viewer should come away with a few cautions:
   - Don't assume it will take 2 years to build equity just because that was typical.
   - Don't assume the 8-year schedule is guaranteed either.
   - Plan for the slow case, since a 10% down payment can leave you near or above 90% loan share for years if prices don't rise.

I'm reading this as a prospective first-time buyer. For me, the takeaway is that my timeline to reach 80% is uncertain, and I shouldn't treat it as a forecast.

### R3 (strip E2)
1. **The idea:** A buyer who puts about 10% down can look like they've reached 80% loan-to-value "on paper" once home prices rise. That doesn't mean the insurance on the loan goes away. I'm guessing the insurance is mortgage insurance, since the image only says "insurance."

2. **What changes:** In frame 1 the loan bar is about 88% of the home-value bar. In frames 2 and 3 the home-value bar is taller, and the loan sits at an 80% line labeled "80% on paper." Frame 3 adds that home value is measured "by a national price index." Frames 4 to 6 switch to a small scene with a house, a person, cash, an apartment building, and a jagged mesh landscape that looks like a range of price outcomes. By frame 6 the house is stacked on the loan, and the label reads "insurance still on."

3. **What it means:** The 80% figure comes from a national index, not from a appraisal of the buyer's own home. So the buyer may look like they have 20% equity while the lender still counts them as lower than that and keeps the insurance. The captions say this is "illustrative" and based on past buyers (FHFA and Freddie Mac data via FRED). They also say it covers the US only and is history, not a forecast.

4. **Advice a viewer would take:** The image gives no direct advice, and it says outright that it's "not a reason to buy, rent or wait." As a renter with about 10% saved, I'd take away three things:
   - Don't count on national price gains to remove mortgage insurance.
   - Ask a lender how and when the insurance can be dropped.
   - Keep paying for that insurance in my budget until the lender confirms it's gone.

### R4 (strip E1)
1. **Idea:** The animation shows how long it takes a buyer who puts 10% down to get their loan down to 80% of the home's value. Frames 1 and 2 are an illustrative version, where the loan share falls steadily along the payment schedule. Frames 3 to 6 replace that with real US data from FHA, Freddie Mac and FRED. Each line is one purchase month between 1991 and 2016.

2. **What changes:**
   - The first two frames show a single smooth line sliding from 90% toward the 80% line.
   - By frame 3 that line hits 80% at about 8 years, labeled "schedule ≈ 8 years."
   - Frames 4 and 5 fill in hundreds of historical lines, one per purchase month. They spread out, and many rise above 90% before they come down.
   - Frame 6 highlights two of them. The typical buyer got to 80% in about 2 years, and the slowest case took about 9 years.

3. **Meaning:** The loan's share of the home's value doesn't just follow the payment schedule. It also depends on what home prices do. When prices rose, many past buyers reached 80% much sooner than the schedule says, in about 2 years for the typical one. When prices fell, the loan share climbed above 90% for a while, and the slowest buyer took about 9 years, which is longer than the schedule. I'm guessing that 80% matters because it's the usual equity threshold, but the image doesn't say so.

4. **Advice:** The frames say outright that this is "a measurement, not a next step" and "not a reason to buy, rent or wait." They also say it's US-only history, not a forecast. A viewer shouldn't take a buy-or-rent instruction from it. What they could take away is that reaching 20% equity with 10% down is uncertain. It has often been quicker than the schedule, but it can also be slower, so they shouldn't count on a particular timeline.
