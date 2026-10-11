# Hooks — Episode 6 (C2 draft v1, WRITER, 2026-10-08)

Three options for the first ~30 s, each a different hook type from `playbook/packaging.md` §2. Same line format as `script.md` (`Hx.n {role} [emotion] narration <!-- claims: … -->`). Each runs straight into the **shared continuation S03 of `script.md`** (define "keeping up" → Ruth introduced as ILLUSTRATIVE, built on real US prices, "today her check falls short" → "US only … history, not a forecast" → "doesn't say which check to choose"). Constraints therefore always come after the hook and the promise (story §1.3). All three open on a present-day fact (August 2026) or the viewer's question (story §1.1). The promise (same sentence in all three) carries no person words, so no `promise_character` and M6 is not triggered.

Timing: `check_script.py` (2.75 spoken words/s, numbers read out, no holds), M1–M6 recomputed for each option with S03 appended. The checker output for each option is pasted at the top of `script.md`.

## H-A — "Câu hỏi của người xem" (viewer's question)

HA.1 {hook} Does an annuity raise of 2 percent a year keep up with prices? <!-- claims: two_pct_growth_20y_pct -->
HA.2 {question} [curious] At 65, a bigger check that never changes, or a smaller one that rises 2 percent a year: which one holds its buying power? <!-- claims: guide_start, two_pct_growth_20y_pct -->
HA.3 {hook} The latest 20-year stretch of US prices ended this August. <!-- claims: latest_end, windows_20y -->
HA.4 {promise} We tested that raise against every 20-year stretch of US prices since 1947, to see how often it kept its buying power, and how much it usually kept. <!-- claims: windows_20y, median_real_value_2pct_payment_after_20y_pct -->

- Visual: V4 (one faceless figure, two cards of equal height: "level check" / "rises 2% a year"; a fixed `ink-muted` line through both), then a calendar strip closing on "Aug 2026".
- Lead character: Ruth first appears at S03.2 (≈ 0:33), still before 0:45, but the first 30 s have no person (story §2b.1 weaker).
- Risk: safe, flat (packaging §2: "an toàn nhưng phẳng").

## H-B — "Nghịch lý" (paradox, on a present-day fact) — **USED in `script.md` (S01–S02)**

HB.1 {hook} Ruth's check rises every year, and it buys less than her first one. <!-- claims: guide_real_2pct_end_pct -->
HB.2 {question} [curious] At 65, she chose the smaller annuity check that rises 2 percent a year, and asked one thing: would 2 percent keep up with prices? <!-- claims: guide_start, two_pct_growth_20y_pct -->
HB.3 {hook} Her twentieth year of checks ended this August. <!-- claims: latest_end, index_last_month -->
HB.4 {promise} We tested that raise against every 20-year stretch of US prices since 1947, to see how often it kept its buying power, and how much it usually kept. <!-- claims: windows_20y, median_real_value_2pct_payment_after_20y_pct -->

- Visual: D-010 world: Ruth (W4 Person, ILLUSTRATIVE badge) beside a row of 10 crates; a check card above her grows a little each beat while crates fade out one by one, ending at 9 lit crates (`latest_window_real_value_2pct_payment_pct`, "about 9 in 10").
- The paradox is true as stated: the check rose 2 % at every anniversary (`two_pct_growth_20y_pct`) and buys 90.4 % of its first check today (`guide_real_2pct_end_pct`). "Buys less than her first one" is the plain wording asked for by C1 (3/3 readers stuck on "ended below where it started").

## H-C — "Cửa sổ / thời điểm" (window: the latest 12 months)

HC.1 {hook} In the 12 months to August, US prices rose 3.4 percent. <!-- claims: cpi_yoy_latest_pct, index_last_month -->
HC.2 {question} [curious] So does an annuity check that rises 2 percent a year keep up with prices over a whole retirement? <!-- claims: two_pct_growth_20y_pct -->
HC.3 {hook} One year proves little, and it's not a forecast; a retirement can run 20 years. <!-- claims: windows_20y -->
HC.4 {promise} We tested that raise against every 20-year stretch of US prices since 1947, to see how often it kept its buying power, and how much it usually kept. <!-- claims: windows_20y, median_real_value_2pct_payment_after_20y_pct -->

- Visual: a single price-index bar for the last 12 months ("+3.4%") next to a check card ("+2%"); HC.3 widens the frame to a 20-year strip.
- Risk (packaging §2, "dễ thành dự báo"): 3.4 % next to 2 % in the first 5 s invites the forbidden reading "with inflation at 3.4 % today, your check will fall behind". HC.3 has to spend its time defusing that; highest claim-risk of the three.

## WRITER's pick

**H-B.** The lead character and the stakes arrive in the first sentence (story §2b.1; M5 is effectively 0 s), the paradox is a measured present-day fact rather than a forecast, it is logline L1 in a single picture (rising check, fewer crates), and her question is the one the final line answers.
- H-A: the cleanest viewer's question, but no person until ≈ 0:33, and packaging §2 calls this type flat.
- H-C: the strongest "now" fact, but it sets 3.4 % against 2 % in the opening seconds, which is the forecast reading claim-risk forbids.
REVIEWER judges (episode.md §3).

## Draft titles (≤ 60 characters)

1. **Does a 2% Annuity Raise Really Keep Up With Prices?** (51), the dossier title (`episode.yaml`).
2. A 2% Annuity Raise vs 715 Stretches of US Prices (48)
3. Her Annuity Check Rose Every Year. It Buys Less. (48), "Her" = Ruth, ILLUSTRATIVE (thumbnail badge).
