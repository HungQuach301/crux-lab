"""Shorts 9:16 (K3.8, checks-appeal A5; D-006 Q3: 2–3 Shorts per episode from Episode 4; K4.4, chủ dự án 13/10: ONE Short per episode from Episode 8, SH07). contract.json `shorts`: [{file}] (paths from the episode root).
A contract written before D-006 (no `format`) and without `shorts` has no Shorts to check (Episodes 1–3): the rules pass with a note. A D-006 contract
(with `format`) without `shorts` = MISSING.
Text size, the player-UI zones and the on-frame labels (ILLUSTRATIVE, "history, not a forecast") need the vertical page's objects (window.CHECKS): they
wait for the factory page to expose them (checks-appeal A8); the rules below measure the delivered file and what the viewer hears."""
import os
import re

from common import ONE_SHORT_FROM, Missing, ebur128, ffprobe, metric, rule, verdict

SH_MAX_S = 180.0   # YouTube accepts square or vertical uploads up to 3 minutes as Shorts (since 2024-10-15); the brief's 60 s is reported, not enforced


def shorts(ctx):
    c = ctx.contract()
    sh = c.get('shorts')
    if sh is None:
        if c.get('format') is None:
            return None
        raise Missing('contract.json: shorts (' + ('1 Short per episode from Episode 8, chủ dự án 13/10' if (ctx.episode_no() or 0) >= ONE_SHORT_FROM
                                                  else 'D-006: 2–3 Shorts per episode') + ')')
    if not isinstance(sh, list) or not sh:
        raise Missing('contract.json: shorts = [{file}]')
    return [ctx.need(x['file'] if isinstance(x, dict) else x) for x in sh]


def _none(rid):
    return verdict(rid, [metric('Shorts checked', 0, '>=', 0)], note='contract before D-006 (no format) and no shorts: nothing to check')


@rule('SH01', 'D-006 Q3, checks-appeal A5', 'every Short of contract.json shorts: ffprobe video stream width × height, codec; an audio stream',
      '1080 × 1920, H.264, one audio stream (AAC)')
def sh01_frame(ctx):
    fs = shorts(ctx)
    if fs is None:
        return _none('SH01')
    bad = []
    for f in fs:
        st = ffprobe(f, '-show_streams')['streams']
        v = next((x for x in st if x['codec_type'] == 'video'), {})
        a = [x for x in st if x['codec_type'] == 'audio']
        if (v.get('width'), v.get('height'), v.get('codec_name')) != (1080, 1920, 'h264') or len(a) != 1 or a[0].get('codec_name') != 'aac':
            bad.append({'file': f.rsplit('/', 1)[-1], 'video': [v.get('width'), v.get('height'), v.get('codec_name')], 'audio': [x.get('codec_name') for x in a]})
    return verdict('SH01', [metric('Shorts not 1080×1920 H.264 + AAC', len(bad), '<=', 0)], details=[{'shorts': len(fs)}, *bad])


@rule('SH02', 'D-006 Q3, checks-appeal A5', 'every Short: container duration (ffprobe format.duration); the share over 60 s is reported',
      '≤ 180 s (YouTube Shorts limit)')
def sh02_length(ctx):
    fs = shorts(ctx)
    if fs is None:
        return _none('SH02')
    d = {f.rsplit('/', 1)[-1]: float(ffprobe(f, '-show_format')['format']['duration']) for f in fs}
    return verdict('SH02', [metric('longest Short s', max(d.values()), '<=', SH_MAX_S, 's')], details=[{'durations': d, 'over60': [k for k, v in d.items() if v > 60]}])


def _ebu_all(ctx, fs):
    return ctx.memo(('sh-ebu', tuple(fs)), lambda: {f.rsplit('/', 1)[-1]: ebur128(f) for f in fs})


@rule('SH03', 'DX-A10, checks-appeal A5', 'every Short: integrated loudness, ITU-R BS.1770-4 (ffmpeg ebur128)', '−14 LUFS ± 1 (−15 … −13) for every Short')
def sh03_lufs(ctx):
    fs = shorts(ctx)
    if fs is None:
        return _none('SH03')
    e = _ebu_all(ctx, fs)
    off = {k: v['I'] for k, v in e.items() if not -15.0 <= v['I'] <= -13.0}
    return verdict('SH03', [metric('Shorts outside −15 … −13 LUFS', len(off), '<=', 0)], details=[{k: v['I'] for k, v in e.items()}])


@rule('SH04', 'DX-A10, checks-appeal A5', 'every Short: true peak, 4× oversampled (ffmpeg ebur128 peak=true)', '≤ −1.0 dBTP for every Short')
def sh04_tp(ctx):
    fs = shorts(ctx)
    if fs is None:
        return _none('SH04')
    e = _ebu_all(ctx, fs)
    return verdict('SH04', [metric('highest true peak dBTP', max(v['TP'] for v in e.values()), '<=', -1.0, 'dBTP')], details=[{k: v['TP'] for k, v in e.items()}])


@rule('SH05', 'DX-I1, DX-I2 (CHARTER §4 protected genes), checks-appeal A5', 'every Short: own ASR of the whole audio (faster-whisper small.en, int8; a Short is '
      'short enough for one clip), split into sentences at . ! ?, against the locked S10 lists ADVICE, FORECAST, FOUR, WE_BAD',
      '0 matches in every Short')
def sh05_identity(ctx):
    from common import whisper
    from r_content import ADVICE, FORECAST, FOUR, WE_BAD
    fs = shorts(ctx)
    if fs is None:
        return _none('SH05')
    hits = []
    for f in fs:
        segs, _ = whisper().transcribe(f, beam_size=5, language='en', condition_on_previous_text=False)
        text = ' '.join(s.text.strip() for s in segs)
        for sent in re.split(r'(?<=[.!?])\s+', text):
            low = sent.lower().replace('’', "'")
            low_nf = re.sub(r"(not|n't|never|isn't|is not) a forecast", '', low)
            for k, pats in (('advice', ADVICE), ('forecast', FORECAST), ('four', FOUR), ('we', WE_BAD)):
                if any(re.search(p, low_nf if k == 'forecast' else low, re.M) for p in pats):
                    hits.append({'file': f.rsplit('/', 1)[-1], 'kind': k, 'sentence': sent[:90]})
                    break
    return verdict('SH05', [metric('advice / forecast / 4% / "we" sentences', len(hits), '<=', 0)], details=hits[:10])


# ---- SH06 (K4.2, checks-appeal A30): the Short's hook fits one line in the vertical safe area, measured on the spec before any render --------------
SH_FONT = os.path.join(os.path.dirname(__file__), '..', '..', 'toolkit', 'render', 'fonts', 'inter-latin-700-normal.woff2')   # Inter Bold, the factory's font
SH_SAFE = (72, 200, 1008, 1600)   # vertical safe area of the factory (toolkit/factory/qc.py SAFE['v'] = world/core.js VSAFE): x0, y0, x1, y1
SH_FLOOR, SH_HOOK_PX, SH_HOOK_Y = 56, 64, 270   # floor px of vertical text; the hook's size and baseline in the world Short renderer (core.js: VSAFE.y0 + 70)


def _hooks(ctx):
    """[(id, hook, px)] from contract.json shorts[].hook (with hookPx), else from the spec episode.yaml shorts[].hook (before any render)."""
    c = ctx.contract()
    rows = [x for x in (c.get('shorts') or []) if isinstance(x, dict) and x.get('hook')]
    if not rows and ctx.has('episode.yaml'):
        import yaml
        rows = [x for x in (yaml.safe_load(open(ctx.path('episode.yaml'))) or {}).get('shorts') or [] if isinstance(x, dict) and x.get('hook')]
    if not rows:
        if c.get('format') is None and c.get('shorts') is None:
            return None
        raise Missing('contract.json shorts[].hook or episode.yaml shorts[].hook (the hook line of every Short)')
    return [(str(x.get('id') or x.get('file') or i), str(x['hook']), float(x.get('hookPx') or SH_HOOK_PX)) for i, x in enumerate(rows)]


def hook_lines(text, px):
    """Lines of the hook as the factory wraps it (greedy by words in the safe width, core.js vt), widths in px (Inter Bold, tabular digits)."""
    from PIL import ImageFont
    f = ImageFont.truetype(SH_FONT, int(round(px)))
    w = lambda s: f.getlength(s, features=['tnum'])
    room = SH_SAFE[2] - SH_SAFE[0]
    lines, cur = [], ''
    for word in text.split():
        t = cur + ' ' + word if cur else word
        if cur and w(t) > room:
            lines.append(cur)
            cur = word
        else:
            cur = t
    lines.append(cur)
    return [(ln, w(ln)) for ln in lines]


@rule('SH06', 'D-006 Q3, lessons T6-10, checks-appeal A30', 'every Short\'s hook line (contract.json shorts[].hook, or the spec episode.yaml shorts[].hook before '
      'render) at its size (shorts[].hookPx, default 64 px = the world Short renderer; floor 56 px), Inter Bold (toolkit/render/fonts/inter-latin-700-normal.woff2, '
      'tabular digits), wrapped by words in the vertical safe width 936 px (x 72–1008) as the factory wraps it; the hook box with its last line on baseline '
      'y 270 (line height 1.2 × px, ascent 0.78 × px) must stay inside the vertical safe area (y ≥ 200)',
      'every hook: size ≥ 56 px, 1 line, the line ≤ 936 px wide, box top ≥ 200 px')
def sh06_hook(ctx):
    hs = _hooks(ctx)
    if hs is None:
        return _none('SH06')
    if not os.path.isfile(SH_FONT):
        raise Missing('toolkit/render/fonts/inter-latin-700-normal.woff2 (the font SH06 measures with)')
    rows, bad = [], []
    for sid, text, px in hs:
        ls = hook_lines(text, px)
        top = SH_HOOK_Y - (len(ls) - 1) * round(px * 1.2) - 0.78 * px
        r = {'short': sid, 'hook': text, 'px': px, 'lines': len(ls), 'widthPx': round(max(w for _, w in ls), 1), 'boxTop': round(top, 1)}
        rows.append(r)
        if px < SH_FLOOR or len(ls) > 1 or top < SH_SAFE[1]:
            bad.append(r)
    import hashlib
    return verdict('SH06', [metric('hooks', len(rows), '>=', 1), metric('hooks over one line, below 56 px or out of the safe area', len(bad), '<=', 0),
                            metric('widest hook px', max(r['widthPx'] for r in rows), '<=', SH_SAFE[2] - SH_SAFE[0], 'px')],
                   details=[{'font': hashlib.sha256(open(SH_FONT, 'rb').read()).hexdigest()[:16]}, *rows])


# ---- K4.4: number of Shorts per episode (chủ dự án 13/10/2026) --------------------------------------------------------------------------------------
@rule('SH07', 'chủ dự án 13/10/2026 (1 Short per episode from Episode 8; D-006 Q3 2–3 before)', 'contract.json shorts[] count; episode number from contract.json '
      'episode ("ep008" → 8). From Episode 8: exactly one Short. Episodes 4–7: 2–3 (D-006) reported, not enforced (the old rules had no count). '
      'A contract without format and without shorts (Episodes 1–3): nothing to check', 'from Episode 8: Shorts = 1')
def sh07_count(ctx):
    n = ctx.episode_no()
    sh = ctx.contract().get('shorts')
    if sh is None and ctx.contract().get('format') is None:
        return _none('SH07')
    if n is None or n < ONE_SHORT_FROM:
        k = len(sh) if isinstance(sh, list) else 0
        return verdict('SH07', [metric('Shorts', k, '>=', 0)], note=f'episode {n}: before Episode 8 the count (D-006 2–3) is reported only')
    if not isinstance(sh, list):
        raise Missing('contract.json: shorts (1 Short per episode from Episode 8, chủ dự án 13/10)')
    return verdict('SH07', [metric('Shorts', len(sh), '==', 1)], details=[{'shorts': [x.get('id') if isinstance(x, dict) else x for x in sh]}])
