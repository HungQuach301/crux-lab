# C4 gốc — Kiểm mù tắt tiếng, giữ chữ/số (01/10/2026)

Ý đồ: `gates/C4-orig-intent.md` (commit 6080561, trước khi chạy). Mẫu: `animatic/strips/KEY-n.png` (eccaae6) + đối chứng tham khảo Tập 1. Khoá mẫu: `review-c4/orig-blind-key.json`. Người chấm: agent độc lập, mù tập; gói chấm `review-c4/orig-rescore-packet.json`; khoá rubric `review-c4/orig-rescore-rubric-key.json` (commit e6b748e, trước khi chấm). Điểm từng lượt: `review-c4/orig-rescore-scores.json`. P không chấm.

## Kết quả (nhịp đọc đúng khi tổng 3 người đọc ≥ 2)
| Nhịp | Tập 2 (/3) | Đọc đúng? | Đối chứng Tập 1 (/1) |
|---|---|---|---|
| KEY-1 | 3 | ✓ | 1 |
| KEY-2 | 1.5 | ✗ | 1 |
| KEY-3 | 3 | ✓ | 1 |
| KEY-4 | 3 | ✓ | 0.5 |
| KEY-5 | 0.5 | ✗ | 1 |
| KEY-6 | 0.5 | ✗ | 1 |
| KEY-7 | 0.5 | ✗ | 1 |

**Nhịp đọc đúng: 3/7 = 43%. Ngưỡng ≥ 80% (≥ 6/7) → TRƯỢT.**

Câu trả lời tự rút ra lời khuyên (người chấm đánh dấu): 6db1ea03 (Tập 2 KEY-7), 458f16ec (Tập 2 KEY-4), 1fbea1f5 (đối chứng), 6be16c08 (đối chứng).

## Nguyên văn và điểm

**Tập 2 · KEY-1 · 64490a85** · điểm 1 — Fixed vs variable loans; variable starts lower then wanders.

This section compares a 9% fixed-rate private loan (a flat line that never changes) with a 7.5% variable-rate loan whose rate starts lower (the green area below the line, meaning savings) but then wanders up and down over time, eventually rising above the fixed line and spiking well past 9%. It means a variable loan may look cheaper at first, but its rate is unpredictable and can end up costing more than the fixed rate. The frames are labeled "illustrative", so this shows the risk, not actual rates.

**Tập 2 · KEY-1 · dc460289** · điểm 1 — Fixed vs variable offers; variable starts lower then fluctuates.

The section compares two loan offers: a 9% fixed rate (a flat, unchanging line) versus a 7.5% variable rate (a line that starts below the fixed line, then drifts upward and swings sharply, ending above the fixed line). It shows that a variable rate may look cheaper at first, but it can rise and fluctuate over time, so you might end up paying more than with the predictable fixed rate (the chart is labeled "illustrative").

**Tập 2 · KEY-1 · 0c0a2911** · điểm 1 — Two offers fixed vs variable; variable starts lower then swings.

The section compares two loan offers: a 9% fixed rate (a flat line that never changes) versus a 7.5% variable rate that starts lower, then drifts up and swings unpredictably over time, eventually rising above the fixed line. It means a variable-rate private loan looks cheaper at first, but its cost can climb past a fixed rate later, so you take on rate risk (the chart is labeled "illustrative").

**Tập 2 · KEY-2 · 1974923d** · điểm 0.5 — Gap range to negative, but as drift over time, not starting gap.

This illustrative section compares a 9% fixed-rate loan with a variable-rate loan: the variable rate starts well below the fixed line, then its advantage shrinks to about 1.5 points, vanishes, and finally rises above the 9% fixed rate (orange bar). It means a variable-rate private loan may look cheaper at first, but its rate can climb over time and end up costing more than a fixed rate, so you carry the risk.

**Tập 2 · KEY-2 · caf0a5a3** · điểm 0.5 — Gap range to zero/negative, but as drift over time, not starting gap.

This illustrative section compares a 9% fixed-rate loan with a variable-rate loan: the variable rate starts below the fixed rate, the gap shrinks (the labeled "1.5 points" gap, down to zero), and then the variable rate rises above the fixed rate (shown in orange). It means a variable-rate private loan can look cheaper at first but can end up costing more than a fixed rate if rates rise, so its savings are not guaranteed.

**Tập 2 · KEY-2 · 614604a5** · điểm 0.5 — Gap range to negative, but as drift over time, not starting gap.

This section illustrates a fixed 9% loan rate versus a variable rate, where the variable rate starts below the fixed line, then narrows (the gap shrinks to "1.5 points", then to zero), and finally rises above the fixed line (orange). It means a variable-rate private loan can look cheaper at first, but its rate can drift up and end up costing more than the fixed rate, so the savings are not guaranteed.

**Tập 2 · KEY-3 · 3d8cebca** · điểm 1 — Most went above fixed; few ended costing more overall.

This section tests every possible loan start date from 1954 to today against the historical interest-rate curve (peaking around 1981): 76.2% of the variable-rate loans saw their rate go above the fixed rate at some point, but the red squares (loans that actually ended up worse off) shrink to 28.4% and then just 3.5%, clustered around the 1970s-early 1980s rate spike. It means a variable rate often looks risky along the way, yet historically it rarely ended up costing more overall than fixed, apart from loans taken out just before the high-rate era. The frames are labeled "illustrative" and the exact criteria for each percentage aren't stated, so that reading is somewhat uncertain.

**Tập 2 · KEY-3 · 0ad7e801** · điểm 1 — 76.2% went above fixed; only rarely cost more overall.

The section overlays historical interest-rate history (1954 to today, peaking around 1981) with a grid of many past borrowing periods, and it tests each against a fixed rate: red cells mark periods where the variable rate went above the fixed rate, while the rest stayed below. The tally shifts from "76.2% went above the fixed rate" at the start to 28.4% and finally 3.5% as the cells are recolored, which suggests that, historically, a variable-rate loan only rarely ended up costing more than a fixed one, and only in a few high-rate eras such as the late 1970s to early 1980s (labeled "illustrative").

**Tập 2 · KEY-3 · 03a4a4c3** · điểm 1 — 76.2% above fixed; only minority actually cost more.

This section shows a long history of interest rates (1954 to today, peaking around 1981) with a grid of past borrowing periods, and it tests each one to see whether a variable rate ended up above a fixed rate. At first, 76.2% of periods went above the fixed rate, but the count shrinks as the red marks that remain are narrowed to the periods that were actually bad: 28.4%, then 3.5%. The point seems to be that a variable-rate loan usually costs more than a fixed one only in a minority of historical cases, mostly around the high-rate years of the late 1970s and early 1980s. The labels say "illustrative", so the exact figures are only an example.

**Tập 2 · KEY-4 · 458f16ec** · điểm 1 — Below fixed fills buffer, above drains it; loss after buffer gone.

This section shows a fixed 9% loan interest rate compared against a fluctuating benchmark (the variable rate): at first the variable rate dips below 9% and the borrower "saves" (the bucket fills), but then the variable rate climbs far above 9% (frame 5, "not to scale"), the savings are wiped out and a large loss appears, and a deep, long stretch below the fixed line is shown at the end (frame 6). The idea is that a fixed rate gives predictability and protection against big rate spikes, while a variable rate may save a little early on but exposes you to potentially much larger costs later.

**Tập 2 · KEY-4 · 155b234e** · điểm 1 — Below fixed fills savings, above drains; losses after bucket drained.

This section illustrates how a fixed 9% loan rate compares with a fluctuating market or variable rate over time. Early on, the variable rate sits below the 9% line, which fills the "bucket" with savings. Later it spikes far above 9%, the savings are wiped out, and the bucket is drained and overflows into red "not to scale" losses. In the last frame the fixed rate is the baseline and the variable rate has stayed lower for good. The point is that variable-rate private loans can save money for a while but carry a risk of large, uncertain losses if rates rise, whereas a fixed rate is predictable.

**Tập 2 · KEY-4 · 5b26ba74** · điểm 1 — Below fixed fills tank, above drains; loss once tank empty.

It compares a 9% fixed-rate loan with a variable-rate loan: the variable rate starts slightly below 9% (saving money, filling the tank), but over time it can spike far above 9% (the orange peak), wiping out the savings and leaving the tank empty with a large unbounded loss ("not to scale"). The idea is that variable rates offer small possible gains but expose you to big, open-ended downside risk, whereas the fixed rate is predictable.

**Tập 2 · KEY-5 · 8dc04f09** · điểm 0 — Rolling holding-period returns; no loan rerun.

The section slides a fixed 10-year window across a long chart (labeled "illustrative") of a series from January 1954 to today, tracing the result of each 10-year stretch and stacking them up. The idea is that outcomes over any 10-year holding period vary widely depending on the start date, with some stretches roughly flat or negative and others strongly positive, so the time you start matters.

**Tập 2 · KEY-5 · 9ce3af8b** · điểm 0.5 — Results arranged by start date; market returns, not loan rerun.

The section slides a 10-year window across the whole history of a market or investment curve since January 1954, taking every possible 10-year stretch in turn and tracking how each one turned out, with the results stacked up as a grid by start date (1954 to today). It means that outcomes over a fixed 10-year holding period vary a lot depending on when you start, and the chart is illustrative of that range of results.

**Tập 2 · KEY-5 · da20620d** · điểm 0 — Rolling market-return windows; no loan rerun, no start-date arrangement.

The section steps a 10-year window across a long chart (apparently market or investment returns) starting in January 1954, building up every possible 10-year stretch from 1954 to today. The point seems to be that outcomes over a decade vary a lot depending on when you start, so the whole history is being summarized into a set of rolling 10-year periods, labeled "illustrative" (the frame 6 chart looks like a summary of these windows). It's an inference, since there are no axis values and the sound is off.

**Tập 2 · KEY-6 · c451a790** · điểm 0.5 — Variable loan cost 43% more; no worst-case framing.

The section tracks a fluctuating line (apparently an interest rate or index, starting April 1977) as it moves forward in time, with a marker following it until it ends near its starting level, labeled 19.3%. The two stacks at the end show a baseline amount of $26,005 versus a second stack that is 43% larger, meaning that over this period the cost or balance (e.g., a loan with variable rates) ended up 43% higher than the baseline, so rate swings over time can make borrowing substantially more expensive, even when rates end up near where they began. (Illustrative, not real data.)

**Tập 2 · KEY-6 · 41681772** · điểm 0 — No worst case or variable-vs-fixed interest; vague compounding guess.

Starting from April 1977, the section tracks a time series (an illustrative market/rate line) as it plays out over time, stepping through a period where it first rises, peaks, and then falls back to roughly where it started; this produces a 19.3% figure, and then two stacks compare a $26,005 amount against a bigger one that ends up 43% more (the extra shown in red). It seems to mean that the same starting point can lead to a much larger total cost or balance (about 43% more) after the timeline, for example due to compounding or rate changes, though without audio the exact quantity is unclear.

**Tập 2 · KEY-6 · db1f5e90** · điểm 0 — Reads as market returns; no worst case, no variable-vs-fixed interest.

An illustrative market-style line (starting April 1977) is traced forward in time, and its end point sits about 19.3% relative to the start, which then converts into dollar stacks ($26,005) where the later outcome shows 43% more than the other. It seems to show that the starting date and the path of returns over time (including ups and downs) can make one outcome end up substantially larger, about 43% more, than another, even when the endpoints look similar. I am not fully certain which two cases the stacks compare.

**Tập 2 · KEY-7 · 6db1ea03** · điểm 0 — Wrong meaning: more risk after 1981; no head-start link.

This section illustrates how loan interest rates were set before and after 1981: variable-rate loans (green band, adding a 1.5-point margin over a fixed 9% rate) were rarely an issue before 1981, but the red hatched bars show that the share of loan "starts" at rates above the fixed 9% (a few percent early on, then 10.5% and finally 72.9%) grows sharply once variable rates take over from 1981. The meaning is that variable rates can rise above a fixed rate, so borrowers face much more exposure to rate swings, which makes a fixed rate safer for planning a large private loan. (The figures are labeled "illustrative," and I am not fully certain of the exact definition of the percentages.)

**Tập 2 · KEY-7 · 57b60cca** · điểm 0.5 — Contrasts pre-1981 vs from-1981; no bigger-head-start-fewer-losses link.

The section compares a 9% fixed-rate loan with a variable-rate loan that starts about 1.5 points cheaper, and shows how the variable rate moves over time: it stays below 9% for most of the period, so most historical loan starts (especially from 1981 on) come out cheaper than the fixed rate. In a few stretches, mostly before 1981, the variable rate rises above 9% (yellow bar), and the red bars show the share of starts where that happens, such as 8.8%, 4.5% and 10.5%. The point is that a variable rate usually saves money, but it carries the risk that rates spike and leave you paying more than the fixed rate. The 72.9% figure is hard to read, and the figures are labeled "illustrative".

**Tập 2 · KEY-7 · 9dab83d6** · điểm 0 — Garbled meaning; no head-start direction or clean-from-1981 contrast.

This section illustrates how the gap between a 9% fixed rate and a variable rate (a 1.5-point spread) plays out over time. The red bars show the share of loan starts in which the fixed rate would have been cheaper or costlier. Before 1981, fixed beat variable in only a small share of starts (8.8%, then 4.5%, then 10.5%). When the variable rate is shifted above the fixed rate (frame 5), that share jumps to 72.9%, with large red bars both before and from 1981. In short, whether a fixed or variable rate comes out ahead depends heavily on the interest-rate era and the spread, so the variable-rate risk is real and cannot be judged from one period.

**Đối chứng Tập 1 · KEY-1 · 1fbea1f5** · điểm 1 — Bottom 5.98% back above 7%; $459/month missed.

Mortgage rates fell to 5.98% (Feb 2026), about 1.5 points below illustrative borrower Nora's 7.62% and a "window" in which refinancing would have saved her $459 a month. That window then closed: rates climbed back above 7% (7.03% by late September 2026), so the saving vanished. In other words, a rate drop is an opportunity that can disappear if you wait, so act while it's open.

**Đối chứng Tập 1 · KEY-2 · 6be16c08** · điểm 1 — 29 weeks, 1.64 points, window closed, history not forecast.

This section shows the weekly US 30-year mortgage rate over Aug 2025 to about Aug 2026 compared with a hypothetical borrower's 7.62% rate ("Nora", illustrative), and it highlights the stretch when market rates sat at least 1 point below her rate: 29 weeks in 2026, with a peak gap of 1.64 points at the low (5.98%). Over time the market rate fell, bottomed around Feb 2026, then climbed back to about 1 point below Nora's rate by late July 2026, so that refinancing "window" has closed. It is only history for the US, not a forecast, and what comes next is unknown. For a grad student with private loans, the lesson is that a rate you lock in may later be refinanceable at a much lower rate, but the opportunity can come and go, so it's not something to count on.

**Đối chứng Tập 1 · KEY-3 · ebed3e5c** · điểm 1 — 3-year test; rule says no, division says 24 months; both incomplete.

The section asks whether refinancing is worth paying fees for: it shows a timeline where the fees must be paid back (through savings) before she sells or moves, tested over an assumed 3-year stay. It then gives two "quick answers" for Nora, an illustrative example: the 1-point rule of thumb says NO (her rate cut is only 0.59 points, short of the 1-point line), while simple division ($5,124 in fees / $221 monthly savings, about 24 months) says YES, so the break-even is well inside 3 years. The final frames flag that both shortcuts leave something out, such as the uncounted fee bill, so neither is the whole story.

**Đối chứng Tập 1 · KEY-4 · 47f3286b** · điểm 0.5 — Restart clock and month 30 stated; missing $1,133 extra owed.

This section shows that refinancing a mortgage restarts the 30-year clock, so the new loan sends more of each early payment to interest and pays down less principal than the old loan did at payment 35. The $5,124 in loan costs is repaid by the $221 monthly saving only at about month 30, not month 24, so the savings take longer to pay off than they first appear.

**Đối chứng Tập 1 · KEY-5 · 96e4a8b1** · điểm 1 — Wide fee range 3,443-8,270; your own numbers differ.

The section builds up a picture of what 2025 refinance bills actually cost: it starts from a single typical bill (about $3,443), then shows that half of all refinance bills fall between roughly $3,443 and $8,270 (with the example borrower Nora at $5,124), so there is a wide range. It then asks what your own rate, bill and balance would be, and adds that fees can be rolled into the loan and a shorter term changes the math, meaning your own cost depends on your situation and the national numbers are only illustrative.

**Đối chứng Tập 1 · KEY-6 · 69316bc6** · điểm 1 — $1,777 short, 1.12 exceeds 1-point, small loans need bigger cut.

The section shows that a borrower (Walt) who takes a small $115,000 loan and sells after 3 years saves only about $68 a month by refinancing at a lower rate. After 3 years that is still $1,777 short of the $3,667 in loan costs plus the balance still owed, so the rate would have to drop by about 1.12 points, more than the usual 1-point rule of thumb. It means a smaller loan needs a bigger rate cut to pay back refinancing costs (Nora's $375,000 loan needs only 0.5 point), because the bill barely shrinks while the savings shrink a lot.

**Đối chứng Tập 1 · KEY-7 · cd929759** · điểm 1 — Three thresholds by size, 1-point fits none, your-loan slot.

This section shows how much a refinance must cut your interest rate to pay back its roughly $5,000 in fees within 3 years, and that the needed cut shrinks as the loan grows: about 1.12 points for a $115,000 loan, 0.5 point for $375,000, and about a third of a point for $655,000. So the common "1-point rule of thumb" doesn't fit any of these borrowers, and whether refinancing is worth it depends on your own loan size (the "your loan?" placeholder).
