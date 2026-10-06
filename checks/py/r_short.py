"""Shorts 9:16 (K3.8, checks-appeal A5; D-006 Q3: 2–3 Shorts per episode from Episode 4). contract.json `shorts`: [{file}] (paths from the episode root).
A contract written before D-006 (no `format`) and without `shorts` has no Shorts to check (Episodes 1–3): the rules pass with a note. A D-006 contract
(with `format`) without `shorts` = MISSING.
Text size, the player-UI zones and the on-frame labels (ILLUSTRATIVE, "history, not a forecast") need the vertical page's objects (window.CHECKS): they
wait for the factory page to expose them (checks-appeal A8); the rules below measure the delivered file and what the viewer hears."""
import re

from common import Missing, ebur128, ffprobe, metric, rule, verdict

SH_MAX_S = 180.0   # YouTube accepts square or vertical uploads up to 3 minutes as Shorts (since 2024-10-15); the brief's 60 s is reported, not enforced


def shorts(ctx):
    c = ctx.contract()
    sh = c.get('shorts')
    if sh is None:
        if c.get('format') is None:
            return None
        raise Missing('contract.json: shorts (D-006: 2–3 Shorts per episode)')
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
