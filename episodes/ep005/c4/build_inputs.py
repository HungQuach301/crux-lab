"""Tập 5 · C4: đầu vào nhà máy cho cả tập + artefact hợp đồng (chạy lại được, không sửa tay file sinh ra). Mẫu: episodes/ep004/design/c4/build_inputs.py.
  python3 episodes/ep005/c4/build_inputs.py            # trước build.sh: c4/gen/{script,claims,tokens,data}.json + design/tokens.json
  python3 episodes/ep005/c4/build_inputs.py --out      # sau build.sh: out/{script,claims,timeline,adbreaks}.json, out/captions.srt, out/video.mp4,
                                                       #   out/audio/stems/*, out/voice/takes.json, out/tempo-map.json, out/sfx-events.json
Vào:  story/script.md (lời + vai), numbers.md (hiển thị), out/model.json (raw = CHƯA làm tròn → claims.json, contract S05), contract.json
      (model.claims: claimId → khoá mô hình), episode.yaml (acts, midrolls, world), out/factory/timeline.json + splice.json (sau build).
Lời: chữ câu = đúng script.md (kể cả thẻ cảm xúc eleven_v3 như Tập 4 — khoá take = SHA-256 của chữ đã nói); phụ đề bỏ thẻ cảm xúc."""
import json, os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.dirname(HERE)
ROOT = os.path.abspath(os.path.join(EP, '..', '..'))
GEN = os.path.join(HERE, 'gen')
LINE = re.compile(r'^(S\d\d)\.(\d+)\s+(?:\{(\w+)\}\s+)?(.+?)\s*<!--\s*claims:\s*([^;>]*?)\s*(?:;[^>]*)?-->')
TAG = re.compile(r'^\[[a-z ]+\]\s+')
ROLE_KEEP = ('hook', 'promise')          # out/script.json: role ∈ hook, promise (checks/CONTRACT.md, S18)


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
    disp = {}
    for ln in open(os.path.join(EP, 'numbers.md'), encoding='utf-8'):
        m = re.match(r'^\| `([a-z0-9_*/ ]+)` \| ([^|]*) \| ([^|]*) \|', ln)
        if m:
            ids = [x.strip() for x in m[1].split('/')]
            shows = [x.strip() for x in m[3].split(' / ')] if len(ids) > 1 else [m[3].strip()]
            for i, cid in enumerate(ids):
                cid = cid if cid.startswith(('ex_', 'sched80', 'robust')) or i == 0 else ids[0].rsplit('_', 1)[0] + '_' + cid
                disp[cid] = shows[min(i, len(shows) - 1)]
    return disp


WORLD3D = '3D world objects drawn by code (lib3d.js W1–W9, obj5.js, c4kit.js)'   # C5: tên tài sản hình (rights ↔ visual-assets)
SHOW = {'value_removal_ltv_early': '75%', 'pmi_required_below20': 'under 20% down', 'hpi_peak_to_trough_pct': '−22.2%'}   # hiển thị ngắn trên hình
MON = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


def fmt(cid, v):
    if isinstance(v, str) and re.match(r'^\d{4}-\d\d-\d\d$', v):
        return f'{MON[int(v[5:7]) - 1]} {v[:4]}'
    if isinstance(v, float) and ('share' in cid or 'ltv' in cid.lower()) and v <= 1.5:
        return f'{100 * v:.1f}%'
    if cid.endswith('_rate') or cid.startswith('rate_'):
        return f'{v:.2f}%'
    if cid.endswith('Pct'):
        return f'{v:+.1f}%'
    if isinstance(v, (int, float)) and abs(v) >= 1000:
        return f'${v:,.0f}'
    return str(v)


def claims():
    """claims.json: mọi claim của hợp đồng (model.claims → giá trị CHƯA làm tròn từ out/model.json raw; params) + claim luật/không mô hình
    của numbers.md. display: cột Hiển thị của numbers.md nếu có, không thì định dạng từ giá trị."""
    C = json.load(open(os.path.join(EP, 'contract.json')))
    M = json.load(open(os.path.join(EP, 'out', 'model.json')))
    raw, P = M['raw'], C['model']['params']
    ill = set(C['claims']['illustrative'])
    cond = {c: x['id'] for x in C['claims']['conditions'] for c in x['claims']}
    core, decisive = set(C['claims']['core']), set(C['claims']['decisive'])
    disp = numbers_display()
    rows = script_rows()
    spoken = {}
    for r in rows:
        for c in r['_claims']:
            for cid in C['model']['claims']:
                if cid == c or (c.endswith('*') and cid.startswith(c[:-1])):
                    spoken.setdefault(cid, []).append({'scene': r['scene'], 'sentence': r['id']})
            if not c.endswith('*') and c not in C['model']['claims']:
                spoken.setdefault(c, []).append({'scene': r['scene'], 'sentence': r['id']})
    out = []
    for cid, key in C['model']['claims'].items():
        if key.startswith('fraction:'):
            v = raw[key[9:]] / 100
        else:
            v = raw[key] if key in raw else P[key]
        hist = not (cid.startswith(('ex_', 'rate_', 'sched', 'midpoint', 'mspus', 'value_removal', 'pmi_')) or cid in ('rate_partial',))
        x = {'claimId': cid, 'value': v, 'display': SHOW.get(cid) or disp.get(cid) or fmt(cid, v), 'unit': key, 'formula': key,
             'source': {'id': 'model', 'url': None}, 'historical': hist, 'illustrative': cid in ill}
        if hist:
            x['dataYears'] = [1991, 2026]
        if isinstance(v, (int, float)) and ('$' in x['display'] or cid in ('ex_price', 'ex_loan', 'ex_down', 'ex_payment_pi', 'ex_target80', 'ex_target78',
                                                                          'ex_extra_down_for_20', 'mspus_latest')):
            x['basis'] = 'nominal'
        m = re.match(r'buyer_(owen|grace|victor)_', cid)
        if m:
            x['character'] = m[1]
        if cid in cond:
            x['conditional'] = cond[cid]
        if cid in core:
            x['core'] = True
        if cid in decisive:
            x['decisive'] = True
        x['callbacks'] = []
        x['shownIn'] = []
        x['spoken'] = spoken.get(cid, [])
        out.append(x)
    have = {c['claimId'] for c in out}
    for cid, val, d in (('pmi_premium', None, '—'), ('borrower_request_conditions', 'written request, good payment history, current, no subordinate lien',
                         'written request · current on payments'), ('value_removal_rule', 'lender/investor rule', "loan owner's rule"),
                        ('value_removal_seasoning_years', 2, '2 years'), ('value_removal_ltv_early', 0.75, '75%')):
        if cid not in have:
            out.append({'claimId': cid, 'value': val, 'display': d, 'unit': 'rule', 'formula': 'rule (numbers.md)', 'source': {'id': 'numbers.md', 'url': None},
                        'historical': False, 'illustrative': False, 'callbacks': [], 'shownIn': [], 'spoken': spoken.get(cid, [])})
    return {'claims': out}


def tokens():
    T = json.load(open(os.path.join(ROOT, 'toolkit', 'visual-library', 'tokens.json')))
    col = T.get('color') or T.get('colors')
    return {'color': col, 'colors': {**col, 'muted': col.get('ink-muted', '#9AA4B2')},
            'series': {'schedule': col.get('ink-muted', '#9AA4B2'), 'onPaper': col['ink'], 'index': col['accent'], 'slow': col['accent'],
                       'cushion': '#269783'}, 'seriesOf': {}}


def main():
    os.makedirs(GEN, exist_ok=True)
    rows = script_rows()
    sc = {'sentences': [{k: v for k, v in r.items() if not k.startswith('_')} for r in rows]}
    json.dump(sc, open(os.path.join(GEN, 'script.json'), 'w'), indent=1, ensure_ascii=False)
    cl = claims()
    json.dump(cl, open(os.path.join(GEN, 'claims.json'), 'w'), indent=1, ensure_ascii=False)
    tk = tokens()
    json.dump(tk, open(os.path.join(GEN, 'tokens.json'), 'w'), indent=1)
    json.dump({'_about': 'Tập 5: mọi cảnh là đoạn thế giới 3D (world:); nhà máy 2D không cần dữ liệu'}, open(os.path.join(GEN, 'data.json'), 'w'))
    os.makedirs(os.path.join(EP, 'design'), exist_ok=True)
    json.dump({k: tk[k] for k in ('colors', 'series', 'seriesOf')}, open(os.path.join(EP, 'design', 'tokens.json'), 'w'), indent=1)
    print('script', len(sc['sentences']), '· claims', len(cl['claims']))
    if '--out' in sys.argv:
        out()


def captions(src, dst):
    """Phụ đề nhà máy, bỏ thẻ cảm xúc eleven_v3 ("[curious] ", chỉ dẫn giọng, không phải chữ nói), rồi gộp cue < 1 s như Tập 4
    (episodes/ep004/design/c4/build_inputs.py captions: cùng chữ, cùng thứ tự; chỉ dời ranh giới cue)."""
    import importlib.util, tempfile
    txt = re.sub(r'\[[a-z ]+\]\s+', '', open(src, encoding='utf-8').read())
    tmp = tempfile.NamedTemporaryFile('w', suffix='.srt', delete=False, encoding='utf-8'); tmp.write(txt); tmp.close()
    sp = importlib.util.spec_from_file_location('c4ep4', os.path.join(ROOT, 'episodes', 'ep004', 'design', 'c4', 'build_inputs.py'))
    E4 = importlib.util.module_from_spec(sp); sp.loader.exec_module(E4)
    E4.captions(tmp.name, dst); os.remove(tmp.name)


def out():
    import yaml
    F = os.path.join(EP, 'out', 'factory')
    W = os.path.join(EP, 'work', 'factory')
    tl = json.load(open(os.path.join(F, 'timeline.json')))
    roles = {r['id']: r.get('role') for r in script_rows()}
    sents = []
    for s in tl['sentences']:
        x = {k: s[k] for k in ('id', 'scene', 'text', 'spoken', 'start', 'end')}
        x['text'] = TAG.sub('', x['text'])   # chữ phụ đề/màn hình: không thẻ cảm xúc (spoken giữ nguyên chuỗi gửi TTS)
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
    # ident = 3 s cuối của cảnh mang nó (đuôi không lời): cold-open kết thúc ở đầu ident; cảnh đó ngắn lại 3 s + cảnh IDENT riêng
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
    takes = []
    for s in tl['scenes']:
        o = (Y.get('voice_overrides') or {}).get(s['id'], {})
        takes.append({'id': s['id'], 'raw': f"voice-takes/{scene_take(s['id'])}.mp3", 'final': 'out/audio/stems/voice.flac', 'model': o.get('model', v['model']),
                      'voiceId': o.get('voice', v['voice']), 'provider': 'elevenlabs', 'seed': o.get('seed', v['seed'])})
    os.makedirs(os.path.join(EP, 'out', 'voice'), exist_ok=True)
    json.dump({'takes': takes, 'voice': {'provider': 'elevenlabs', 'voiceId': v['voice'], 'model': v['model']}, 'build': rep.get('steps', {}).get('voice')},
              open(os.path.join(EP, 'out', 'voice', 'takes.json'), 'w'), indent=1)
    bj = os.path.join(ROOT, Y['audio']['music']) if os.path.isabs(Y['audio']['music']) else os.path.join(EP, Y['audio']['music'])
    if os.path.exists(bj + '.json'):   # lưới phách nhạc nền F-3 (bed.py) → tempo-map
        B = json.load(open(bj + '.json'))
        beats = B.get('beats') or B.get('grid', {}).get('beats') or []
        json.dump({'bpm': B.get('bpm', 114.0), 'beats': beats, 'accents': B.get('accents', [])}, open(os.path.join(EP, 'out', 'tempo-map.json'), 'w'))
    ev = []
    for w in Y.get('world') or []:   # sự kiện sfx của đoạn thế giới, giờ của tập (x = giữa khung: vật phát tiếng không có toạ độ màn hình riêng)
        sp = json.load(open(os.path.join(EP, w['dir'], 'spine.json')))
        t0 = next(s['start'] for s in tl['scenes'] if s['id'] == w['scenes'][0])
        ev += [{'t': round(t0 + e['t'], 3), 'x': 960, 'kind': e['kind']} for e in sp['events'] if e['kind'] != 'data']
    json.dump({'events': sorted(ev, key=lambda e: e['t'])}, open(os.path.join(EP, 'out', 'sfx-events.json'), 'w'))
    E4 = json.load(open(os.path.join(ROOT, 'episodes', 'ep004', 'out', 'rights.json')))['assets']
    voice = {**E4[0], 'name': 'voice: Eric (ElevenLabs premade, eleven_v3, seed 1005; S18 seed 1006)'}
    inter = next(a for a in E4 if a['kind'] == 'font')
    rights = {'assets': [voice,
        {'name': 'music bed (style C, generated by code from the tension map, F-3)', 'stems': ['music'], 'visuals': [], 'kind': 'music', 'origin': 'project code, no third-party samples (RIGHTS.md A-MUSIC); sliced per world segment (toolkit/factory/world/audio.py music_plan.bed)',
         'licence': 'own work', 'thirdParty': False, 'commercial': True, 'generator': 'episodes/ep005/world/music/bed.py'},
        {'name': 'data sounds, effects, camera-move whooshes and room tone (synthesised by code from the spine)', 'stems': ['sonify', 'sfx', 'whoosh', 'room'], 'visuals': [], 'kind': 'sfx', 'origin': 'project code, no samples',
         'licence': 'own work', 'thirdParty': False, 'commercial': True, 'generator': 'toolkit/factory/world/audio.py'},
        inter,
        {'name': '3D world, charts and cards drawn by code (three.js scene + 2D overlay)', 'stems': [], 'visuals': [WORLD3D], 'kind': 'model3d', 'origin': 'toolkit/factory/world/lib3d.js, core.js, episodes/ep005/world/obj5.js, c4kit.js, world/c4/*/scene.js; no model or texture files; three.js 0.186.1 (MIT) is code',
         'licence': 'own work', 'thirdParty': False, 'commercial': True, 'generator': 'toolkit/factory/world/lib3d.js'},
        {'name': 'three.js 0.186.1 (WebGL library that draws the 3D world; code, no model or texture files)', 'stems': [], 'visuals': [], 'kind': 'code',
         'origin': 'npm package three 0.186.1, toolkit/factory/world/vendor/package.json (npm ci; node_modules not committed)', 'licence': 'MIT', 'thirdParty': True, 'commercial': True,
         'terms': {'quote': 'Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software',
                   'url': 'https://github.com/mrdoob/three.js/blob/r186/LICENSE'}}]}
    json.dump(rights, open(os.path.join(EP, 'out', 'rights.json'), 'w'), indent=1, ensure_ascii=False)
    json.dump({'assets': [{'name': 'Inter', 'kind': 'font', 'family': 'Inter', 'paths': ['../../toolkit/render/fonts/inter-latin-*.woff2']},
                          {'name': WORLD3D, 'kind': 'model3d'}],   # C5: vật 3D dựng bằng mã lúc chạy (lib3d/obj5/c4kit), không file mô hình/texture
               'generated': [{'glob': 'work/world-data/derived.json', 'generator': 'world/derive.py'}]}, open(os.path.join(EP, 'out', 'visual-assets.json'), 'w'), indent=1)
    extras(Y, tl)
    print('out: script.json', len(sents), '· claims.json · captions.srt · timeline.json · adbreaks.json · video.mp4 · stems · takes.json')


def extras(Y, tl):
    """Artefact hợp đồng đo được từ chính bản dựng: tension-map (bản đồ căng F-3 + mức nhạc đo trên stem + mật độ âm/chuyển động từ spine),
    cues.json (ô nhịp nhạc nền), transitions.json (ranh giới đoạn thế giới), preprod/shotlist.json (cảnh render của spine), mô tả nháp (F10)."""
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
        samples.append({'t': round(float(t), 2), 'cutRate': sum(1 for m in mv if abs(m['t0'] - t) <= 30) * 2 / 60 * 60 / 2,
                        'audioDensity': sum(1 for e in ev if abs(e - t) <= 5) / 10, 'musicLevel': round(float(10 * np.log10(np.mean(seg ** 2) + 1e-12)), 1),
                        'tension': round(float(np.interp(t, *zip(*kf))), 3)})
    ten = [x['tension'] for x in samples]
    pk = [samples[i]['t'] for i in range(1, len(ten) - 1) if ten[i] >= ten[i - 1] and ten[i] > ten[i + 1] and ten[i] >= 0.7]
    va = [samples[i]['t'] for i in range(1, len(ten) - 1) if ten[i] <= ten[i - 1] and ten[i] < ten[i + 1] and ten[i] <= 0.35]
    json.dump({'samples': samples, 'peaks': [{'t': t} for t in pk], 'valleys': [{'t': t} for t in va],
               '_about': 'tension = F-3 tension map (world/music/tension.py); musicLevel = music stem dBFS (1 s); audioDensity = spine sfx/data events per s (±5 s); cutRate = camera moves per min (±30 s)'},
              open(os.path.join(EP, 'out', 'tension-map.json'), 'w'), indent=1)
    src = os.path.join(EP, 'review-c4', 'tension-map.png')
    if os.path.exists(src):
        shutil.copy(src, os.path.join(EP, 'out', 'tension-map.png'))
    json.dump({'cues': [{'t': b['t0'], 'end': b['t1'], 'function': {'A': 'act-1 bed', 'B': 'act-2/3 bed', 'C': 'landing'}.get(b['sec'], b['sec']), 'key': b['key'],
                         'tempo': round(240 / b['len'], 3), 'layer': '+'.join(b['layers'])} for b in B['bars']],
               'silences': [{'t': B['mr1_silence'][0], 'end': B['mr1_silence'][1], 'what': 'MR1'}]}, open(os.path.join(EP, 'out', 'cues.json'), 'w'), indent=1)
    cuts = []
    for a_, b_ in zip(Y['world'], Y['world'][1:]):
        t = next(s['start'] for s in tl['scenes'] if s['id'] == b_['scenes'][0])
        dip = a_['id'].startswith('a-')
        cuts.append({'t': round(t, 3), 'from': a_['id'], 'to': b_['id'], 'type': 'dissolve' if dip else 'cut', 'match': None if dip else 'geometric', 'audio': None,
                     'reason': 'ident: world dims to the channel mark, act 1 fades in from dark' if dip else 'segment boundary on a held camera: last frame of one segment = first frame of the next (same pose, same objects)'})
    json.dump({'cuts': cuts}, open(os.path.join(EP, 'out', 'transitions.json'), 'w'), indent=1)
    sh = [{'id': f"{m['seg']}:{m['id']}", 'scene': next(s['id'] for s in tl['scenes'] if s['start'] <= m['t0'] < s['start'] + s['dur']), 'size': 'world' if m['to'].startswith(('w', 'f')) else 'chart',
           'move': m['verb'] + (' (fly)' if m.get('style') == 'fly' else ''), 'moveReason': m['reason']} for m in mv]
    os.makedirs(os.path.join(EP, 'preprod'), exist_ok=True)
    json.dump({'shots': sh}, open(os.path.join(EP, 'preprod', 'shotlist.json'), 'w'), indent=1, ensure_ascii=False)
    os.makedirs(os.path.join(EP, 'out', 'package'), exist_ok=True)
    acts = {a['id']: a for a in json.load(open(os.path.join(EP, 'out', 'timeline.json')))['acts']}
    mmss = lambda t: f'{int(t // 60)}:{int(t % 60):02d}'
    ch = [('cold-open', 'The question: buy with 10% down, or wait for 20%?'), ('act1', 'What mortgage insurance is, and the law\'s two dates'),
          ('act2', 'Replaying every purchase month, 1991 to 2016'), ('act3', 'Three illustrative buyers'), ('method', 'How we know this'), ('outro', 'Back to the question')]
    CL = {c['claimId']: c for c in json.load(open(os.path.join(EP, 'out', 'claims.json')))['claims']}
    dsp = lambda k: CL[k]['display']
    # C5 (G2 package): pasted verbatim into YouTube; title T1 lives in out/package/package.json + HUONG-DAN-DANG.md. REVIEWER R1: no premium amount.
    desc = [f"How long did mortgage insurance last for a buyer who put 10% down? We replayed every US purchase month from {dsp('firstB')} to {dsp('lastB')} "
            "and asked when the loan reached 80% of the home's value on paper, by a national price index, against the payment schedule the law uses. "
            f"The typical answer: {dsp('medianB_months_to80')} months on paper. On paper is not the same as the insurance being removed. "
            "US only · history, not a forecast. This video does not say whether to buy, rent or wait.",
            'Owen, Grace and Victor are ILLUSTRATIVE buyers built from real purchase months.', '',
            'Chapters'] + [f"{mmss(acts[a]['start'])} {txt}" for a, txt in ch if a in acts] + ['',
            'Method and sources',
            '- Mortgage rates: Freddie Mac PMMS 30-year fixed, weekly (FRED MORTGAGE30US, https://fred.stlouisfed.org/series/MORTGAGE30US), monthly mean; cross-check: Optimal Blue 30-year conforming (FRED OBMMIC30YF).',
            '- Home prices: FHFA purchase-only house price index, United States, not seasonally adjusted (FRED HPIPONM226N, https://fred.stlouisfed.org/series/HPIPONM226N); cross-check: S&P Cotality Case-Shiller U.S. National Home Price Index (FRED CSUSHPINSA). Illustrative price from the Census/HUD median sales price (FRED MSPUS).',
            f"- The loan: 10% down, 30-year fixed at each purchase month's rate. \"On paper\" = the balance is at or under 80% of the purchase price times the national index change since purchase; no single home tracks the index. {dsp('nB')} purchase months ({dsp('firstB')} to {dsp('lastB')}, each with ten years of prices after it); the two-year check uses {dsp('nA')} purchase months ({dsp('firstA')} to {dsp('lastA')}).",
            '- The law: Homeowners Protection Act, 12 U.S.C. 4901 (cancellation and termination dates) and 12 U.S.C. 4902 (the borrower may ask to cancel when the scheduled balance reaches 80% of the original value; it ends automatically at 78% if payments are current). https://www.law.cornell.edu/uscode/text/12/4902',
            "- Removal on today's value is the loan owner's rule, not the law. For Fannie Mae loans only: Fannie Mae Servicing Guide B-8.1-04 (a waiting period and, in the early years, a 75% bar). Other investors and lenders set their own rules. https://servicing-guide.fanniemae.com/svc/b-8.1-04/termination-conventional-mortgage-insurance",
            '- CFPB: "When can I remove private mortgage insurance (PMI) from my loan?" https://www.consumerfinance.gov/ask-cfpb/when-can-i-remove-private-mortgage-insurance-pmi-from-my-loan-en-202/ and "What is private mortgage insurance?" https://www.consumerfinance.gov/ask-cfpb/what-is-private-mortgage-insurance-en-122/',
            '', 'Not modeled: what the insurance costs (this video puts no dollar figure on it), appraisals and fees, rent, local prices, how fast savings grow, missed payments, each lender\'s or investor\'s own rules.',
            '', 'US only · history, not a forecast. Not advice.']
    json.dump({'title': '10% Down and Mortgage Insurance: How Long Did It Last?', 'titleId': 'T1 (G1, approved)', 'description': 'out/package/description.md',
               'thumbnails': [f'out/package/thumb-{n}.png' for n in (1, 2, 3)], 'thumbnailSidecars': [f'out/package/thumb-{n}.json' for n in (1, 2, 3)],
               'thumbnailsMadeBy': 'design/g2/thumbs.js', 'r1': 'no mortgage-insurance premium amount in title, description or thumbnails'},
              open(os.path.join(EP, 'out', 'package', 'package.json'), 'w'), indent=1, ensure_ascii=False)
    open(os.path.join(EP, 'out', 'package', 'description.md'), 'w', encoding='utf-8').write('\n'.join(desc) + '\n')


def scene_take(sc):
    sys.path.insert(0, os.path.join(EP, 'world'))
    import wlib
    return wlib.voice_scenes()[sc]['take'].replace('.mp3', '')


if __name__ == '__main__':
    main()
