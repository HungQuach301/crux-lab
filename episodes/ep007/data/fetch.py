"""Tập 7 (Việc 0): tải lãi vay PMMS 30 năm và 15 năm (Freddie Mac qua FRED), ghi SHA-256, URL ghim, ngày tải, điều khoản, quan sát cuối vào data/sources.json; dựng
data/normalized/*.csv cho đối chiếu (checks S04). Dữ liệu không commit (episodes/ep007/.gitignore).

    python3 episodes/ep007/data/fetch.py            # tải mới toàn bộ (vintage mới: viết lại sources.json)
    python3 episodes/ep007/data/fetch.py --verify   # file thiếu → tải lại từ pinnedUrl; kiểm SHA raw + normalized + bản ghim hồ sơ

Chính: MORTGAGE30US, MORTGAGE15US (Freddie Mac PMMS, trung bình tuần, %). Đối chiếu: OBMMIC30YF, OBMMIC15YF (Optimal Blue, khoản vay
chuẩn, ngày, từ 2017): trung bình các ngày trong 7 ngày kết thúc ở ngày PMMS so với PMMS, lệch ≤ 0,5 điểm. Tải bằng curl."""
import datetime, hashlib, html, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(EP))
RAW, NORM, PIN = os.path.join(HERE, 'raw'), os.path.join(HERE, 'normalized'), os.path.join(HERE, 'raw', 'dossier-pin')
DOSSIER = os.path.join(ROOT, 'topics-r2', 'machine', 'debt-1', 'sources.json')
FRED = 'https://fred.stlouisfed.org/graph/fredgraph.csv?id='
SERIES = [  # (id, role, what)
    ('MORTGAGE30US', 'primary', '30-Year Fixed Rate Mortgage Average in the United States, percent, weekly (Freddie Mac PMMS via FRED)'),
    ('MORTGAGE15US', 'primary', '15-Year Fixed Rate Mortgage Average in the United States, percent, weekly (Freddie Mac PMMS via FRED)'),
    ('OBMMIC30YF', 'crosscheck', '30-Year Fixed Rate Conforming Mortgage Index, percent, daily (Optimal Blue via FRED): crosscheck of PMMS 30-year, internal only'),
    ('OBMMIC15YF', 'crosscheck', '15-Year Fixed Rate Conforming Mortgage Index, percent, daily (Optimal Blue via FRED): crosscheck of PMMS 15-year, internal only'),
]
TOL = 0.50   # điểm %: |% đổi 12 tháng NSA − SA|
CMD = 'python3 episodes/ep007/data/fetch.py --verify'


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
    a30 = dict(rows(os.path.join(RAW, 'MORTGAGE30US.csv')))
    a15 = dict(rows(os.path.join(RAW, 'MORTGAGE15US.csv')))
    weeks = sorted(set(a30) & set(a15))
    out.append(write_csv('pmms_weekly.csv', 'week,rate30,rate15', [(w, a30[w], a15[w]) for w in weeks]))
    for term, ob in (('30', 'OBMMIC30YF'), ('15', 'OBMMIC15YF')):
        obd = dict(rows(os.path.join(RAW, ob + '.csv')))
        a = a30 if term == '30' else a15
        pairs, gaps = [], []
        for w in sorted(a):
            d0 = datetime.date.fromisoformat(w)
            win = [obd[k] for k in ((d0 - datetime.timedelta(days=i)).isoformat() for i in range(7)) if k in obd]
            if win:
                ob_mean = round(sum(win) / len(win), 4)
                pairs.append((w, a[w], ob_mean)); gaps.append(abs(a[w] - ob_mean))
                if abs(a[w] - ob_mean) > TOL:
                    mism.append({'key': w, 'series': f'MORTGAGE{term}US', 'note': f'PMMS {a[w]} vs {ob} 7-day mean {ob_mean}: gap > {TOL} pt'})
        out.append(write_csv(f'crosscheck{term}.csv', 'week,pmms,ob7', pairs))
        summ[f'mortgage{term}'] = {'weeks': len(pairs), 'within': sum(g <= TOL for g in gaps), 'maxGapPp': round(max(gaps), 3),
                                    'meanGapPp': round(sum(gaps) / len(gaps), 3), 'from': pairs[0][0], 'to': pairs[-1][0],
                                    'note': 'Optimal Blue (locked rates, conforming) vs PMMS (survey, prime, ~20% down): different populations; tolerance 0.5 pt.'}
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
           '_about': f'FRED copies, not committed ({CMD} re-downloads from pinnedUrl and checks SHA-256). "Now" of the data: PMMS to '
                     f'{files[0]["lastObservation"]["date"]} (weekly survey, released Thursdays; downloaded {today}).'}
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
