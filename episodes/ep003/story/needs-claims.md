# Needs-claims — Episode 3 (C2 draft v1)

**Status 2026-10-04:** NC-1 → claim `steady_breakeven_tb3ms_pct` = 3.47 and NC-2 → claim `share_avg_rule_agrees_pct` = 100.0 (numbers.md §C, independently checked). Both are now used in S08.4 and S08.6 and on the KEY-7 gate label. NC-3 unchanged (wording guard). NC-4 not used.

Numbers the script would like to use but that have **no claim ID** in `numbers.md`. None of these is in the narration now; the script reads correctly without them. P computes + independent check, or drops.

| # | Wanted number | Definition (for P) | Approx. (WRITER's arithmetic, NOT a claim) | Where it would go | If approved | If rejected |
|---|---|---|---|---|---|---|
| NC-1 (**DONE → claim**) | `steady_breakeven_tb3ms_pct` — the bill rate (same basis as TB3MS, model convention rate/12 compounded monthly) that, held constant for 240 months, turns 1 into exactly 2 | 100 × 12 × (2^(1/240) − 1) | ≈ 3.47 | S08.4 (self-check line, KEY-7) and the gate label on the bill-rate scale; also lets S03 say "a little lower" with a number on screen | S08.4 → "…the roll would need about 3.47 percent a year, every year, just to reach double; the long-run average sat just under it." Gate label shows the number. | Keep current wording: "a little above that [3.42] across all 20 years" — the gate stays unlabelled. |
| NC-2 (**DONE → claim, 873/873**) | `share_avg_rule_agrees_pct` — share of the 873 starts where "20-year average TB3MS > NC-1" gives the same verdict as "roll ended above double" | compare sign(mean(TB3MS over 240 months) − NC-1) with sign(roll − 2) per start | unknown (should be very high; compounding of a varying rate is slightly below compounding of its average, so a few near-double starts may disagree) | Supports the word "roughly" in S08.5 and the KEY-7 muted read ("average must land above the line") | Keep S08.5 as is; method card can add "average rule matches X% of starts". | If agreement is low, rewrite S08.4–S08.5 as "steady rate" only (no "average" claim). |
| NC-3 | Explicit statement that **1.378–1.388× and the 2.40% fixed rate are not comparable to each other** — no number, a wording check | — | — | Not used | — | — (listed so nobody adds "2.40 percent for 20 years gives about 1.6 times" — 1.024^20 ≈ 1.61 has no claim and invites a comparison the episode avoids) |
| NC-4 | `ctx_tb_sep` (3.94%, Sep 2026) | already in numbers.md §B but outside the pin | — | Not used; data stay pinned to August 2026 per C1 | — | — |

Notes for P
- "Not until 2046"-type derived dates (Dana's horizon end) were deliberately avoided: no claim.
- No dollar amounts are used anywhere (Dana's savings stay "a chunk"); if C3 wants a dollar figure on the envelope it needs an ILLUSTRATIVE claim first.
- `ctx_ee_rate` must be updated after the 2026-11-01 announcement (P3/C6); S02.4 wording "for bonds issued May to October 2026" stays correct as long as the episode keeps that date range.
