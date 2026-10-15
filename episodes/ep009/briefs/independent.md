You are an independent checker. Do NOT read episodes/ep009/model/model.py, episodes/ep009/out/, or anything under episodes/ep008. Work only from the raw data files and the definition below. Do not spawn agents.

Write `episodes/ep009/model/independent/check.py` (Python 3, standard library only; you may use csv) that reads:
- `episodes/ep009/data/raw/HPIPONM226N.csv` (FHFA house price index, monthly; columns observation_date, HPIPONM226N)
- `episodes/ep009/data/raw/CUUR0000SEHA.csv` (CPI rent; 2025-10 is empty: fill with geometric mean of 2025-09 and 2025-11)
- `episodes/ep009/data/raw/MORTGAGE30US.csv` (weekly 30-year rate; monthly rate = mean of weekly values dated in that month)
- `episodes/ep009/data/raw/ff3_monthly.csv` (Fama/French; use ONLY the first monthly block, rows whose first field is YYYYMM, stop at the line containing "Annual"; monthly stock total return = (Mkt-RF + RF)/100)
Then run it and write `episodes/ep009/model/independent/result.json` with the quantities listed below.

Definition (two illustrative twins, same start month s, same money):
- Price P = 400000 at month s. Buyer: down 20 %, closing 3 %, 30-year fixed loan of 0.8P at the start-month mortgage rate (monthly rate r = rate/1200, standard annuity payment). Ownership cost each month = 0.025/12 × P × HPI(m)/HPI(s). Buyer outlay(m) = payment + ownership cost. Loan balance updates monthly: bal = bal×(1+r) − payment.
- Renter: anchor yield y0 = 0.05 at anchor month 2026-07. Start yield y(s) = y0 × (CPI(s)/HPI(s)) / (CPI(2026-07)/HPI(2026-07)). Rent(m) = y(s)×P/12 × CPI(m)/CPI(s).
- Renter pot starts at 0.23P. For k = 0..12H−1 with m = s+k months: gap = outlay(m) − rent(m) (may be negative).
  - mode cash: pot += gap.
  - mode stocks: pot += gap, then pot ×= (1 + stock return of month m).
  - mode lump: pot is NOT changed by gap; pot ×= (1 + stock return of month m) (only the initial 0.23P is invested).
- End month e = s + 12H. Buyer equity = 0.94 × P × HPI(e)/HPI(s) − bal. Buyer advantage = equity − pot. Buyer ahead if advantage > 0.
- Valid start months: s from 1991-01, s has a mortgage rate, HPI and CPI exist for every month s..e, and stock returns exist for months s..e−1.

Quantities (H = 10 unless stated): n windows; share (%) buyer ahead for cash, stocks, lump (1 decimal); number of windows renter ahead for each mode; median advantage for each mode (round to dollar); start month and value of min and max advantage for stocks; number of windows where buyer is ahead with cash but not with stocks; same for 15-year windows (n, share cash, share stocks); for eras 1991-01..1999-12, 2002-01..2007-12, 2009-01..2016-07: share buyer ahead for cash and stocks; advantage for starts 2006-06, 2012-04, 1991-01 in cash and stocks; number of 10-year windows where $1 in stocks (product of 1+return over the 120 months) ended below 1; share of windows buyer ahead (stocks) when y0 = 0.04 and 0.06.

Finally print the result JSON and a one-paragraph note of any ambiguity you had to resolve. Keep it short.
