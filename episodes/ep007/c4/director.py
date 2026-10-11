"""Tập 7 · C4/C5 · lượt đạo diễn máy trên bản cả tập (chẩn đoán, không ngưỡng — QF §10; chép c3/director.py): headless Opus khoá Console,
0 agent con, ≤ 10 khung mỗi lượt (≤ 2 cảnh × 5 khung).
  python3 c4/director.py <video> <outdir> <cảnh>[,<cảnh>] [<cảnh>,<cảnh> …]   # mỗi đối số = một lượt độc lập
Khung: 5 mốc đều trong khoảng cảnh (out/factory/timeline.json); đầu bài = ý đồ beats.md (muted read / job) + lời + mốc từ (giây của cảnh)."""
import json, re, subprocess, sys, concurrent.futures as cf
from pathlib import Path
EP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(EP)); import blind  # noqa: E402
TL = json.load(open(EP / 'out/factory/timeline.json'))
SC = {s['id']: s for s in TL['scenes']}
AX = ("Score each scene 1–5 on four axes: (1) emotion/story, (2) understood with sound off, (3) pacing (dead time, late cues), "
      "(4) composition / eye-line / text legibility. Then give at most 4 concrete notes per scene, each with a time in seconds (scene time), what is "
      "wrong, and a fix that changes the picture (not a label) when possible. Diagnostic only. Plain text, ≤ 350 words.")


def beats():
    out = {}
    for ln in open(EP / 'story/beats.md', encoding='utf-8'):
        if ln.startswith('| B'):
            c = [x.strip() for x in ln.strip().strip('|').split('|')]
            out[c[1]] = c[5].strip('"“” ')
    return out


def one(video, o, scenes):
    bt = beats()
    parts = ["You are a film director reviewing silent-frame samples of scenes from a 3D explainer episode for a faceless US personal-finance YouTube "
             "channel (low-poly world, faceless illustrative characters). For each scene you get the intended picture, the narration with word "
             "times, and 5 frames. Use the Read tool to open exactly the listed PNG files and nothing else.\n"]
    for sid in scenes:
        s = SC[sid]; a, d = s['start'], s['dur']
        words = ' '.join(f"{w['w']}@{w['s'] - a:.1f}" for w in TL['words'] if a <= w['s'] < a + d) if TL.get('words') and 'w' in TL['words'][0] else ''
        narr = ' '.join(x['text'] for x in TL['sentences'] if x['scene'] == sid)
        fr = []
        for i in range(5):
            t = round(d * (i + 0.5) / 5, 2); p = o / f'{sid}-{i + 1}.png'
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{a + t:.3f}', '-i', str(video), '-frames:v', '1', str(p)], check=True)
            fr.append((t, p))
        parts.append(f"## Scene {sid} ({d:.1f} s)\nIntended picture: {bt.get(sid, '')}\nNarration: {narr}\n" + (f"Word times: {words}\n" if words else '')
                     + '\n'.join(f"- frame at {t} s: {p}" for t, p in fr))
    parts.append(AX)
    name = '+'.join(scenes); (o / f'{name}.txt').write_text('\n\n'.join(parts))
    return name, blind.run(o / f'{name}.txt', o / f'{name}.json', read=True, model='opus')


if __name__ == '__main__':
    video = Path(sys.argv[1]).resolve(); o = Path(sys.argv[2]).resolve(); o.mkdir(parents=True, exist_ok=True)
    with cf.ThreadPoolExecutor(3) as ex:
        for name, r in ex.map(lambda x: one(video, o, x.split(',')), sys.argv[3:]):
            print('=====', name, r and r.get('cost_usd')); print(r and r['answer'])
