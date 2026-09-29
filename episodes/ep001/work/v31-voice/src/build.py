"""Ghép lời đọc v3.1: cắt mỗi take về đoạn có tiếng (-50 dBFS, cửa sổ 10 ms) +40 ms trước / +120 ms sau, fade 5 ms; không cắt trong câu,
không giãn/nén. Nghỉ do dựng: 0,45 / 1,0 [beat] / 1,4 cảnh / 2,0 sequence; 0,5 s đầu, 1,0 s cuối. Chỉ gain."""
import json, os, sys
import numpy as np, pyloudnorm as pyln, av
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen import decode, span, EP, ROOT, MODEL, VOICE
SR = 48000; LEAD, TAIL = 0.5, 1.0; TARGET = -19.5
OUT = f'{EP}/out/voice-v31'; RC4 = f'{EP}/review-c4'
os.makedirs(OUT, exist_ok=True); os.makedirs(RC4, exist_ok=True)
g = json.load(open(f'{EP}/work/v31-voice/gen-result.json')); rows = g['rows']
clips = []
for r in rows:
    x = decode(os.path.join(ROOT, r['take_file']), SR); a, b = span(x, SR)
    s, e = max(0, int((a - 0.04) * SR)), min(len(x), int((b + 0.12) * SR)); c = x[s:e].copy()
    f = int(0.005 * SR); ramp = np.linspace(0, 1, f); c[:f] *= ramp; c[-f:] *= ramp[::-1]
    clips.append(c); r['take_raw_s'] = round(len(x) / SR, 3); r['trim_in_take_s'] = [round(s / SR, 3), round(e / SR, 3)]
t = LEAD; parts = [np.zeros(int(LEAD * SR))]
for r, c in zip(rows, clips):
    if r['n'] > 1:
        parts.append(np.zeros(int(round(r['pause_before_s'] * SR)))); t += r['pause_before_s']
    r['start_s'] = round(t, 3); parts.append(c); t += len(c) / SR; r['end_s'] = round(t, 3)
    t = sum(len(p) for p in parts) / SR  # giữ mốc khớp mẫu
    r['end_s'] = round(t, 3); r['duration_s'] = round(len(c) / SR, 3)
parts.append(np.zeros(int(TAIL * SR))); y = np.concatenate(parts)
meter = pyln.Meter(SR); before = meter.integrated_loudness(y)
gain = 10 ** ((TARGET - before) / 20); peak = np.abs(y).max() * gain
if 20 * np.log10(peak) > -1.0: gain *= 10 ** ((-1.0 - 20 * np.log10(peak)) / 20)
y *= gain; lufs = meter.integrated_loudness(y); pk = 20 * np.log10(np.abs(y).max())
# AAC 96 kbps mono
o = av.open(f'{RC4}/narration.m4a', 'w'); st = o.add_stream('aac', rate=SR); st.bit_rate = 96000; st.layout = 'mono'
a32 = y.astype(np.float32).reshape(1, -1)
for i in range(0, a32.shape[1], 1024):
    fr = av.AudioFrame.from_ndarray(np.ascontiguousarray(a32[:, i:i + 1024]), format='flt', layout='mono'); fr.sample_rate = SR
    for p in st.encode(fr): o.mux(p)
for p in st.encode(None): o.mux(p)
o.close()
total = len(y) / SR
# câu
sent = []
for r in rows:
    nw = len(r['tts_text'].split())
    ws = r['asr_words']; asp = ws[-1]['end'] - ws[0]['start'] if ws else 0
    sent.append({'n': r['n'], 'sequence': r['sequence'], 'scene': r['scene'], 'script_line': r['script_line'], 'text_plain': r['text_plain'], 'tts_text': r['tts_text'],
                 'model': MODEL, 'voice': 'Eric (cjVigY5qzO86Huf0OWal)', 'voice_settings': 'API default (not sent); no speed', 'seed': r['seed'],
                 'source': r['source'], 'c2_n': r.get('c2_n'), 'c2_take': r.get('c2_take'), 'regenerated': r['regenerated'],
                 'generations_this_step': sum(1 for tk in r['takes'] if 'characterCost' in tk),
                 'character_cost': sum(tk.get('characterCost', 0) for tk in r['takes']),
                 'take_file': r['take_file'], 'take_raw_s': r['take_raw_s'], 'duration_s': r['duration_s'], 'spoken_words': nw,
                 'wpm_ref': round(60 * nw / r['duration_s'], 1), 'wpm_asr_span_ref': round(60 * nw / asp, 1) if asp else None,
                 'keys': r['keys'], 'missing_keys_first_take': r['missing_keys_first_take'], 'missing_keys_final': r['missing_keys_final'], 'asr_text': r['asr_text'],
                 'takes': [{k: v for k, v in tk.items() if k != 'words'} for tk in r['takes']]})
json.dump({'source': 'episodes/ep001/story/script-v3.1.md', 'model': MODEL + ' (only model)', 'voice': 'Eric cjVigY5qzO86Huf0OWal (chosen at C3, G-010 · chọn)',
           'endpoint': 'POST /v1/text-to-speech/{voice}/with-timestamps?output_format=mp3_44100_128, body {text, model_id, seed}; no speed, no voice_settings',
           'normalization': 'toolkit/voice/normalize.js toSpoken(); pre-step "Month D," -> ordinal words; post-step "N dollars loan/bill" -> "N dollar loan/bill"; first letter capitalised (as C2)',
           'reuse_rule': 'take C2 reused when tts_text is byte-identical to the C2 tts_text (same model, voice, default settings)',
           'asr': 'faster-whisper small.en int8 beam 5; keys via checks/py/r_audio.py key_words/match_keys (imported only)',
           'sentences': sent}, open(f'{OUT}/sentences.json', 'w'), indent=1, ensure_ascii=False)
tl = {'total_s': round(total, 3), 'sample_rate': SR, 'lead_s': LEAD, 'tail_s': TAIL,
      'pauses_s': {'same_scene': 0.45, 'beat': 1.0, 'scene': 1.4, 'sequence': 2.0}, 'note': 'Pauses are editorial defaults for C4 to retime against picture; no cut inside any take.',
      'trim': 'speech span (-50 dBFS, 10 ms windows) +40 ms before / +120 ms after, 5 ms fades',
      'loudness': {'before_gain_lufs': round(before, 2), 'gain_db': round(20 * np.log10(gain), 2), 'integrated_lufs': round(lufs, 2), 'sample_peak_dbfs': round(pk, 2), 'processing': 'gain only'},
      'file': 'episodes/ep001/review-c4/narration.m4a (AAC 96 kbps mono 48 kHz)',
      'events': []}
prev = None
for r in rows:
    if r['n'] > 1: tl['events'].append({'type': 'pause', 'kind': r['pause_kind'], 'start_s': round(r['start_s'] - r['pause_before_s'], 3), 'end_s': r['start_s'], 'dur_s': r['pause_before_s'], 'before_n': r['n']})
    tl['events'].append({'type': 'sentence', 'n': r['n'], 'sequence': r['sequence'], 'scene': r['scene'], 'start_s': r['start_s'], 'end_s': r['end_s'], 'text': r['text_plain']})
json.dump(tl, open(f'{OUT}/timeline.json', 'w'), indent=1, ensure_ascii=False)
with open(f'{RC4}/transcript.txt', 'w') as fh:
    for i, r in enumerate(rows):
        if i and r['scene'] != rows[i - 1]['scene']: fh.write('\n')
        fh.write(r['text_plain'] + '\n')
# thống kê
seqs = {}
for r in rows:
    s = seqs.setdefault(r['sequence'], {'n': 0, 'words': 0, 'talk': 0.0, 'start': r['start_s'], 'end': 0, 'new': 0, 'reused': 0})
    s['n'] += 1; s['words'] += len(r['tts_text'].split()); s['talk'] += r['duration_s']; s['end'] = r['end_s']; s['new' if r['source'] == 'new' else 'reused'] += 1
for k, s in seqs.items(): s['wpm_talk'] = round(60 * s['words'] / s['talk'], 1); s['wpm_all'] = round(60 * s['words'] / (s['end'] - s['start']), 1)
W = sum(s['words'] for s in seqs.values()); T = sum(s['talk'] for s in seqs.values())
json.dump({'total_s': total, 'lufs': lufs, 'peak': pk, 'before': before, 'seqs': seqs, 'words': W, 'wpm_talk': 60 * W / T, 'wpm_all': 60 * W / (rows[-1]['end_s'] - rows[0]['start_s'])},
          open(f'{EP}/work/v31-voice/stats.json', 'w'), indent=1)
print(json.dumps({'total': total, 'lufs': lufs, 'peak': pk, 'before': before, 'W': W}, indent=0)); print(json.dumps(seqs, indent=0))
