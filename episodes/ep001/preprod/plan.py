"""Episode 1 pre-production plan (Stage 4b, script v2): one shot per scene of story/script.md, the single source of the shot
list, storyboard, animatic and cue sheet.

    python3 episodes/ep001/preprod/plan.py      # needs out/script-draft.json (preprod/script_from_story.py)

Shot: scene -> (layout family/variant, shot size, camera move, reason for the move, data-sound elements that change:
bar / line / dot / counter). The picture text is the script's own picture note for the scene.
Characters (ILLUSTRATIVE; numbers are HMDA 2025 medians): Nora = median = positive green, circle, centre;
Walt = small = warn amber, triangle, left; Anjali = large = negative red, square, right (design/tokens.json shapes/series).
Rate line = accent blue, no marker. Old loan = ink-muted, new loan = accent. Names in ink beside the marker.
2.5D only: moves are pans/pushes on the chart plane, no simulated lens or 3D angle.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.join(HERE, '..')

S = {
    'S01': ('line/peak', 'wide', 'track right 3.0 s', 'follow the rate line as it draws up to the October 2023 peak', ['line', 'dot']),
    'S02': ('letter/offer', 'close', 'tilt down 1.5 s', 'read the letter top to bottom and stop on the bill line', ['counter']),
    'S03': ('ident/logo', 'wide', 'none', 'no move on the 3 s ident', []),
    'S04': ('ruler/empty', 'medium', 'none', 'hold: the empty rate-drop ruler is the promise', ['dot']),
    'S05': ('line/low-to-peak', 'wide', 'track right 4.0 s', 'travel from the 2021 low to the 2023 peak along the line', ['line', 'dot']),
    'S06': ('grid/houses', 'medium', 'push-in 1.5 s', 'from ten houses into the one that is Nora\'s', ['bar']),
    'S07': ('line/nora-lands', 'medium', 'none', 'hold: Nora\'s circle drops onto October 2023', ['dot']),
    'S08': ('letter/today', 'medium', 'track right 1.5 s', 'from her month to the week of September 24, 2026 on the line', ['line', 'dot']),
    'S09': ('bars/payment', 'close', 'none', 'hold: the payment bar shrinks by $221', ['bar']),
    'S10': ('blocks/bill-vs-saving', 'medium', 'pull-out 1.2 s', 'reveal the $5,124 block beside the small $221 block', ['bar']),
    'S11': ('letter/two-slots', 'wide', 'none', 'hold: two empty answer slots', []),
    'S12': ('split/line-vs-division', 'medium', 'none', 'split screen: the one-point line and the counter', ['counter']),
    'S13': ('letter/missing-line', 'close', 'push-in 1.5 s', 'into the blank line of the letter before the break', []),
    'S14': ('blocks/stack', 'medium', 'tilt up 2.0 s', 'follow the monthly blocks up to the bill line', ['bar']),
    'S15': ('balance/stairs', 'medium', 'none', 'hold: two balance lines, old steeper than new', ['line']),
    'S16': ('balance/gap24', 'close', 'push-in 1.3 s', 'into the gap between the lines at month 24', ['dot']),
    'S17': ('clock/30', 'medium', 'none', 'hold while the counter passes 24 and stops at 30', ['counter']),
    'S18': ('clock/38', 'medium', 'none', 'hold: division stops at 38', ['counter']),
    'S19': ('clock/never', 'wide', 'pull-out 1.5 s', 'the break-even mark drifts out of frame', ['line']),
    'S20': ('ruler/test', 'medium', 'track left 1.2 s', 'the circle tries the one-point mark, then a quarter', ['dot']),
    'S21': ('ruler/nora', 'medium', 'none', 'hold: the circle lands at 0.5', ['dot']),
    'S22': ('person/walt', 'medium', 'track left 1.5 s', 'cross to Walt on the left', ['bar']),
    'S23': ('blocks/three-bills', 'wide', 'none', 'hold: three bills beside three loans, to scale', ['bar']),
    'S24': ('blocks/walt-stack', 'medium', 'none', 'hold: $68 blocks stack slowly', ['bar', 'counter']),
    'S25': ('timeline/walt3', 'medium', 'track right 1.2 s', 'along Walt\'s timeline to year 3', ['bar']),
    'S26': ('ruler/walt', 'medium', 'track right 1.2 s', 'the triangle lands past the one-point mark', ['dot']),
    'S27': ('person/anjali', 'medium', 'track right 1.5 s', 'cross to Anjali on the right', ['bar']),
    'S28': ('ruler/anjali', 'medium', 'pull-out 1.2 s', 'the square lands at 0.32; all three markers in frame', ['dot']),
    'S29': ('ruler/answer', 'wide', 'none', 'the letter and the ruler: same objects as the open', ['dot']),
    'S30': ('timeline/nora3', 'medium', 'none', 'hold on year 3', ['bar']),
    'S31': ('timeline/nora7', 'wide', 'pull-out 1.5 s', 'the timeline extends to year 7', ['bar']),
    'S32': ('card/method', 'medium', 'none', 'method card: static, readable', []),
    'S33': ('card/history', 'medium', 'none', 'static card: 13 drops since 1971, 3 marked', ['dot']),
    'S34': ('end/screen', 'wide', 'drift 8 px/s', 'slow drift into the end-screen space', []),
}

SONIFY = [
    {'element': 'bar', 'sound': "S2 'minimal' (owner's pick, 2026-09-28): a soft low pulse at the value's pitch (MIDI 36-60, D minor pentatonic) with a soft filtered tick (4.5-7 kHz) at the start",
     'mapping': 'pitch = bar value on one fixed scale for the film, snapped to the music key; lasts while the bar grows', 'pan': 'x of the bar',
     'timing': 'starts when the bar starts to grow (moved into the nearest syllable gap if the voice is sounding)'},
    {'element': 'line', 'sound': 'S2: soft low pulses on eighth notes while the tip moves, pitch following the slope, each with a faint filtered tick',
     'mapping': 'pitch follows the slope at the drawing tip (rising line = higher)', 'pan': 'x of the tip', 'timing': 'while the tip moves; notes land in syllable gaps'},
    {'element': 'dot', 'sound': 'S2: one deeper pulse, pitch from the dot height, plus a soft filtered tick', 'mapping': 'pitch from the dot height on screen',
     'pan': 'x of the dot', 'timing': 'on the frame the dot appears (nearest syllable gap, -60..+120 ms)'},
    {'element': 'counter', 'sound': 'S2: a soft filtered tick per value change; above 8 changes/s the ticks merge into a soft roll', 'mapping': 'one event per value change',
     'pan': 'x of the counter', 'timing': 'on the digit change'},
]

SEPARATION = [
    'Owner, 2026-09-28 (sổ gu G-006): the voice comes first; the data sounds must not cover it; never solved by raising the level.',
    'Side-chain: the whole data layer ducks 8 dB while the voice is active (20 ms attack, 250 ms release).',
    'Band: while the voice is active the data layer loses 1-4 kHz (the speech band) almost entirely.',
    'Timing: notes that would start while a syllable sounds move to the quietest instant within -60..+120 ms.',
    'Level: -16 dB under the voice before the side-chain (toolkit/audio/sonify_palettes.py); never raised.',
]
CHARACTERS = {'median': {'name': 'Nora', 'color': 'median', 'shape': 'circle', 'side': 'centre'},
              'small': {'name': 'Walt', 'color': 'small', 'shape': 'triangle', 'side': 'left'},
              'large': {'name': 'Anjali', 'color': 'large', 'shape': 'square', 'side': 'right'}}


def main():
    d = json.load(open(os.path.join(EP, 'out', 'script-draft.json')))
    scenes = d['scenes']
    ids = [s['id'] for s in scenes]
    assert sorted(ids) == sorted(S), (set(ids) ^ set(S))
    shots = []
    for i, sc in enumerate(scenes):
        lay, size, move, why, son = S[sc['id']]
        shots.append({'id': f'sh{i + 1:03d}', 'scene': sc['id'], 'act': sc['act'], 'beat': sc['beat'], 'layout': lay, 'size': size, 'move': move,
                      'moveReason': why, 'picture': sc['picture'], 'sonify': son})
    json.dump({'source': 'story/script.md (v2) via out/script-draft.json', 'shots': shots, 'characters': CHARACTERS, 'sonification': SONIFY, 'separation': SEPARATION},
              open(os.path.join(HERE, 'shotlist.json'), 'w'), indent=1, ensure_ascii=False)
    md = ['# Episode 1 — shot list (Stage 4b, script v2)', '', 'Generated by `preprod/plan.py` from `story/script.md`. 2.5D: moves on the chart plane only.', '',
          '| shot | scene | act | size | move | why the move | layout | data sounds | picture |', '|---|---|---|---|---|---|---|---|---|']
    md += [f"| {s['id']} | {s['scene']} | {s['act']} | {s['size']} | {s['move']} | {s['moveReason']} | `{s['layout']}` | {', '.join(s['sonify']) or '-'} | {s['picture']} |" for s in shots]
    open(os.path.join(HERE, 'shotlist.md'), 'w').write('\n'.join(md) + '\n')
    print(len(shots), 'shots')


if __name__ == '__main__':
    main()
