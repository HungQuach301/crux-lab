# Packaging brief — Episode {N}: {working title}
<!-- Mẫu (Phiên Thị trường bước 7). P3 sinh bản điền sẵn bằng `python3 toolkit/market/brief.py episodes/epNNN --topic <id hồ sơ cầu>`
     → episodes/epNNN/out/package/PACKAGING-BRIEF.md, gửi kèm gói G2. Tiếng Anh, ≤ 1 trang, chủ dự án dán NGUYÊN khối dưới vạch vào ChatGPT,
     đính kèm 2–3 ảnh nền bg-*.png. ChatGPT làm tiêu đề, mô tả, thumbnail; chủ dự án dán kết quả vào prompt P4 (cùng câu trả lời G2);
     P4 kiểm bằng toolkit/market/package_check.py (S21, claim-risk, chương khớp timeline, chữ trên ảnh). -->
---
You are packaging one YouTube video for **Crux**, a US personal-finance channel that replays real history with data. Make: 3 titles, 1 description, 1 thumbnail (1280×720) on one of the attached background frames.

**Episode.** {2–3 sentences: the viewer question, what was replayed (series, years), the answer in plain words, the guide character.}

**Allowed numbers — use only these, exactly as written:** {display list from out/claims.json}. Any other number, dollar amount or year is forbidden.
**Rules (hard):** say "history, not a forecast" and "US only" in the description · characters are ILLUSTRATIVE (write the word next to any character figure) · no advice (no "you should", "best", "do this"), no prediction ("will", "next year") · no dollar amount without a source above · no "your loan/your money will…" (use "a buyer who…").

**Chapters (paste exactly):**
{0:00 … from out/timeline.json acts}

**Title frames that win in this niche** (pick 3, fill with the allowed numbers; ≤ 60 characters):
1. {frame 1}
2. {frame 2}
3. {frame 3}

**Thumbnail:** {winning style from market/REPORT.md §3}. Max **{3–4} large words**; one idea; readable at phone size (168×94). Use an attached frame as the background (3D world, faceless figures, money stacks). Colors: background #0E1116, text #F2F4F7, accent #4C8DFF, warn #F2B441, positive #3FBF7F, negative #E5484D. Font: Inter Bold. No faces, no logos, no arrows that imply a prediction.

**Description keywords** (first 2 lines, ~150 characters, must contain the first keyword): {keywords}

**Audience questions this video answers** (use their words in the title/description): {X, Y, Z}

Return: three titles (mark your pick), the full description (summary paragraph → chapters → a line that is exactly `[METHOD AND SOURCES]` — Crux pastes its sourced method block there → disclaimers), and the thumbnail image.
