#!/usr/bin/env python3
"""Tập 2 · C4 animatic timing: the ONLY timing the animatic reads (animatic/timing.json) + the temporary narration track.

    python3 src/make_timing.py            # ASR (cached in work/asr/), align to script v5 sentences, write timing.json + work/narration.m4a

Pattern: episodes/ep001/animatic/src/make_timing.py. Here there is no TTS timeline with sentence marks (the takes are one
ElevenLabs call per scene), so sentence times come from faster-whisper `small.en` (CPU, int8) word timestamps on each
scene's chosen take (`use` in review-c2/table-read.json), aligned word-by-word (difflib) to the spoken form of the script v5
sentences (story/table_read.py rows(): the same text that was sent to the voice). Words the ASR spells differently (numbers)
are placed by spreading the unmatched ASR words of the gap over them.

Narration = the takes joined like table_read.py (aresample 44100, mono, apad) with each scene padded to a whole number of
frames: 0.8 s after every scene, except S11 (method card held for >= 1 s per 3 words of the card: padded to CARD_S) and
S13 (end-screen tail, padded to END_S). Picture scene k = [offset_k, offset_k + whole_k) on the narration clock, so cuts land
on frames and the picture never drifts from the voice. When the voice is regenerated: update table-read.json, delete
work/asr/, rerun this, then build_anchors.py and re-render (every action is anchored to a sentence + keyword)."""
import difflib, importlib.util, json, math, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__)); AN = os.path.dirname(HERE); EP = os.path.dirname(AN); ROOT = os.path.dirname(os.path.dirname(EP))
TAKES = f'{EP}/review-c2/takes'; ASR = f'{AN}/work/asr'
PAD = 0.8
CARD_WORDS_FILE = f'{HERE}/method_card.json'   # the card's lines (words counted here and in check.py)
END_S = 16.0                                     # S13 end-screen tail (script: 15-20 s)
# silence inserted AFTER a sentence, inside its scene (owner C4 Q3a: S10.1 figures held >= 3 s each; voice unchanged)
INSERT = {'S10.1': 2.0}

spec = importlib.util.spec_from_file_location('tr', f'{EP}/story/table_read.py'); tr = importlib.util.module_from_spec(spec)
sys.argv = [sys.argv[0]]; spec.loader.exec_module(tr)
rows = tr.rows()
script_txt = {}
for ln in open(f'{EP}/story/script.md', encoding='utf-8'):
    m = re.match(r'^(S\d\d\.\d+) \| (.+?) \| ', ln)
    if m: script_txt[m.group(1)] = re.sub(r'^\[[a-z\- ]+\]\s+', '', m.group(2).strip())
read = json.load(open(f'{EP}/review-c2/table-read.json'))['scenes']
scenes = sorted({r['scene'] for r in rows})
assert scenes == [f'S{i:02d}' for i in range(1, 14)], scenes

def norm(s): return [w for w in re.sub(r"[^a-z0-9']+", ' ', s.lower().replace('’', "'")).split() if w]

def dur(f):
    out = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-ac', '1', '-ar', '44100', '-f', 's16le', '-'], capture_output=True, check=True).stdout
    return len(out) / 2 / 44100

def asr(sc, f):
    p = f'{ASR}/{sc}.json'
    if os.path.exists(p) and json.load(open(p))['file'] == os.path.basename(f): return json.load(open(p))['words']
    from faster_whisper import WhisperModel
    m = WhisperModel('small.en', device='cpu', compute_type='int8')
    segs, _ = m.transcribe(f, word_timestamps=True, language='en', beam_size=5, condition_on_previous_text=False)
    w = [{'w': x.word.strip(), 'start': round(x.start, 3), 'end': round(x.end, 3)} for g in segs for x in g.words]
    os.makedirs(ASR, exist_ok=True); json.dump({'file': os.path.basename(f), 'words': w}, open(p, 'w'), indent=0); return w

card = json.load(open(CARD_WORDS_FILE))
WRD = lambda s: len([w for w in s.split() if re.search(r'[A-Za-z0-9]', w)])
card_words = WRD(''.join(p[0] for p in card['title'])) + sum(WRD(l['text']) for l in card['lines'])
CARD_S = math.ceil(card_words / 3.0 + 3.5)          # >= 1 s per 3 words once fully shown, plus the line-by-line reveal and a margin

out_sc, offset, notes = [], 0.0, []
for sc in scenes:
    rs = [r for r in rows if r['scene'] == sc]
    e = read[sc]; f = f"{TAKES}/{e['use']}"
    sent_text = tr.scene_text(rs)
    if e['text'] != sent_text: notes.append(f'{sc}: take text differs from script v5 spoken text')
    words = asr(sc, f)
    # flatten: script tokens (per sentence) and ASR tokens (per word)
    S_tok, S_sid = [], []
    for r in rs:
        for t in norm(r['tts']): S_tok.append(t); S_sid.append(r['id'])
    A_tok, A_w = [], []
    for i, w in enumerate(words):
        for t in norm(w['w']): A_tok.append(t); A_w.append(i)
    sm = difflib.SequenceMatcher(a=S_tok, b=A_tok, autojunk=False)
    st, en = [None] * len(S_tok), [None] * len(S_tok)
    pairs = []
    for a, b, n in sm.get_matching_blocks():
        for k in range(n): pairs.append((a + k, b + k))
    for a, b in pairs: st[a] = words[A_w[b]]['start']; en[a] = words[A_w[b]]['end']
    # gaps: spread unmatched ASR words of the gap over the unmatched script tokens
    anchors = [(-1, -1)] + pairs + [(len(S_tok), len(A_tok))]
    for (a0, b0), (a1, b1) in zip(anchors, anchors[1:]):
        if a1 - a0 <= 1: continue
        ws = sorted({A_w[b] for b in range(b0 + 1, b1)})
        if ws: t0, t1 = words[ws[0]]['start'], words[ws[-1]]['end']
        else:
            t0 = en[a0] if a0 >= 0 else (words[0]['start'] if words else 0.0)
            t1 = st[a1] if a1 < len(S_tok) else (words[-1]['end'] if words else t0)
        n = a1 - a0 - 1
        for j in range(n):
            st[a0 + 1 + j] = t0 + (t1 - t0) * j / n; en[a0 + 1 + j] = t0 + (t1 - t0) * (j + 1) / n
    d = dur(f)
    ins = [(sid, P) for sid, P in INSERT.items() if sid.startswith(sc + '.')]
    cut = None
    if ins:
        sid, P = ins[0]
        ia = [k for k, x in enumerate(S_sid) if x == sid][-1]
        cut = (en[ia] + st[ia + 1]) / 2 if ia + 1 < len(S_tok) else d
        for k in range(len(S_tok)):
            if st[k] >= cut: st[k] += P; en[k] += P
        d_ins = P
    else: d_ins = 0.0
    pad = PAD
    if sc == 'S11': pad = max(PAD, CARD_S - d)
    if sc == 'S13': pad = max(PAD, END_S - d)
    whole = math.ceil((d + d_ins + pad) * 30 - 1e-6) / 30
    sents = []
    for r in rs:
        idx = [k for k, s in enumerate(S_sid) if s == r['id']]
        toks = [{'t': S_tok[k], 'start': round(offset + st[k], 3), 'end': round(offset + en[k], 3)} for k in idx]
        matched = sum(1 for k in idx if any(p[0] == k for p in pairs))
        sents.append({'id': r['id'], 'start': toks[0]['start'], 'end': toks[-1]['end'], 'text': script_txt[r['id']], 'spoken': r['tts'],
                      'tag': r['tag'], 'matched': f'{matched}/{len(idx)}', 'words': toks})
    out_sc.append({'id': sc, 'start': round(offset, 4), 'end': round(offset + whole, 4), 'dur': round(whole, 4), 'take': e['use'],
                   'audio_s': round(d, 3), 'pad_s': round(whole - d - d_ins, 3), 'inserted': [{'after': ins[0][0], 'at_take_s': round(cut, 3), 'pause_s': ins[0][1]}] if ins else [], 'sentences': sents})
    offset += whole

timing = {'_about': 'C4 animatic timing (generated by src/make_timing.py; do not edit by hand). Absolute seconds on the narration '
                    'track work/narration.m4a. Scene k = [start, end): its take, then silence (0.8 s; S11 held for the method card; '
                    'S13 end-screen tail). Sentence/word times: faster-whisper small.en word timestamps on the take, aligned to the '
                    'script v5 spoken text.', 'total_s': round(offset, 4), 'fps': 30, 'pad_s': PAD,
          'method_card': {'words': card_words, 'min_s': round(card_words / 3, 2), 'scene_s': None}, 'notes': notes, 'scenes': out_sc}
timing['method_card']['scene_s'] = next(s['dur'] for s in out_sc if s['id'] == 'S11')
json.dump(timing, open(f'{AN}/timing.json', 'w'), indent=1, ensure_ascii=False)
# narration: same ffmpeg filter as story/table_read.py, each scene padded to its whole frame length
inp, flt = [], ''
for k, s in enumerate(out_sc):
    inp += ['-i', f"{TAKES}/{s['take']}"]
    if s['inserted']:
        c, P = s['inserted'][0]['at_take_s'], s['inserted'][0]['pause_s']
        flt += (f"[{k}:a]aresample=44100,aformat=channel_layouts=mono,asplit=2[p{k}][q{k}];[p{k}]atrim=end={c:.4f},asetpts=PTS-STARTPTS,apad=pad_dur={P:.4f}[pp{k}];"
                f"[q{k}]atrim=start={c:.4f},asetpts=PTS-STARTPTS[qq{k}];[pp{k}][qq{k}]concat=n=2:v=0:a=1,apad=whole_dur={s['dur']:.6f}[a{k}];")
    else:
        flt += f"[{k}:a]aresample=44100,aformat=channel_layouts=mono,apad=whole_dur={s['dur']:.6f}[a{k}];"
flt += ''.join(f'[a{k}]' for k in range(len(out_sc))) + f'concat=n={len(out_sc)}:v=0:a=1[o]'
os.makedirs(f'{AN}/work', exist_ok=True)
subprocess.run(['ffmpeg', '-y', '-v', 'error', *inp, '-filter_complex', flt, '-map', '[o]', '-c:a', 'aac', '-b:a', '128k', f'{AN}/work/narration.m4a'], check=True)
for s in out_sc:
    print(s['id'], f"{s['start']:7.2f} {s['end']:7.2f} {s['dur']:6.2f}s  audio {s['audio_s']:.2f}  ", ' '.join(f"{x['id'][4:]}:{x['start']-s['start']:.1f}-{x['end']-s['start']:.1f}({x['matched']})" for x in s['sentences']))
print('total', round(offset, 2), 's; card words', card_words, '-> S11', timing['method_card']['scene_s'], 's;', notes)
