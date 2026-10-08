"""Tập 6 · lời theo cảnh (episode.md §4): mỗi cảnh một lần gọi ElevenLabs qua toolkit/factory/voice.py (cùng cache với nhà máy,
take ở episodes/ep006/voice-takes/, commit), rồi ASR kiểm từ khoá (checks/py/r_audio.py key_words/match_keys, chỉ đọc).
Chỉ sinh cảnh có chữ mới; cảnh trùng băm lấy từ cache.
    python3 episodes/ep006/story/voice_scenes.py [--dry] [--skip S03,S12] [--only S05,S06]"""
import json, os, re, sys
ROOT = '/home/user/crux-lab'; EP = f'{ROOT}/episodes/ep006'
sys.path[:0] = [f'{ROOT}/toolkit/factory', f'{ROOT}/checks/py']
import voice as V  # noqa: E402
import yaml  # noqa: E402
from r_audio import key_words, match_keys  # noqa: E402

LINE = re.compile(r'^(S\d\d)\.(\d+)\s+(?:\{(\w+)\}\s+)?(.+?)\s*<!--')
TAG = re.compile(r'^\[[a-z ]+\]\s+')


def pcm16k(path):
    # av của faster_whisper lệch phiên bản trong container (metadata_errors) → giải mã bằng ffmpeg
    import subprocess, numpy as np
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-f', 's16le', '-ac', '1', '-ar', '16000', '-'], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32) / 32768


def rows():
    out = []
    for ln in open(f'{EP}/story/script.md', encoding='utf-8'):
        m = LINE.match(ln)
        if m: out.append({'id': f'{m.group(1)}.{m.group(2)}', 'scene': m.group(1), 'text': m.group(4).strip()})
    for r, k in zip(out, key_words([{'text': TAG.sub('', r['text'])} for r in out])): r['keys'] = k
    return out


def arg(name):
    return sys.argv[sys.argv.index(name) + 1].split(',') if name in sys.argv else []


def main():
    cfg = yaml.safe_load(open(f'{EP}/episode.yaml'))['voice']
    rs = rows(); scenes = sorted({r['scene'] for r in rs})
    scenes = [s for s in scenes if s not in arg('--skip') and (not arg('--only') or s in arg('--only'))]
    if '--dry' in sys.argv:
        for sc in scenes:
            sp = V.to_spoken([r['text'] for r in rs if r['scene'] == sc]); print(sc, sum(len(s) + 1 for s in sp) - 1)
        print('chars', sum(sum(len(s) + 1 for s in V.to_spoken([r['text'] for r in rs if r['scene'] == sc])) - 1 for sc in scenes)); return
    from faster_whisper import WhisperModel
    wm = WhisperModel('small.en', device='cpu', compute_type='int8')
    rep_p = f'{EP}/review-g1/voice-scenes.json'
    rep = json.load(open(rep_p)) if os.path.exists(rep_p) else {}
    for sc in scenes:
        sents = [r for r in rs if r['scene'] == sc]
        v = V.voice_scene(cfg, [{'id': r['id'], 'scene': sc, 'text': r['text']} for r in sents], f'{EP}/voice-takes', f'{EP}/work/voice')
        segs, _ = wm.transcribe(pcm16k(v['wav']), word_timestamps=True, language='en', beam_size=5, condition_on_previous_text=False)
        words = [{'w': w.word.strip(), 'start': w.start, 'end': w.end} for g in segs for w in g.words]
        keys = [k for r in sents for k in r['keys']]
        miss = match_keys(keys, words) if keys else []
        rep[sc] = {'take': os.path.basename(v['mp3']), 'duration': v['duration'], 'charsSpent': 0 if v['cached'] else v['chars'],
                   'keys': len(keys), 'missingKeys': miss, 'asr': ' '.join(w['w'] for w in words)}
        print(sc, v['duration'], 'chars', rep[sc]['charsSpent'], 'missing', miss, flush=True)
        json.dump(rep, open(rep_p, 'w'), indent=1, ensure_ascii=False)
    print('total chars spent', sum(rep[s]['charsSpent'] for s in scenes), 'dur', round(sum(rep[s]['duration'] for s in rep), 1))


if __name__ == '__main__':
    main()
