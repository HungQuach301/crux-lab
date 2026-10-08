"""Hai thước hình–âm theo cine-lab Q28/Q30 (TAP6-G2-V2 §3) — CHỈ BÁO, chưa là ngưỡng (áp tổng kết Tập 5, mục 14).

tone   — tông màu theo hồi (Q30): khung 1/giây, 64×36, CIELAB; chỉ điểm ảnh L* > 15 (bỏ nền tối, như Q30). Mỗi hồi (`out/timeline.json`
         `acts`, bỏ `ident`) một tông trung bình (L*, a*, b*); báo ΔE76 giữa hai hồi liền nhau, tỉ lệ cặp hồi có ΔE ≥ 5 ("đổi tông
         thấy được") và hồi lạnh nhất (b* thấp nhất). Crux chưa khai màu từng hồi → đo "có đổi tông theo hồi không", không đo "đúng màu".
states — mỗi vật thể thế giới đổi trạng thái có tiếng riêng (Q28 c): đổi trạng thái = `visual_cues` của spine (mốc `beats[].cues`),
         tiếng = `events` của spine (bỏ `data` — tiếng dữ liệu là lớp sonify, không phải tiếng vật thể). Một lần đổi "có tiếng" khi có
         sự kiện bắt đầu trong [t − 0,3 s, t + 0,5 s]. Báo: tỉ lệ lần đổi có tiếng, số loại tiếng khác nhau dùng ở các lần đổi, loại
         chiếm nhiều nhất (%). Tập không có spine: đổi trạng thái = cắt trong cảnh (`out/transitions.json`), tiếng = `out/sfx-events.json`.
    python3 toolkit/indicators/av_indicators.py tone <video> <timeline.json>
    python3 toolkit/indicators/av_indicators.py states spine <spine.json …>
    python3 toolkit/indicators/av_indicators.py states episode <thư mục out/>
"""
import collections, json, os, sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import video as V  # noqa: E402


def tone(vid, timeline):
    acts = [a for a in json.load(open(timeline)).get('acts', []) if a['id'] != 'ident']
    t, fr = V.frames(vid, fps=1, w=64, h=36)
    L = V.lab(fr)
    rows = []
    for a in acts:
        sel = (t >= a['start']) & (t < a['end'])
        px = L[sel].reshape(-1, 3)
        px = px[px[:, 0] > 15]
        if len(px) == 0:
            rows.append({'act': a['id'], 'L': None}); continue
        m = px.mean(0)
        rows.append({'act': a['id'], 'L': round(m[0], 1), 'a': round(m[1], 1), 'b': round(m[2], 1)})
    ok = [r for r in rows if r['L'] is not None]
    dE = [round(float(np.linalg.norm(np.array([x['L'], x['a'], x['b']]) - np.array([y['L'], y['a'], y['b']]))), 1)
          for x, y in zip(ok, ok[1:])]
    return {'acts': rows, 'dE_adjacent': dE, 'share_dE_ge5': round(sum(d >= 5 for d in dE) / len(dE), 2) if dE else None,
            'coldest': min(ok, key=lambda r: r['b'])['act'] if ok else None}


def _score(changes, sounds):
    hit, kinds = 0, []
    for t in changes:
        near = [k for (s, k) in sounds if t - 0.3 <= s <= t + 0.5]
        if near:
            hit += 1; kinds.append(near[0])
    c = collections.Counter(kinds)
    return {'changes': len(changes), 'with_sound': round(hit / len(changes), 2) if changes else None,
            'kinds': len(c), 'top_kind': (c.most_common(1)[0][0], round(c.most_common(1)[0][1] / hit, 2)) if hit else None}


def states_spine(paths):
    ch, so = [], []
    for p in paths:
        d = json.load(open(p))
        off = d.get('episode_t0', 0.0) or 0.0
        beats = {b['id']: b for b in d.get('beats', [])}
        for vc in d.get('visual_cues', []):
            b, _, k = vc.partition('.')
            t = beats.get(b, {}).get('cues', {}).get(k)
            if t is not None:
                ch.append(t + off)
        so += [(e['t'] + off, e['kind']) for e in d.get('events', []) if e.get('kind') != 'data']
    return _score(sorted(ch), sorted(so))


def states_episode(out):
    tr = json.load(open(os.path.join(out, 'transitions.json'))).get('cuts', [])
    sfx = json.load(open(os.path.join(out, 'sfx-events.json'))).get('events', [])
    sfx = sfx if isinstance(sfx, list) else []
    return _score(sorted(c['t'] for c in tr), sorted((e['t'], e.get('kind', '?')) for e in sfx))


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[0] == 'tone':
        r = tone(a[1], a[2])
    elif a[1] == 'spine':
        r = states_spine(a[2:])
    else:
        r = states_episode(a[2])
    print(json.dumps(r, ensure_ascii=False))
