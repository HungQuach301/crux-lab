"""Tập 9 · M3: sinh lời thật cả tập bằng nhà máy (toolkit/factory/voice.py, cache SHA-256 trong voice-takes/; cảnh đã có take = 0 ký tự).
    python3 episodes/ep009/prod/voice.py --dry     # chỉ đếm ký tự sẽ sinh
    python3 episodes/ep009/prod/voice.py           # sinh (khoá EL qua proxy; không in khoá)
Điều kiện (G1 15/10): đọc hạn mức GET /v1/user/subscription TRƯỚC — còn < 15.000 ký tự → dừng."""
import json, os, re, sys, hashlib
import yaml
HERE = os.path.dirname(os.path.abspath(__file__)); EP = os.path.dirname(HERE); ROOT = os.path.abspath(os.path.join(EP, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'toolkit', 'factory')); sys.dont_write_bytecode = True
import voice as V  # noqa: E402
LINE = re.compile(r'^(S\d\d)\.(\d+)\s+(?:\{(\w+)\}\s+)?(.+?)\s*<!--')
Y = yaml.safe_load(open(os.path.join(EP, 'episode.yaml')))
rows = [(f'{m[1]}.{m[2]}', m[1], m[4].strip()) for m in (LINE.match(l) for l in open(os.path.join(EP, 'story', 'script.md'), encoding='utf-8')) if m]
todo, chars = [], 0
for s in Y['scenes']:
    cfg = V.scene_cfg(Y['voice'], Y.get('voice_overrides'), s['id'])
    sents = [{'id': i, 'text': t} for i, sc, t in rows if sc == s['id']]
    text = ' '.join(V.to_spoken([x['text'] for x in sents]))
    key = hashlib.sha256(json.dumps([text, cfg['voice'], cfg['model'], cfg['seed'], cfg.get('settings', {'stability': 0.5, 'speed': 0.9})], sort_keys=True).encode()).hexdigest()
    if cfg.get('take') or os.path.exists(os.path.join(EP, 'voice-takes', key[:16] + '.mp3')):
        continue
    todo.append((s['id'], cfg, sents)); chars += len(text)
print('cảnh cần sinh:', [t[0] for t in todo], '· ký tự:', chars)
if '--dry' in sys.argv or not todo:
    sys.exit(0)
spent = 0
for sid, cfg, sents in todo:
    v = V.voice_scene(cfg, sents, os.path.join(EP, 'voice-takes'), os.path.join(EP, 'work', 'voice'))
    spent += 0 if v['cached'] else v['chars']; print(sid, v['duration'], 'cache' if v['cached'] else f"{v['chars']} ký tự", flush=True)
print('EL đã dùng:', spent)
