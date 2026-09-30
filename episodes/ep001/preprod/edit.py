"""Episode 1 edit plan (Stage 4b, script v2) from the V8 voice takes.

    python3 episodes/ep001/preprod/edit.py

Reads out/script-draft.json (story/script.md), out/voice/takes.json + el-takes.json + choice-report.json (final clips = raw takes
trimmed to the speech span, no time stretching), preprod/shotlist.json.
Writes:
  work/table-read.wav, review-b/table-read-full.m4a   continuous table read (0.35 s between sentences, 0.75 s between scenes)
  script/table-read-notes.md                          pace per act and sentence, key words, regenerated sentences and why, credits
  preprod/timeline-plan.json                          planned edit timeline (picture lead, ident, script pauses, card holds, end screen)
  out/timeline.json, out/script.json, out/adbreaks.json   contract files for the animatic timeline (checks/CONTRACT.md); the render
                                                      re-times them at M2
  edit/cues.json, preprod/cue-sheet.md, preprod/tension-map.json/.png, preprod/shotlist.md, preprod/color-script.md
"""
import json
import os
import re
import subprocess

import numpy as np
import soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.join(HERE, '..')
SR = 48000
J = lambda p: json.load(open(os.path.join(EP, p)))

LEAD = 0.9          # picture before the first word (Stage 4c: 1.5 -> 0.9 s to bring the cold open toward the approved ~20 s)
GAP = 0.45          # between sentences of a scene
GAP_COLD = 0.12     # cold open: between sentences, between its two scenes and into the ident (Stage 4c: 0.3/0.7 -> 0.12)
GAP_SCENE = 0.7     # between scenes
IDENT = 3.0
CARD_HOLD = {'S32.4': 5.0, 'S32.5': 5.0, 'S33.1': 16.0}   # on-screen-only card blocks (method card >= 12 s; history card 16 s)
MUSIC = {'cold-open': ('D minor', 72, 'suspense under the open question: pad and low pulse, no melody'),
         'ident': ('D minor', 72, 'ident sting over the long rate-line tone'),
         'act1': ('D minor', 84, 'curious, light pulse; Nora\'s motif (piano)'),
         'act2': ('D minor', 92, 'build through the balance gap to the quarter-point climax (S19), release on the full point'),
         'act3': ('F major', 88, 'Walt (low plucks), Anjali (high bells); resolves on the three-line answer (S29)'),
         'method': ('F major', 70, 'thin pad under the method cards'),
         'outro': ('F major', 76, 'resolved; three motifs together; tail into the end screen')}
CLIMAX = {'act1': 'S13', 'act2': 'S19', 'act3': 'S29'}
TURNS = {'S13': 'act 1 turn: neither answer is right; the division misses one line', 'S16': 'the missing line: $1,133 more owed at month 24',
         'S19': 'act 2 climax: at a quarter point the bill never comes back', 'S23': 'act 3 turn: the bill barely shrinks with the loan',
         'S29': 'the answer: a third of a point, half a point, more than one'}


def dur(path):
    i = sf.info(path)
    return i.frames / i.samplerate


def move_seconds(m):
    x = re.search(r'([\d.]+) s', m)
    return float(x.group(1)) if x else 0.0


def main():
    D0 = J('out/script-draft.json')
    rows, scenes_src = D0['sentences'], {s['id']: s for s in D0['scenes']}
    takes = {t['id']: t for t in J('out/voice/takes.json')['takes']}
    el = J('out/voice/el-takes.json')
    rep = J('out/voice/choice-report.json')
    shots = {s['scene']: s for s in J('preprod/shotlist.json')['shots']}
    lines = [r for r in rows if r['kind'] == 'line']
    D = {r['id']: dur(os.path.join(EP, takes[r['id']]['final'])) for r in lines}

    # 1) continuous table read
    parts, t, prev, tr = [], 0.3, None, []
    parts.append(np.zeros(int(0.3 * SR)))
    for r in lines:
        if prev is not None:
            g = 0.75 if r['scene'] != prev else 0.35
            parts.append(np.zeros(int(g * SR))); t += g
        x, sr = sf.read(os.path.join(EP, takes[r['id']]['final']), always_2d=False)
        x = x.mean(1) if x.ndim > 1 else x
        assert sr == SR
        tr.append({'id': r['id'], 'start': round(t, 3), 'end': round(t + len(x) / SR, 3)})
        parts.append(x); t += len(x) / SR; prev = r['scene']
    parts.append(np.zeros(int(0.5 * SR)))
    y = np.concatenate(parts)
    os.makedirs(os.path.join(EP, 'work'), exist_ok=True)
    os.makedirs(os.path.join(EP, 'review-b'), exist_ok=True)
    sf.write(os.path.join(EP, 'work', 'table-read.wav'), y, SR)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', os.path.join(EP, 'work', 'table-read.wav'), '-af', 'loudnorm=I=-16:TP=-1.5', '-c:a', 'aac', '-b:a', '128k',
                    os.path.join(EP, 'review-b', 'table-read-full.m4a')], check=True)
    json.dump({'sentences': tr, 'duration': round(len(y) / SR, 2)}, open(os.path.join(EP, 'work', 'table-read.json'), 'w'), indent=1)

    # 2) planned edit timeline
    t, acts, scenes, sents, breaks, sil = 0.0, [], [], [], [], []
    pending, cur_scene, cur_act = 0.0, None, None
    for r in rows:
        if r['scene'] != cur_scene:
            # gap before a new scene: the pending pause, at least GAP_SCENE after a spoken line (GAP_COLD inside the cold open),
            # nothing after a card, the ident or a hold
            if cur_scene is not None and pending:
                t += max(pending, GAP_COLD if cur_act == 'cold-open' else GAP_SCENE)
            pending = 0.0
            if r['act'] != cur_act:
                acts.append({'id': r['act'], 'start': round(t, 3)})
                cur_act = r['act']
            scenes.append({'id': r['scene'], 'act': r['act'], 'start': round(t, 3)})
            cur_scene = r['scene']
            if r['scene'] == 'S01':
                t += LEAD
        if r['kind'] == 'line':
            t += pending
            st = t; t += D[r['id']]
            sents.append({'id': r['id'], 'scene': r['scene'], 'text': r['text'], 'spoken': r['spoken'], 'start': round(st, 3), 'end': round(t, 3), 'claims': r['claims']})
            pending = GAP_COLD if r['act'] == 'cold-open' else GAP
        elif r['kind'] == 'pause':
            pending = max(pending, r['pause'])
            sil.append({'t': round(t + 0.05, 3), 'dur': r['pause'], 'after': sents[-1]['id'], 'why': 'ad break' if r.get('adBreak') else f"script pause after {sents[-1]['id']}"})
            if r.get('adBreak'):
                breaks.append({'t': round(t + r['pause'] / 2, 3), 'after': sents[-1]['id']})
        elif r['kind'] == 'card':
            if r['scene'] == 'S03':
                t += IDENT
            else:
                t += pending; pending = 0.0; t += CARD_HOLD.get(r['id'], 4.0)
            pending = 0.0
        elif r['kind'] == 'hold':
            t += pending; pending = 0.0; t += r['pause']
    total = round(t + pending, 3)
    for i, sc in enumerate(scenes):
        nxt = scenes[i + 1]['start'] if i + 1 < len(scenes) else total
        sh = shots[sc['id']]
        sc.update({'dur': round(nxt - sc['start'], 3), 'layout': sh['layout'], 'shot': sh['size'], 'panels': ['*'], 'chart': sh['layout'].split('/')[0],
                   'move': move_seconds(sh['move']), 'moveText': sh['move'], 'sonify': sh['sonify']})
    for i, a in enumerate(acts):
        a['end'] = acts[i + 1]['start'] if i + 1 < len(acts) else total
        if a['id'] in CLIMAX:
            a['climax'] = next(x['start'] for x in scenes if x['id'] == CLIMAX[a['id']])
    sstart = {s['id']: s['start'] for s in scenes}
    turns = [{'t': sstart[k], 'what': v} for k, v in TURNS.items()]
    rehook = next(s for s in sents if s['id'] == 'S04.2')
    marks = {'coldOpenEnd': next(a['start'] for a in acts if a['id'] == 'ident'), 'rehook': [rehook['start'], rehook['end']],
             'acts': {a['id']: [a['start'], a['end']] for a in acts}, 'adBreaks': [b['t'] for b in breaks], 'total': total}
    json.dump({'fps': 30, 'total': total, 'acts': acts, 'scenes': scenes, 'sentences': sents, 'turns': turns, 'marks': marks,
               'note': 'PLANNED at Stage 4b from the V8 takes (animatic timeline); the render re-times at M2'}, open(os.path.join(HERE, 'timeline-plan.json'), 'w'), indent=1)
    os.makedirs(os.path.join(EP, 'out'), exist_ok=True)
    json.dump({'fps': 30, 'total': total, 'acts': acts, 'scenes': [{k: v for k, v in s.items() if k not in ('sonify', 'moveText')} for s in scenes], 'turns': turns,
               'source': 'animatic timeline (preprod/edit.py, Stage 4b); not yet a render'}, open(os.path.join(EP, 'out', 'timeline.json'), 'w'), indent=1)
    json.dump({'sentences': [{k: s[k] for k in ('id', 'scene', 'text', 'spoken', 'start', 'end')} for s in sents],
               'source': 'story/script.md v2; times = animatic timeline (preprod/edit.py)'}, open(os.path.join(EP, 'out', 'script.json'), 'w'), indent=1, ensure_ascii=False)
    json.dump({'breaks': [b['t'] for b in breaks]}, open(os.path.join(EP, 'out', 'adbreaks.json'), 'w'), indent=1)

    # 3) cues + silences
    cues = [{'t': a['start'], 'end': a['end'], 'function': MUSIC[a['id']][2], 'key': MUSIC[a['id']][0], 'tempo': MUSIC[a['id']][1], 'layer': 'music'} for a in acts]
    cues += [{'t': round(max(a['start'], a['climax'] - 20), 2), 'end': a['climax'], 'function': f"build to the {a['id']} climax", 'key': MUSIC[a['id']][0], 'tempo': MUSIC[a['id']][1],
              'layer': 'music-dynamics'} for a in acts if 'climax' in a]
    os.makedirs(os.path.join(EP, 'edit'), exist_ok=True)
    json.dump({'cues': cues, 'silences': sil, 'adBreaks': breaks}, open(os.path.join(EP, 'edit', 'cues.json'), 'w'), indent=1)
    json.dump({'cues': cues, 'silences': sil, 'source': 'planned cue sheet (preprod/edit.py, Stage 4b); M2 writes the rendered cues'}, open(os.path.join(EP, 'out', 'cues.json'), 'w'), indent=1)
    SH = J('preprod/shotlist.json')
    son_count = {}
    for sc in scenes:
        for e in sc['sonify']:
            son_count[e] = son_count.get(e, 0) + 1
    L = ['# Episode 1 — cue sheet (Stage 4b, script v2)', '', f'Planned length **{total / 60:.2f} min** ({total:.1f} s) from the V8 takes. Music is generated in code; no third-party audio.', '',
         '## Music cues', '', '| t (s) | end | layer | key | tempo | dramatic function |', '|---|---|---|---|---|---|']
    L += [f"| {c['t']:.1f} | {c['end']:.1f} | {c['layer']} | {c['key']} | {c['tempo']} | {c['function']} |" for c in cues]
    L += ['', '## Intentional silences (script pauses; ~300 ms release in, room tone floor)', '', '| t (s) | length | after | why |', '|---|---|---|---|']
    L += [f"| {x['t']:.2f} | {x['dur']} s | `{x['after']}` | {x['why']} |" for x in sil]
    L += ['', f"Ad breaks: {', '.join('%.1f s' % b['t'] for b in breaks)} (end of act 1, end of act 2).", '',
          '## Data sonification plan (sổ gu G-001, G-005, G-006)', '',
          'Timbre: **S2**, palette `minimal` of `toolkit/audio/sonify_palettes.py` (owner\'s pick, 2026-09-28): soft filtered tick (4.5-7 kHz) + low pulse (MIDI 36-60). Bands for T1: 60-270 Hz + 4.5-7 kHz.', '',
          '| element | timbre | value mapping | pan | timing | scenes using it |', '|---|---|---|---|---|---|']
    L += [f"| {r['element']} | {r['sound']} | {r['mapping']} | {r['pan']} | {r['timing']} | {son_count.get(r['element'], 0)} |" for r in SH['sonification']]
    L += ['', '### Heard without covering the voice', ''] + [f'- {x}' for x in SH['separation']]
    open(os.path.join(HERE, 'cue-sheet.md'), 'w').write('\n'.join(L) + '\n')

    # 4) planned tension map
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
    json.dump({'samples': [{'t': float(x), 'cutRate': float(c), 'tension': round(float(v), 3)} for x, c, v in zip(ts, cut, ten)], 'peaks': peaks,
               'valleys': [{'t': round(p['t'] + 10, 1)} for p in peaks], 'note': 'PLANNED targets (Stage 4b); M2 measures from the edit and stems'},
              open(os.path.join(HERE, 'tension-map.json'), 'w'), indent=1)
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(12, 3.2), dpi=100)
    ax.plot(ts, ten, color='#4c8dff'); ax.set_xlim(0, total); ax.set_ylim(0, 1.05)
    for a in acts:
        ax.axvline(a['start'], color='#9aa4b2', lw=0.6); ax.text(a['start'] + 2, 1.0, a['id'], fontsize=7, color='#555')
    for x in sil:
        ax.axvspan(x['t'], x['t'] + x['dur'], color='#f2b441', alpha=0.4, lw=0)
    ax.set_xlabel('seconds'); ax.set_title('Episode 1 — planned tension (script v2)', fontsize=9)
    fig.tight_layout(); fig.savefig(os.path.join(HERE, 'tension-map.png')); plt.close(fig)

    # 5) shot list with times, colour script
    L = ['# Episode 1 — shot list (Stage 4b, script v2)', '', 'Every shot: size, camera move, reason. Times from the animatic timeline. 2.5D: moves on the chart plane only.', '',
         '| # | t (s) | scene | act | layout | size | move | reason | picture | data sounds |', '|---|---|---|---|---|---|---|---|---|---|']
    L += [f"| {s['id']} | {sstart[s['scene']]:.1f} | `{s['scene']}` | {s['act']} | {s['layout']} | {s['size']} | {s['move']} | {s['moveReason']} | {s['picture']} | {', '.join(s['sonify']) or '—'} |"
          for s in SH['shots']]
    open(os.path.join(HERE, 'shotlist.md'), 'w').write('\n'.join(L) + '\n')
    CS = ['# Episode 1 — colour script (script v2)', '', 'All colours are channel tokens (`design/tokens.json`). Characters: Nora = positive green circle (centre), Walt = warn amber triangle (left), '
          'Anjali = negative red square (right); names in ink. Rate line = accent, no marker. Bill/saved bars use ink-muted or a pattern whenever a character marker is on screen.', '',
          '| act | background | lead colour | feeling |', '|---|---|---|---|',
          '| cold open | bg | accent rate line to the 2023 peak; the paper letter (light) | a gain with a price |',
          '| act 1 | bg | accent line; Nora green enters; the bill block ink-muted | story, calm |',
          '| act 2 | bg | ink-muted old loan vs accent new loan; hatched gap | doubt rises to the quarter-point climax |',
          '| act 3 | bg | amber Walt (left), red Anjali (right), green Nora (centre) on one ruler | contrast, resolution |',
          '| method | surface | ink-muted text | quiet |', '| outro | bg | the three markers together | resolved |']
    open(os.path.join(HERE, 'color-script.md'), 'w').write('\n'.join(CS) + '\n')

    # 6) table-read notes
    acts_w = rep['acts']
    ch = {r['id']: r for r in rep['sentences']}
    wp = [(r['id'], r['chosen']['wpm']) for r in rep['sentences'] if r['chosen']['wpm']]
    lo, hi = min(wp, key=lambda x: x[1]), max(wp, key=lambda x: x[1])
    missing = [(r['id'], r['chosen']['missing']) for r in rep['sentences'] if r['chosen']['missing']]
    regen = []
    for r in lines:
        tk = sorted([x for x in el.values() if x['sid'] == r['id']], key=lambda x: (x['model'], x['take']))
        if len(tk) > 1:
            why = '; '.join(f"t{x['take']} {x['model'].replace('eleven_', '')}: {x['wpm']} wpm" + (f", missing {', '.join(x['missing'])}" if x['missing'] else '') for x in tk)
            regen.append((r['id'], ch[r['id']]['chosen'], why))
    cred = J('out/voice/el-credits.json')
    N = ['# Episode 1 — table read notes (Stage 4b, voice V8)', '',
         f"Voice: ElevenLabs Eric (V8), `eleven_v3`, fallback `eleven_multilingual_v2` per sentence. No time stretching (final clip = raw take trimmed to the speech span).",
         f"Audio: `review-b/table-read-full.m4a` ({len(y) / SR:.1f} s). Pace measured on the clean take: spoken words / ASR word span (faster-whisper small.en) of the raw take trimmed to its speech span.", '',
         '## Pace per act (wpm)', '', '| act | wpm |', '|---|---|'] + [f'| {k} | {v["rawWpm"]} |' for k, v in acts_w.items()] + [
         '', f'Slowest sentence: {lo[0]} {lo[1]} wpm. Fastest: {hi[0]} {hi[1]} wpm. Outside 120-190: ' + (', '.join(f'{k} ({v})' for k, v in wp if not 120 <= v <= 190) or 'none') + '.',
         f"Key words missing from ASR: {', '.join(f'{k} {v}' for k, v in missing) or 'none'}.", '',
         f"ElevenLabs characters (Character-Cost header, cumulative: takes in use + retired takes + calibration calls): **{cred.get('cumulativeCharacterCost', cred['allTakesCharacterCost'])}**; takes in the store: {cred['takesGenerated']}.", '',
         '## Sentences regenerated (more than one take) and why', '', '| sentence | chosen | takes (wpm, missing key words) |', '|---|---|---|']
    N += [f"| {sid} | t{c['take']} {c['model'].replace('eleven_', '')} {c['wpm']} wpm | {why} |" for sid, c, why in regen]
    open(os.path.join(EP, 'script', 'table-read-notes.md'), 'w').write('\n'.join(N) + '\n')
    print(json.dumps({'tableRead': round(len(y) / SR, 1), 'plannedTotal': total, 'marks': marks, 'actWpm': {k: v['rawWpm'] for k, v in acts_w.items()}, 'min': lo, 'max': hi,
                      'missing': missing, 'regenerated': len(regen)}, indent=1))


if __name__ == '__main__':
    main()
