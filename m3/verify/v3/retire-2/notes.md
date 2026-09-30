# retire-2 recomputation notes (data: FRED CWUR0000SA0 CSV fetched 2026-09-30, last obs 2026-08-01)
- cola_2021_pct = 5.9: Q3 = simple mean of Jul/Aug/Sep NSA values (unrounded); COLA rounded half-up to 0.1 (Decimal, "nearest one-tenth"); chain from base 1983 over 1984..2023; the computed chain reproduces all official COLAs incl. 0 in 2009/2010/2015 (computed -2.1, -0.6, -0.4).
- cola_2022_pct = 8.7: same chain; base 2021.
- shortfall_2022_avg_pct = 6.7573: base b=2021; mean of (1 - Q3(2021)/CPIW(m))*100 over Jan-Dec 2022.
- shortfall_2022_months = 0.81088: same sum without x100/12.
- shortfall_2021_2023_months = 1.63521: bases 2020, 2021, 2022 for payment years 2021, 2022, 2023. "Positive computed COLA" read as the rounded value > 0.
- cumulative_1985_2024_months = 9.88165: 480 months, negatives included; base for 2010-2011 is 2008, for 2016 is 2014, for 2017 is 2016 (2016 COLA 0.3 > 0).
- avg_annual_shortfall_1985_2024_pct = 2.05868: cumulative / 480 x 100.
- years_retirees_ahead_1985_2024 = 4: payment years with negative 12-month sum: 2009, 2010, 2015, 2016.
