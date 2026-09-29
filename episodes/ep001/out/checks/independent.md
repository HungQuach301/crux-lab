# Episode 1: independent check (K2 lock `f9e24c91`)

Model claims vs the checker's re-computation (checks/py/r_model.py): **47/47 match (100.0%)**. S01 on out/model.json: {'values compared': 619, 'mismatches': 0, 'model parts not re-computed': 0}.

| rule | status | failing | why |
|---|---|---|---|
| F11 | FAIL | declared artefacts not delivered = 23 | every CONTRACT.md release file is declared in artefacts.M3; the video, voice, stems and render files are not produced yet (M3) |
| A13 | PASS |  |  |
| A15 | MISSING |  | needs out/video.mp4 (ASR on the master) |
| S01 | PASS |  |  |
| S03 | PASS |  |  |
| S04 | PASS |  |  |
| S05 | PASS |  |  |
| S06 | MISSING |  | needs out/checks/page.json (page sampler on the rendered page: yearsTrack/casesTrack); no page yet (M2) |
| S07 | MISSING |  | needs out/checks/page.json (numbers on screen) |
| S08 | MISSING |  | needs out/checks/page.json |
| S09 | MISSING |  | needs out/checks/page.json |
| S10 | PASS |  |  |
| S11 | MISSING |  | needs out/checks/page.json |
| S12 | MISSING |  | needs out/checks/page.json |
| S13 | PASS |  |  |
| S14 | MISSING |  | needs out/video.mp4 (master silences) |
| S15 | FAIL | cold open s = 21.94 |  |
| S16 | PASS |  |  |
| R02 | PASS |  |  |
| V04 | MISSING |  | page rule: needs out/checks/page.json (rendered page) |
| V09 | MISSING |  | page rule: needs out/checks/page.json (rendered page) |
| T1 | MISSING |  | needs the stems and out/video.mp4; on the animatic stems (scratch root) still MISSING: out/video.mp4 |
| L1 | MISSING |  | needs the stems; on the animatic stems (scratch root, out/checks/animatic-T1-L1.json): PASS, 29.2 dB, 0 key words lost |

## Mismatches

none

## Claims

| claim | checker key | ours | checker | match |
|---|---|---|---|---|
| loan_median | median.loan | 375000.0 | 375000.0 | yes |
| cost_median | median.cost | 5123.53 | 5123.53 | yes |
| sav_median | median.monthlySavings | 221.3018074230754 | 221.3018 | yes |
| be_simple_median | median.simple | 24 | 24.0 | yes |
| be_bal_median | median.withBalance | 30 | 30.0 | yes |
| net36_median | median.net36 | 1039.0512106753022 | 1039.0512 | yes |
| net84_median | median.net84 | 8092.993053949721 | 8092.9931 | yes |
| cut36_median | median.cut36 | 0.5 | 0.4954 | yes |
| loan_small | small.loan | 115000.0 | 115000.0 | yes |
| cost_small | small.cost | 3667.05 | 3667.05 | yes |
| sav_small | small.monthlySavings | 67.86588760974325 | 67.8659 | yes |
| be_simple_small | small.simple | 55 | 55.0 | yes |
| be_bal_small | small.withBalance | 75 | 75.0 | yes |
| net36_small | small.net36 | -1777.1917620595937 | -1777.1918 | yes |
| net84_small | small.net84 | 386.0170698779193 | 386.0171 | yes |
| cut36_small | small.cut36 | 1.12 | 1.1179 | yes |
| loan_large | large.loan | 655000.0 | 655000.0 | yes |
| cost_large | large.cost | 5513.97 | 5513.97 | yes |
| sav_large | large.monthlySavings | 386.54049029897214 | 386.5405 | yes |
| be_simple_large | large.simple | 15 | 15.0 | yes |
| be_bal_large | large.withBalance | 18 | 18.0 | yes |
| net36_large | large.net36 | 5250.005181312897 | 5250.0052 | yes |
| net84_large | large.net84 | 17570.890267565774 | 17570.8903 | yes |
| cut36_large | large.cut36 | 0.32 | 0.3165 | yes |
| gap24 | gap | 1132.951085689303 | 1132.9511 | yes |
| be_simple_025 | simple@025 | 38 | 38 | yes |
| be_bal_025 | bal@025 | None | None | yes |
| be_simple_05 | simple@05 | 26 | 26 | yes |
| be_bal_05 | bal@05 | 36 | 36 | yes |
| be_simple_10 | simple@10 | 16 | 16 | yes |
| be_bal_10 | bal@10 | 18 | 18 | yes |
| n_eps | n_eps | 13 | 13 | yes |
| beh_min | beh_min | 10 | 10 | yes |
| beh_max | beh_max | 20 | 20 | yes |
| behs_min | behs_min | 10 | 10 | yes |
| behs_max | behs_max | 21 | 21 | yes |
| n_further | n_further | 3 | 3 | yes |
| n_nofurther | n_nofurther | 10 | 10 | yes |
| ex_be | ex_be | 19 | 19 | yes |
| ex_gap | ex_gap | 7 | 7 | yes |
| be23 | be23 | 19 | 19 | yes |
| behd_min | behd_min | 18 | 18 | yes |
| behd_max | behd_max | 39 | 39 | yes |
| behl_max | behl_max | 11 | 11 | yes |
| m81 | m81 | 2 | 2 | yes |
| be81 | be81 | 13 | 13 | yes |
| cut36_large_words | large.cut36 | 0.32 | 0.3165 | yes |
