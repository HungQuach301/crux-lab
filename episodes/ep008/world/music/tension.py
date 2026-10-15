"""Tập 8 · F-3 — bản đồ căng của cả tập (0–1) cho nhạc bằng mã (D-010 §5; mẫu episodes/ep006/world/music/tension.py).
  python3 episodes/ep008/world/music/tension.py --timeline episodes/ep008/out/factory/timeline.json   → in bản đồ + mốc

Mốc giờ: đầu cảnh = timeline của nhà máy (out/factory/timeline.json, `--timeline`, bắt buộc: c4/build_inputs.py --timeline). Giờ câu/từ =
alignment của take đã có (0 ký tự ElevenLabs).
Hình dạng (script.md: đỉnh hồi 1 S06.3 the stack đủ cao, đỉnh hồi 2 S15.2 {peak} "fewer than 1 in 5", đỉnh hồi 3 S30.3 "Same plan, a different week"):
  cold open 0,40–0,56 (giá đường lui, câu hỏi + lời hứa) → Hồi 1 thấp (hai khoản trả) dâng tới the stack (S06.3) → chùng qua lãi hai khoản, MR1
  (nhạc 0) → Hồi 2 phương pháp + khoảng chênh, dâng qua hàng chồng tới ĐỈNH S15.2 → đối trọng → thập kỷ (S18 lật) → Tessa tự thử (N1) → MR2 →
  Hồi 3 the bar, lịch sử lãi, Leo → ĐỈNH S30.3 → ngưỡng → giới hạn thấp → kết: khúc đóng A (F-12) chạm sau chữ cuối S33.3.
Ba số neo (episode.md §5b, ≤ 3/tập): S06.1 "$2,948 a month" (trả 30 năm trong 15), S18.1 "$20,374" (lãi thấp hơn, đường lui đắt hơn),
S28.1 "about 1 week in 5" (the bar của Tessa) — mỗi số mở đầu cảnh, nhạc về 0 trong 0,75 s TRƯỚC câu (nằm trong đuôi của cảnh trước, không
thêm giây vào tập); điểm nhấn felt ở từ khoá."""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
WORLD = os.path.dirname(HERE)
EP = os.path.dirname(WORLD)
sys.path.insert(0, WORLD)
sys.dont_write_bytecode = True

# (mốc, mức căng). 'S10' = từ đầu cảnh, 'S10.2' = đầu câu, 'S15.2:fewer' = đầu từ, '…+2.4' = mốc + 2,4 s, 'ident' = giữa ident, 'end' = hết tập.
MAP = [
    # cold open: ba sự thật lật kỳ vọng, câu hỏi, nghịch lý
    ('S01', 0.38), ('S01.2', 0.46), ('S02', 0.52), ('S02.2', 0.58), ('S02.3', 0.50), ('S03', 0.54), ('S03.2', 0.40), ('S03.4', 0.36),
    ('ident', 0.45),
    # Hồi 1 · hai người song sinh trả gì, tiền mặt nằm yên, thẻ tiền thuê
    ('S04', 0.24), ('S05', 0.30), ('S05.5', 0.34), ('S06', 0.32), ('S07', 0.42), ('S07.3', 0.48), ('S07.4', 0.40),
    # MR1 · Hồi 2 · đi dọc phố
    ('S08', 0.34), ('S08.4', 0.42), ('S09', 0.50), ('S10', 0.56), ('S11', 0.62), ('S12', 0.54), ('S13', 0.60), ('S13.1', 0.70), ('S14', 0.50),
    ('S15', 0.62), ('S16', 0.52), ('S17', 0.66), ('S17.1', 0.82), ('S18', 0.70), ('S19', 0.58), ('S19.3', 0.46), ('S20', 0.44), ('S21', 0.54),
    ('S22', 0.50), ('S22.3', 0.56), ('S22.5', 0.42),
    # MR2 · Hồi 3 · hai người hàng xóm, thẻ xoay, tháng đầu của Nina
    ('S23', 0.44), ('S23.5', 0.54), ('S24', 0.56), ('S25', 0.70), ('S26', 0.76), ('S26.2', 0.62), ('S27', 0.52), ('S28', 0.50), ('S29', 0.48),
    ('S30', 0.56), ('S30.3', 0.46),
    # giới hạn + bảng điểm + câu của Nina + câu hỏi còn mở
    ('S31', 0.32), ('S32', 0.36), ('S32.4', 0.44), ('S33', 0.40), ('end', 0.15),
]
ACTS = [('cold open', 'S01'), ('Hồi 1', 'S04'), ('Hồi 2 · đi dọc phố', 'S08'), ('Hồi 3', 'S23'), ('giới hạn + kết', 'S31')]
ANCHORS = ['S13.1', 'S17.1', 'S25.1']                                   # số neo: nhạc về 0 trong 0,75 s trước câu
ACCENTS = ['S13.1:three', 'S17.1:Ten', 'S25.1:At']                         # felt nhấn đúng từ


def scene_starts(timeline):
    if not (timeline and os.path.exists(timeline)):
        raise SystemExit('tension: cần --timeline episodes/ep008/out/factory/timeline.json (c4/build_inputs.py --timeline)')
    tl = json.load(open(timeline))
    st = {s['id']: float(s['start']) for s in tl['scenes']}
    return st, float(tl['total']), {s['id']: float(s['start'] + s['dur']) for s in tl['scenes']}


def anchors(timeline=None):
    """Giờ (s, trong tập) của mọi câu/từ + mốc ident, MR1/MR2, neo, khúc đóng, end."""
    import wlib
    st, total, ends = scene_starts(timeline)
    words, sent, first, last = [], {}, {}, {}
    for sc in sorted(st):
        W = wlib.scene_words(sc)
        for w in W['words']:
            if w['w'].startswith('['): continue
            t0, t1 = st[sc] + float(w['s']), st[sc] + float(w['e'])
            words.append({'w': w['w'], 'sid': w['sid'], 's': t0, 'e': t1})
            sent.setdefault(w['sid'], t0)
            first.setdefault(sc, t0)
            last[sc] = t1
    import yaml
    mr = [float(m['t']) for m in (yaml.safe_load(open(os.path.join(EP, 'episode.yaml'))) or {}).get('midrolls') or []]
    if len(mr) != 2:
        raise SystemExit(f'tension: lab cần 2 mid-roll trong episode.yaml, có {len(mr)}')
    return {'scene_start': st, 'first': first, 'last': last, 'sent': sent, 'words': words, 'mr': mr,
            'ident': [ends['S03'] - 3.0, ends['S03']], 'total': total, 'last_word': max(w['e'] for w in words)}


def resolve(a, A):
    if '+' in a:
        a, d = a.split('+')
        return resolve(a, A) + float(d)
    if a == 'end': return A['total']
    if a == 'ident': return 0.5 * (A['ident'][0] + A['ident'][1])
    if ':' in a:
        sid, w = a.split(':')
        c = [x for x in A['words'] if x['sid'] == sid and x['w'].strip('.,;:?!"\'').lower().startswith(w.lower())]
        if not c: raise SystemExit(f'tension: không thấy từ "{w}" trong {sid}')
        return c[0]['s']
    if '.' in a: return A['sent'][a]
    return A['first'][a]


def keyframes(A):
    kf = [(resolve(a, A), v, a) for a, v in MAP]
    ts = [k[0] for k in kf]
    if any(b < a for a, b in zip(ts, ts[1:])):
        raise SystemExit('tension: mốc không theo thứ tự thời gian')
    return kf


def curve(kf, t):
    return np.interp(t, [k[0] for k in kf], [k[1] for k in kf])


def build(timeline=None):
    A = anchors(timeline)
    kf = keyframes(A)
    return {'total': A['total'], 'mr': A['mr'], 'ident': A['ident'], 'last_word': A['last_word'],
            'anchors': [(a, A['sent'][a]) for a in ANCHORS], 'accents': [(a, resolve(a, A)) for a in ACCENTS],
            'keyframes': [{'t': round(t, 3), 'v': v, 'at': a} for t, v, a in kf],
            'scenes': {sc: round(A['first'][sc], 3) for sc in sorted(A['first'])},
            'acts': [(n, round(A['first'][s], 3)) for n, s in ACTS]}


def main():
    tl = sys.argv[sys.argv.index('--timeline') + 1] if '--timeline' in sys.argv else None
    M = build(tl)
    for k in M['keyframes']:
        print(f"{k['t']:8.2f}  {k['v']:.2f}  {k['at']}")
    print('MR', M['mr'], 'ident', M['ident'], 'anchors', M['anchors'], 'last word', round(M['last_word'], 2), 'total', M['total'])


if __name__ == '__main__':
    main()
