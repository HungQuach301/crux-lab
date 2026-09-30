# tax-2 recomputation notes

Parameters were checked against the downloaded texts in data/: USC 21, 24 and 32 (uscode.house.gov), IRB 2025-45 (Rev. Proc. 2025-32) and IR-2025-103. All of them match input.json.

- credit_2026_usd_at_100k = 2100.00. The rate at AGI 100,000 is 50 - ceil(85,000/2,000) = 50 - 43, which floors at 35%. 35% x 6,000 = 2,100. No ambiguity.
- fsa_saving_usd_at_100k_12pct = 1473.75. This is 7,500 x 0.1965. The claim's "$1,474" is this figure rounded.
- advantage_credit_usd_at_100k = 626.25. I followed the definition literally. Earned income = wages. The FSA path cuts the expense cap to 0. I didn't round to whole dollars or use the IRS tax tables or EIC tables (I used the continuous formulas).
- advantage_credit_usd_at_80k = 626.25. Same method. At 80k the EIC is 0 on both paths and the credit is fully used.
- advantage_fsa_usd_at_40k = 2153.25. Same method, with the sign flipped.
- advantage_fsa_usd_at_180k = 603.75. Same method, with the sign flipped. The care rate at 180k is 35 - ceil(30,000/4,000) = 27%.
- credit_wins_from_wages_usd = 70500. On the $500 grid the difference is -89.55 at 70,000 and +15.75 at 70,500. The range extends contiguously from 100,000.
- credit_wins_to_wages_usd = 139000. The difference is +26.25 at 139,000 and -23.75 at 139,500.
- cap_6000_in_current_prices_usd = 10748. This one is ambiguous. The FRED file has a blank value for 2025-10 (no BLS release), so the named window Sep 2025 to Aug 2026 holds only 11 values. I used the most literal reading: the mean of the 11 values present in that window, divided by the 2003 mean (12 values), times 6,000. The alternatives give different results. The last 12 non-missing values (Aug 2025 to Aug 2026, skipping Oct) give 10731, which matches the claim. Interpolating October as the mean of Sep and Nov gives 10734.
