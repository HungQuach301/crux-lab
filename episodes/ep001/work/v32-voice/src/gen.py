"""C4 · lời đọc cả tập v3.2 theo công thức bản Y (V3 của thử mù): mỗi CẢNH một lần gọi, eleven_v3, Eric, không voice_settings/speed,
seed 1; [beat] trong cảnh -> xuống đoạn (dòng trống) như V3; thẻ cảm xúc đặt đầu câu. Sinh lại tối đa 1 lần/cảnh (seed 2) chỉ khi ASR
thấy mất từ khoá/số/tên (hoặc lỗi đo được, ghi lý do tay qua --regen Sxx:lý_do). Khoá API do proxy tiêm; không đọc, không in.
    python3 gen.py --dry          # in chữ gửi + số ký tự, không gọi API
    python3 gen.py                # sinh cảnh chưa có take
"""
import json, os, re, sys, tempfile
ROOT = '/home/user/crux-lab'; EP = f'{ROOT}/episodes/ep001'; W = f'{EP}/work/v32-voice'; TAKES = f'{W}/takes'
sys.path.insert(0, f'{EP}/work/voice-test/src')
import gen as VT  # synth(), asr(), scene_text() của thử mù (URL, model, voice cố định trong đó)
from r_audio import key_words, match_keys
from parse import parse, to_tts

SRC = f'{EP}/story/script-v3.2.md'
# 8 thẻ theo story/voice-tags.md (thứ tự trong kịch bản); tách TRƯỚC khi parse (parse.py coi [chữ] là claim ID)
TAGS8 = ['[softly]', '[curious]', '[thoughtful]', '[serious]', '[warmly]', '[serious]', '[matter-of-fact]', '[softly]']
Y_TAGS = {4: '[softly]', 7: '[curious]', 50: '[thoughtful]', 52: '[serious]'}  # vị trí đã nghe trong bản Y
REV = {'S18': 'r2'}  # 30/09: S18 sửa chữ, sinh lại (take cũ giữ trong gen-result.json khoá 'S18@r1')
TAG_RE = re.compile(r'^\[(softly|curious|thoughtful|serious|warmly|matter-of-fact)\]\s+')


def rows_v32():
    lines = open(SRC, encoding='utf-8').read().split('\n'); found = []; out = []
    for ln in lines:
        m = TAG_RE.match(ln)
        if m: found.append(('[' + m.group(1) + ']', ln[m.end():].strip())); ln = ln[m.end():]
        out.append(ln)
    assert [t for t, _ in found] == TAGS8, found
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f: f.write('\n'.join(out)); tmp = f.name
    rows = parse(tmp); os.unlink(tmp)
    ref = parse(f'{EP}/story/script-v3.1.md')
    # 30/09 (C5, chủ dự án): S18.4–S18.6 bỏ dạng sở hữu (A14 "Walt's"→"Waltz"); mọi câu khác vẫn phải trùng v3.1
    assert len(rows) == 105 and all(a['text_plain'] == b['text_plain'] or (a['scene'] == 'S18' and a['text_plain'].startswith('For '))
                                    for a, b in zip(rows, ref)), 'v3.2 bỏ thẻ phải trùng v3.1 (trừ S18 thước)'
    for i, (r, t) in enumerate(zip(rows, to_tts([r['text_plain'] for r in rows]))): r['tts_text'] = t; r['n'] = i + 1
    for r, k in zip(rows, key_words([{'text': r['text_plain']} for r in rows])): r['keys'] = k
    assert not any('[' in r['tts_text'] or ']' in r['tts_text'] for r in rows)
    tags = {}
    for tag, line in found:  # thẻ -> câu đầu tiên của dòng lời đó
        hit = [r for r in rows if r['script_line'] == line and r['text_plain'] and line.startswith(r['text_plain'][:20])]
        assert len(hit) == 1, (tag, line, hit); tags[hit[0]['n']] = tag
    assert len(tags) == 8
    for n, t in Y_TAGS.items(): assert tags[n] == t, (n, tags.get(n))
    y = json.load(open(f'{EP}/work/voice-test/gen-result.json'))['result']['V3']
    for n, t in Y_TAGS.items():  # cùng câu (từng ký tự) với bản Y
        assert any(f'{t} {rows[n - 1]["tts_text"]}' in s['text_sent'] for s in y), n
    return rows, tags


def scenes(rows, tags):
    out = []
    for sc in [f'S{i:02d}' for i in range(1, 21)]:
        rs = [r for r in rows if r['scene'] == sc]; text = VT.scene_text(rs, tags)
        out.append({'scene': sc, 'rows': rs, 'text': text})
    return out


def main():
    rows, tags = rows_v32(); scs = scenes(rows, tags)
    nt = sum(s['text'].count(t) for s in scs for t in set(TAGS8)); assert nt == 8, nt
    total = sum(len(s['text']) for s in scs)
    if '--dry' in sys.argv:
        for s in scs: print(s['scene'], len(s['text']), repr(s['text'])[:160])
        print('tags', tags, 'chars total', total); return
    regen = dict(a.split(':', 1) for a in sys.argv[1:] if re.match(r'^S\d\d:', a))  # sinh lại tay (lỗi đo được), ghi lý do
    resf = f'{W}/gen-result.json'; res = json.load(open(resf)) if os.path.exists(resf) else {}
    for s in scs:
        sc = s['scene']; keys = [k for r in s['rows'] for k in r['keys']]
        e = res.get(sc) or {'scene': sc, 'n': [r['n'] for r in s['rows']], 'text_sent': s['text'], 'tags': {str(r['n']): tags[r['n']] for r in s['rows'] if r['n'] in tags},
                            'sentences': [r['tts_text'] for r in s['rows']], 'text_plain': [r['text_plain'] for r in s['rows']], 'takes': []}
        assert e['text_sent'] == s['text']
        want = 1 if not e['takes'] else (2 if (e['takes'][0]['missing'] or sc in regen) else len(e['takes']))
        while len(e['takes']) < want:
            seed = len(e['takes']) + 1; p = f'{TAKES}/{sc}{REV.get(sc, "")}.seed{seed}'
            m = VT.synth(s['text'], p, seed); assert 'error' not in m, m
            w = VT.asr(p + '.mp3')
            tk = {'file': os.path.basename(p) + '.mp3', 'seed': seed, 'characterCost': m['characterCost'], 'len': m['len'], 'requestId': m['requestId'],
                  'asr': ' '.join(x['w'] for x in w), 'asr_words': w, 'missing': match_keys(keys, w)}
            if seed == 2: tk['why'] = ('ASR mất: ' + ', '.join(e['takes'][0]['missing'])) if e['takes'][0]['missing'] else regen[sc]
            e['takes'].append(tk)
            print(sc, 'seed', seed, len(s['text']), 'cost', m['characterCost'], 'missing', tk['missing'], '|', tk['asr'][:200], flush=True)
            res[sc] = e; json.dump(res, open(resf, 'w'), indent=1, ensure_ascii=False)
        # chọn: ít từ khoá mất hơn; hoà -> seed 1 (không chọn theo tai)
        e['use'] = min(e['takes'], key=lambda t: len(t['missing']))['file']; res[sc] = e
    json.dump(res, open(resf, 'w'), indent=1, ensure_ascii=False)
    sent = sum(t['len'] for e in res.values() for t in e['takes']); cost = sum(t['characterCost'] for e in res.values() for t in e['takes'])
    print('calls', sum(len(e['takes']) for e in res.values()), 'sent', sent, 'charged', cost)


if __name__ == '__main__':
    main()
