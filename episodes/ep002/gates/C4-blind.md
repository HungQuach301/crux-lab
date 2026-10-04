# C4 — Kiểm mù tắt tiếng + che chữ/số trên animatic (01/10/2026)

Ý đồ: `gates/C4-intent.md` (commit faac2e9, không đổi). Mẫu: `animatic/strips/KEY-n-masked.png` (commit 4f8bab5) + đối chứng Tập 1 `review-c3/control/C-Sxx-strip-masked.png`. Khoá `review-c4/blind-key.json` (commit ebb1315, trước khi chạy). 42 người đọc mới (sonnet), mỗi người một mẫu, thứ tự trộn, câu hỏi cố định.

## Kết quả
| Nhịp | Tập 2 (/3) | Đối chứng Tập 1 (/3) |
|---|---|---|
| KEY-1 | 1.5 | 1.5 |
| KEY-2 | 1.5 | 2 |
| KEY-3 | 3 | 0 |
| KEY-4 | 2.5 | 3 |
| KEY-5 | 3 | 1.5 |
| KEY-6 | 3 | 0 |
| KEY-7 | 1 | 2 |
| **Trung bình** | **15.5/21 = 0.738** | **10/21 = 0.476** |

**Ngưỡng 0,70 → Tập 2 ĐẠT (0.738).** Không có KEY-7: 14.5/18 = 0.806. Đối chứng Tập 1: 0.476; bộ đo phân biệt được (Tập 2 cao hơn rõ).

Nhịp dưới 2/3 điểm: KEY-1 (1,5: người đọc thấy một người, hai lựa chọn, một thứ phẳng, một thứ lên xuống; khoảng chênh xanh bị đọc thành "lời ở trên vạch"), KEY-2 (1,5; như các vòng trước), KEY-7 (1).

## Nguyên văn và điểm

**Tập 2 · KEY-1 · b8e9dd45** · điểm 0.5 — hai lựa chọn của một người ✓; đọc khoảng chênh xanh là "lời ở trên vạch", không thấy "bắt đầu thấp hơn"

A person holds up two documents (likely a loan/contract or two options), and a line appears across them. A growing line chart then starts on the right document: it begins small and positive (green, above the baseline), then climbs and swings up and down, dipping back to or below the baseline. This looks like a balance or investment value changing over time. The comparison with the baseline suggests that early gains can be erased by later volatility, or that a balance such as a loan that grows may end up no better than where it started.

**Tập 2 · KEY-1 · 1cadac28** · điểm 0.5 — một người, hai tài liệu, một thứ phẳng, một thứ lên xuống ✓; "bắt đầu thấp hơn" ✗

A person holds up two documents (likely two loan or account statements) over a shared baseline. Over time, a green-shaded gap opens on the right document and a line starts at the baseline, then swings up and down as it grows. I read this as one balance or value (probably the loan) drifting and fluctuating away from its starting point while the other stays flat, so the amount owed or gained diverges from the original over time. I'm only moderately sure, because all the text is covered.

**Tập 2 · KEY-1 · d78a7de4** · điểm 0.5 — như trên: khoảng chênh đọc thành "lời ban đầu ở trên vạch"

The section shows a person holding up two documents (likely two loan or investment options) on either side of a shared baseline, and then a line chart growing out of the right-hand document over time: it starts as a small green gain above the baseline, then climbs and becomes volatile, swinging up and then falling back below the baseline. It suggests that one option (the right-hand one) starts out looking better than the baseline, but its value fluctuates and can end up worse or roughly equal, so an early advantage is not guaranteed over the long run.

**Tập 2 · KEY-2 · 2adef489** · điểm 0.5 — thấy khoảng cách lớn → 0 → đảo; đọc là một số dư đổi dấu

A bar hanging below a zero baseline (teal, like a negative balance or debt) shrinks step by step over the frames until it reaches zero in frame 5. In frame 6 it flips above the line in orange. My best reading is that a loan balance is paid down to nothing, and what follows is a positive balance, meaning net worth turns from negative to positive once the debt is gone. The text is hidden, so this is an interpretation and I can't be certain.

**Tập 2 · KEY-2 · 875098b9** · điểm 0.5 — như trên

It looks like a running balance relative to a zero line: a green block below the line (a debt or negative balance) starts large, shrinks and wobbles a bit (frames 1-4), reaches zero in frame 5, and then turns into a small yellow/orange block above the line in frame 6. My best guess is that it shows a loan being paid down to zero and then flipping to a positive position (savings or net worth), though the hidden text means I can't be sure of the exact meaning.

**Tập 2 · KEY-2 · 90f845e3** · điểm 0.5 — như trên (có "figure holds up two documents")

A figure holds up two documents (probably a statement and a loan or account record) with a horizontal baseline across them. A green block (a positive amount) sits below the line and shrinks from frame 1 to 4, then disappears at 5. In frame 6 an amber block appears above the line. This looks like a balance being paid down to zero and then flipping into a different state, which could be a surplus, or a warning about growing debt. The most likely reading is that a loan balance is shrinking and then changes sign, but the covered text means I can't be sure.

**Tập 2 · KEY-3 · 68da0e36** · điểm 1 — đa số ổn, kết quả tệ dồn quanh đỉnh/giai đoạn đầu

The section shows a time-series line chart (a sharp peak, then a decline and partial recovery) with a grid of cells underneath that starts fully filled (frames 1-2) and then turns mostly dark with red cells clustered around the peak and a few later ones (frames 3-6), then fades. My read: the grid is a set of individual items (such as loans or borrowers), and the red ones are those that went bad or got hurt when the peak turned into a downturn. The idea is that most are fine, but trouble concentrates around the peak and its aftermath, so risk from borrowing is concentrated in specific periods rather than spread evenly.

**Tập 2 · KEY-3 · 358f6997** · điểm 1 — chỉ vài giai đoạn tệ, quanh đỉnh; còn lại ổn; tuỳ lúc vay

The section shows a time series (a blue line that rises to a sharp peak and then declines, probably something like interest rates or a market/economic indicator) over a row of grid cells, one cell per period. As the frames advance, the cells go from all lit to mostly dark, with red marking a small set of periods clustered around and before the peak. It seems to mean that only a few specific stretches of that history were bad or "unfavorable", mostly around the peak, and the rest are fine. For a borrower, that suggests the outcome depends heavily on when you borrow or repay, and most periods are not the risky ones.

**Tập 2 · KEY-3 · 47c47201** · điểm 1 — thiệt hại dồn vào vài giai đoạn quanh đỉnh

The section shows a time-series line chart (a large rise to a sharp peak, then a long decline and a partial recovery) over a row of grid cells, one per period. The cells start fully lit (gray/white) and are then progressively "blacked out" or turned red, with the red clustered around the peak and a few later points, which looks like marking the periods that are bad or at risk. It appears to say that most of the damage or risk is concentrated in a few specific stretches around the peak, and that the rest of the timeline is not affected. I can't tell the exact subject because the text is covered.

**Tập 2 · KEY-4 · 5fadb4a5** · điểm 1 — ở dưới: hũ đầy; ở trên: hũ cạn; cạn → khối đỏ

This section shows a borrower's balance over time: first a small dip below zero (money borrowed, which fills a "tank" of funds), then the balance climbing into a huge gold area above the line as interest accrues, which drains the tank to empty and leaves a red hatched "danger" block (the debt grows far beyond what was borrowed). Frame 6 contrasts this with a larger, flat borrowed amount that never grows. The meaning is that a loan whose interest compounds or capitalizes can balloon well past the amount borrowed, so extra private-loan debt gets much more expensive the longer it goes unpaid.

**Tập 2 · KEY-4 · 268943f2** · điểm 1 — hũ đầy rồi cạn; cạn → cảnh báo đỏ

This section shows a loan balance as a tank: during school (frames 1-3) the borrowed amount sits as a small, slowly growing debt while the tank fills with loan money; then, once payments start, the debt is paid down while the tank drains (frame 4). In frame 5, interest accrues and compounds, so the debt balloons far above the original amount and the tank is empty with a red warning (likely default or being unable to cover costs), whereas in frame 6 the debt stays flat and level beneath the baseline. The idea is that unpaid or deferred interest makes a private loan grow much larger over time than what you originally borrowed.

**Tập 2 · KEY-4 · d825bda1** · điểm 0.5 — ở trên làm hũ cạn, cạn → đỏ; không nói hũ đầy khi ở dưới

This section appears to show how a loan balance grows when it is not paid down: a small initial borrowed amount (green, below the zero line) is followed by interest accruing (orange, rising far above the line) that overwhelms the available money (the tank empties and a red warning appears), meaning that borrowing beyond what you can repay lets interest compound so the debt balloons well past the original amount. The last frame shows a large flat borrowed block with a fuller tank, suggesting the borrowing amount itself is big and takes a long stretch of time to climb out of.

**Tập 2 · KEY-5 · 31e1dce2** · điểm 1 — cửa sổ cố định trượt; nhiều điểm bắt đầu; xếp kết quả

The section shows a long, noisy, upward-trending line (like a stock-market or portfolio value chart) with a highlighted window that slides along it, tracing a fixed-length holding period from different start dates. The final frame stacks the results of many such windows into a histogram-like grid around a big peak, which suggests that outcomes over a fixed horizon vary widely depending on when you start, even though the long-run trend is upward.

**Tập 2 · KEY-5 · 75ac5523** · điểm 1 — như trên; "every possible window", tuỳ lúc bắt đầu

The section shows a long, noisy, generally rising line (likely a market or index value over time) with a fixed-length window sliding from the start toward later periods, and in the last frame the view zooms out to a much longer history with a grid of stacked blocks (one per window) lining up beneath it. The idea seems to be that results over a fixed holding period depend heavily on when you start, so looking at every possible window across history shows the range of outcomes (including bad periods around a peak) rather than a single average; I'm inferring this since all text is hidden.

**Tập 2 · KEY-5 · f666ef06** · điểm 1 — như trên; khối mỗi cửa sổ

This section shows a long, noisy, generally rising time series (like a market or stock-price chart) with a fixed-length window that slides along it, and the stretch inside the window is then compared against a baseline line (one stretch of the window is highlighted). In the last frame the window sits near a low point after a big peak, and a grid of many stacked blocks (one per window or period) appears to tally how often a given outcome happens. The idea seems to be that results depend heavily on which period you start in, so you check many rolling periods of history to see how often returns, or a debt or investment balance, end up above or below a baseline. I'm only moderately sure of this reading because all the text is hidden.

**Tập 2 · KEY-6 · 51a93436** · điểm 1 — đoạn dài ở trên vạch → chồng cao hơn với phần đỏ thêm

A price/balance-style line chart (a rise and fall over time) is compared against a fixed horizontal baseline (the starting level): a marker sweeps left to right along the chart, highlighting the stretch where the line sits at or above that baseline until it ends back near the baseline. In the last frames this is turned into two stacks of bars (a long one, and a taller one with red segments on top), which I read as showing that the total accumulated amount ends up larger than the original, with the red part being extra cost such as accrued interest piling on top of the principal. I'm fairly unsure of the exact meaning because all text is hidden.

**Tập 2 · KEY-6 · 3cf6a2a8** · điểm 1 — lên đỉnh rồi xuống; chồng có phần đỏ thêm, tốn hơn

A line chart of a fluctuating series (it rises, peaks, then falls back to roughly its starting level) is traced out over time, with a highlighted horizontal baseline marking the starting level; at the end, two stacks of bars appear, one taller than the other, with a red segment on top. My reading is that the section shows a balance or value rising and falling over the period and finishing about where it began, so the later comparison shows the stack with the extra red portion costing more in total, such as a loan balance with accumulated interest on top of the original amount. I can't be certain, because all text and numbers are hidden.

**Tập 2 · KEY-6 · caeb336f** · điểm 1 — như trên

The section shows a fluctuating line (like a balance or value over time) that rises and falls around a fixed baseline, with a highlighted marker sweeping from the start to the end of the period. Once the timeline is complete, two stacks of bars appear (the right one taller, with a red top part), suggesting a comparison of totals, such as what you originally borrowed versus what you end up owing or paying once interest/extra costs accumulate over time.

**Tập 2 · KEY-7 · 67a1c333** · điểm 0.5 — thanh xanh ↔ cột đỏ giảm, thanh vàng ↔ cột đỏ tăng (đúng quan hệ), nhưng đọc là trả nợ; không thấy hai nửa khác nhau

Two red "debt" columns (probably the loan principal and its accrued interest or a second loan) are paid down step by step toward zero while a green income/budget bar stays steady above them. In frame 5 the bar turns yellow and both debt columns jump back up to large balances, which looks like a tighter-budget or high-borrowing scenario where debt stays big or grows. The overall message seems to be that the loan balance shrinks only when income comfortably covers the payments, and a big balance squeezes the budget. I'm only moderately confident because all the labels are hidden.

**Tập 2 · KEY-7 · 896e0642** · điểm 0 — nợ tăng do lãi; không có quan hệ khoảng chênh

It looks like a loan balance (red hatched bars) growing over a long period while the borrower isn't paying it down: in frames 1-4 the balance in the first bar is small and the second bar is empty or near-empty, then in frame 5 (with a switch to an amber payment bar) both bars fill up substantially, before frame 6 resets to a tiny balance. The meaning is that interest accrues and compounds on the debt, so what you owe snowballs well beyond the amount originally borrowed unless it is paid down early, which matters for private loans beyond the federal limit.

**Tập 2 · KEY-7 · a490b7f3** · điểm 0.5 — thanh teal ↔ đỏ giảm, cột thứ hai rỗng; thanh vàng ↔ đỏ tăng; nghĩa gán là khoản trả

It looks like a loan being paid down over time. With a steady payment or income (the teal bar), the red debt column shrinks toward zero across frames 1-4 and 6, while the second, empty column stays a goal or empty slot. In frame 5 the bar turns yellow (a smaller or different payment) and both red debt columns swell, which suggests that paying too little lets debt and interest pile up instead of shrinking. I can't be certain, because all the labels are hidden.

**Đối chứng Tập 1 · KEY-1 · 9fe06d5b** · điểm 0.5 — S01: đường xuống dưới mức rồi lên lại; thiếu "đã lỡ"

The section shows a line chart (likely a balance or debt-related value) that first drifts downward below a dotted baseline, and a stack of cash that stays the same size, gets a new bundle added on top, and then grows. In the last frame the line climbs back up above the baseline. This suggests that a balance or position can fall at first and then recover and grow over time, for example loan or investment dynamics where early costs or interest cause a dip before a later gain.

**Đối chứng Tập 1 · KEY-1 · a99cf8a2** · điểm 0.5 — S01: như trên

A line chart (likely a portfolio or balance) falls below a reference line and stays in a shaded "underwater" stretch, then later recovers past that line, while the stack-of-cash scenes show a pile of money that gets topped up with another bundle and grows. It seems to illustrate that a balance or investment can drop and stay below its earlier level for a long time before recovering, and that adding more money during the dip is what helps it come back, so the timing and duration of a drawdown matter as much as the size.

**Đối chứng Tập 1 · KEY-1 · b34d93ff** · điểm 0.5 — S01: như trên

The section shows a line chart (likely a balance or loan amount against a threshold line) that first drops below a reference level, then, alongside a stack of cash that grows as more bills are added on top, later climbs back up past that level. It seems to illustrate a balance or debt changing over time, with money added and compounding so the value first lags and eventually recovers and surpasses where it started.

**Đối chứng Tập 1 · KEY-2 · 25943e36** · điểm 1 — S05: thấp hơn mức trong một cửa sổ dài rồi lên lại (cửa sổ đóng)

A line (likely a rate or price, e.g. interest rates) starts near a baseline, dips well below it for a long stretch, then climbs back above it and spikes at the end. The video highlights that low-period window, marks its lowest point with a green bar, and then contrasts the window with what came after. The idea: rates were unusually low for years but have since risen sharply, so borrowing costs now are much higher than the recent past, and a loan taken (or a rate locked) at the low point would have been far cheaper.

**Đối chứng Tập 1 · KEY-2 · a58cc66a** · điểm 0.5 — S05: đoạn dưới mốc được tô; thiếu "cửa sổ đóng"

The section shows a line chart (such as a rate or price that falls below a reference level and later climbs back above it) with a period highlighted, then a marker placed at the low point, and finally a boxed callout about that period. It seems to illustrate that over a stretch of time the value stayed below its benchmark (for example, rates or returns dipping and then recovering), so timing, such as when you borrow or lock in a rate, makes a big difference. I can't be sure of the exact subject because all the text is hidden.

**Đối chứng Tập 1 · KEY-2 · 9f998c70** · điểm 0.5 — S05: như trên

The section shows a line chart (likely a market or rate series) that dips below a reference level and then climbs back above it, with a highlighted period in which it stays below that level. A green marker is then placed at the low point, and the span is hatched and marked at its end. The idea seems to be that a downturn has a bottom and a recovery time, and that a recovery period can be measured, from the drop to the point where the series gets back to where it started. For a borrower, I read this as the cost or wait of being "underwater" and the time it takes to recover. I can't be sure of that reading, because all the text and numbers are hidden.

**Đối chứng Tập 1 · KEY-3 · 19449aa0** · điểm 0 — S08: đọc thành tiến tới mục tiêu

The section appears to show a journey from a starting point (house icon) toward a goal (flag) along a green progress bar, then shifts to a timeline with a moving green dot approaching a dashed marker, alongside a grid of squares (likely months or payments) that gets filled in or greyed out as time passes. My best guess: it illustrates progress through a repayment or time-based milestone (e.g., how many months or payments remain until a deadline or payoff), though with all text hidden I cannot be certain of the exact meaning.

**Đối chứng Tập 1 · KEY-3 · 6df9eb2a** · điểm 0 — S08: như trên

The section shows a progress bar (a green bar running from a home icon toward a flag/goal) that is reduced to a single dot on a timeline, and then a row of squares (likely months or payments) that are all filled, then greyed out, then filled again. It seems to illustrate progress toward a goal, such as paying off a loan, being tracked over time, with units of time (months) being used up or reset. I can't tell the exact meaning because all text and numbers are hidden.

**Đối chứng Tập 1 · KEY-3 · 06989495** · điểm 0 — S08: như trên

The section appears to show a timeline from a starting point (the house) toward a goal flag, with a green bar that fills and then shrinks to a single dot on a line. That dot sits just short of a dashed marker, next to a grid of blocks that lights up and dims, which seems to show a position or milestone moving toward a target over time, such as a loan balance or payoff progress month by month. I can't tell the exact quantities because the text is hidden.

**Đối chứng Tập 1 · KEY-4 · 206bb54c** · điểm 1 — S10: khối thêm đặt lên trên → nợ nhiều hơn

The section shows a gauge/dial and a progress bar (a fixed-size allowance filled in green) that then reset, followed by a stack of cash and a small box whose top gets covered in red stripes. The tall blocks on the right are also marked with a dashed red overflow, and the timeline ticks turn red. This looks like borrowing past a fixed limit (the federal cap). Once the allowance is used up, extra borrowing and its accruing interest pile up on top as an overflow or cost, shown in red, so the debt grows beyond the original amount over time.

**Đối chứng Tập 1 · KEY-4 · b6228f2d** · điểm 1 — S10: như trên

The section appears to show a loan's cost growing over time: a gauge (likely an interest rate or a clock) and progress bars first show a small share of something, then the gauge resets while a second bar appears. In the 3D scene, a stack of cash (the amount borrowed) sits next to a box that gains a red striped layer (accrued interest) as a timeline advances, and the stack and boxes beside it get taller. This suggests that interest accumulates and is added to the balance, so the amount owed ends up well above what was originally borrowed. I can't be sure of the details because all text and numbers are hidden.

**Đối chứng Tập 1 · KEY-4 · 4134b98b** · điểm 1 — S10: như trên

The section appears to show a loan balance growing over time as interest accrues: a stack of money (the borrowed amount) sits beside a box that gets red-hatched "extra" layers added on top as the timeline advances, and the taller blocks beside them grow or gain dashed outlines. This suggests the debt ends up larger than the amount originally borrowed, because interest is added to it while time passes. The opening gauge and bar-meter frames likely set up a rate or limit, but with the text hidden I can't be sure of the exact figures.

**Đối chứng Tập 1 · KEY-5 · 085320a9** · điểm 0.5 — S19: một khoảng kết quả rộng; thiếu "số của bạn sẽ khác"

The section appears to show a range of possible outcomes (a blue band around a single marked estimate on a line) that stays centered on the same point but widens or shifts as time passes (frame 3 to 5). A house icon and highlighted callouts then link that range to a concrete real-world cost or decision. I read this as a loan or cost projection, where the further out you look, the more uncertain the outcome, so borrowing beyond the federal limit means a bigger and less predictable repayment burden. The text is covered, so this is a best guess.

**Đối chứng Tập 1 · KEY-5 · 0c5ba256** · điểm 0.5 — S19: như trên

The section shows a range along a timeline (a blue band with a marker for the typical or expected point) that is first set up from three differently sized bars and then repeatedly stretches or shifts over time. Once a house icon and highlighted labels appear, it seems to show how an uncertain range of outcomes, such as a loan balance, payment or cost, spreads out or moves, and what that means for a borrower's finances. I can't tell the exact quantities because the text is covered.

**Đối chứng Tập 1 · KEY-5 · add07722** · điểm 0.5 — S19: như trên

The section appears to start by comparing three different amounts (three bars of different heights), then focus on a single range of possible outcomes (a line with a blue band and a marker). In the later frames a home icon and highlighted labels appear below it, suggesting that over time a loan or cost falls within a low-to-high range, with the highlighted items marking specific figures or scenarios. Since all text is hidden, I can only infer this loosely.

**Đối chứng Tập 1 · KEY-6 · 5e856a4e** · điểm 0 — S16: đọc thành lãi kép

Over time, a small pile of cash beside a house grows into a huge stack (frames 1-2), then the view switches to a timeline where a marker moves along and a highlighted span appears (frames 3-4), and a second point plus two houses and paired bars are added for comparison (frames 5-6). This looks like loan interest compounding: the debt balloons the longer it goes unpaid, so a longer repayment period or deferred interest means paying far more than was borrowed, with the bars comparing the borrowed amount and the total cost under two scenarios (my reading, since all text is hidden).

**Đối chứng Tập 1 · KEY-6 · d6d09940** · điểm 0 — S16: như trên

This section appears to show a loan balance growing over time while nothing is being paid: a small stack of cash beside a house piles up into a large stack as a timeline advances (frames 1-2), and a timeline marker then moves out to a later point (frames 3-4). It seems to mean that interest accrues and capitalizes during school or deferment, so the debt is much larger at repayment than the amount originally borrowed, and the final bar comparisons (frames 5-6) likely compare two scenarios, such as the original amount against the larger balance owed. I can't be certain of the details because all text and numbers are hidden.

**Đối chứng Tập 1 · KEY-6 · 82623406** · điểm 0 — S16: như trên

The section shows borrowed money piling up over time: in the first two frames a small stack of cash next to a house grows into a tall stack as the timeline ticks forward, with a red warning marker on the building, which suggests interest accruing on a loan so the debt balloons. The later frames reduce this to a timeline marker (an orange bar/triangle) that moves along a line, then compare it with a green milestone (a home purchase) and bar charts of orange vs. green amounts, which suggests that years of accumulated loan interest can delay or compete with later goals like buying a house.

**Đối chứng Tập 1 · KEY-7 · 52af2a13** · điểm 0.5 — S18: ba thanh theo cỡ nhà; thiếu ngưỡng/vạch

The section starts with a loan document, then compares three bars (a tall amber one, then a green one and a red one that appear in sequence) that sit above house icons of growing size. A dashed outline house and a dashed reference line then appear, which seems to show a balance or cost that grows over time (the red bar is likely a private loan accruing interest) compared with the original amount (the amber bar). In other words, the debt ends up much larger than what was first borrowed, though I can't be certain without the text.

**Đối chứng Tập 1 · KEY-7 · ba62982c** · điểm 0.5 — S18: ba cách vay, đường mốc; thiếu chiều "nhỏ cần nhiều hơn"

The section starts with a loan document, then shows three bars (a tall yellow one, a green one and a red one) that sit above house icons of increasing size. A dotted outline house is added between the green and red bars, and a dashed line later extends from the top of the yellow bar across the chart. My best reading is that the same house is being financed in three ways, with a different cost or balance for each. The yellow bar is the largest, and the green and red bars are much smaller. The dashed line marks the yellow level as the benchmark the others are compared against, so the point is how much more one option costs than the others. I can't tell exactly what the bars measure, such as interest, total repayment or loan balance, because all the text is covered.

**Đối chứng Tập 1 · KEY-7 · 974172da** · điểm 1 — S18: thanh nhỏ dần khi nhà lớn dần + nhà nét đứt "giả định"

The section starts with a loan document, then shows three bars (amber, green, red) paired with house icons of increasing size. A fourth, dashed "ghost" house appears between the green and red ones, and a dashed reference line is drawn across from the top of the amber bar. My reading is that it compares a loan balance or cost at successive stages. The amber bar is the largest, the green is smaller, and the red is smaller still, so the dashed line shows how far the amount has moved from the starting level. This probably means the amount owed or paid changes with the loan's stage or terms, and a missing or hypothetical option (the dashed house) would change the outcome. The numbers are hidden, so I can't be sure whether this is about interest growth, repayment, or comparing scenarios.

## Chấm lại độc lập (lệnh chủ dự án C4, 01/10/2026)

Người chấm: một agent mới, chỉ đọc `review-c4/rescore-packet.json` (42 câu trả lời + 14 rubric gán nhãn R01–R14 xáo trộn, không biết mẫu nào là Tập 2 hay đối chứng; khoá rubric `review-c4/rescore-rubric-key.json` commit 17c1d17 trước khi chấm). Điểm từng lượt: `review-c4/rescore-scores.json`.

| Nhịp | Tập 2 · P chấm | Tập 2 · chấm lại | Đối chứng · P chấm | Đối chứng · chấm lại |
|---|---|---|---|---|
| KEY-1 | 1.5 | 1.5 | 1.5 | 0 |
| KEY-2 | 1.5 | 0 | 2 | 1 |
| KEY-3 | 3 | 1.5 | 0 | 0 |
| KEY-4 | 2.5 | 0.5 | 3 | 0 |
| KEY-5 | 3 | 3 | 1.5 | 0.5 |
| KEY-6 | 3 | 0.5 | 0 | 0 |
| KEY-7 | 1 | 0 | 2 | 0 |
| **Trung bình /21** | **0.738** | **0.333** | 0.476 | 0.071 |

Trùng điểm từng lượt giữa hai người chấm: 15/42. Chấm lại Tập 2 **0.333 < 0,70** (không có KEY-7: 0.389). Theo lệnh: báo chủ dự án quyết, **không sửa ý đồ, không hạ ngưỡng**.
Khác biệt chính: người chấm lại đòi câu trả lời nêu đúng **nghĩa** của rubric (ví dụ KEY-3 phải nói "lãi thả nổi thường vượt mức cố định"; KEY-6 phải nói "lãi cao trong thời gian dài"), còn P chấm cả câu chỉ tả đúng hình (ví dụ "phần đỏ dồn quanh đỉnh"). Thứ tự giữa hai tập giữ nguyên ở cả hai cách chấm: Tập 2 hơn đối chứng (0,738 vs 0,476; 0,333 vs 0,071).
