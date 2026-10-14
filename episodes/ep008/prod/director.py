"""Tập 8 · M5 · lượt đạo diễn máy trên nháp cả tập (chẩn đoán, D-010 §6; ý đồ gates/M5-intent.md §5 + P10) — chép rút gọn ep007 c4/director.py.
Một lượt headless khoá Console, 0 agent con: 4 tấm × 12 khung theo hồi (cùng tấm của bài nhớ lại, prod/recall.py sheets) + lời có mốc giây.
  python3 prod/director.py <run>          # đọc review-m5/<run>/sheet{1..4}.png + narration.txt → review-m5/<run>/director.{txt,json,md}
Lời phê chỉ thành việc sửa khi phép thử của vai sở hữu cũng trượt ở đúng chỗ đó (episode.md §1a)."""
import json, sys
from pathlib import Path
EP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(EP)); import blind  # noqa: E402
import yaml  # noqa: E402

AX = ("Score each of the four parts 1–5 on four axes: (1) emotion/story, (2) understood with sound off, (3) pacing (dead time, late cues, "
      "motion that means nothing), (4) composition / eye-line / text legibility. Then give at most 4 concrete notes per part, each with a time "
      "in seconds (episode time), what is wrong, and a fix that changes the picture (not a label) when possible. Diagnostic only. Plain text, ≤ 500 words.")


def main(run):
    o = EP / 'review-m5' / run
    tl = json.load(open(EP / 'out/factory/timeline.json')); S = {s['id']: s for s in tl['scenes']}
    acts = {a['id']: a['scenes'] for a in yaml.safe_load(open(EP / 'episode.yaml'))['acts']}
    groups = [['cold-open', 'act1'], ['act2'], ['act3'], ['limits']]
    parts = ["You are a film director reviewing a full 3D explainer episode (about 10 minutes) for a faceless US personal-finance YouTube channel "
             "(low-poly world, faceless illustrative characters, a street where each house is one start month). You get four contact sheets of 12 "
             "frames each, one per part, in time order, plus the full narration with times. Use the Read tool to open exactly the four listed PNG "
             "files and the narration file, nothing else.\n"]
    for k, g in enumerate(groups):
        sc = [S[s] for a in g for s in acts[a]]
        t0, t1 = min(s['start'] for s in sc), max(s['start'] + s['dur'] for s in sc)
        ts = ', '.join(f'{i + 1}={t0 + (i + 0.5) * (t1 - t0) / 12:.0f}s' for i in range(12))
        parts.append(f"- Part {k + 1} ({t0:.0f}–{t1:.0f} s): {o / f'sheet{k + 1}.png'} — frame numbers → times: {ts}")
    parts.append(f"- Narration with times: {o / 'narration.txt'}")
    parts.append(AX)
    (o / 'director.txt').write_text('\n'.join(parts))
    r = blind.run(o / 'director.txt', o / 'director.json', read=True, model='opus')
    (o / 'director.md').write_text(f"# Lượt đạo diễn (chẩn đoán) — {run}\n\nchi ${r.get('cost_usd')}\n\n{r['answer']}\n")
    print(r.get('cost_usd')); print(r['answer'])


if __name__ == '__main__':
    main(sys.argv[1])
