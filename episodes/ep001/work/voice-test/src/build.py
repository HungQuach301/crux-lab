"""Ghép V1/V2/V3, đo prosody, chuẩn hoá độ to (chỉ gain, cùng LUFS, đỉnh ≤ −1 dBFS), xáo X/Y/Z bằng secrets, mã hoá AAC 192 kbps mono 48 kHz (PyAV)."""
import json, os, sys, secrets
import numpy as np, pyloudnorm as pyln, av
from scipy.signal import resample_poly
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import prosody as P
ROOT = '/home/user/crux-lab'; EP = f'{ROOT}/episodes/ep001'; TK = f'{EP}/work/voice-test'; TAKES = f'{TK}/takes'; OUT = f'{EP}/review-c4/voice-test'
SR = 48000; LEAD, TAIL = 0.5, 1.0; GAP = {'same': 0.45, 'beat': 1.0, 'scene': 1.4, 'first': 0.0}
G = json.load(open(f'{TK}/gen-result.json'))


def trim(x):
    a, b = P.span(x, SR, -50.0, 0.01); s, e = max(0, int((a - 0.04) * SR)), min(len(x), int((b + 0.12) * SR)); c = x[s:e].copy()
    f = int(0.005 * SR); r = np.linspace(0, 1, f); c[:f] *= r; c[-f:] *= r[::-1]; return c, s / SR


def spk(c, off):  # vùng có tiếng của một đoạn, theo mốc bản ghép
    a, b = P.span(c, SR, -50.0, 0.01); return off + a, off + b


def build_v1():
    parts = [np.zeros(int(LEAD * SR))]; t = LEAD; sents = []; prev_sc = None
    for i, r in enumerate(G['result']['V1']):
        if i:
            k = 'scene' if r['scene'] != prev_sc else r['pause_kind']; k = 'scene' if k == 'sequence' else k
            parts.append(np.zeros(int(round(GAP[k] * SR)))); t += GAP[k]
        c, _ = trim(P.decode(f'{TAKES}/{r["use"]}', SR)); a, b = spk(c, t); parts.append(c); t += len(c) / SR
        sents.append({'n': r['n'], 'scene': r['scene'], 'text': r['tts_text'], 'start': a, 'end': b}); prev_sc = r['scene']
    parts.append(np.zeros(int(TAIL * SR))); return np.concatenate(parts), sents


def build_scene(v):
    parts = [np.zeros(int(LEAD * SR))]; t = LEAD; sents = []
    for i, sc in enumerate(G['result'][v]):
        if i: parts.append(np.zeros(int(1.4 * SR))); t += 1.4
        raw = P.decode(f'{TAKES}/{sc["use"]}', SR); c, off0 = trim(raw)
        m = json.load(open(f'{TAKES}/{sc["use"][:-4]}.json')); al = m['alignment']; txt = ''.join(al['characters']); assert txt == m['text']
        st, en = al['character_start_times_seconds'], al['character_end_times_seconds']
        idx = []; cur = 0
        for s in sc['sentences']:
            j = txt.find(s, cur); assert j >= 0, s; idx.append((j, j + len(s) - 1)); cur = j + len(s)
        db = P.frames_db(raw, SR, 0.01)
        cuts = [0.0]
        for (a0, a1), (b0, b1) in zip(idx[:-1], idx[1:]):
            lo, hi = en[a1], st[b0]
            fl, fh = int(lo / 0.01), max(int(lo / 0.01) + 1, int(hi / 0.01))
            cuts.append((fl + int(np.argmin(db[fl:fh]))) * 0.01 + 0.005 if fh > fl else (lo + hi) / 2)
        cuts.append(len(raw) / SR)
        for k, s in enumerate(sc['sentences']):
            seg = raw[int(cuts[k] * SR):int(cuts[k + 1] * SR)]; a, b = P.span(seg, SR, -50.0, 0.01)
            sents.append({'n': sc['n'][k], 'scene': sc['scene'], 'text': s, 'start': t + cuts[k] - off0 + a, 'end': t + cuts[k] - off0 + b})
        parts.append(c); t += len(c) / SR
    parts.append(np.zeros(int(TAIL * SR))); return np.concatenate(parts), sents


def measure(y, sents):
    y16 = resample_poly(y, 1, 3); ms = []
    for s in sents:
        m = P.sentence(y16[int(s['start'] * 16000):int(s['end'] * 16000)], len(s['text'].split())); m.update(n=s['n'], scene=s['scene']); ms.append(m)
    gaps = [{'after_n': a['n'], 'kind': 'scene' if a['scene'] != b['scene'] else 'in_scene', 's': round(b['start'] - a['end'], 3)} for a, b in zip(sents[:-1], sents[1:])]
    ins = np.array([g['s'] for g in gaps if g['kind'] == 'in_scene'])
    return {'passage': P.passage(ms), 'sentence_gaps': {'in_scene_mean_s': round(float(ins.mean()), 3), 'in_scene_sd_s': round(float(ins.std()), 3),
                                                       'in_scene_min_max_s': [round(float(ins.min()), 3), round(float(ins.max()), 3)], 'all': gaps},
            'pauses_file_ge120ms': {k: v for k, v in P.pauses(y16).items() if k != 'all_s'}, 'sentences': [P.strip(m) for m in ms]}


audio, info = {}, {}
audio['V1'], s1 = build_v1(); audio['V2'], s2 = build_scene('V2'); audio['V3'], s3 = build_scene('V3')
for v, s in (('V1', s1), ('V2', s2), ('V3', s3)):
    info[v] = measure(audio[v], s); info[v]['sentence_spans_s'] = [[s_['n'], round(s_['start'], 3), round(s_['end'], 3)] for s_ in s]
meter = pyln.Meter(SR)
L = {v: meter.integrated_loudness(y) for v, y in audio.items()}; pk = {v: 20 * np.log10(np.abs(y).max()) for v, y in audio.items()}
target = min(-19.5, min(-1.0 - (pk[v] - L[v]) for v in audio))
for v in audio:
    audio[v] = audio[v] * 10 ** ((target - L[v]) / 20)
    info[v].update(duration_s=round(len(audio[v]) / SR, 2), lufs=round(meter.integrated_loudness(audio[v]), 2), peak_dbfs=round(20 * np.log10(np.abs(audio[v]).max()), 2),
                   gain_db=round(target - L[v], 2))


def enc(y, path):
    o = av.open(path, 'w', format='mp4'); st = o.add_stream('aac', rate=SR); st.bit_rate = 192000; st.layout = 'mono'
    a32 = y.astype(np.float32).reshape(1, -1)
    for i in range(0, a32.shape[1], 1024):
        fr = av.AudioFrame.from_ndarray(np.ascontiguousarray(a32[:, i:i + 1024]), format='flt', layout='mono'); fr.sample_rate = SR
        for p in st.encode(fr): o.mux(p)
    for p in st.encode(None): o.mux(p)
    o.close()


os.makedirs(OUT, exist_ok=True)
order = ['V1', 'V2', 'V3']; secrets.SystemRandom().shuffle(order)
key = dict(zip(['X', 'Y', 'Z'], order))
for lab, v in key.items():
    enc(audio[v], f'{OUT}/sample-{lab}.m4a')
    z = P.decode(f'{OUT}/sample-{lab}.m4a', SR); info[v]['encoded'] = {'file': f'sample-{lab}.m4a', 'duration_s': round(len(z) / SR, 2), 'lufs': round(meter.integrated_loudness(z), 2),
                                                                         'peak_dbfs': round(20 * np.log10(np.abs(z).max()), 2)}
json.dump({'key': key, 'target_lufs': round(target, 2), 'raw': {'lufs': L, 'peak': pk}, 'info': info}, open(f'{TK}/build.json', 'w'), indent=1, ensure_ascii=False, default=float)
for lab, v in key.items():
    p = info[v]['passage']; g = info[v]['sentence_gaps']
    print(lab, info[v]['encoded'], {k: p[k] for k in ('st_sd_all', 'st_range_sentence_mean', 'sd_of_sentence_means_st', 'sd_of_onsets_st', 'energy_sd_db_mean', 'contour_corr_mean', 'finals', 'wpm_talk', 'wpm_cv')},
          'gap', g['in_scene_mean_s'], g['in_scene_sd_s'], g['in_scene_min_max_s'])
