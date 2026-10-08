"""Tập 6 · bản đọc thử trước G1 (episode.md §3.9): sinh giọng S01–S04 bằng toolkit/factory/voice.py (cùng cache với nhà máy:
take ở episodes/ep005/voice-takes/, commit), đặt cảnh nối nhau như nhà máy (đuôi 1,0 s/cảnh, ident 3 s sau S03), đo M1–M5 trên
mốc thời gian thật của ElevenLabs, ASR kiểm chữ. Ghép clip lời cold open S01–S03 cho gói G1.
    python3 episodes/ep005/story/table_read.py [--dry]"""
import json, os, re, subprocess, sys
ROOT = '/home/user/crux-lab'; EP = f'{ROOT}/episodes/ep006'
sys.path.insert(0, f'{ROOT}/toolkit/factory')
import voice as V  # noqa: E402
import yaml  # noqa: E402

SCENES = sys.argv[sys.argv.index('--scenes') + 1].split(',') if '--scenes' in sys.argv else ['S01', 'S02', 'S03', 'S04']
CLIP_TO = sys.argv[sys.argv.index('--clip-to') + 1] if '--clip-to' in sys.argv else 'S03'
CAST = sys.argv[sys.argv.index('--cast') + 1].split(',') if '--cast' in sys.argv else []; TAIL = 1.0; IDENT_AFTER = 'S03'; IDENT = 3.0
LINE = re.compile(r'^(S\d\d)\.(\d+)\s+(?:\{(\w+)\}\s+)?(.+?)\s*<!--')


def rows():
    out = []
    for ln in open(f'{EP}/story/script.md', encoding='utf-8'):
        m = LINE.match(ln)
        if m and m.group(1) in SCENES:
            out.append({'id': f'{m.group(1)}.{m.group(2)}', 'scene': m.group(1), 'role': m.group(3), 'text': m.group(4).strip()})
    return out


def main():
    cfg = yaml.safe_load(open(f'{EP}/episode.yaml'))['voice']
    rs = rows()
    if '--dry' in sys.argv:
        sp = V.to_spoken([r['text'] for r in rs]); print('chars', sum(len(s) + 1 for s in sp))
        for r, s in zip(rs, sp): print(r['id'], r['role'], s)
        return
    t, timeline, wavs, chars = 0.0, [], [], 0
    for sc in SCENES:
        v = V.voice_scene(cfg, [r for r in rs if r['scene'] == sc], f'{EP}/voice-takes', f'{EP}/work/voice')
        chars += 0 if v['cached'] else v['chars']
        for s in v['sentences']:
            r = next(x for x in rs if x['id'] == s['id'])
            timeline.append({**r, 'start': round(t + s['start'], 2), 'end': round(t + s['end'], 2)})
        wavs.append((sc, v['wav'], t)); t += v['duration'] + TAIL + (IDENT if sc == IDENT_AFTER else 0)
    # M1–M5
    first = lambda role: next((x for x in timeline if x['role'] == role), None)
    M = {'M1 hook ends ≤ 5.0': first('hook')['end'], 'M2 promise ends ≤ 30': first('promise')['end'],
         'M3 question ≤ 30': (first('question') or first('hook'))['end']}
    blk, longest = None, 0.0
    prev_end = None
    for x in timeline:  # khối = câu constraint/define liền nhau; khoảng lặng > 1,5 s (ident, đổi cảnh dài) cắt khối
        if x['start'] >= 60: break
        if x['role'] in ('constraint', 'define'):
            if blk is None or (prev_end is not None and x['start'] - prev_end > 1.5): blk = x['start']
            longest = max(longest, min(x['end'], 60) - blk)
        else: blk = None
        prev_end = x['end']
    M['M4 longest constraint/define block 0–60 s ≤ 10'] = round(longest, 2)
    stake = re.compile(r'\b(' + '|'.join(CAST + ['you', 'your']) + r')\b', re.I)
    M['M5 character/stake returns ≤ 45'] = next((x['start'] for x in timeline if x['start'] > first('promise')['end'] and stake.search(x['text'])), None)
    m6 = 0.0  # M6: mỗi câu promise_character được trả (tên trong CAST xuất hiện) ≤ 90 s; ngoài phần đọc → None (ước ở check_script)
    for i, x in enumerate(timeline):
        if x['role'] == 'promise_character':
            pay = next((y for y in timeline[i + 1:] if any(re.search(r'\b' + c + r'\b', y['text']) for c in CAST)), None)
            m6 = max(m6, pay['start'] - x['end']) if pay and m6 is not None else None
    M['M6 character promise paid ≤ 90'] = None if m6 is None else round(m6, 2)
    lim = {'M1': 5.0, 'M2': 30, 'M3': 30, 'M4': 10, 'M5': 45, 'M6': 90}
    res = {k: {'value': v, 'pass': v is not None and v <= lim[k[:2]]} for k, v in M.items()}
    # clip S01–S03 + ASR
    os.makedirs(f'{EP}/review-g1', exist_ok=True)
    parts = wavs[:SCENES.index(CLIP_TO) + 1]
    inputs, flt = [], []
    for i, (sc, w, t0) in enumerate(parts):
        inputs += ['-i', w]; flt.append(f'[{i}:a]adelay={int(t0 * 1000)}[a{i}]')
    flt.append(''.join(f'[a{i}]' for i in range(len(parts))) + f'amix=inputs={len(parts)}:normalize=0[o]')
    clip = f'{EP}/review-g1/cold-open.m4a'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', *inputs, '-filter_complex', ';'.join(flt), '-map', '[o]', '-c:a', 'aac', '-b:a', '160k', clip], check=True)
    from faster_whisper import WhisperModel
    segs, _ = WhisperModel('small.en', device='cpu', compute_type='int8').transcribe(clip)
    asr = ' '.join(s.text.strip() for s in segs)
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', clip], capture_output=True, text=True).stdout)
    rep = {'el_chars_spent': chars, 'clip': os.path.relpath(clip, ROOT), 'clip_s': round(dur, 1), 'M': res, 'timeline': timeline, 'asr': asr}
    json.dump(rep, open(f'{EP}/review-g1/table-read.json', 'w'), indent=1, ensure_ascii=False)
    print(json.dumps({k: rep[k] for k in ('el_chars_spent', 'clip_s', 'M')}, ensure_ascii=False, indent=1))
    for x in timeline: print(f"{x['start']:6.2f}–{x['end']:6.2f} {x['id']} {x['role'] or ''}")
    print('ASR:', asr)


if __name__ == '__main__':
    main()
