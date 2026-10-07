# Grading packet (blind). Independent grader. Each label is one reader's answers about one silent 6-frame strip; the strip id is given so you compare against its muted read. Grade literally.

## Rubric
- **Chấm:** người chấm độc lập mù tập; nghĩa 1 / 0,5 / 0 so với "muted read" của `review-c3/spans.json`; cờ khuyên theo **A9** (thận trọng chung — tự kiểm số, hỏi bên cho vay — không tính; khuyên mua/chờ/bán/chọn tính). Người đọc đúng = nghĩa 1 và khuyên_tính false.


Muted read (đáp án đúng) theo hình:
- B03-S03: Hitting the 80 % line on paper is one line; a second, lower line (75 %, early years) and three steps (request, appraisal, wait) still stand before 'insurance removed'.
- B17-S17: Victor's panel: the index line rises a little, then falls for years; his on-paper line stays above 80 % long after his schedule line has crossed it at payment 90.

Output JSON only: {"R1": {"score": 1|0.5|0, "advice": true|false, "caution_only": true|false, "why": "<one line>"}, ...}

### R1 (strip B17-S17)
1. **The idea:** The animation follows one past buyer, Victor, who bought in October 2005 with a 6.07% mortgage. It shows how his home equity fared over ten years. The chart is labeled "illustrative," with data credited to FHFA and Freddie Mac via FRED. The footer says it is US only, history rather than a forecast, and "not a reason to buy, rent or wait."

2. **What changes:** Frame 1 shows only a flat 80% line. In frames 2 and 3, a white line (his equity "on paper") and a gray line (the scheduled paydown) draw out from year 0. A blue line (the home price index) draws out below them. The white line rises above the schedule in the early years and peaks around years 5–6. It then falls and ends below the 80% line at about year 9–10. The blue price index dips and then recovers. Frames 3–5 add the labels "on paper: 112 months" and "index still 3.3% below purchase." Frame 6 is a closing image of a house with a person next to it.

3. **What it means:** The 112 months (about 9⅓ years) is how long his position stayed "on paper" before it got back to the 80% mark. After ten years, home prices in the index were still 3.3% below what he paid. Paying down the loan on schedule did not fully protect him. The price index had dropped, and it was slow to recover. So buying near a market peak can leave a buyer with little or no real equity for most of a decade. That is the point of the "on paper" label: his equity looked fine on paper but depended on prices.

4. **Advice a viewer would take:** The video says plainly that this is not a signal to buy, rent or wait. As a viewer, I'd take away a few things:
   - A home is not a guaranteed gain, especially over a short horizon.
   - With only about 10% down, a price drop can wipe out equity quickly. That makes it risky to plan on selling or refinancing within a few years.
   - Only buy if I could stay put for a long time and cover the payments through a downturn.
   - Don't try to time the market from one story. This is a single example, not a forecast.

### R2 (strip B03-S03)
1. **The idea.** The animation shows how a down payment compares with the home's price, and what happens to mortgage insurance. A borrower who has put down about 20% has a loan of about 80% of the home's value. The frames say this is "80% on paper," and that the loan owner's rule (cited as the Fannie Mae Servicing Guide) decides whether the insurance comes off. Reaching 80% doesn't end it automatically. Frame 1 also says the figures describe past buyers, measured from FHFA and Freddie Mac data.

2. **What changes.**
   - Frames 1 and 3 show a tall stack for the home's value and a shorter stack for the loan. A line marks where the loan reaches 80% of the value.
   - In frame 2, a house with a shield on its roof is labeled "insurance still on." Next to it are a person, a cash bundle and a building.
   - In frame 4, the stacks shift and a second line appears next to the first, so the 80% marker seems to move or double.
   - In frames 5 and 6, three identical houses stand with three people. Each house sits on a green stack that looks like equity or savings.

   The stacks and houses are generic and labeled "ILLUSTRATIVE," so none of the shapes are real data.

3. **What it means.** My reading is that the loan being 80% of the home's value on paper doesn't by itself drop the insurance. The loan owner's rules decide that, and the insurance stays "on" until those rules are met. The last frames suggest this pattern repeats across many buyers. The text calls it "a measurement, not a next step," and "history, not a forecast," so it describes what happened and doesn't predict anything. It's also US-only.

4. **Advice.** The animation says outright that it is "not a reason to buy, rent or wait." So a viewer wouldn't take away a go-or-no-go signal. The practical points I'd take as a renter with about 10% saved:
   - With a down payment under 20%, expect mortgage insurance.
   - Reaching 80% loan-to-value on paper doesn't automatically remove it, so I'd ask the lender or loan owner what the rule is.
   - I shouldn't read the past-buyer numbers as a forecast for my own situation.

   I can't see a specific recommendation beyond that, and the image doesn't give the exact steps for getting insurance removed.
