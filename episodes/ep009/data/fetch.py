"""Tập 9 (Việc 0): tải dữ liệu — 4 chuỗi FRED của Tập 8 ở ĐÚNG bản ghim (coed, SHA của Tập 8, để con phố Tập 8 tái lập trùng)
+ chuỗi tổng lợi nhuận cổ phiếu Mỹ (Kenneth R. French Data Library, Fama/French 3 Factors monthly: Mkt-RF + RF; dữ liệu dựng từ CRSP)
+ đối chiếu độc lập (Robert J. Shiller, ie_data.xls: S&P Composite giá + cổ tức, chỉ đến 2023-09 ở URL Yale — dùng để so, không vào lời).
Dữ liệu không commit (.gitignore: episodes/*/data/raw/). Ghi data/sources.json (SHA, URL, ngày tải, quan sát cuối, trích điều khoản).

    python3 episodes/ep009/data/fetch.py            # tải + ghi sources.json
    python3 episodes/ep009/data/fetch.py --verify   # tải lại, so SHA với sources.json (thoát 1 khi lệch)
"""
import datetime, hashlib, io, json, os, subprocess, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, 'raw')
EP8 = json.load(open(os.path.join(HERE, 'ep008-sources.json')))   # chép từ origin/ep008 episodes/ep008/data/sources.json
FRENCH = 'https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip'
FRENCH_PAGE = 'https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html'
SHILLER = 'http://www.econ.yale.edu/~shiller/data/ie_data.xls'


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def get(url, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    subprocess.run(['curl', '-sSfL', '-m', '120', '-o', path, url], check=True)
    return path


def main(verify=False):
    old = json.load(open(os.path.join(HERE, 'sources.json'))) if verify else None
    today = datetime.date.today().isoformat()
    out = {'series': [], 'provisions': EP8['provisions'], 'notUsed': [], 'files': []}
    for s in EP8['files']:
        p = get(s['url'], os.path.join(RAW, s['series'] + '.csv'))
        out['files'].append(dict(s, path='data/raw/%s.csv' % s['series'], downloaded=today, sha256=sha(p), ep008Sha=s['sha256'],
                                 matchEp008=sha(p) == s['sha256']))
    z = get(FRENCH, os.path.join(RAW, 'F-F_Research_Data_Factors_CSV.zip'))
    with zipfile.ZipFile(z) as zf:
        name = [n for n in zf.namelist() if n.lower().endswith('.csv')][0]
        txt = zf.read(name).decode('latin-1')
    open(os.path.join(RAW, 'ff3_monthly.csv'), 'w').write(txt)
    head = txt.splitlines()[0].strip()
    rows = [l.split(',')[0].strip() for l in txt.splitlines() if l[:6].strip().isdigit() and len(l.split(',')[0].strip()) == 6]
    out['files'].append({
        'path': 'data/raw/F-F_Research_Data_Factors_CSV.zip', 'series': 'FF3_MONTHLY', 'role': 'primary', 'url': FRENCH, 'downloaded': today,
        'sha256': sha(z), 'lastObservation': rows[-1][:4] + '-' + rows[-1][4:], 'fileHeader': head,
        'what': 'Fama/French 3 Factors, monthly, percent. US stock market total return (dividends reinvested) = Mkt-RF + RF: value-weight return of '
                'all CRSP firms incorporated in the US and listed on the NYSE, AMEX, or NASDAQ. Before fees and taxes.',
        'terms': {'quote': 'Copyright Eugene F. Fama and Kenneth R. French (page footer). No license text on the page; data offered for free '
                           'download without registration.', 'url': FRENCH_PAGE,
                  'assessment': 'Facts (monthly returns) used to compute derived results; raw file not committed or redistributed; on screen '
                                'and in the description: "Source: Kenneth R. French Data Library (CRSP data)". Owner decides at G1 (RIGHTS D-FRENCH).'},
    })
    x = get(SHILLER, os.path.join(RAW, 'ie_data.xls'))
    out['files'].append({
        'path': 'data/raw/ie_data.xls', 'series': 'SHILLER_IE', 'role': 'crosscheck', 'url': SHILLER, 'downloaded': today, 'sha256': sha(x),
        'lastObservation': '2023-09',
        'what': 'Robert J. Shiller, "Stock Market Data Used in Irrational Exuberance": S&P Composite monthly price P and dividend D. Used only to '
                'cross-check the French total return 1991-01..2023-09; not spoken, not on screen.',
        'terms': {'quote': 'The data and CAPE Ratio on this spreadsheet were developed by Robert J. Shiller using various public sources. Neither '
                           'Robert J. Shiller nor any affiliates or consultants, are registered investment advisers and do not guarantee the '
                           'accuracy or completeness of the CAPE Ratio here, or any data or methodology either included therein or upon which '
                           'it is based.', 'url': SHILLER, 'sheet': 'Disclaimer'},
    })
    out['notUsed'] = [
        {'id': 'SP500 (FRED)', 'why': 'Copyrighted: Pre-Approval Required on FRED, and price only (no dividends), last 10 years only.'},
        {'id': 'Damodaran histretSP.xls', 'why': 'Annual only; the file at the public URL was last updated 2021 (44561).'},
        {'id': 'shillerdata.com', 'why': 'Not reachable from this container (2026-10-15); the Yale copy stops at 2023-09.'},
    ]
    out['dataNow'] = {f['series']: f.get('lastObservation') or EP8['dataNow'].get(f['series']) for f in out['files']}
    if verify:
        bad = [f['series'] for f, o in zip(out['files'], old['files']) if f['sha256'] != o['sha256']]
        print('SHA lệch:', bad or 'không'); sys.exit(1 if bad else 0)
    json.dump(out, open(os.path.join(HERE, 'sources.json'), 'w'), indent=1, ensure_ascii=False)
    for f in out['files']:
        print(f['series'], f['sha256'][:16], f.get('lastObservation', ''), 'trùng Tập 8' if f.get('matchEp008') else '')


if __name__ == '__main__':
    main('--verify' in sys.argv)
