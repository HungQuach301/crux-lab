"""Tập 3 · C4 animatic: lời theo cảnh (G-015 · chọn: Eric eleven_v3, theo cảnh, thẻ cảm xúc thưa, không speed, không giãn).
- Cảnh có chữ trùng table read C2 (`review-c2/table-read.json`, so theo chuỗi gửi TTS): cắt đúng đoạn của cảnh từ `review-c2/table-read.m4a`
  (bản ghép các take, mỗi take + 0,8 s lặng), ranh giới tìm bằng ASR mức từ. Không gọi ElevenLabs.
- Cảnh đổi chữ: sinh lại bằng chính hàm của `story/table_read.py` (seed 1; seed 2 chỉ khi ASR mất từ khoá), take tên theo hash chữ ở `animatic/work/takes/`.
Ra: animatic/work/voice/Sxx.wav (48 kHz mono), animatic/work/voice.wav (các cảnh nối, 0,8 s lặng sau mỗi cảnh), animatic/timing.json
(cảnh: start, dur, nguồn; câu: start, end theo ASR mức từ căn với chữ kịch bản), animatic/voice-report.json (ký tự EL, từ khoá mất).
    python3 episodes/ep003/animatic/voice.py
"""
import difflib, hashlib, json, os, re, subprocess, sys
ROOT = '/home/user/crux-lab'; EP = f'{ROOT}/episodes/ep003'; A = f'{EP}/animatic'; WK = f'{A}/work'
sys.path.insert(0, f'{EP}/story')
import table_read as TR  # noqa: E402
TR.TAKES = f'{WK}/takes'
GAP, SR = 0.8, 48000


def norm(s):
    return [t for t in re.sub(r"[^a-z0-9' ]", ' ', s.lower().replace('-', ' ')).split() if t]


def asr_words(path):
    return [(w['start'], w['end'], w['w']) for w in TR.asr(path)]


def dur(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p], capture_output=True, text=True).stdout)


def align(sentences, words, offset=0.0):
    """Câu kịch bản ↔ từ ASR: SequenceMatcher trên token; mốc câu = từ khớp đầu/cuối trong khoảng của câu (nội suy khi thiếu)."""
    st, owner = [], []
    for i, s in enumerate(sentences):
        toks = norm(s['text']); st += toks; owner += [i] * len(toks)
    at = [norm(w)[0] if norm(w) else '' for _, _, w in words]
    sm = difflib.SequenceMatcher(None, st, at, autojunk=False)
    hit = {}
    for a, b, n in sm.get_matching_blocks():
        for k in range(n):
            hit[a + k] = b + k
    out = []
    for i, s in enumerate(sentences):
        idx = [j for j, o in enumerate(owner) if o == i]
        m = [hit[j] for j in idx if j in hit]
        out.append({'id': s['id'], 'text': s['text'], 'start': words[min(m)][0] + offset if m else None,
                    'end': words[max(m)][1] + offset if m else None, 'matched': f'{len(m)}/{len(idx)}'})
    for k, o in enumerate(out):  # nội suy câu không khớp từ nào (hiếm)
        if o['start'] is None:
            prev = out[k - 1]['end'] if k else offset
            nxt = next((x['start'] for x in out[k + 1:] if x['start'] is not None), prev + 2)
            o['start'], o['end'] = prev + 0.1, nxt - 0.1
    return out


def main():
    os.makedirs(f'{WK}/voice', exist_ok=True); os.makedirs(TR.TAKES, exist_ok=True)
    rs = TR.rows(); scenes = sorted({r['scene'] for r in rs})
    texts = {sc: TR.scene_text([r for r in rs if r['scene'] == sc]) for sc in scenes}
    tr = json.load(open(f'{EP}/review-c2/table-read.json'))['scenes']
    src = f'{EP}/review-c2/table-read.m4a'
    # ranh giới cảnh trong table read: chữ của từng cảnh C2 căn trên ASR toàn file
    allw = asr_words(src) if any(tr[sc]['text'] == texts[sc] for sc in scenes) else []
    c2_sent = [{'id': sc, 'text': re.sub(r'\[[a-z ]+\]\s*', '', tr[sc]['text'])} for sc in scenes]
    c2_al = align(c2_sent, allw)
    report, sc_files = {'elChars': 0, 'scenes': {}}, {}
    for k, sc in enumerate(scenes):
        f = f'{WK}/voice/{sc}.wav'
        if tr[sc]['text'] == texts[sc]:
            a = max(0.0, c2_al[k]['start'] - 0.12)
            b = (c2_al[k + 1]['start'] - 0.12) if k + 1 < len(scenes) else dur(src)
            subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', f'{a:.3f}', '-to', f'{b:.3f}', '-i', src, '-af',
                            f'silenceremove=stop_periods=-1:stop_duration=0.5:stop_threshold=-45dB,afade=t=in:d=0.02,aresample={SR}', '-ac', '1', f], check=True)
            report['scenes'][sc] = {'source': 'table-read C2 (cắt)', 'span': [round(a, 3), round(b, 3)], 'take': tr[sc]['use'], 'elChars': 0}
        else:
            keys = [kk for r in rs if r['scene'] == sc for kk in r['keys']]
            takes = []
            for seed in (1, 2):
                p = f'{TR.TAKES}/{sc}.{hashlib.sha1(texts[sc].encode()).hexdigest()[:8]}.seed{seed}'
                m = TR.synth(texts[sc], p, seed); w = TR.asr(p + '.mp3')
                takes.append({'file': os.path.basename(p) + '.mp3', 'seed': seed, 'characterCost': m['characterCost'], 'missing': TR.match_keys(keys, w)})
                report['elChars'] += m['characterCost'] or 0
                if not takes[-1]['missing']:
                    break
            use = min(takes, key=lambda t: len(t['missing']))
            subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', f"{TR.TAKES}/{use['file']}", '-af', f'aresample={SR}', '-ac', '1', f], check=True)
            report['scenes'][sc] = {'source': 'ElevenLabs (sinh lại, chữ đổi)', 'text': texts[sc], 'takes': takes, 'use': use['file'], 'elChars': sum(t['characterCost'] or 0 for t in takes)}
        sc_files[sc] = f
    # time base: cảnh nối tiếp, GAP lặng sau mỗi cảnh; mốc câu bằng ASR trên chính file cảnh
    t, tl = 0.0, {'gap': GAP, 'scenes': [], 'sentences': []}
    for sc in scenes:
        d = dur(sc_files[sc]); sents = [{'id': r['id'], 'text': r['text']} for r in rs if r['scene'] == sc]
        al = align(sents, asr_words(sc_files[sc]), offset=t)
        tl['scenes'].append({'id': sc, 'start': round(t, 3), 'dur': round(d, 3), 'file': os.path.relpath(sc_files[sc], A)})
        for x in al:
            tl['sentences'].append({**x, 'scene': sc, 'start': round(x['start'], 3), 'end': round(x['end'], 3)})
        t += d + GAP
    tl['total'] = round(t, 3)
    lst = f'{WK}/voice-list.txt'
    with open(lst, 'w') as fh:
        for sc in scenes:
            fh.write(f"file '{sc_files[sc]}'\n")
    flt = ''.join(f'[{k}:a]apad=pad_dur={GAP}[a{k}];' for k in range(len(scenes))) + ''.join(f'[a{k}]' for k in range(len(scenes))) + f'concat=n={len(scenes)}:v=0:a=1[o]'
    inp = [x for sc in scenes for x in ('-i', sc_files[sc])]
    subprocess.run(['ffmpeg', '-y', '-v', 'error', *inp, '-filter_complex', flt, '-map', '[o]', '-ar', str(SR), f'{WK}/voice.wav'], check=True)
    json.dump(tl, open(f'{A}/timing.json', 'w'), indent=1)
    json.dump(report, open(f'{A}/voice-report.json', 'w'), indent=1, ensure_ascii=False)
    print('total', tl['total'], 's; EL chars', report['elChars'], '; weak sentence matches:',
          [(s['id'], s['matched']) for s in tl['sentences'] if s['matched'].split('/')[0] in ('0', '1')])


if __name__ == '__main__':
    main()
