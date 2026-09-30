# debt-6 recalculation notes
Data: FRED fredgraph.csv downloaded 2026-09-30 into ./data/ (2541 rows each, 2017-01-03..2026-09-29); non-numeric values ('.'/blank) dropped. Provision text not fetched: the fee (1.25%) is fixed in the definitions themselves.
- n_days: 2434. Count of dates with numeric values in both series, within 2017-01-03..2026-09-29. No ambiguity.
- share_days_va_below_best_conv: 92.4. Strict VA < conv on integer thousandths (values already have 3 decimals); ties count as not below; half-up rounding.
- n_days_since_20230407: 866. Common dates >= 2023-04-07 (inclusive).
- share_days_va_below_since_20230407: 99.9. Same strict comparison as above.
- mean_va_since_20230407: 6.261. Simple arithmetic mean over window dates (unweighted).
- mean_conv_since_20230407: 6.581. Same.
- mean_gap_since_20230407: 0.320. Mean of daily (conv - VA); equals difference of means.
- monthly_saving_per_100k: 20.97. p(rc)-p(rv) using unrounded window means.
- breakeven_months_payment_only: 59.6. 1250/(p(rc)-p(rv)). Note the claim cites 47 months, which is the net figure, not this one.
- breakeven_months_net: 47. First m with m*dp + (B_conv(m) - B_va(m)) >= 1250; balances iterated in float.
- net_gain_10y_per_100k: 1952. 120*dp + (B_conv(120)-B_va(120)) - 1250, undiscounted, half-up to dollar.
