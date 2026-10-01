"""C5 Tập 2 · luồng A: sinh lại MỘT cảnh khi chữ kịch bản đổi (hoặc ASR thiếu từ khoá vì giọng), bằng chính story/table_read.py (synth: endpoint stream,
thử lại; Eric, eleven_v3, mặc định, không speed). Seed 1 cho chữ mới; seed kế chỉ khi ASR thiếu từ khoá. Ghi take vào review-c2/takes (tên theo hash chữ),
cập nhật mục cảnh trong review-c2/table-read.json (`use`, takes, ký tự EL; mục cũ giữ ở `previous`). Khoá API do proxy tiêm; không đọc, không in.
    python3 episodes/ep002/audio_src/regen_scene.py S08 [--checks <copy>/py]
"""
import hashlib, importlib.util, json, os, sys
EP = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
args = sys.argv[1:]; sc = args[0]
CK = args[args.index('--checks') + 1] if '--checks' in args else None
sys.argv = [sys.argv[0]]
spec = importlib.util.spec_from_file_location('tr', os.path.join(EP, 'story', 'table_read.py')); tr = importlib.util.module_from_spec(spec); spec.loader.exec_module(tr)
if CK:
    sys.path.insert(0, CK)
    for k in [k for k in sys.modules if k.startswith('r_')]: del sys.modules[k]
    import r_audio
    tr.key_words, tr.match_keys = r_audio.key_words, r_audio.match_keys
rs = tr.rows(); text = tr.scene_text([r for r in rs if r['scene'] == sc])
keys = [k for r, kk in zip(rs, tr.key_words([{'text': r['text']} for r in rs])) if r['scene'] == sc for k in kk]
resf = os.path.join(EP, 'review-c2', 'table-read.json'); res = json.load(open(resf))
old = res['scenes'][sc]
assert old['text'] != text, 'text unchanged: nothing to regenerate'
e = {'text': text, 'takes': [], 'previous': {k: old[k] for k in ('text', 'use', 'takes')}, 'regenerated': 'C5 stream A (script change)'}
for seed in (1, 2):
    p = os.path.join(tr.TAKES, f"{sc}.{hashlib.sha1(text.encode()).hexdigest()[:8]}.seed{seed}")
    m = tr.synth(text, p, seed); w = tr.asr(p + '.mp3')
    e['takes'].append({'file': os.path.basename(p) + '.mp3', 'seed': seed, 'characterCost': m['characterCost'], 'len': m['len'],
                       'missing': tr.match_keys(keys, w), 'asr': ' '.join(x['w'] for x in w)})
    print(sc, 'seed', seed, 'chars', m['characterCost'], 'len', m['len'], 'missing', e['takes'][-1]['missing'], flush=True)
    if not e['takes'][-1]['missing']: break
e['use'] = min(e['takes'], key=lambda t: len(t['missing']))['file']
res['scenes'][sc] = e
res['chars'] = sum(t['characterCost'] or t['len'] for x in res['scenes'].values() for t in x['takes'] + x.get('previous', {}).get('takes', []))
json.dump(res, open(resf, 'w'), indent=1)
print('use', e['use'])
