"""topics-r1 validity check, rules V0, V1, V2, V4, V5 (topics-r1/DESIGN.md "Kiểm hợp lệ"). V3 is a separate blind agent.

Adapted from m3/verify/verify.py for the topic dossier (card.json, result.json, sources.json, novelty.json,
claim-risk.md, calc.py). Written before any machine topic existed. Works on a frozen copy: never edits topics-r1/machine/.
For each thesis: re-downloads every series/document into topics-r1/verify/work/<id>/data/ (fresh, not the generator's copy),
compares SHA-256 (V1), runs the thesis calc.py against the fresh files (V2), checks the source page and terms quote
(V4), checks provisions on official domains (V5). Result: topics-r1/verify/out/<id>.json. Resumable (skips existing results;
--force re-runs). Network retries 2/4/8/16 s.
Usage: python3 topics-r1/verify/verify.py [ids...] [--force]
"""
import hashlib, html, io, json, os, re, shutil, subprocess, sys, time
from urllib.parse import urlparse
import requests

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))
import cardcheck  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MACHINE = os.path.join(ROOT, 'machine')
WORK = os.path.join(ROOT, 'verify', 'work')
OUT = os.path.join(ROOT, 'verify', 'out')
UA_FALLBACK = {'User-Agent': 'Mozilla/5.0'}  # default requests UA first; proxy drops some custom UAs
OFFICIAL = ('irs.gov', 'uscode.house.gov', 'law.cornell.edu', 'ecfr.gov', 'federalregister.gov', 'consumerfinance.gov',
            'fred.stlouisfed.org', 'stlouisfed.org', 'govinfo.gov', 'ssa.gov', 'congress.gov', 'treasury.gov')
REL_TOL, ABS_TOL = 0.005, 0.01


def get(url, binary=False):
    last = None
    for wait in [2, 4, 8, 16, None]:
        try:
            r = requests.get(url, timeout=(30, 120))
            if r.status_code == 403:
                r = requests.get(url, headers=UA_FALLBACK, timeout=(30, 120))
            if r.status_code in (429, 500, 502, 503, 504):
                raise requests.ConnectionError(f'HTTP {r.status_code}')
            return r
        except (requests.ConnectionError, requests.Timeout) as e:
            last = e
            if wait is None:
                break
            time.sleep(wait)
    raise last


def page_text(r):
    ctype = r.headers.get('content-type', '')
    if 'pdf' in ctype or r.content[:4] == b'%PDF':
        try:
            from pypdf import PdfReader
            t = ' '.join((p.extract_text() or '') for p in PdfReader(io.BytesIO(r.content)).pages)
        except Exception as e:  # noqa: BLE001
            return f'<<pdf-unreadable {e}>>'
    else:
        t = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', ' ', r.text)
        t = html.unescape(re.sub(r'(?s)<[^>]+>', ' ', t))
    return squash(t)


def squash(t):
    t = t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    t = t.replace('–', '-').replace('—', '-').replace('\xa0', ' ')
    return re.sub(r'\s+', ' ', t).strip().lower()


def quote_in(quote, text):
    q = squash(quote).strip(' ."\'')
    return bool(q) and q in text


def close(a, b):
    try:
        a, b = float(a), float(b)
    except (TypeError, ValueError):
        return str(a).strip().lower() == str(b).strip().lower()
    return abs(a - b) <= ABS_TOL or abs(a - b) <= REL_TOL * max(abs(a), abs(b))


def official(url):
    host = urlparse(url).hostname or ''
    return any(host == d or host.endswith('.' + d) for d in OFFICIAL)


def verify(tid):
    src = os.path.join(MACHINE, tid)
    th = {}
    v0 = {'ok': True, 'items': []}
    for f in ('card.json', 'calc.py', 'result.json', 'sources.json', 'novelty.json', 'claim-risk.md'):
        ok = os.path.exists(os.path.join(src, f))
        v0['items'].append({'file': f, 'ok': ok})
        v0['ok'] &= ok
    try:
        card = json.load(open(os.path.join(src, 'card.json')))
        viol = cardcheck.check(card)
        v0['items'].append({'cardcheck': viol, 'ok': not viol})
        v0['ok'] &= not viol
        result = json.load(open(os.path.join(src, 'result.json')))
        sources = json.load(open(os.path.join(src, 'sources.json')))
        th = {'numbers': result.get('numbers', []), 'series': sources.get('series', []),
              'provisions': sources.get('provisions', [])}
        nov = json.load(open(os.path.join(src, 'novelty.json')))
        qs = nov.get('queries', [])
        per_q = {q: sum(1 for r in nov.get('results', []) if r.get('query') == q and r.get('url')) for q in qs}
        nov_ok = (len(qs) >= 3 and all(n >= 1 for n in per_q.values())
                  and nov.get('verdict') in ('not-found', 'answered-without-data'))
        v0['items'].append({'novelty': {'queries': len(qs), 'resultsPerQuery': per_q, 'verdict': nov.get('verdict')},
                            'ok': nov_ok})
        v0['ok'] &= nov_ok
    except Exception as e:  # noqa: BLE001
        v0['ok'] = False
        v0['why'] = f'{type(e).__name__}: {e}'[:300]
    work = os.path.join(WORK, tid)
    shutil.rmtree(work, ignore_errors=True)
    os.makedirs(work)
    shutil.copy(os.path.join(src, 'calc.py'), work)
    res = {'id': tid, 'V0': v0, 'V1': {'ok': True, 'items': []}, 'V2': {'ok': True, 'items': []},
           'V4': {'ok': True, 'items': []}, 'V5': {'ok': True, 'items': []}}
    pages = {}

    def text_of(url):
        if url not in pages:
            try:
                r = get(url)
                pages[url] = (r.status_code, page_text(r) if r.status_code == 200 else '')
            except Exception as e:  # noqa: BLE001
                pages[url] = (f'ERR {type(e).__name__}', '')
        return pages[url]

    # V1 — fresh download, SHA compare
    for s in th.get('series', []):
        it = {'id': s.get('id'), 'file': s.get('file')}
        url = s.get('url')
        rel = s.get('file') or ''
        if not url or not rel:
            it.update(ok=False, why='missing url or file')
        else:
            dest = os.path.join(work, rel if not rel.startswith('/') else os.path.basename(rel))
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            try:
                r = get(url)
                if r.status_code != 200:
                    it.update(ok=False, why=f'HTTP {r.status_code}')
                else:
                    open(dest, 'wb').write(r.content)
                    sha = hashlib.sha256(r.content).hexdigest()
                    it.update(sha256=sha, declared=s.get('sha256'), shaMatch=(sha == s.get('sha256')), ok=True)
                    if sha != s.get('sha256'):
                        it['note'] = 'SHA lệch: V2 chạy trên tệp tải lại'
            except Exception as e:  # noqa: BLE001
                it.update(ok=False, why=f'{type(e).__name__}: {e}'[:200])
        res['V1']['items'].append(it)
        res['V1']['ok'] &= it['ok']
    if not th.get('series'):
        res['V1']['note'] = 'no series declared'

    # V2 — run calc.py on fresh files
    declared = {n['id']: n.get('value') for n in th.get('numbers', [])}
    got, p = None, None
    try:
        p = subprocess.run([sys.executable, 'calc.py'], cwd=work, capture_output=True, text=True, timeout=600)
        out = p.stdout.strip()
        try:
            got = json.loads(out)
        except ValueError:
            got = json.loads(out.splitlines()[-1])
    except Exception as e:  # noqa: BLE001
        res['V2'].update(ok=False, why=f'calc.py failed: {type(e).__name__}: {e}'[:300],
                         stderr=(p.stderr[-600:] if p is not None else ''))
    if got is not None:
        for k, v in declared.items():
            ok = k in got and close(got[k], v)
            res['V2']['items'].append({'id': k, 'declared': v, 'recomputed': got.get(k), 'ok': ok})
            res['V2']['ok'] &= ok
        if not declared:
            res['V2'].update(ok=False, why='no numbers declared')

    # V4 — source page exists, terms quote present
    for s in th.get('series', []):
        it = {'id': s.get('id')}
        page = s.get('seriesPage') or s.get('url')
        st, _ = text_of(page)
        terms = s.get('terms') or {}
        tst, ttxt = text_of(terms.get('url', '')) if terms.get('url') else ('no terms url', '')
        it.update(page=page, pageStatus=st, termsUrl=terms.get('url'), termsStatus=tst,
                  quoteFound=quote_in(terms.get('quote', ''), ttxt))
        it['ok'] = st == 200 and tst == 200 and it['quoteFound']
        res['V4']['items'].append(it)
        res['V4']['ok'] &= it['ok']
    if not th.get('series'):
        res['V4'].update(ok=False, why='no sources declared')

    # V5 — provisions on official pages, quote present
    for pv in th.get('provisions', []):
        url = pv.get('url', '')
        st, txt = text_of(url) if url else ('no url', '')
        it = {'cite': pv.get('cite'), 'url': url, 'official': official(url), 'status': st,
              'quoteFound': quote_in(pv.get('quote', ''), txt)}
        it['ok'] = it['official'] and st == 200 and it['quoteFound']
        res['V5']['items'].append(it)
        res['V5']['ok'] &= it['ok']
    if not th.get('provisions'):
        res['V5']['note'] = 'không viện điều luật: không áp dụng'

    res['ok_V01245'] = all(res[k]['ok'] for k in ('V0', 'V1', 'V2', 'V4', 'V5'))
    return res


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    force = '--force' in sys.argv
    os.makedirs(OUT, exist_ok=True)
    ids = args or sorted(d for d in os.listdir(MACHINE) if os.path.isdir(os.path.join(MACHINE, d)))
    for i, tid in enumerate(ids, 1):
        out = os.path.join(OUT, f'{tid}.json')
        if os.path.exists(out) and not force:
            print(f'[{i}/{len(ids)}] {tid} done, skip', flush=True)
            continue
        t0 = time.time()
        r = verify(tid)
        json.dump(r, open(out, 'w'), indent=1, ensure_ascii=False)
        print(f'[{i}/{len(ids)}] {tid} V0={r["V0"]["ok"]} V1={r["V1"]["ok"]} V2={r["V2"]["ok"]} V4={r["V4"]["ok"]} V5={r["V5"]["ok"]} '
              f'({time.time() - t0:.0f}s)', flush=True)


if __name__ == '__main__':
    main()
