#!/usr/bin/env python3
"""Merge src/anchors_*.json (rows: scene, id, sentence n, at, dt, action, muted meaning) into animatic/anchors.json,
resolving each anchor's time against timing.json (so the table shows where it lands now)."""
import glob, json, os
HERE = os.path.dirname(os.path.abspath(__file__)); AN = os.path.dirname(HERE)
tm = json.load(open(os.path.join(AN, 'timing.json')))
sent = {s['n']: s for sc in tm['scenes'] for s in sc['sentences']}
start = {sc['id']: sc['start'] for sc in tm['scenes']}
rows = []
for f in sorted(glob.glob(os.path.join(HERE, 'anchors_*.json'))):
    rows += json.load(open(f))
out = []
for sc, i, n, at, dt, act, mean in rows:
    s = sent[n]; assert s['text'] and n in sent
    if at == 'start': t = s['start']
    elif at == 'end': t = s['end']
    else:
        k = s['text'].lower().find(at.lower())
        t = s['start'] + (s['end'] - s['start']) * (k / len(s['text'])) if k >= 0 else s['start']
    out.append({'scene': sc, 'id': i, 'n': n, 'at': at, 'dt': dt, 'action': act, 'meaning_muted': mean,
                'sentence': s['text'], 'resolved_s': round(t + dt, 2), 'local_s': round(t + dt - start[sc], 2), 'keyword_found': at in ('start', 'end') or s['text'].lower().find(at.lower()) >= 0})
json.dump({'_about': 'C4 animatic anchor table: every meaningful picture action is tied to a sentence number (script-v3.1 order) and a keyword in it (or its start/end), plus a small offset dt. Scenes read these through T.a(id); times are re-resolved from timing.json at render, so a new voice only needs a new timing.json. resolved_s/local_s show where the anchor lands with the current timing; meaning_muted = what the action must say with the sound off.',
           'anchors': out}, open(os.path.join(AN, 'anchors.json'), 'w'), indent=1, ensure_ascii=False)
print(len(out), 'anchors;', sum(not o['keyword_found'] for o in out), 'keywords not found:', [o['id'] for o in out if not o['keyword_found']])
