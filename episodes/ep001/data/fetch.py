"""Episode 1 data: download the raw files, record SHA-256, URL, download date and the terms of use (quoted verbatim
from the pages fetched in the same run), and write data/sources.json (DX-H4) and data/normalized/*.csv.

    python3 episodes/ep001/data/fetch.py            # re-download everything (new vintage: rewrites sources.json)
    python3 episodes/ep001/data/fetch.py --verify   # restore the pinned files and check them against sources.json

The FRED files are NOT stored in the repo (the repo is public; FRED/Freddie Mac and Optimal Blue data are copyrighted, not public
domain: amendments.md E1-A2). --verify works from a fresh clone: a raw file that is missing is downloaded again from its pinned URL
(`pinnedUrl` = the FRED CSV cut at the recorded last observation, `coed=`, so a later FRED release does not change the bytes), its
SHA-256 must equal the one in sources.json, and the normalized files derived from it (data/normalized/mortgage30_weekly.csv,
crosscheck_weekly.csv) are rebuilt from the raw files and checked against their recorded SHA-256 too. Exit code 0 = everything matches.

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


EP = os.path.join(HERE, '..')
FETCH_CMD = 'python3 episodes/ep001/data/fetch.py --verify'
STORAGE = ('not stored in the repo: the repo is public and this FRED series is copyrighted by its provider (FRED: "Copyrighted: Citation Required"), '
           'not public domain (amendments.md E1-A2); re-download with the fetch command, which checks the SHA-256 below')


def pinned_url(sid, last_date):
    """FRED CSV cut at the recorded last observation: the same bytes after later releases (unless FRED revises past values)."""
    return f'https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}&coed={last_date}'


def download(url, dest):
    r = requests.get(url, timeout=120)
    r.raise_for_status()
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, 'wb').write(r.content)
    return r


def verify():
    src = json.load(open(os.path.join(HERE, 'sources.json')))
    bad, fetched = [], []
    for f in src['files']:
        p = os.path.join(EP, f['path'])
        if not os.path.exists(p):
            url = f.get('pinnedUrl') or pinned_url(f['series'], f['latestObservation']['date'])
            print('missing, downloading', f['path'], '<-', url)
            download(url, p)
            fetched.append(f['path'])
        if sha(p) != f['sha256']:
            bad.append(f['path'])
    if not bad:
        want = {d['path']: d['sha256'] for d in src.get('derived', [])}
        if any(not os.path.exists(os.path.join(EP, q)) for q in want) or fetched:
            normalize()
            print('rebuilt normalized files from the raw files:', sorted(want))
        bad += [q for q, h in want.items() if sha(os.path.join(EP, q)) != h]
    print('downloaded:', fetched or 'none')
    print('sha256 mismatches:', bad or 'none')
    return not bad


def normalize():
    """data/normalized/mortgage30_weekly.csv (the primary, weekly, as published) and crosscheck_weekly.csv (each PMMS week vs the mean of the
    Optimal Blue daily rates of the 7 days ending that Thursday). Deterministic: rebuilt from data/raw/* alone."""
    os.makedirs(NORM, exist_ok=True)
    rows = [l.split(',') for l in open(os.path.join(RAW, 'MORTGAGE30US.csv')).read().strip().splitlines()[1:]]
    prim = [(d, float(v)) for d, v in rows if v not in ('', '.')]
    with open(os.path.join(NORM, 'mortgage30_weekly.csv'), 'w') as f:
        f.write('date,rate\n' + ''.join(f'{d},{v}\n' for d, v in prim))
    rows = [l.split(',') for l in open(os.path.join(RAW, 'OBMMIC30YF.csv')).read().strip().splitlines()[1:]]
    ob = {d: float(v) for d, v in rows if v not in ('', '.')}
    D = datetime.date.fromisoformat
    cmp_, mism = [], []
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
            mism.append({'week': d, 'key': d, 'series': 'mortgage30', 'note': f'MORTGAGE30US vs OBMMIC30YF: {v:.2f} vs {m_:.3f} ({v - m_:+.3f} pp)'})
    with open(os.path.join(NORM, 'crosscheck_weekly.csv'), 'w') as f:
        f.write('week,mortgage30us,obmmic30yf_weekmean,diff_pp\n' + ''.join(f'{a},{b},{c},{d}\n' for a, b, c, d in cmp_))
    return cmp_, mism


TOL = 0.50


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
        p = os.path.join(RAW, f'{sid}.csv')
        r = download(url, p)
        page = text_of(f'https://fred.stlouisfed.org/series/{sid}')
        k = page.find('Notes:', page.find('Frequency:'))
        notes_q = page[k:page.find('Suggested Citation', k)].strip()
        m = re.search(r'Suggested Citation: (.*?https://fred\.stlouisfed\.org/series/\w+)', page)
        status = re.search(r'Copyrighted: [A-Za-z ]+?(?= |$)|Public Domain: [A-Za-z ]+?(?= |$)', page)
        fq = re.search(r'Frequency: [^:]*?(?= Notes:| Fullscreen)', page)
        up = re.search(r'Updated: [A-Z][a-z]{2} \d{1,2}, \d{4} [\d:]+ [AP]M [A-Z]{3}', page)
        nr = re.search(r'Next Release Date: [A-Z][a-z]{2} \d{1,2}, \d{4}', page)
        last = [l.split(',') for l in r.text.strip().splitlines()[1:] if not l.endswith(',.') and not l.endswith(',')][-1]
        files.append({'path': os.path.relpath(p, EP), 'role': role, 'series': sid, 'url': url, 'pinnedUrl': pinned_url(sid, last[0]),
                      'inRepo': False, 'storage': STORAGE, 'fetch': FETCH_CMD,
                      'seriesPage': f'https://fred.stlouisfed.org/series/{sid}', 'sha256': sha(p), 'downloaded': today,
                      'bytes': len(r.content),
                      'latestObservation': {'date': last[0], 'value': last[1],
                                            'frequencyQuote': fq.group(0).strip() if fq else None,
                                            'updatedQuote': up.group(0) if up else None,
                                            'nextReleaseQuote': nr.group(0) if nr else None,
                                            'quotedFrom': f'https://fred.stlouisfed.org/series/{sid}', 'retrieved': today},
                      'terms': {'quote': notes_q, 'url': f'https://fred.stlouisfed.org/series/{sid}#notes',
                                'fredCopyrightStatus': 'Copyrighted: Citation Required' if 'itation' in (status.group(0) if status else 'itation') else status.group(0),
                                'fredLegalQuote': legal_q, 'fredLegalProhibitedQuote': prohibited_q, 'fredLegalUrl': LEGAL,
                                'suggestedCitation': m.group(1) if m else None}})
    cmp_, mism = normalize()
    diffs = [abs(x[3]) for x in cmp_]
    src = {'files': files,
           'tolerance': {'mortgage_rate_pp': TOL, 'basis': 'weekly PMMS rate vs mean of Optimal Blue daily rates of the 7 days ending that Thursday'},
           'crosscheckSummary': {'weeks': len(cmp_), 'meanAbsDiffPp': round(sum(diffs) / len(diffs), 3), 'maxAbsDiffPp': round(max(diffs), 3),
                                 'outsideTolerance': len(mism)},
           'mismatches': mism,
           'derived': [{'path': os.path.relpath(os.path.join(NORM, n), EP), 'from': ['data/raw/MORTGAGE30US.csv'] + (['data/raw/OBMMIC30YF.csv'] if 'cross' in n else []),
                        'sha256': sha(os.path.join(NORM, n)), 'inRepo': False, 'storage': 'not stored in the repo (verbatim copy of the FRED series); rebuilt from data/raw by the fetch command',
                        'fetch': FETCH_CMD} for n in ('mortgage30_weekly.csv', 'crosscheck_weekly.csv')],
           'storage': {'inRepo': False, 'why': 'public repo; FRED MORTGAGE30US (Freddie Mac) and OBMMIC30YF (Optimal Blue) are copyrighted, not public domain (amendments.md E1-A2)',
                       'fetch': FETCH_CMD, 'refresh': 'python3 episodes/ep001/data/fetch.py (new vintage; then python3 episodes/ep001/build.py)'},
           'notUsed': [{'source': 'HMDA loan-level data (ffiec.cfpb.gov / files.ffiec.cfpb.gov / s3 cfpb-hmda-public)',
                        'status': 'not a FRED file: streamed from ffiec.cfpb.gov (files.ffiec.cfpb.gov now reachable), not stored; SHA-256, URLs and terms in data/hmda-sources.json (HMDA-ACCESS.md is the earlier blocked-access record)'}]}
    json.dump(src, open(os.path.join(HERE, 'sources.json'), 'w'), indent=1, ensure_ascii=False)
    print(json.dumps(src['crosscheckSummary']), [(f['series'], f['sha256'][:12], f['bytes']) for f in files])


if __name__ == '__main__':
    sys.exit(0 if verify() else 1) if '--verify' in sys.argv else main()
