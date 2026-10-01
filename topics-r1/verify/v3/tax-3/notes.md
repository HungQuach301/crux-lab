# tax-3 V3 recalculation notes
Data: SP500.csv downloaded from pinned FRED URL; SHA-256 67e7bafb...815dc7 MATCHES declared. 2491 non-blank closes (96 blank holiday rows dropped), 2016-11-01..2026-09-30.
- tax_saving_if_flat_usd_24: (0.24-0.15)*10000 = 900.00.
- after_tax_sell_now_usd_24: 50000-2400 = 47600.
- breakeven_drop_pct_24: x*=(47600-6000)/42500=0.978824; 100*(1-x*)=2.118 (3 dp). Formula valid since V*x*>C.
- windows_n: 2491-21 = 2470.
- first_window_start: 2016-11-01 (first non-blank close).
- last_window_start: 2026-08-31 (index W-1 = 21 trading days before 2026-09-30).
- share_wait_worse_pct_24: 440/2470 strict d<0 -> 17.81 (2 dp).
- median_wait_minus_now_usd_24: even count, mean of positions 1234,1235 -> 1653.78.
- p05_wait_minus_now_usd_24: sorted d[floor(0.05*2469)=123] -> -1825.31.
- worst_wait_minus_now_usd_24: min d -> -14083.41.
- worst_window_start: argmin x_i -> 2020-02-21 (unique).
- worst_window_index_change_pct: -32.97 (2 dp).
- breakeven_drop_pct_22: x*=(47800-6000)/42500; -> 1.647 (3 dp).
- share_wait_worse_pct_22: strict d<0 with t=0.22 -> 20.24 (2 dp).
- share_index_down_pct: strict x<1 (no ties x==1) -> 30.81. Ambiguity: definition gives no rounding; rounded to 2 dp like the other shares.
