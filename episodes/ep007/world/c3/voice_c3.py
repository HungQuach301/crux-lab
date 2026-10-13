"""Tập 7 · C3 · lời thật cho năm đoạn thế giới: mỗi cảnh một take (toolkit/factory/voice.py, cache SHA-256, take commit ở voice-takes/).
  python3 episodes/ep007/world/c3/voice_c3.py          → chỉ in số ký tự sẽ dùng (không gọi API)
  python3 episodes/ep007/world/c3/voice_c3.py --go     → sinh (take đã có = 0 ký tự), ghi world/c3/voice-scenes.json
Trần C3 = 3.000 ký tự ElevenLabs: vượt → dừng trước khi gọi API. Cấu hình giọng = `voice:` của episode.yaml."""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); W7 = os.path.dirname(HERE)
sys.path.insert(0, W7)
import wlib            # script_rows, spoken; thêm toolkit/factory vào sys.path  # noqa: E402
import voice as V      # noqa: E402
import yaml            # noqa: E402

SCENES, CAP = ['S01', 'S06', 'S21', 'S23', 'S25'], 3000
cfg = yaml.safe_load(open(os.path.join(wlib.EP, 'episode.yaml')))['voice']
cfg = {'voice': cfg['voice'], 'model': cfg['model'], 'seed': cfg['seed'], 'settings': cfg['settings']}
rows = wlib.script_rows()
plan, need = {}, 0
for sc in SCENES:
    sents = [{'id': r['id'], 'text': r['text']} for r in rows if r['scene'] == sc]
    text = ' '.join(wlib.spoken(sents))
    import hashlib
    key = hashlib.sha256(json.dumps([text, cfg['voice'], cfg['model'], cfg['seed'], cfg['settings']], sort_keys=True).encode()).hexdigest()
    have = os.path.exists(os.path.join(wlib.TAKES, key[:16] + '.json'))
    plan[sc] = {'sents': sents, 'text': text, 'key': key[:16], 'cached': have}
    need += 0 if have else len(text)
    print(f'{sc}: {len(text)} ký tự {"(đã có take, 0)" if have else ""} — {text}')
print(f'tổng sẽ dùng: {need} ký tự (trần C3 {CAP})')
if need > CAP: raise SystemExit('vượt trần C3 — dừng, báo phiên điều phối')
if '--go' not in sys.argv: raise SystemExit(0)

out, spent = {}, 0
wav_dir = os.path.join(wlib.EP, 'work', 'voice-wav')
for sc in SCENES:
    r = V.voice_scene(cfg, plan[sc]['sents'], wlib.TAKES, wav_dir)
    meta = json.load(open(r['mp3'][:-4] + '.json'))
    assert meta['text'] == plan[sc]['text'] and ''.join(meta['alignment']['characters']) == plan[sc]['text'], f'{sc}: chữ take ≠ lời kịch bản'
    spent += 0 if r['cached'] else r['chars']
    out[sc] = {'take': os.path.basename(r['mp3']), 'duration': r['duration'], 'chars': r['chars'], 'cached': r['cached'],
               'sentences': [s['id'] for s in plan[sc]['sents']], 'text_matches_script': True}
json.dump({**out, '_spent_chars': spent, '_config': cfg}, open(os.path.join(HERE, 'voice-scenes.json'), 'w'), indent=1)
print('đã ghi voice-scenes.json; ký tự tiêu lần này', spent)
