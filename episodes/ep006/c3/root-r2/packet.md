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
**1. The idea.** The animation shows how inflation wears down a fixed income payment. Ruth is an illustrative retiree whose first check buys 10 crates of goods. The crates stand for what the check can buy. The frames are labelled as US consumer prices (CPI-U), "history, not a forecast".

**2. What changes across the frames.** In frames 1 to 3, Ruth and a row of crates are shown, and the last crate on the right turns dark and drops out. In frames 4 and 5, the scene is redrawn flatter and a label appears: "check: +2% a year". The bracket "first check: 10 crates" marks where she started, and the last crate is still dark. In frame 6, a new label says "today: about 9 in 10 crates (90.4%)". So the check is the same size or slightly larger, but it buys fewer crates.

**3. What it means.** Prices rise over time, so a given dollar amount buys less each year. The check in frame 6 buys about 90% of what the first one did, so roughly 10% of its purchasing power has gone. The image doesn't say how many years that took. The figure is also described as illustrative history for the US only, so it isn't a prediction.

**4. Advice for a viewer like me, at 64 and weighing two annuity payout options.**
- Don't judge an annuity only by the size of the first check. Ask what that check will buy in 10 or 20 years.
- The "+2% a year" label suggests one of the options may have payments that rise each year. That kind of option usually starts with a lower first payment but keeps up better with prices. A flat payment starts higher but loses purchasing power, as the dark crates show.
- I'd compare the two quotes over a long retirement, since I could live 25 or 30 years. I'd also check whether other income, such as Social Security, already adjusts for inflation.
- The image doesn't say which option is better or give the actual quotes. It only shows the cost of ignoring inflation, so I'd need to run the numbers on my own quotes.

### R2 (strip N1-s24-carl)
1. **The idea.** The animation shows inflation eroding the buying power of a fixed income. Carl (an illustrative character) starts in January 1966 with a first check worth 10 crates of goods. His check rises 2% a year, while US consumer prices (CPI-U) rise 6.38% a year, which the animation calls the fastest stretch. A second character, Ruth, appears in the first frame and again in the last.

2. **What changes.** Frames 1–2 introduce Ruth and Carl with a row of crates. Frame 3 adds the price label (6.38% a year). Frame 4 adds the check label (+2% a year) and the first check buying 10 crates. In frame 5, at year 11, the crates start going dark, so the check buys fewer of them. In frame 6, at year 20, only about 4 of the 10 crates are left (43.1%). The caption says he has "less buying power on 20 of 20 anniversaries." A small line chart and a note say Ruth's buying power was "back above in early years." That seems to mean her income, probably one that adjusts, recovered, though the image doesn't spell it out.

3. **What it means.** An income that rises more slowly than prices loses real value every year. Carl's check kept growing in dollars, but it bought about 57% less after 20 years. A fixed or slowly rising payment can look fine at first and still shrink in real terms. The labels "ILLUSTRATIVE," "US only" and "history, not a forecast" mean this is one past example, not a prediction.

4. **Advice a viewer might take.** I'm answering as a 64-year-old comparing two annuity payouts. The takeaway is to look at inflation protection before choosing, not only the starting payment.
   - A payout that is level or rises about 2% a year starts higher but can lose a lot of buying power if inflation runs high.
   - An option that adjusts for inflation starts lower but protects purchasing power.
   - The animation doesn't say which option to pick. It also doesn't say that a bad stretch like 1966–1986 will repeat.
   - I'd compare the two quotes by asking how long I expect to need the income and how much inflation risk I can bear. I'd also ask whether other income, such as Social Security with its cost-of-living adjustments, already covers part of that risk.

### R3 (strip N1-s29-three)
1. **The idea:** Inflation steadily erodes what a fixed income can buy. The animation compares three illustrative retirees, Edna, Ruth and Carl. Each starts with a "same 2% raise" income, and the video measures that income in crates of goods. The setting is US consumer prices (CPI-U), and the video says it is "history, not a forecast." Each retiree is tied to a different starting date: Edna to Jan 1949, Ruth to Aug 2006 and Carl to Jan 1966.

2. **What changes:** In frames 1 and 2, each person has a full row of crates. In frame 2, Ruth's and Carl's rows have started to shrink at the right-hand end. By frame 3, a caption says "crates at year 20 · same 2% raise," and the rows have been cut to different lengths. Edna's row is still nearly full. Ruth's has lost a little. Carl's has lost much more, and the missing crates show as dark empty slots. Frames 4 to 6 add labels. Edna's row reads "10," Ruth's reads "about 9," and Carl's reads "about 4." That means after 20 years Edna can still buy about 10 crates, Ruth about 9, and Carl only about 4.

3. **What it means:** A raise of the same size, 2% a year, does not protect people equally. How well it holds up depends on how much prices actually rose during those 20 years. Edna's period (starting 1949) had mild inflation, so her buying power held up. Ruth's period (starting 2006) had somewhat more inflation, so she lost a little. Carl's period (starting 1966) included the high inflation of the 1970s, so his 2% raises fell far behind prices and his buying power was cut by more than half. The "illustrative" and "history, not a forecast" labels warn that these are past examples. They don't predict what will happen to you.

4. **Advice a viewer would take:** Don't judge a fixed payout only by the dollar amount today. Buying power over 20 or more years is uncertain, and a payout that grows by a set 2% a year can fall badly behind if inflation runs high. For someone choosing between two annuity payouts, the lesson is to look closely at whether and how the income adjusts for inflation. A higher flat payout now may buy much less later. A lower starting payout with real inflation protection may hold its value better. The video doesn't say which option is better, and it doesn't recommend one. It only shows that the outcome depends on the inflation you happen to live through, which nobody can know in advance.

### R4 (strip N1-s07-ruth)
1. **The idea:** Inflation gradually erodes what a fixed income can buy. A character named Ruth, labeled "illustrative", gets a first check that buys 10 crates of goods. The captions say this uses US consumer prices (CPI-U) and is "history, not a forecast."

2. **What changes:** In frames 1–3, the camera pulls in on Ruth and a row of 10 crates, and the last crate turns dark and drops out. Frames 4–5 add the labels "check: +2% a year" and "first check: 10 crates." The last crate is greyed out, which shows that the same check now buys fewer goods. Frame 6 adds "today: about 9 in 10 crates (90.4%)." Her check has grown 2% a year, but prices have grown faster, so it buys about 90% of what it first did.

3. **What it means:** An income that rises by a fixed 2% a year doesn't keep up if inflation runs higher than 2%. The dollar amount grows, but its purchasing power shrinks. In this example, Ruth lost about 10% of her buying power.

4. **Advice for a viewer (and for me at 64):** Look beyond the starting payment when comparing income annuity options. A level payout is usually larger at the start but loses buying power over a retirement that may last 25 to 30 years or more. A payout that rises each year, either by a fixed percentage or by tying it to CPI, starts lower and protects against inflation. A fixed 2% step-up is only a partial hedge, as Ruth's example shows. The video doesn't tell anyone which option to pick. It says the figures are illustrative and not a forecast, so I'd compare the real quotes. I'd look at how long the payments need to last, how much inflation protection I want, and what my other income sources, such as Social Security, already cover.

### R5 (strip N1-s27-edna)
1. **The idea.** The animation shows that the same income annuity can turn out very differently depending on when you retire. It compares two illustrative retirees, Edna, who starts in January 1949, and Carl, who starts in January 1966. Each has a check that grows 2% a year. The animation tests that check against US consumer prices (CPI-U). The footer says "US only · history, not a forecast."

2. **What changes across the frames.**
   - Frame 1 introduces Edna with a row of ten crates (the stack of ten "crates" or "lights" represents her purchasing power).
   - Frames 2 and 3 follow her forward. Her check rises 2% a year, and by year 20 all 10 crates are "still lit." Her check kept up with prices, since 1949 is "the last start month that did."
   - Frame 4 shrinks her timeline to a bar.
   - Frame 5 adds Carl's bar, which starts in 1966 and overlaps the end of Edna's. The caption reads "same years of prices: her last, his first."
   - Frame 6 shows Edna at year 20 with all crates lit, while Carl at year 3 already has his last crates fading out.

3. **What it means.** A fixed 2% annual raise only protects you if inflation stays at or below about 2%. Edna retired in a stretch where it did, so her buying power held up. Carl retired just before the high-inflation years that followed. His crates dim early, which means his check buys less and less. The outcome depends on the inflation that happens to arrive, which you don't control.

4. **Advice a viewer might take.** The animation doesn't give explicit advice. A viewer would probably take away these points:
   - A fixed payout, or one with a small fixed raise, carries inflation risk.
   - The starting date matters a lot.
   - Before choosing between a level payout and an inflation-adjusted one, think about whether a 2% raise would really be enough.

   For me, at 64 and weighing two payout options, that would mean asking how much a lower starting payment with true CPI adjustment would cost compared with a higher fixed or 2% payout. It would also mean not assuming that low inflation will continue. The animation uses history only and says it is not a forecast, so it supports caution rather than a specific choice.

### R6 (strip N1-s24-carl)
**1. The idea.** The animation shows how inflation wears down a fixed income. Carl gets a check that grows only 2% a year while consumer prices rise faster. His check buys fewer and fewer goods over time. The crates stand for what the check buys. The labels say "illustrative" and "US only · history, not a forecast."

**2. What changes across the frames.**
- Frames 1 and 2 introduce two people, Ruth and Carl. Each has a row of crates, which is the buying power of a first check.
- Frame 3 sets Carl in January 1966, with prices rising 6.38% a year, which the frame calls the fastest stretch.
- Frame 4 adds that his check rises only 2% a year. It starts at 10 crates.
- In frame 5, at year 11, the row has started to fade. Several crates are dark, meaning he can no longer afford them.
- In frame 6, at year 20, only about 4 of the 10 crates remain, which is 43.1% of the original buying power. His check bought less than the first check on all 20 anniversaries. A small chart and a note say Ruth's buying power was "back above" her first check in the early years.

**3. What it means.** A check that is the same size or grows slowly can lose a lot of real value over a long retirement, especially if inflation runs high. The check looks steady, but what it buys shrinks. Ruth's note suggests that a payout that rises with prices, or one whose buying power recovers, avoids this. The image doesn't say exactly how Ruth's payout works, so I'm inferring that part.

**4. Advice a viewer would take.** Don't judge a payout only by its first-year amount. For your quote, compare the two options over 20 or more years of inflation:
- A higher starting payment that stays fixed, or rises only a little, will buy much less later in retirement.
- A lower starting payment that is adjusted for inflation costs you income now but protects your buying power later.

The image gives no recommendation and no forecast. The 1966 stretch is a historical example, not a prediction. It's a reason to take inflation seriously when you choose between the two options.

### R7 (strip N1-s27-edna)
**1. The idea.** The animation shows that an income check that rises a fixed 2% a year doesn't always keep up with prices. Whether it does depends on when you retire and what inflation does afterward. The frames use two made-up retirees, Edna and Carl, and US consumer prices (CPI-U). The labels say "illustrative" and "history, not a forecast."

**2. What changes across the frames.**
- Frames 1–3: Edna starts in January 1949 with a check that grows 2% a year. Her row of 10 crates stands for what the check buys. After 20 years all 10 crates are still lit, so her purchasing power held up. The caption says this was "the last start month that did" keep up.
- Frame 4: Edna's 20-year span appears as a bar.
- Frames 5–6: Carl is added, starting in January 1966 with the same +2% a year check. His 20-year bar overlaps the end of Edna's, so the caption says "same years of prices: her last, his first."
- Frame 6: By Carl's year 3, his crates are already dimming, so his check is buying less. Edna's are still all lit at year 20.

**3. What it means.** The same 2% annual raise worked for Edna and failed for Carl. Edna's last years and Carl's first years had the same prices. What differed was where in the inflation cycle each person started. Carl's retirement began just as prices accelerated faster than 2%, so his raises fell behind. How a retirement turns out depends on the sequence of inflation you happen to get, which you can't predict.

**4. Advice a viewer would take (and how it applies to a 64-year-old comparing annuity quotes).**
- A fixed 2% escalator is not the same as protection against inflation. It only works if inflation stays at or below 2%.
- When comparing payout options, check how each one adjusts over time. A level payout, a fixed-step increase and a CPI-linked increase protect you differently. The starting payment is usually lower when there is an inflation adjustment.
- Don't assume the future will resemble a good stretch of the past. The animation is US-only history and illustrative, so it can't tell you which option is right. It only shows the risk of picking a fixed raise and hoping inflation cooperates.

### R8 (strip N1-s29-three)
1. **The idea.** Inflation steadily erodes what a fixed income can buy. Three illustrative retirees each get the same 2% raise. Edna retired in Jan 1949, Ruth in Aug 2006 and Carl in Jan 1966. Each is shown with a row of crates, which stands for what their income buys. The frames use US consumer price history (CPI-U) and are labeled "ILLUSTRATIVE" and "history, not a forecast."

2. **What changes over time.**
   - In frames 1–2, all three rows start out full and equal. By the end of frame 2, Ruth's and Carl's rows have started to shorten.
   - In frame 3, the caption says "crates at year 20 · same 2% raise." Edna's row is still full. Ruth's is slightly shorter. Carl's is clearly shrunken, with dark empty slots.
   - In frames 4–6, the counts are labeled: Edna keeps 10 crates, Ruth about 9 and Carl about 4.

3. **What it means.** The same 2% raise protects a retiree very differently depending on when they retire. After 20 years, Edna's income still buys about all it did at the start. Ruth's buys about 90% of it. Carl's buys less than half, because the high inflation of the late 1960s and 1970s outran his raises. The outcome depends on which inflation era you retire into, and nobody knows that in advance.

4. **What a viewer would take from it.** I'm answering this as a 64-year-old comparing two annuity payout options. I'd read the animation as a caution about a flat payout, because a fixed annuity can lose a lot of purchasing power over 20 or more years. If one of the two options has an inflation adjustment (a COLA) or a built-in annual increase, it deserves serious weight, even though it starts lower. A 2% escalator helps, but Carl's case shows it can still fall short in a bad inflation stretch. The video doesn't say which option to choose. It also isn't a forecast, so I'd compare the actual quotes, including the starting payout, any escalator and the break-even age, and not draw a conclusion from this picture alone.
