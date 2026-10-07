"""Sinh lại một cảnh với seed khác (cùng chữ) và so ASR medium.en với lời từng từ.
  python3 story/seed_check.py S04 1006 1007"""
import difflib, json, re, sys
sys.path[:0] = ['/home/user/crux-lab/episodes/ep005/story', '/home/user/crux-lab/toolkit/factory']
import voice_scenes as VS, voice as V, yaml
from faster_whisper import WhisperModel
sc = sys.argv[1]; seeds = [int(s) for s in sys.argv[2:]]
EP = VS.EP; cfg = yaml.safe_load(open(f'{EP}/episode.yaml'))['voice']
sents = [{'id': r['id'], 'scene': sc, 'text': r['text']} for r in VS.rows() if r['scene'] == sc]
norm = lambda s: re.findall(r"[a-z0-9']+", re.sub(r'\[[a-z ]+\]', '', s.lower()).replace('%', ' percent'))
ref = norm(' '.join(V.to_spoken([s['text'] for s in sents])))
m = WhisperModel('medium.en', device='cpu', compute_type='int8'); out = {}
for seed in seeds:
    v = V.voice_scene({**cfg, 'seed': seed}, sents, f'{EP}/voice-takes', f'{EP}/work/voice')
    segs, _ = m.transcribe(v['wav'], language='en', beam_size=5, condition_on_previous_text=False)
    hyp = norm(' '.join(g.text for g in segs))
    ops = [(t, ' '.join(ref[a:b]), ' '.join(hyp[c:d])) for t, a, b, c, d in difflib.SequenceMatcher(None, ref, hyp).get_opcodes() if t != 'equal']
    out[seed] = {'take': v['mp3'].split('/')[-1], 'chars': 0 if v['cached'] else v['chars'], 'diffs': ops}
    print(seed, out[seed]['take'], 'chars', out[seed]['chars'], 'diffs', ops, flush=True)
json.dump(out, open(f'{EP}/review-c4/{sc}-seeds.json', 'w'), indent=1)
