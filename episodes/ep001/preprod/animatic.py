"""Review clip for M1: the first 2 minutes of the planned edit (cold open, ident, act 1 with the rehook) as an animatic:
table-read voice placed on the planned timeline, one storyboard frame (or a picture card) per scene, narration as a
caption. Not a render of the film: picture = storyboard.

    python3 episodes/ep001/preprod/animatic.py [seconds=120]
"""
import json
import os
import subprocess
import sys
import textwrap

import numpy as np
import soundfile as sf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.join(HERE, '..')
sys.path.insert(0, HERE)
import storyboard as SB  # noqa: E402

SR = 48000
LIMIT = float(sys.argv[1]) if len(sys.argv) > 1 else 120.0
FN = {sc: fn for sc, _, fn in SB.FRAMES}
FN.update({'a1-rates': lambda a: SB.f_line(a, None), 'a1-low': lambda a: SB.f_line(a, None), 'a1-drops': lambda a: SB.f_line(a, 'episodes'),
           'a1-spread': SB.f_hist, 'a1-big': SB.f_bands, 'a1-turn': SB.f_bands, 'a1-keep': SB.f_bands})


def card(ax, sc, shot):
    SB.frame(ax)
    ax.text(8, 5.6, shot['layout'], ha='center', fontsize=11, color=SB.MUT)
    for i, line in enumerate(textwrap.wrap(shot['picture'], 60)[:4]):
        ax.text(8, 4.6 - i * 0.6, line, ha='center', fontsize=10, color=SB.INK)


def main():
    tl = json.load(open(os.path.join(HERE, 'timeline-plan.json')))
    shots = {s['scene']: s for s in json.load(open(os.path.join(HERE, 'shotlist.json')))['shots']}
    takes = {t['id']: t for t in json.load(open(os.path.join(EP, 'out', 'voice', 'takes.json')))['takes']}
    work = os.path.join(EP, 'work', 'animatic')
    os.makedirs(work, exist_ok=True)
    scenes = [s for s in tl['scenes'] if s['start'] < LIMIT]
    sub = {s['scene']: s['text'] for s in tl['sentences']}
    lst = []
    for i, sc in enumerate(scenes):
        fig = plt.figure(figsize=(19.2, 10.8), dpi=100, facecolor=SB.BG)
        ax = fig.add_axes([0, 0.12, 1, 0.88])
        if sc['id'] == 'ident':
            SB.frame(ax); ax.text(8, 4.5, 'CRUX  ·  decision lab', ha='center', fontsize=28, fontweight='bold', color=SB.INK)
        else:
            (FN.get(sc['id']) or (lambda a: card(a, sc['id'], shots[sc['id']])))(ax)
        fig.text(0.5, 0.06, '\n'.join(textwrap.wrap(sub.get(sc['id'], ''), 90)), ha='center', va='center', fontsize=20, color=SB.INK)
        fig.text(0.015, 0.975, f"{sc['id']}  ·  {sc['start']:.1f} s  ·  {sc['shot']}  ·  {sc['move']}", fontsize=12, color=SB.WARN, va='top')
        fig.text(0.985, 0.975, 'M1 animatic: storyboard + table read, not the film', fontsize=12, color=SB.MUT, va='top', ha='right')
        p = os.path.join(work, f'f{i:03d}.png'); fig.savefig(p, facecolor=SB.BG); plt.close(fig)
        d = min(sc['start'] + sc['dur'], LIMIT) - sc['start']
        lst.append(f"file '{p}'\nduration {d:.3f}")
    lst.append(f"file '{os.path.join(work, f'f{len(scenes) - 1:03d}.png')}'")
    open(os.path.join(work, 'list.txt'), 'w').write('\n'.join(lst) + '\n')
    N = int(LIMIT * SR)
    v = np.zeros(N)
    for s in tl['sentences']:
        if s['start'] >= LIMIT:
            continue
        x, _ = sf.read(os.path.join(EP, takes[s['id']]['final']), always_2d=False)
        i0 = int(s['start'] * SR); n = min(len(x), N - i0)
        v[i0:i0 + n] += x[:n]
    wav = os.path.join(work, 'voice.wav'); sf.write(wav, v, SR)
    out = os.path.join(EP, 'review-m1', f'animatic-0000-{int(LIMIT):04d}.mp4')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', os.path.join(work, 'list.txt'), '-i', wav,
                    '-vf', 'scale=1280:720,fps=30,format=yuv420p', '-c:v', 'libx264', '-preset', 'medium', '-crf', '26', '-af', 'loudnorm=I=-16:TP=-1.5',
                    '-c:a', 'aac', '-b:a', '128k', '-t', str(LIMIT), '-movflags', '+faststart', out], check=True)
    print(out, os.path.getsize(out) // 1024, 'KB')


if __name__ == '__main__':
    main()
