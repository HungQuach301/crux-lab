"""Nhà máy · F-2 (BACKLOG; checks-appeal A19): kiểm tự động MẬT ĐỘ HIỆU ỨNG ÂM và NHÃN ĐÈ NHAU — bộ đo của bên dựng, không thay checks/.
Ngưỡng dưới đây là TẠM (A19: "bên dựng làm bộ đo trước, K hiệu chuẩn rồi mới thành ngưỡng"); cấp mỗi phát hiện là WARN hoặc BLOCK.

  sfx    : spine.events (trừ 'data' = âm dữ liệu, lớp riêng; trừ nền liên tục SFX_BEDS) — sự kiện/phút cả đoạn, số sự kiện tối đa trong
           cửa sổ trượt 10 s, sự kiện bắt đầu TRONG một từ đang nói (spine.words [s, e]); quá ngưỡng → WARN.
           Âm vang (t → t + dur) chạm một TỪ KHOÁ (spine.beats[].cues → từ) → đo che lấp: có stem (<đoạn>.audio/stems/{voice,sfx}.wav)
           thì SNR lời/sfx trong khoảng từ khoá < KEYWORD_SNR_MIN_DB → BLOCK, < KEYWORD_SNR_WARN_DB → WARN, còn lại chỉ báo;
           không có stem → BLOCK (không chứng minh được không che).
  labels : nhật ký trang (core.js) mỗi 0,1 s — hai hộp chữ cùng khung giao nhau quá LABEL_TOL_PX; đường vẽ trên lớp phủ (log.lines, F-2) cắt
           hộp chữ (đường vẽ SAU chữ, hoặc chữ không có nền). Cả hai ở trạng thái đọc (độ mờ ≥ STEADY_ALPHA, như C14) → BLOCK; đang mờ dần → WARN.
Giới hạn: đường 3D (WebGL) và đường cong (bezier/arc) không vào log.lines — chỉ moveTo/lineTo trên lớp phủ 2D.
"""
import json, os
import numpy as np

# ---- ngưỡng (tạm, K hiệu chuẩn — A19) ----
SFX_PER_MIN_WARN = 30      # > 1 sự kiện / 2 s trung bình cả đoạn: lớp sfx thành trang trí liên tục thay vì dấu nhấn (lượt đạo diễn: "sfx dày")
SFX_WINDOW_S = 10.0        # cửa sổ trượt
SFX_WINDOW_WARN = 6        # > 6 trong 10 s: một nhịp ~3 s chỉ đỡ ~1 cử chỉ (whoosh + chạm = 2 sự kiện) → > 3 cử chỉ / 10 s là dày
SFX_ON_SPEECH_WARN_SHARE = 0.5   # > 50 % sự kiện bắt đầu trong một từ THƯỜNG (không phải từ khoá): lớp sfx tranh với lời thay vì nhấn
                                 # (S2: âm nằm ở khe lời hoặc đúng dấu nhấn từ khoá — dấu nhấn đo riêng bằng SNR bên dưới)
KEYWORD_SNR_MIN_DB = 10.0  # lời/sfx trong khoảng từ khoá: ≥ +10 dB thì tiếng không lời gần như không giảm độ hiểu từ (SRT người nghe thường
                           # ≈ −5 dB với nhiễu dải rộng; chừa ~15 dB cho loa điện thoại / người nghe không bản ngữ); < 10 → BLOCK
KEYWORD_SNR_WARN_DB = 15.0  # 10–15 dB: sát ngưỡng che → WARN; ≥ 15 dB: dấu nhấn đúng thiết kế, chỉ báo
SFX_BEDS = {'drone_on'}    # nền liên tục, không phải sự kiện nhấn
DEFAULT_DUR = {'tick': 0.15, 'land': 0.3, 'chime': 1.0, 'impact': 1.0, 'thud': 0.6, 'gather': 1.6}   # thời gian vang khi spine không ghi dur
LABEL_TOL_PX = 1.0         # giao nhau ≤ 1 px (thiết kế 1920×1080) = chạm mép, không tính (hộp đo glyph, làm tròn 0,1 px)
LABEL_MIN_ALPHA = 0.1      # chữ mờ hơn coi như chưa hiện
STEADY_ALPHA = 0.95        # như C14: chữ ở trạng thái đọc


def _dur(e):
    if 'dur' in e: return float(e['dur'])
    for k in ('to', 'until'):
        if k in e: return float(e[k]) - float(e['t'])
    return DEFAULT_DUR.get(e['kind'], 0.3)


def sfx_events(spine):
    return sorted(({'t': round(float(e['t']), 3), 'kind': e['kind'], 'end': round(float(e['t']) + _dur(e), 3)}
                   for e in spine.get('events', []) if e['kind'] != 'data' and e['kind'] not in SFX_BEDS), key=lambda e: e['t'])


def spoken(spine):
    return [w for w in spine.get('words', []) if not str(w['w']).startswith('[') and w['e'] > w['s']]


def keywords(spine):
    """beats[].cues → [{name, t, s, e, w}] (từ có đầu = mốc, không thì từ chứa mốc)."""
    W, out = spoken(spine), []
    for b in spine.get('beats', []):
        for k, t in b.get('cues', {}).items():
            w = min(W, key=lambda w: abs(w['s'] - t), default=None)
            if w is None or abs(w['s'] - t) > 0.02:
                w = next((w for w in W if w['s'] <= t < w['e']), None)
            if w: out.append({'name': f"{b['id']}.{k}", 't': t, 's': w['s'], 'e': w['e'], 'w': w['w']})
    return sorted(out, key=lambda k: k['t'])


def thin_events(spine, max10s=4, kinds=('tick',), plain=True, plain_kinds=('tick', 'land')):
    """F-18 (sfx dày — D-010 §6, T4): bản spine bớt dấu nhấn thừa, TẤT ĐỊNH. Chỉ bỏ sự kiện thuộc `kinds` (mặc định tick: dấu nhấn rời, không
    gắn cú máy — whoosh/rise gắn động tác máy quay theo quy tắc 3 thì giữ). (1) plain=True: bỏ sự kiện thuộc `plain_kinds` bắt đầu trong một
    từ THƯỜNG (không phải từ khoá; cùng định nghĩa với checks T4) — gồm `land` (tiếng chạm khi máy tới: whoosh của cú máy vẫn còn, tiếng chạm
    giữa từ thường tranh với lời, G-006); (2) còn cửa sổ 10 s nào > max10s sự kiện (mọi kind trừ data/nền) → bỏ sự kiện `kinds`
    MUỘN NHẤT của cửa sổ dày nhất, lặp tới khi hết hoặc cửa sổ không còn sự kiện bỏ được (báo `stuck`).
    Trả spine mới (events đã bớt + `sfx_thin` ghi sự kiện bỏ và lý do); spine gốc không đổi. Ghi spine này ra spine.json của đoạn = khai
    trên spine (checks T4 và audio.py cùng đọc một danh sách)."""
    W = spoken(spine)
    kw = {round(t, 3) for b in spine.get('beats', []) for t in (b.get('cues') or {}).values()}
    on_plain = lambda t: any(w['s'] <= t < w['e'] and not any(abs(w['s'] - k) <= 0.02 or w['s'] <= k < w['e'] for k in kw) for w in W)
    ev = list(spine.get('events', []))
    counted = lambda e: e['kind'] != 'data' and e['kind'] not in SFX_BEDS
    drop = []
    if plain:
        for e in ev:
            if e['kind'] in plain_kinds and on_plain(float(e['t'])):
                drop.append({'t': e['t'], 'kind': e['kind'], 'why': 'plain word'})
        ids = {(d['t'], d['kind']) for d in drop}
        ev = [e for e in ev if (e['t'], e['kind']) not in ids]
    stuck = []
    while True:
        ts = sorted(float(e['t']) for e in ev if counted(e))
        best = max(((sum(1 for x in ts if t <= x < t + SFX_WINDOW_S), t) for t in ts), default=(0, 0.0))
        if best[0] <= max10s:
            break
        t0 = best[1]
        cand = [e for e in ev if e['kind'] in kinds and t0 <= float(e['t']) < t0 + SFX_WINDOW_S]
        if not cand:
            stuck.append(round(t0, 3)); break
        e = max(cand, key=lambda e: float(e['t']))
        drop.append({'t': e['t'], 'kind': e['kind'], 'why': f'>{max10s} in 10 s from {round(t0, 3)}'})
        ev.remove(e)
    out = dict(spine)
    out['events'] = ev
    out['sfx_thin'] = {'max10s': max10s, 'kinds': list(kinds), 'plain': plain, 'plain_kinds': list(plain_kinds), 'dropped': drop, 'stuck': stuck}
    return out


# ---- F-18 (chủ dự án 15/10, mục 2e): nhãn cảnh → tệp ghi âm thật, không lặp ----
ACCENT_KINDS = ('tick', 'land')            # dấu nhấn rời → tiếng foley theo nhãn cảnh
MOVE_KINDS = ('whoosh_mode', 'whoosh_push', 'whoosh_soft', 'whoosh_air', 'swish')   # tiếng động tác máy quay → 'chuyen-canh'
KIND_DEFAULT = {'tick': 'go-nhe', 'land': 'va-mem'}   # cảnh không khai nhãn
REUSE_S = 60.0                              # một tệp không dùng lại trong 60 s (giờ của tập)
PITCH_ST = 1.0                              # biến thể độ cao ± 1 nửa cung (đổi tốc độ phát)
GAIN_JITTER_DB = 1.5


def _scene_spans(spine):
    """{cảnh: (a, b)} theo giờ của đoạn: từ từ đầu tiên của cảnh tới từ đầu tiên của cảnh sau (cảnh đầu từ 0, cảnh cuối tới total)."""
    first = {}
    for w in spoken(spine):
        sc = str(w.get('sid', '')).split('.')[0]
        if sc and sc not in first:
            first[sc] = float(w['s'])
    ids = [sc for sc in spine.get('scenes', []) if sc in first] or sorted(first, key=first.get)
    out = {}
    for i, sc in enumerate(ids):
        out[sc] = (0.0 if i == 0 else first[sc], first[ids[i + 1]] if i + 1 < len(ids) else float(spine.get('total') or 1e9))
    return out


def plan_real(spine, labels, manifest, seed=1807, used=None, reuse_s=REUSE_S, only_scenes=None):
    """Gắn tệp thật cho sự kiện sfx của spine, TẤT ĐỊNH (rng = hạt + id đoạn). labels = {cảnh: [nhãn…]} (nhãn = tags của manifest:
    giay, tien-xu, dong-ho, may-chu, cua, chuyen-canh, …). tick/land trong cảnh có nhãn → xoay vòng các nhãn của cảnh; cảnh không nhãn →
    KIND_DEFAULT; whoosh → 'chuyen-canh'. Tệp chọn ngẫu nhiên (hạt cố định) trong các tệp của nhãn CHƯA dùng trong `reuse_s` s (giờ của tập =
    episode_t0 + t; `used` {id: giờ dùng cuối} truyền qua các đoạn); không còn tệp → giữ tiếng tổng hợp (ghi `kept_synth`), không lặp tệp.
    Biến thể: tốc độ 2^(±PITCH_ST/12), mức ± GAIN_JITTER_DB, điểm bắt đầu trong tệp dài (≥ 3 s). Trả spine mới: events có
    {real, rate, gain_db, offset, label} + `sfx_real: {planned: true, labels, seed, reuse_s, plan}` (audio.py chỉ phát tệp cho sự kiện có `real`).
    only_scenes: chỉ thay ở các cảnh này (cảnh khác giữ tiếng tổng hợp, không vào kế hoạch)."""
    import hashlib
    used = {} if used is None else used
    t0 = float(spine.get('episode_t0') or 0)
    rng = np.random.default_rng(int(hashlib.sha256(f"{seed}|{spine.get('segment', '')}".encode()).hexdigest()[:12], 16))
    pool = {}
    for r in sorted(manifest.values(), key=lambda r: r['id']):
        for tg in r.get('tags', []):
            pool.setdefault(tg, []).append(r)
    spans = _scene_spans(spine)
    scene_of = lambda t: next((sc for sc, (a, b) in spans.items() if a <= t < b), None)
    turn = {}
    ev, plan = [], []
    for e in sorted(spine.get('events', []), key=lambda e: (float(e['t']), e['kind'])):
        e = dict(e)
        k, t = e['kind'], float(e['t'])
        sc = scene_of(t)
        if only_scenes is not None and sc not in only_scenes:
            ev.append(e); continue
        if k in ACCENT_KINDS:
            labs = list((labels or {}).get(sc) or []) or [KIND_DEFAULT[k]]
            i = turn.get(sc, 0); turn[sc] = i + 1
            label = labs[i % len(labs)]
        elif k in MOVE_KINDS:
            label = 'chuyen-canh'
        else:
            ev.append(e); continue
        T = t0 + t
        free = [r for r in pool.get(label, []) if T - used.get(r['id'], -1e9) >= reuse_s]
        if not free:
            plan.append({'t': round(T, 3), 'kind': k, 'scene': sc, 'label': label, 'kept_synth': True})
            ev.append(e); continue
        r = free[int(rng.integers(len(free)))]
        used[r['id']] = T
        e.update({'real': r['id'], 'label': label, 'rate': round(float(2 ** (rng.uniform(-PITCH_ST, PITCH_ST) / 12)), 4),
                  'gain_db': round(float(rng.uniform(-GAIN_JITTER_DB, GAIN_JITTER_DB)), 2),
                  'offset': round(float(rng.uniform(0, max(0.0, r['dur'] - 3.0))), 3) if r['dur'] >= 3.0 else 0.0})
        plan.append({'t': round(T, 3), 'kind': k, 'scene': sc, 'label': label, 'file': r['id'], 'rate': e['rate'], 'gain_db': e['gain_db']})
        ev.append(e)
    out = dict(spine)
    out['events'] = ev
    out['sfx_real'] = {'planned': True, 'labels': labels, 'seed': seed, 'reuse_s': reuse_s, 'plan': plan}
    return out


def repeat_report(plan, reuse_s=REUSE_S):
    """Đo lặp tệp trên kế hoạch (giờ của tập): số lần cùng tệp dùng lại trong reuse_s s, số tệp khác nhau / số sự kiện phát tệp."""
    last, rep = {}, 0
    real = [p for p in plan if p.get('file')]
    for p in sorted(real, key=lambda p: p['t']):
        if p['t'] - last.get(p['file'], -1e9) < reuse_s:
            rep += 1
        last[p['file']] = p['t']
    return {'events_real': len(real), 'files': len({p['file'] for p in real}), 'reused_within': rep,
            'kept_synth': sum(1 for p in plan if p.get('kept_synth'))}


def _load_stems(audio_dir):
    if not audio_dir: return None
    p = {k: os.path.join(audio_dir, 'stems', k + '.wav') for k in ('voice', 'sfx')}
    if not all(os.path.exists(v) for v in p.values()): return None
    from scipy.io import wavfile
    out = {}
    for k, f in p.items():
        sr, x = wavfile.read(f); x = np.asarray(x, np.float64)
        out[k] = (sr, x.mean(axis=1) if x.ndim == 2 else x)
    return out


def _snr(stems, s, e):
    (sr, v), (_, x) = stems['voice'], stems['sfx']
    i0, i1 = int(s * sr), max(int(e * sr), int(s * sr) + 1)
    rv, rx = np.sqrt(np.mean(v[i0:i1] ** 2) + 1e-20), np.sqrt(np.mean(x[i0:i1] ** 2) + 1e-20)
    return round(float(20 * np.log10(rv / rx)), 1)


def sfx_check(spine, audio_dir=None):
    ev, W, total = sfx_events(spine), spoken(spine), float(spine.get('total') or 0) or None
    total = total or max([e['end'] for e in ev] + [w['e'] for w in W] + [1e-9])
    per_min = round(len(ev) / (total / 60), 1) if total else 0.0
    best = (0, None)
    for e in ev:
        n = [x['t'] for x in ev if e['t'] <= x['t'] < e['t'] + SFX_WINDOW_S]
        if len(n) > best[0]: best = (len(n), {'t0': e['t'], 't1': round(e['t'] + SFX_WINDOW_S, 3), 'times': n})
    K = keywords(spine)
    on_speech = [{'t': e['t'], 'kind': e['kind'], 'word': w['w'], 'keyword': any(k['s'] == w['s'] for k in K)}
                 for e in ev for w in W if w['s'] <= e['t'] < w['e']]
    plain = [o for o in on_speech if not o['keyword']]
    stems, kw_hits = _load_stems(audio_dir), []
    for k in K:
        hit = [e for e in ev if e['t'] < k['e'] and e['end'] > k['s']]
        if not hit: continue
        snr = _snr(stems, k['s'], k['e']) if stems else None
        kw_hits.append({'keyword': k['name'], 'word': k['w'], 's': k['s'], 'e': k['e'], 'events': [(e['t'], e['kind']) for e in hit],
                        'snr_db': snr, 'level': 'BLOCK' if snr is None or snr < KEYWORD_SNR_MIN_DB else 'WARN' if snr < KEYWORD_SNR_WARN_DB else 'OK'})
    warn, block = [], []
    if per_min > SFX_PER_MIN_WARN: warn.append(f'sfx {per_min}/phút > {SFX_PER_MIN_WARN}')
    if best[0] > SFX_WINDOW_WARN: warn.append(f"sfx {best[0]} sự kiện trong {SFX_WINDOW_S:g} s từ {best[1]['t0']} > {SFX_WINDOW_WARN}")
    if ev and len(plain) / len(ev) > SFX_ON_SPEECH_WARN_SHARE:
        warn.append(f'sfx đè từ thường {len(plain)}/{len(ev)} sự kiện > {SFX_ON_SPEECH_WARN_SHARE:.0%}: ' + ', '.join(f"{o['t']} {o['kind']}/'{o['word']}'" for o in plain))
    for h in (h for h in kw_hits if h['level'] != 'OK'):
        msg = f"sfx {h['events']} trên từ khoá {h['keyword']} '{h['word']}' {h['s']}–{h['e']}" + \
              (f" SNR {h['snr_db']} dB" + (f' < {KEYWORD_SNR_MIN_DB:g}' if h['level'] == 'BLOCK' else '') if h['snr_db'] is not None else ' (không có stem để đo)')
        (block if h['level'] == 'BLOCK' else warn).append(msg)
    return {'events': len(ev), 'duration_s': round(total, 2), 'per_min': per_min,
            'max_window': {'count': best[0], **(best[1] or {})}, 'on_speech': {'count': len(on_speech), 'plain_words': len(plain), 'times': on_speech},
            'keyword_hits': kw_hits, 'stems': bool(stems), 'warn': warn, 'block': block}


# ------------------------------------------------------------------ nhãn
def _inter(a, b, tol=LABEL_TOL_PX):
    w, h = min(a[2], b[2]) - max(a[0], b[0]), min(a[3], b[3]) - max(a[1], b[1])
    return (round(w, 1), round(h, 1)) if w > tol and h > tol else None


def seg_hits_box(seg, box, pad=0.0):
    """Đoạn thẳng [x0,y0,x1,y1] cắt vào hộp [x0,y0,x1,y1] co vào LABEL_TOL_PX (nới bởi pad = nửa bề dày nét) — Liang–Barsky."""
    bx0, by0, bx1, by1 = box[0] + LABEL_TOL_PX - pad, box[1] + LABEL_TOL_PX - pad, box[2] - LABEL_TOL_PX + pad, box[3] - LABEL_TOL_PX + pad
    if bx1 <= bx0 or by1 <= by0: return False
    x0, y0, x1, y1 = seg; dx, dy = x1 - x0, y1 - y0; u0, u1 = 0.0, 1.0
    for p, q in ((-dx, x0 - bx0), (dx, bx1 - x0), (-dy, y0 - by0), (dy, by1 - y0)):
        if p == 0:
            if q < 0: return False
        else:
            r = q / p
            if p < 0: u0 = max(u0, r)
            else: u1 = min(u1, r)
            if u0 > u1: return False
    return True


def label_check(logs):
    """logs: [{t, texts: [{text, box, opacity?, n?, plate?}], lines?: [{n, a, w, seg: [[x0,y0,x1,y1]…]}]}] (core.js)."""
    overlaps, crossings, lines_logged = [], [], any('lines' in l for l in logs)
    for l in logs:
        T = [x for x in l.get('texts', []) if x.get('opacity', 1) >= LABEL_MIN_ALPHA]
        for i in range(len(T)):
            for j in range(i + 1, len(T)):
                a, b = T[i], T[j]
                if a['text'] == b['text'] and max(abs(p - q) for p, q in zip(a['box'], b['box'])) <= LABEL_TOL_PX: continue   # cùng nhãn vẽ hai lần
                ov = _inter(a['box'], b['box'])
                if ov:
                    steady = min(a.get('opacity', 1), b.get('opacity', 1)) >= STEADY_ALPHA
                    overlaps.append({'t': l['t'], 'a': a['text'], 'b': b['text'], 'overlap_px': ov, 'level': 'BLOCK' if steady else 'WARN'})
        for ln in l.get('lines', []):
            if ln.get('a', 1) < LABEL_MIN_ALPHA: continue
            for x in T:
                if x.get('plate') and ln.get('n', 1e9) < x.get('n', -1): continue   # đường vẽ trước chữ có nền: nền che đường
                if any(seg_hits_box(s, x['box'], ln.get('w', 0) / 2) for s in ln['seg']):
                    steady = min(ln.get('a', 1), x.get('opacity', 1)) >= STEADY_ALPHA
                    crossings.append({'t': l['t'], 'text': x['text'], 'line_n': ln.get('n'), 'level': 'BLOCK' if steady else 'WARN'})
    def spans(items, key):
        out = {}
        for it in items:
            k = key(it); s = out.setdefault(k, {'what': k, 't0': it['t'], 't1': it['t'], 'samples': 0, 'level': 'WARN'})
            s['t0'], s['t1'] = min(s['t0'], it['t']), max(s['t1'], it['t']); s['samples'] += 1
            if it['level'] == 'BLOCK': s['level'] = 'BLOCK'
        return list(out.values())
    ov_s = spans(overlaps, lambda o: ' × '.join(sorted((o['a'], o['b']))))
    cr_s = spans(crossings, lambda c: f"đường × {c['text']}")
    warn = [f"{s['what']} {s['t0']}–{s['t1']} s ({s['samples']} mẫu)" for s in ov_s + cr_s if s['level'] == 'WARN']
    block = [f"{s['what']} {s['t0']}–{s['t1']} s ({s['samples']} mẫu)" for s in ov_s + cr_s if s['level'] == 'BLOCK']
    return {'samples': len(logs), 'overlaps': {'count': len(overlaps), 'spans': ov_s, 'examples': overlaps[:8]},
            'line_crossings': {'count': len(crossings), 'spans': cr_s, 'examples': crossings[:8]} if lines_logged else {'skipped': 'nhật ký không có lines (render trước F-2)'},
            'warn': warn, 'block': block}


def check(spine, logs, audio_dir=None):
    s, l = sfx_check(spine, audio_dir), label_check(logs)
    block, warn = s['block'] + l['block'], s['warn'] + l['warn']
    return {'level': 'BLOCK' if block else 'WARN' if warn else 'OK', 'block': block, 'warn': warn, 'sfx': s, 'labels': l}


def summary(r):
    s, l = r['sfx'], r['labels']
    return {'level': r['level'], 'sfx_per_min': s['per_min'], 'sfx_max_10s': s['max_window']['count'], 'sfx_on_speech': s['on_speech']['count'], 'sfx_on_plain_words': s['on_speech']['plain_words'],
            'sfx_events': s['events'], 'keyword_hits': len(s['keyword_hits']), 'min_keyword_snr_db': min((h['snr_db'] for h in s['keyword_hits'] if h['snr_db'] is not None), default=None), 'label_overlaps': l['overlaps']['count'],
            'line_crossings': l['line_crossings'].get('count', 'không ghi'), 'block': len(r['block']), 'warn': len(r['warn'])}


if __name__ == '__main__':   # chạy đọc-không-ghi: python3 sfx_labels.py <spine.json> <video.log.json> [<audio_dir>]
    import sys
    r = check(json.load(open(sys.argv[1])), sorted(json.load(open(sys.argv[2])), key=lambda l: l['t']), sys.argv[3] if len(sys.argv) > 3 else None)
    print(json.dumps({'summary': summary(r), 'block': r['block'], 'warn': r['warn'],
                      'on_speech': r['sfx']['on_speech']['times'], 'max_window': r['sfx']['max_window'],
                      'keyword_hits': r['sfx']['keyword_hits']}, ensure_ascii=False, indent=1))
