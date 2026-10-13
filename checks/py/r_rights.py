"""Quyền và trung thực footage ngoài (K4.4; checks-appeal A39, gộp A44 của nhánh ep008; RIGHTS.md §F — D-013, chủ dự án 13/10/2026;
học theo cine-lab scripts/ll/rights_check.py).

Footage ngoài = mọi tệp ảnh / video / bản đồ không do dự án tự sinh mà đi vào hình của tập. Khai (gộp theo `file`, thứ tự ưu tiên):
  1. out/timeline.json  external: [{file, rid, kind, t0, t1}]  (và scenes[].external[], cùng dạng) — nhà máy ghi, giờ chính xác;
  2. episode.yaml       external: [{id, rights, kind, file?, scenes?, t0?, t1?}]  (A39) — không có t0/t1 thì lấy trọn khoảng các cảnh `scenes`
     (cận trên cho trần thời lượng).
`kind` = archival (tư liệu, phải có năm + nguồn trên hình) | illustrative (minh hoạ, phải có nhãn minh hoạ, không đi cùng số của claim).
`rid`/`rights` = Mã một dòng bảng RIGHTS.md (gốc repo §F6; RIGHTS.md của tập nếu có). Dòng phải có (theo tên cột, thiếu cột thì tìm cả dòng):
  URL nguồn (http/https) · giấy phép (tên) · trích NGUYÊN VĂN câu giấy phép trong ngoặc kép (≥ 20 ký tự) · ngày tải YYYY-MM-DD ·
  SHA-256 của tệp (64 hex, phải khớp tệp đang dùng — tệp ở work/external/, ngoài git, có mặt ở container chạy checks) · ghi nguồn.
Mọi chuỗi trong out/timeline.json trỏ tới tệp ảnh/video/bản đồ (đuôi MEDIA) mà không có trong các khai trên và không khớp luật tự sinh
(contract rights.generated / out/visual-assets.json generated[].glob) = footage KHÔNG HỒ SƠ.
Trần thời lượng (RIGHTS §F3): Tập 8 ≤ 15 %, từ Tập 9 ≤ 20 % (số tập: contract.json episode); episode.yaml footage.max_share hoặc
contract.json rights.externalMaxShare chỉ được HẠ.
"""
import fnmatch
import hashlib
import os
import re

from common import Missing, metric, numbers_in_text, rule, verdict

MEDIA = re.compile(r'\.(png|jpe?g|webp|gif|tiff?|bmp|svg|mp4|mov|m4v|webm|mkv|avi|geojson|pbf|mbtiles|osm|kml|gpx|shp)$', re.I)
KINDS = ('archival', 'illustrative')
RUN_MAX = 6.0      # RIGHTS §F3: mỗi lần ≤ 6 s liền
OPEN_S = 5.0       # RIGHTS §F3: không mở tập (5 s đầu ở thế giới, quy tắc 7)


def share_cap(ctx):
    """RIGHTS §F3: 0.15 in Episode 8, 0.20 otherwise; episode.yaml footage.max_share / contract rights.externalMaxShare may only lower it."""
    cap = 0.15 if ctx.episode_no() == 8 else 0.20
    lower = []
    try:
        r = ctx.contract().get('rights')
        lower.append((r or {}).get('externalMaxShare') if isinstance(r, dict) else None)
    except Missing:
        pass
    lower.append(((_yaml(ctx).get('footage') or {}) if isinstance(_yaml(ctx).get('footage'), dict) else {}).get('max_share'))
    for c in lower:
        if isinstance(c, (int, float)) and 0 <= c < cap:
            cap = float(c)
    return cap


# giấy phép CẤM (RIGHTS §F2; mọi footage là hình): NC, ND, BY-SA
FORBIDDEN = [('NC', re.compile(r'\bNC\b|non-?commercial', re.I)), ('ND', re.compile(r'\bND\b|no-?deriv', re.I)),
             ('BY-SA', re.compile(r'\bBY-SA\b|share-?alike', re.I))]
# danh sách trắng RIGHTS §F1 (bậc 1–6); attribution = phải ghi nguồn trong mô tả YouTube
KNOWN = [('public domain', re.compile(r'public domain|\bCC0\b|\bPDM\b|u\.?s\.? government work|17 u\.s\.c\. ?§ ?105|natural earth|tiger/line', re.I), False),
         ('no known restrictions (organisation assessment)', re.compile(r'no known restrictions', re.I), False),
         ('Pexels / Pixabay licence', re.compile(r'\bpexels\b|\bpixabay\b', re.I), False),
         ('CC BY', re.compile(r'\bCC[ -]BY\b(?![ -](SA|NC|ND))', re.I), True),
         ('ODbL (OpenStreetMap data)', re.compile(r'\bODbL\b|openstreetmap', re.I), True)]
QUOTE = re.compile(r'["“]([^"”]{20,})["”]')
URL = re.compile(r'https?://\S+')
DATE = re.compile(r'\b20\d\d-\d\d-\d\d\b')
SHA = re.compile(r'\b[0-9a-f]{64}\b', re.I)
YEAR = re.compile(r'\b(1[6-9]\d\d|20\d\d)\b')
SOURCE = re.compile(r'\bsource\b|\bphoto\b|\bcourtesy\b|©|\bdata:', re.I)
ILLUS = re.compile(r'illustrat', re.I)


def _yaml(ctx):
    def get():
        if not ctx.has('episode.yaml'):
            return {}
        import yaml
        y = yaml.safe_load(open(ctx.path('episode.yaml'), encoding='utf-8')) or {}
        return y if isinstance(y, dict) else {}
    return ctx.memo(('episode.yaml',), get)


def _repo(ctx):
    d = os.path.dirname(os.path.abspath(ctx.root))
    while True:
        if os.path.exists(os.path.join(d, 'RIGHTS.md')):
            return d
        up = os.path.dirname(d)
        if up == d:
            return None
        d = up


def rights_rows(ctx):
    """Every table row of RIGHTS.md (repo, then the episode's own): {first cell: {'cells': {header: text}, 'line': whole row}}."""
    rows = {}
    for base in (_repo(ctx), ctx.root):
        f = os.path.join(base, 'RIGHTS.md') if base else None
        if not f or not os.path.exists(f):
            continue
        head = None
        for ln in open(f, encoding='utf-8'):
            ln = ln.strip()
            if not ln.startswith('|'):
                head = None
                continue
            c = [x.strip() for x in ln.strip('|').split('|')]
            if all(re.fullmatch(r':?-{3,}:?', x) for x in c if x):
                continue
            if head is None:
                head = [x.lower() for x in c]
                continue
            if c and c[0]:
                rows[c[0].strip('`')] = {'cells': dict(zip(head, c)), 'line': ln}
    return rows


def _cell(row, *keys):
    for h, v in row['cells'].items():
        if any(k in h for k in keys):
            return v
    return None


def external_items(ctx):
    """Declared external footage, merged by file (timeline first): [{file, rid, kind, t0, t1, from}]."""
    tl = ctx.timeline()
    items, seen = [], set()
    for it in list(tl.get('external') or []) + [x for s in tl.get('scenes') or [] for x in (s.get('external') or [])]:
        items.append({'file': it.get('file'), 'rid': it.get('rid') or it.get('rights'), 'kind': it.get('kind'), 't0': it.get('t0'), 't1': it.get('t1'),
                      'from': 'out/timeline.json'})
        seen.add(it.get('file') or it.get('rid'))
    sc = {s['id']: s for s in tl.get('scenes') or []}
    for it in _yaml(ctx).get('external') or []:
        if not isinstance(it, dict) or (it.get('file') or it.get('rights') or it.get('rid')) in seen:
            continue
        t0, t1 = it.get('t0'), it.get('t1')
        if t0 is None and it.get('scenes'):
            ss = [sc[x] for x in it['scenes'] if x in sc]
            if ss:
                t0, t1 = min(s['start'] for s in ss), max(s.get('end', s['start'] + s.get('dur', 0)) for s in ss)
        items.append({'file': it.get('file'), 'rid': it.get('rights') or it.get('rid'), 'kind': it.get('kind'), 't0': t0, 't1': t1, 'id': it.get('id'),
                      'from': 'episode.yaml'})
    return items


def _generated(ctx):
    globs = []
    try:
        r = ctx.contract().get('rights')
        globs += [g.get('glob') for g in ((r or {}).get('generated') or []) if isinstance(g, dict)]
    except Missing:
        pass
    if ctx.has('out/visual-assets.json'):
        globs += [g.get('glob') for g in (ctx.json('out/visual-assets.json').get('generated') or []) if isinstance(g, dict)]
    return [g for g in globs if g]


def _media_strings(o, out):
    if isinstance(o, dict):
        for k, v in o.items():
            if k != 'external':
                _media_strings(v, out)
    elif isinstance(o, list):
        for v in o:
            _media_strings(v, out)
    elif isinstance(o, str) and MEDIA.search(o.split('?')[0]):
        out.append(o)


def _file(ctx, rel):
    for base in (ctx.root, _repo(ctx)):
        if base and rel and not os.path.isabs(rel) and '..' not in rel.split('/'):
            p = os.path.join(base, rel)
            if os.path.isfile(p):
                return p
    return None


def _sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def licence_of(text):
    for name, rx in FORBIDDEN:
        if rx.search(text):
            return name, 'forbidden', False
    for name, rx, attr in KNOWN:
        if rx.search(text):
            return name, 'ok', attr
    return None, 'unknown', False


def _norm(s):
    return re.sub(r'\s+', ' ', s.replace('(c)', '©').replace('(C)', '©')).strip().lower()


def _intervals(items):
    iv = []
    for it in items:
        try:
            a, b = float(it['t0']), float(it['t1'])
        except (KeyError, TypeError, ValueError):
            continue
        if b > a:
            iv.append((a, b))
    iv.sort()
    out = []
    for a, b in iv:
        if out and a <= out[-1][1]:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([a, b])
    return out


@rule('F13', 'checks-appeal A39 (+ A44), RIGHTS.md §F (D-013, chủ dự án 13/10/2026), cine-lab rights_check',
      'external footage = out/timeline.json external[] ∪ scenes[].external[] {file, rid, kind, t0, t1} ∪ episode.yaml external[] {id, rights, kind, file, '
      'scenes | t0, t1} (merged by file; no times → the span of its scenes), plus every string of out/timeline.json naming an image/video/map file '
      '(MEDIA suffixes) not declared there and not matching a generated rule. Each item: a RIGHTS.md row (repo §F6, or the episode\'s) whose first cell '
      '= rid, with source URL (http/https), licence, the licence text quoted verbatim ("…", ≥ 20 characters), download date YYYY-MM-DD, SHA-256 equal to '
      'the file in use, a credit line, kind archival|illustrative, t0 < t1. Licence (licence cell, else the row) against RIGHTS §F: NC, ND, BY-SA → '
      'forbidden; recognised = public domain / CC0 / PDM / US government work / Natural Earth / TIGER, "No known restrictions", Pexels / Pixabay, '
      'CC BY, ODbL / OpenStreetMap data; anything else = not usable (ask the owner, CHARTER §5). CC BY and ODbL need their credit line in '
      'out/package/description.md (whitespace and case ignored; (c) = ©), OpenStreetMap items also the word "OpenStreetMap". Share = union of '
      '[t0, t1) / timeline total, ceiling 15 % in Episode 8, 20 % otherwise (episode.yaml footage.max_share, contract rights.externalMaxShare only lower it)',
      '0 footage without a complete record; 0 forbidden or unrecognised licences; 0 attribution licences without the credit in the description; '
      'share ≤ ceiling')
def f13_external_rights(ctx):
    items = external_items(ctx)
    declared = {it.get('file') for it in items}
    gen = _generated(ctx)
    loose = []
    _media_strings(ctx.timeline(), loose)
    undeclared = sorted({s for s in loose if s not in declared and not any(fnmatch.fnmatch(s, g) or fnmatch.fnmatch(os.path.basename(s), g) for g in gen)})
    rows = rights_rows(ctx) if (items or undeclared) else {}
    desc = _norm(open(ctx.path('out/package/description.md'), encoding='utf-8').read()) if ctx.has('out/package/description.md') else None
    norecord, banned, nocredit = [{'file': s, 'why': 'not declared as external footage (no rights record)'} for s in undeclared], [], []
    for it in items:
        f, rid = it.get('file'), it.get('rid')
        why = []
        row = rows.get(rid) if rid else None
        if row is None:
            norecord.append({'file': f, 'rid': rid, 'why': 'no RIGHTS.md row'})
            continue
        line = row['line']
        url = _cell(row, 'url', 'nguồn/url', 'source') or line
        lic = _cell(row, 'giấy phép', 'licen') or line
        quote = _cell(row, 'nguyên văn', 'quote', 'trích') or lic
        date = _cell(row, 'ngày', 'date') or line
        sha = _cell(row, 'sha') or line
        credit = _cell(row, 'ghi nguồn', 'ghi công', 'credit', 'attribution')
        f = f or _cell(row, 'tệp', 'file')
        f = f.strip('`') if f else f
        if not URL.search(url):
            why.append('no source URL')
        if not QUOTE.search(quote):
            why.append('licence not quoted verbatim')
        if not DATE.search(date):
            why.append('no download date')
        p = _file(ctx, f)
        if p is None:
            why.append(f'file not found: {f}')
        else:
            m = SHA.search(sha)
            if not m:
                why.append('no SHA-256')
            elif m.group(0).lower() != _sha(p):
                why.append('SHA-256 does not match the file')
        if it.get('kind') not in KINDS:
            why.append(f"kind {it.get('kind')!r} not in {KINDS}")
        try:
            if not float(it['t0']) < float(it['t1']):
                why.append('t0 ≥ t1')
        except (KeyError, TypeError, ValueError):
            why.append('no t0/t1 (and no scenes)')
        if why:
            norecord.append({'file': f, 'rid': rid, 'why': '; '.join(why)})
        name, state, attr = licence_of(lic)   # the licence cell only: a verbatim ODbL quote says "share-alike" of the database, not of the picture
        if state != 'ok':
            banned.append({'file': f, 'rid': rid, 'licence': name or lic[:80], 'why': 'forbidden for picture (NC, ND, BY-SA)' if state == 'forbidden' else 'licence not on the RIGHTS §F whitelist'})
        elif attr:
            has_credit = credit and credit.strip() not in ('—', '-', '')
            need = [credit] if has_credit else []
            if name.startswith('ODbL') or re.search(r'openstreetmap', line, re.I):
                need.append('OpenStreetMap')
            miss = None if has_credit else 'no credit line in RIGHTS.md'
            if desc is None:
                miss = 'out/package/description.md missing'
            elif not miss:
                lost = [x for x in need if _norm(x.strip('"“”')) not in desc]
                miss = ('credit not in description: ' + ' | '.join(lost)) if lost else None
            if miss:
                nocredit.append({'file': f, 'rid': rid, 'licence': name, 'why': miss})
    cap = share_cap(ctx)
    tot = sum(b - a for a, b in _intervals(items))
    total = ctx.total()
    return verdict('F13', [metric('external footage items', len(items) + len(undeclared), '>=', 0),
                           metric('footage without a complete rights record', len(norecord), '<=', 0),
                           metric('footage under a forbidden or unrecognised licence', len(banned), '<=', 0),
                           metric('attribution licences without the credit in the description', len(nocredit), '<=', 0),
                           metric('external footage share (%)', 100 * tot / total if total else 0.0, '<=', round(100 * cap, 3), '%')],
                   details=[{'noRecord': norecord[:40], 'licence': banned[:40], 'credit': nocredit[:40], 'externalSeconds': round(tot, 3), 'ceiling': cap}])


def _states(track, a, b):
    """Text states of the page text track (one entry per change) that are on screen at some time in [a, b)."""
    out, last = [], None
    for s in track:
        if s['t'] <= a + 1e-6:
            last = s
        elif s['t'] < b - 1e-6:
            out.append(s)
    return ([last] if last else []) + out


@rule('F15', 'checks-appeal A39 (CHÍNH: trung thực footage), RIGHTS.md §F3–F4 (D-013)',
      'per declared external footage interval [t0, t1) (F13 sources): the on-screen text states of the page sampler text track (out/checks/page.json '
      'textTrack) that are visible in it. archival: every state shows a year (1600–2099) and a source word (Source/Photo/Courtesy/©/Data:); illustrative: '
      'every state shows an "illustrat…" label and no number that equals a claim display (out/claims.json). Each footage run ≤ 6 s; none starts in the '
      'first 5 s of the episode. No declared footage = nothing to check',
      '0 archival intervals without year + source on screen; 0 illustrative intervals without the label or with a claim number; 0 runs > 6 s; 0 runs in the first 5 s')
def f15_external_honesty(ctx):
    items = [it for it in external_items(ctx) if it.get('t0') is not None and it.get('t1') is not None]
    if not items:
        return verdict('F15', [metric('external footage intervals', 0, '>=', 0)], note='no declared external footage')
    if not ctx.has('out/checks/page.json'):
        raise Missing('out/checks/page.json (page sampler text track) for the on-screen year + source of external footage')
    track = ctx.json('out/checks/page.json').get('textTrack')
    if track is None:
        raise Missing('out/checks/page.json textTrack')
    claims = set()
    for c in ctx.claims() if ctx.has('out/claims.json') else []:
        claims.update(cn for cn, _ in numbers_in_text(str(c.get('display', ''))))
    noyear, illus, long_, opening = [], [], [], []
    for it in items:
        a, b = float(it['t0']), float(it['t1'])
        st = _states(track, a, b)
        texts = [' · '.join(x['text'] for x in s['items']) for s in st]
        if it.get('kind') == 'archival':
            bad = [round(s['t'], 2) for s, t in zip(st, texts) if not (YEAR.search(t) and SOURCE.search(t))]
            if bad or not st:
                noyear.append({'file': it.get('file'), 'rid': it.get('rid'), 'statesWithout': bad[:10] or ['no text on screen']})
        elif it.get('kind') == 'illustrative':
            nolab = [round(s['t'], 2) for s, t in zip(st, texts) if not ILLUS.search(t)]
            nums = sorted({cn for t in texts for cn, _ in numbers_in_text(t) if cn in claims})
            if nolab or nums or not st:
                illus.append({'file': it.get('file'), 'rid': it.get('rid'), 'statesWithoutLabel': nolab[:10], 'claimNumbers': nums[:10]})
        if b - a > RUN_MAX + 1e-6:
            long_.append({'file': it.get('file'), 'seconds': round(b - a, 3)})
        if a < OPEN_S:
            opening.append({'file': it.get('file'), 't0': a})
    return verdict('F15', [metric('external footage intervals', len(items), '>=', 0),
                           metric('archival footage without year + source on screen', len(noyear), '<=', 0),
                           metric('illustrative footage without label or with a claim number', len(illus), '<=', 0),
                           metric('footage runs over 6 s', len(long_), '<=', 0), metric('footage in the first 5 s', len(opening), '<=', 0)],
                   details=[{'archival': noyear[:20], 'illustrative': illus[:20], 'long': long_[:20], 'opening': opening}])
