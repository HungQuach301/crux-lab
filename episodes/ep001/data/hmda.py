"""Episode 1: closing costs of refinance loans from HMDA (CFPB/FFIEC), read as a stream; the raw file is NOT stored.

    python3 episodes/ep001/data/hmda.py [--years 2024,2023,2022] [--states ...]
    python3 episodes/ep001/data/hmda.py --conforming 2025 [--purchase-rates 2023]   # large-character band + context

For every year the Data Browser CSV is requested with the server-side filters
    actions_taken=1 (loan originated), loan_purposes=31,32 (refinance, cash-out refinance) (the API takes at most two filters)
and every row is filtered again on our side: action_taken == 1, loan_purpose in {31, 32}, lien_status == 1,
loan_term == 360 (months), total_loan_costs and loan_amount numeric and > 0.

The stream is hashed while it is read (SHA-256 of the exact bytes received), so the summary can cite the file it came
from; the file itself is not written to disk.

Aggregates (data/normalized/hmda_refi_costs.csv): per year x purpose group (refi 31, cash-out 32, all) x loan-size band
(and "all"): count, 25th/50th/75th percentile of total_loan_costs in dollars (nominal, data year) and of
total_loan_costs / loan_amount in percent. Percentiles: numpy linear interpolation on every kept row (exact, no binning).

Field meaning (HMDA filing instructions): total_loan_costs = "Total Loan Costs" of the Closing Disclosure (Section D:
origination charges, services borrower did and did not shop for), reported for loans subject to the TRID rule (not quoted from a reachable page: see hmda-sources.json);
loan_amount in the public data is binned (observed: values end in 5,000, e.g. 115000, 375000), so its medians are bin
midpoints. Quoted field definitions and the open terms-of-use item are in data/hmda-sources.json.
"""
import csv
import datetime
import hashlib
import io
import json
import os
import sys
import time

import numpy as np
import requests

HERE = os.path.dirname(os.path.abspath(__file__))
NORM = os.path.join(HERE, 'normalized')
BASE = 'https://ffiec.cfpb.gov/v2/data-browser-api/view/{scope}csv?{geo}years={y}&actions_taken=1&loan_purposes=31,32'
BANDS = [(0, 150_000, 'under $150k'), (150_000, 300_000, '$150k-$300k'), (300_000, 450_000, '$300k-$450k'),
         (450_000, 750_000, '$450k-$750k'), (750_000, 1e12, '$750k and over')]


def stream_year(year, states=None):
    url = BASE.format(scope='' if states else 'nationwide/', geo=f'states={states}&' if states else '', y=year)
    t0 = time.time()
    r = requests.get(url, stream=True, timeout=600, allow_redirects=True)
    r.raise_for_status()
    h = hashlib.sha256()
    nbytes = 0
    kept = {'amount': [], 'cost': [], 'purpose': []}
    seen = 0
    reasons = {'term': 0, 'lien': 0, 'purpose': 0, 'action': 0, 'cost_missing': 0}

    def chunks():
        nonlocal nbytes
        for c in r.iter_content(chunk_size=1 << 20):
            h.update(c)
            nbytes += len(c)
            yield c
    text = io.TextIOWrapper(_Iter(chunks()), encoding='utf-8', newline='')
    rd = csv.DictReader(text)
    for row in rd:
        seen += 1
        if row.get('action_taken') != '1':
            reasons['action'] += 1; continue
        if row.get('loan_purpose') not in ('31', '32'):
            reasons['purpose'] += 1; continue
        if row.get('lien_status') != '1':
            reasons['lien'] += 1; continue
        if row.get('loan_term') != '360':
            reasons['term'] += 1; continue
        try:
            a, c = float(row['loan_amount']), float(row['total_loan_costs'])
        except (ValueError, KeyError, TypeError):
            reasons['cost_missing'] += 1; continue
        if not (a > 0 and c > 0):
            reasons['cost_missing'] += 1; continue
        kept['amount'].append(a); kept['cost'].append(c); kept['purpose'].append(int(row['loan_purpose']))
    return {'url': url, 'finalUrl': r.url, 'sha256': h.hexdigest(), 'bytes': nbytes, 'rowsRead': seen, 'excluded': reasons,
            'seconds': round(time.time() - t0, 1)}, {k: np.array(v) for k, v in kept.items()}


class _Iter(io.RawIOBase):
    def __init__(self, it):
        self.it, self.buf = it, b''

    def readable(self):
        return True

    def readinto(self, b):
        while not self.buf:
            try:
                self.buf = next(self.it)
            except StopIteration:
                return 0
        n = min(len(b), len(self.buf))
        b[:n] = self.buf[:n]
        self.buf = self.buf[n:]
        return n


def pct(x):
    return [float(np.percentile(x, q)) for q in (25, 50, 75)] if len(x) else [None] * 3


def summarize(year, d):
    rows = []
    groups = [('refinance (31)', d['purpose'] == 31), ('cash-out refinance (32)', d['purpose'] == 32), ('all refinance (31+32)', np.ones(len(d['purpose']), bool))]
    for gname, gm in groups:
        for lo, hi, bname in [(0, 1e12, 'all sizes')] + BANDS:
            m = gm & (d['amount'] >= lo) & (d['amount'] < hi)
            c, a = d['cost'][m], d['amount'][m]
            usd, share = pct(c), pct(100 * c / a) if len(c) else [None] * 3
            rows.append({'year': year, 'purpose': gname, 'loanSize': bname, 'n': int(m.sum()),
                         'cost_p25_usd': usd[0], 'cost_p50_usd': usd[1], 'cost_p75_usd': usd[2],
                         'cost_p25_pct': share[0], 'cost_p50_pct': share[1], 'cost_p75_pct': share[2],
                         'loan_p50_usd': float(np.median(a)) if len(a) else None})
    return rows


# ------------------------------------------------------------------ conforming-limit bands (ep001 large character) + context
EXT = 'https://ffiec.cfpb.gov/v2/data-browser-api/view/nationwide/csv?years={y}&actions_taken=1&loan_purposes={p}'
# Upper conforming band for the large character: loan_purpose 31, same filters as above, HMDA flag
# conforming_loan_limit == 'C' (at or below the county's limit) AND loan_amount < CONF_HI so the ORIGINAL October 2023 loan
# would also sit under the 2023 one-unit baseline ($726,200, FHFA): loan_amount is published as 10k-bin midpoints, so
# < 720,000 keeps bins 600-610k ... 710-720k only. CONF_BANDS lower edges are analysis parameters.
CONF_HI = 720_000
CONF_BANDS = [(450_000, CONF_HI, '$450k-<$720k, conforming (C)'), (600_000, CONF_HI, '$600k-<$720k, conforming (C)')]


def stream_ext(year, purposes):
    """Stream one year (server filters actions_taken=1, loan_purposes=`purposes`), keep first-lien 360-month rows with the
    columns needed for the conforming bands and the context facts. Returns (info, arrays)."""
    url = EXT.format(y=year, p=purposes)
    t0 = time.time()
    r = requests.get(url, stream=True, timeout=600, allow_redirects=True)
    r.raise_for_status()
    h = hashlib.sha256(); nbytes = 0; seen = 0
    K = {'purpose': [], 'amount': [], 'cost': [], 'rate': [], 'cll': [], 'ltype': []}

    def chunks():
        nonlocal nbytes
        for c in r.iter_content(chunk_size=1 << 20):
            h.update(c); nbytes += len(c); yield c
    for row in csv.DictReader(io.TextIOWrapper(_Iter(chunks()), encoding='utf-8', newline='')):
        seen += 1
        if row.get('action_taken') != '1' or row.get('lien_status') != '1' or row.get('loan_term') != '360':
            continue
        try:
            a = float(row['loan_amount'])
        except (ValueError, KeyError, TypeError):
            continue
        def num(k):
            try:
                return float(row[k])
            except (ValueError, KeyError, TypeError):
                return np.nan
        K['purpose'].append(int(row['loan_purpose'])); K['amount'].append(a); K['cost'].append(num('total_loan_costs'))
        K['rate'].append(num('interest_rate')); K['cll'].append(row.get('conforming_loan_limit', '')); K['ltype'].append(row.get('loan_type', ''))
    info = {'url': url, 'finalUrl': r.url, 'sha256': h.hexdigest(), 'bytes': nbytes, 'rowsRead': seen, 'rowsKept': len(K['amount']),
            'seconds': round(time.time() - t0, 1), 'year': year, 'downloaded': datetime.date.today().isoformat(), 'stored': False,
            'filters': {'server': f'actions_taken=1, loan_purposes={purposes}, nationwide', 'client': 'action_taken=1, lien_status=1, loan_term=360'}}
    return info, {k: np.array(v) for k, v in K.items()}


def conforming_main(year):
    info, d = stream_ext(year, '31')
    rows = []
    base = (d['purpose'] == 31) & (d['amount'] > 0) & (d['cost'] > 0)
    for lo, hi, name in CONF_BANDS + [(0, 1e12, 'all sizes, conforming (C)'), (750_000, 1e12, '$750k and over, conforming (C)'), (750_000, 1e12, '$750k and over, nonconforming (NC)')]:
        flag = 'NC' if '(NC)' in name else 'C'
        m = base & (d['cll'] == flag) & (d['amount'] >= lo) & (d['amount'] < hi)
        c, a = d['cost'][m], d['amount'][m]
        usd, share = pct(c), pct(100 * c / a)
        rows.append({'year': year, 'purpose': 'refinance (31)', 'loanSize': name, 'n': int(m.sum()), 'cost_p25_usd': usd[0], 'cost_p50_usd': usd[1], 'cost_p75_usd': usd[2],
                     'cost_p25_pct': share[0], 'cost_p50_pct': share[1], 'cost_p75_pct': share[2], 'loan_p50_usd': float(np.median(a)) if len(a) else None,
                     'loan_max_usd': float(a.max()) if len(a) else None, 'conventional_share_pct': 100 * float(np.mean(d['ltype'][m] == '1')) if len(a) else None})
    # context: the whole kept population and the interest rates of the new loans
    ctx = {'n_all_31': int(base.sum()), 'n_31_flag': {f: int((base & (d['cll'] == f)).sum()) for f in ('C', 'NC', 'U')},
           'n_31_any_cost': int(((d['purpose'] == 31)).sum()),
           'rate_31_p50': float(np.nanmedian(d['rate'][base])), 'rate_31_valid': int(np.isfinite(d['rate'][base]).sum()),
           'conventional_share_31_pct': 100 * float(np.mean(d['ltype'][base] == '1'))}
    with open(os.path.join(NORM, 'hmda_refi31_conforming.csv'), 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader()
        for r_ in rows:
            w.writerow({k: (round(v, 4) if isinstance(v, float) else v) for k, v in r_.items()})
    return info, ctx


def purchase_rates_main(year):
    """Context: first-lien 30-year home-purchase originations of `year` by interest rate (how many borrowed at >= 7%)."""
    info, d = stream_ext(year, '1')
    m = (d['purpose'] == 1) & np.isfinite(d['rate']) & (d['rate'] > 0)
    r_ = d['rate'][m]
    ctx = {'n_purchase_rate_valid': int(m.sum()), 'n_purchase_kept': int((d['purpose'] == 1).sum()),
           'share_ge_7_pct': 100 * float(np.mean(r_ >= 7.0)), 'share_ge_6_pct': 100 * float(np.mean(r_ >= 6.0)),
           'n_ge_7': int((r_ >= 7.0).sum()), 'rate_p50': float(np.median(r_))}
    return info, ctx


def ext_main(args):
    src_p = os.path.join(HERE, 'hmda-sources.json')
    meta = json.load(open(src_p))
    meta.setdefault('extFiles', []); meta.setdefault('context', {})
    jobs = []
    if '--conforming' in args:
        jobs.append(('conforming', int(args[args.index('--conforming') + 1]), conforming_main))
    if '--purchase-rates' in args:
        jobs.append(('purchaseRates', int(args[args.index('--purchase-rates') + 1]), purchase_rates_main))
    for key, y, fn in jobs:
        info, ctx = fn(y)
        info['use'] = key
        print(json.dumps(info), json.dumps(ctx), flush=True)
        meta['extFiles'] = [f for f in meta['extFiles'] if not (f['use'] == key and f['year'] == y)] + [info]
        meta['context'][f'{key}{y}'] = {k: (round(v, 4) if isinstance(v, float) else v) for k, v in ctx.items()}
        json.dump(meta, open(src_p, 'w'), indent=1)


def main():
    args = sys.argv[1:]
    if '--conforming' in args or '--purchase-rates' in args:
        return ext_main(args)
    years = [int(y) for y in (args[args.index('--years') + 1] if '--years' in args else '2024,2023,2022').split(',')]
    states = args[args.index('--states') + 1] if '--states' in args else None
    os.makedirs(NORM, exist_ok=True)
    out_p = os.path.join(NORM, 'hmda_refi_costs.csv')
    src_p = os.path.join(HERE, 'hmda-sources.json')
    rows = [r for r in csv.DictReader(open(out_p))] if os.path.exists(out_p) else []
    meta = json.load(open(src_p)) if os.path.exists(src_p) else {'files': []}
    for y in years:
        info, d = stream_year(y, states)
        info.update({'year': y, 'downloaded': datetime.date.today().isoformat(), 'rowsKept': int(len(d['cost'])), 'stored': False,
                     'filters': {'server': 'actions_taken=1, loan_purposes=31,32' + (f', states={states}' if states else ', nationwide'),
                                 'client': 'action_taken=1, loan_purpose in {31,32}, lien_status=1, loan_term=360, total_loan_costs>0, loan_amount>0'}})
        print(json.dumps(info), flush=True)
        rows = [r for r in rows if str(r['year']) != str(y)] + summarize(y, d)
        meta['files'] = [f for f in meta['files'] if f['year'] != y] + [info]
        with open(out_p, 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=list(summarize(y, d)[0].keys()))
            w.writeheader()
            for r in sorted(rows, key=lambda r: (-int(r['year']), r['purpose'], r['loanSize'])):
                w.writerow({k: (round(float(v), 4) if isinstance(v, float) else v) for k, v in r.items()})
        json.dump(meta, open(src_p, 'w'), indent=1)


if __name__ == '__main__':
    main()
