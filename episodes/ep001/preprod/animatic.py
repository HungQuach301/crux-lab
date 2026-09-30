"""Episode 1 animatic (Stage 4b, script v2) and the Gate B clip.

    python3 episodes/ep001/preprod/animatic.py

Picture = the storyboard frame of each scene (preprod/storyboard.py), the sentence on screen as a caption, timeline =
preprod/timeline-plan.json (V8 takes, script pauses, ident, card holds, end screen). Sound = the voice (final takes, no stretching)
+ the data sounds in the owner's palette S2 ('minimal', toolkit/audio/sonify_palettes.py) on the planned chart events of each shot
(shotlist `sonify`: dot / bar / counter at the change, a line over its first 1.5 s). G-006: the data layer keeps the palette's own
level (-16 dB under the voice, side-chain -8 dB, 1-4 kHz carved while the voice sounds); it is never raised. No music (M2).
Writes
  review-b/animatic-full.mp4  the whole film
  review-b/clip-b.mp4         Gate B clip: cold open + ident + re-hook (to the end of S04), then the act 1 turn (S13) if the total
                              stays <= 90 s; H.264 + AAC, 1280x720, faststart
  work/animatic/stems/{voice,sonify}.flac, work/animatic/sonify-events.json
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

SR, FPS = 48000, 30
OUT = os.path.join(EP, 'review-b')


def frame_png(path, scene, caption, header):
    fig = plt.figure(figsize=(12.8, 7.2), dpi=100, facecolor=SB.BG)
    ax = fig.add_axes([0, 0.13, 1, 0.87])
    SB.FR[scene](ax)
    if caption:
        fig.text(0.5, 0.065, '\n'.join(textwrap.wrap(caption, 95)[:3]), ha='center', va='center', fontsize=15, color=SB.INK)
    fig.text(0.012, 0.985, header, fontsize=9, color=SB.WARN, va='top')
    fig.text(0.988, 0.985, 'animatic: storyboard + V8 voice + S2 data sounds, not the film', fontsize=9, color=SB.MUT, va='top', ha='right')
    fig.savefig(path, facecolor=SB.BG); plt.close(fig)


def main():
    tl = json.load(open(os.path.join(HERE, 'timeline-plan.json')))
    takes = {t['id']: t for t in json.load(open(os.path.join(EP, 'out', 'voice', 'takes.json')))['takes']}
    work = os.path.join(EP, 'work', 'animatic')
    shutil.rmtree(work, ignore_errors=True); os.makedirs(os.path.join(work, 'f')); os.makedirs(os.path.join(work, 'stems'))
    os.makedirs(OUT, exist_ok=True)
    total = tl['total']
    # picture: a new still at every scene start and every sentence start/end (caption on while the sentence plays)
    cuts = []
    for sc in tl['scenes']:
        cuts.append((sc['start'], sc['id'], ''))
    for s in tl['sentences']:
        cuts.append((s['start'], s['scene'], s['text']))
        cuts.append((s['end'] + 0.25, s['scene'], ''))
    cuts.sort(key=lambda x: x[0])
    st = {s['id']: s for s in tl['scenes']}
    lst, cache = [], {}
    for i, (t0, sc, cap) in enumerate(cuts):
        # a sentence end must not move the picture back to an earlier scene
        t1 = cuts[i + 1][0] if i + 1 < len(cuts) else total
        if t1 <= t0:
            continue
        key = (sc, cap)
        if key not in cache:
            p = os.path.join(work, 'f', f'{len(cache):04d}.png')
            frame_png(p, sc, cap, f"{sc} · {st[sc]['act']} · {st[sc]['shot']} · {st[sc]['moveText']}")
            cache[key] = p
        lst.append(f"file '{cache[key]}'\nduration {t1 - t0:.3f}")
    lst.append(f"file '{cache[key]}'")
    open(os.path.join(work, 'list.txt'), 'w').write('\n'.join(lst) + '\n')
    # voice stem
    N = int(total * SR) + SR
    v = np.zeros(N)
    for s in tl['sentences']:
        x, _ = sf.read(os.path.join(EP, takes[s['id']]['final']), always_2d=False)
        x = x.mean(1) if x.ndim > 1 else x
        i0 = int(s['start'] * SR); v[i0:i0 + len(x)] += x[:N - i0]
    # planned chart events -> S2 (element types from the shot list; decisive sentences carry a dot at their start)
    ev = {'fps': FPS, 'line': [], 'dot': [], 'bar': [], 'tick': []}
    for sc in tl['scenes']:
        t0 = sc['start'] + 0.3
        for e in sc['sonify']:
            if e == 'dot':
                ev['dot'].append({'f': int(t0 * FPS), 'id': sc['id'], 'x': 960, 'y': 420})
            elif e == 'bar':
                ev['bar'].append({'f0': int(t0 * FPS), 'f1': int((t0 + 0.6) * FPS), 'x': 900, 'value': 0.5, 'chart': sc['id']})
            elif e == 'counter':
                ev['tick'] += [{'f': int((t0 + k * 0.12) * FPS), 'x': 960} for k in range(6)]
            elif e == 'line':
                ev['line'] += [{'f': int(t0 * FPS) + k, 'id': sc['id'] + '-line', 'slope': 0.4 * np.sin(k / 8), 'x': 400 + 20 * k} for k in range(45)]
    root = os.path.join(work, 'root')
    os.makedirs(os.path.join(root, 'out', 'audio', 'stems'))
    json.dump(ev, open(os.path.join(root, 'out', 'sonify-events.json'), 'w'))
    shutil.copy(os.path.join(root, 'out', 'sonify-events.json'), os.path.join(work, 'sonify-events.json'))
    sf.write(os.path.join(root, 'out', 'audio', 'stems', 'voice.flac'), v, SR)
    SP.process(root, 'minimal', os.path.join(work, 'son.wav'))
    son, _ = sf.read(os.path.join(work, 'son.wav'), always_2d=True)
    n = min(len(son), N)
    sf.write(os.path.join(work, 'stems', 'voice.flac'), np.stack([v, v], 1)[:n], SR)
    sf.write(os.path.join(work, 'stems', 'sonify.flac'), son[:n], SR)
    mix = np.stack([v, v], 1)[:n] + son[:n]
    wav = os.path.join(work, 'mix.wav'); sf.write(wav, mix, SR)
    full = os.path.join(OUT, 'animatic-full.mp4')
    enc = ['-c:v', 'libx264', '-preset', 'medium', '-crf', '28', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart']
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', os.path.join(work, 'list.txt'), '-i', wav,
                    '-vf', 'scale=1280:720,fps=30', '-af', 'loudnorm=I=-16:TP=-1.5', *enc, '-t', f'{total:.3f}', full], check=True)
    # Gate B clip
    mk = tl['marks']
    s04_end = next(s['start'] + s['dur'] for s in tl['scenes'] if s['id'] == 'S04')
    parts = [(0.0, s04_end)]
    s13 = next(s for s in tl['scenes'] if s['id'] == 'S13')
    turn = (next(s['start'] for s in tl['scenes'] if s['id'] == 'S12') + 0.0, s13['start'] + s13['dur'])
    if s04_end + (turn[1] - turn[0]) <= 90:
        parts.append(turn)
    elif s04_end + s13['dur'] <= 90:
        parts.append((s13['start'], s13['start'] + s13['dur']))
    segs = []
    for i, (a, b) in enumerate(parts):
        p = os.path.join(work, f'clip{i}.mp4')
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', f'{a:.3f}', '-i', full, '-t', f'{b - a:.3f}', *enc, p], check=True)
        segs.append(p)
    open(os.path.join(work, 'clip.txt'), 'w').write(''.join(f"file '{p}'\n" for p in segs))
    clip = os.path.join(OUT, 'clip-b.mp4')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', os.path.join(work, 'clip.txt'), *enc, clip], check=True)
    d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', clip], capture_output=True, text=True).stdout)
    info = {'full': full, 'fullSeconds': total, 'fullMB': round(os.path.getsize(full) / 2 ** 20, 1), 'clip': clip, 'clipSeconds': round(d, 2),
            'clipMB': round(os.path.getsize(clip) / 2 ** 20, 1), 'clipParts': [[round(a, 2), round(b, 2)] for a, b in parts], 'marks': mk,
            'events': {k: len(x) for k, x in ev.items() if k != 'fps'}}
    json.dump(info, open(os.path.join(OUT, 'clip-b.json'), 'w'), indent=1)
    print(json.dumps(info, indent=1))


if __name__ == '__main__':
    main()
