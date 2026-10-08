"""Tốc độ đọc thật của Eric và tỉ lệ thời lượng/từ, Tập 2–5 (REPORT §2c). Chạy: python3 tongket-t5/measure_pace.py"""
import json, os, re, statistics as st

def words(s):
    return len(re.sub(r'\[[^\]]*\]', '', s or '').split())

for ep in ['ep002', 'ep003', 'ep004', 'ep005']:
    S = json.load(open(f'episodes/{ep}/out/script.json'))['sentences']
    spoken = sum(words(x['spoken']) for x in S)
    speech = sum(x['end'] - x['start'] for x in S)
    tl = f'episodes/{ep}/out/factory/timeline.json'
    if not os.path.exists(tl):
        tl = f'episodes/{ep}/out/timeline.json'
    total = json.load(open(tl))['total']
    per = {}
    for x in S:
        a = per.setdefault(x['scene'], [0, 0.0]); a[0] += words(x['spoken']); a[1] += x['end'] - x['start']
    r = [w / d for w, d in per.values() if d > 0]
    print(f'{ep}: từ nói {spoken} · giây lời {speech:.1f} · tổng {total:.1f} · '
          f'đọc {spoken/speech:.2f} từ/s · thời lượng {spoken/total:.2f} từ/s · ngoài lời {total/speech-1:.0%} · '
          f'theo cảnh {min(r):.2f}–{max(r):.2f} (trung vị {st.median(r):.2f})')
