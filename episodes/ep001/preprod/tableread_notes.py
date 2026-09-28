"""Table-read report (DX-S9): pace per act and sentence, key words not heard, credits. -> script/table-read-notes.md

    python3 episodes/ep001/preprod/tableread_notes.py
"""
import glob
import json
import os

EP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
r = json.load(open(os.path.join(EP, 'out', 'voice', 'choice-report.json')))
tr = json.load(open(os.path.join(EP, 'work', 'table-read.json')))
st = {s['id']: s['start'] for s in tr['sentences']}
cur = sum(json.load(open(f))['characterCost'] for f in glob.glob(os.path.join(EP, 'out', 'voice', 'el', '*.json')))
old = sum(json.load(open(f))['characterCost'] for f in glob.glob(os.path.join(EP, 'work', 'replaced-takes', '**', '*.json'), recursive=True))
takes = len(glob.glob(os.path.join(EP, 'out', 'voice', 'el', '*.mp3')))
mm = lambda t: f'{int(t // 60)}:{t % 60:04.1f}'
bad = [x for x in r['sentences'] if x['chosen']['wpm'] and not 120 <= x['chosen']['wpm'] <= 190]
miss = [x for x in r['sentences'] if x['chosen']['missing']]
models = {}
for x in r['sentences']:
    models[x['chosen']['model']] = models.get(x['chosen']['model'], 0) + 1
L = ['# Episode 1 — table read M1b: audio and list of fixes', '',
     f"- Audio: `review-m1b/table-read-full.m4a` ({mm(tr['duration'])}, largest gap between sentences {tr['maxGap']} s). Voice: ElevenLabs Eric, `eleven_v3` first, `eleven_multilingual_v2` (speed-controlled) as the per-sentence fallback; no time stretching. Provisional voice, not decision #158.",
     f"- Chosen takes by model: {', '.join(f'{k} {v}' for k, v in models.items())}. Takes generated in `out/voice/el/`: {takes}.",
     f"- Credits (sum of `character-cost` headers): takes in use or generated this round {cur:,}; earlier rounds kept in `work/replaced-takes/` {old:,}.", '',
     '## Pace (DX-A7: every act 150-160 wpm, every sentence 120-190)', '', '| act | wpm |', '|---|---|']
L += [f"| {k} | {v['rawWpm']} |" for k, v in r['acts'].items()]
L += ['', f'{len(bad)} sentences outside 120-190 wpm:', ''] + ([f"- `{x['id']}` at {mm(st[x['id']])}: {x['chosen']['wpm']} wpm ({x['chosen']['model']})" for x in bad] or ['- none'])
L += ['', f'Key words not heard by the builder\'s ASR: {len(miss)}', ''] + ([f"- `{x['id']}`: {x['chosen']['missing']} | heard: \"{x['chosen']['heard'][:100]}\"" for x in miss] or ['- none'])
L += ['', 'The machine list does not replace listening (DX-S9): the owner judges the read by ear.']
open(os.path.join(EP, 'script', 'table-read-notes.md'), 'w').write('\n'.join(L) + '\n')
print(r['acts'], len(bad), len(miss))
