# Packaging brief — Episode {N}: {working title}
<!-- BỎ từ Tập 8 (D-013: không thumbnail, không ChatGPT) — chỉ tham chiếu. Trước đây: ĐƯỜNG CHÍNH từ Tập 7 (câu trả lời tổng kết Tập 6 câu 3, 11/10; `playbook/packaging.md` §7). P4 (video hoàn tất, trước G3) sinh bản điền sẵn:
     python3 toolkit/market/brief.py episodes/epNNN --topic <id> --trend <trend7.json> --anchors <neo.json> --objects "…" --banned "…" --frame <png> ×3–4
     → episodes/epNNN/out/package/PACKAGING-BRIEF.md. Tiếng Anh; chủ dự án dán NGUYÊN khối dưới vạch vào ChatGPT, đính kèm 3–4 khung PNG (f).
     ChatGPT làm tiêu đề, mô tả, thumbnail, tag; chủ dự án dán kết quả lại vào P4 → P4 kiểm (package_check.py + rescore.py + đọc) → câu sửa sẵn nếu lệch. -->
---
You are packaging one finished YouTube video for **Crux**, a US personal-finance channel that replays real history with data. Make: 3 titles (mark your pick), 1 description, ≤ 5 tags, 1 thumbnail (1280×720).

**Episode.** {2–3 sentences: the viewer question, what was replayed (series, years), the answer in plain words, the guide character.}

**(a) What is rising this week on this topic** (last 7 days, fastest views/day; patterns, not titles to copy):
{trend}

**(b) Anchor videos — make ours the natural next video after these** (same viewer question, 30–90 days old, fastest in the topic):
{anchors}

**(c) Title.** Put the search phrase FIRST in the title and in the first 2 lines of the description (~150 characters). Search phrase: **{phrase}**. Title frames that win in this niche (≤ 60 characters, fill only with allowed numbers):
1. {frame 1}
2. {frame 2}
3. {frame 3}
Title approved at G1 (keep its idea): {g1 title}

**(d) Thumbnail.** Winning style (90 days): {winning style from market/REPORT.md §3}. Center it on **this video's own object, named exactly as the narration says: {objects}**. Never: {banned}. Base it on one attached frame (3D low-poly world, faceless figures, no photos, no faces, no logos, no prediction arrows). Max **{3–4} large words**; one idea; readable at phone size (168×94). Characters are ILLUSTRATIVE (write the word next to any figure).

**(e) Facts you may use.** Allowed numbers — only these, exactly as written: {display list from out/claims.json}. Any other number, dollar amount or year is forbidden.
Forbidden: advice ("you should", "best", "do this"), prediction ("will", "next year"), "your loan/your money will…" (use "a buyer who…"), dollar amounts not listed above. The description must say "history, not a forecast" and "US only".
Chapters (paste exactly):
{0:00 … from out/timeline.json acts}
Audience questions this video answers (use their words): {X, Y, Z}
Description keywords: {keywords}

**(f) Attached frames:** {frames} — the best frames of the finished video; use them as the visual reference and background.

Return: three titles (mark your pick), the full description (2 search lines → summary → chapters → a line that is exactly `[METHOD AND SOURCES]` — Crux pastes its sourced method block there → disclaimers), ≤ 5 tags, and the thumbnail image.
