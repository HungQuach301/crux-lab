"""One ElevenLabs with-timestamps request for the whole 45 s test clip (toolkit/factory/voice.py, cached by SHA-256).
   python3 rnd-hybrid/clip/voice_clip.py  → rnd-hybrid/clip/voice-takes/<hash>.{mp3,json} + work/voice.json"""
import json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'toolkit', 'factory'))
from voice import voice_scene, to_spoken  # noqa: E402
HERE = os.path.dirname(os.path.abspath(__file__))
sents = json.load(open(os.path.join(HERE, 'narration.json')))
spoken = ' '.join(to_spoken([s['text'] for s in sents]))
print('chars sent:', len(spoken)); assert len(spoken) <= 800, 'brief cap: ≤ 800 characters'
cfg = {'voice': 'cjVigY5qzO86Huf0OWal', 'model': 'eleven_v3', 'seed': 1401, 'settings': {'stability': 0.5, 'speed': 0.9}}  # Eric, as Tập 1–7
r = voice_scene(cfg, sents, os.path.join(HERE, 'voice-takes'), os.path.join(ROOT, 'rnd-hybrid', 'work'))
json.dump(r, open(os.path.join(ROOT, 'rnd-hybrid', 'work', 'voice.json'), 'w'), indent=1)
print(json.dumps({k: r[k] for k in ('duration', 'chars', 'cached')}), [(s['id'], s['start'], s['end']) for s in r['sentences']])
