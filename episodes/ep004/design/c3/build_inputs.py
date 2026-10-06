"""Tập 4 · C3: đầu vào nhà máy cho style frame N1/N2 (chạy lại được, không sửa tay file sinh ra).
  python3 episodes/ep004/design/c3/build_inputs.py
Vào:  story/script.md (câu Sxx.n), numbers.md (claim ID, giá trị, nghĩa) + out/model.json (giá trị làm tròn, tham số),
      data/CPIAUCNS.csv (fetch.py; không commit), toolkit/visual-library/tokens.json (màu kênh).
Ra:   design/c3/gen/script.json, gen/claims.json, gen/tokens.json (commit) · design/c3/work/data.js (không commit: chuỗi CPI FRED).
Mọi số trên hình đi qua claim: display dựng ở đây từ giá trị (≈ cho số làm tròn của mô hình)."""
import csv, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.abspath(os.path.join(HERE, '..', '..'))
ROOT = os.path.abspath(os.path.join(EP, '..', '..'))
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
NAMES = {'us': 'US average', 'new_york': 'New York', 'los_angeles': 'Los Angeles', 'san_diego': 'San Diego',
         'san_francisco': 'San Francisco', 'san_jose': 'San Jose'}
name = lambda s: NAMES.get(s, s.replace('_', ' ').title())
money = lambda v: f'${v:,.0f}'


def script():
    out = []
    for ln in open(os.path.join(EP, 'story', 'script.md'), encoding='utf-8'):
        m = re.match(r'^(S\d+)\.(\d+) \| (.+?) \| ', ln)
        if m:
            out.append({'id': f'{m[1]}.{m[2]}', 'scene': m[1], 'text': m[3].strip()})
    return {'sentences': out}


def claims(model):
    R, P, out = model['rounded'], model['params'], []
    now = P['cpiNowMonth']
    for ln in open(os.path.join(EP, 'numbers.md'), encoding='utf-8'):
        m = re.match(r'^\| `([a-z0-9_]+)` \| ([^|]+) \| ([^|]+) \|', ln)
        if not m:
            continue
        cid, raw, mean = m[1], m[2].strip(), m[3].strip()
        v = R.get(cid, raw)
        hist = cid in R and cid not in ('excl_joint_limit_usd',)          # tính từ dữ liệu FHFA/CPI = lịch sử
        illus = bool(re.match(r'(illustrative_price_|gain_at_|cross_quarter_at_|stay_quarter_at_)', cid))
        if cid.startswith('threshold_') and isinstance(v, (int, float)):
            d = '≈ ' + money(v)
        elif cid.startswith('gain_at_') and isinstance(v, (int, float)):
            d = '≈ ' + money(v)
        elif cid == 'excl_joint_1997_in_now':
            d = f'≈ {money(v)} ({MON[int(now[5:7]) - 1]} {now[:4]} dollars)'
        elif cid.startswith('growth_'):
            d = f'×{v:.1f}'
        elif cid in ('excl_joint_limit_usd', 'excl_single_limit_usd') or cid.startswith('illustrative_price_'):
            d = money(float(v))
        elif cid == 'exclusion_effective_month':
            d = f'{MON[int(raw[5:7]) - 1]} {raw[:4]}'
        elif isinstance(v, list):
            d = ', '.join(name(x) for x in v)
        elif cid.endswith('_metro'):
            d = name(v)
        elif isinstance(v, float) and v.is_integer():
            d = str(int(v))
        else:
            d = str(v)
        out.append({'claimId': cid, 'value': v, 'display': d, 'unit': mean, 'source': {'id': 'numbers.md', 'url': None},
                    'historical': hist, 'illustrative': illus})
    return {'claims': out}


def data(model):
    R, P = model['rounded'], model['params']
    rows = [r for r in csv.reader(open(os.path.join(EP, 'data', 'CPIAUCNS.csv')))][1:]
    cpi = [[d[:7], float(x)] for d, x in rows if x.strip() and P['cpiBaseMonth'] <= d <= P['cpiNowMonth']]
    metros = sorted({k[len('threshold_joint_'):] for k in R if k.startswith('threshold_joint_') and f'growth_{k[16:]}' in R})
    rungs = [{'slug': s, 'name': name(s), 'threshold': R[f'threshold_joint_{s}'], 'growth': R[f'growth_{s}'],
              'national': s == 'us'} for s in metros]
    return {'cpi': cpi, 'cap': P['exclusionJoint'], 'rungs': sorted(rungs, key=lambda r: r['threshold'])}


def main():
    model = json.load(open(os.path.join(EP, 'out', 'model.json')))
    gen, work = os.path.join(HERE, 'gen'), os.path.join(HERE, 'work')
    os.makedirs(gen, exist_ok=True); os.makedirs(work, exist_ok=True)
    json.dump(script(), open(os.path.join(gen, 'script.json'), 'w'), indent=1, ensure_ascii=False)
    json.dump(claims(model), open(os.path.join(gen, 'claims.json'), 'w'), indent=1, ensure_ascii=False)
    lib = json.load(open(os.path.join(ROOT, 'toolkit', 'visual-library', 'tokens.json')))
    c = lib['color']
    tok = {'_about': 'Tập 4 C3: màu kênh toolkit/visual-library/tokens.json (bảng E2) + vai của tập (beats.md): cap = ink-muted (đứng yên), '
                     'gain = ink, above = warn (trên trần, ILLUSTRATIVE), index = accent (chỉ số thị trường).',
           'version': lib['version'], 'color': c, 'type': lib['type'],
           'roles': {'cap': c['ink-muted'], 'gain': c['ink'], 'above': c['warn'], 'index': c['accent']}}
    json.dump(tok, open(os.path.join(gen, 'tokens.json'), 'w'), indent=1, ensure_ascii=False)
    d = data(model)
    open(os.path.join(work, 'data.js'), 'w').write('const DATA = ' + json.dumps(d) + ';\n')
    print('script', len(script()['sentences']), 'câu · claims', len(claims(model)['claims']), '· cpi', len(d['cpi']), 'tháng · rungs', len(d['rungs']))


if __name__ == '__main__':
    main()
