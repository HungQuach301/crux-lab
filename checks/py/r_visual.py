"""§4 (pre-production, camera, colour, transitions), §4.7 layout repetition, §7 thumbnails."""
import json
import re
import subprocess

import numpy as np
from scipy import stats

from common import FPS, Missing, metric, rule, verdict, video_frames, words
from r_audio import asr_master, camera_moves, camera_speed

SHOT_FIELDS = ('size', 'move', 'moveReason')  # 2.5D (DX-V12): the brief-D fields focalMm and angle (3D lens and camera angle) are dropped


@rule('V01', 'DX-V12', 'preprod/shotlist.json shots[]: fields size, move, moveReason (2.5D shot list: no simulated focal length, no 3D camera angle); '
      'coverage of out/timeline.json scenes (shots[].scene); storyboard (preprod/storyboard.*) and colour script (preprod/color-script.*) present',
      'every shot has all 3 fields non-empty; moveReason ≥ 3 words; every timeline scene has ≥ 1 shot; storyboard and colour script present')
def v01_shotlist(ctx):
    import glob
    sl = ctx.json('preprod/shotlist.json')['shots']
    bad = []
    for s in sl:
        miss = [f for f in SHOT_FIELDS if s.get(f) in (None, '', [])]
        if miss:
            bad.append((s.get('id'), 'missing ' + ','.join(miss)))
        elif len(words(str(s['moveReason']))) < 3:
            bad.append((s.get('id'), 'reason too short'))
    covered = {s.get('scene') for s in sl}
    unc = [s['id'] for s in ctx.scenes() if s['id'] not in covered]
    sb = glob.glob(ctx.path('preprod/storyboard.*')) + glob.glob(ctx.path('preprod/storyboard/*'))
    cs = glob.glob(ctx.path('preprod/color-script.*')) + glob.glob(ctx.path('preprod/color-script/*'))
    return verdict('V01', [metric('shots', len(sl), '>=', 1), metric('shots with field problems', len(bad), '<=', 0), metric('scenes without a shot', len(unc), '<=', 0),
                           metric('storyboard present', bool(sb), '==', True), metric('colour script present', bool(cs), '==', True)], details=[{'bad': bad[:10], 'uncovered': unc[:10]}])


def move_profile(t, pos, a, b, pad=18):
    """Unit progress u(t) of a move from the rest position `pad` frames before it to the rest position `pad` frames after it."""
    i0, i1 = max(0, a - pad), min(len(t), b + pad)
    p0, p1 = pos[i0], pos[i1 - 1]
    d = p1 - p0
    L = np.linalg.norm(d)
    if L < 1e-9:
        return None, None
    u = (pos[i0:i1] - p0) @ d / (L * L)
    return t[i0:i1], u


@rule('V05', 'DX-V8', 'camera path out/camera.json, per frame: 2.5D {t, x, y, zoom} (pan over the chart plane in page px, zoom = scale) or the legacy {t, pos, target, fovDeg, focusDist}. '
      'Speeds/accelerations normalised to frame widths (fw; 2.5D: pan / (1920/zoom) + |d ln zoom|). '
      'Moves as in A10, ≥ 0.5 s. Per move: ease = mean speed over the first and last 10% of the move ÷ peak; linear = speed stays within ±10% of its mean over ≥ 60% of the move; '
      'progress u from the rest position 0.6 s before to the rest position 0.6 s after; anticipation = u ≤ −0.3% before the peak-speed instant; overshoot = u peaks 0.3–8% past 1 after it and settles within 0.3%; peak |acceleration|. '
      'Truth check: Spearman ρ between camera speed and picture change (mean |ΔY| per 0.5 s window)',
      '≥ 5 moves; every move eased (≤ 0.4) and none linear; anticipation in ≥ 30% and overshoot in ≥ 30% of moves ≥ 1 s; no overshoot > 8%; peak |a| ≤ 8 fw/s²; ρ ≥ 0.3')
def v05_camera(ctx):
    t, sp, pos, tgt, width = camera_speed(ctx)
    moves = [(a, b) for a, b in camera_moves(t, sp) if t[b - 1] - t[a] >= 0.5]
    dt = np.gradient(t)
    acc = np.abs(np.gradient(sp) / dt)
    rows = []
    for a, b in moves:
        n = b - a
        k = max(1, n // 10)
        pk = sp[a:b].max()
        ease = (sp[a:a + k].mean() + sp[b - k:b].mean()) / 2 / pk
        m = sp[a:b].mean()
        linear = np.mean(np.abs(sp[a:b] - m) <= 0.1 * m) >= 0.6
        tt, u = move_profile(t, (pos + tgt) / 2, a, b)
        anti = over = False
        ov = 0.0
        if u is not None:
            k = int(np.argmin(np.abs(tt - t[a + int(np.argmax(sp[a:b]))])))  # peak-speed instant
            anti = u[:k].min() <= -0.003 if k else False
            ov = float(u[k:].max() - 1)
            over = 0.003 <= ov <= 0.08 and abs(u[-1] - 1) < 0.003
        rows.append({'t': round(float(t[a]), 2), 'dur': round(float(t[b - 1] - t[a]), 2), 'ease': round(float(ease), 2), 'linear': bool(linear),
                     'anticipation': bool(anti), 'overshoot': round(ov, 4), 'overshootOK': bool(over), 'peakAcc': round(float(acc[a:b].max()), 2)})
    long_ = [r for r in rows if r['dur'] >= 1.0]
    pct = lambda xs: 100 * len(xs) / len(long_) if long_ else None
    # picture truth check
    diffs, prev = {}, None
    for tt_, y in video_frames(ctx.video(), scale=8):
        y = y.astype(np.int16)
        if prev is not None:
            diffs[round(tt_ * 2) / 2] = diffs.get(round(tt_ * 2) / 2, []) + [float(np.mean(np.abs(y - prev)))]
        prev = y
    ks = sorted(diffs)
    cam = [float(np.interp(k, t, sp)) for k in ks]
    rho = stats.spearmanr(cam, [np.mean(diffs[k]) for k in ks]).statistic if len(ks) > 5 else None
    ms = [metric('camera moves', len(rows), '>=', 5), metric('worst ease ratio', max((r['ease'] for r in rows), default=None), '<=', 0.4),
          metric('linear moves', sum(r['linear'] for r in rows), '<=', 0), metric('anticipation in moves ≥1 s (%)', pct([r for r in long_ if r['anticipation']]), '>=', 30.0, '%'),
          metric('overshoot in moves ≥1 s (%)', pct([r for r in long_ if r['overshootOK']]), '>=', 30.0, '%'),
          metric('overshoot > 8%', sum(r['overshoot'] > 0.08 for r in rows), '<=', 0), metric('peak |a| fw/s²', max((r['peakAcc'] for r in rows), default=None), '<=', 8.0),
          metric('camera~picture Spearman', float(rho) if rho is not None else None, '>=', 0.3)]
    return verdict('V05', ms, details=rows[:40])


# ---- colour vision -------------------------------------------------------------------------------
MACHADO = {  # Machado, Oliveira & Fernandes 2009, severity 1.0, linear RGB
    'protanopia': np.array([[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]]),
    'deuteranopia': np.array([[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]]),
}


def srgb_to_lin(c):
    c = np.asarray(c, float) / 255
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def lin_to_lab(l):
    M = np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]])
    X, Y, Z = M @ np.clip(l, 0, 1)
    wn = (0.95047, 1.0, 1.08883)
    f = lambda v: np.where(v > (6 / 29) ** 3, np.cbrt(v), v / (3 * (6 / 29) ** 2) + 4 / 29)
    fx, fy, fz = f(X / wn[0]), f(Y / wn[1]), f(Z / wn[2])
    return np.array([116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)])


def de2000(l1, l2):
    L1, a1, b1 = l1
    L2, a2, b2 = l2
    C1, C2 = np.hypot(a1, b1), np.hypot(a2, b2)
    Cb = (C1 + C2) / 2
    G = 0.5 * (1 - np.sqrt(Cb ** 7 / (Cb ** 7 + 25 ** 7)))
    a1p, a2p = (1 + G) * a1, (1 + G) * a2
    C1p, C2p = np.hypot(a1p, b1), np.hypot(a2p, b2)
    h1p, h2p = np.degrees(np.arctan2(b1, a1p)) % 360, np.degrees(np.arctan2(b2, a2p)) % 360
    dLp, dCp = L2 - L1, C2p - C1p
    dh = h2p - h1p
    if C1p * C2p == 0:
        dh = 0
    elif dh > 180:
        dh -= 360
    elif dh < -180:
        dh += 360
    dHp = 2 * np.sqrt(C1p * C2p) * np.sin(np.radians(dh / 2))
    Lbp, Cbp = (L1 + L2) / 2, (C1p + C2p) / 2
    hbp = (h1p + h2p) / 2 if abs(h1p - h2p) <= 180 else (h1p + h2p + 360) / 2
    if C1p * C2p == 0:
        hbp = h1p + h2p
    T = 1 - 0.17 * np.cos(np.radians(hbp - 30)) + 0.24 * np.cos(np.radians(2 * hbp)) + 0.32 * np.cos(np.radians(3 * hbp + 6)) - 0.2 * np.cos(np.radians(4 * hbp - 63))
    dth = 30 * np.exp(-(((hbp - 275) / 25) ** 2))
    Rc = 2 * np.sqrt(Cbp ** 7 / (Cbp ** 7 + 25 ** 7))
    Sl = 1 + 0.015 * (Lbp - 50) ** 2 / np.sqrt(20 + (Lbp - 50) ** 2)
    Sc, Sh = 1 + 0.045 * Cbp, 1 + 0.015 * Cbp * T
    Rt = -np.sin(np.radians(2 * dth)) * Rc
    return float(np.sqrt((dLp / Sl) ** 2 + (dCp / Sc) ** 2 + (dHp / Sh) ** 2 + Rt * (dCp / Sc) * (dHp / Sh)))


def hex_rgb(h):
    h = h.lstrip('#')
    return [int(h[i:i + 2], 16) for i in (0, 2, 4)]


def rel_lum(rgb):
    return float(np.dot([0.2126, 0.7152, 0.0722], srgb_to_lin(rgb)))


def cvd_report(c1, c2):
    l1, l2 = srgb_to_lin(hex_rgb(c1)), srgb_to_lin(hex_rgb(c2))
    out = {k: de2000(lin_to_lab(M @ l1), lin_to_lab(M @ l2)) for k, M in MACHADO.items()}
    y1, y2 = rel_lum(hex_rgb(c1)), rel_lum(hex_rgb(c2))
    out['grey contrast'] = (max(y1, y2) + 0.05) / (min(y1, y2) + 0.05)
    return out


@rule('V09', 'DX-V4, DX-X3', 'main colour of each character = most frequent fill/stroke of objects with char "1966" / "mirror" seen by the page sampler; simulated with Machado 2009 '
      '(severity 1) protanopia and deuteranopia, ΔE2000 between the two simulated colours; grey = WCAG relative-luminance contrast between them',
      'ΔE2000 ≥ 20 under each simulation; grey contrast ≥ 1.5:1')
def v09_cvd(ctx):
    ch = ctx.json('out/checks/page.json').get('characters', {})
    if '1966' not in ch or 'mirror' not in ch:
        return verdict('V09', [metric('both characters seen on screen', False, '==', True)])
    c1, c2 = ch['1966']['mainColour'], ch['mirror']['mainColour']
    r = cvd_report(c1, c2)
    return verdict('V09', [metric('ΔE2000 protanopia', r['protanopia'], '>=', 20.0), metric('ΔE2000 deuteranopia', r['deuteranopia'], '>=', 20.0),
                           metric('grey contrast', r['grey contrast'], '>=', 1.5)], details=[{'1966': c1, 'mirror': c2}])


# ---- transitions ------------------------------------------------------------------------------------
def dissolve_at(frames):
    """frames: list of luma arrays around a cut (float). A dissolve: ≥ 4 consecutive inner frames that fit F ≈ αA + (1−α)B
    (A first, B last frame) with α strictly inside (0.1, 0.9), monotone, and residual RMS ≤ 3 codes, where A and B differ (mean |A−B| ≥ 8)."""
    A, B = frames[0], frames[-1]
    D = A - B
    if np.mean(np.abs(D)) < 8:
        return False, []
    als = []
    for F in frames[1:-1]:
        al = float(np.sum((F - B) * D) / np.sum(D * D))
        res = float(np.sqrt(np.mean((F - (al * A + (1 - al) * B)) ** 2)))
        als.append((al, res))
    run, best = [], []
    for al, res in als:
        if 0.1 < al < 0.9 and res <= 3 and (not run or al <= run[-1] + 0.02):
            run.append(al)
            best = max(best, run, key=len)
        else:
            run = [al] if 0.1 < al < 0.9 and res <= 3 else []
    return len(best) >= 4, als


def salient_centroid(y):
    m = y > (np.median(y) + 2 * y.std())
    if m.sum() < 20:
        return None
    ys, xs = np.nonzero(m)
    return xs.mean() / y.shape[1], ys.mean() / y.shape[0]


@rule('V10', 'DX-V10', 'out/transitions.json cuts[] (t, from, to, type, match: geometric|semantic, audio: j|l, reason). Match cut, geometric: centroid of the bright salient region '
      '(Y > median + 2σ) of the last outgoing and first incoming frame within 10% of the frame; semantic: reason ≥ 5 words. J-cut: first own-ASR word of the incoming scene\'s first sentence '
      'starts ≥ 0.2 s before the cut; L-cut: last ASR word of the outgoing scene\'s last sentence ends ≥ 0.2 s after it. Dissolve detector on every cut ±15 frames (see dissolve_at)',
      '≥ 5 verified match cuts; ≥ 4 verified J/L-cuts; every declared dissolve has a reason ≥ 5 words and not "default"; 0 undeclared dissolves detected')
def v10_transitions(ctx):
    cuts = ctx.json('out/transitions.json')['cuts']
    sents = ctx.sentences()
    asr = asr_master(ctx)
    want = sorted({round((c['t'] + k / FPS) * FPS) / FPS for c in cuts for k in range(-16, 16)})
    fr = {round(t * FPS): y.astype(np.float32) for t, y in video_frames(ctx.video(), times=want, scale=4)}
    match_ok, jl_ok, undeclared, bad_diss = [], [], [], []
    for c in cuts:
        f = round(c['t'] * FPS)
        if c.get('match') == 'geometric' and f - 1 in fr and f in fr:
            a, b = salient_centroid(fr[f - 1]), salient_centroid(fr[f])
            if a and b and np.hypot(a[0] - b[0], a[1] - b[1]) <= 0.1:
                match_ok.append(c['t'])
        elif c.get('match') == 'semantic' and len(words(str(c.get('reason', '')))) >= 5:
            match_ok.append(c['t'])
        if c.get('audio') in ('j', 'l'):
            if c['audio'] == 'j':
                s = next((s for s in sents if s['scene'] == c.get('to')), None)
                ws = [w for w in asr if s and s['start'] - 1.5 <= w['start'] <= s['end']] if s else []
                if ws and ws[0]['start'] <= c['t'] - 0.2:
                    jl_ok.append(c['t'])
            else:
                s = next((s for s in reversed(sents) if s['scene'] == c.get('from')), None)
                ws = [w for w in asr if s and s['start'] <= w['start'] <= s['end'] + 1.5] if s else []
                if ws and ws[-1]['end'] >= c['t'] + 0.2:
                    jl_ok.append(c['t'])
        seq = [fr.get(i) for i in range(f - 15, f + 16)]
        if all(x is not None for x in seq):
            is_d, _ = dissolve_at(seq)
            if c.get('type') == 'dissolve':
                if len(words(str(c.get('reason', '')))) < 5 or 'default' in str(c.get('reason', '')).lower():
                    bad_diss.append(c['t'])
            elif is_d:
                undeclared.append(c['t'])
    return verdict('V10', [metric('verified match cuts', len(match_ok), '>=', 5), metric('verified J/L cuts', len(jl_ok), '>=', 4),
                           metric('dissolves without reason', len(bad_diss), '<=', 0), metric('undeclared dissolves', len(undeclared), '<=', 0)],
                   details=[{'declaredMatch': sum(1 for c in cuts if c.get('match')), 'declaredJL': sum(1 for c in cuts if c.get('audio') in ('j', 'l')), 'undeclared': undeclared[:10]}])


@rule('C11', 'DX-V11 (C rule layout-repeat)', 'scenes[].layout of out/timeline.json; for each scene start, scenes with the same layout starting within the next 90 s',
      'no layout used more than 2 times in any 90 s window')
def c11_layout_repeat(ctx):
    sc = ctx.scenes()
    rep = []
    for s in sc:
        w = [x['id'] for x in sc if x.get('layout') == s.get('layout') and s['start'] <= x['start'] < s['start'] + 90]
        if len(w) > 2:
            rep.append((s.get('layout'), w))
    return verdict('C11', [metric('layout repeats >2 in 90 s', len(rep), '<=', 0)], details=rep[:10])


FAST = 0.10  # fw/s, as checks/page/sampler.js: at or above this camera speed the frame is "in a move" and layout rules judge the move's settled ends
MOVE_MAX_S = 3.0
MOVE_SHARE_MAX = 15.0


def fast_moves(ctx):
    """Runs of frames in a move: measured from out/camera.json (speed ≥ FAST, gaps < 0.2 s merged) or, without it, the declared scenes[].move."""
    if ctx.has('out/camera.json'):
        t, sp, *_ = camera_speed(ctx)
        runs = camera_moves(t, sp, thr=FAST, gap=0.2, min_dur=0.0)
        return [(float(t[a]), float(t[b - 1]) + 1 / FPS) for a, b in runs], 'camera.json'
    return [(s['start'], s['start'] + s['move']) for s in ctx.scenes() if s.get('move')], 'declared scenes[].move'


@rule('V13', 'DX-V9, DX-V8 (replaces the camera-move exemption)', 'frames "in a move" = camera speed ≥ 0.10 fw/s from out/camera.json (same speed as V05; gaps < 0.2 s merged), '
      'or the declared scenes[].move when there is no camera file. The layout rules (C01, C03, C04, C07, V02, C12) judge a move by its settled ends; this rule bounds the frames '
      'they do not judge. The text rules have no exemption: V12 (text integrity) on every frame, V03/V08/V11/C14 with their moving-text criteria in the page sampler',
      'every move ≤ 3.0 s; frames in a move ≤ 15% of the video')
def v13_moves(ctx):
    runs, src = fast_moves(ctx)
    total = ctx.total()
    long_ = [(round(a, 2), round(b - a, 2)) for a, b in runs if b - a > MOVE_MAX_S]
    share = 100 * sum(b - a for a, b in runs) / total if total else None
    return verdict('V13', [metric('moves longer than 3.0 s', len(long_), '<=', 0), metric('frames in a move (%)', share, '<=', MOVE_SHARE_MAX, '%')],
                   details=[{'source': src, 'moves': len(runs), 'longest': max((round(b - a, 2) for a, b in runs), default=0), 'tooLong': long_[:10]}])


# ---- thumbnails ---------------------------------------------------------------------------------------
def read_png(path):
    pr = json.loads(subprocess.run(['ffprobe', '-v', 'error', '-of', 'json', '-show_streams', path], capture_output=True, text=True, check=True).stdout)['streams'][0]
    w, h = pr['width'], pr['height']
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(h, w, 3)


def token_share(img, tokens, tol=12):
    """Share of pixels within `tol` (RGB Euclidean) of a token or of the straight blend between two tokens (anti-aliasing)."""
    px = img.reshape(-1, 3).astype(np.float32)[::7]
    T = np.array([hex_rgb(t) for t in tokens], np.float32)
    best = np.full(len(px), 1e9, np.float32)
    for i in range(len(T)):
        for j in range(i, len(T)):
            a, b = T[i], T[j]
            d = b - a
            L = float(d @ d)
            u = np.clip(((px - a) @ d) / L, 0, 1) if L > 0 else np.zeros(len(px))
            best = np.minimum(best, np.linalg.norm(px - (a + u[:, None] * d), axis=1))
    return float(np.mean(best <= tol))


@rule('P01', 'DX-P2', 'out/package/thumb-1..3.png with sidecars thumb-N.json texts[] (text, box [x,y,w,h], fontPx); design/tokens.json colours. Token share = pixels within 12 (RGB) of a token '
      'or of a blend of two tokens. Readability at 10%: area-downscale to 128×72; in each text box, WCAG contrast between the 95th and 5th luminance percentile',
      '3 thumbnails, each 1280×720; token share ≥ 97%; every text fontPx ≥ 90 (≥ 9 px at 10%) and contrast at 10% ≥ 3:1')
def p01_thumbs(ctx):
    tokens = list(ctx.json('design/tokens.json')['colors'].values())
    ms, det = [], []
    for n in (1, 2, 3):
        p = ctx.need(f'out/package/thumb-{n}.png')
        meta = ctx.json(f'out/package/thumb-{n}.json')
        img = read_png(p)
        h, w = img.shape[:2]
        ms.append(metric(f'thumb {n} size', f'{w}x{h}', '==', '1280x720'))
        ms.append(metric(f'thumb {n} token share (%)', 100 * token_share(img, tokens), '>=', 97.0, '%'))
        small = img[: h - h % 10, : w - w % 10].reshape(h // 10, 10, w // 10, 10, 3).mean(axis=(1, 3))
        lum = np.apply_along_axis(lambda c: rel_lum(c), 2, small)
        worst = None
        for tx in meta.get('texts', []):
            x, y, bw, bh = [int(v / 10) for v in tx['box']]
            reg = lum[y:y + max(1, bh), x:x + max(1, bw)]
            if reg.size == 0:
                continue
            c = (np.percentile(reg, 95) + 0.05) / (np.percentile(reg, 5) + 0.05)
            worst = c if worst is None else min(worst, c)
            if tx.get('fontPx', 0) < 90:
                det.append((n, tx.get('text'), 'fontPx < 90'))
        ms.append(metric(f'thumb {n} min contrast at 10%', worst, '>=', 3.0))
    ms.append(metric('thumb texts below 90 px', len(det), '<=', 0))
    return verdict('P01', ms, details=det[:10])
