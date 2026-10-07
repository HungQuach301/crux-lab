"""Tập 5 · F-3 — bản đồ căng của cả tập (0–1) cho nhạc bằng mã (D-010 §5: "nhạc bằng mã theo bản đồ căng, biên độ rộng hơn bản thử").
  python3 episodes/ep005/world/music/tension.py [--timeline out/factory/timeline.json] [--png <out.png>]   → in bản đồ + mốc, vẽ PNG nếu cần

Mốc giờ: giờ đầu cảnh = timeline của nhà máy nếu có (out/factory/timeline.json, `--timeline`), không thì `wlib.episode_offsets()`
(take + đuôi 1,0 s; ident 3 s sau S03 — như SPINE-PLAN). Giờ câu/từ = alignment của take đã có (0 ký tự ElevenLabs).

Hình dạng (theo SPINE-PLAN §1 và các hồi của script.md):
  cold open 0,40–0,55 (câu hỏi + lời hứa) → ident 0,50 → Hồi 1 thấp (S04–S06 ≈ 0,22–0,28: định nghĩa, ví dụ) → leo nhẹ ở hai mốc luật
  (S07–S09) → MR1: nhạc về 0 (≥ 1 s lặng) → Hồi 2 = PHẦN PHÁT LẠI S10–S14 DÂNG đều: dựng máy (0,42→0,66) → đáp án điển hình S11 (0,74)
  → chùng ngắn "But that's on paper" S12 (0,55) → đuôi chậm S13 (0,74→0,88) → ĐỈNH S14.1 "October 2005: 112 months" (0,95)
  → Hồi 3 (F trưởng) mở lại thấp 0,42, ba người mua 0,55–0,70 → S18–S19 hạ (0,50→0,22) → S20 dâng lại 0,32→0,62 tới "never"
  → CHỐT ở "removed" (S20.2): cadence V→I đúng phách mạnh, sau đó 0,28→0,15 tới hết.

Chọn "removed" nào: S20.2 ("…and on paper is never the same as removed."). S03.2 ("That's not the same as getting the insurance removed")
mới ĐẶT khác biệt giấy/thật trong cold open — nó mở câu hỏi, không đóng. S20.1 hỏi lại đúng câu mở đầu ("how long does the insurance
last?") và S20.2 trả lời; "removed" là từ cuối của câu trả lời, nơi máy quay về khiên trên mái (SPINE-PLAN S20: mode → wHouse ở "never").
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
WORLD = os.path.dirname(HERE)
EP = os.path.dirname(WORLD)
ROOT = os.path.abspath(os.path.join(EP, '..', '..'))
sys.path.insert(0, WORLD)
sys.dont_write_bytecode = True

# (mốc, mức căng). Mốc: 'S10' = đầu cảnh (từ đầu tiên), 'S10.4' = đầu câu, 'S20.2:removed' = đầu từ, '…+2.4' = mốc + 2,4 s, 'ident' = giữa ident,
# 'end' = hết tập. Nội suy tuyến tính giữa các mốc (rồi làm mượt 1,5 s ở bed.py).
MAP = [
    ('S01', 0.40), ('S01.2', 0.46), ('S02', 0.50), ('S02.2', 0.56), ('S03', 0.46), ('S03.2', 0.40), ('S03.4', 0.48), ('S03.5', 0.40),
    ('ident', 0.50),
    # Hồi 1 · khái niệm (thấp, nghe rõ lời định nghĩa)
    ('S04', 0.22), ('S04.4', 0.24), ('S04.5', 0.30), ('S05', 0.24), ('S06', 0.26), ('S06.3', 0.30),
    ('S07', 0.38), ('S07.2', 0.42), ('S08', 0.42), ('S08.3', 0.48), ('S09', 0.48), ('S09.2', 0.52), ('S09.4', 0.42),
    # MR1 (nhạc 0 do cổng ở bed.py) · Hồi 2 · phát lại: dâng
    ('S10', 0.42), ('S10.3', 0.50), ('S10.4', 0.58), ('S10.5', 0.66),
    ('S11', 0.74), ('S11.2', 0.70), ('S11.4', 0.66),
    ('S12', 0.55), ('S12.3', 0.62), ('S12.4', 0.66),
    ('S13', 0.74), ('S13.2', 0.82), ('S13.3', 0.88),
    ('S14', 0.95), ('S14.2', 0.90), ('S14.3', 0.76), ('S14.4', 0.68),
    # Hồi 3 · ba người mua (F trưởng)
    ('S15', 0.42), ('S15.3', 0.48), ('S16', 0.55), ('S16.2', 0.62), ('S17', 0.62), ('S17.2', 0.70), ('S17.3', 0.66), ('S17.4', 0.52),
    ('S18', 0.50), ('S18.2', 0.44), ('S18.5', 0.38), ('S18.6', 0.34),
    # giới hạn + outro: chốt ở "removed"
    ('S19', 0.22), ('S20', 0.32), ('S20.2', 0.42), ('S20.2:never', 0.55), ('S20.2:removed', 0.62),
    ('S20.2:removed+2.4', 0.28), ('end', 0.15),
]
ACTS = [('cold open', 'S01'), ('Hồi 1', 'S04'), ('Hồi 2 · phát lại', 'S10'), ('Hồi 3', 'S15'), ('outro', 'S19')]
ACCENTS = ['S11.1:twenty-three', 'S14.1:one', 'S16.2:thirteen', 'S20.2:removed']   # lời đọc số bằng chữ ("one hundred twelve")   # felt nhấn đúng từ (số then chốt + chốt)
KEY_CHANGE = 'S15'   # D dorian → F trưởng (G-016 · chọn: dorian rồi F trưởng)
LANDING = 'S20.2:removed'


def scene_starts(timeline=None):
    import wlib
    if timeline and os.path.exists(timeline):
        tl = json.load(open(timeline))
        vs = wlib.voice_scenes()
        st = {s['id']: float(s['start']) for s in tl['scenes'] if s['id'] in vs}   # chỉ cảnh có lời (bỏ thẻ/ident)
        return st, float(tl['total'])
    off = wlib.episode_offsets()
    end = off.pop('_end')
    return off, end


def anchors(timeline=None):
    """Giờ (s, trong tập) của mọi câu/từ + mốc ident, MR1, end."""
    import wlib
    st, total = scene_starts(timeline)
    words, sent, first, last = [], {}, {}, {}
    for sc in sorted(st):
        W = wlib.scene_words(sc)
        for w in W['words']:
            if w['w'].startswith('['): continue   # thẻ cảm xúc eleven_v3, không phải từ nói
            t0, t1 = st[sc] + float(w['s']), st[sc] + float(w['e'])
            words.append({'w': w['w'], 'sid': w['sid'], 's': t0, 'e': t1})
            sent.setdefault(w['sid'], t0)
            first.setdefault(sc, t0)
            last[sc] = t1
    mr1 = None
    yml = os.path.join(EP, 'episode.yaml')
    try:
        import yaml
        mr = (yaml.safe_load(open(yml)) or {}).get('midrolls') or []
        if mr: mr1 = float(mr[0]['t'])
    except Exception:
        mr1 = None
    if mr1 is None:   # script.md: MR1 trong khoảng giữ sau S09.4 → giữa từ cuối S09 và từ đầu S10
        mr1 = 0.5 * (last['S09'] + first['S10'])
    ident = 0.5 * (last['S03'] + first['S04'])
    return {'scene_start': st, 'first': first, 'last': last, 'sent': sent, 'words': words, 'mr1': mr1, 'ident': ident, 'total': total}


def resolve(a, A):
    if '+' in a:
        a, d = a.split('+')
        return resolve(a, A) + float(d)
    if a == 'end': return A['total']
    if a == 'ident': return A['ident']
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
    return {'total': A['total'], 'mr1': A['mr1'], 'ident': A['ident'], 'landing': resolve(LANDING, A),
            'key_change': A['first'][KEY_CHANGE] - 1.0, 'accents': [(a, resolve(a, A)) for a in ACCENTS],
            'keyframes': [{'t': round(t, 3), 'v': v, 'at': a} for t, v, a in kf],
            'scenes': {sc: round(A['first'][sc], 3) for sc in sorted(A['first'])},
            'acts': [(n, round(A['first'][s], 3)) for n, s in ACTS],
            'sections': sections(A)}


def sections(A):
    """Đoạn để đo LUFS nhạc: tên → (t0, t1) giữa các từ (không gồm khoảng MR1)."""
    f, l = A['first'], A['last']
    return {'cold open S01–S03': (f['S01'], l['S03']), 'Hồi 1 calm S04–S06': (f['S04'], l['S06']),
            'Hồi 1 dates S07–S09': (f['S07'], l['S09']), 'replay setup S10–S11': (f['S10'], l['S11']),
            'replay peak S13–S14': (f['S13'], l['S14']), 'Hồi 3 S15–S18': (f['S15'], l['S18']),
            'outro S20 → removed': (f['S20'], resolve(LANDING, A)), 'after removed': (resolve(LANDING, A), A['total'])}


def plot(M, png, music_lufs=None):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    t = np.linspace(0, M['total'], 4000)
    kf = [(k['t'], k['v']) for k in M['keyframes']]
    y = curve(kf, t)
    fig, ax = plt.subplots(figsize=(14, 4.2), dpi=120)
    ax.fill_between(t / 60, 0, y, color='#4C6EF5', alpha=0.18, lw=0)
    ax.plot(t / 60, y, color='#364FC7', lw=2, label='tension (map)')
    for n, s in M['acts']:
        ax.axvline(s / 60, color='#adb5bd', lw=0.8)
        ax.text(s / 60 + 0.03, 1.02, n, fontsize=9, color='#495057', va='bottom')
    ax.axvspan((M['mr1'] - 0.6) / 60, (M['mr1'] + 0.6) / 60, color='#e03131', alpha=0.25)
    ax.text(M['mr1'] / 60, 0.04, ' MR1 (music 0)', color='#c92a2a', fontsize=9)
    ax.axvline(M['landing'] / 60, color='#2b8a3e', lw=1.5, ls='--')
    ax.text(M['landing'] / 60 - 0.05, 0.75, '"removed" (S20.2)\nV→I landing', color='#2b8a3e', fontsize=9, ha='right')
    for sc, s in M['scenes'].items():
        ax.text(s / 60, -0.07, sc, fontsize=7, color='#868e96', ha='left', rotation=90, va='top')
    if music_lufs is not None:
        ax2 = ax.twinx()
        ax2.plot(music_lufs[0] / 60, music_lufs[1], color='#f08c00', lw=1, alpha=0.8, label='music stem LUFS-S (mixed)')
        ax2.set_ylabel('music stem short-term LUFS', color='#f08c00')
        ax2.set_ylim(np.nanpercentile(music_lufs[1], 1) - 3, np.nanmax(music_lufs[1]) + 3)
    ax.set_xlim(0, M['total'] / 60)
    ax.set_ylim(0, 1.08)
    ax.set_xlabel('episode time (min)', labelpad=22)
    ax.set_ylabel('tension 0–1')
    ax.set_title('Tập 5 · tension map → code music (style C, ~114 BPM; D dorian → F major at S15)', fontsize=11, loc='left')
    fig.tight_layout()
    fig.savefig(png)
    plt.close(fig)


def main():
    tl = sys.argv[sys.argv.index('--timeline') + 1] if '--timeline' in sys.argv else None
    M = build(tl)
    for k in M['keyframes']:
        print(f"{k['t']:8.2f}  {k['v']:.2f}  {k['at']}")
    print('MR1', round(M['mr1'], 2), 'landing', round(M['landing'], 2), 'total', M['total'])
    if '--png' in sys.argv:
        plot(M, sys.argv[sys.argv.index('--png') + 1])


if __name__ == '__main__':
    main()
