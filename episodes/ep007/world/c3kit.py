"""Tập 7 · C3 · phần chung của năm đoạn (the stack, N1 đường tháng, the bar): lời thật cắt theo câu (wlib), nhịp/động tác/kiểm quy tắc
(spine v2 nhà máy), khung khoá trạng thái vật (giá trị theo giờ) và âm của mỗi lần đổi trạng thái.
  steps(times, values, ramp, v0, pitch) — khung khoá [[t, v], …] (scene.js nội suy tuyến tính, giữ trước mốc đầu / sau mốc cuối) + mỗi lần đổi
      một nốt 'data' (cao độ = pitch(v) ∈ [0, 1], audio.py S2); over=True → nốt có bội âm sáng (dùng cho ô trễ / phần warn).
Mật độ sfx (F-2, sfx_labels.py): nốt 'data' là lớp âm dữ liệu riêng (không tính vào sfx/phút); 'tick'/'land'/whoosh giữ ≤ 6 trong 10 s."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import wlib            # take hiện tại, cắt theo câu, đầu từ theo năng lượng  # noqa: E402
import spine as SV     # spine v2 nhà máy (wlib đã thêm toolkit/factory/world vào sys.path)  # noqa: E402

PAD = 0.25
CLAIMS = json.load(open(os.path.join(HERE, 'claims.json')))
G = CLAIMS['_geom']
INPUTS = ['episodes/ep007/world/claims.json', 'episodes/ep007/world/obj7.js', 'episodes/ep007/world/c3kit.js']


def steps(times, values, ramp=0.25, v0=None, pitch=lambda v: v, over=False):
    """Khung khoá [[t, v]] + nốt dữ liệu: tại times[i] giá trị đi từ giá trị trước tới values[i] trong ramp s."""
    prev = values[0] if v0 is None else v0
    kf, ev = [[0.0, prev]], []
    for t, v in zip(times, values):
        kf += [[round(t, 3), prev], [round(t + ramp, 3), v]]
        ev.append({'t': round(t, 3), 'kind': 'data', 'v': round(min(1.0, max(0.0, pitch(v))), 3), **({'over': True} if over else {})})
        prev = v
    return kf, ev


def spread(a, b, n):
    """n mốc đều trong [a, b] (mốc đầu = a)."""
    return [a + (b - a) * i / max(1, n - 1) for i in range(n)]


def moves_from(specs, eps=0.01):
    out = []
    for verb, a, b, after, before, dur, reason, snd, kw in specs:
        t0, t1 = SV.window(after, before, dur, PAD, eps=eps, **kw)
        out.append({'verb': verb, 'from': a, 'to': b, 't0': t0, 't1': t1, 'reason': reason, 'sound': snd})
    return out


def finish(here, name, words, takes, lines, end, beats, moves, events, extra, accents, hold=1.0):
    """Ghép spine.json, tự kiểm quy tắc 2/3/7, ghi inputs.json (khoá cache render), in tóm tắt; thoát 1 nếu vi phạm."""
    total = round(end + hold, 2)
    ev = sorted(events + SV.move_sounds(moves, lambda m: 0.6), key=lambda e: e['t'])
    errs = SV.check_rules(beats, moves, PAD)
    if any(e['t'] > total for e in ev): errs.append('sự kiện âm sau cuối đoạn')
    tension = [[0, 0.2], [beats[0]['t0'], 0.3], [beats[len(beats) // 2]['t0'], 0.45], [total - 1.2, 0.3], [total, 0.1]]
    spine = {'segment': name, 'version': 1, 'total': total, 'fps': 30, 'pad': PAD, 'takes': takes, 'words': words, 'beats': beats, 'moves': moves,
             'events': ev, 'tension': tension, 'shots': SV.shots_for(moves, total), 'music_plan': wlib.music_plan_flat(total, accents),
             'mix': {'music_db': 17.0, 'data_db': 25.0}, **extra, 'checks': {'rule2_rule3_rule7': errs or 'OK'}}
    json.dump(spine, open(os.path.join(here, 'spine.json'), 'w'), indent=1, ensure_ascii=False)
    json.dump(INPUTS, open(os.path.join(here, 'inputs.json'), 'w'))
    print('total', total, 'moves', [(m['verb'], m['t0'], m['t1']) for m in moves])
    for b in beats: print(' ', b['id'], b['mode'], round(b['t0'], 2), round(b['t1'], 2), {k: round(v, 2) for k, v in b['cues'].items()})
    print('checks', errs or 'OK')
    sys.exit(1 if errs else 0)
