"""Review clip (M1b): the first seconds of the planned edit (cold open, ident, act 1 with the rehook) as an animatic:
table-read voice on the planned timeline, one storyboard frame (or a picture card) per scene, narration as a caption,
and the data sounds in the owner's chosen palette S2 ('minimal', toolkit/audio/sonify_palettes.py) on the planned chart
events of each shot (shotlist `sonify`: dot / bar / counter at the change, line over the first 1.5 s), with the same
voice side-chain, 1-4 kHz carve and syllable-gap placement as the blind test. Picture = storyboard, not the film.

    python3 episodes/ep001/preprod/animatic.py [seconds=80] [out dir=review-m1b]
"""
import json
import os
import shutil
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
sys.path.insert(0, os.path.join(EP, '..', '..', 'toolkit', 'audio'))
import storyboard as SB  # noqa: E402
import sonify_palettes as SP  # noqa: E402

SR = 48000
LIMIT = float(sys.argv[1]) if len(sys.argv) > 1 else 80.0
OUTDIR = os.path.join(EP, sys.argv[2] if len(sys.argv) > 2 else 'review-m1b')
FN = {sc: fn for sc, _, fn in SB.FRAMES}
FN.update({'co-rate': SB.f_maya, 'co-question': SB.f_bill, 'a1-dan': SB.f_three, 'a1-dan2': SB.f_three, 'a1-dan3': SB.f_three, 'a1-priya': SB.f_three,
           'a1-priya2': SB.f_three, 'a1-priya3': SB.f_three, 'a1-you': SB.f_today})


def card(ax, shot):
    SB.frame(ax)
    ax.text(8, 5.6, shot['layout'], ha='center', fontsize=11, color=SB.MUT)
    for i, line in enumerate(textwrap.wrap(shot['picture'], 60)[:4]):
        ax.text(8, 4.6 - i * 0.6, line, ha='center', fontsize=10, color=SB.INK)


def main():
    tl = json.load(open(os.path.join(HERE, 'timeline-plan.json')))
    shots = {s['scene']: s for s in json.load(open(os.path.join(HERE, 'shotlist.json')))['shots']}
    takes = {t['id']: t for t in json.load(open(os.path.join(EP, 'out', 'voice', 'takes.json')))['takes']}
    work = os.path.join(EP, 'work', 'animatic-m1b')
    shutil.rmtree(work, ignore_errors=True); os.makedirs(work)
    os.makedirs(OUTDIR, exist_ok=True)
    scenes = [s for s in tl['scenes'] if s['start'] < LIMIT]
    sub = {s['scene']: s['text'] for s in tl['sentences']}
    lst = []
    for i, sc in enumerate(scenes):
        fig = plt.figure(figsize=(19.2, 10.8), dpi=100, facecolor=SB.BG)
        ax = fig.add_axes([0, 0.12, 1, 0.88])
        if sc['id'] == 'ident':
            SB.frame(ax); ax.text(8, 4.5, 'CRUX  ·  decision lab', ha='center', fontsize=28, fontweight='bold', color=SB.INK)
        else:
            (FN.get(sc['id']) or (lambda a: card(a, shots[sc['id']])))(ax)
        fig.text(0.5, 0.06, '\n'.join(textwrap.wrap(sub.get(sc['id'], ''), 90)), ha='center', va='center', fontsize=20, color=SB.INK)
        fig.text(0.015, 0.975, f"{sc['id']}  ·  {sc['start']:.1f} s  ·  {sc['shot']}  ·  {sc['move']}", fontsize=12, color=SB.WARN, va='top')
        fig.text(0.985, 0.975, 'M1b animatic: storyboard + table read + data sounds S2, not the film', fontsize=12, color=SB.MUT, va='top', ha='right')
        p = os.path.join(work, f'f{i:03d}.png'); fig.savefig(p, facecolor=SB.BG); plt.close(fig)
        dd = min(sc['start'] + sc['dur'], LIMIT) - sc['start']
        lst.append(f"file '{p}'\nduration {dd:.3f}")
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
    # planned chart events -> S2 data sounds (same rules as the blind test)
    fps, ev = 30, {'fps': 30, 'line': [], 'dot': [], 'bar': [], 'tick': []}
    for sc in scenes:
        t0 = sc['start'] + 0.25
        for e in shots.get(sc['id'], {}).get('sonify', []):
            if e == 'dot':
                ev['dot'].append({'f': int(t0 * fps), 'id': sc['id'], 'x': 960, 'y': 420})
            elif e == 'bar':
                ev['bar'].append({'f0': int(t0 * fps), 'f1': int((t0 + 0.6) * fps), 'x': 900, 'value': 0.5, 'chart': sc['id']})
            elif e == 'counter':
                ev['tick'] += [{'f': int((t0 + k * 0.12) * fps), 'x': 960} for k in range(6)]
            elif e == 'line':
                ev['line'] += [{'f': int(t0 * fps) + k, 'id': sc['id'] + '-line', 'slope': 0.4 * np.sin(k / 8), 'x': 400 + 20 * k} for k in range(45)]
    root = os.path.join(work, 'root')
    os.makedirs(os.path.join(root, 'out', 'audio', 'stems'))
    json.dump(ev, open(os.path.join(root, 'out', 'sonify-events.json'), 'w'))
    sf.write(os.path.join(root, 'out', 'audio', 'stems', 'voice.flac'), v, SR)
    SP.process(root, 'minimal', os.path.join(work, 'son.wav'))
    son, _ = sf.read(os.path.join(work, 'son.wav'), always_2d=True)
    son = son[:N]
    mix = np.stack([v, v], 1)[:len(son)] + son
    wav = os.path.join(work, 'mix.wav'); sf.write(wav, mix, SR)
    out = os.path.join(OUTDIR, f'animatic-0000-{int(LIMIT):04d}.mp4')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', os.path.join(work, 'list.txt'), '-i', wav,
                    '-vf', 'scale=1280:720,fps=30,format=yuv420p', '-c:v', 'libx264', '-preset', 'medium', '-crf', '26', '-af', 'loudnorm=I=-16:TP=-1.5',
                    '-c:a', 'aac', '-b:a', '128k', '-t', str(LIMIT), '-movflags', '+faststart', out], check=True)
    print(out, os.path.getsize(out) // 1024, 'KB', '| events', {k: len(x) for k, x in ev.items() if k != 'fps'})


if __name__ == '__main__':
    main()
