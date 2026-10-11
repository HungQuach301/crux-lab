"""Tập 6 (Việc 0): tải CPI từ FRED, ghi SHA-256, URL ghim, ngày tải, điều khoản, quan sát cuối vào data/sources.json; dựng
data/normalized/*.csv cho đối chiếu (checks S04). Dữ liệu không commit (episodes/ep006/.gitignore).

    python3 episodes/ep006/data/fetch.py            # tải mới toàn bộ (vintage mới: viết lại sources.json)
    python3 episodes/ep006/data/fetch.py --verify   # file thiếu → tải lại từ pinnedUrl; kiểm SHA raw + normalized + bản ghim hồ sơ

Chính: CPIAUCNS (CPI-U all items, US city average, NSA, tháng). Đối chiếu: CPIAUCSL (cùng chỉ số, đã khử mùa): % đổi 12 tháng
SA vs NSA trong 0,5 điểm. Độ vững (không phải đối chiếu): CWUR0000SA0 (CPI-W, chỉ số dùng cho COLA An sinh xã hội) và PCEPI
(chỉ số giá PCE, BEA, từ 1959). bls.gov bị proxy chặn (403) → mọi file qua FRED. Tải bằng curl."""
import datetime, hashlib, html, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(EP))
RAW, NORM, PIN = os.path.join(HERE, 'raw'), os.path.join(HERE, 'normalized'), os.path.join(HERE, 'raw', 'dossier-pin')
DOSSIER = os.path.join(ROOT, 'topics-r1', 'machine', 'retire-1', 'sources.json')
FRED = 'https://fred.stlouisfed.org/graph/fredgraph.csv?id='
SERIES = [  # (id, role, what)
    ('CPIAUCNS', 'primary', 'CPI-U, all items in U.S. city average, all urban consumers, index 1982-84=100, monthly, not seasonally adjusted (BLS via FRED)'),
    ('CPIAUCSL', 'crosscheck', 'CPI-U, all items, seasonally adjusted (BLS via FRED): crosscheck of 12-month % change'),
    ('CWUR0000SA0', 'robust', 'CPI-W, urban wage earners and clerical workers, all items, NSA (BLS via FRED): the index behind Social Security COLAs'),
    ('PCEPI', 'robust', 'Personal consumption expenditures chain-type price index, 2017=100, monthly, SA (BEA via FRED), from 1959'),
]
TOL = 0.50   # điểm %: |% đổi 12 tháng NSA − SA|
CMD = 'python3 episodes/ep006/data/fetch.py --verify'


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def curl(url, dest):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    subprocess.run(['curl', '-sSfL', '--retry', '4', '--retry-all-errors', '-o', dest, url], check=True)


def page_text(url):
    r = subprocess.run(['curl', '-sSfL', '--retry', '4', '--retry-all-errors', url], check=True, capture_output=True)
    t = re.sub(r'<script.*?</script>|<style.*?</style>', '', r.stdout.decode('utf-8', 'replace'), flags=re.S)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', t)))


def rows(p):
    out = []
    for line in open(p).read().strip().splitlines()[1:]:
        d, v = line.split(',')[:2]
        if v not in ('', '.'):
            out.append((d, float(v)))
    return out


def blanks(p):
    return [line.split(',')[0] for line in open(p).read().strip().splitlines()[1:] if line.split(',')[1] in ('', '.')]


def write_csv(name, header, data):
    os.makedirs(NORM, exist_ok=True)
    p = os.path.join(NORM, name)
    with open(p, 'w') as f:
        f.write(header + '\n' + ''.join(','.join(str(x) for x in r) + '\n' for r in data))
    return 'data/normalized/' + name


def normalize():
    """Đối chiếu tất định, dựng lại chỉ từ raw/. Trả (derived paths, mismatches, summary)."""
    mism, summ, out = [], {}, []
    a = dict(rows(os.path.join(RAW, 'CPIAUCNS.csv')))
    c = dict(rows(os.path.join(RAW, 'CPIAUCSL.csv')))
    out.append(write_csv('cpiaucns.csv', 'month,index', sorted(a.items())))

    def back(m, k):
        y, mo = int(m[:4]), int(m[5:7]) - k
        while mo < 1:
            y, mo = y - 1, mo + 12
        return f'{y:04d}-{mo:02d}-01'
    pa, pc, gaps = [], [], []
    for m in sorted(a):
        q = back(m, 12)
        if q in a and m in c and q in c:
            x, y = round(100 * (a[m] / a[q] - 1), 4), round(100 * (c[m] / c[q] - 1), 4)
            pa.append((m, x)); pc.append((m, y)); gaps.append(abs(x - y))
            if abs(x - y) > TOL:
                mism.append({'key': m, 'series': 'cpi_yoy', 'note': f'CPIAUCNS {x:+.2f}% vs CPIAUCSL {y:+.2f}% 12-month ({x - y:+.2f} pp)'})
    out.append(write_csv('cpiaucns_yoy.csv', 'month,pct', pa))
    out.append(write_csv('cpiaucsl_yoy.csv', 'month,pct', pc))
    summ['cpi_yoy'] = {'months': len(gaps), 'within': sum(g <= TOL for g in gaps), 'maxGapPp': round(max(gaps), 3),
                       'meanGapPp': round(sum(gaps) / len(gaps), 4), 'from': pa[0][0], 'to': pa[-1][0],
                       'blankPrimary': blanks(os.path.join(RAW, 'CPIAUCNS.csv')), 'blankCrosscheck': blanks(os.path.join(RAW, 'CPIAUCSL.csv')),
                       'note': 'Same index, seasonal adjustment removed only within-year pattern; 12-month changes should agree closely.'}
    return out, mism, summ


def dossier_pins():
    res = []
    for s in json.load(open(DOSSIER))['series']:
        p = os.path.join(PIN, s['id'] + '.csv')
        if not os.path.exists(p) or '--verify' not in sys.argv:
            curl(s['url'], p)
        old = rows(p)
        new = [r for r in rows(os.path.join(RAW, s['id'] + '.csv')) if r[0] <= old[-1][0]]
        res.append({'series': s['id'], 'url': s['url'], 'sha256Dossier': s['sha256'], 'sha256Now': sha(p),
                    'matchesDossier': sha(p) == s['sha256'], 'freshPrefixIdentical': new == old,
                    'freshAddsObservations': len(rows(os.path.join(RAW, s['id'] + '.csv'))) - len(old)})
    return res


def fetch():
    today = datetime.date.today().isoformat()
    files = []
    for sid, role, what in SERIES:
        p = os.path.join(RAW, sid + '.csv')
        curl(FRED + sid, p)
        last = rows(p)[-1]
        pinned = f'{FRED}{sid}&coed={last[0]}'
        curl(pinned, p)
        assert rows(p)[-1] == last, sid
        page = f'https://fred.stlouisfed.org/series/{sid}'
        t = page_text(page)
        status = re.search(r'(Public Domain: Citation Requested|Copyrighted: Citation Required|Copyrighted: Pre-Approval Required)', t)
        upd = re.search(r'Updated: [A-Z][a-z]{2} \d{1,2}, \d{4},? [\d:]+ [AP]M [A-Z]{3}', t)
        units = re.search(r'Units: (.{5,80}?) Frequency', t)
        files.append({'path': f'data/raw/{sid}.csv', 'role': role, 'series': sid, 'what': what,
                      'url': FRED + sid, 'pinnedUrl': pinned, 'seriesPage': page, 'sha256': sha(p), 'downloaded': today,
                      'bytes': os.path.getsize(p), 'inRepo': False, 'fetch': CMD, 'firstObservation': rows(p)[0][0],
                      'lastObservation': {'date': last[0], 'value': last[1], 'updatedQuote': upd.group(0) if upd else None,
                                          'unitsQuote': units.group(1).strip() if units else None, 'quotedFrom': page, 'retrieved': today},
                      'terms': {'quote': status.group(1) if status else None, 'url': page,
                                'citation': f'{sid}, retrieved from FRED, Federal Reserve Bank of St. Louis; {page}'}})
        print(sid, role, rows(p)[0][0], last, sha(p)[:16], status.group(1) if status else 'TERMS?')
    derived, mism, summ = normalize()
    pins = dossier_pins()
    src = {'files': files, 'mismatches': mism,
           'derived': [{'path': d, 'sha256': sha(os.path.join(EP, d)), 'from': 'data/fetch.py normalize() over data/raw/*'} for d in derived],
           'crosscheckSummary': summ, 'dossierPins': pins, 'provisions': [],
           'blocked': {'bls.gov': 'HTTP 403 from the session proxy (2026-10-08): R-CPI-E (BLS research index for Americans 62+) not fetched; '
                                  'the retiree-basket limit is stated qualitatively, no R-CPI-E number is used.'},
           '_about': f'FRED copies, not committed ({CMD} re-downloads from pinnedUrl and checks SHA-256). "Now" of the data: CPI-U to '
                     f'{files[0]["lastObservation"]["date"]} (September 2026 CPI not yet released on {today}).'}
    json.dump(src, open(os.path.join(HERE, 'sources.json'), 'w'), indent=1, ensure_ascii=False)
    for pn in pins:
        print('dossier pin', pn['series'], 'SHA', 'OK' if pn['matchesDossier'] else 'KHÁC', '| prefix', 'OK' if pn['freshPrefixIdentical'] else 'SỬA',
              '| +obs', pn['freshAddsObservations'])
    for k, v in summ.items():
        print('crosscheck', k, {x: v[x] for x in v if x != 'note'})


def verify():
    src = json.load(open(os.path.join(HERE, 'sources.json')))
    bad, got = [], []
    for f in src['files']:
        p = os.path.join(EP, f['path'])
        if not os.path.exists(p):
            curl(f['pinnedUrl'], p); got.append(f['path'])
        if sha(p) != f['sha256']:
            bad.append(f['path'])
    if not bad:
        derived, _, _ = normalize()
        want = {d['path']: d['sha256'] for d in src['derived']}
        bad += [d for d in derived if sha(os.path.join(EP, d)) != want.get(d)]
    pins = dossier_pins()
    bad += [f"dossier-pin:{p['series']}" for p in pins if not p['matchesDossier']]
    print('downloaded:', got or 'none')
    print('sha256 mismatches:', bad or 'none')
    return not bad


if __name__ == '__main__':
    if '--verify' in sys.argv:
        sys.exit(0 if verify() else 1)
    fetch()
