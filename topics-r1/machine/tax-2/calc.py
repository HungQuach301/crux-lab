"""tax-2: for a married couple who bought in 2000, the purchase price above which a home that appreciated like its
metro's house price index has a gain larger than the fixed $500,000 joint home-sale exclusion (2026 Q2 values),
and what the 1997 limit would be in today's dollars. Reads data/ only; prints one JSON object {id: value}."""
import csv, json, os

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
EXCL_JOINT = 500000   # joint-return limit (quoted in provisions)
EXCL_SINGLE = 250000  # single limit (quoted in provisions)
NOW = '2026-04-01'    # 2026 Q2, latest quarter in every file
BUY_YEAR = '2000'

METROS = {  # FHFA all-transactions index, metropolitan division / MSA code -> short name
    '31084': 'los_angeles', '41740': 'san_diego', '41884': 'san_francisco', '41940': 'san_jose',
    '42644': 'seattle', '14454': 'boston', '35614': 'new_york', '33124': 'miami',
    '19740': 'denver', '38060': 'phoenix', '19124': 'dallas', '16984': 'chicago',
}


def load(name):
    out = {}
    for row in list(csv.reader(open(os.path.join(D, name + '.csv'))))[1:]:
        if len(row) > 1 and row[1] not in ('', '.'):
            out[row[0]] = float(row[1])
    return out


def growth(s):
    base = [v for k, v in s.items() if k.startswith(BUY_YEAR)]
    assert len(base) == 4
    return s[NOW] / (sum(base) / 4)


out = {}
thr = {}
for code, name in METROS.items():
    g = growth(load(f'ATNHPIUS{code}Q'))
    out[f'growth_{name}'] = round(g, 4)
    thr[name] = EXCL_JOINT / (g - 1)
    out[f'threshold_joint_{name}_usd'] = round(thr[name], -2)
g_us = growth(load('USSTHPI'))
out['growth_us'] = round(g_us, 4)
out['threshold_joint_us_usd'] = round(EXCL_JOINT / (g_us - 1), -2)
out['threshold_single_us_usd'] = round(EXCL_SINGLE / (g_us - 1), -2)
out['threshold_joint_min_usd'] = round(min(thr.values()), -2)
out['threshold_joint_max_usd'] = round(max(thr.values()), -2)
out['metros_threshold_under_200k'] = sum(1 for v in thr.values() if v < 200000)
out['metros_threshold_under_300k'] = sum(1 for v in thr.values() if v < 300000)
cpi = load('CPIAUCNS')
out['cpi_1997_05'] = cpi['1997-05-01']
out['cpi_2026_08'] = cpi['2026-08-01']
out['excl_joint_1997_in_2026_usd'] = round(EXCL_JOINT * cpi['2026-08-01'] / cpi['1997-05-01'], -3)
print(json.dumps(out))
