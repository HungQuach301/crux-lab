"""Tập 6 · C4: đầu vào nhà máy cho cả tập + artefact hợp đồng (chạy lại được, không sửa tay file sinh ra). Mẫu: episodes/ep005/c4/build_inputs.py.
  python3 episodes/ep006/c4/build_inputs.py              # c4/gen/{script,claims,tokens,data}.json + design/tokens.json
  python3 episodes/ep006/c4/build_inputs.py --timeline   # + timeline KHÔ của nhà máy (spec-free: load_inputs → voice → resolve, 0 ký tự EL:
                                                         #   dừng nếu một cảnh không trúng take trong voice-takes/) → out/factory/timeline.json,
                                                         #   captions.srt; rồi nhạc nền work/factory/music/bed.wav (audio.music_cmd) nếu chưa có
  python3 episodes/ep006/c4/build_inputs.py --out        # sau build.sh: out/{script,claims,timeline,adbreaks}.json, out/captions.srt, out/video.mp4,
                                                         #   out/audio/stems/*, out/voice/takes.json, out/tempo-map.json, out/sfx-events.json, …
Vào:  story/script.md (lời + vai), numbers.md (hiển thị), out/model.json (raw = CHƯA làm tròn → claims.json, contract S05), contract.json
      (model.claims: claimId → khoá mô hình), episode.yaml (acts, midrolls, world), out/factory/timeline.json + splice.json (sau build).
Lời: chữ câu = đúng script.md (kể cả thẻ cảm xúc eleven_v3 — khoá take = SHA-256 của chữ đã nói); phụ đề bỏ thẻ cảm xúc."""
import hashlib, json, os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.dirname(HERE)
ROOT = os.path.abspath(os.path.join(EP, '..', '..'))
GEN = os.path.join(HERE, 'gen')
LINE = re.compile(r'^(S\d\d)\.(\d+)\s+(?:\{(\w+)\}\s+)?(.+?)\s*<!--\s*claims:\s*([^;>]*?)\s*(?:;[^>]*)?-->')
TAG = re.compile(r'^\[[a-z ]+\]\s+')
ROLE_KEEP = ('hook', 'promise')          # out/script.json: role ∈ hook, promise (checks/CONTRACT.md, S18)
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
CHAR = {'guide_': 'ruth', 'latest_window_real_value_2pct': 'ruth', 'latest_window_real_value_level': 'ruth', 'worst_': 'carl', 'raise_needed_all': 'carl',
        'kept_up_last_start': 'edna'}


def script_rows():
    out = []
    for ln in open(os.path.join(EP, 'story', 'script.md'), encoding='utf-8'):
        m = LINE.match(ln)
        if m:
            x = {'id': f'{m[1]}.{m[2]}', 'scene': m[1], 'text': m[4].strip()}
            if m[3] in ROLE_KEEP:
                x['role'] = m[3]
            x['_claims'] = [c.strip() for c in m[5].split(',') if c.strip() and c.strip() != '—']
            out.append(x)
    return out


def numbers_display():
    """numbers.md cột Hiển thị (bỏ phần trong ngoặc: dạng ngắn trên hình); dòng nhiều id 'a / b' tách theo ' / ' nếu có."""
    disp = {}
    for ln in open(os.path.join(EP, 'numbers.md'), encoding='utf-8'):
        m = re.match(r'^\| `([a-z0-9_ /`]+)` \| ([^|]*) \| ([^|]*) \|', ln)
        if m:
            ids = [x.strip(' `') for x in m[1].split('/')]
            shows = [x.strip() for x in m[3].split(' / ')] if ' / ' in m[3] else [m[3].strip()] * len(ids)
            for cid, s in zip(ids, shows):
                disp[cid] = re.sub(r'\s*\(.*\)$', '', s).strip()
    return disp


def ym(v):
    return f'{MON[int(v[5:7]) - 1]} {v[:4]}'


# hiển thị ngắn trên hình (core.claimSpans khớp NGUYÊN VĂN chuỗi này trong chữ của khung)
SHOW = {'latest_start': 'Aug 2006', 'latest_end': 'Aug 2026', 'guide_start': 'Aug 2006', 'index_last_month': 'Aug 2026',
        'kept_up_first_start_20y': 'Sep 1947', 'kept_up_last_start_20y': 'Jan 1949', 'worst_window_start_year_20y': 'Jan 1966',
        'two_pct_growth_20y_pct': '48.6%', 'latest_window_real_value_2pct_payment_pct': 'about 9 in 10',
        'latest_window_real_value_level_payment_pct': 'about 6 in 10', 'guide_years_2pct_at_or_above_100': '12 of the first 15',
        'guide_last_year_2pct_at_or_above_100': '15 years', 'guide_year_level_reaches_2pct_end': 'year 5',
        'median_year_level_reaches_2pct_end_median': 'about year 8', 'worst_window_years_2pct_fell_20y': '20 of 20',
        'windows_20y': '715', 'windows_2pct_kept_up_20y': '17', 'windows_25y': '655', 'windows_2pct_kept_up_25y': '0 of 655',
        'by_decade_2000_kept': '0 of 79', 'cpiu_from_pce_start_kept_up_20y': '0 of 571', 'raise_needed_half_20y_pct': '3.1%',
        'median_inflation_20y_pct_per_year': '3.1% a year', 'raise_needed_all_20y_pct': '6.38%', 'cpi_yoy_latest_pct': '3.4%',
        'robust_cpiw_share_kept_up_20y_pct': '2.9%', 'worst_real_value_level_payment_after_20y_pct': '29.0%'}
WORLD3D = '3D world objects drawn by code (lib3d.js W1–W10, c4kit.js)'


def CONST(raw, P):
    """Hằng số / đại lượng dẫn xuất CÓ trên hình mà chưa có claim mô hình. Mỗi dòng: (claimId, value, display, formula, nguồn, role)."""
    gp = raw['guide_path']
    d90, d00 = raw['by_decade']['1990'], raw['by_decade']['2000']
    rows = [
        ('raise_2pct', P['raise'], '2%', 'model.params.raise: the check rises 2% once a year, at each anniversary', 'contract'),
        ('raise_3pct', 0.03, '3%', 'model.params.raiseGrid rung 0.030 (raise_grid_3pct is its share)', 'contract'),
        ('main_years', P['mainYears'], '20-year', 'model.params.mainYears: a 20-year stretch of retirement (240 months)', 'contract'),
        ('main_years_raises', P['mainYears'], '20 raises', 'model.params.mainYears: 20 anniversaries = 20 raises', 'contract'),
        ('main_years_after', P['mainYears'], '20 years', 'model.params.mainYears', 'contract'),
        ('long_years', P['horizonsYears'][1], '25-year', 'model.params.horizonsYears[1]', 'contract'),
        ('first_start_month', raw['first_start_20y'], 'Jan 1947', 'first start month of the 20-year windows (model.params.firstStart)', 'model'),
        ('first_start_year', 1947, '1947', 'year of first_start_20y', 'model'),
        ('crates_first', 10, '10 crates', "the first check's buying power drawn as a row of 10 crates (crates = round(10 × share), numbers.md)", 'rule'),
        ('crates_all', 10, 'all 10', 'crate row at or above 100% of the first check: all 10 lit (capped at 10)', 'rule'),
        ('crates_full', 10, '10', 'Edna at year 20: 100.2% → round(10 × 1.002) = 10 crates (capped at 10)', 'rule'),
        ('crates_ruth', round(10 * raw['guide_real_2pct_end_pct'] / 100), 'about 9', 'round(10 × guide_real_2pct_end_pct / 100)', 'model'),
        ('crates_carl', round(10 * raw['worst_real_value_2pct_payment_after_20y_pct'] / 100), 'about 4', 'round(10 × worst_real_value_2pct_payment_after_20y_pct / 100)', 'model'),
        ('crates_carl_of10', round(10 * raw['worst_real_value_2pct_payment_after_20y_pct'] / 100), 'about 4 of 10', 'round(10 × worst_real_value_2pct_payment_after_20y_pct / 100) of 10', 'model'),
        ('crates_median', round(10 * raw['median_real_value_2pct_payment_after_20y_pct'] / 100), 'about 8 of 10', 'round(10 × median_real_value_2pct_payment_after_20y_pct / 100) of 10', 'model'),
        ('guide_age_start', P['guide']['age'], 'age 65', 'model.params.guide.age (ILLUSTRATIVE)', 'contract'),
        ('guide_age_2021', gp[15]['age'], 'age 80', 'guide_path[15].age', 'model'),
        ('guide_age_2022', gp[16]['age'], 'age 81', 'guide_path[16].age', 'model'),
        ('guide_age_end', gp[20]['age'], 'age 85', 'guide_path[20].age', 'model'),
        ('guide_month_2021', gp[15]['month'], 'Aug 2021', 'guide_path[15].month (anniversary 15)', 'model'),
        ('guide_month_2022', gp[16]['month'], 'Aug 2022', 'guide_path[16].month (anniversary 16)', 'model'),
        ('guide_real_2pct_2021_pct', gp[15]['real_2pct_pct'], '100.3%', 'guide_path[15].real_2pct_pct: the 2% check at anniversary 15 (last at or above 100%)', 'model'),
        ('share_kept_1_in', round(100 / raw['share_2pct_kept_up_20y_pct']), 'about 1 in 42', '1 in round(715 / 17)', 'model'),
        ('by_decade_1990_kept_n', d90['kept'], '0 of 120', f"by_decade['1990'].kept of n = {d90['n']}", 'model'),
        ('by_decade_2000_n', d00['n'], '79', "by_decade['2000'].n: starts 2000-01 to 2006-08", 'model'),
        ('decade_1990', 1990, '1990s', 'start decade 1990-01..1999-12', 'model'),
        ('decade_1960', 1960, '1960s', 'start decade 1960-01..1969-12', 'model'),
        ('decade_2000', 2000, '2000', 'first start year of the 2000s group', 'model'),
        ('robust_cpiw_kept_up_n', raw['robust_cpiw_kept_up_20y'], '21 of 715', 'robust_cpiw_kept_up_20y of robust_cpiw_windows_20y', 'model'),
        ('pce_first_year', int(raw['robust_pce_first_start'][:4]), '1959', 'first start year of the PCE windows (robust_pce_first_start)', 'model'),
        ('cpi_yoy_months', 12, '12 months', 'cpi_yoy_latest_pct window: 12 months to the last index month', 'rule'),
        ('edna_end_year', int(raw['kept_up_last_start_20y'][:4]) + 20, '1969', 'kept_up_last_start_20y + 20 years', 'model'),
        ('carl_end_year', raw['worst_window_start_year_20y'] + 20, '1986', 'worst_window_start_year_20y + 20 years', 'model'),
        ('carl_start_year', raw['worst_window_start_year_20y'], '1966', 'worst_window_start_year_20y', 'model'),
        ('edna_start_year', int(raw['kept_up_last_start_20y'][:4]), '1949', 'year of kept_up_last_start_20y', 'model'),
        # C5b (S07): "the gentler 2000s and 2010s" (S19.1): the 2000s start group (starts 2000-01..2006-08) runs its 20 years through 2010–2019
        ('decade_2010', 2010, '2010s', "years 2010-01..2019-12 inside the 20-year windows of the 2000s start group (by_decade['2000']: ends 2020-01..2026-08)", 'model'),
    ]
    rows += [(f'axis_year_{k}', k, f'year {k}', f'anniversary counter (year {k} of 20)', 'axis') for k in range(1, 21)]
    return rows


# C5b (S07): câu nói một hằng số / claim CONST (lời không đổi; chú thích claims của script.md chỉ liệt kê claim mô hình)
EXTRA_SPOKEN = {'raise_2pct': ['S01.2', 'S05.3', 'S12.4', 'S13.3', 'S27.1', 'S28.2', 'S32.2'], 'raise_3pct': ['S30.2'],
                'main_years': ['S02.2', 'S06.1', 'S06.2', 'S12.3', 'S13.1', 'S16.2', 'S25.1', 'S30.2'], 'long_years': ['S21.1'],
                'first_start_year': ['S02.2', 'S13.1'], 'guide_age_start': ['S01.2', 'S04.1'], 'guide_age_2021': ['S10.1'],
                'guide_month_2021': ['S10.1'], 'guide_month_2022': ['S11.1'], 'guide_age_end': ['S28.1', 'S32.3'], 'share_kept_1_in': ['S14.2'],
                'crates_first': ['S16.3', 'S24.4'], 'crates_all': ['S27.5'], 'crates_carl': ['S29.2'], 'decade_2000': ['S19.1'],
                'decade_2010': ['S19.1'], 'decade_1960': ['S26.1']}


def model_value(raw, P, key):
    """Giá trị CHƯA làm tròn của một khoá mô hình, cùng luật khoá suy ra của checks/py/r_model.py frw_value (kind fixed-raise-vs-index-windows):
    by_decade_<thập kỷ>_<n|kept|median_real_2pct|…>, raise_grid_<r>pct, guide_real_<2pct|level>_<năm>_pct; còn lại = raw[key] hoặc params."""
    m = re.fullmatch(r'by_decade_(\d{4})_(n|kept|median_real_\w+|min_real_\w+|max_real_\w+|median_inflation)', key)
    if m:
        d = raw['by_decade'][m[1]]
        return d[m[2]] if m[2] in ('n', 'kept') else d[m[2] + '_pct']
    m = re.fullmatch(r'raise_grid_(\d+(?:p\d+)?)pct', key)
    if m:
        return raw['raise_grid'][f"{float(m[1].replace('p', '.')) / 100:.3f}"]
    m = re.fullmatch(r'guide_real_(level|2pct)_(\d{4})_pct', key)
    if m:
        row = next(r for r in raw['guide_path'] if int(r['month'][:4]) == int(m[2]))
        return row['real_level_pct' if m[1] == 'level' else 'real_2pct_pct']
    return raw[key] if key in raw else P[key]


def claims():
    C = json.load(open(os.path.join(EP, 'contract.json')))
    M = json.load(open(os.path.join(EP, 'out', 'model.json')))
    raw, P = M['raw'], M['params'] if 'params' in M else C['model']['params']
    ill = set(C['claims'].get('illustrative', []))
    cond = {}   # C5b (S17): một claim mang MỘT cờ (checks: conditional = id); điều kiện khai trước thắng (trước đây khai sau ghi đè)
    for x in C['claims'].get('conditions', []):
        for c in x.get('claims', []):
            cond.setdefault(c, x['id'])
    core, decisive = set(C['claims'].get('core', [])), set(C['claims'].get('decisive', []))
    disp = numbers_display()
    spoken = {}
    for r in script_rows():
        for c in r['_claims']:
            spoken.setdefault(c, []).append({'scene': r['scene'], 'sentence': r['id']})
    out = []
    for cid, key in C['model']['claims'].items():
        v = model_value(raw, P, key)
        hist = cid not in ('two_pct_growth_20y_pct',)
        d = SHOW.get(cid) or disp.get(cid) or (ym(v) if isinstance(v, str) else str(v))
        x = {'claimId': cid, 'value': v, 'display': d, 'unit': key, 'formula': key, 'source': {'id': 'model', 'url': None},
             'historical': hist, 'illustrative': cid in ill}
        if hist:
            x['dataYears'] = [1947, 2026]
        ch = next((c for p, c in CHAR.items() if cid.startswith(p)), None)
        if ch:
            x['character'] = ch
            x['illustrative'] = True   # S05: mọi claim của nhân vật ILLUSTRATIVE mang cờ (C4 checks lần 1: 7 claim Carl/Edna/Ruth thiếu)
        for k, flag in (('conditional', cid in cond), ('core', cid in core), ('decisive', cid in decisive)):
            if flag:
                x[k] = cond[cid] if k == 'conditional' else True
        x.update(callbacks=[], shownIn=[], spoken=spoken.get(cid, []))
        out.append(x)
    for cid, val, d, formula, src in CONST(raw, C['model']['params']):
        x = {'claimId': cid, 'value': val, 'display': d, 'unit': 'const', 'formula': formula,
             'source': {'id': {'contract': 'contract.json', 'model': 'model', 'rule': 'numbers.md', 'axis': 'axis'}[src], 'url': None},
             'historical': src == 'model', 'illustrative': cid.startswith(('guide_', 'crates_ruth', 'crates_carl')), 'callbacks': [], 'shownIn': [], 'spoken': []}
        if src == 'axis':
            x['role'] = 'axis'
        if x['historical']:
            x['dataYears'] = [1947, 2026]
            if cid in cond:
                x['conditional'] = cond[cid]
        out.append(x)
    by = {c['claimId']: c for c in out}
    for cid, sids in EXTRA_SPOKEN.items():
        have_s = {q['sentence'] for q in by[cid]['spoken']}
        by[cid]['spoken'] += [{'scene': sid.split('.')[0], 'sentence': sid} for sid in sids if sid not in have_s]
    ids = [c['claimId'] for c in out]
    assert len(ids) == len(set(ids)), 'claimId trùng'
    return {'claims': out}


def tokens():
    T = json.load(open(os.path.join(ROOT, 'toolkit', 'visual-library', 'tokens.json')))
    col = T.get('color') or T.get('colors')
    C_ = json.load(open(os.path.join(EP, 'contract.json')))
    chars = {f'char-{k}': v['color'] for k, v in C_['characters'].items() if isinstance(v, dict) and v.get('color')}
    return {'color': col, 'colors': {**col, 'muted': col.get('ink-muted', '#9AA4B2'), 'cushion': '#269783', **chars},
            'series': {'rising': col['ink'], 'level': col.get('ink-muted', '#9AA4B2'), 'prices': col['accent'], 'fellShort': col['warn'],
                       'keptUp': '#269783'}, 'seriesOf': {}}


def main():
    os.makedirs(GEN, exist_ok=True)
    rows = script_rows()
    sc = {'sentences': [{k: v for k, v in r.items() if not k.startswith('_')} for r in rows]}
    json.dump(sc, open(os.path.join(GEN, 'script.json'), 'w'), indent=1, ensure_ascii=False)
    cl = claims()
    json.dump(cl, open(os.path.join(GEN, 'claims.json'), 'w'), indent=1, ensure_ascii=False)
    tk = tokens()
    json.dump(tk, open(os.path.join(GEN, 'tokens.json'), 'w'), indent=1)
    json.dump({'_about': 'Tập 6: mọi cảnh là đoạn thế giới 3D (world:); nhà máy 2D không cần dữ liệu'}, open(os.path.join(GEN, 'data.json'), 'w'))
    os.makedirs(os.path.join(EP, 'design'), exist_ok=True)
    json.dump({k: tk[k] for k in ('colors', 'series', 'seriesOf')}, open(os.path.join(EP, 'design', 'tokens.json'), 'w'), indent=1)
    print('script', len(sc['sentences']), '· claims', len(cl['claims']))
    if '--timeline' in sys.argv:
        timeline()
    if '--out' in sys.argv:
        out()


def timeline():
    """Timeline KHÔ của nhà máy: đúng các bước load_inputs → voice → resolve của toolkit/factory/build.py (không spec, không render).
    Trước khi gọi voice: mỗi cảnh phải TRÚNG take có sẵn (băm SHA-256 như voice.py) — trượt một cảnh → dừng, không gọi API."""
    import yaml
    sys.path[:0] = [os.path.join(ROOT, 'toolkit', 'factory'), os.path.join(ROOT, 'toolkit', 'factory', 'world')]
    import build as BUILD
    import voice as VOICE
    yml = os.path.join(EP, 'episode.yaml')
    Y = yaml.safe_load(open(yml))
    rows = script_rows()
    miss = []
    for s in Y['scenes']:
        cfg = VOICE.scene_cfg(Y['voice'], Y.get('voice_overrides'), s['id'])
        text = ' '.join(VOICE.to_spoken([r['text'] for r in rows if r['scene'] == s['id']]))
        key = hashlib.sha256(json.dumps([text, cfg['voice'], cfg['model'], cfg['seed'], cfg.get('settings', {'stability': 0.5, 'speed': 0.9})],
                                        sort_keys=True).encode()).hexdigest()[:16]
        if not os.path.exists(os.path.join(EP, 'voice-takes', key + '.mp3')):
            miss.append((s['id'], key))
    if miss:
        raise SystemExit(f'take không có trong voice-takes/ (lệch băm) — DỪNG, không sinh giọng: {miss}')
    B = BUILD.Build(yml, [yml])
    B.load_inputs()
    v = B.do_voice()
    assert v['el_chars_spent'] == 0 and v['cache_hits'] == len(Y['scenes']), v
    r = B.do_resolve()
    print(f"timeline: {r['total']} s ({int(r['total'] // 60)}:{r['total'] % 60:04.1f}) · voice {v['cache_hits']}/{len(Y['scenes'])} cache · EL 0")
    bed = os.path.join(EP, Y['audio']['music'])
    if not os.path.exists(bed):
        subprocess.run(Y['audio']['music_cmd'].format(total=r['total'], out=bed), shell=True, cwd=ROOT, check=True)


def captions(src, dst):
    """Phụ đề nhà máy, bỏ thẻ cảm xúc eleven_v3, gộp cue < 1 s như Tập 4/5 (episodes/ep004/design/c4/build_inputs.py captions)."""
    import importlib.util, tempfile
    txt = re.sub(r'\[[a-z ]+\]\s+', '', open(src, encoding='utf-8').read())
    tmp = tempfile.NamedTemporaryFile('w', suffix='.srt', delete=False, encoding='utf-8'); tmp.write(txt); tmp.close()
    sp = importlib.util.spec_from_file_location('c4ep4', os.path.join(ROOT, 'episodes', 'ep004', 'design', 'c4', 'build_inputs.py'))
    E4 = importlib.util.module_from_spec(sp); sp.loader.exec_module(E4)
    E4.captions(tmp.name, dst); os.remove(tmp.name)


def scene_take(sc):
    sys.path.insert(0, os.path.join(EP, 'world'))
    import wlib
    return wlib.voice_scenes()[sc]['take'].replace('.mp3', '')


def out():
    """Như Tập 5 (episodes/ep005/c4/build_inputs.py out): artefact hợp đồng từ chính bản dựng; ident = cảnh IDENT 3 s riêng."""
    import yaml
    F = os.path.join(EP, 'out', 'factory')
    W = os.path.join(EP, 'work', 'factory')
    tl = json.load(open(os.path.join(F, 'timeline.json')))
    roles = {r['id']: r.get('role') for r in script_rows()}
    sents = []
    for s in tl['sentences']:
        x = {k: s[k] for k in ('id', 'scene', 'text', 'spoken', 'start', 'end')}
        x['text'] = TAG.sub('', x['text'])
        if roles.get(s['id']):
            x['role'] = roles[s['id']]
        sents.append(x)
    json.dump({'sentences': sents}, open(os.path.join(EP, 'out', 'script.json'), 'w'), indent=1, ensure_ascii=False)
    shutil.copy(os.path.join(GEN, 'claims.json'), os.path.join(EP, 'out', 'claims.json'))
    captions(os.path.join(F, 'captions.srt'), os.path.join(EP, 'out', 'captions.srt'))
    Y = yaml.safe_load(open(os.path.join(EP, 'episode.yaml')))
    acts = Y.get('acts') or []
    S = {s['id']: s for s in tl['scenes']}
    A = [{'id': a['id'], 'start': S[a['scenes'][0]]['start'], 'end': round(S[a['scenes'][-1]]['start'] + S[a['scenes'][-1]]['dur'], 4)} for a in acts]
    scenes = [{'id': s['id'], 'start': s['start'], 'dur': s['dur'], 'end': round(s['start'] + s['dur'], 4), 'world': s.get('world'),
               'act': next((a['id'] for a in acts if s['id'] in a['scenes'] and a['id'] != 'ident'), None)} for s in tl['scenes']]
    for a in A:
        if a['id'] == 'ident':
            a['start'] = round(a['end'] - 3.0, 4)
            prev = next(x for x in A if x['end'] == a['end'] and x['id'] != 'ident'); prev['end'] = a['start']
            sc = next(x for x in scenes if abs(x['end'] - a['end']) < 1e-3)
            sc['dur'] = round(sc['dur'] - 3.0, 4); sc['end'] = a['start']
            scenes.insert(scenes.index(sc) + 1, {'id': 'IDENT', 'start': a['start'], 'dur': 3.0, 'end': a['end'], 'world': sc.get('world'), 'act': 'ident'})
    A.sort(key=lambda a: a['start'])
    json.dump({'fps': tl['fps'], 'total': tl['total'], 'acts': A, 'scenes': scenes, 'world': tl.get('world', [])},
              open(os.path.join(EP, 'out', 'timeline.json'), 'w'), indent=1)
    json.dump({'breaks': [m['t'] for m in Y.get('midrolls') or []]}, open(os.path.join(EP, 'out', 'adbreaks.json'), 'w'), indent=1)
    vd = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=duration', '-of', 'csv=p=0',
                         os.path.join(W, 'video.mp4')], capture_output=True, text=True, check=True).stdout.strip()
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', os.path.join(W, 'video.mp4'), '-map', '0', '-c', 'copy', '-t', vd,
                    '-movflags', '+faststart', os.path.join(EP, 'out', 'video.mp4')], check=True)
    st = os.path.join(EP, 'out', 'audio', 'stems')
    os.makedirs(st, exist_ok=True)
    for f in os.listdir(st):
        os.remove(os.path.join(st, f))
    for f in os.listdir(os.path.join(W, 'stems')):
        shutil.copy(os.path.join(W, 'stems', f), os.path.join(st, f))
    rep = json.load(open(os.path.join(F, 'build-report.json')))
    v = Y['voice']
    takes = [{'id': s['id'], 'raw': f"voice-takes/{scene_take(s['id'])}.mp3", 'final': 'out/audio/stems/voice.flac', 'model': v['model'],
              'voiceId': v['voice'], 'provider': 'elevenlabs', 'seed': v['seed']} for s in tl['scenes']]
    os.makedirs(os.path.join(EP, 'out', 'voice'), exist_ok=True)
    json.dump({'takes': takes, 'voice': {'provider': 'elevenlabs', 'voiceId': v['voice'], 'model': v['model']}, 'build': rep.get('steps', {}).get('voice')},
              open(os.path.join(EP, 'out', 'voice', 'takes.json'), 'w'), indent=1)
    bj = os.path.join(EP, Y['audio']['music'])
    if os.path.exists(bj + '.json'):   # lưới phách nhạc nền F-3 (bed.py) → tempo-map
        B = json.load(open(bj + '.json'))
        json.dump({'bpm': B.get('bpm'), 'beats': B.get('beats', []), 'accents': B.get('accents', [])}, open(os.path.join(EP, 'out', 'tempo-map.json'), 'w'))
    ev = []
    for w in Y.get('world') or []:   # sự kiện sfx của đoạn thế giới, giờ của tập
        sp = json.load(open(os.path.join(EP, w['dir'], 'spine.json')))
        t0 = next(s['start'] for s in tl['scenes'] if s['id'] == w['scenes'][0])
        ev += [{'t': round(t0 + e['t'], 3), 'x': 960, 'kind': e['kind']} for e in sp['events'] if e['kind'] != 'data']
    json.dump({'events': sorted(ev, key=lambda e: e['t'])}, open(os.path.join(EP, 'out', 'sfx-events.json'), 'w'))
    E4 = json.load(open(os.path.join(ROOT, 'episodes', 'ep004', 'out', 'rights.json')))['assets']
    voice = {**E4[0], 'name': 'voice: Eric (ElevenLabs premade, eleven_v3, seed 1005)'}
    inter = next(a for a in E4 if a['kind'] == 'font')
    rights = {'assets': [voice,
        {'name': 'music bed (style C, one cue per act, generated by code from the tension map, F-3) + channel ident A and closing cue A (F-12)', 'stems': ['music'],
         'visuals': [], 'kind': 'music', 'origin': 'project code, no third-party samples (episodes/ep006/world/music/bed.py, toolkit/factory/theme/)',
         'licence': 'own work', 'thirdParty': False, 'commercial': True, 'generator': 'episodes/ep006/world/music/bed.py'},
        {'name': 'data sounds, effects, camera-move whooshes and room tone (synthesised by code from the spine)', 'stems': ['sonify', 'sfx', 'whoosh', 'room'],
         'visuals': [], 'kind': 'sfx', 'origin': 'project code, no samples', 'licence': 'own work', 'thirdParty': False, 'commercial': True,
         'generator': 'toolkit/factory/world/audio.py'},
        inter,
        {'name': '3D world, charts and cards drawn by code (three.js scene + 2D overlay)', 'stems': [], 'visuals': [WORLD3D], 'kind': 'model3d',
         'origin': 'toolkit/factory/world/lib3d.js, core.js, episodes/ep006/world/c4kit.js, world/c4/*/scene.js; no model or texture files; three.js 0.186.1 (MIT) is code',
         'licence': 'own work', 'thirdParty': False, 'commercial': True, 'generator': 'toolkit/factory/world/lib3d.js'},
        {'name': 'three.js 0.186.1 (WebGL library that draws the 3D world; code, no model or texture files)', 'stems': [], 'visuals': [], 'kind': 'code',
         'origin': 'npm package three 0.186.1, toolkit/factory/world/vendor/package.json (npm ci; node_modules not committed)', 'licence': 'MIT',
         'thirdParty': True, 'commercial': True,
         'terms': {'quote': 'Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software',
                   'url': 'https://github.com/mrdoob/three.js/blob/r186/LICENSE'}}]}
    json.dump(rights, open(os.path.join(EP, 'out', 'rights.json'), 'w'), indent=1, ensure_ascii=False)
    json.dump({'assets': [{'name': 'Inter', 'kind': 'font', 'family': 'Inter', 'paths': ['../../toolkit/render/fonts/inter-latin-*.woff2']},
                          {'name': WORLD3D, 'kind': 'model3d'}],
               'generated': [{'glob': 'world/grid.json', 'generator': 'world/derive.py'}]}, open(os.path.join(EP, 'out', 'visual-assets.json'), 'w'), indent=1)
    extras(Y, tl)
    print('out: script.json', len(sents), '· claims.json · captions.srt · timeline.json · adbreaks.json · video.mp4 · stems · takes.json')


def extras(Y, tl):
    """tension-map, cues.json (mỗi hồi một cue), transitions.json (ranh giới đoạn thế giới), preprod/shotlist.json (động tác máy của spine)."""
    import numpy as np, soundfile as sf
    B = json.load(open(os.path.join(EP, Y['audio']['music']) + '.json'))
    total, kf = tl['total'], [(k['t'], k['v']) for k in B['tension']['keyframes']]
    ev, mv = [], []
    for w in Y['world']:
        sp = json.load(open(os.path.join(EP, w['dir'], 'spine.json'))); t0 = sp['episode_t0']
        ev += [t0 + e['t'] for e in sp['events']]; mv += [{**m, 't0': t0 + m['t0'], 't1': t0 + m['t1'], 'seg': w['id']} for m in sp['moves']]
    mus, sr = sf.read(os.path.join(EP, 'out', 'audio', 'stems', 'music.flac'), always_2d=True); mus = mus.mean(1)
    samples = []
    for t in np.arange(0.5, total, 1.0):
        seg = mus[int((t - 0.5) * sr):int((t + 0.5) * sr)]
        samples.append({'t': round(float(t), 2), 'cutRate': sum(1 for m in mv if abs(m['t0'] - t) <= 30), 'audioDensity': sum(1 for e in ev if abs(e - t) <= 5) / 10,
                        'musicLevel': round(float(10 * np.log10(np.mean(seg ** 2) + 1e-12)), 1), 'tension': round(float(np.interp(t, *zip(*kf))), 3)})
    json.dump({'samples': samples, '_about': 'tension = F-3 tension map (world/music/tension.py); musicLevel = music stem dBFS (1 s); audioDensity = spine sfx/data events per s (±5 s); cutRate = camera moves per min (±30 s)'},
              open(os.path.join(EP, 'out', 'tension-map.json'), 'w'), indent=1)
    json.dump({'cues': B.get('cues', []), 'silences': B.get('silences', [])}, open(os.path.join(EP, 'out', 'cues.json'), 'w'), indent=1)
    cuts = []
    for a_, b_ in zip(Y['world'], Y['world'][1:]):
        t = next(s['start'] for s in tl['scenes'] if s['id'] == b_['scenes'][0])
        dip = a_['id'].startswith('a-')
        cuts.append({'t': round(t, 3), 'from': a_['id'], 'to': b_['id'], 'type': 'dissolve' if dip else 'cut', 'match': None, 'audio': None,
                     'reason': 'ident: world dims to the channel ident, act 1 fades in from dark' if dip else 'segment boundary at an act/scene turn; the next segment opens on its own first pose (short fade from the background)'})
    json.dump({'cuts': cuts}, open(os.path.join(EP, 'out', 'transitions.json'), 'w'), indent=1)
    sh = [{'id': f"{m['seg']}:{m.get('id', m['verb'])}", 'scene': next(s['id'] for s in tl['scenes'] if s['start'] <= m['t0'] < s['start'] + s['dur']),
           'size': 'world' if str(m['to']).startswith('w') else 'chart', 'move': m['verb'] + (' (fly)' if m.get('style') == 'fly' else ''), 'moveReason': m['reason']} for m in mv]
    os.makedirs(os.path.join(EP, 'preprod'), exist_ok=True)
    json.dump({'shots': sh}, open(os.path.join(EP, 'preprod', 'shotlist.json'), 'w'), indent=1, ensure_ascii=False)


if __name__ == '__main__':
    main()
