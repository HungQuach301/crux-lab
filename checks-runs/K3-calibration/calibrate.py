"""K3 calibration of the voice warnings on Episode 1 (branch ep001 @ bbc28fb, episodes/ep001/out/voice/).

    python3 checks-runs/K3-calibration/calibrate.py <episode root with out/voice/>   -> prints the JSON written to checks-runs/K3-calibration/ep001.json"""
import collections
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'checks', 'py'))
import common  # noqa: E402
import r_voice  # noqa: E402

root = sys.argv[1]
V = os.path.join(root, 'out', 'voice')
sents = json.load(open(os.path.join(V, 'sentences.json')))['sentences']
kinds, hit = collections.Counter(), 0
for s in sents:
    fb = r_voice.fake_breaks(s['text'], s.get('spoken') or '')
    hit += bool(fb)
    kinds.update(k for k, _ in fb)
takes = json.load(open(os.path.join(V, 'takes.json')))['takes']
prof = {}
for tk in takes:
    prof.setdefault(tk['model'], []).append(r_voice.ltas(common.decode_audio(os.path.join(root, tk['raw']), channels=1)))
allp = [p for v in prof.values() for p in v]
med = np.median(np.stack(allp), 0)
per = {m: sorted(round(float(np.sqrt(np.mean((p - med) ** 2))), 2) for p in v) for m, v in prof.items()}
d, p99 = r_voice.group_distance(prof['eleven_v3'], prof['eleven_multilingual_v2'])
out = {'A16': {'sentences': len(sents), 'withFakeBreak': hit, 'marks': dict(kinds)},
       'A18': {'takesByModel': {m: len(v) for m, v in prof.items()},
               'perTakeDistanceToMedianDb': {m: {'p50': float(np.percentile(v, 50)), 'p95': float(np.percentile(v, 95)), 'max': max(v)} for m, v in per.items()},
               'multilingualV2PerTakeDb': per['eleven_multilingual_v2'],
               'groupDistanceDb': round(d, 2), 'chanceP99Db': round(p99, 2)}}
print(json.dumps(out, indent=1))
