"""Episode 1 M1 edit plan from the table-read takes.

    python3 episodes/ep001/preprod/edit.py

Reads out/voice/takes.json (final clips = raw takes trimmed, no stretching), out/script-draft.json, preprod/shotlist.json.
Writes:
  work/table-read.wav + review-m1/table-read-full.m4a   continuous reading, every gap <= 0.8 s (M1 item 3)
  preprod/timeline-plan.json                            planned edit timeline (picture lead, ident, pauses, ad breaks, outro)
  edit/cues.json, preprod/cue-sheet.md                  music cues, intentional silences, sound design, sonification plan
  preprod/tension-map.json + .png                       planned tension curve (targets, not measurements)
  preprod/shotlist.md, preprod/color-script.md
"""
import json
import os
import subprocess

import numpy as np
import soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.join(HERE, '..')
SR = 48000
J = lambda p: json.load(open(os.path.join(EP, p)))

GAP_READ = 0.35          # table read: between sentences
GAP_READ_ACT = 0.75      # table read: between acts (still <= 0.8 s)
LEAD = 0.9               # cold open: picture before words (Maya's card)
GAP_COLD = 0.3           # between the short cold-open lines
IDENT = 3.0
GAP = 0.45               # edit: between sentences
DECISIVE_PAUSE = 1.2     # after a sentence that says a decisive number (DX-R3 >= 1.0 s)
SILENCES = {'a1-median': (1.2, 'Maya\'s bill is the national median: let it land'), 'a2-real': (1.3, 'the thesis lands: 24 becomes 30'),
            'a3-answer2': (1.3, 'the answer lands'), 'a1-payoff': (1.6, 'end of act 1: ad break'), 'a2-payoff': (1.6, 'end of act 2: ad break')}
OUTRO_HOLD = 12.0        # end screen after the last line (outro >= 20 s)
MUSIC = {'cold-open': ('A minor', 72, 'suspense under the open question; pad + pulse, no melody'),
         'ident': ('A minor', 72, 'ident sting'),
         'act1': ('C major', 84, 'curious, light pulse; the three households get motifs (Dan: low plucks, Maya: piano, Priya: high bells)'),
         'act2': ('D minor', 92, 'building to the thesis (a2-real: 24 becomes 30), valley after it; re-voiced at Dan\'s and Priya\'s positions'),
         'act3': ('F major', 88, 'history: darker at the further-drop turn, resolves on the answer'),
         'method': ('F major', 70, 'thin pad under the method card'),
         'outro': ('C major', 76, 'resolved; both motifs together')}
CLIMAX = {'act1': 'a1-turn', 'act2': 'a2-real', 'act3': 'a3-answer2'}


def dur(path):
    i = sf.info(path)
    return i.frames / i.samplerate


def main():
    draft = J('out/script-draft.json')['sentences']
    takes = {t['id']: t for t in J('out/voice/takes.json')['takes']}
    shots = {s['scene']: s for s in J('preprod/shotlist.json')['shots']}
    claims = {c['claimId']: c for c in J('out/claims.json')['claims']}
    choice = J('out/voice/choice-report.json')
    wpm = {r['id']: r['chosen']['wpm'] for r in choice['sentences']}
    D = {s['id']: dur(os.path.join(EP, takes[s['id']]['final'])) for s in draft}
    # cold open: cut the breath/decay after the last word at ASR end + 250 ms (the same cut toolkit/audio/d_m2_audio.py makes
    # after decisive lines; trimming, not stretching). M2 must apply it in the voice stem too (timeline-plan.json: tailCut).
    EL = J('out/voice/el-takes.json')
    TAIL = {}
    for s in draft:
        if s['act'] == 'cold-open':
            rec = EL.get(os.path.basename(takes[s['id']]['raw'])[:-4])
            if rec and rec.get('words'):
                cut = 0.03 + rec['words'][-1]['end'] + 0.25
                if cut < D[s['id']]:
                    TAIL[s['id']] = round(cut, 3); D[s['id']] = cut

    # 1) continuous table read
    parts, t, prev_act, tr = [], 0.0, None, []
    for s in draft:
        if prev_act and s['act'] != prev_act:
            g = GAP_READ_ACT
        else:
            g = GAP_READ if prev_act else 0.3
        parts.append(np.zeros(int(g * SR))); t += g
        x, sr = sf.read(os.path.join(EP, takes[s['id']]['final']), always_2d=False)
        if x.ndim > 1:
            x = x.mean(1)
        if sr != SR:
            raise SystemExit('unexpected sample rate')
        tr.append({'id': s['id'], 'start': round(t, 3), 'end': round(t + len(x) / SR, 3)})
        parts.append(x); t += len(x) / SR
        prev_act = s['act']
    parts.append(np.zeros(int(0.5 * SR)))
    y = np.concatenate(parts)
    os.makedirs(os.path.join(EP, 'work'), exist_ok=True)
    os.makedirs(os.path.join(EP, 'review-m1b'), exist_ok=True)
    sf.write(os.path.join(EP, 'work', 'table-read.wav'), y, SR)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', os.path.join(EP, 'work', 'table-read.wav'), '-af', 'loudnorm=I=-16:TP=-1.5', '-c:a', 'aac', '-b:a', '128k',
                    os.path.join(EP, 'review-m1b', 'table-read-full.m4a')], check=True)
    gaps = [b['start'] - a['end'] for a, b in zip(tr, tr[1:])]
    json.dump({'sentences': tr, 'maxGap': round(max(gaps), 3), 'duration': round(len(y) / SR, 2)}, open(os.path.join(EP, 'work', 'table-read.json'), 'w'), indent=1)

    # 2) planned edit timeline
    decisive = {sp['sentence'] for c in claims.values() if c.get('decisive') for sp in c['spoken']}
    t, scenes, acts, sents, prev = 0.0, [], [], [], None
    for s in draft:
        if s['act'] != prev:
            if prev == 'cold-open':
                acts.append({'id': 'ident', 'start': round(t, 3)}); scenes.append({'id': 'ident', 'act': 'ident', 'start': round(t, 3), 'dur': IDENT}); t += IDENT
            acts.append({'id': s['act'], 'start': round(t, 3)})
            if s['act'] == 'cold-open':
                t += LEAD
            prev = s['act']
        if s['scene'] == 'a1-rehook' and t < 30.3:
            t = 30.3  # a breath before the promise: the rehook starts inside 0:30-0:45 (DX-S4)
        st = t
        t += D[s['id']]
        sents.append({'id': s['id'], 'scene': s['scene'], 'text': s['text'], 'start': round(st, 3), 'end': round(t, 3)})
        pause = GAP_COLD if s['act'] == 'cold-open' else GAP
        if s['scene'] == 'co-question':
            pause = 0.0  # the ident starts on the question's last syllable decay
        if s['id'] in decisive:
            pause = max(pause, DECISIVE_PAUSE)
        if s['scene'] in SILENCES:
            pause = max(pause, SILENCES[s['scene']][0] + 0.3)
        t += pause
        scenes.append({'id': s['scene'], 'act': s['act'], 'start': round(st if scenes else 0.0, 3)})
    t += OUTRO_HOLD
    for i, sc in enumerate(scenes):
        nxt = scenes[i + 1]['start'] if i + 1 < len(scenes) else t
        if sc['id'] != 'ident':
            sc['dur'] = round(nxt - sc['start'], 3)
        sh = shots[sc['id']]
        sc.update({'layout': sh['layout'], 'shot': sh['size'], 'move': sh['move'], 'sonify': sh['sonify']})
    for i, a in enumerate(acts):
        a['end'] = acts[i + 1]['start'] if i + 1 < len(acts) else round(t, 3)
        if a['id'] in CLIMAX:
            a['climax'] = next(x['start'] for x in scenes if x['id'] == CLIMAX[a['id']])
    total = round(t, 3)
    json.dump({'fps': 30, 'total': total, 'acts': acts, 'scenes': scenes, 'sentences': sents, 'tailCut': TAIL, 'note': 'PLANNED at M1 from the table-read takes; M2 re-times from the final takes'},
              open(os.path.join(HERE, 'timeline-plan.json'), 'w'), indent=1)

    # 3) cues + silences + sonification counts
    cues = []
    for a in acts:
        k, bpm, fn = MUSIC[a['id']]
        cues.append({'t': a['start'], 'end': a['end'], 'function': fn, 'key': k, 'tempo': bpm, 'layer': 'music'})
    for a in acts:
        if 'climax' in a:
            cues.append({'t': round(a['climax'] - 20, 2), 'end': a['climax'], 'function': f"build to the {a['id']} climax (+6 dB over 20 s)", 'key': MUSIC[a['id']][0], 'tempo': MUSIC[a['id']][1], 'layer': 'music-dynamics'})
    sil = []
    for s in sents:
        if s['scene'] in SILENCES:
            sil.append({'t': round(s['end'] + 0.08, 3), 'dur': SILENCES[s['scene']][0], 'why': SILENCES[s['scene']][1], 'after': s['id']})
    breaks = [x for x in sil if 'ad break' in x['why']]
    os.makedirs(os.path.join(EP, 'edit'), exist_ok=True)
    json.dump({'cues': cues, 'silences': sil, 'adBreaks': [{'t': round(x['t'] + x['dur'] / 2, 3), 'after': x['after']} for x in breaks]},
              open(os.path.join(EP, 'edit', 'cues.json'), 'w'), indent=1)
    son_count = {}
    for sc in scenes:
        for e in sc['sonify']:
            son_count[e] = son_count.get(e, 0) + 1
    SH = J('preprod/shotlist.json')
    L = ['# Episode 1 — cue sheet (M1 plan)', '', f'Planned length **{total / 60:.2f} min** ({total:.1f} s) from the table-read takes. Music is generated in code (toolkit/audio/d_m2_audio.py, one reverb space, per-act arrangement); no third-party audio.', '',
         '## Music cues', '', '| t (s) | end | layer | key | tempo | dramatic function |', '|---|---|---|---|---|---|']
    L += [f"| {c['t']:.1f} | {c['end']:.1f} | {c['layer']} | {c['key']} | {c['tempo']} | {c['function']} |" for c in cues]
    L += ['', '## Intentional silences (DX-R6: ~300 ms release in, room tone floor, back in 200 ms)', '', '| t (s) | length | after | why |', '|---|---|---|---|']
    L += [f"| {x['t']:.2f} | {x['dur']} s | `{x['after']}` | {x['why']} |" for x in sil]
    ab = ', '.join('%.1f s' % b['t'] for b in json.load(open(os.path.join(EP, 'edit', 'cues.json')))['adBreaks'])
    L += ['', f"Ad breaks (DX-S10): {ab}, inside the act1|act2 and act2|act3 silences.", '',
          '## Sound design', '', '- whoosh per camera move, level from peak speed (A10); riser into each reveal; impact on the decisive numbers (`cost_med`, `sp36_mid`); room tone throughout.',
          '- every spoken number: music and sfx dip from 0.5 s before to 1.6 s after (DX-A6); the data sounds follow the voice side-chain below.', '',
          '## Data sonification plan (DX-A1, sổ gu G-001, G-005, G-006), per element type', '',
          'Timbre: **S2**, chosen by the owner in the blind test on a phone speaker (sổ gu G-005, 2026-09-28): palette `minimal` of `toolkit/audio/sonify_palettes.py`, soft filtered tick + low pulse. "S2 không lấn lời."', '',
          '| element | timbre | value mapping | pan | timing | scenes using it |', '|---|---|---|---|---|---|']
    L += [f"| {r['element']} | {r['sound']} | {r['mapping']} | {r['pan']} | {r['timing']} | {son_count.get(r['element'], 0)} |" for r in SH['sonification']]
    L += ['', '### Heard without covering the voice', ''] + [f'- {x}' for x in SH['separation']]
    L += ['', 'Measured on the 10 s sample, blind palettes (review-m1/sonify-metrics.json): data layer about -21 dB under the voice; 1-4 kHz while speaking 31-56 dB under the voice; T1-style lift median 0 dB (up to 6.6 dB in voice pauses). The m0 version at +10 dB (-6 dB under the voice) was judged by the owner to cover the voice.']
    open(os.path.join(HERE, 'cue-sheet.md'), 'w').write('\n'.join(L) + '\n')

    # 4) planned tension map (targets): cut rate from scene lengths, music level from the cue plan, density from layers
    ts = np.arange(0, total, 1.0)
    starts = np.array([s['start'] for s in scenes])
    cut = np.array([((starts > x - 5) & (starts <= x + 5)).sum() for x in ts], float)
    ten = np.zeros_like(ts)
    for a in acts:
        if 'climax' in a:
            c = a['climax']
            ten += np.clip(1 - np.abs(ts - c) / 25, 0, 1) * (ts <= c) + np.clip(1 - (ts - c) / 8, 0, 1) * (ts > c) * 0.3
    ten = 0.4 * cut / max(cut.max(), 1) + 0.6 * ten
    peaks = [{'t': a['climax'], 'act': a['id']} for a in acts if 'climax' in a]
    valleys = [{'t': round(p['t'] + 10, 1)} for p in peaks]
    json.dump({'samples': [{'t': float(x), 'cutRate': float(c), 'tension': round(float(v), 3)} for x, c, v in zip(ts, cut, ten)], 'peaks': peaks, 'valleys': valleys,
               'note': 'PLANNED targets at M1; M2 measures cut rate, music level and audio density from the edit and stems (toolkit/audio/d_tension.py)'},
              open(os.path.join(HERE, 'tension-map.json'), 'w'), indent=1)
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(12, 3.2), dpi=100)
    ax.plot(ts, ten, color='#4c8dff'); ax.set_xlim(0, total); ax.set_ylim(0, 1.05)
    for a in acts:
        ax.axvline(a['start'], color='#9aa4b2', lw=0.6); ax.text(a['start'] + 2, 1.0, a['id'], fontsize=7, color='#555')
    for p in peaks:
        ax.plot(p['t'], np.interp(p['t'], ts, ten), 'v', color='#e5484d')
    for x in sil:
        ax.axvspan(x['t'], x['t'] + x['dur'], color='#f2b441', alpha=0.4, lw=0)
    ax.set_xlabel('seconds'); ax.set_title('Episode 1 — planned tension (peaks at the act climaxes, amber = intentional silences)', fontsize=9)
    fig.tight_layout(); fig.savefig(os.path.join(HERE, 'tension-map.png')); plt.close(fig)

    # 5) human-readable shot list + colour script
    L = ['# Episode 1 — shot list (M1)', '', 'Every shot: size, camera move, reason (DX-V8, DX-V12). Planned times from the table read. Data sounds: element types that change in the shot.', '',
         '| # | t (s) | scene | layout | size | move | reason | picture | data sounds |', '|---|---|---|---|---|---|---|---|---|']
    tmap = {s['id']: s['start'] for s in scenes}
    for s in SH['shots']:
        L.append(f"| {s['id']} | {tmap.get(s['scene'], 0):.1f} | `{s['scene']}` | {s['layout']} | {s['size']} | {s['move']} | {s['moveReason']} | {s['picture']} | {', '.join(s['sonify']) or '—'} |")
    open(os.path.join(HERE, 'shotlist.md'), 'w').write('\n'.join(L) + '\n')
    CS = ['# Episode 1 — colour script', '', 'All colours are channel tokens (`design/tokens.json`). One grade for the whole film; light fixed grain and vignette.', '',
          '| act | background | lead colour | feeling |', '|---|---|---|---|',
          '| cold open | bg | accent (new payment) against negative (the bill) | a gain with a price |',
          '| act 1 | bg | ink data, amber SMALL / blue LARGE introduced | inventory, calm |',
          '| act 2 | bg, surface panels for the curve | ink curve; amber and blue curves at the turn; positive/negative shading at the flip | tension rises to the cliff |',
          '| act 3 | bg | accent rate line, grey ILLUSTRATIVE bars pre-2018, negative marks for "next point came first" | history, weight |',
          '| method | surface | ink-muted text | quiet |', '| outro | bg | ink + accent | resolved |']
    open(os.path.join(HERE, 'color-script.md'), 'w').write('\n'.join(CS) + '\n')
    acts_wpm = choice['acts']
    print(json.dumps({'tableRead': round(len(y) / SR, 1), 'maxGap': round(max(gaps), 3), 'plannedTotal': total, 'acts': {a['id']: round(a['end'] - a['start'], 1) for a in acts},
                      'actWpm': acts_wpm, 'fastSentences': sorted([(k, v) for k, v in wpm.items() if v and v > 190], key=lambda x: -x[1])[:10]}, indent=1))


if __name__ == '__main__':
    main()
