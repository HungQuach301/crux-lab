"""Tập 5 · S18.5 "illustrative": sinh lại cùng chữ, seed khác (tối đa 2), ASR small.en + medium.en (chủ dự án, 2026-10-06)."""
import json, sys
sys.path[:0] = ['/home/user/crux-lab/episodes/ep005/story', '/home/user/crux-lab/toolkit/factory']
import voice_scenes as VS, voice as V, yaml
from faster_whisper import WhisperModel
EP = VS.EP; cfg = yaml.safe_load(open(f'{EP}/episode.yaml'))['voice']
sents = [{'id': r['id'], 'scene': 'S18', 'text': r['text']} for r in VS.rows() if r['scene'] == 'S18']
models = {m: WhisperModel(m, device='cpu', compute_type='int8') for m in ('small.en', 'medium.en')}
out = {}
for seed in [cfg['seed']] + [int(s) for s in sys.argv[1:]]:
    v = V.voice_scene({**cfg, 'seed': seed}, sents, f'{EP}/voice-takes', f'{EP}/work/voice')
    hits = {}
    for name, m in models.items():
        segs, _ = m.transcribe(v['wav'], word_timestamps=True, language='en', beam_size=5, condition_on_previous_text=False)
        ws = [(w.word.strip(' ,.').lower(), round(w.probability, 2)) for g in segs for w in g.words]
        hits[name] = [w for w in ws if w[0].startswith('illustr')]
    out[seed] = {'take': v['mp3'].split('/')[-1], 'chars': 0 if v['cached'] else v['chars'], 'illustr': hits}
    print(seed, out[seed], flush=True)
json.dump(out, open(f'{EP}/review-g1/s18-seeds.json', 'w'), indent=1)
