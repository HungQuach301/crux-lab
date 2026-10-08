"""So ASR medium.en với lời TỪNG TỪ cho take hiện dùng của mọi cảnh (seed theo voice_overrides). Không gọi API (take có sẵn).
  python3 story/asr_all.py  → review-c4/asr-all.json"""
import difflib, json, re, sys
sys.path[:0] = ['/home/user/crux-lab/episodes/ep005/story', '/home/user/crux-lab/toolkit/factory']
import voice_scenes as VS, voice as V, yaml, os
from faster_whisper import WhisperModel
EP = VS.EP; Y = yaml.safe_load(open(f'{EP}/episode.yaml')); base = Y['voice']; ov = Y.get('voice_overrides') or {}
norm = lambda s: re.findall(r"[a-z0-9']+", re.sub(r'\[[a-z ]+\]', '', s.lower()).replace('%', ' percent'))
NUMOK = lambda a, b: re.fullmatch(r"[\d,.' ]+", b.replace(' ', '')) is not None  # "twenty"→"20": cách viết số của ASR
m = WhisperModel('medium.en', device='cpu', compute_type='int8'); rows = VS.rows(); out = {}
for sc in sorted({r['scene'] for r in rows}):
    cfg = {**base, **ov.get(sc, {})}
    sents = [{'id': r['id'], 'scene': sc, 'text': r['text']} for r in rows if r['scene'] == sc]
    v = V.voice_scene(cfg, sents, f'{EP}/voice-takes', f'{EP}/work/voice')
    assert v['cached'], f'{sc}: take chưa có (không gọi API ở đây)'
    segs, _ = m.transcribe(v['wav'], language='en', beam_size=5, condition_on_previous_text=False)
    ref = norm(' '.join(V.to_spoken([s['text'] for s in sents]))); hyp = norm(' '.join(g.text for g in segs))
    ops = [(t, ' '.join(ref[a:b]), ' '.join(hyp[c:d])) for t, a, b, c, d in difflib.SequenceMatcher(None, ref, hyp).get_opcodes() if t != 'equal']
    sus = [o for o in ops if not (o[0] == 'replace' and NUMOK(o[1], o[2]))]
    out[sc] = {'take': os.path.basename(v['mp3']), 'seed': cfg['seed'], 'diffs': ops, 'suspect': sus}
    print(sc, cfg['seed'], 'suspect', sus, flush=True)
json.dump(out, open(f'{EP}/review-c4/asr-all.json', 'w'), indent=1)
