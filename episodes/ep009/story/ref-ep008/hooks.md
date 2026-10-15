# Hooks — Episode 8 (C2 v2 + cold open v3 sau G1, WRITER, 2026-10-13)

Three options for the first ~50 s (story-d013 §1.7), one per opening type: **tin thời sự** (H-A) / **nghịch lý** (H-B) / **được–mất** (H-C). Same line format as `script.md` (`Hx.n {role} [emotion] narration <!-- claims: … -->`). Each option holds its own hook, three `fact` lines and Nina's question; all three then run into the **shared continuation S03 of `script.md`**: the paradox promise (S03.1) → the one spoken limit, "history, not a forecast" (S03.2, after the promise) → "It shows Nina a whole street of answers, one house for each month" (S03.3, Nina returns; closing line of chapter 1 is S03.4) → "the same pair of twins" (S03.4). "US only", "not advice on whether to buy or rent" and "ILLUSTRATIVE" are on screen (beats B01–B03), not spoken.

**Shared promise** (S03.1, no person words, so no `promise_character`, M6 = 0): *"We replayed her choice in every month since 1991, one twin buying, one renting, and after ten years, the same rules gave opposite answers."* Paradox: same rules, opposite answers; the street (S08–S22) and the rent tag (S24–S28) take it apart. The core number ("3 in 4") is not spoken in any hook; it is read in digits once, at S13.2.

Rules for all three (story-d013 §1.1–1.5): hook ≤ 5 s (M1) on a present-day or dated fact with a claim · 3 `fact` lines, the third ending ≤ 35 s (M7) · Nina's question ≤ 40 s (M3) · promise ≤ 50 s (M2) · ≤ 1 `constraint` line in 0:00–1:00, after the promise (M8) · Nina back ≤ 45 s (M5). Timing: `check_script.py` (2.66 spoken words/s), each option with S03 appended; output at the top of `script.md`.

## H-A — "Tin thời sự" (today's rent, Nina's own question) — **USED in `script.md` (S01–S02)**

HA.1 {hook} It's September 2026, and Nina's rent looks cheap beside buying. <!-- claims: rate_month_latest, today_rent_to_outlay -->
HA.2 {fact} Against a buyer's first month, her rent is a smaller share than in any month we replayed. <!-- claims: today_rent_to_outlay, rent_to_outlay_min_10y -->
HA.3 {hook} Nina has a down payment saved for a $400,000 home. <!-- claims: price, down_usd -->
HA.4 {fact} In 72 start months in a row, the buyer ended ahead just 6 times. <!-- claims: era_2002-2007_n, era_2002-2007_share -->
HA.5 {fact} Yet over fifteen years, the buyer ended ahead every time. <!-- claims: n_15y, share_buyer_ahead_15y -->
HA.6 {question} [worried] Is her rent money wasted? <!-- claims: — -->

- Visual: Nina (warm lamp, ILLUSTRATIVE) at her apartment door at the end of an unlit street; the rent tag beside a buyer's first-month stack; the down-payment and closing-cost stacks; a run of 72 grid cells going dark with 6 lit (dates on screen: "2002 to 2007"); the 15-year grid all lit; the question as text.
- Why used: keeps H-A's idea (her own question, the dossier's top question, answered by S32.4), now opened on a dated present-day fact. The three facts swing the viewer twice (rent looks cheap today → a 72-month run where renting mostly came out ahead → over fifteen years buying always did), so the question arrives already unsettled. The 72-month run is named "2002 through 2007" at S11.1 (callback).

## H-B — "Nghịch lý" (two facts that seem unable to both be true)

HB.1 {hook} Over fifteen years, the buyer ended ahead every time. <!-- claims: n_15y, share_buyer_ahead_15y -->
HB.2 {fact} Yet in 72 start months in a row, the buyer ended ahead just 6 times. <!-- claims: era_2002-2007_n, era_2002-2007_share -->
HB.3 {fact} And from 2009 to mid-2016, every start ended with the buyer ahead. <!-- claims: era_2009-2016_share -->
HB.4 {fact} In September 2026, Nina's rent is a smaller share of a buyer's first month than in any month we replayed. <!-- claims: rate_month_latest, today_rent_to_outlay, rent_to_outlay_min_10y -->
HB.5 {question} [worried] So is her rent money wasted? <!-- claims: — -->

- Visual: the 15-year grid fully lit, then the 10-year grid with its dark 72-month block ("2002 to 2007" on screen), then the lit 2009–2016 columns; Nina at the end of the street with her tag.
- Risk: opens on a historical fact, not today's; Nina arrives at ~18 s (still < 45 s, M5) and the savings that put her at the decision are only on screen.

## H-C — "Được–mất" (a stake, on today's numbers)

HC.1 {hook} Nina's rent is $1,667 a month. <!-- claims: today_rent_month1 -->
HC.2 {fact} In September 2026, buying the same home would cost her $2,933 in the first month. <!-- claims: rate_month_latest, today_buyer_month1 -->
HC.3 {fact} Her rent is a smaller share of that than in any month we replayed. <!-- claims: today_rent_to_outlay, rent_to_outlay_min_10y -->
HC.4 {fact} Yet over fifteen years, the buyer ended ahead every time. <!-- claims: n_15y, share_buyer_ahead_15y -->
HC.5 {hook} Nina has her down payment saved. <!-- claims: down_usd -->
HC.6 {question} [worried] Is her rent money wasted? <!-- claims: — -->

- Visual: the rent tag on Nina's door beside a taller stack for the buyer's first month (both dated, ILLUSTRATIVE), then the 15-year grid all lit.
- Risk: claim-risk — two monthly dollar figures in the first 11 s read easily as "renting is cheaper, so…"; the episode only says these are first months (S30.3), and the hook spends act 3's "today" beat. Not chosen.
