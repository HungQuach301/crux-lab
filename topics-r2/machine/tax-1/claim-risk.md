# tax-1 claim risk: TIPS in a taxable account

**Phrasings that would overstate the claim**
- "TIPS lose money in a taxable account." The result is for a model bond at a 24% federal rate held ten years. It is negative in about 39% of past purchase months, not always.
- "Your TIPS will lose to inflation." This is history, not a forecast. The outcome depends on the real yield at purchase and on inflation over the holding period.
- "The IRA always gives a positive real return." It returns exactly the real yield at purchase, which was below zero in 18 of the 166 purchase months.
- The 2022 tax-versus-coupon figure assumes the minimum coupon. Say "a holding with the minimum coupon", not "every TIPS".

**What the episode must not say**
- No advice. Do not say "move your TIPS into your IRA" or "never buy TIPS in a taxable account". Show the comparison and let the viewer place themselves.
- No forecast of inflation or real yields.
- Do not call TIPS "tax-free". The interest is state-exempt only, and the model ignores state tax.

**Data and rule limits**
- FII10 is a constant-maturity monthly average, not an auction yield. Real bonds trade at premiums or discounts and pay semiannual coupons with a 0.125% floor.
- The indexation lag is modeled as three months, monthly. Treasury interpolates daily and used a substitute index for the missing October 2025 CPI. The model skips that month instead.
- Deflation years are taxed symmetrically, which is a simplification of the OID and deflation-adjustment rules.
- Tax treatment is quoted from IRS Publication 550 (inflation-indexed debt instruments). One rate, 24%, is used for all years, although bracket rates differed before 2018.
