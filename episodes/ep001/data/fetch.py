"""Episode 1 data: download the raw files, record SHA-256, URL, download date and the terms of use (quoted verbatim
from the pages fetched in the same run), and write data/sources.json (DX-H4) and data/normalized/*.csv.

    python3 episodes/ep001/data/fetch.py            # re-download everything
    python3 episodes/ep001/data/fetch.py --verify   # recompute SHA-256 of the committed files against sources.json

Primary: FRED MORTGAGE30US (Freddie Mac PMMS, 30-year fixed, weekly since 1971-04-02).
Cross-check (DX-H5): FRED OBMMIC30YF (Optimal Blue 30-year fixed conforming, daily since 2017-01-03), a different
survey (locked rates on actual loans), compared as weekly means; the tolerance and every week outside it are listed.
HMDA closing costs (ffiec.cfpb.gov): NOT downloadable from this environment, see data/HMDA-ACCESS.md.
"""
import datetime
import hashlib
import html
import json
import os
import re
import sys

import requests

HERE = os.path.dirname(os.path.abspath(__file__))
RAW, NORM = os.path.join(HERE, 'raw'), os.path.join(HERE, 'normalized')
SERIES = {
    'MORTGAGE30US': 'primary',
    'OBMMIC30YF': 'crosscheck',
}
LEGAL = 'https://fred.stlouisfed.org/legal/'


def text_of(url):
    t = requests.get(url, timeout=60).text
    t = re.sub(r'<script.*?</script>|<style.*?</style>', '', t, flags=re.S)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', t)))


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def verify():
    src = json.load(open(os.path.join(HERE, 'sources.json')))
    bad = [f['path'] for f in src['files'] if sha(os.path.join(HERE, '..', f['path'])) != f['sha256']]
    print('sha256 mismatches:', bad or 'none')
    return not bad


def main():
    os.makedirs(RAW, exist_ok=True)
    os.makedirs(NORM, exist_ok=True)
    today = datetime.date.today().isoformat()
    legal = text_of(LEGAL)
    i = legal.find('Copyrighted: Citation required')
    legal_q = legal[i:legal.find('Link to these series', i)].strip()
    j = legal.find('Redistribute any third party')
    prohibited_q = legal[j:legal.find('.', j) + 1].strip()
    files = []
    for sid, role in SERIES.items():
        url = f'https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}'
        r = requests.get(url, timeout=120)
        r.raise_for_status()
        p = os.path.join(RAW, f'{sid}.csv')
        open(p, 'wb').write(r.content)
        page = text_of(f'https://fred.stlouisfed.org/series/{sid}')
        k = page.find('Notes:', page.find('Frequency:'))
        notes_q = page[k:page.find('Suggested Citation', k)].strip()
        m = re.search(r'Suggested Citation: (.*?https://fred\.stlouisfed\.org/series/\w+)', page)
        status = re.search(r'Copyrighted: [A-Za-z ]+?(?= |$)|Public Domain: [A-Za-z ]+?(?= |$)', page)
        files.append({'path': os.path.relpath(p, os.path.join(HERE, '..')), 'role': role, 'series': sid, 'url': url,
                      'seriesPage': f'https://fred.stlouisfed.org/series/{sid}', 'sha256': sha(p), 'downloaded': today,
                      'bytes': len(r.content),
                      'terms': {'quote': notes_q, 'url': f'https://fred.stlouisfed.org/series/{sid}#notes',
                                'fredCopyrightStatus': 'Copyrighted: Citation Required' if 'itation' in (status.group(0) if status else 'itation') else status.group(0),
                                'fredLegalQuote': legal_q, 'fredLegalProhibitedQuote': prohibited_q, 'fredLegalUrl': LEGAL,
                                'suggestedCitation': m.group(1) if m else None}})
    # normalized weekly primary and weekly means of the cross-check
    rows = [l.split(',') for l in open(os.path.join(RAW, 'MORTGAGE30US.csv')).read().strip().splitlines()[1:]]
    prim = [(d, float(v)) for d, v in rows if v not in ('', '.')]
    with open(os.path.join(NORM, 'mortgage30_weekly.csv'), 'w') as f:
        f.write('date,rate\n' + ''.join(f'{d},{v}\n' for d, v in prim))
    rows = [l.split(',') for l in open(os.path.join(RAW, 'OBMMIC30YF.csv')).read().strip().splitlines()[1:]]
    ob = {d: float(v) for d, v in rows if v not in ('', '.')}
    D = datetime.date.fromisoformat
    cmp_, mism = [], []
    TOL = 0.50
    for d, v in prim:
        e = D(d)
        if e < D('2017-01-06'):
            continue
        wk = [ob[(e - datetime.timedelta(days=k)).isoformat()] for k in range(0, 7) if (e - datetime.timedelta(days=k)).isoformat() in ob]
        if not wk:
            continue
        m_ = sum(wk) / len(wk)
        cmp_.append((d, v, round(m_, 3), round(v - m_, 3)))
        if abs(v - m_) > TOL:
            mism.append({'week': d, 'series': 'MORTGAGE30US vs OBMMIC30YF', 'note': f'{v:.2f} vs {m_:.3f} ({v - m_:+.3f} pp)'})
    with open(os.path.join(NORM, 'crosscheck_weekly.csv'), 'w') as f:
        f.write('week,mortgage30us,obmmic30yf_weekmean,diff_pp\n' + ''.join(f'{a},{b},{c},{d}\n' for a, b, c, d in cmp_))
    diffs = [abs(x[3]) for x in cmp_]
    src = {'files': files,
           'tolerance': {'mortgage_rate_pp': TOL, 'basis': 'weekly PMMS rate vs mean of Optimal Blue daily rates of the 7 days ending that Thursday'},
           'crosscheckSummary': {'weeks': len(cmp_), 'meanAbsDiffPp': round(sum(diffs) / len(diffs), 3), 'maxAbsDiffPp': round(max(diffs), 3),
                                 'outsideTolerance': len(mism)},
           'mismatches': mism,
           'notUsed': [{'source': 'HMDA loan-level data (ffiec.cfpb.gov / files.ffiec.cfpb.gov / s3 cfpb-hmda-public)',
                        'status': 'not reachable from this environment (proxy 403 / S3 AccessDenied), see data/HMDA-ACCESS.md'}]}
    json.dump(src, open(os.path.join(HERE, 'sources.json'), 'w'), indent=1, ensure_ascii=False)
    print(json.dumps(src['crosscheckSummary']), [(f['series'], f['sha256'][:12], f['bytes']) for f in files])


if __name__ == '__main__':
    sys.exit(0 if verify() else 1) if '--verify' in sys.argv else main()
