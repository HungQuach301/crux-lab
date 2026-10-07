"""Crux factory qc (Mốc B): the builder's working rules on what the factory just made. Not a substitute for checks/ (the judge);
a rule the builder thinks checks/ should hold goes to checks-appeal.md.

run(build) → out/factory/qc.json + qc.md. Each item ĐẠT/TRƯỢT; every measured value within ±5 % of its threshold is named (CHARTER §4).
Items: floor · contrast · safe area · label collisions · ILLUSTRATIVE/history tags · axis from 0 · freezedetect d=3 ∩ speech = 0 ·
visual ≥ word · loudness · part size · Short length · format rules · F-2 label overlap (box intersection on the frame log; CẢNH BÁO = warn,
does not fail qc — engine collisions above stay TRƯỢT; 2D logs carry no line geometry or opacity, so line crossings are world-only).
"""
import json
import os
import re
import subprocess

import spec as SPEC
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'world'))
import sfx_labels  # noqa: E402  (F-2: same overlap rule as world/verify_seg.py)

SAFE = {'h': (96, 64, 1920 - 96, 1080 - 56), 'v': (72, 200, 1080 - 72, 1920 - 320)}
FLOOR = {'h': 40, 'v': 56}
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DIM = {'h': (1920, 1080), 'v': (1080, 1920)}


class Q:
    def __init__(self):
        self.items, self.near = [], []

    def item(self, name, ok, value, threshold, note=''):
        self.items.append({'item': name, 'result': 'ĐẠT' if ok else 'TRƯỢT', 'value': value, 'threshold': threshold, 'note': note})

    def close(self, name, value, thr):
        if thr and abs(value - thr) <= 0.05 * abs(thr):
            self.near.append({'item': name, 'value': value, 'threshold': thr})


def frame_rules(q, logs, orient, tag, cws=None):
    W, H = DIM[orient]
    sx0, sy0, sx1, sy1 = SAFE[orient]
    texts = [(L['t'] if 't' in L else L['f'], x) for L in logs for x in L['texts']]
    mpx = min((x['px'] for _, x in texts), default=None)
    q.item(f'{tag} sàn chữ', mpx is None or mpx >= FLOOR[orient] - 0.01, mpx, f"≥ {FLOOR[orient]} px", f"{sum(len(L['raised']) for L in logs)} lần engine nâng cỡ")
    if mpx:
        q.close(f'{tag} sàn chữ', mpx, FLOOR[orient])
    mc = min((x['contrast'] for _, x in texts), default=None)
    q.item(f'{tag} tương phản', mc is None or mc >= 4.5, mc, '≥ 4.5:1', f"{sum(len(L['recoloured']) for L in logs)} lần đổi màu")
    if mc:
        q.close(f'{tag} tương phản', mc, 4.5)
    worst, bad = 0.0, []
    for t, x in texts:
        z = x.get('z', 1)
        b = [W / 2 + (x['box'][0] - W / 2) * z, H / 2 + (x['box'][1] - H / 2) * z, W / 2 + (x['box'][2] - W / 2) * z, H / 2 + (x['box'][3] - H / 2) * z]
        out = max(sx0 - b[0], sy0 - b[1], b[2] - sx1, b[3] - sy1)
        if out > 1:
            bad.append({'t': t, 's': x['s'], 'out_px': round(out, 1)})
        worst = max(worst, out)
    q.item(f'{tag} vùng an toàn', not bad, len(bad), '0 hộp chữ ra ngoài (> 1 px)', json.dumps(bad[:3], ensure_ascii=False) if bad else '')
    col = [c for L in logs for c in L['collisions']]
    q.item(f'{tag} va chạm nhãn', not col, len(col), '0', json.dumps(col[:3], ensure_ascii=False) if col else '')
    lc = label_overlap_2d(logs, W, H)
    q.items.append({'item': f'{tag} nhãn giao nhau (F-2)', 'result': 'ĐẠT' if not lc['overlaps']['count'] else 'CẢNH BÁO', 'value': lc['overlaps']['count'],
                    'threshold': f'0 cặp hộp chữ giao nhau > {sfx_labels.LABEL_TOL_PX:g} px (cảnh báo)',
                    'note': '; '.join(s['what'] + f" {s['t0']}–{s['t1']} s" for s in lc['overlaps']['spans'][:3])})
    miss = []
    for L in logs:
        need = set()
        if L['hist']:
            need.add('HISTORY')
        if L['illus']:
            need.add('ILLUSTRATIVE')
        if orient == 'v' and (L['claims'] or L['hist']):
            need |= {'HISTORY', 'ILLUSTRATIVE'}
        if need - set(L['tags']):
            miss.append(L['t'] if 't' in L else L['f'])
    q.item(f'{tag} nhãn ILLUSTRATIVE / history', not miss, len(miss), '0 khung thiếu nhãn', f'{len(logs)} khung log (mỗi 6 khung)')
    for c in cws or []:  # each declared counterweight must actually be on screen ≥ 1 s (log every 6 frames)
        n = sum(('CW:' + c['id']) in L['tags'] for L in logs) * 6
        q.item(f"{tag} đối trọng \"{c['text']}\"", n >= 30, n, '≥ 30 khung (1 s)')


def label_overlap_2d(logs, W, H):
    """F-2 on the 2D engine log: boxes after camera zoom (about the centre), every text pair in the same logged frame."""
    fr = []
    for L in logs:
        T = []
        for x in L['texts']:
            z = x.get('z', 1)
            T.append({'text': x['s'], 'box': [W / 2 + (x['box'][0] - W / 2) * z, H / 2 + (x['box'][1] - H / 2) * z,
                                              W / 2 + (x['box'][2] - W / 2) * z, H / 2 + (x['box'][3] - H / 2) * z]})
        fr.append({'t': L['t'] if 't' in L else L['f'], 'texts': T})
    return sfx_labels.label_check(fr)


def speech_spans(words, gap=0.3):
    spans = []
    for w in words:
        if spans and w['s'] - spans[-1][1] <= gap:
            spans[-1][1] = max(spans[-1][1], w['e'])
        else:
            spans.append([w['s'], w['e']])
    return spans


def freezes(video):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-i', video, '-vf', 'freezedetect=n=-60dB:d=3', '-map', '0:v', '-f', 'null', '-'],
                       capture_output=True, text=True)
    st = [float(x) for x in re.findall(r'freeze_start: ([\d.]+)', r.stderr)]
    en = [float(x) for x in re.findall(r'freeze_end: ([\d.]+)', r.stderr)]
    return [[a, en[i] if i < len(en) else 1e9] for i, a in enumerate(st)]


def loud(path):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', path, '-filter_complex', 'ebur128=peak=true', '-f', 'null', '-'],
                       capture_output=True, text=True)
    tail = r.stderr[r.stderr.rindex('Summary:'):]
    return float(re.search(r'I:\s+(-?[\d.]+) LUFS', tail)[1]), float(re.search(r'Peak:\s+(-?[\d.]+) dBFS', tail)[1])


def run(B):
    q = Q()
    tl = B.tl
    logs = json.load(open(os.path.join(B.work, 'frame-log.json')))
    frame_rules(q, logs, 'h', 'master', B.counterweights)
    # axis from 0: bars/line draw length from 0 by construction; a min > 0 on them is a breach (swarm/timeline are positions, exempt)
    bad = [s['id'] for s in tl['shots'] if s['template'] in ('bars', 'line') and s['p'].get('min', 0) not in (0, None)]
    q.item('trục từ 0', not bad, len(bad), '0 shot bars/line có min > 0', 'swarm: vị trí chấm, không phải độ dài')
    sp = speech_spans(tl['words'])
    fz = freezes(B.video)
    hit = [[max(a, c), min(b, d)] for a, b in fz for c, d in sp if min(b, d) - max(a, c) > 0]
    q.item('freezedetect d=3 ∩ lời', not hit, round(sum(b - a for a, b in hit), 2), '0 s', f'{len(fz)} đoạn đứng yên ≥ 3 s cả phim: {fz[:3]}')
    early = [a for a in tl['anchors'] if a['visual_t'] < a['word_t'] - 1e-3]
    q.item('mốc hình ≥ mốc từ', not early, len(early), '0', f"{len(tl['anchors'])} mốc")
    I, tp = loud(B.video)
    A = B.S.get('audio') or {}
    q.item('loudness', abs(I - A.get('lufs', -14)) <= 1.0 and tp <= A.get('true_peak', -1.0), f'{I} LUFS / {tp} dBTP',
           f"{A.get('lufs', -14)} ± 1 LUFS, ≤ {A.get('true_peak', -1.0)} dBTP")
    q.close('loudness TP', tp, A.get('true_peak', -1.0))
    big = [p for p in B.parts if p['mb'] > 90]
    q.item('kích thước phần', not big, max(p['mb'] for p in B.parts), '≤ 90 MB mỗi phần', f'{len(B.parts)} phần 720p')
    for S in B.shorts:
        q.item(f"{S['id']} thời lượng", S['duration'] <= 60, S['duration'], '≤ 60 s')
        q.close(f"{S['id']} thời lượng", S['duration'], 60)
        frame_rules(q, json.load(open(os.path.join(B.work, f"{S['id']}-frame-log.json"))), 'v', S['id'], B.counterweights)
        Is, tps = loud(os.path.join(ROOT, S['file']))
        q.item(f"{S['id']} loudness", tps <= -1.0 and abs(Is + 14) <= 2.0, f'{Is} LUFS / {tps} dBTP', '−14 ± 2 LUFS, ≤ −1 dBTP')
    P = SPEC.check(B.S, B.root, duration=B.total)
    fp = [p for p in P if p['level'] in ('BLOCK', 'ASK')]
    q.item('luật format', not fp, B.S.get('format'), f"scope {B.S.get('scope', 'full')}",
           'đoạn trích: bỏ qua thời lượng/mid-roll' if B.S.get('scope') == 'excerpt' else '; '.join(p['msg'] for p in P))
    res = {'items': q.items, 'near': q.near, 'pass': all(i['result'] != 'TRƯỢT' for i in q.items)}
    json.dump(res, open(os.path.join(B.out, 'qc.json'), 'w'), indent=1, ensure_ascii=False)
    with open(os.path.join(B.out, 'qc.md'), 'w') as f:
        f.write(f"# qc nhà máy — {B.S['episode']} ({B.S.get('scope', 'full')})\n\n| Mục | Kết quả | Đo | Ngưỡng | Ghi chú |\n|---|---|---|---|---|\n")
        for i in q.items:
            f.write(f"| {i['item']} | {i['result']} | {i['value']} | {i['threshold']} | {i['note'].replace('|', '/')} |\n")
        f.write('\n**Sát ngưỡng ±5 %:** ' + (', '.join(f"{n['item']} ({n['value']} vs {n['threshold']})" for n in q.near) or 'không có') + '\n')
    return {'pass': res['pass'], 'failed': [i['item'] for i in q.items if i['result'] == 'TRƯỢT'],
            'warned': [i['item'] for i in q.items if i['result'] == 'CẢNH BÁO'], 'near': [n['item'] for n in q.near]}
