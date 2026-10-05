"""Mốc B · hiệu chuẩn bộ đo hấp dẫn: lời cuối (out/script.json) → orig-<ep>.txt (một câu một dòng, id + mốc thời gian thật)."""
import json, sys, os
R = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(R, '..', '..'))
def mmss(t): return f'{int(t // 60)}:{int(t % 60):02d}'
for ep in ['ep002', 'ep003']:
    S = json.load(open(f'{ROOT}/episodes/{ep}/out/script.json'))['sentences']
    words = sum(len(s['text'].split()) for s in S); dur = S[-1]['end']
    with open(f'{R}/orig-{ep}.txt', 'w') as f:
        for s in S: f.write(f"{s['id']} [{mmss(s['start'])}] {s['text']}\n")
    print(ep, len(S), 'sentences', words, 'words', round(dur), 's', round(words / dur * 60), 'wpm')
