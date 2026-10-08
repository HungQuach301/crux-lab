"""§0 and §6 — the delivered file, measured from out/video.mp4 itself (ffprobe + decoded packets/frames)."""
import re

import numpy as np

from common import FPS, Missing, metric, rule, verdict, ffprobe, run, video_frames


def _streams(ctx):
    return ctx.memo(('probe',), lambda: ffprobe(ctx.video(), '-show_streams', '-show_format', '-show_chapters'))


def _vs(ctx):
    return next(s for s in _streams(ctx)['streams'] if s['codec_type'] == 'video')


def _as(ctx):
    s = [s for s in _streams(ctx)['streams'] if s['codec_type'] == 'audio']
    if not s:
        raise Missing('audio stream in out/video.mp4')
    return s[0]


def _packets(ctx, sel):
    def get():
        out = run(['ffprobe', '-v', 'error', '-select_streams', sel, '-show_entries', 'packet=pts,dts,duration,size,flags', '-of', 'csv=p=0', ctx.video()]).stdout
        rows = [r.split(',') for r in out.strip().splitlines() if r]
        return rows
    return ctx.memo(('packets', sel), get)


@rule('F01', 'DX-F1, DX-F2', 'ffprobe of the video stream: codec, profile, pixel format, frame size, display aspect',
      'h264 / High / yuv420p / 1920×1080 / 16:9 (square pixels)')
def f01_video_format(ctx):
    v = _vs(ctx)
    sar = v.get('sample_aspect_ratio', '1:1')
    ms = [metric('codec', v['codec_name'], '==', 'h264'), metric('profile', v.get('profile'), '==', 'High'),
          metric('pix_fmt', v['pix_fmt'], '==', 'yuv420p'), metric('size', f"{v['width']}x{v['height']}", '==', '1920x1080'),
          metric('square pixels', sar in ('1:1', 'N/A', '0:1'), '==', True)]
    return verdict('F01', ms)


@rule('F02', 'DX-F1', 'r_frame_rate and avg_frame_rate from the stream header, and every packet duration (PTS step) in stream time base',
      'both rates exactly 30/1 and every PTS step = 1/30 s (constant frame rate)')
def f02_cfr(ctx):
    v = _vs(ctx)
    tb = [int(x) for x in v['time_base'].split('/')]
    pts = sorted(int(r[0]) for r in _packets(ctx, 'v:0') if r[0] not in ('N/A', ''))
    d = np.diff(pts)
    step = tb[1] / tb[0] / FPS
    bad = int(np.sum(np.abs(d - step) > 0.5))
    ms = [metric('r_frame_rate', v['r_frame_rate'], '==', '30/1'), metric('avg_frame_rate', v['avg_frame_rate'], '==', '30/1'),
          metric('PTS steps != 1/30 s', bad, '<=', 0)]
    return verdict('F02', ms, details=[{'stepsSeen': {str(k): int(c) for k, c in zip(*np.unique(d, return_counts=True))}}])


@rule('F03', 'DX-F3', 'video packet PTS sorted: a repeated PTS is a duplicated frame, a step of k>1 frame periods is k-1 dropped frames; '
      'frame count compared with duration × 30', 'dropped = 0, duplicated = 0, first PTS = 0, |frames − duration×30| ≤ 1')
def f03_pts(ctx):
    v = _vs(ctx)
    tb = [int(x) for x in v['time_base'].split('/')]
    step = tb[1] / tb[0] / FPS
    pts = sorted(int(r[0]) for r in _packets(ctx, 'v:0') if r[0] not in ('N/A', ''))
    d = np.diff(pts)
    dup = int(np.sum(d == 0))
    dropped = int(np.sum(np.maximum(0, np.round(d / step) - 1)))
    dur = float(_streams(ctx)['format']['duration'])
    ms = [metric('dropped frames', dropped, '<=', 0), metric('duplicated frames', dup, '<=', 0),
          metric('first PTS', pts[0] if pts else None, '==', 0), metric('|frames - duration*30|', abs(len(pts) - dur * FPS), '<=', 1)]
    return verdict('F03', ms)


@rule('F04', 'DX-F2', 'video bitrate = sum of video packet sizes × 8 / stream duration (measured, not the header value)', '≥ 16 Mbps')
def f04_bitrate(ctx):
    pk = _packets(ctx, 'v:0')
    size = sum(int(r[3]) for r in pk)
    dur = len(pk) / FPS
    mbps = size * 8 / dur / 1e6
    return verdict('F04', [metric('video Mbps', mbps, '>=', 16.0, 'Mbps')])


@rule('F05', 'DX-F2', 'stream colour tags (color_primaries, color_transfer, color_space, color_range) + decoded luma codes of 1 frame/10 s: '
      'share of Y samples outside 16–235', 'all tags bt709, range tv (limited); Y outside 16–235 ≤ 0.1% of samples')
def f05_bt709(ctx):
    v = _vs(ctx)
    ms = [metric('color_primaries', v.get('color_primaries'), '==', 'bt709'), metric('color_transfer', v.get('color_transfer'), '==', 'bt709'),
          metric('color_space', v.get('color_space'), '==', 'bt709'), metric('color_range', v.get('color_range'), '==', 'tv')]
    n = out = 0
    for _, y in video_frames(ctx.video(), every=FPS * 10):
        n += y.size
        out += int(np.sum((y < 16) | (y > 235)))
    ms.append(metric('Y outside 16-235 (%)', 100 * out / max(1, n), '<=', 0.1, '%'))
    return verdict('F05', ms)


@rule('F06', 'DX-F4', 'ffprobe of the audio stream; bitrate = audio packet bytes × 8 / duration', 'AAC (LC), 48 kHz, 2 channels, measured ≥ 272 kbps (= 85% of the 320 kbps nominal: ffmpeg\'s native AAC at -b:a 320k measured 276 kbps on test C\'s master, so the measure allows its ABR undershoot but not a 256k or lower setting)')
def f06_audio_format(ctx):
    a = _as(ctx)
    pk = _packets(ctx, 'a:0')
    size = sum(int(r[3]) for r in pk)
    dur = float(a.get('duration') or _streams(ctx)['format']['duration'])
    kbps = size * 8 / dur / 1000
    ms = [metric('codec', a['codec_name'], '==', 'aac'), metric('sample_rate', int(a['sample_rate']), '==', 48000),
          metric('channels', int(a['channels']), '==', 2), metric('audio kbps', kbps, '>=', 272.0, 'kbps')]
    return verdict('F06', ms)


@rule('F07', 'DX-S1 (CH §1 length)', 'container duration (ffprobe format.duration); K3: the range of CHARTER §1 (8–15 minutes)', '480 … 900 s (8:00–15:00)')
def f07_duration(ctx):
    dur = float(_streams(ctx)['format']['duration'])
    return verdict('F07', [metric('duration s', dur, 'in', [480.0, 900.0], 's')])


# ---- banding ------------------------------------------------------------------------------------
def banding_score(y, dark_max=80, min_run=12, win=240, blk=16):
    """Banding on dark gradients in one luma plane (uint8 codes).

    Dark gradient area: 240×240 tiles whose mean Y ≤ dark_max (≈ 25% brightness in limited range) and whose 16×16-block
    means fit a plane with residual RMS ≤ 1 code while the plane spans 2–40 codes (a smooth gradient: not flat fill, not an edge or pattern).
    In those tiles a band edge is the end of a run of ≥ min_run identical codes along a row or column that steps by exactly
    1–2 codes. Score = share of dark-gradient pixels lying in such runs. Grain or dither breaks the runs; a quantised
    gradient leaves wide flat steps."""
    h, w = y.shape
    yf = y.astype(np.int16)
    band_px = area = 0
    for ty in range(0, h - win + 1, win):
        for tx in range(0, w - win + 1, win):
            t = yf[ty:ty + win, tx:tx + win]
            if t.mean() > dark_max:
                continue
            s = t.reshape(win // blk, blk, win // blk, blk).mean(axis=(1, 3))
            # a smooth gradient: block means fit a plane closely and the plane spans ≥ 2 codes
            gy, gx = np.mgrid[: s.shape[0], : s.shape[1]]
            A = np.stack([gx.ravel(), gy.ravel(), np.ones(gx.size)], 1)
            coef, *_ = np.linalg.lstsq(A, s.ravel(), rcond=None)
            fit = A @ coef
            span = fit.max() - fit.min()
            if span < 2 or span > 40 or np.sqrt(np.mean((s.ravel() - fit) ** 2)) > 1.0:
                continue
            area += t.size
            for arr in (t, t.T):
                d = np.diff(arr, axis=1)
                nzr, nzc = np.nonzero(d)
                for r in range(arr.shape[0]):
                    cols = nzc[nzr == r]
                    edges = np.concatenate(([-1], cols))
                    L = np.diff(edges)  # run length ending at each change
                    step = np.abs(d[r, cols])
                    good = (L >= min_run) & (step >= 1) & (step <= 2)
                    band_px += L[good].sum() / 2  # counted in both directions
    return (band_px / area if area else 0.0), area


@rule('F08', 'DX-V5', 'decoded luma of 1 frame/2 s; banding score per frame (banding_score: 240 px tiles, mean Y ≤ 80, 16-px block means fitting a plane that spans 2–40 codes with residual ≤ 1 code; share of their pixels in flat runs ≥ 12 px ending in a 1–2 code step)',
      'worst frame ≤ 5% (frames with < 1% dark-gradient area are skipped)')
def f08_banding(ctx):
    worst, worst_t, n = 0.0, None, 0
    per = []
    for t, y in video_frames(ctx.video(), every=FPS * 2):
        sc, area = banding_score(y)
        if area < 0.01 * y.size:
            continue
        n += 1
        per.append((round(t, 1), round(sc * 100, 2)))
        if sc > worst:
            worst, worst_t = sc, t
    per.sort(key=lambda x: -x[1])
    return verdict('F08', [metric('worst banding (%)', worst * 100, '<=', 5.0, '%')], details=[{'framesJudged': n, 'worst': per[:5]}])


# ---- subtitles ----------------------------------------------------------------------------------
def parse_srt(text):
    blocks = re.split(r'\n\s*\n', text.strip().replace('\r', ''))
    out = []
    tt = lambda s: sum(float(x) * m for x, m in zip(s.replace(',', '.').split(':'), (3600, 60, 1)))
    for b in blocks:
        ls = b.strip().split('\n')
        if len(ls) < 2:
            continue
        m = re.match(r'(\S+)\s*-->\s*(\S+)', ls[1])
        if not m:
            continue
        out.append({'start': tt(m.group(1)), 'end': tt(m.group(2)), 'lines': ls[2:]})
    return out


def norm_words(s):
    return re.sub(r'\s+', ' ', s.replace('’', "'").replace('—', '-').strip())


@rule('F09', 'DX-F5', 'out/captions.srt parsed; joined subtitle text vs joined narration text of out/script.json (whitespace-normalised, exact characters otherwise); '
      'per cue: characters per line, lines, duration; cues must not overlap',
      'text identical (100%); every line ≤ 42 chars; ≤ 2 lines; 1.0 ≤ duration ≤ 7.0 s; 0 overlaps')
def f09_srt(ctx):
    cues = parse_srt(ctx.text('out/captions.srt'))
    script = norm_words(' '.join(s['text'] for s in ctx.sentences()))
    subs = norm_words(' '.join(' '.join(c['lines']) for c in cues))
    long_lines = [l for c in cues for l in c['lines'] if len(l) > 42]
    many = [c for c in cues if len(c['lines']) > 2]
    bad_dur = [(round(c['start'], 2), round(c['end'] - c['start'], 2)) for c in cues if not (1.0 - 1e-6 <= c['end'] - c['start'] <= 7.0 + 1e-6)]
    overl = [round(b['start'], 2) for a, b in zip(cues, cues[1:]) if b['start'] < a['end'] - 1e-6]
    # first difference, for the report
    diff = None
    if subs != script:
        i = next((k for k in range(min(len(subs), len(script))) if subs[k] != script[k]), min(len(subs), len(script)))
        diff = {'at': i, 'subs': subs[max(0, i - 30): i + 30], 'script': script[max(0, i - 30): i + 30]}
    ms = [metric('text identical to script', subs == script, '==', True), metric('lines > 42 chars', len(long_lines), '<=', 0),
          metric('cues > 2 lines', len(many), '<=', 0), metric('cues outside 1-7 s', len(bad_dur), '<=', 0), metric('overlapping cues', len(overl), '<=', 0)]
    return verdict('F09', ms, details=[{'firstDiff': diff, 'longLines': long_lines[:5], 'badDurations': bad_dur[:8], 'overlaps': overl[:5], 'cues': len(cues)}])


def parse_chapters_desc(text):
    out = []
    for m in re.finditer(r'^\s*(?:(\d+):)?(\d{1,2}):(\d{2})\s+(.+)$', text, re.M):
        h, mi, s, title = m.groups()
        out.append({'start': int(h or 0) * 3600 + int(mi) * 60 + int(s), 'title': title.strip()})
    return out


@rule('F10', 'DX-F6', 'chapters from out/package/description.md (lines "m:ss Title") and, if present, the MP4 chapter atoms; '
      'chapter length = next start − start (last: to end of video)', '≥ 3 chapters; first at 0:00; each ≥ 10 s; MP4 chapters (if any) equal the description\'s')
def f10_chapters(ctx):
    ch = parse_chapters_desc(ctx.text('out/package/description.md'))
    dur = float(_streams(ctx)['format']['duration'])
    lens = [b['start'] - a['start'] for a, b in zip(ch, ch[1:])] + ([dur - ch[-1]['start']] if ch else [])
    mp4 = [{'start': round(float(c['start_time'])), 'title': c.get('tags', {}).get('title')} for c in _streams(ctx).get('chapters', [])]
    same = (not mp4) or [c['start'] for c in mp4] == [c['start'] for c in ch]
    ms = [metric('chapters', len(ch), '>=', 3), metric('first chapter start s', ch[0]['start'] if ch else None, '==', 0),
          metric('shortest chapter s', min(lens) if lens else 0, '>=', 10.0, 's'), metric('mp4 chapters agree', same, '==', True)]
    return verdict('F10', ms, details=[{'chapters': ch, 'mp4': mp4}])


RELEASE_FILES = ['out/video.mp4', 'out/captions.srt', 'out/package/description.md', 'out/timeline.json', 'out/script.json', 'out/claims.json',
                 'out/audio/stems/voice.*', 'out/audio/stems/music.*', 'out/audio/stems/sfx.*', 'out/audio/stems/whoosh.*', 'out/audio/stems/room.*',
                 'out/audio/stems/sonify.*', 'out/voice/takes.json', 'out/camera.json', 'out/sfx-events.json', 'out/sonify-events.json', 'out/tempo-map.json',
                 'out/transitions.json', 'out/cues.json', 'out/tension-map.json', 'out/tension-map.png', 'out/adbreaks.json', 'preprod/shotlist.json',
                 'design/tokens.json', 'out/package/thumb-1.png', 'out/package/thumb-2.png', 'out/package/thumb-3.png', 'out/page.json']


# K4.1 (checks-appeal A10, A16): an episode built by the factory (out/factory/build-report.json) is judged on what the factory makes, not on the old
# pipeline's list: the core release files, the stems its mix wrote, the artefacts of its `artefacts` step and, per world segment it spliced, the
# segment video and the products of build_seg.py (<video>.build.json, <video>.verify.json, <video minus .mp4>.log.json).
FACTORY_CORE = ['out/video.mp4', 'out/captions.srt', 'out/package/description.md', 'out/package/thumb-1.png', 'out/package/thumb-2.png',
                'out/package/thumb-3.png', 'out/timeline.json', 'out/script.json', 'out/claims.json', 'out/voice/takes.json', 'out/adbreaks.json',
                'out/rights.json', 'out/visual-assets.json', 'out/audio/stems/voice.*', 'out/audio/stems/music.*']


def factory_release(ctx):
    """The release list of a factory build, from out/factory/build-report.json (+ out/factory/splice.json for world segments)."""
    br = ctx.json('out/factory/build-report.json')
    st = br.get('steps') or {}
    req = list(FACTORY_CORE)
    for seg in ((st.get('mix') or {}).get('world') or {}).get('segments') or []:
        req += [f'out/audio/stems/{k}.*' for k in (seg.get('layers_rms_dbfs') or {})]
    a = st.get('artefacts') or {}
    if a.get('camera'):
        req.append('out/camera.json')
    if a.get('sonify'):
        req.append('out/sonify-events.json')
    if a.get('page'):
        req.append('out/page.json')
    if 'world' in st:
        for seg in ctx.json('out/factory/splice.json')['segments'] if ctx.has('out/factory/splice.json') else []:
            v = seg['video']
            req += [v, v + '.build.json', v + '.verify.json', v[:-4] + '.log.json']
    seen = []
    for r in req:
        if r not in seen:
            seen.append(r)
    return seen


def factory_built(ctx):
    """The factory built THIS film: its build report exists and the total it resolved equals out/timeline.json total (±0.5 s; an excerpt it built does not count)."""
    if not ctx.has('out/factory/build-report.json') or not ctx.has('out/timeline.json'):
        return False
    tot = ((ctx.json('out/factory/build-report.json').get('steps') or {}).get('resolve') or {}).get('total')
    return tot is not None and abs(float(tot) - ctx.total()) <= 0.5


def _repo_path(ctx, rel):
    """A factory path: relative to the episode root, or (only when it starts with episodes/) to the repository that holds the episode — the parent
    folder that contains episodes/<this root's name>. Absolute paths are refused (they would match anywhere)."""
    import glob
    import os
    if os.path.isabs(rel):
        return False
    if glob.glob(os.path.join(ctx.root, rel)):
        return True
    if not rel.startswith('episodes/'):
        return False
    d = os.path.dirname(ctx.root)
    while True:
        if os.path.isdir(os.path.join(d, 'episodes')) and os.path.basename(ctx.root) in os.listdir(os.path.join(d, 'episodes')):
            return bool(glob.glob(os.path.join(d, rel)))
        up = os.path.dirname(d)
        if up == d:
            return False
        d = up


@rule('F11', 'CH §4 khâu 3 (hợp đồng tập, K2; K4.1: danh sách của nhà máy, checks-appeal A10, A16)', 'factory build (out/factory/build-report.json present and its resolved total = out/timeline.json total ±0.5 s; an excerpt does not count): the release list '
      'is factory_release — FACTORY_CORE, every stem the mix wrote (steps.mix.world.segments[].layers_rms_dbfs), out/camera.json / out/sonify-events.json / out/page.json '
      'when the artefacts step made them, and per spliced world segment (out/factory/splice.json) its video and build_seg products (.build.json, .verify.json, .log.json); '
      'each must match ≥ 1 file (globs; a factory path may be relative to the repository); contract.json artefacts.M3 is reported, not required. Other builds (K2): '
      'artefacts.M3 of the episode contract, each matching ≥ 1 file under the root, and it must include every release file of checks/CONTRACT.md (RELEASE_FILES); '
      'contract without artefacts.M3 = MISSING',
      'factory: every factory release file delivered; else every declared M3 artefact delivered and every checks/CONTRACT.md release file declared')
def f11_artefacts(ctx):
    import fnmatch
    import glob
    if factory_built(ctx):
        req = factory_release(ctx)
        absent = [p for p in req if not _repo_path(ctx, p)]
        decl = (ctx.contract().get('artefacts') or {}).get('M3') or []
        return verdict('F11', [metric('factory release files', len(req), '>=', 1), metric('factory release files not delivered', len(absent), '<=', 0)],
                       details=[{'source': 'factory', 'notDelivered': absent[:40], 'required': req,
                                 'declaredNotMadeByFactory': [d for d in decl if not any(fnmatch.fnmatch(r, d) or fnmatch.fnmatch(d, r) for r in req)]}])
    decl = ctx.cfield('artefacts', 'M3', kind=list)
    absent = [p for p in decl if not glob.glob(ctx.path(p))]
    undeclared = [r for r in RELEASE_FILES if not any(fnmatch.fnmatch(r, d) or fnmatch.fnmatch(d, r) for d in decl)]
    return verdict('F11', [metric('declared M3 artefacts', len(decl), '>=', 1), metric('declared artefacts not delivered', len(absent), '<=', 0),
                           metric('release files not declared', len(undeclared), '<=', 0)], details=[{'source': 'K2', 'notDelivered': absent[:30], 'notDeclared': undeclared}])


STEMS = ['voice', 'music', 'sfx', 'whoosh', 'room', 'sonify']


def _in_repo(ctx, rel):
    """A path relative to the root or to one of its parent folders (the repository holds the toolkit that generated an asset)."""
    import os
    d = ctx.root
    while True:
        if os.path.exists(os.path.join(d, rel)):
            return True
        up = os.path.dirname(d)
        if up == d:
            return False
        d = up


VISUAL_KINDS = ('image', 'document', 'font', 'model3d', 'texture', 'quote-card')
# K3.1: what a loaded page resource is, by URL extension (content type and Playwright resource type as a fallback)
RES_EXT = {'image': {'png', 'jpg', 'jpeg', 'gif', 'webp', 'avif', 'svg', 'bmp', 'ico', 'tif', 'tiff', 'apng', 'jxl'}, 'document': {'pdf'},
           'model3d': {'glb', 'gltf', 'obj', 'fbx', 'stl', 'ply', 'usdz', 'dae', '3ds'}, 'texture': {'ktx', 'ktx2', 'basis', 'dds', 'hdr', 'exr', 'tga'}}
FONT_EXT = {'woff', 'woff2', 'ttf', 'otf', 'eot'}
INTERNAL_SCHEMES = ('data', 'blob', 'about', 'chrome', 'chrome-extension', 'chrome-error', 'chrome-search', 'devtools', 'javascript')


def _declared(ctx):
    """Declared visual assets and generated-file rules: contract.json rights.visual[] / rights.generated[] and/or the builder's manifest
    out/visual-assets.json {assets:[…], generated:[{glob, generator}]} (assets: union by name). No visual list anywhere = MISSING:
    the checker never infers the build's pictures from nothing."""
    items, gen, found = [], [], False
    try:
        c = ctx.contract()
    except Missing:
        c = {}
    r = c.get('rights') if isinstance(c.get('rights'), dict) else {}
    if isinstance(r.get('visual'), list):
        items += r['visual']
        found = True
    gen += [g for g in r.get('generated') or [] if isinstance(g, dict)]
    if ctx.has('out/visual-assets.json'):
        m = ctx.json('out/visual-assets.json')
        if isinstance(m.get('assets'), list):
            items += m['assets']
            found = True
        gen += [g for g in m.get('generated') or [] if isinstance(g, dict)]
    if not found:
        raise Missing('visual asset list (contract.json rights.visual or out/visual-assets.json)')
    seen = {}
    for v in items:
        if isinstance(v, dict) and v.get('name'):
            seen.setdefault(v['name'], v)
        else:
            seen.setdefault('?%d' % len(seen), {'name': None, 'kind': None})
    return list(seen.values()), gen


def _url(x):
    from urllib.parse import urlparse
    return urlparse(x or '').scheme in ('http', 'https')


def _loaded(ctx):
    """Resources the page really loaded while the sampler rendered it (out/checks/page.json resources, K3.1 sampler). Returns
    (visual resources [(location, kind)], font families loaded). Excluded as browser-internal: data:/blob:/about:/chrome*:/devtools: URLs,
    failed requests and HTTP ≥ 400, the browser's own /favicon.ico probe (type other). Fonts are judged by family (document.fonts, status
    loaded), whatever their source (a font file, a data: URL, a buffer); only @font-face / FontFace faces are listed, never system fonts."""
    import os
    from urllib.parse import urlparse, unquote
    pg = ctx.json('out/checks/page.json')
    res = pg.get('resources')
    if not isinstance(res, dict):
        raise Missing('out/checks/page.json resources (run the K3.1 page sampler)')
    root = os.path.realpath(ctx.root)
    out, seen = [], set()
    rows = [r for r in res.get('requests') or [] if not r.get('failed') and not (isinstance(r.get('status'), int) and r['status'] >= 400)]
    rows += [{'url': e.get('url'), 'type': e.get('initiator')} for e in res.get('entries') or []]
    for r in rows:
        u = urlparse(r.get('url') or '')
        if not u.scheme or u.scheme in INTERNAL_SCHEMES:
            continue
        p = unquote(u.path)
        if p.endswith('/favicon.ico') and r.get('type') == 'other':
            continue
        ext = p.rsplit('.', 1)[-1].lower() if '.' in os.path.basename(p) else ''
        ct = (r.get('contentType') or '').lower()
        if ext in FONT_EXT or r.get('type') == 'font' or ct.startswith('font/'):
            continue  # judged by family below
        kind = next((k for k, xs in RES_EXT.items() if ext in xs), None)
        if kind is None:
            kind = 'image' if ct.startswith('image/') or r.get('type') in ('image', 'img') else 'model3d' if ct.startswith('model/') else 'document' if ct == 'application/pdf' else None
        if kind is None:
            continue  # page code, styles, data: not a picture
        if u.scheme == 'file':
            rp = os.path.realpath(p)
            loc = os.path.relpath(rp, root) if rp.startswith(root + os.sep) else rp
        else:
            loc = u.scheme + '://' + u.netloc + p
        if loc not in seen:
            seen.add(loc)
            out.append((loc, kind))
    fams = sorted({(f.get('family') or '').strip().strip('"\'') for f in res.get('fonts') or [] if f.get('status') == 'loaded'} - {''})
    return out, fams


def _matches(loc, pattern):
    import fnmatch
    pattern = pattern[2:] if pattern.startswith('./') else pattern
    return loc == pattern or loc.endswith('/' + pattern) or fnmatch.fnmatch(loc, pattern) or fnmatch.fnmatch(loc, '*/' + pattern)


@rule('F12', 'DX-A3 (sổ giấy phép), CH §5 (K3: quyền tài sản; K3.1: tài sản hình)', 'rights ledger out/rights.json {assets:[{name, stems:[…], visuals:[…], kind, origin, licence, '
      'thirdParty, terms:{quote, url}, commercial, generator, publicDomain, pdBasis, source:{url}, quoteSource:{who, url}}]}. (1) Sound: every delivered stem '
      '(out/audio/stems/<name>.wav|flac of voice, music, sfx, whoosh, room, sonify) with sound (1 s RMS above −60 dBFS somewhere) must be covered by an asset '
      'listing it in stems. (2) Pictures (K3.1): the visual asset list = contract.json rights.visual[] ∪ out/visual-assets.json assets[] ({name, kind ∈ image, '
      'document, font, model3d, texture, quote-card, path|paths (root-relative path or glob of the loaded file), family (font)}); neither declared = MISSING. '
      'Every listed visual must be covered by an asset listing its name in visuals. (3) Loaded (K3.1): the page sampler records what the render page really '
      'loads (Playwright requests + Resource Timing; document.fonts). Every loaded picture file (image, pdf, 3D model, texture by extension or content type) '
      'must match a declared visual (path/paths glob, else file name = name), and every loaded font family (status loaded) must be a declared font (family or '
      'name, case-insensitive). Not counted: browser-internal URLs (data:, blob:, about:, chrome*:, devtools:), failed loads, the browser\'s /favicon.ico '
      'probe, page code/styles/data; files made by the project\'s own code = matching a generated rule {glob, generator} (contract rights.generated or '
      'manifest generated) whose generator path exists. No sampler resources = MISSING. '
      'Every asset: origin and licence non-empty, thirdParty a boolean. Public-domain asset (publicDomain = true, e.g. a US federal document): source.url http(s) '
      'and pdBasis ≥ 20 chars (the ground for public domain), no terms needed. Other third-party asset (TTS voice, library music or sound, photo, font, 3D model, '
      'texture, …): terms quote ≥ 20 chars and http(s) terms URL, commercial = true (the terms allow an ad-supported channel). An asset made by this project: '
      'generator = a path that exists under the root or one of its parent folders. A reconstructed quote card (kind or listed kind quote-card), whoever drew it: '
      'quoteSource.who non-empty and quoteSource.url http(s) (where the quoted words come from)',
      '0 sounding stems without a rights entry; visual list declared; 0 listed visuals without a rights entry; 0 visuals of an unknown kind; 0 loaded picture '
      'files or font families not declared; 0 generated rules without an existing generator; 0 assets with a missing field; 0 third-party assets without terms '
      '(or public-domain source and basis) or not cleared for commercial use; ≥ 1 asset')
def f12_rights(ctx):
    import r_audio
    from common import frame_rms_db
    assets = ctx.json('out/rights.json').get('assets') or []
    visuals, generated = _declared(ctx)
    loaded, families = _loaded(ctx)
    covered = {s for a in assets for s in (a.get('stems') or [])}
    vcovered = {s for a in assets for s in (a.get('visuals') or [])}
    uncovered, bad = [], []
    for name in STEMS:
        try:
            x = r_audio.stem_audio(ctx, name)
        except Missing:
            continue
        _, db = frame_rms_db(x, win=1.0)
        if len(db) and db.max() > -60 and name not in covered:
            uncovered.append(name)
    vkind = {v.get('name'): v.get('kind') for v in visuals}
    vbadkind = [v.get('name') or '?' for v in visuals if v.get('kind') not in VISUAL_KINDS]
    vuncovered = [v.get('name') or '?' for v in visuals if v.get('name') not in vcovered]
    # loaded but not declared
    gen_ok = [g for g in generated if g.get('glob') and g.get('generator') and _in_repo(ctx, g['generator'])]
    gen_bad = [g.get('glob') or '?' for g in generated if g not in gen_ok]
    undeclared = []
    for loc, kind in loaded:
        pats = [(v, p) for v in visuals if v.get('kind') != 'font' for p in ([v['path']] if isinstance(v.get('path'), str) else []) + [x for x in v.get('paths') or [] if isinstance(x, str)]]
        if any(_matches(loc, p) for _, p in pats) or any(v.get('name') == loc.rsplit('/', 1)[-1] for v in visuals if v.get('kind') != 'font'):
            continue
        if any(_matches(loc, g['glob']) for g in gen_ok):
            continue
        undeclared.append(f'{kind}: {loc}')
    fonts = {(v.get('family') or v.get('name') or '').strip().lower() for v in visuals if v.get('kind') == 'font'}
    undeclared += [f'font: {f}' for f in families if f.lower() not in fonts]
    for a in assets:
        nm = a.get('name') or '?'
        if not (a.get('origin') or '').strip() or not (a.get('licence') or '').strip() or not isinstance(a.get('thirdParty'), bool):
            bad.append((nm, 'origin, licence or thirdParty missing'))
            continue
        quote_card = a.get('kind') == 'quote-card' or any(vkind.get(v) == 'quote-card' for v in (a.get('visuals') or []))
        if quote_card:
            q = a.get('quoteSource') or {}
            if not (q.get('who') or '').strip() or not _url(q.get('url')):
                bad.append((nm, 'quote card without the origin of the quote (quoteSource.who/url)'))
        if a.get('publicDomain') is True:
            if not _url((a.get('source') or {}).get('url')) or len((a.get('pdBasis') or '').strip()) < 20:
                bad.append((nm, 'public domain without source url or basis (pdBasis)'))
        elif a['thirdParty']:
            t = a.get('terms') or {}
            if len(t.get('quote') or '') < 20 or not _url(t.get('url')):
                bad.append((nm, 'terms quote/url missing'))
            if a.get('commercial') is not True:
                bad.append((nm, 'not cleared for commercial use'))
        elif not a.get('generator') or not _in_repo(ctx, a['generator']):
            bad.append((nm, 'generator path missing'))
    return verdict('F12', [metric('assets', len(assets), '>=', 1), metric('sounding stems without a rights entry', len(uncovered), '<=', 0),
                           metric('listed visuals without a rights entry', len(vuncovered), '<=', 0),
                           metric('visuals of an unknown kind', len(vbadkind), '<=', 0),
                           metric('loaded picture files or fonts not declared', len(undeclared), '<=', 0),
                           metric('generated rules without an existing generator', len(gen_bad), '<=', 0),
                           metric('assets with a problem', len(bad), '<=', 0)],
                   details=[{'uncovered': uncovered}, {'visualsUncovered': vuncovered[:30]}, {'visualsBadKind': vbadkind[:30]},
                            {'loadedUndeclared': undeclared[:30]}, {'loaded': len(loaded), 'fontFamilies': families}, {'generatedBad': gen_bad[:30]},
                            {'problems': bad[:30]}])
