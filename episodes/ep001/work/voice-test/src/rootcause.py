"""VIỆC 1: đo prosody voice-B (C3) vs v3.1 (cùng đoạn, cả tập), take tái dùng C2 vs take mới. Ghi rootcause.json."""
import json, os, sys
import numpy as np
from scipy.stats import mannwhitneyu
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from prosody import *
ROOT = '/home/user/crux-lab'; EP = f'{ROOT}/episodes/ep001'; TK = f'{EP}/work/voice-test'


def clip_take(path, rule):
    x = decode(path)
    if rule == 'c3':  # C3 build: -45 dBFS cửa sổ 20 ms, ±30 ms
        a, b = span(x, SR, -45.0, 0.02); return x[max(0, int((a - 0.03) * SR)):int((b + 0.03) * SR)]
    a, b = span(x, SR, -50.0, 0.01); return x[max(0, int((a - 0.04) * SR)):int((b + 0.12) * SR)]


def nwords(t): return len(t.split())


res = {}
# A. voice-B: take C3 G1
kB = json.load(open(f'{EP}/review-c3/voice/key.json'))['files']['voice-B.m4a']
textsB = [json.load(open(f'{ROOT}/{p[:-4]}.json'))['text'] for p in kB['takes']]
sB = [sentence(clip_take(f'{ROOT}/{p}', 'c3'), nwords(t)) for p, t in zip(kB['takes'], textsB)]
res['B_C3'] = {'sentences': [strip(s) for s in sB], 'passage': passage(sB), 'pauses_file': pauses(decode(f'{EP}/review-c3/voice/voice-B.m4a'))}
# B. v3.1
S = json.load(open(f'{EP}/out/voice-v31/sentences.json'))['sentences']
tl = json.load(open(f'{EP}/out/voice-v31/timeline.json'))
narr = decode(f'{EP}/review-c4/narration.m4a')
sV = []
for r in S:
    m = sentence(clip_take(f'{ROOT}/{r["take_file"]}', 'v31'), nwords(r['tts_text'])); m.update(n=r['n'], scene=r['scene'], source=r['source'], seed=r['seed']); sV.append(m)
same = sV[:7]  # cùng đoạn với voice-B (S01 + S02 tới hết câu hỏi 1)
end7 = [e for e in tl['events'] if e['type'] == 'sentence' and e['n'] == 7][0]['end_s']
res['V31_same7'] = {'sentences': [strip(s) for s in same], 'passage': passage(same), 'pauses_file': pauses(narr[:int((end7 + 0.3) * SR)])}
res['V31_all'] = {'passage': passage(sV), 'pauses_file': strip(pauses(narr))}
res['V31_all']['pauses_file'].pop('all_s', None)
# promise-S02.m4a (bản chủ dự án nghe)
res['promise_S02_file'] = {'pauses_file': pauses(decode(f'{EP}/review-c3/promise-S02.m4a')), 'dur_s': round(len(decode(f'{EP}/review-c3/promise-S02.m4a')) / SR, 2)}
# C. cùng chữ, khác seed: câu 1–5 (C3 seed 11 vs C2 seed 1)
pair = []
for i in range(5):
    assert textsB[i] == S[i]['tts_text']
    pair.append({'n': i + 1, 'text': S[i]['tts_text'][:50], 'C3_seed11': {k: sB[i].get(k) for k in ('dur_s', 'wpm', 'st_range_p5_p95', 'st_sd', 'energy_sd_db', 'final', 'final_delta_st')},
                 'C2_seed1': {k: sV[i].get(k) for k in ('dur_s', 'wpm', 'st_range_p5_p95', 'st_sd', 'energy_sd_db', 'final', 'final_delta_st')}})
res['same_text_seed11_vs_seed1'] = pair
# D. tái dùng C2 vs mới (cả tập)
def grp(src):
    g = [s for s in sV if s['source'] == src and 'st_sd' in s]
    return g
new, old = grp('new'), grp('reused_c2')
cmp = {}
for k in ('st_range_p5_p95', 'st_sd', 'energy_sd_db', 'wpm', 'final_delta_st', 'slope_st_per_s', 'st_mean'):
    a = [s[k] for s in new]; b = [s[k] for s in old]
    cmp[k] = {'new_median': round(float(np.median(a)), 2), 'reused_median': round(float(np.median(b)), 2), 'mannwhitney_p': round(float(mannwhitneyu(a, b).pvalue), 3)}
cmp['n_new'] = len(new); cmp['n_reused'] = len(old)
cmp['finals_new'] = passage(new)['finals']; cmp['finals_reused'] = passage(old)['finals']
res['reused_vs_new_v31'] = cmp
# E. các câu v3.1: chỉ số theo câu (không mảng)
res['V31_sentences'] = [strip(s) for s in sV]
json.dump(res, open(f'{TK}/rootcause.json', 'w'), indent=1, ensure_ascii=False, default=float)
for k in ('B_C3', 'V31_same7', 'V31_all'):
    print(k, json.dumps(res[k]['passage'], ensure_ascii=False)); p = res[k]['pauses_file']; print('  pauses', {x: p[x] for x in p if x != 'all_s'}, p.get('all_s'))
print('promise', res['promise_S02_file'])
for p in pair: print(p)
print(json.dumps(cmp, ensure_ascii=False, indent=0))
