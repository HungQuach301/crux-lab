"""Tập 9 · M2/M3: đầu vào nhà máy cho cả tập + artefact hợp đồng (chạy lại được, không sửa tay file sinh ra). Mẫu: episodes/ep006/prod/build_inputs.py.
  python3 episodes/ep009/prod/build_inputs.py              # prod/gen/{script,claims,tokens,data}.json + design/tokens.json
  python3 episodes/ep009/prod/build_inputs.py --timeline   # + timeline KHÔ của nhà máy (spec-free: load_inputs → voice → resolve, 0 ký tự EL:
                                                         #   dừng nếu một cảnh không trúng take trong voice-takes/) → out/factory/timeline.json,
                                                         #   captions.srt; rồi nhạc nền work/factory/music/bed.wav (audio.music_cmd) nếu chưa có
  python3 episodes/ep009/prod/build_inputs.py --out        # sau build.sh: out/{script,claims,timeline,adbreaks}.json, out/captions.srt, out/video.mp4,
                                                         #   out/audio/stems/*, out/voice/takes.json, out/tempo-map.json, out/sfx-events.json, …
Vào:  story/script.md (lời + vai), numbers.md (hiển thị), out/model.json (quantities[k].value = CHƯA làm tròn → claims.json; claim ID = khoá
      quantities, contract.json không có model.claims), world/claims.json (chuỗi trên hình của thế giới: display + claim phụ `of` — derive.py),
      contract.json (claims: illustrative/core/decisive/conditions), episode.yaml (acts, midrolls, world), out/factory/timeline.json (sau build).
Lời: chữ câu = đúng script.md (kể cả thẻ cảm xúc eleven_v3 — khoá take = SHA-256 của chữ đã nói); phụ đề bỏ thẻ cảm xúc."""
import hashlib, json, os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.dirname(HERE)
ROOT = os.path.abspath(os.path.join(EP, '..', '..'))
GEN = os.path.join(HERE, 'gen')
LINE = re.compile(r'^(S\d\d)\.(\d+)\s+(?:\{(\w+)\}\s+)?(.+?)\s*<!--\s*claims:\s*([^;>]*?)\s*(?:;[^>]*)?-->')
TAG = re.compile(r'^\[[a-z ]+\]\s+')
ROLE_KEEP = ('hook', 'promise')          # out/script.json: role ∈ hook, promise (checks/CONTRACT.md, S18)
LEO = 'leo_'   # không dùng ở Tập 9
TESSA = tuple(json.load(open(os.path.join(EP, 'contract.json')))['claims']['illustrative'])   # claim minh hoạ của Nina
WORLD3D = '3D world objects drawn by code (lib3d.js W1–W5, w8.js/w9.js N1 Street / N2 RentTag / N3 NinaLamp / N4 GlassBox / N6 StockPile)'


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
    """numbers.md cột Hiển thị, bỏ phần trong ngoặc cuối (dạng ngắn trên hình)."""
    disp = {}
    for ln in open(os.path.join(EP, 'numbers.md'), encoding='utf-8'):
        m = re.match(r'^\| `(\w+)` \| ([^|]*) \| ([^|]*) \|', ln)
        if m:
            disp[m[1]] = re.sub(r'\s*\(.*\)$', '', m[3].strip()).strip()
    return disp


def claims():
    C = json.load(open(os.path.join(EP, 'contract.json')))
    M = json.load(open(os.path.join(EP, 'out', 'model.json')))
    Q = M['quantities']
    W = {k: v for k, v in json.load(open(os.path.join(EP, 'world', 'claims.json'))).items() if not k.startswith('_')}
    CC = C.get('claims') or {}
    ill = set(CC.get('illustrative', []))
    cond = {}   # một claim mang MỘT cờ (checks S17): điều kiện khai trước thắng
    for x in CC.get('conditions', []):
        for c in x.get('claims', []):
            cond.setdefault(c, x['id'])
    core, decisive = set(CC.get('core', [])), set(CC.get('decisive', []))
    disp = numbers_display()
    spoken = {}
    for r in script_rows():
        for c in r['_claims']:
            spoken.setdefault(c, []).append({'scene': r['scene'], 'sentence': r['id']})
    out = []
    for cid, q in Q.items():
        d = W[cid]['display'] if cid in W else disp.get(cid, str(q['value']))   # số nội bộ không có dòng numbers.md (hpi_last…): không lên hình
        x = {'claimId': cid, 'value': q['value'], 'display': d, 'unit': q.get('unit'), 'formula': q.get('definition'),
             'source': {'id': 'model', 'url': None}, 'historical': True, 'dataYears': [1991, 2026], 'illustrative': cid in ill}
        ch = 'nina' if cid in TESSA else None
        if ch:
            x['character'] = ch
            x['illustrative'] = True
        for k, flag in (('conditional', cid in cond), ('core', cid in core), ('decisive', cid in decisive)):
            if flag:
                x[k] = cond[cid] if k == 'conditional' else True
        x.update(callbacks=[], shownIn=[], spoken=spoken.get(cid, []))
        out.append(x)
    # claim phụ của thế giới (derive.py): cùng giá trị một claim mô hình / tham số, chuỗi trên hình khác (`of`)
    for cid, w in W.items():
        if cid in Q:
            continue
        of = w.get('of', 'params.' + cid)
        src = of if of.startswith('params.') else 'model'
        base = Q.get(of)
        x = {'claimId': cid, 'value': w['value'], 'display': w['display'], 'unit': 'const' if base is None else base.get('unit'),
             'formula': f"same quantity as {of}: {w['display_full']}", 'source': {'id': 'model' if src == 'model' else 'contract.json', 'url': None},
             'historical': base is not None, 'illustrative': of in TESSA, 'of': of,
             'callbacks': [], 'shownIn': [], 'spoken': spoken.get(cid, [])}
        if base is not None:
            x['dataYears'] = [1991, 2026]
            if of in cond and cid not in cond:
                x['conditional'] = cond[of]
        if cid in cond:
            x['conditional'] = cond[cid]
        if x['illustrative']:
            x['character'] = 'nina'
        out.append(x)
    for x in out:   # G2 câu 6 (checks S09): mọi số $ là đô la danh nghĩa (mô hình không hiệu chỉnh lạm phát)
        if '$' in str(x['display']):
            x['basis'] = 'nominal'
    ids = [c['claimId'] for c in out]
    assert len(ids) == len(set(ids)), 'claimId trùng'
    return {'claims': out}


def tokens():
    T = json.load(open(os.path.join(ROOT, 'toolkit', 'visual-library', 'tokens.json')))
    col = T.get('color') or T.get('colors')
    C_ = json.load(open(os.path.join(EP, 'contract.json')))
    chars = {f'char-{k}': v['color'] for k, v in (C_.get('characters') or {}).items() if isinstance(v, dict) and v.get('color')}
    # vai màu E2 (beats.md Colour roles): buyer = lit (ấm, cửa sổ sáng N1) · renter = warn (cửa tối, hộp tiền mặt) · accent = dữ liệu thị trường ·
    # ink = Nina/nhà/người · ink-muted = vật cố định (thẻ tiền thuê giả định, mức chi sở hữu)
    return {'color': col, 'colors': {**col, 'muted': col.get('ink-muted', '#9AA4B2'), 'lit': '#F6D58E', **chars},
            'series': {'buyer': '#F6D58E', 'renter': col['warn'], 'market': col['accent'], 'fixed': col.get('ink-muted', '#9AA4B2')}, 'seriesOf': {}}


def main():
    os.makedirs(GEN, exist_ok=True)
    rows = script_rows()
    sc = {'sentences': [{k: v for k, v in r.items() if not k.startswith('_')} for r in rows]}
    json.dump(sc, open(os.path.join(GEN, 'script.json'), 'w'), indent=1, ensure_ascii=False)
    cl = claims()
    json.dump(cl, open(os.path.join(GEN, 'claims.json'), 'w'), indent=1, ensure_ascii=False)
    tk = tokens()
    json.dump(tk, open(os.path.join(GEN, 'tokens.json'), 'w'), indent=1)
    json.dump({'_about': 'Tập 9: mọi cảnh là đoạn thế giới 3D (world:); nhà máy 2D không cần dữ liệu'}, open(os.path.join(GEN, 'data.json'), 'w'))
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
    yml = os.path.join(EP, os.environ.get('CRUX_YAML', 'episode.yaml'))   # M2 animatic: animatic.yaml (take khô, prod/dry_takes.py)
    Y = yaml.safe_load(open(yml))
    rows = script_rows()
    miss, vsc = [], {}
    for s in Y['scenes']:
        cfg = VOICE.scene_cfg(Y['voice'], Y.get('voice_overrides'), s['id'])
        text = ' '.join(VOICE.to_spoken([r['text'] for r in rows if r['scene'] == s['id']]))
        key = hashlib.sha256(json.dumps([text, cfg['voice'], cfg['model'], cfg['seed'], cfg.get('settings', {'stability': 0.5, 'speed': 0.9})],
                                        sort_keys=True).encode()).hexdigest()[:16]
        name = cfg['take'] if cfg.get('take') else key
        if not os.path.exists(os.path.join(EP, 'voice-takes', name + '.mp3')):
            miss.append((s['id'], key))
        else:
            vsc[s['id']] = {'take': name + '.mp3', 'duration': float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0',
                            os.path.join(EP, 'voice-takes', name + '.mp3')], capture_output=True, text=True).stdout), 'dry': name.startswith('dry-')}
    if miss:
        raise SystemExit(f'take không có trong voice-takes/ (lệch băm) — DỪNG, không sinh giọng: {miss}')
    os.makedirs(os.path.join(EP, 'work', 'factory'), exist_ok=True)
    json.dump(vsc, open(os.path.join(EP, 'work', 'factory', 'voice-scenes.json'), 'w'), indent=1)   # wlib.scene_take
    B = BUILD.Build(yml, [yml])
    B.load_inputs()
    v = B.do_voice()
    assert v['el_chars_spent'] == 0 and v['cache_hits'] == len(Y['scenes']), v
    r = B.do_resolve()
    print(f"timeline: {r['total']} s ({int(r['total'] // 60)}:{r['total'] % 60:04.1f}) · voice {v['cache_hits']}/{len(Y['scenes'])} cache · EL 0")
    bed = os.path.join(EP, Y['audio']['music'])
    if not os.path.exists(bed) or '--bed' in sys.argv:
        subprocess.run(Y['audio']['music_cmd'].format(total=r['total'], out=bed), shell=True, cwd=ROOT, check=True)


def captions(src, dst):
    """Phụ đề nhà máy, bỏ thẻ cảm xúc eleven_v3, gộp cue < 1 s như Tập 4–6 (episodes/ep004/design/prod/build_inputs.py captions)."""
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
    """Như Tập 6 (episodes/ep006/prod/build_inputs.py out): artefact hợp đồng từ chính bản dựng; ident = cảnh IDENT 3 s riêng."""
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
    voice = {**E4[0], 'name': f"voice: Eric (ElevenLabs premade, {v['model']}, seed {v['seed']})"}
    inter = next(a for a in E4 if a['kind'] == 'font')
    rights = {'assets': [voice,
        {'name': 'music bed (style C, one cue per act, generated by code from the tension map, F-3) + channel ident A and closing cue A (F-12)', 'stems': ['music'],
         'visuals': [], 'kind': 'music', 'origin': 'project code, no third-party samples (episodes/ep009/world/music/bed.py, toolkit/factory/theme/)',
         'licence': 'own work', 'thirdParty': False, 'commercial': True, 'generator': 'episodes/ep009/world/music/bed.py'},
        {'name': 'data sounds, effects, camera-move whooshes and room tone (synthesised by code from the spine)', 'stems': ['sonify', 'sfx', 'whoosh', 'room'],
         'visuals': [], 'kind': 'sfx', 'origin': 'project code, no samples', 'licence': 'own work', 'thirdParty': False, 'commercial': True,
         'generator': 'toolkit/factory/world/audio.py'},
        inter,
        {'name': '3D world, charts and cards drawn by code (three.js scene + 2D overlay)', 'stems': [], 'visuals': [WORLD3D], 'kind': 'model3d',
         'origin': 'toolkit/factory/world/lib3d.js, core.js, episodes/ep009/world/obj7.js, kit.js, world/seg/*/scene.js; no model or texture files; three.js 0.186.1 (MIT) is code',
         'licence': 'own work', 'thirdParty': False, 'commercial': True, 'generator': 'toolkit/factory/world/lib3d.js'},
        {'name': 'three.js 0.186.1 (WebGL library that draws the 3D world; code, no model or texture files)', 'stems': [], 'visuals': [], 'kind': 'code',
         'origin': 'npm package three 0.186.1, toolkit/factory/world/vendor/package.json (npm ci; node_modules not committed)', 'licence': 'MIT',
         'thirdParty': True, 'commercial': True,
         'terms': {'quote': 'Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software',
                   'url': 'https://github.com/mrdoob/three.js/blob/r186/LICENSE'}}]}
    json.dump(rights, open(os.path.join(EP, 'out', 'rights.json'), 'w'), indent=1, ensure_ascii=False)
    json.dump({'assets': [{'name': 'Inter', 'kind': 'font', 'family': 'Inter', 'paths': ['../../toolkit/render/fonts/inter-latin-*.woff2']},
                          {'name': WORLD3D, 'kind': 'model3d'}],
               'generated': [{'glob': 'world/claims.json', 'generator': 'world/derive.py'}]}, open(os.path.join(EP, 'out', 'visual-assets.json'), 'w'), indent=1)
    extras(Y, tl)
    # M6: Short nhà máy (work/factory/SH*.mp4 + nhật ký khung) → out/shorts/ (contract.json shorts[].file)
    import glob as _gl, shutil as _sh
    for f in sorted(_gl.glob(os.path.join(EP, 'work', 'factory', 'SH[0-9].mp4'))) + sorted(_gl.glob(os.path.join(EP, 'work', 'factory', 'SH[0-9]-frame-log.json'))):
        os.makedirs(os.path.join(EP, 'out', 'shorts'), exist_ok=True); _sh.copy2(f, os.path.join(EP, 'out', 'shorts', os.path.basename(f)))
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
