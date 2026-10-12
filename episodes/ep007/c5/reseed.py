"""Tập 7 · C5 · A14 (CHẶN, ASR mất từ khoá): sinh lại cảnh bằng seed khác (episode.yaml voice_overrides, B+1), chọn take đầu tiên mà ASR
small.en (như A14: word timestamps, không VAD, không điều kiện câu trước) nghe đủ từ khoá của cảnh. Chữ kịch bản không đổi.
    python3 episodes/ep007/c5/reseed.py S09,S12,S15,S21,S25,S33 [--seeds 1008,1009,1010]   → in kết quả, ghi c5/reseed.json"""
import json, os, sys
EP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(EP, 'story'))
import voice_scenes as VS  # noqa: E402  (rows(), pcm16k(), V, key_words/match_keys qua checks/py)
import yaml  # noqa: E402

scenes = sys.argv[1].split(',')
seeds = [int(s) for s in (sys.argv[sys.argv.index('--seeds') + 1] if '--seeds' in sys.argv else '1008,1009,1010').split(',')]
base = yaml.safe_load(open(os.path.join(EP, 'episode.yaml')))['voice']
from faster_whisper import WhisperModel  # noqa: E402
wm = WhisperModel('small.en', device='cpu', compute_type='int8')
rs = VS.rows()
out = json.load(open(os.path.join(EP, 'c5', 'reseed.json'))) if os.path.exists(os.path.join(EP, 'c5', 'reseed.json')) else {}
spent = 0
for sc in scenes:
    sents = [r for r in rs if r['scene'] == sc]
    keys = [k for r in sents for k in r['keys']]
    for seed in seeds:
        cfg = {**base, 'seed': seed}
        v = VS.V.voice_scene(cfg, [{'id': r['id'], 'scene': sc, 'text': r['text']} for r in sents], os.path.join(EP, 'voice-takes'), os.path.join(EP, 'work', 'voice'))
        spent += 0 if v['cached'] else v['chars']
        segs, _ = wm.transcribe(VS.pcm16k(v['wav']), word_timestamps=True, language='en', beam_size=5, condition_on_previous_text=False)
        words = [{'w': w.word.strip(), 'start': w.start, 'end': w.end} for g in segs for w in g.words]
        miss = VS.match_keys(keys, words) if keys else []
        out.setdefault(sc, {})[str(seed)] = {'take': os.path.basename(v['mp3']), 'duration': v['duration'], 'missing': miss}
        print(sc, seed, v['duration'], 'missing', miss, flush=True)
        json.dump(out, open(os.path.join(EP, 'c5', 'reseed.json'), 'w'), indent=1)
        if not miss:
            break
print('chars spent', spent)
