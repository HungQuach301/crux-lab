"""Quyền footage ngoài (K4.4, chủ dự án 13/10/2026; học theo cine-lab scripts/ll/rights_check.py).

Footage ngoài = mọi tệp ảnh / video / bản đồ không do dự án tự sinh mà đi vào hình của tập. Khai trong out/timeline.json:
  external: [{file, rid, kind: image|video|map, t0, t1}]          (cấp tập; hoặc scenes[].external, cùng dạng)
`rid` = mã một dòng bảng trong RIGHTS.md (gốc repo; RIGHTS.md của tập nếu có cũng được đọc). Dòng đó phải có (theo tên cột, thiếu cột thì tìm trong cả dòng):
  URL nguồn (http/https) · giấy phép (tên/SPDX) · trích NGUYÊN VĂN câu giấy phép trong ngoặc kép (≥ 20 ký tự) · ngày tải YYYY-MM-DD ·
  SHA-256 của tệp (64 hex, phải khớp tệp đang dùng) · ghi nguồn (câu ghi công).
Mọi chuỗi trong out/timeline.json trỏ tới tệp ảnh/video/bản đồ (đuôi MEDIA) mà không có trong external[] và không khớp luật tự sinh
(contract rights.generated / out/visual-assets.json generated[].glob) = footage KHÔNG HỒ SƠ.
"""
import fnmatch
import glob
import hashlib
import os
import re

from common import Missing, metric, rule, verdict

MEDIA = re.compile(r'\.(png|jpe?g|webp|gif|tiff?|bmp|svg|mp4|mov|m4v|webm|mkv|avi|geojson|pbf|mbtiles|osm|kml|gpx)$', re.I)
KINDS = ('image', 'video', 'map')
SHARE_MAX = 0.20   # trần thời lượng footage ngoài / thời lượng tập (như cine-lab rights_check: 20 %); contract rights.externalMaxShare chỉ được hạ

# giấy phép CẤM (mọi footage ngoài ở đây đều là hình: ảnh, video, bản đồ) — NC, ND, BY-SA
FORBIDDEN = [('NC', re.compile(r'\bNC\b|non-?commercial', re.I)), ('ND', re.compile(r'\bND\b|no-?deriv', re.I)),
             ('BY-SA', re.compile(r'\bBY-SA\b|share-?alike', re.I))]
# giấy phép NHẬN DIỆN (ngoài danh sách → chưa dùng được: thêm qua phiên K kèm trích nguyên văn); attribution = phải ghi nguồn trong mô tả
KNOWN = [('public domain', re.compile(r'public domain|\bCC0\b|\bPDM\b|u\.?s\.? government work|17 u\.s\.c\. ?§ ?105|no known restrictions', re.I), False),
         ('CC BY', re.compile(r'\bCC[ -]BY\b(?![ -](SA|NC|ND))', re.I), True),
         ('ODbL (OpenStreetMap)', re.compile(r'\bODbL\b|openstreetmap', re.I), True)]
QUOTE = re.compile(r'["“]([^"”]{20,})["”]')
URL = re.compile(r'https?://\S+')
DATE = re.compile(r'\b20\d\d-\d\d-\d\d\b')
SHA = re.compile(r'\b[0-9a-f]{64}\b', re.I)


def _repo(ctx):
    """The repository holding the episode: the nearest parent with RIGHTS.md (the episode root itself counts)."""
    d = os.path.abspath(ctx.root)
    while True:
        if os.path.exists(os.path.join(d, 'RIGHTS.md')) and d != os.path.abspath(ctx.root):
            return d
        up = os.path.dirname(d)
        if up == d:
            return None
        d = up


def rights_rows(ctx):
    """Every table row of RIGHTS.md (repo, then the episode's own): {rid: {'cells': {header: text}, 'line': whole row}}."""
    files = [os.path.join(p, 'RIGHTS.md') for p in (_repo(ctx), ctx.root) if p]
    rows = {}
    for f in files:
        if not os.path.exists(f):
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
    tl = ctx.timeline()
    items = list(tl.get('external') or [])
    for s in tl.get('scenes') or []:
        items += list(s.get('external') or [])
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


@rule('F13', 'chủ dự án 13/10/2026 (luật kiểm quyền footage ngoài; RIGHTS.md; cine-lab rights_check)',
      'external footage = out/timeline.json external[] ∪ scenes[].external[] {file, rid, kind image|video|map, t0, t1}, plus every string of out/timeline.json '
      'naming an image/video/map file (MEDIA suffixes) that is not declared there and does not match a generated rule (contract rights.generated, '
      'out/visual-assets.json generated[].glob). Each item: a RIGHTS.md row (repo root, or the episode\'s) whose first cell = rid, with source URL (http/https), '
      'licence, the licence text quoted verbatim ("…", ≥ 20 characters), download date YYYY-MM-DD, SHA-256 equal to the file in use, and a credit line. '
      'Licence (licence cell, else the row): NC, ND, BY-SA → forbidden (all external footage is picture); recognised = public domain/CC0/US government work, '
      'CC BY, ODbL/OpenStreetMap; anything else = not usable until a K session adds it. CC BY and ODbL/OpenStreetMap need their credit line in '
      'out/package/description.md (whitespace and case ignored; (c) = ©), and OpenStreetMap items the word "OpenStreetMap" there',
      '0 footage without a complete record (row, URL, verbatim quote, date, SHA match, file present, kind, t0 < t1); 0 forbidden or unrecognised licences; '
      '0 attribution-licence items whose credit is missing from the description')
def f13_external_rights(ctx):
    items = external_items(ctx)
    declared = {it.get('file') for it in items}
    gen = _generated(ctx)
    loose = []
    _media_strings(ctx.timeline(), loose)
    undeclared = sorted({s for s in loose if s not in declared and not any(fnmatch.fnmatch(s, g) or fnmatch.fnmatch(os.path.basename(s), g) for g in gen)})
    rows = rights_rows(ctx) if (items or undeclared) else {}
    desc = _norm(open(ctx.path('out/package/description.md'), encoding='utf-8').read()) if ctx.has('out/package/description.md') else None
    norecord, banned, nocredit = [{'file': s, 'why': 'not declared in external[] (no rights record)'} for s in undeclared], [], []
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
        if not URL.search(url):
            why.append('no source URL')
        if not QUOTE.search(quote):
            why.append('licence not quoted verbatim')
        if not DATE.search(date):
            why.append('no download date')
        p = _file(ctx, f)
        if p is None:
            why.append('file not found')
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
            why.append('no t0/t1')
        if why:
            norecord.append({'file': f, 'rid': rid, 'why': '; '.join(why)})
        name, state, attr = licence_of(lic)   # the licence cell only: a verbatim ODbL quote says "share-alike" of the database, not of the picture
        if state != 'ok':
            banned.append({'file': f, 'rid': rid, 'licence': name or lic[:80], 'why': 'forbidden for picture (NC, ND, BY-SA)' if state == 'forbidden' else 'licence not recognised'})
        elif attr:
            need = [x for x in ([credit] if credit and credit not in ('—', '-') else []) if x]
            if name.startswith('ODbL') or re.search(r'openstreetmap', line, re.I):
                need.append('OpenStreetMap')
            miss = 'no credit line in RIGHTS.md' if not credit or credit in ('—', '-') else None
            if desc is None:
                miss = 'out/package/description.md missing'
            elif not miss:
                lost = [x for x in need if _norm(x.strip('"“”')) not in desc]
                miss = ('credit not in description: ' + ' | '.join(lost)) if lost else None
            if miss:
                nocredit.append({'file': f, 'rid': rid, 'licence': name, 'why': miss})
    return verdict('F13', [metric('external footage items', len(items) + len(undeclared), '>=', 0),
                           metric('footage without a complete rights record', len(norecord), '<=', 0),
                           metric('footage under a forbidden or unrecognised licence', len(banned), '<=', 0),
                           metric('attribution licences without the credit in the description', len(nocredit), '<=', 0)],
                   details=[{'noRecord': norecord[:40], 'licence': banned[:40], 'credit': nocredit[:40]}])


@rule('F15', 'chủ dự án 13/10/2026 (luật kiểm quyền footage ngoài: trần thời lượng)',
      'share = length of the union of [t0, t1) of the external footage (out/timeline.json external[] ∪ scenes[].external[]) / timeline total; '
      f'ceiling {int(SHARE_MAX * 100)} % (contract.json rights.externalMaxShare may only lower it)',
      f'share ≤ {int(SHARE_MAX * 100)} % (or the lower contract ceiling)')
def f15_external_share(ctx):
    items = external_items(ctx)
    cap = SHARE_MAX
    try:
        r = ctx.contract().get('rights')
        c = (r or {}).get('externalMaxShare') if isinstance(r, dict) else None
        if isinstance(c, (int, float)) and 0 <= c < cap:
            cap = float(c)
    except Missing:
        pass
    iv = []
    for it in items:
        try:
            a, b = float(it['t0']), float(it['t1'])
        except (KeyError, TypeError, ValueError):
            raise Missing(f"out/timeline.json external: {it.get('file')} without t0/t1")
        if b > a:
            iv.append((a, b))
    iv.sort()
    tot, cur = 0.0, None
    for a, b in iv:
        if cur and a <= cur[1]:
            cur[1] = max(cur[1], b)
        else:
            if cur:
                tot += cur[1] - cur[0]
            cur = [a, b]
    if cur:
        tot += cur[1] - cur[0]
    total = ctx.total()
    return verdict('F15', [metric('external footage share (%)', 100 * tot / total if total else 0.0, '<=', 100 * cap, '%')],
                   details=[{'externalSeconds': round(tot, 3), 'total': total, 'ceiling': cap}])
