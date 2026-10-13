You are an independent checker. Work ONLY inside the repository directory episodes/ep008/. Do NOT spawn sub-agents. Do NOT read
episodes/ep008/model/model.py, episodes/ep008/out/model.json, or anything under topics-r2/ (those are the builder's work; you must stay blind to them).

Inputs you may read: episodes/ep008/data/raw/*.csv (FRED CSV files: HPIPONM226N = FHFA purchase-only house price index, monthly;
CUUR0000SEHA = CPI-U rent of primary residence, monthly, October 2025 missing; MORTGAGE30US = Freddie Mac 30-year rate, weekly, percent;
TB3MS = 3-month T-bill rate, monthly, percent) and this brief.

Definitions (write your own Python from these; save it as episodes/ep008/model/independent/check.py and run it with python3):
- Months are YYYY-MM. Monthly mortgage rate for month s = mean of the weekly MORTGAGE30US values dated in month s.
- CPI rent for 2025-10 = geometric mean of 2025-09 and 2025-11.
- Two illustrative people start in month s. Price P = 400000. Buyer: 20% down + 3% closing costs paid upfront; loan 0.8P, 30-year (360 months)
  level payment at month-s rate (x = rate/1200, pay = L*x/(1-(1+x)^-360)); balance updates monthly bal = bal*(1+x) - pay.
  Owner costs each month k = 0.025/12 * P * HPI(s+k)/HPI(s). Buyer outlay month k = pay + owner cost.
- Renter: month-1 rent = y(s)*P/12, where y(s) = 0.05 * (CPI(s)/HPI(s)) / (CPI(2026-07)/HPI(2026-07)). Rent month k = rent0 * CPI(s+k)/CPI(s).
- Renter pot starts at 0.23P; each month k pot += buyer outlay - rent (may go negative; no interest in the main case).
- After H years (12H months, k = 0..12H-1), end month e = s+12H: buyer equity = 0.94 * P*HPI(e)/HPI(s) - balance. Advantage = equity - pot.
- Valid start months: s >= 1991-01 with a rate in s and HPI and CPI for every month s..e. H in {5,10,15}.
- Variant T-bill: after adding each month's difference, pot *= 1 + TB3MS(s+k)/1200 (needs TB3MS for s..e-1).
- Variant anchor yields: replace 0.05 by 0.04, 0.06, and by 12*1579/339100 and 12*1464/363800.
- "Today": latest complete rate month = month of last weekly date if the date 7 days later is in the next month, else the previous month;
  today buyer month-1 outlay = pay at that month's mean rate (rounded to 0.01 first? NO: use unrounded) + 0.025/12*P; today rent = 0.05*P/12.

Compute and print (rounding: shares to 0.1 percentage point, dollars to whole dollars, rates to 0.01):
n_10y, first_10y, last_10y, share_buyer_ahead_10y (advantage > 0), median_adv_10y, best_start_10y, best_adv_10y, worst_start_10y, worst_adv_10y,
n_renter_ahead_10y (advantage <= 0), the same seven for 5y and 15y, worst_price_change_10y and best_price_change_10y (HPI change over window, %),
worst_rate_10y, best_rate_10y, era shares for starts 1991-01..1999-12, 2002-01..2007-12, 2009-01..2016-07 (10y), renter_first_10y and renter_last_10y
(first and last start with advantage <= 0), share_tbills_10y, share_yield4pct_10y, share_yield6pct_10y, share for the two Census anchors,
rate_month_latest, rate_latest, today_buyer_month1, today_rent_month1, today_rent_to_outlay (%, 0.1), and the lowest month-1 rent/outlay ratio
across 10y windows with its start month.

Then write episodes/ep008/model/independent/report.md: a table quantity | your value, and the exact command you ran. Keep it short. Do not edit any other file.

TOOL NOTE: you are started in the repository root. Run the script with exactly `python3 episodes/ep008/model/independent/check.py` (no `cd`, no `&&`, no pipes) — only commands starting with `python3 ` are permitted. Use the Write tool to create files.
