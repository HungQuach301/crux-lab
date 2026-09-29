"""Frame rules evaluated by the page sampler (checks/page/sampler.js) — here they get their verdicts from out/checks/page.json."""
from common import asr_join, Missing, canon_matches, metric, numbers_in_text, rule, spoken_numbers, verdict
from r_audio import asr_master


def pr(ctx, rid):
    p = ctx.json('out/checks/page.json')
    if rid not in p['rules']:
        raise Missing(f'page rule {rid} in out/checks/page.json')
    return p['rules'][rid]


def frames_rule(rid, section, measure):
    def fn(ctx):
        r = pr(ctx, rid)
        return verdict(rid, [metric('frames flagged', r['framesFlagged'], '<=', 0)], details=[{'scenes': r['scenes'][:10], 'examples': r['examples']}])
    fn.__name__ = 'page_' + rid
    return rule(rid, section, measure, '0 flagged frames')(fn)


frames_rule('C01', 'DX-V11 (C rule scene-leak)', 'every 0.1 s outside the camera move at scene start: shapes of a panel not listed in scenes[].panels, not background, opacity > 0.05, ≥ 16 px² on frame')
frames_rule('C02', 'DX-V11 (C rule bg-over-data)', 'every 0.1 s: a background object (role bg) painted after (above) the first data shape and overlapping a data shape')
frames_rule('C03', 'DX-V11 (C rule unlabelled-curve)', 'settled frames, every 0.1 s: a visible curve (≥ 80 px diagonal, opacity > 0.1) without its bound label within 240 px, or any text within 60 px if unbound')
frames_rule('C04', 'DX-V11 (C rule axis-anchors)', 'settled frames, every 0.1 s: a line series (role series, or an open stroke: unfilled path/polyline of ≥ 10 vertices stroked in a series colour; ≥ 120 px) without an axis of its chart and ≥ 2 numeric anchors. Filled shapes (pie wedges, closed polygons, marks) are not line series')
frames_rule('C05', 'DX-V11, DX-X4 (C rule grey-emphasis)', 'every 0.1 s: a level-1/emphasis text below 7:1 against the bg token in grey, or a 48 px+ non-emphasis text brighter in grey than it')
frames_rule('C06', 'DX-V11 (C rule number-colour)', 'every 0.1 s: a number in a series colour whose colour differs from its series (data-series map) or from the nearest mark within 150 px')
frames_rule('C07', 'DX-V11 (C rule bar-proportion)', 'settled frames: a bar cropped along its value axis without an axis break, or bars of one chart (data-value, full) with scales differing > 3%')
frames_rule('C15', 'DX-V5 (C rule tokens only)', 'every 0.1 s: a colour on a visible object (text runs, text background, shape fill/stroke; gradients excepted) that is not in design/tokens.json colors')


@rule('C10', 'DX-V1 (C rule level1)', 'chart scenes of ≥ 2 s: share of samples (0.1 s) with exactly one visible level-1 text; max simultaneous', '≥ 50% of samples with exactly one, never two')
def c10(ctx):
    r = pr(ctx, 'C10')
    return verdict('C10', [metric('scenes failing', len(r['failing']), '<=', 0)], details=r['failing'][:10])


@rule('C12', 'DX-V11 (C rule split-view)', 'camera frozen at t, page at t + 0.1 s; union box of changed objects (a growing object counts only its new strip); outside camera moves',
      'no run ≥ 1.0 s where the changes span > 60% of frame width or height')
def c12(ctx):
    r = pr(ctx, 'C12')
    return verdict('C12', [metric('split-view runs', len(r['violations']), '<=', 0)], details=r['violations'][:10])


@rule('C14', 'DX-V11, DX-X4 (legible at 25%)', 'every frame (no camera-move exemption), every 0.2 s, texts with opacity ≥ 0.95 standing still on screen (moving texts: V12): smallest font run in px; on the delivered video frame downscaled 4× (box average), '
      'WCAG contrast between the 95th and 5th luminance percentile inside the text box', 'every text ≥ 28 px (cap height ≥ 5 px at 25%) and ≥ 3:1 at 25%; 0 violations')
def c14(ctx):
    r = pr(ctx, 'C14')
    return verdict('C14', [metric('text samples not legible at 25%', r['violations'], '<=', 0)], details=r['examples'])


@rule('V02', 'DX-V1', 'settled frames every 0.1 s: centre of each visible level-1 text vs the four thirds intersections (±96 px x, ±54 px y), or the vertical centre line (±48 px) '
      'when the scene declares composition "center"', '≥ 90% of level-1 samples placed')
def v02(ctx):
    r = pr(ctx, 'V02')
    share = 100 * r['ok'] / r['samples'] if r['samples'] else None
    return verdict('V02', [metric('level-1 samples', r['samples'], '>=', 1), metric('level-1 placed (%)', share, '>=', 90.0, '%')], details=r['examples'])


@rule('V03', 'DX-V3', 'every frame (no camera-move exemption), every 0.2 s: ink bounding box of each visible text from the page\'s text layer (alpha > 64, badges included). '
      'A text travelling in or out of frame (its box moved ≥ 4 px since the object sample 0.1 s earlier) may cross the edge', 'all text ink of non-travelling texts inside x 96–1824, y 54–1026 (90% safe area); 0 violations')
def v03(ctx):
    r = pr(ctx, 'V03')
    return verdict('V03', [metric('text outside safe area', r['violations'], '<=', 0)], details=[{'travellingSamples': r.get('travellingSamples')}, *r['examples']])


def contract_characters(ctx):
    """contract.json characters: {key: {color, shape, side?, illustrative?}}; `color` = a token name of design/tokens.json (colors, series, seriesOf)
    or a #hex. Entries that are not objects (e.g. a "note") are ignored. A character without color or shape = MISSING."""
    chars = {k: v for k, v in ctx.cfield('characters', kind=dict).items() if isinstance(v, dict)}
    if not chars:
        raise Missing('contract.json: characters (no character declared)')
    tok = ctx.json('design/tokens.json') if ctx.has('design/tokens.json') else {}
    pal = {**(tok.get('seriesOf') or {}), **(tok.get('series') or {}), **(tok.get('colors') or {})}
    out = {}
    for k, v in chars.items():
        for f in ('color', 'shape'):
            if not v.get(f):
                raise Missing(f'contract.json: characters.{k}.{f}')
        c = v['color']
        if not str(c).startswith('#'):
            if c not in pal:
                raise Missing(f'design/tokens.json colour token "{c}" (contract characters.{k}.color)')
            c = pal[c]
        out[k] = {**v, 'hex': str(c).lower()}
    return out


SIDE_ORDER = {'left': 0, 'centre': 1, 'center': 1, 'right': 2}


@rule('V04', 'DX-V4, DX-X3', 'characters read from the episode contract (contract.json characters: color token or hex, shape, side); page objects with that `char` every 0.1 s: '
      'main colour and main shape of each (most frequent fill/stroke, shape) and their shares; for every pair of characters seen together (|Δx| ≥ 20 px) the sign of their '
      'horizontal order; year axis labels (role axis-label with year) ordered left → right. Contract without characters (or a character without color/shape) = MISSING',
      'every declared character seen; main colour = declared colour and ≥ 95% of its observations; main shape = declared shape and ≥ 95%; declared colours all differ; '
      'each pair keeps one side for the whole video, and the side the contract declares (left < centre < right) when both sides are declared; 0 time-order violations')
def v04(ctx):
    want = contract_characters(ctx)
    r = pr(ctx, 'V04')
    ch = r['characters']
    ms = []
    for k, w in want.items():
        c = ch.get(k)
        ms.append(metric(f'{k} seen', c is not None, '==', True))
        if c is None:
            continue
        ms += [metric(f'{k} main colour is the declared {w["color"]}', str(c['mainColour']).lower() == w['hex'], '==', True), metric(f'{k} colour share', c['colourShare'], '>=', 0.95),
               metric(f'{k} main shape is the declared {w["shape"]}', c['mainShape'] == w['shape'], '==', True), metric(f'{k} shape share', c['shapeShare'], '>=', 0.95)]
    hexes = [w['hex'] for w in want.values()]
    ms.append(metric('declared colours differ', len(set(hexes)) == len(hexes), '==', True))
    bad_side = []
    for pair, sp in (r.get('pairs') or {}).items():
        a, b = pair.split('|')
        if a not in want or b not in want:
            continue
        signs = {int(float(x)) for x, n in sp['signs'].items() if n and int(float(x))}
        sa, sb = SIDE_ORDER.get(want[a].get('side')), SIDE_ORDER.get(want[b].get('side'))
        expect = None if sa is None or sb is None or sa == sb else (-1 if sa < sb else 1)
        if len(signs) > 1 or (expect is not None and signs and signs != {expect}):
            bad_side.append({'pair': pair, 'signs': sp['signs'], 'declared': [want[a].get('side'), want[b].get('side')]})
    ms += [metric('character pairs on the wrong or on both sides', len(bad_side), '<=', 0), metric('time-order violations', len(r['timeOrderViolations']), '<=', 0)]
    return verdict('V04', ms, details=[ch, *bad_side[:5], r['timeOrderViolations'][:5]])


@rule('V08', 'DX-V6', 'every frame (no camera-move exemption), every 0.2 s, texts with opacity ≥ 0.95 standing still on screen (box moved < 2 px in 0.1 s; moving texts are judged by V12), on the delivered video frame: text colour = median of glyph-core pixels (glyph mask eroded 1 px), background = median of the ring '
      '1–4 px around the ink (inside the badge for badge text); WCAG contrast', '≥ 4.5:1 for every text sample')
def v08(ctx):
    r = pr(ctx, 'V08')
    worst = r['worst']['cr'] if r.get('worst') else None
    return verdict('V08', [metric('worst text contrast', worst, '>=', 4.5), metric('samples below 4.5:1', r['violations'], '<=', 0)], details=[r.get('worst'), *r['examples']])


@rule('V11', 'DX-V11 (C rule text-line-collision, upgraded to pixels)', 'every frame (no camera-move exemption), every 0.2 s: text ink from the page\'s text layer (glyphs, badges with their pill, axis labels; alpha > 64) '
      'dilated by 2 px vs ink of the graphics layer (lines, axes, series, bars, marks, stroked outlines; neutral cards and backgrounds excluded); and text vs text (each text rendered alone). '
      'A text standing still collides when it overlaps in one sample; a text moving on screen (box moved ≥ 2 px in 0.1 s), or a pair of texts one of which moves, when the same overlap is there in two consecutive samples (0.2 s)',
      '< 4 overlapping pixels for every text in every sample (moving text: not in two consecutive samples); 0 violations')
def v11(ctx):
    r = pr(ctx, 'V11')
    return verdict('V11', [metric('text collisions', r['violations'], '<=', 0)], details=[{'byRole': r['byRole'], 'movingNotPersistent': r.get('movingNotPersistent')}, *r['examples']])


@rule('V12', 'DX-V9 (replaces the camera-move exemption)', 'every frame, every 0.2 s, every text with opacity ≥ 0.95 fully on frame: normalised cross-correlation of luma between the delivered video frame\'s coded Y plane and the clean page render\'s Y\' (BT.709 weights) of the same instant (window.CHECKS.seek), '
        'inside the text box + 4 px. A doubled, smeared or motion-blurred label correlates poorly with its single sharp render (a ghost copy at 30% opacity: ≈ 0.96; at 50%: ≈ 0.91); '
      'grain, grade and vignette barely move it (affine inside a box). Texts with no ink contrast in the render (RMS < 8 codes) are skipped and counted',
      'NCC ≥ 0.97 for every text sample; 0 violations')
def v12(ctx):
    r = pr(ctx, 'V12')
    return verdict('V12', [metric('text samples', r['textSamples'], '>=', 1), metric('text samples below NCC 0.97', r['violations'], '<=', 0)],
                   details=[{k: r.get(k) for k in ('staticMedian', 'staticP05', 'movingMedian', 'movingP05', 'movingSamples', 'skippedFlat', 'lowest')}, *r['worst']])


def number_run(ws, want):
    """Shortest run of ASR words (≤ 6) that says the value `want`: (first index, last index)."""
    for L in range(1, 7):
        for i in range(len(ws) - L + 1):
            if canon_matches(want, spoken_numbers(asr_join(ws[i:i + L]))):
                return i, i + L - 1
    return None


@rule('C13', 'DX-V11 (number–voice sync ±250 ms)', 'for each narration sentence saying a number that is shown in the same scene: onset = start of the own-ASR word run saying the value; '
      'screen = first frame (frame-accurate) the claim span shows its final display text in that scene (page sampler claimFinal); when several claims of the scene carry the value, the one closest to the onset', '|screen − onset| ≤ 250 ms for every pair; 0 spoken numbers missing from ASR')
def c13(ctx):
    p = ctx.json('out/checks/page.json')
    final = p['claimFinal']
    asr = asr_master(ctx)
    rows, notheard = [], []
    claims = {c['claimId']: c for c in ctx.claims()}
    for s in ctx.sentences():
        nums = [c for c, _ in numbers_in_text(s['text'])]
        if not nums:
            continue
        ws = [w for w in asr if s['start'] - 1 <= w['start'] <= s['end'] + 1]
        for n in dict.fromkeys(nums):
            # claims shown in this scene that carry the spoken value; the voice refers to the one closest in time
            cands = []
            for k, t in final.items():
                cid, sc = k.split('|')
                c = claims.get(cid)
                if sc != s['scene'] or not c:
                    continue
                if any(canon_matches(n, [w]) for w, _ in numbers_in_text(str(c['display']))):
                    cands.append((cid, t))
            if not cands:
                continue
            run = number_run(ws, n)
            if not run:
                notheard.append((cands[0][0], s.get('id')))
                continue
            onset = ws[run[0]]['start']
            cid, t = min(cands, key=lambda x: abs(x[1] - onset))
            rows.append((cid, s['scene'], round(1000 * (t - onset))))
    worst = max((abs(r[2]) for r in rows), default=None)
    bad = [r for r in rows if abs(r[2]) > 250]
    return verdict('C13', [metric('pairs', len(rows), '>=', 1), metric('worst |offset| ms', worst, '<=', 250.0, 'ms'), metric('pairs > 250 ms', len(bad), '<=', 0),
                           metric('spoken numbers not in ASR', len(notheard), '<=', 0)], details=[{'over': bad[:10], 'notHeard': notheard[:10]}])
