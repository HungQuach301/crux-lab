# Hooks — Episode 5 (C2 draft v1, WRITER, 2026-10-06)

Three options for the first ~30 s, each a different hook type from `playbook/packaging.md` §2. Same line format as `script.md` (`Hx.n {role} [emotion] narration <!-- claims: … -->`). Each runs straight into the **shared continuation S03 of `script.md`** ("on paper" defined → "not the same as getting the insurance removed" → the lender's rule with the 75 % bar → three illustrative buyers → "US only, history, not a forecast, won't say whether to buy or wait"). Constraints therefore always come after the hook and the promise, never between the question and the promise (story §1.3).

Timing: 2.4 words/s with numbers read out, no holds (same counter as `check_script.py`, which recomputes M1–M5 for each option with S03 appended). Visuals: H-A = `beats.md` B01–B02; H-B and H-C notes below.

## H-A — "Câu hỏi của người xem" (viewer's question) — **USED in `script.md` (S01–S02)**

HA.1 {hook} You've saved 10 percent of a home's price. <!-- claims: ex_extra_down_for_20 -->
HA.2 {question} [curious] Do you buy now and pay mortgage insurance, or keep renting until you reach 20 percent? <!-- claims: ex_extra_down_for_20 -->
HA.3 {hook} On the payment schedule alone, that's about 8 years of insurance, until the loan falls to 80 percent of the price. <!-- claims: sched80_months_latest, rate_latest -->
HA.4 {promise} We replayed real US prices and rates month by month, so you'll see how long it took on paper, typically and in slow cases. <!-- claims: nB, medianB_months_to80, maxB_months_to80 -->

- Est.: **M1 3.3 s** (hook ends) · **M3 10.0 s** (question) · **M2 28.8 s** (promise) · **M4 9.6 s** (longest define block, S03.3) · **M5 39.6 s** (stake returns: S03.2 "not the same as getting the insurance removed").
- New numbers: 10, 20, 8, 80 (≤ 2 per scene: S01 = 10, 20; S02 = 8, 80). Checker warning: 20 → 8 → 80 fall within ≈ 8 s; the 80 lands at the end of HA.3.
- Visual: V4 figure between two equal cards ("10% down + mortgage insurance" / "20% down"), then V3: loan as % of price drifting to the 80 % line at "~8 years".

## H-B — "Chi phí ẩn" (hidden cost)

HB.1 {hook} 10 percent down has a cost that isn't in the price. <!-- claims: ex_extra_down_for_20 -->
HB.2 {hook} Mortgage insurance, paid month after month, often until the loan falls to 80 percent of the price. <!-- claims: sched80_months_latest -->
HB.3 {question} [curious] So how long would you be paying it? <!-- claims: — -->
HB.4 {promise} On the schedule alone, about 8 years, and we replayed real US prices and rates month by month, so you'll see how long it took on paper. <!-- claims: sched80_months_latest, nB, medianB_months_to80 -->

- Est.: **M1 4.6 s** · **M3 15.0 s** · **M2 26.2 s** · **M4 9.6 s** · **M5 37.1 s** (S03.2).
- New numbers: 10, 80, 8.
- Visual: price tag on a house ($ amount hidden, no PMI amount anywhere); a thin slab slides under the monthly payment block, label "mortgage insurance"; a V3 time strip runs under it to "~8 years".
- Risk (packaging §2): no one "hides" it and it is not called a fee; still, the "cost" has no amount in this episode (no premium source), so the hook promises a duration, not a dollar figure — weaker G-008 stake than H-A.

## H-C — "Cú sốc con số" (number shock)

HC.1 {hook} 23 months, or about 8 years? <!-- claims: medianB_months_to80, sched80_months_latest -->
HC.2 {hook} With 10 percent down, that's the gap in how long a loan took to reach 80 percent of the home's value. <!-- claims: medianB_months_to80, sched80_months_latest, ex_extra_down_for_20 -->
HC.3 {question} So which one looks more like your own plan? <!-- claims: — -->
HC.4 {promise} You'll see where each number comes from: the payment schedule, and a month by month replay of real US prices and rates, on paper. <!-- claims: sched80_months_latest, nB -->

- Est.: **M1 2.5 s** · **M3 15.0 s** · **M2 25.0 s** · **M4 9.6 s** · **M5 35.8 s** (S03.2).
- New numbers: 23, 8, 10, 80 in the first 9 s (density warning); if chosen, S11.1 must recall the 23 in words ("the typical month from the opening"), since the core number may be read in digits only once.
- Visual: black screen, "23 months" and "~8 years" appear side by side as two bars of very different length; the short bar gets the label "on paper" immediately.
- Risk (packaging §2): the 23 months is *on paper* and the median of a national replay, not a removal date; HC.2 says "took to reach 80 percent of the home's value" and S03 follows within 10 s, but a viewer who leaves at 0:05 has seen "23 months" next to "mortgage insurance". Strongest pull, highest overclaim risk.

## WRITER's pick

**H-A.** It is the approved logline L2 in the viewer's own words (story §1.1 "câu hỏi của người xem", C1 readers 2/2 T correct, 0 advice flags), the hook ends at 3.3 s, and it carries the decision (10 % vs 20 %) rather than a number that S03 must immediately qualify (H-C) or a cost the episode cannot price (H-B). REVIEWER judges.

## Draft titles (≤ 60 characters)

1. **10% Down and Mortgage Insurance: How Long Did It Last?** (54) — dossier title (`episode.yaml`).
2. How Long Does PMI Last With 10% Down? We Replayed History (57)
3. Mortgage Insurance at 10% Down: The Schedule vs. History (56)
