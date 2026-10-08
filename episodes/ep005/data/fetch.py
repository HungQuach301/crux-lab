"""Tập 5 (Việc 0): tải dữ liệu FRED mới, ghi SHA-256, URL ghim, ngày tải, điều khoản và quan sát cuối vào data/sources.json,
dựng data/normalized/*.csv cho đối chiếu (checks S04). Dữ liệu không commit (episodes/ep005/.gitignore).

    python3 episodes/ep005/data/fetch.py            # tải mới toàn bộ (vintage mới: viết lại sources.json)
    python3 episodes/ep005/data/fetch.py --verify   # file thiếu → tải lại từ pinnedUrl; kiểm SHA raw + normalized + bản ghim hồ sơ

Chính: HPIPONM226N (FHFA purchase-only HPI, tháng, NSA), MORTGAGE30US (Freddie Mac PMMS, tuần), MSPUS (giá bán trung vị, quý;
chỉ dùng chọn giá nhà minh hoạ). Đối chiếu: CSUSHPINSA (S&P Cotality Case-Shiller national, tháng, NSA) cho chỉ số giá
(so % đổi theo tháng), OBMMIC30YF (Optimal Blue 30-yr conforming, ngày) cho lãi (trung bình 7 ngày tới thứ Năm, như Tập 1).
Bản ghim hồ sơ topics-r2/machine/debt-2/sources.json (URL có coed=) được tải lại vào raw/dossier-pin/ để biết FRED có sửa số cũ không.
fhfa.gov bị proxy chặn → mọi file qua FRED. Tải bằng curl (urllib/requests bị proxy ngắt, Tập 4)."""
import datetime, hashlib, html, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(EP))
RAW, NORM, PIN = os.path.join(HERE, 'raw'), os.path.join(HERE, 'normalized'), os.path.join(HERE, 'raw', 'dossier-pin')
DOSSIER = os.path.join(ROOT, 'topics-r2', 'machine', 'debt-2', 'sources.json')
FRED = 'https://fred.stlouisfed.org/graph/fredgraph.csv?id='
SERIES = [  # (id, role, what)
    ('HPIPONM226N', 'primary', 'FHFA purchase-only house price index, United States, monthly, NSA (Jan 1991=100)'),
    ('MORTGAGE30US', 'primary', 'Freddie Mac PMMS 30-year fixed rate, weekly (Thursday), percent'),
    ('MSPUS', 'primary', 'Census/HUD median sales price of houses sold, United States, quarterly, USD (illustrative price only)'),
    ('CSUSHPINSA', 'crosscheck', 'S&P Cotality Case-Shiller U.S. National Home Price Index, monthly, NSA (crosscheck for HPIPONM226N)'),
    ('OBMMIC30YF', 'crosscheck', 'Optimal Blue 30-year fixed conforming rate, daily, percent (crosscheck for MORTGAGE30US)'),
]
TOL_HPI = 0.50   # điểm %: |Δ% tháng FHFA − Δ% tháng Case-Shiller|
TOL_RATE = 0.50  # điểm %: |PMMS tuần − trung bình Optimal Blue 7 ngày|
CMD = 'python3 episodes/ep005/data/fetch.py --verify'


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


def write_csv(name, header, data):
    os.makedirs(NORM, exist_ok=True)
    p = os.path.join(NORM, name)
    with open(p, 'w') as f:
        f.write(header + '\n' + ''.join(','.join(str(x) for x in r) + '\n' for r in data))
    return 'data/normalized/' + name


def normalize():
    """Đối chiếu tất định, dựng lại chỉ từ raw/. Trả (derived paths, mismatches, summary)."""
    mism, summ, out = [], {}, []
    # 1) chỉ số giá: % đổi so với tháng trước, các tháng có cả hai chuỗi
    a = dict(rows(os.path.join(RAW, 'HPIPONM226N.csv')))
    c = dict(rows(os.path.join(RAW, 'CSUSHPINSA.csv')))
    ms = sorted(m for m in a if m in c)
    pa, pc, n_ok, gaps = [], [], 0, []
    for i in range(1, len(ms)):
        m, q = ms[i], ms[i - 1]
        x, y = round(100 * (a[m] / a[q] - 1), 4), round(100 * (c[m] / c[q] - 1), 4)
        pa.append((m, x)); pc.append((m, y)); gaps.append(abs(x - y))
        if abs(x - y) > TOL_HPI:
            mism.append({'key': m, 'series': 'hpi_mom', 'note': f'HPIPONM226N {x:+.2f}% vs CSUSHPINSA {y:+.2f}% m/m ({x - y:+.2f} pp)'})
        else:
            n_ok += 1
    out.append(write_csv('hpipo_mom.csv', 'month,pct', pa))
    out.append(write_csv('csushpinsa_mom.csv', 'month,pct', pc))
    yoy = [abs(100 * (a[ms[i]] / a[ms[i - 12]] - 1) - 100 * (c[ms[i]] / c[ms[i - 12]] - 1)) for i in range(12, len(ms))]
    summ['hpi_mom'] = {'months': len(gaps), 'within': n_ok, 'maxGapPp': round(max(gaps), 3), 'from': ms[1], 'to': ms[-1],
                       'yoyInfo': {'months': len(yoy), 'withinHalfPp': sum(g <= 0.5 for g in yoy), 'medianGapPp': round(sorted(yoy)[len(yoy) // 2], 3),
                                   'maxGapPp': round(max(yoy), 3)},
                       'note': 'Case-Shiller is a 3-month moving average of repeat sales (all transactions), FHFA purchase-only covers GSE loans; '
                               'month-to-month timing differs. Robustness of the headline on Case-Shiller is in out/model.json raw.robust_cs_*.'}
    # 2) lãi: tuần PMMS vs trung bình Optimal Blue 7 ngày tới thứ Năm (từ 2017-01-06)
    pm = rows(os.path.join(RAW, 'MORTGAGE30US.csv'))
    ob = dict(rows(os.path.join(RAW, 'OBMMIC30YF.csv')))
    D, td = datetime.date.fromisoformat, datetime.timedelta
    cw, prim, gaps = [], [], []
    for d, v in pm:
        prim.append((d, v))
        if D(d) < D('2017-01-06'):
            continue
        wk = [ob[k] for k in ((D(d) - td(days=j)).isoformat() for j in range(7)) if k in ob]
        if not wk:
            continue
        m_ = round(sum(wk) / len(wk), 4)
        cw.append((d, m_)); gaps.append(abs(v - m_))
        if abs(v - m_) > TOL_RATE:
            mism.append({'key': d, 'series': 'mortgage30', 'note': f'MORTGAGE30US {v:.2f} vs OBMMIC30YF 7-day mean {m_:.3f} ({v - m_:+.3f} pp)'})
    out.append(write_csv('mortgage30_weekly.csv', 'date,rate', prim))
    out.append(write_csv('crosscheck_weekly.csv', 'week,obmmic30yf_weekmean', cw))
    summ['mortgage30'] = {'weeks': len(gaps), 'within': sum(g <= TOL_RATE for g in gaps), 'maxGapPp': round(max(gaps), 3),
                          'meanGapPp': round(sum(gaps) / len(gaps), 3), 'from': cw[0][0], 'to': cw[-1][0]}
    return out, mism, summ


def dossier_pins():
    """Tải lại đúng URL ghim của hồ sơ; so SHA và so phần đầu của file mới (số cũ có bị sửa không)."""
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
        curl(pinned, p)  # cùng bytes với bản ghim → --verify tái lập được
        assert rows(p)[-1] == last, sid
        page = f'https://fred.stlouisfed.org/series/{sid}'
        t = page_text(page)
        status = re.search(r'(Public Domain: Citation Requested|Copyrighted: Citation Required|Copyrighted: Pre-Approval Required)', t)
        upd = re.search(r'Updated: [A-Z][a-z]{2} \d{1,2}, \d{4} [\d:]+ [AP]M [A-Z]{3}', t)
        units = re.search(r'Units: (.{5,80}?) Frequency', t)
        files.append({'path': f'data/raw/{sid}.csv', 'role': role, 'series': sid, 'what': what,
                      'url': FRED + sid, 'pinnedUrl': pinned, 'seriesPage': page, 'sha256': sha(p), 'downloaded': today,
                      'bytes': os.path.getsize(p), 'inRepo': False, 'fetch': CMD,
                      'lastObservation': {'date': last[0], 'value': last[1], 'updatedQuote': upd.group(0) if upd else None,
                                          'unitsQuote': units.group(1).strip() if units else None, 'quotedFrom': page, 'retrieved': today},
                      'terms': {'quote': status.group(1) if status else None, 'url': page,
                                'citation': f'{sid}, retrieved from FRED, Federal Reserve Bank of St. Louis; {page}'}})
        print(sid, role, last, sha(p)[:16], status.group(1) if status else 'TERMS?')
    derived, mism, summ = normalize()
    pins = dossier_pins()
    src = {'files': files, 'mismatches': mism,
           'derived': [{'path': d, 'sha256': sha(os.path.join(EP, d)), 'from': 'data/fetch.py normalize() over data/raw/*'} for d in derived],
           'crosscheckSummary': summ, 'dossierPins': pins,
           'provisions': json.load(open(DOSSIER))['provisions'] + [{
               'cite': '12 U.S.C. 4902(c) (final termination, midpoint of amortization)',
               'url': 'https://www.law.cornell.edu/uscode/text/12/4902',
               'quote': 'in no case may such a requirement be imposed on residential mortgage transactions beyond the first day of the month '
                        'immediately following the date that is the midpoint of the amortization period of the loan if the mortgagor is current '
                        'on the payments required by the terms of the mortgage', 'retrieved': today}],
           '_about': f'FRED copies, not committed ({CMD} re-downloads from pinnedUrl and checks SHA-256). "Now" of the data: HPI and Case-Shiller '
                     f'to {files[0]["lastObservation"]["date"]}, PMMS to {files[1]["lastObservation"]["date"]}. CSUSHPINSA is '
                     '"Copyrighted: Pre-Approval Required": used only as an internal crosscheck, never shown on screen.'}
    json.dump(src, open(os.path.join(HERE, 'sources.json'), 'w'), indent=1, ensure_ascii=False)
    for pn in pins:
        print('dossier pin', pn['series'], 'SHA', 'OK' if pn['matchesDossier'] else 'KHÁC', '| prefix', 'OK' if pn['freshPrefixIdentical'] else 'SỬA',
              '| +obs', pn['freshAddsObservations'])
    for k, v in summ.items():
        print('crosscheck', k, {x: v[x] for x in v if x not in ('note',)})


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
