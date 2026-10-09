"""Tập 6 · F-3 — bản đồ căng của cả tập (0–1) cho nhạc bằng mã (D-010 §5; mẫu episodes/ep005/world/music/tension.py).
  python3 episodes/ep006/world/music/tension.py [--timeline episodes/ep006/out/factory/timeline.json]   → in bản đồ + mốc

Mốc giờ: đầu cảnh = timeline của nhà máy (out/factory/timeline.json, `--timeline`), không thì wlib.episode_offsets() (take + đuôi 1,0 s; ident 3 s
sau S03). Giờ câu/từ = alignment của take đã có (0 ký tự ElevenLabs).
Hình dạng (script.md: đỉnh hồi 1 S10.2, đỉnh hồi 2 S14.1 "17 of the 715", đỉnh hồi 3 S25 Carl 43,1 %):
  cold open 0,40–0,56 (câu hỏi + lời hứa) → Hồi 1 thấp (định nghĩa, hai séc) dâng dần qua năm theo năm → ĐỈNH S10.2 (rơi dưới vạch) → chùng,
  MR1 (nhạc 0) → Hồi 2 phát lại DÂNG tới S14.1 (0,82) → giảm qua điển hình / độ vững → Hồi 3 dâng qua Carl tới S25 (0,85) → Edna, ba người, thang
  tăng → giới hạn thấp → kết: khúc đóng A (F-12) chạm sau chữ cuối S32.3.
Ba số neo (episode.md §5b, ≤ 3/tập): S11.1 "ninety-four point five", S14.1 "seventeen", S25.1 "forty-three point one" — mỗi số mở đầu cảnh, nhạc về 0
trong 0,8 s TRƯỚC câu (nằm trong đuôi lời của cảnh trước, không thêm giây vào tập); điểm nhấn felt đúng từ số."""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
WORLD = os.path.dirname(HERE)
EP = os.path.dirname(WORLD)
sys.path.insert(0, WORLD)
sys.dont_write_bytecode = True

# (mốc, mức căng). 'S10' = từ đầu cảnh, 'S10.2' = đầu câu, 'S14.1:seventeen' = đầu từ, '…+2.4' = mốc + 2,4 s, 'ident' = giữa ident, 'end' = hết tập.
MAP = [
    ('S01', 0.40), ('S01.2', 0.46), ('S02', 0.50), ('S02.2', 0.56), ('S03', 0.42), ('S03.3', 0.36),
    ('ident', 0.45),
    # Hồi 1 · hai séc, sức mua, hai mươi năm của Ruth
    ('S04', 0.22), ('S05', 0.26), ('S06', 0.32), ('S06.2', 0.38), ('S07', 0.40), ('S07.2', 0.46), ('S08', 0.40), ('S09', 0.46),
    ('S09.2', 0.52), ('S10', 0.58), ('S10.2', 0.72), ('S11', 0.56), ('S12', 0.48), ('S12.4', 0.54),
    # MR1 · Hồi 2 · phát lại 715 quãng
    ('S13', 0.42), ('S13.3', 0.55), ('S13.4', 0.62), ('S14', 0.82), ('S14.2', 0.76), ('S15', 0.70), ('S16', 0.55), ('S17', 0.52),
    ('S17.3', 0.44), ('S19', 0.40), ('S21', 0.48), ('S22', 0.36), ('S23', 0.44),
    # Hồi 3 · cùng mức tăng, ba tháng bắt đầu
    ('S24', 0.50), ('S24.3', 0.62), ('S24.5', 0.74), ('S25', 0.85), ('S25.3', 0.70), ('S26', 0.58), ('S27', 0.50), ('S27.5', 0.62),
    ('S28', 0.46), ('S29', 0.60), ('S29.2', 0.68), ('S29.3', 0.52), ('S30', 0.48), ('S30.2', 0.58), ('S30.4', 0.66), ('S30.5', 0.42),
    # giới hạn + kết
    ('S31', 0.24), ('S31.4', 0.22), ('S32', 0.30), ('S32.3', 0.42), ('end', 0.15),
]
ACTS = [('cold open', 'S01'), ('Hồi 1', 'S04'), ('Hồi 2 · phát lại', 'S13'), ('Hồi 3', 'S24'), ('giới hạn + kết', 'S31')]
ANCHORS = ['S11.1', 'S14.1', 'S25.1']                        # số neo: nhạc về 0 trong 0,8 s trước câu
ACCENTS = ['S11.1:ninety-four', 'S14.1:seventeen', 'S25.1:forty-three', 'S30.2:forty-two']   # felt nhấn đúng từ số


def scene_starts(timeline=None):
    import wlib
    if timeline and os.path.exists(timeline):
        tl = json.load(open(timeline))
        st = {s['id']: float(s['start']) for s in tl['scenes']}
        return st, float(tl['total']), {s['id']: float(s['start'] + s['dur']) for s in tl['scenes']}
    off = wlib.episode_offsets()
    end = off.pop('_end')
    return off, end, None


def anchors(timeline=None):
    """Giờ (s, trong tập) của mọi câu/từ + mốc ident, MR1, neo, khúc đóng, end."""
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
    mr1 = None
    try:
        import yaml
        mr = (yaml.safe_load(open(os.path.join(EP, 'episode.yaml'))) or {}).get('midrolls') or []
        if mr: mr1 = float(mr[0]['t'])
    except Exception:
        mr1 = None
    brk = mr1 is not None
    if mr1 is None:
        mr1 = 0.5 * (last['S12'] + first['S13'])
    ident_end = ends['S03'] if ends else first['S04']
    return {'scene_start': st, 'first': first, 'last': last, 'sent': sent, 'words': words, 'mr1': mr1, 'mr1_break': brk,
            'ident': [ident_end - 3.0, ident_end], 'total': total, 'last_word': max(w['e'] for w in words)}


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
    return {'total': A['total'], 'mr1': A['mr1'], 'mr1_break': A['mr1_break'], 'ident': A['ident'], 'last_word': A['last_word'],
            'anchors': [(a, A['sent'][a]) for a in ANCHORS], 'accents': [(a, resolve(a, A)) for a in ACCENTS],
            'keyframes': [{'t': round(t, 3), 'v': v, 'at': a} for t, v, a in kf],
            'scenes': {sc: round(A['first'][sc], 3) for sc in sorted(A['first'])},
            'acts': [(n, round(A['first'][s], 3)) for n, s in ACTS]}


def main():
    tl = sys.argv[sys.argv.index('--timeline') + 1] if '--timeline' in sys.argv else None
    M = build(tl)
    for k in M['keyframes']:
        print(f"{k['t']:8.2f}  {k['v']:.2f}  {k['at']}")
    print('MR1', round(M['mr1'], 2), 'ident', M['ident'], 'anchors', M['anchors'], 'last word', round(M['last_word'], 2), 'total', M['total'])


if __name__ == '__main__':
    main()
