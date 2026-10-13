"""Tập 7 · C3 · lượt đạo diễn máy (chẩn đoán, không ngưỡng — QF §10): headless Opus khoá Console, 0 agent con, ≤ 10 khung mỗi lượt.
  python3 c3/director.py <outdir> <đoạn>[,<đoạn>] [<đoạn>,<đoạn> …]   # mỗi đối số = một lượt (≤ 2 đoạn × 5 khung)
Khung: 5 mốc đều (tâm 5 lát) của clip 540p `world/c3/out/<đoạn>.mp4`; đầu bài = ý đồ beats.md + lời + mốc từ spine.json."""
import json, os, subprocess, sys, concurrent.futures as cf
from pathlib import Path
EP = Path(__file__).resolve().parents[1]; ROOT = EP.parents[1]
sys.path.insert(0, str(EP)); import blind  # noqa: E402
SP = json.load(open(EP / 'world/c3/spans.json'))['strips']
AX = ("Score each segment 1–5 on four axes: (1) emotion/story, (2) understood with sound off, (3) pacing (dead time, late cues), "
      "(4) composition / eye-line / text legibility. Then give at most 4 concrete notes per segment, each with a time in seconds, what is wrong, and a fix "
      "that changes the picture (not a label) when possible. Diagnostic only. Plain text, ≤ 350 words.")


def frames(seg, o):
    clip = EP / f'world/c3/out/{seg}.mp4'
    dur = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(clip)]))
    out = []
    for i in range(5):
        t = round(dur * (i + 0.5) / 5, 2); p = o / f'{seg}-{i + 1}.png'
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(t), '-i', str(clip), '-frames:v', '1', str(p)], check=True)
        out.append((t, p))
    return dur, out


def one(o, segs):
    parts = ["You are a film director reviewing short silent-frame samples of 3D explainer segments for a faceless US personal-finance YouTube "
             "channel (low-poly world, faceless illustrative characters). For each segment you get the intended picture, the narration with word "
             "times, and 5 frames. Use the Read tool to open exactly the listed PNG files and nothing else.\n"]
    for seg in segs:
        k = next(v for v in SP.values() if v['segment'].endswith(seg))
        sp = json.load(open(ROOT / k['segment'] / 'spine.json'))
        words = ' '.join(f"{w['w']}@{w['s']:.1f}" for w in sp['words'])
        dur, fr = frames(seg, o)
        parts.append(f"## Segment {seg} ({dur:.1f} s)\nIntended picture: {k['muted_read']}\nNarration: {' '.join(k['narration'])}\nWord times: {words}\n"
                     + '\n'.join(f"- frame at {t} s: {p}" for t, p in fr))
    parts.append(AX)
    name = '+'.join(segs); (o / f'{name}.txt').write_text('\n\n'.join(parts))
    return name, blind.run(o / f'{name}.txt', o / f'{name}.json', read=True, model='opus')


if __name__ == '__main__':
    o = Path(sys.argv[1]).resolve(); o.mkdir(parents=True, exist_ok=True)
    with cf.ThreadPoolExecutor(3) as ex:
        for name, r in ex.map(lambda a: one(o, a.split(',')), sys.argv[2:]):
            print('=====', name, r and r.get('cost_usd')); print(r and r['answer'])
