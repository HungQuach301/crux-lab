# WRITER — Tập 9 rút cold open theo bản đọc thật (một lượt headless, 0 agent con)

You are a new WRITER. Edit only scenes S01–S03 of `episodes/ep009/story/script.md` (+ `story/hooks.md` HB text to match, + one header line "Table-read fix"). Read `playbook/story.md` §1 and `episodes/ep009/review-g1/table-read.json` (real ElevenLabs timings, key "timeline" and "M"). Do not spawn agents. Do not touch `check_script.py`.

On the real voice (Eric, speed 0.9) the opening is too slow: M2 promise ends 56.5 s (limit 50), M3 question ends 42.3 s (limit 40), M7 third `fact` ends 36.1 s (limit 35). Cut **≥ 8 s of speech before the end of the promise**, keeping all roles and meaning:
- S03.3 promise is 13.6 s — make it ≤ 9 s (one paradox, two halves; keep "since 1991" or move it to S03.5).
- S01.2 (4.6 s) and S02.1 (6.6 s): tighten (e.g. merge S01.1–S01.2 into one hook ≤ 5 s ending by 5.0 s; S02.1 ≤ 5 s).
- Keep: three `fact` lines with their claims, the question text as close as possible ("So if Nina rents and invests the difference, does she end up ahead of owning?"), the one constraint "It's history, not a forecast." after the promise, the street definition of lit/dark, S03.6–S03.7.
- "nine in ten" was heard by ASR as "nine and ten": write it so it can't be misheard (e.g. "nine times out of ten").
Speech rate on this voice ≈ 2.45 words/s. Reply with the new S01–S03 lines and your estimated end times for the third fact, the question and the promise.
