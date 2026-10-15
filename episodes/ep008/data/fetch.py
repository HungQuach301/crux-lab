"""Tập 8 (Việc 0): tải lại 4 chuỗi FRED của hồ sơ topics-r2/machine/rent-buy-1 — bản ghim (coed hồ sơ) để so SHA với hồ sơ, và bản mới nhất.
Dữ liệu không commit (.gitignore: episodes/*/data/raw/). Ghi data/sources.json (SHA, URL, ngày tải, quan sát cuối, điều khoản chép từ hồ sơ).

    python3 episodes/ep008/data/fetch.py"""
import datetime, hashlib, json, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
DOSSIER = os.path.join(ROOT, 'topics-r2', 'machine', 'rent-buy-1', 'sources.json')
RAW, PIN = os.path.join(HERE, 'raw'), os.path.join(HERE, 'raw', 'dossier-pin')
FRED = 'https://fred.stlouisfed.org/graph/fredgraph.csv?id='


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def get(url, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    subprocess.run(['curl', '-sSf', '-m', '60', '-o', path, url], check=True)
    return path


def main():
    dos = json.load(open(DOSSIER))
    today = datetime.date.today().isoformat()
    out = {'dataNow': {}, 'series': [], 'provisions': dos['provisions'], 'notUsed': dos['notUsed'], 'pinCheck': []}
    for s in dos['series']:
        pin = get(s['url'], os.path.join(PIN, s['id'] + '.csv'))
        ok = sha(pin) == s['sha256']
        out['pinCheck'].append({'id': s['id'], 'pinnedUrl': s['url'], 'dossierSha': s['sha256'], 'refetchSha': sha(pin), 'match': ok})
        new = get(FRED + s['id'], os.path.join(RAW, s['id'] + '.csv'))
        rows = [l.split(',') for l in open(new).read().strip().splitlines()[1:]]
        last = [r for r in rows if r[1].strip() not in ('', '.')][-1][0]
        prefix = open(new).read().startswith(open(pin).read().rstrip('\n').rsplit('\n', 1)[0])
        d = dict(s, url=FRED + s['id'], pinnedUrl=s['url'], file='data/raw/%s.csv' % s['id'], sha256=sha(new),
                 bytes=os.path.getsize(new), retrieved=today, lastObservation=last, pinPrefixOfNew=prefix)
        out['series'].append(d)
    out['dataNow'] = {s['id']: s['lastObservation'] for s in out['series']}
    json.dump(out, open(os.path.join(HERE, 'sources.json'), 'w'), indent=1, ensure_ascii=False)
    for p in out['pinCheck']:
        print(p['id'], 'SHA ghim khớp hồ sơ' if p['match'] else 'SHA ghim LỆCH hồ sơ')
    for s in out['series']:
        print(s['id'], 'mới nhất', s['lastObservation'], 'bản ghim là tiền tố:', s['pinPrefixOfNew'])


if __name__ == '__main__':
    main()
