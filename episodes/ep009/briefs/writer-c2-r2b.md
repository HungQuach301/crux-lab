# WRITER — Tập 9 C2 v2b (hai sửa nhỏ; một lượt headless, 0 agent con)

You are a new WRITER. Edit only `episodes/ep009/story/script.md` (+ the matching `beats.md` row and one line in the script header "C2 v2 changes"). Read `episodes/ep009/numbers.md` for claim IDs. Do not spawn agents. Do not touch `check_script.py`.

The machine checker fails on two points:
1. `S18.1: câu có số nhưng không claim: ['ten']` — S18.1 "Stay fifteen years instead of ten…" speaks "ten"/"fifteen" with no claim. Reword so no bare number is spoken without a claim (e.g. "Stay longer, and with stocks most of the lights go out"), or attach the right claim IDs (`n_15y` / `n_10y`).
2. Estimated length 532 s < 540 s (`lab` floor): about 18 more spoken words are needed — **with sourced substance, not padding**. Use the unused real result for audience question 2 (holding period): over **five** years with the pile in stocks the buyer was ahead in `share_buyer_ahead_stocks_5y` = 53.4 % ("Hiển thị" in numbers.md), versus about 3 in 4 with cash (`share_buyer_ahead_cash_5y` 74.4 %) — add one or two short lines just before the fifteen-year scene (S18), so the holding-period beat reads five → ten → fifteen. Respect ≤ 2 new spoken numbers per scene (put the cash figure on screen if needed) and keep each line ≤ 20 words. Add the beat to `beats.md`.
Do not change other lines. Reply with the changed/added line IDs and their text only.
