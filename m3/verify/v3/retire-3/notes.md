# retire-3 recalculation notes
Data: FRED CPIAUCNS CSV (coed=2026-08-01), downloaded 2026-09-30; 2025-10 is blank in the file and treated as missing (not interpolated).
- windows_25y: starts 1947-01..2001-08 (s+300 <= 2026-08) = 656 candidates; 2000-10 dropped (end 2025-10 missing) -> 655. No ambiguity.
- min_loss_25y_pct: min of (1 - CPI(s)/CPI(s+300))*100, unrounded. No ambiguity.
- min_loss_25y_start_yyyymm: argmin start month; unique minimum. No ambiguity.
- median_loss_25y_pct: statistics.median of the 655 losses (odd count, middle value). No ambiguity.
- max_loss_25y_pct: max loss x100. No ambiguity.
- share_25y_over_half_pct: strict > 0.5, denominator = 655 valid windows.
- min_loss_30y_pct: starts 1947-01..1996-08 (596 candidates); 1995-10 dropped (end 2025-10 missing) -> 595 windows. No ambiguity.
- median_loss_30y_pct: statistics.median of the 595 30-year losses (odd count). No ambiguity.
