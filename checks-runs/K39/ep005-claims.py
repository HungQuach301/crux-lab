# numbers.md (origin/ep005) claim IDs → (kind key, value as written in numbers.md). Values written at display precision; checked at that precision.
CLAIMS = [
 ('rate_month_latest', 'rate_month_latest', '2026-09-01'), ('rate_latest', 'rate_latest', 6.862), ('rate_partial', 'rate_partial', 7.28),
 ('sched80_months_latest', 'sched80_months_latest', 99), ('sched78_months_latest', 'sched78_months_latest', 114),
 ('midpoint_months', 'midpoint_months', 180), ('midpoint_end_month', 'midpoint_end_month', 181),
 ('midpoint_binding_rate_min', 'midpoint_binding_rate_min', 12.56), ('midpoint_binding_last_month', 'midpoint_binding_last_month', '1985-05-01'),
 ('sched80_min_A', 'sched80_min_A', 58), ('sched80_max_A', 'sched80_max_A', 132), ('rate_min_A', 'rate_min_A', 2.68), ('rate_max_A', 'rate_max_A', 9.64),
 ('nA', 'nA', 403), ('firstA', 'firstA', '1991-01'), ('lastA', 'lastA', '2024-07'),
 ('shareA_ltv24_le80', 'shareA_ltv24_le80', 0.586), ('shareA_ltv24_le75', 'shareA_ltv24_le75', 0.156),
 ('nB', 'nB', 307), ('firstB', 'firstB', '1991-01'), ('lastB', 'lastB', '2016-07'),
 ('medianB_months_to80', 'medianB_months_to80', 23), ('minB_months_to80', 'minB_months_to80', 13), ('shareB_over60', 'shareB_over60', 0.147),
 ('maxB_months_to80', 'maxB_months_to80', 112), ('maxB_start', 'maxB_start', '2005-10-01'), ('shareB_le_sched80', 'shareB_le_sched80', 0.906),
 *[x for n, m, r, t, s8, s7, ch, l24 in [('fast', '2004-01-01', 5.71, 13, 86, 100, 11.2, 0.725), ('typical', '2014-06-01', 4.16, 23, 71, 83, 9.8, 0.784),
                                         ('slow', '2005-10-01', 6.07, 112, 90, 104, -3.3, 0.867)]
    for x in [(f'buyer_{n}_purchaseMonth', f'buyer_{n}_purchaseMonth', m), (f'buyer_{n}_rate', f'buyer_{n}_rate', r),
              (f'buyer_{n}_monthsTo80Index', f'buyer_{n}_monthsTo80Index', t), (f'buyer_{n}_sched80Months', f'buyer_{n}_sched80Months', s8),
              (f'buyer_{n}_sched78Months', f'buyer_{n}_sched78Months', s7), (f'buyer_{n}_hpiChangeTo80Pct', f'buyer_{n}_hpiChangeTo80Pct', ch),
              (f'buyer_{n}_ltvIndexAt24', f'buyer_{n}_ltvIndexAt24', l24)]],
 ('mspus_latest', 'mspus_latest', 410700.0), ('mspus_quarter', 'mspus_quarter', '2026-04-01'),
 ('ex_price', 'illustrativePrice', 400000), ('ex_loan', 'ex_loan', 360000.0), ('ex_down', 'ex_down', 40000), ('ex_payment_pi', 'ex_payment_pi', 2361.94),
 ('ex_target80', 'ex_target80', 320000), ('ex_target78', 'ex_target78', 312000), ('ex_extra_down_for_20', 'ex_extra_down_for_20', 40000),
 ('value_removal_ltv_early', 'lenderLtvEarly', 0.75), ('pmi_required_below20', 'requestLtv', 0.80),
 ('slowB_n', 'slowB_n', 45), ('slowB_years', 'slowB_years', [2005, 2006, 2007, 2008, 2009]), ('slowB_first', 'slowB_first', '2005-05-01'),
 ('slowB_last', 'slowB_last', '2009-02-01'),
 ('hpi_peak_month', 'hpi_peak_month', '2007-06-01'), ('hpi_peak', 'hpi_peak', 226.0), ('hpi_trough_month', 'hpi_trough_month', '2012-01-01'),
 ('hpi_trough', 'hpi_trough', 175.8), ('hpi_peak_to_trough_pct', 'hpi_peak_to_trough_pct', -22.2),
 ('buyer_slow_index_peak', 'fraction:buyer_slow_indexPeakPct', 0.0433), ('buyer_slow_index_peak_month', 'buyer_slow_indexPeakMonth', 20),
 ('buyer_slow_index_trough', 'fraction:buyer_slow_indexTroughPct', -0.1885), ('buyer_slow_index_trough_month', 'buyer_slow_indexTroughMonth', 75),
 ('robust_cs_medianB', 'robust_cs_medianB_months_to80', 23), ('robust_cs_maxB', 'robust_cs_maxB_months_to80', 119),
 ('robust_cs_maxB_start', 'robust_cs_maxB_start', '2006-04-01'), ('robust_cs_shareB_over60', 'robust_cs_shareB_over60', 0.147),
 ('robust_cs_shareA_le80', 'robust_cs_shareA_ltv24_le80', 0.561), ('robust_cs_shareA_le75', 'robust_cs_shareA_ltv24_le75', 0.233),
]
# numbers.md IDs not mapped to the kind (rules / not modelled): midpoint rule text aside, these are legal provisions or editorial.
NOT_MODEL = ['pmi_premium', 'borrower_request_conditions', 'value_removal_rule', 'value_removal_seasoning_years']
