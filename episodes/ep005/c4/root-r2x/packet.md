# Grading packet (blind). Independent grader. Each label is one reader's answers about one silent 6-frame strip; the strip id is given so you compare against its muted read. Grade literally.

## Rubric
- **Chấm:** người chấm độc lập mù tập; nghĩa 1 / 0,5 / 0 so với "muted read" của `review-c3/spans.json`; cờ khuyên theo **A9** (thận trọng chung — tự kiểm số, hỏi bên cho vay — không tính; khuyên mua/chờ/bán/chọn tính). Người đọc đúng = nghĩa 1 và khuyên_tính false.


Muted read (đáp án đúng) theo hình:
- B17-S17: Victor's panel: the index line rises a little, then falls for years; his on-paper line stays above 80 % long after his schedule line has crossed it at payment 90.

Output JSON only: {"R1": {"score": 1|0.5|0, "advice": true|false, "caution_only": true|false, "why": "<one line>"}, ...}

### R1 (strip B17-S17)
**1. The idea.** The animation follows one past buyer, Victor, who bought in October 2005 with a 6.07% mortgage. It shows what happened to the loan against the home's value over the next ten years. The data comes from FHFA and Freddie Mac via FRED. The "illustrative" tag and the footer say this is measured history, not a forecast.

**2. What changes across the frames.**
- Frame 1 is an empty chart with only a flat 80% line.
- In frame 2 the white "on paper" line and the gray "schedule" line start near each other. The blue price index starts to dip.
- By frame 3 the price index sinks well below its starting level, bottoming around year 6. The white line rises far above the schedule line as the home's value falls, peaking around years 3 to 4. It then comes back down.
- In frames 4 and 5 the picture is complete. At about 112 months the white line drops below the 80% line, but the label says the price index is still 3.3% below the purchase price.
- Frame 6 is a house with a question mark.

**3. What it means.** My reading is that the white line is the loan as a share of the home's value, and 80% is the usual threshold for having a solid equity cushion. When prices fell, Victor's loan looked much larger relative to the home than the payment schedule alone would suggest. He spent years above the 80% line even though he paid on time. He got back under it after about 9 years, mostly through paying down the loan, because prices had not fully recovered. So a buyer can be "underwater" or thinly cushioned for a long time, and home prices don't rebound on any schedule.

**4. What a viewer would take from it.** The footer says this is "not a reason to buy, rent or wait," so it isn't telling anyone to act. The practical takeaways, as I read them:
- Plan to stay a long time, since equity can take close to a decade to rebuild after a bad entry point.
- Don't count on price gains. Principal paydown did much of the work here.
- Keep a cushion, meaning a bigger down payment, emergency savings, and a payment you can afford, so a price dip doesn't force a sale.

As a renter with about 10% saved, I'd see this as a reminder that a 10% down payment leaves less room than Victor's 20% if prices drop. It's one example, not a prediction.
