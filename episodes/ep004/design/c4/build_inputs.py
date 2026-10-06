"""Tập 4 · C4: đầu vào nhà máy cho cả tập + artefact hợp đồng (chạy lại được, không sửa tay file sinh ra).
  python3 episodes/ep004/design/c4/build_inputs.py            # trước build.sh
  python3 episodes/ep004/design/c4/build_inputs.py --out      # sau build.sh: out/script.json (thời điểm thật + role), out/claims.json, ...
Vào:  story/script.md, numbers.md, out/model.json (raw = chưa làm tròn; rounded = hiển thị), data/*.csv (fetch.py; không commit),
      design/c3/build_inputs.py (cách dựng display, dữ liệu N1/N2), topics-r1/machine/tax-2/sources.json.
Ra:   design/c4/gen/script.json (role hook/promise), gen/claims.json (value chưa làm tròn, display như C3), data/sources.json,
      design/c4/work/data.js (không commit: chuỗi FRED). --out: out/script.json, out/claims.json, out/captions.srt, out/timeline.json,
      out/adbreaks.json (từ out/factory/timeline.json + episode.yaml midrolls)."""
import csv, importlib.util, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.abspath(os.path.join(HERE, '..', '..'))
ROOT = os.path.abspath(os.path.join(EP, '..', '..'))
spec = importlib.util.spec_from_file_location('c3', os.path.join(EP, 'design', 'c3', 'build_inputs.py'))
C3 = importlib.util.module_from_spec(spec); spec.loader.exec_module(C3)

ROLES = {'S01.1': 'hook', 'S01.3': 'promise'}           # hooks.md H2: stake = H2.1, promise = H2.3
METROS = ['los_angeles', 'san_diego', 'san_francisco', 'san_jose', 'seattle', 'boston', 'new_york', 'miami', 'denver', 'phoenix',
          'dallas', 'chicago']
FILES = {'los_angeles': 'ATNHPIUS31084Q', 'san_diego': 'ATNHPIUS41740Q', 'san_francisco': 'ATNHPIUS41884Q', 'san_jose': 'ATNHPIUS41940Q',
         'seattle': 'ATNHPIUS42644Q', 'boston': 'ATNHPIUS14454Q', 'new_york': 'ATNHPIUS35614Q', 'miami': 'ATNHPIUS33124Q',
         'denver': 'ATNHPIUS19740Q', 'phoenix': 'ATNHPIUS38060Q', 'dallas': 'ATNHPIUS19124Q', 'chicago': 'ATNHPIUS16984Q', 'us': 'USSTHPI'}


def script():
    s = C3.script()
    for x in s['sentences']:
        if x['id'] in ROLES:
            x['role'] = ROLES[x['id']]
    return s


def uses():
    """claim → sentences that carry it (script.md claim column) and scenes."""
    sp = {}
    for ln in open(os.path.join(EP, 'story', 'script.md'), encoding='utf-8'):
        m = re.match(r'^(S\d+)\.(\d+) \| .+? \| ([^|]*) \|', ln)
        if m:
            for cid in re.findall(r'[a-z0-9_]+', m[3]):
                sp.setdefault(cid, []).append({'scene': m[1], 'sentence': f'{m[1]}.{m[2]}'})
    return sp


def claims(model, shown):
    raw, sp = model['raw'], uses()
    out = []
    for c in C3.claims(model)['claims']:
        cid = c['claimId']
        v = raw.get(cid, c['value'])
        if isinstance(v, str):
            try:
                v = float(v) if '.' in v or v.isdigit() else v
            except ValueError:
                pass
        if cid == 'sale_quarter':
            v = model['params']['saleQuarter']
        x = {'claimId': cid, 'value': v, 'display': c['display'], 'unit': c['unit'], 'formula': c['unit'],
             'source': {'id': 'model', 'url': None} if cid in raw else {'id': 'numbers.md', 'url': None},
             'historical': c['historical'], 'illustrative': c['illustrative']}
        if c['historical']:
            x['dataYears'] = [1997, 2026] if cid.startswith(('cpi_', 'excl_joint_1997')) else [2000, 2026]
        if '$' in str(c['display']) or cid.startswith(('threshold_', 'gain_at_', 'illustrative_price_', 'excl_')) and 'month' not in cid:
            x['basis'] = 'nominal'
        if cid.startswith(('threshold_', 'gain_at_', 'cross_quarter_at_', 'stay_quarter_at_', 'metros_')):
            x['conditional'] = 'like-average'
        if cid.startswith(('gain_at_', 'cross_quarter_at_', 'stay_quarter_at_')):
            x['character'] = 'rosa_frank' if cid.endswith('_phoenix') and '200k' in cid else None
            if not x['character']:
                del x['character']
        x['callbacks'] = []
        x['shownIn'] = sorted(shown.get(cid, []))
        x['spoken'] = sp.get(cid, [])
        out.append(x)
    return {'claims': out}


def quarterly(sid):
    rows = list(csv.reader(open(os.path.join(EP, 'data', FILES[sid] + '.csv'))))[1:]
    return [(d[:7], float(v)) for d, v in rows if v.strip() not in ('', '.')]


def data(model):
    d = C3.data(model)
    P = model['params']
    y0 = str(P['buyYear'])
    for sid in METROS:
        q = quarterly(sid)
        base = sum(v for k, v in q if k.startswith(y0)) / 4
        q = [(k, v) for k, v in q if k >= f'{y0}-01' and k <= P['saleQuarter'][:7]]
        d.setdefault('index', {})[sid] = [{'x': k, 'y': v} for k, v in q]
        for price in (200000, 300000):
            d.setdefault(f'gain{price // 1000}', {})[sid] = [{'x': k, 'y': price * (v / base - 1)} for k, v in q]
    return d


def sources():
    S = json.load(open(os.path.join(ROOT, 'topics-r1', 'machine', 'tax-2', 'sources.json')))
    files = [{'path': s['file'], 'role': 'primary', 'url': s['url'], 'sha256': s['sha256'], 'downloaded': s['retrieved'],
              'terms': s['terms'], 'series': s['id']} for s in S['series']]
    return {'files': files, 'mismatches': [],
            '_about': 'FRED (FHFA all-transactions HPI, CPI-U); copies re-fetched by data/fetch.py --verify (SHA-256 above). '
                      'No second source reachable for the FHFA indexes (fhfa.gov blocked by the proxy): no cross-check file.'}


def shown_in():
    """claim → scenes whose shots name it in episode.yaml ({id} or claim keys) or whose counterweight it triggers."""
    import yaml
    sys.path.insert(0, os.path.join(ROOT, 'toolkit', 'factory'))
    import spec as SPEC
    Y = yaml.safe_load(open(os.path.join(EP, 'episode.yaml')))
    out = {}
    for sc in Y.get('scenes', []):
        for sh in sc.get('shots', []):
            for cid in SPEC.claim_ids_in(sh.get('p', {})):
                out.setdefault(cid, set()).add(sc['id'])
            for it in (sh.get('p', {}).get('items') or []):
                out.setdefault(it['claim'], set()).add(sc['id'])
    return {k: sorted(v) for k, v in out.items()}


def main():
    model = json.load(open(os.path.join(EP, 'out', 'model.json')))
    gen, work = os.path.join(HERE, 'gen'), os.path.join(HERE, 'work')
    os.makedirs(gen, exist_ok=True); os.makedirs(work, exist_ok=True)
    cl = claims(model, shown_in())
    json.dump(script(), open(os.path.join(gen, 'script.json'), 'w'), indent=1, ensure_ascii=False)
    json.dump(cl, open(os.path.join(gen, 'claims.json'), 'w'), indent=1, ensure_ascii=False)
    json.dump(sources(), open(os.path.join(EP, 'data', 'sources.json'), 'w'), indent=1, ensure_ascii=False)
    col = json.load(open(os.path.join(EP, 'design', 'c3', 'gen', 'tokens.json')))['color']   # contract tokens (V09, P01): same palette
    json.dump({'colors': {**col, 'muted': col['ink-muted']}, 'series': {'cap': col['ink-muted'], 'gain': col['ink'], 'above': col['warn'],
               'index': col['accent']}, 'seriesOf': {}}, open(os.path.join(EP, 'design', 'tokens.json'), 'w'), indent=1)
    open(os.path.join(work, 'data.js'), 'w').write('const DATA = ' + json.dumps(data(model)) + ';\n')
    print('script', len(script()['sentences']), '· claims', len(cl['claims']))
    if '--out' in sys.argv:
        out()


def captions(src, dst):
    """Factory captions, with a cue shorter than 1 s (sentence tail) merged into the cue before it when the two fit 2 × 42 chars
    and 7 s (F09). Else the cue starts earlier, taken from the cue before (≤ 0,3 s here). Same words, same order; only cue boundaries move."""
    sys.path.insert(0, os.path.join(ROOT, 'toolkit', 'factory'))
    from build import wrap, srt_time
    ts = lambda s: sum(float(x) * m for x, m in zip(s.replace(',', '.').split(':'), (3600, 60, 1)))
    cues = []
    for blk in open(src).read().strip().split('\n\n'):
        L = blk.split('\n')
        a, b = L[1].split(' --> ')
        cues.append({'s': ts(a), 'e': ts(b), 'text': ' '.join(L[2:])})
    out, merged = [], 0
    for c in cues:
        if out and c['e'] - c['s'] < 1.0:
            p = out[-1]; t = p['text'] + ' ' + c['text']
            if len(wrap(t)) <= 2 and c['e'] - p['s'] <= 7.0:
                p['text'], p['e'] = t, c['e']; merged += 1
                continue
            need = 1.0 - (c['e'] - c['s']) + 0.002            # else start it earlier: the cue before gives up the time (stays ≥ 1 s)
            if p['e'] - p['s'] - need >= 1.0:
                c = dict(c); c['s'] -= need; p['e'] = c['s'] - 0.001; merged += 1
        out.append(dict(c))
    with open(dst, 'w') as f:
        for i, c in enumerate(out, 1):
            f.write(f"{i}\n{srt_time(c['s'])} --> {srt_time(c['e'])}\n" + '\n'.join(wrap(c['text'])) + '\n\n')
    print('captions:', len(cues), '→', len(out), 'cues (merged', merged, ')')


def out():
    """Contract artefacts from the factory build (out/factory/timeline.json): sentence times are the real ones of the master."""
    import shutil, yaml
    F = os.path.join(EP, 'out', 'factory')
    tl = json.load(open(os.path.join(F, 'timeline.json')))
    sents = []
    for s in tl['sentences']:
        x = {k: s[k] for k in ('id', 'scene', 'text', 'spoken', 'start', 'end')}
        if s['id'] in ROLES:
            x['role'] = ROLES[s['id']]
        sents.append(x)
    json.dump({'sentences': sents}, open(os.path.join(EP, 'out', 'script.json'), 'w'), indent=1, ensure_ascii=False)
    shutil.copy(os.path.join(HERE, 'gen', 'claims.json'), os.path.join(EP, 'out', 'claims.json'))
    captions(os.path.join(F, 'captions.srt'), os.path.join(EP, 'out', 'captions.srt'))
    Y = yaml.safe_load(open(os.path.join(EP, 'episode.yaml')))
    acts = Y.get('acts') or []
    sc = {s['id']: s for s in tl['scenes']}
    A = []
    for a in acts:
        ids = a['scenes']
        A.append({'id': a['id'], 'start': sc[ids[0]]['start'], 'end': round(sc[ids[-1]]['start'] + sc[ids[-1]]['dur'], 4)})
    scenes = [{'id': s['id'], 'start': s['start'], 'dur': s['dur'], 'end': round(s['start'] + s['dur'], 4),
               'act': next((a['id'] for a in acts if s['id'] in a['scenes']), None)} for s in tl['scenes']]
    json.dump({'fps': tl['fps'], 'total': tl['total'], 'acts': A, 'scenes': scenes}, open(os.path.join(EP, 'out', 'timeline.json'), 'w'), indent=1)
    json.dump({'breaks': [m['t'] for m in Y.get('midrolls') or []]}, open(os.path.join(EP, 'out', 'adbreaks.json'), 'w'), indent=1)
    # master + voice stem + takes (video and stems are not committed: .gitignore / work/)
    W = os.path.join(EP, 'work', 'factory')
    # F03: the picture has ≤ 3 frames fewer than the mix (segment rounding): cut the audio to the picture length (copy, no re-encode)
    import subprocess
    vd = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=duration', '-of', 'csv=p=0',
                         os.path.join(W, 'video.mp4')], capture_output=True, text=True, check=True).stdout.strip()
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', os.path.join(W, 'video.mp4'), '-map', '0', '-c', 'copy', '-t', vd,
                    '-movflags', '+faststart', os.path.join(EP, 'out', 'video.mp4')], check=True)
    os.makedirs(os.path.join(EP, 'out', 'audio', 'stems'), exist_ok=True)
    for st in os.listdir(os.path.join(W, 'stems')):
        shutil.copy(os.path.join(W, 'stems', st), os.path.join(EP, 'out', 'audio', 'stems', st))
    os.makedirs(os.path.join(EP, 'out', 'shorts'), exist_ok=True)
    for sh in Y.get('shorts') or []:
        p = os.path.join(W, sh['id'] + '.mp4')
        if os.path.exists(p):
            shutil.copy(p, os.path.join(EP, 'out', 'shorts', sh['id'] + '.mp4'))
    rep = json.load(open(os.path.join(F, 'build-report.json')))
    v = Y['voice']
    takes = [{'id': s['id'], 'final': 'out/audio/stems/voice.flac', 'model': v['model'], 'voiceId': v['voice'], 'provider': 'elevenlabs',
              'seed': v['seed']} for s in tl['scenes']]
    os.makedirs(os.path.join(EP, 'out', 'voice'), exist_ok=True)
    json.dump({'takes': takes, 'build': rep.get('steps', {}).get('voice')}, open(os.path.join(EP, 'out', 'voice', 'takes.json'), 'w'), indent=1)
    print('out: script.json', len(sents), '· claims.json · captions.srt · timeline.json · adbreaks.json')


if __name__ == '__main__':
    main()
