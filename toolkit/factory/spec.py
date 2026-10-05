"""Crux factory spec check (Mốc B): episode.yaml against playbook/episode.md §5, §9 and CHARTER §5, before any API call or render.

  python3 toolkit/factory/spec.py episodes/epNNN/episode.yaml [--duration <s>]   → prints problems, exit 1 if any is blocking

check(spec, root, duration=None) -> [{'level': 'BLOCK'|'ASK'|'WARN', 'rule', 'msg'}]
  BLOCK  the build stops (missing claim, unknown template, format maximum, bad mid-roll …)
  ASK    an exception the owner must decide (custom_symbols > 2): build stops and the reason goes to the issue
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
            if sh.get('template') not in TEMPLATES:
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
    n_sym = len(spec.get('custom_symbols') or [])
    if n_sym > 2:
        add('ASK', 'custom_symbols', f'{n_sym} new symbols (> 2 per episode, CHARTER §5): owner must approve the exception')
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
