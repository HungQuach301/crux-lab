"""Crux factory spec check (Mốc B): episode.yaml against playbook/episode.md §5, §9 and CHARTER §5, before any API call or render.

  python3 toolkit/factory/spec.py episodes/epNNN/episode.yaml [--duration <s>]   → prints problems, exit 1 if any is blocking

check(spec, root, duration=None) -> [{'level': 'BLOCK'|'ASK'|'WARN', 'rule', 'msg'}]
  BLOCK  the build stops (missing claim, unknown template, format maximum, bad mid-roll …)
  ASK    an exception the owner must decide: build stops and the reason goes to the issue (none at present)
  WARN   reported in qc (101 below its soft minimum: "không độn", so never padded)
"""
import json
import os
import re
import sys

import yaml

FORMATS = {'lab': {'min': 540, 'max': 660, 'midrolls': 2}, '101': {'min': 480, 'max': 540, 'midrolls': 1}}
TEMPLATES = {'title', 'bignum', 'bars', 'line', 'swarm', 'paths', 'timeline', 'method', 'person', 'endcard'}
ANCHOR = re.compile(r'^@(?P<sid>[A-Za-z0-9]+\.\d+)(?P<end>\$)?(?::(?P<word>[^+]+?))?(?:\+(?P<off>[\d.]+))?$')


def claim_ids_in(v):
    """Claim ids named in a param value: {id} placeholders and claim/level/gate/gateDef keys."""
    out = set()
    if isinstance(v, str):
        out |= set(re.findall(r'\{([a-z0-9_]+)\}', v, re.I))
    elif isinstance(v, list):
        for x in v:
            out |= claim_ids_in(x)
    elif isinstance(v, dict):
        for k, x in v.items():
            if k in ('claim', 'level', 'gateDef') or (k == 'gate' and isinstance(x, str)):
                out.add(x)
            else:
                out |= claim_ids_in(x)
    return out


def anchors_in(v):
    if isinstance(v, str):
        return [v] if v.startswith('@') else []
    if isinstance(v, list):
        return [a for x in v for a in anchors_in(x)]
    if isinstance(v, dict):
        return [a for x in v.values() for a in anchors_in(x)]
    return []


def required_counterweights(spec, root):
    """What the dossier says must be on screen: script counterweight labels (scenes built here), claim-risk "Always say", contract
    assumptions (regex). Returns [{'src', 'text' | 'pattern'}]."""
    D, built, req = spec.get('dossier') or {}, {sc['id'] for sc in spec.get('scenes', [])}, []
    sm = os.path.join(root, D.get('script_md', 'story/script.md'))
    if os.path.exists(sm):
        for ln in open(sm, encoding='utf-8'):
            m = re.match(r'^(S\d+)\.\d+\s*\|', ln)
            for t in re.findall(r'[Cc]ounterweight[^"]*"([^"]+)"', ln):
                if m and m[1] in built:
                    req.append({'src': f'{os.path.basename(sm)} {ln.split("|")[0].strip()}', 'text': t})
    if D.get('claim_risk'):
        cr = os.path.join(root, D['claim_risk'])
        for t in re.findall(r'Always say "([^"]+)"', open(cr, encoding='utf-8').read()):
            req.append({'src': os.path.relpath(cr, root), 'text': t})
    ct = os.path.join(root, D.get('contract', 'contract.json'))
    if os.path.exists(ct):
        for a in json.load(open(ct)).get('claims', {}).get('assumptions', []):
            req.append({'src': f"contract.json assumption {a['id']}", 'pattern': a['pattern']})
    return req


def strings_in(v):
    if isinstance(v, str):
        return [v]
    if isinstance(v, list):
        return [s for x in v for s in strings_in(x)]
    if isinstance(v, dict):
        return [s for x in v.values() for s in strings_in(x)]
    return []


def counterweights(spec, root, claims):
    """counterweights: REQUIRED field. Every line the dossier demands must be declared (a contract assumption may instead be met by a
    visible shot string, e.g. the what-if legend); every declared line needs a trigger the engine can test on each frame."""
    P, add = [], None
    add = lambda level, msg: P.append({'level': level, 'rule': 'counterweights', 'msg': msg})
    if 'counterweights' not in spec:
        add('BLOCK', 'missing required field `counterweights` (list of {id, text, claims | when}); see playbook §5 / factory README')
        return P
    cws = spec.get('counterweights') or []
    norm = lambda t: re.sub(r'\s+', ' ', t.strip().lower())
    texts = [norm(c.get('text', '')) for c in cws]
    shown = texts + [norm(x) for sc in spec.get('scenes', []) for sh in sc.get('shots', []) for x in strings_in(sh.get('p', {}))]
    for r in required_counterweights(spec, root):
        if 'text' in r and norm(r['text']) not in texts:
            add('BLOCK', f"{r['src']} requires counterweight \"{r['text']}\" on screen; not declared in `counterweights`")
        if 'pattern' in r and not any(re.search(r['pattern'], t, re.I) for t in shown):
            add('BLOCK', f"{r['src']} (/{r['pattern']}/) is not on screen: no counterweight or shot text matches")
    for c in cws:
        if not c.get('id') or not c.get('text'):
            add('BLOCK', f'counterweight {c!r} needs id and text')
        if not c.get('claims') and c.get('when') not in ('historical', 'numbers'):
            add('BLOCK', f"counterweight {c.get('id')}: needs a trigger (claims: [...] or when: historical|numbers)")
        for cid in c.get('claims') or []:
            if cid not in claims:
                add('BLOCK', f"counterweight {c.get('id')}: claim {cid!r} is not in {spec['claims']}")
        if re.search(r'\d', c.get('text', '')) and not re.search(r'\{[a-z0-9_]+\}', c.get('text', '')):
            add('BLOCK', f"counterweight {c.get('id')}: a number on screen must be a claim ({{claimId}})")
    return P


def claims_unrounded(spec, root):
    """Việc treo nhà máy Tập 5 (tổng kết Tập 5 mục 11): `claims.json` phải ghi giá trị CHƯA làm tròn của mô hình. Tập 5 C4: S05 sai số
    0,005 — với số đã làm tròn của numbers.md trượt 4 claim. Khi tập có `contract.json` `model.claims` (claimId → khoá mô hình) và
    `out/model.json` `raw`, mỗi claim số phải bằng đúng `raw[khoá]` (sai số 1e-9); giá trị trùng `rounded[khoá]` mà khác raw → BLOCK."""
    P = []
    ct, mj = os.path.join(root, 'contract.json'), os.path.join(root, 'out', 'model.json')
    if not (os.path.exists(ct) and os.path.exists(mj)):
        return P
    keys = (json.load(open(ct)).get('model') or {}).get('claims') or {}
    M = json.load(open(mj))
    raw, rnd = M.get('raw') or {}, M.get('rounded') or {}
    vals = {c['claimId']: c.get('value') for c in json.load(open(os.path.join(root, spec['claims'])))['claims']}
    for cid, key in keys.items():
        v, r = vals.get(cid), raw.get(key)
        if not isinstance(r, (int, float)) or isinstance(r, bool) or not isinstance(v, (int, float)):
            continue
        if abs(v - r) > 1e-9:
            hint = ' (equals the ROUNDED model value)' if key in rnd and rnd[key] == v else ''
            P.append({'level': 'BLOCK', 'rule': 'claims_unrounded',
                      'msg': f'claim {cid}: claims.json value {v!r} != model raw {key} {r!r}{hint}; write the unrounded value (display carries rounding)'})
    return P


def check(spec, root, duration=None):
    P = []
    add = lambda level, rule, msg: P.append({'level': level, 'rule': rule, 'msg': msg})
    fmt, scope = spec.get('format'), spec.get('scope', 'full')
    if fmt not in FORMATS:
        add('BLOCK', 'format', f'format must be lab or 101, got {fmt!r}')
        return P
    claims = {c['claimId'] for c in json.load(open(os.path.join(root, spec['claims'])))['claims']}
    sents = {s['id']: s for s in json.load(open(os.path.join(root, spec['script'])))['sentences']}
    for sc in spec.get('scenes', []):
        for sh in sc.get('shots', []):
            if sh.get('template') not in TEMPLATES | {c['id'] for c in spec.get('custom_symbols') or []}:
                add('BLOCK', 'template', f"{sh.get('id')}: unknown template {sh.get('template')!r}")
            for cid in sorted(claim_ids_in(sh.get('p', {}))):
                if cid not in claims:
                    add('BLOCK', 'claim', f"{sh['id']}: claim {cid!r} is not in {spec['claims']}")
            for a in anchors_in(sh.get('p', {})) + [sh.get('from', '')]:
                m = ANCHOR.match(a)
                if not m:
                    add('BLOCK', 'anchor', f"{sh['id']}: bad anchor {a!r}")
                elif m['sid'] not in sents or sents[m['sid']]['scene'] != sc['id']:
                    add('BLOCK', 'anchor', f"{sh['id']}: {a!r} names a sentence outside scene {sc['id']}")
    for sh in spec.get('shorts', []):
        for cid in sorted(claim_ids_in({'h': sh.get('hook', ''), 'e': sh.get('end', '')})):
            if cid not in claims:
                add('BLOCK', 'claim', f"{sh['id']}: claim {cid!r} is not in {spec['claims']}")
    # B+2 (Mốc V): ≤ 2 số MỚI được NÓI mỗi cảnh; số thứ ba trở đi thành nhãn trên hình (toolkit/factory/numbers_said.py)
    import numbers_said as NS
    import voice as VOICE
    order = list(sents.values())
    if order:
        _, NP = NS.check_scenes(order, VOICE.to_spoken([re.sub(r'^\[[a-z ]+\]\s+', '', s['text']) for s in order]), spec.get('spoken_numbers_max', 2))
        legacy = spec.get('episode') in NS.LEGACY   # tập đã phát hành trước luật: chỉ báo, không chặn dựng lại
        P += [{**p, 'level': 'WARN'} if legacy else p for p in NP]
    scene_ids = {sc.get('id') for sc in spec.get('scenes', [])}
    for sid, o in (spec.get('voice_overrides') or {}).items():   # B+1 (Mốc V)
        if sid not in scene_ids:
            add('BLOCK', 'voice_overrides', f'{sid}: not a scene of this episode')
        elif not isinstance(o, dict) or not o or set(o) - {'seed', 'settings', 'voice', 'model', 'take'}:
            add('BLOCK', 'voice_overrides', f'{sid}: {o!r} — allowed keys: seed, settings, voice, model, take')
        elif 'take' in o and not os.path.isfile(os.path.join(root, 'voice-takes', str(o['take']) + '.mp3')):
            add('BLOCK', 'voice_overrides', f"{sid}: take {o['take']!r} not in voice-takes/")
    for w in spec.get('world') or []:   # D-010 (Mốc V): đoạn thế giới 3D, dựng bằng toolkit/factory/world/build_seg.py
        d = os.path.join(root, str(w.get('dir', '')))
        miss = [f for f in ('spine.py', 'scene.js') if not os.path.isfile(os.path.join(d, f))]
        if not w.get('id') or not w.get('dir') or miss:
            add('BLOCK', 'world', f"{w.get('id')}: needs id, dir with spine.py + scene.js (missing: {miss or 'id/dir'})")
        bad = [s for s in w.get('scenes') or [] if s not in scene_ids]
        if not w.get('scenes') or bad:
            add('BLOCK', 'world', f"{w.get('id')}: scenes {bad or '[]'} — must list scenes of this episode")
        order = [sc.get('id') for sc in spec.get('scenes', [])]   # F-5: một đoạn = một khoảng liền của master (world/splice.py)
        ws = [s for s in w.get('scenes') or [] if s in scene_ids]
        if ws and not bad and order[order.index(ws[0]):order.index(ws[0]) + len(ws)] != ws:
            add('BLOCK', 'world', f"{w.get('id')}: scenes {ws} must be consecutive, in episode order (the segment replaces one span of the master)")
    seen = [s for w in spec.get('world') or [] for s in w.get('scenes') or []]
    if len(seen) != len(set(seen)):
        add('BLOCK', 'world', f'a scene is in two world segments: {sorted({s for s in seen if seen.count(s) > 1})}')
    # B+2: nhãn thay số nói (`label: "…"` trong chú thích câu của script.md) phải có trên hình ở cảnh được dựng
    sm = os.path.join(root, (spec.get('dossier') or {}).get('script_md', 'story/script.md'))
    if os.path.exists(sm):
        shown = {sc['id']: ' '.join(x for sh in sc.get('shots', []) for x in strings_in(sh.get('p', {}))) for sc in spec.get('scenes', [])}
        for ln in open(sm, encoding='utf-8'):
            m = re.match(r'^(S\d+)\.\d+', ln)
            for t in re.findall(r'label:\s*"([^"]+)"', ln):
                if m and m[1] in shown and t not in shown[m[1]]:
                    add('WARN', 'labels', f'{ln.split()[0]}: label "{t}" (number moved off the voice) is not on screen in {m[1]}')
    P += counterweights(spec, root, claims)
    P += claims_unrounded(spec, root)
    n_sym = len(spec.get('custom_symbols') or [])
    if n_sym > 2:   # D-009 (b): không còn trần số ký hiệu mới; hình mới đi qua C3 (clip có chuyển động + âm)
        add('WARN', 'custom_symbols', f'{n_sym} new symbols: each must pass C3 (clip with motion and sound), D-009 (b)')
    for c in spec.get('custom_symbols') or []:
        if not os.path.isfile(os.path.join(root, c.get('file', ''))):
            add('BLOCK', 'custom_symbols', f"{c.get('id')}: symbol file {c.get('file')!r} not found")
    n_short = len(spec.get('shorts') or [])
    if scope == 'full' and not 2 <= n_short <= 3:
        add('BLOCK', 'shorts', f'{n_short} shorts; a full episode has 2–3 (playbook §5)')
    elif scope == 'excerpt' and n_short < 1:
        add('WARN', 'shorts', 'excerpt without a short')
    if scope == 'excerpt':
        return P  # length and mid-roll rules apply to a full episode only
    F = FORMATS[fmt]
    mids = spec.get('midrolls') or []
    if len(mids) != F['midrolls']:
        # owner decision (e.g. Tập 5, 08/10: a 101 under 8:00 runs with no mid-roll, no padding): `midrolls: []` + `midrolls_waiver: <reason>` → WARN
        if not mids and str(spec.get('midrolls_waiver') or '').strip():
            add('WARN', 'midrolls', f"{fmt}: 0 mid-rolls (need {F['midrolls']}) — owner waiver: {spec['midrolls_waiver']}")
        else:
            add('BLOCK', 'midrolls', f"{fmt}: {len(mids)} mid-rolls, need {F['midrolls']}")
    if duration is not None:
        if duration > F['max']:
            add('BLOCK', 'duration', f"{fmt}: {duration:.0f} s > hard maximum {F['max']} s")
        elif duration < F['min']:
            add('WARN', 'duration', f"{fmt}: {duration:.0f} s < soft minimum {F['min']} s (không độn: shorter is fine, never pad)")
        for m in mids:
            t = m.get('t') if isinstance(m, dict) else m
            if isinstance(t, (int, float)) and (t < 120 or t > duration - 120):
                add('BLOCK', 'midrolls', f'mid-roll at {t} s is inside the first/last 120 s')
    for m in mids:
        if not isinstance(m, dict) or 'after_act' not in m:
            add('BLOCK', 'midrolls', f'mid-roll {m!r} must name the act boundary it sits on (after_act)')
    return P


def main():
    path = sys.argv[1]
    dur = float(sys.argv[sys.argv.index('--duration') + 1]) if '--duration' in sys.argv else None
    spec = yaml.safe_load(open(path))
    P = check(spec, os.path.dirname(os.path.abspath(path)), dur)
    for p in P:
        print(f"{p['level']:5} {p['rule']:14} {p['msg']}")
    print('spec:', 'OK' if not P else f'{len(P)} problem(s)')
    sys.exit(1 if any(p['level'] in ('BLOCK', 'ASK') for p in P) else 0)


if __name__ == '__main__':
    main()
