# Hooks — Episode 7 (C2 v1, WRITER, 2026-10-11)

Three options for the first ~30 s, each a different hook type from `playbook/packaging.md` §2. Same line format as `script.md` (`Hx.n {role} [emotion] narration <!-- claims: … -->`). Each runs straight into the **shared continuation S03 of `script.md`** (Tessa named as illustrative with real rates → this week's 6.73 % / 7.40 % → "US only … history, not a forecast" → "won't say which loan to take, or whether to invest"). Constraints therefore always come after the hook and the promise (story §1.3). All three open on a present-day fact (the week of October 8, 2026) or the viewer's own question (story §1.1).

**Shared promise** (identical in all three, no person words, so no `promise_character`, M6 = 0): *"We replayed every week the US survey priced both loans, to put that fallback in dollars and find what each extra dollar of principal earns."* It answers the anchor video's question ("30-year mortgage paid in 15" vs a 15-year, `tongket-t6/anchors/q13-15-vs-30-mortgage.json`) inside 30 s, and names both deliverables of logline L1: the dollar price of the fallback, and the bar (viewer question 1).

Timing: `check_script.py` (2.66 spoken words/s, numbers read out), M1–M6 recomputed for each option with S03 appended; output pasted at the top of `script.md`.

## H-A — "Câu hỏi của người xem" (viewer's question, the anchor's phrase)

HA.1 {hook} A 30-year mortgage paid in 15, or a 15-year mortgage? <!-- claims: pay30on15_now -->
HA.2 {question} [curious] If the house is paid off on the same day either way, what does the 30-year's lower required payment cost? <!-- claims: pay30on15_now, pay30_now -->
HA.3 {hook} Tessa is borrowing $320,000, and that is her question. <!-- claims: interest_15_now -->
HA.4 {promise} We replayed every week the US survey priced both loans, to put that fallback in dollars and find what each extra dollar of principal earns. <!-- claims: n_weeks -->

- Visual: V4 adapted (one faceless figure, two offer cards "15-year" / "30-year paid in 15", same height), then W1 house + W4 Tessa with the ILLUSTRATIVE badge at HA.3.
- Strength: the exact search phrase of the anchor and of the dossier keywords. Risk (packaging §2): safe but flat; no number and no stake until HA.3.

## H-B — "Chi phí ẩn" (a cost the viewer hasn't counted) — **USED in `script.md` (S01–S02)**

HB.1 {hook} Tessa's mortgage fallback costs $120 a month. <!-- claims: extra_vs15_month_now -->
HB.2 {hook} She's borrowing $320,000, and in her city that payment is her biggest bill. <!-- claims: interest_15_now -->
HB.3 {question} [curious] A 15-year mortgage, or a 30-year paid off in 15 years anyway, with its lower payment kept for a bad month? <!-- claims: pay30on15_now -->
HB.4 {promise} We replayed every week the US survey priced both loans, to put that fallback in dollars and find what each extra dollar of principal earns. <!-- claims: n_weeks -->

- Visual: D-010 world: Tessa (W4, ILLUSTRATIVE) by her house (W1); a thin W2 stack of bills grows beside the house, one bundle per beat, with "$120 a month" over it; at HB.3 two offer cards hang above her.
- The cost is a measured present-day fact (`extra_vs15_month_now`, at the survey rates of the week of October 8, 2026 on $320,000; G1 answer: dated in S03.1 and on screen in B01), not a "hidden fee": nothing is said to be hidden, and the word "fee" is not used (packaging §2 risk). The fallback is named in sentence 1 and explained by sentence 3.
- Lead character, stake and the central object (the stack) arrive in the first 4 s; M5 is effectively 0 s.

## H-C — "Luật quen bị thử" (a familiar rule, tested)

HC.1 {hook} Paying a mortgage off early is often treated as the obvious win. <!-- claims: — -->
HC.2 {hook} Each extra dollar of principal earns the loan's rate: this week, 7.40 percent. <!-- claims: bar_now, r30_now -->
<!-- G1 lô: HC không chọn, không sinh giọng; "this week" ở HC.2 giữ nguyên (đổi thành ngày đẩy M2 HC lên 28,9 s, sát ngưỡng). -->
HC.3 {question} [curious] A 15-year mortgage, or a 30-year paid off in 15 years anyway, with a lower payment kept for a bad month? <!-- claims: pay30on15_now -->
HC.4 {promise} We replayed every week the US survey priced both loans, to put that fallback in dollars and find what each extra dollar of principal earns. <!-- claims: n_weeks -->

- Visual: W3 beam (the bar) rises to "7.40% a year, before taxes" beside a W1 house; at HC.3 the two offer cards.
- Risk: "tested" must not read as "refuted" (packaging §2), and 7.40 % in the first 5 s invites a markets comparison the episode refuses (claim-risk: before taxes, not an investment return). It also opens on viewer question 1 rather than on the lead's decision, so Tessa arrives only at S03.1 (≈ 0:30).

## WRITER's pick

**H-B.** The lead character, the stake and the central object (the stack) arrive in the first sentence (story §2b.1); the stake is a measured present-day dollar figure, so it is concrete without being a forecast; and Tessa's question in HB.3 is the one her final line (S33.3) answers with the same words ("a 30-year paid in 15").
- H-A: the cleanest anchor-phrase match, but no person and no stake until ≈ 0:12; flat by packaging §2.
- H-C: strongest for viewer question 1, but highest claim-risk (7.40 % next to "obvious win" invites "prepaying beats investing") and the lead arrives last.
REVIEWER judges (episode.md §3).

## Draft titles (≤ 60 characters; final at G1, packaging.md §7)

1. **15-Year Mortgage or a 30-Year Paid in 15? The Real Price** (57), the dossier title (`episode.yaml`).
2. A 30-Year Paid in 15 Costs $120 a Month More. Worth It? (55): "$120 a month" is the survey rates of the week of October 8, 2026 on $320,000 (description says so).
3. Pay Extra on a Mortgage? The Bar Each Dollar Has to Clear (59).
