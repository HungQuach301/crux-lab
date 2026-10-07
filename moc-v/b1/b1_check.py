"""Mốc V · B+1 — ca kiểm thật: Tập 5 (bản sao CHỈ ĐỌC của nhánh ep005) dựng lời theo voice_overrides.
  python3 moc-v/b1/b1_check.py <episode_dir> <out.json>
- Mỗi cảnh: cfg = toolkit/factory/voice.scene_cfg(voice, voice_overrides, cảnh) → voice_scene() (API BỊ KHOÁ: chỉ dùng take đã có).
- So với không override: những cảnh không khai báo phải ra đúng cùng take (cùng khoá SHA-256, cùng file mp3 — byte giống hệt).
- S18: ASR (faster-whisper small.en) trên take được chọn phải có từ "illustrative" (và không có "illustrated")."""
import hashlib, json, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'toolkit/factory'))
sys.modules['requests'] = None          # khoá API: voice_scene không được gọi mạng (import requests → lỗi)
import voice as V  # noqa: E402
import yaml  # noqa: E402

EP, out_p = sys.argv[1:3]
LINE = re.compile(r'^(S\d\d)\.(\d+)\s+(?:\{(\w+)\}\s+)?(.+?)\s*<!--')
rows = []
for ln in open(os.path.join(EP, 'story/script.md'), encoding='utf-8'):
    m = LINE.match(ln)
    if m: rows.append({'id': f'{m.group(1)}.{m.group(2)}', 'scene': m.group(1), 'text': m.group(4).strip()})
Y = yaml.safe_load(open(os.path.join(EP, 'episode.yaml')))
base, ov = Y['voice'], Y.get('voice_overrides') or {}
scenes = sorted({r['scene'] for r in rows})
md5 = lambda p: hashlib.md5(open(p, 'rb').read()).hexdigest()
rep = {'episode': EP, 'voice_overrides': ov, 'scenes': {}}
for sc in scenes:
    sents = [{'id': r['id'], 'scene': sc, 'text': r['text']} for r in rows if r['scene'] == sc]
    work = os.path.join(ROOT, 'moc-v/work/b1-wav')
    with_ov = V.voice_scene(V.scene_cfg(base, ov, sc), sents, os.path.join(EP, 'voice-takes'), work)
    try:
        no_ov = V.voice_scene(base, sents, os.path.join(EP, 'voice-takes'), work)
        no_take = os.path.basename(no_ov['mp3'])
    except BaseException as e:   # take mặc định có thể không còn trong voice-takes
        no_ov, no_take = None, f'(không có take mặc định: {e})'
    rep['scenes'][sc] = {'override': ov.get(sc), 'take': os.path.basename(with_ov['mp3']), 'seed': json.load(open(with_ov['mp3'][:-4] + '.json'))['seed'],
                         'take_without_override': no_take, 'cached': with_ov['cached'], 'mp3_md5': md5(with_ov['mp3']),
                         'identical_to_no_override': (no_ov is not None and with_ov['mp3'] == no_ov['mp3'] and md5(with_ov['mp3']) == md5(no_ov['mp3']))}
from faster_whisper import WhisperModel  # noqa: E402
wm = WhisperModel('small.en', device='cpu', compute_type='int8')
for sc in ov:
    for tag, take in (('override', rep['scenes'][sc]['take']), ('default', rep['scenes'][sc]['take_without_override'])):
        p = os.path.join(EP, 'voice-takes', take)
        if not os.path.exists(p): continue
        import subprocess, numpy as np
        pcm = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'], capture_output=True, check=True).stdout, np.float32)
        segs, _ = wm.transcribe(pcm, word_timestamps=True, language='en', beam_size=5, condition_on_previous_text=False)
        words = [re.sub(r'[^\w]', '', w.word).lower() for g in segs for w in g.words]
        rep['scenes'][sc][f'asr_{tag}'] = {'illustrative': 'illustrative' in words, 'illustrated': 'illustrated' in words}
others = [s for s in scenes if s not in ov]
rep['summary'] = {'scenes': len(scenes), 'all_cached_no_api': all(v['cached'] for v in rep['scenes'].values()),
                  'non_override_scenes_identical': sum(rep['scenes'][s]['identical_to_no_override'] for s in others), 'non_override_scenes': len(others),
                  'S18_illustrative': rep['scenes'].get('S18', {}).get('asr_override', {}).get('illustrative')}
json.dump(rep, open(out_p, 'w'), indent=1, ensure_ascii=False)
print(json.dumps(rep['summary'], ensure_ascii=False)); print(json.dumps({k: v for k, v in rep['scenes'].items() if k in ov}, ensure_ascii=False))
