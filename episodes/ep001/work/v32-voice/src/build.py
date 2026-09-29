"""Ghép lời v3.2 theo cách bản Y (work/voice-test/src/build.py build_scene): mỗi cảnh cắt về vùng có tiếng (-50 dBFS, +40/+120 ms, fade 5 ms),
0,5 s đầu, 1,4 s giữa hai cảnh, 1,0 s cuối; không cắt trong cảnh. Mốc từng câu: ranh câu = khung năng lượng thấp nhất giữa ký tự cuối câu trước
và ký tự đầu câu sau (alignment with-timestamps), rồi vùng có tiếng trong đoạn đó. Chỉ gain: -19,5 LUFS tích hợp, đỉnh mẫu <= -1 dBFS.
AAC 192 kbps mono 48 kHz (PyAV). Ra: out/voice-v32/timeline.json, sentences.json, review-c4/narration-v32.m4a, transcript-v32.txt, build.json."""
import json, os, sys
import numpy as np, pyloudnorm as pyln
ROOT = '/home/user/crux-lab'; EP = f'{ROOT}/episodes/ep001'; W = f'{EP}/work/v32-voice'; TAKES = f'{W}/takes'; OUT = f'{EP}/out/voice-v32'
sys.path.insert(0, f'{EP}/work/voice-test/src')
import prosody as P
from gen import rows_v32
SR = 48000; LEAD, TAIL, GAP = 0.5, 1.0, 1.4


def trim(x):
    a, b = P.span(x, SR, -50.0, 0.01); s, e = max(0, int((a - 0.04) * SR)), min(len(x), int((b + 0.12) * SR)); c = x[s:e].copy()
    f = int(0.005 * SR); r = np.linspace(0, 1, f); c[:f] *= r; c[-f:] *= r[::-1]; return c, s / SR


def enc(y, path):
    import av
    o = av.open(path, 'w', format='mp4'); st = o.add_stream('aac', rate=SR); st.bit_rate = 192000; st.layout = 'mono'
    a32 = y.astype(np.float32).reshape(1, -1)
    for i in range(0, a32.shape[1], 1024):
        fr = av.AudioFrame.from_ndarray(np.ascontiguousarray(a32[:, i:i + 1024]), format='flt', layout='mono'); fr.sample_rate = SR
        for p in st.encode(fr): o.mux(p)
    for p in st.encode(None): o.mux(p)
    o.close()


G = json.load(open(f'{W}/gen-result.json')); rows, tags = rows_v32(); R = {r['n']: r for r in rows}
parts = [np.zeros(int(LEAD * SR))]; t = LEAD; sents = []; scenes = []
for i in range(1, 21):
    sc = G[f'S{i:02d}']
    if i > 1: parts.append(np.zeros(int(GAP * SR))); t += GAP
    raw = P.decode(f'{TAKES}/{sc["use"]}', SR); c, off0 = trim(raw)
    m = json.load(open(f'{TAKES}/{sc["use"][:-4]}.json')); al = m['alignment']; txt = ''.join(al['characters']); assert txt == m['text'] == sc['text_sent']
    st, en = al['character_start_times_seconds'], al['character_end_times_seconds']
    idx = []; cur = 0
    for s in sc['sentences']:
        j = txt.find(s, cur); assert j >= 0, s; idx.append((j, j + len(s) - 1)); cur = j + len(s)
    db = P.frames_db(raw, SR, 0.01); cuts = [0.0]
    for (a0, a1), (b0, b1) in zip(idx[:-1], idx[1:]):
        lo, hi = en[a1], st[b0]; fl, fh = int(lo / 0.01), max(int(lo / 0.01) + 1, int(hi / 0.01))
        cuts.append((fl + int(np.argmin(db[fl:fh]))) * 0.01 + 0.005 if fh > fl else (lo + hi) / 2)
    cuts.append(len(raw) / SR)
    for k, n in enumerate(sc['n']):
        seg = raw[int(cuts[k] * SR):int(cuts[k + 1] * SR)]; a, b = P.span(seg, SR, -50.0, 0.01)
        sents.append({'n': n, 'scene': sc['scene'], 'sequence': R[n]['sequence'], 'pause_kind': R[n]['pause_kind'], 'text': R[n]['text_plain'], 'tts_text': R[n]['tts_text'],
                      'tag': tags.get(n), 'start': round(t + cuts[k] - off0 + a, 3), 'end': round(t + cuts[k] - off0 + b, 3),
                      'align_start_in_take': round(st[idx[k][0]], 3), 'align_end_in_take': round(en[idx[k][1]], 3)})
    scenes.append({'scene': sc['scene'], 'take': sc['use'], 'start_s': round(t, 3), 'dur_s': round(len(c) / SR, 3), 'raw_dur_s': round(len(raw) / SR, 3)})
    parts.append(c); t += len(c) / SR
parts.append(np.zeros(int(TAIL * SR))); y = np.concatenate(parts)
assert [s['n'] for s in sents] == list(range(1, 106))
meter = pyln.Meter(SR); L = meter.integrated_loudness(y); pk = 20 * np.log10(np.abs(y).max())
target = -19.5; assert pk - L + target <= -1.0, ('đỉnh sẽ > -1 dBFS ở -19,5 LUFS', pk - L + target)
y = y * 10 ** ((target - L) / 20)
os.makedirs(OUT, exist_ok=True); nar = f'{EP}/review-c4/narration-v32.m4a'; enc(y, nar)
z = P.decode(nar, SR); encd = {'duration_s': round(len(z) / SR, 3), 'lufs': round(meter.integrated_loudness(z), 2), 'peak_dbfs': round(20 * np.log10(np.abs(z).max()), 2)}
loud = {'before_gain_lufs': round(L, 2), 'gain_db': round(target - L, 2), 'integrated_lufs': round(meter.integrated_loudness(y), 2),
        'sample_peak_dbfs': round(20 * np.log10(np.abs(y).max()), 2), 'processing': 'gain only', 'encoded_m4a': encd}
ev = []
for k, s in enumerate(sents):
    if k:
        p = sents[k - 1]; kind = 'scene' if p['scene'] != s['scene'] else s['pause_kind']
        ev.append({'type': 'pause', 'kind': kind, 'start_s': p['end'], 'end_s': s['start'], 'dur_s': round(s['start'] - p['end'], 3), 'before_n': s['n']})
    ev.append({'type': 'sentence', 'n': s['n'], 'sequence': s['sequence'], 'scene': s['scene'], 'start_s': s['start'], 'end_s': s['end'], 'text': s['text']})
total = round(len(y) / SR, 3)
tl = {'total_s': total, 'sample_rate': SR, 'lead_s': LEAD, 'tail_s': TAIL, 'pauses_s': {'scene': GAP, 'in_scene': 'natural (one TTS call per scene; not edited)'},
      'note': 'Voice v3.2 (script-v3.2.md, 8 emotion tags): one eleven_v3 call per scene (recipe of sample Y). Sentence start/end = speech span (-50 dBFS) '
              'inside the sentence segment; segment boundaries = lowest-energy 10 ms frame between the aligned last char of a sentence and first char of the next '
              '(with-timestamps alignment). In-scene pauses are the model\'s own; 1.4 s silence between scene clips; no cut inside any scene.',
      'trim': 'scene speech span (-50 dBFS, 10 ms windows) +40 ms before / +120 ms after, 5 ms fades', 'loudness': loud,
      'file': 'episodes/ep001/review-c4/narration-v32.m4a (AAC 192 kbps mono 48 kHz)', 'scenes': scenes, 'events': ev}
json.dump(tl, open(f'{OUT}/timeline.json', 'w'), indent=1, ensure_ascii=False)
json.dump({'source': 'episodes/ep001/story/script-v3.2.md', 'model': 'eleven_v3', 'voice': 'Eric cjVigY5qzO86Huf0OWal',
           'endpoint': 'POST /v1/text-to-speech/{voice}/with-timestamps?output_format=mp3_44100_128, body {text, model_id, seed}; no speed, no voice_settings',
           'sentences': sents}, open(f'{OUT}/sentences.json', 'w'), indent=1, ensure_ascii=False)
open(f'{EP}/review-c4/transcript-v32.txt', 'w').write('\n'.join(s['text'] for s in sents) + '\n')
ins = np.array([e['dur_s'] for e in ev if e['type'] == 'pause' and e['kind'] != 'scene'])
bt = np.array([e['dur_s'] for e in ev if e['type'] == 'pause' and e['kind'] == 'beat']); sm = np.array([e['dur_s'] for e in ev if e['type'] == 'pause' and e['kind'] == 'same'])
sc_g = np.array([e['dur_s'] for e in ev if e['type'] == 'pause' and e['kind'] == 'scene'])
stats = {'total_s': total, 'loudness': loud, 'gaps': {k: {'n': len(a), 'mean': round(float(a.mean()), 3), 'sd': round(float(a.std()), 3), 'min': round(float(a.min()), 3),
                                                        'max': round(float(a.max()), 3)} for k, a in (('same', sm), ('beat', bt), ('scene', sc_g), ('in_scene_all', ins))},
         'scenes': scenes}
json.dump(stats, open(f'{W}/build.json', 'w'), indent=1)
print(json.dumps({k: v for k, v in stats.items() if k != 'scenes'}, indent=1))
