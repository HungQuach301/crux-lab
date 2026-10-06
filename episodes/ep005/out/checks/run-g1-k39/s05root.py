"""Synthetic root for S05 (as K's run): out/claims.json built from out/model.json raw (unrounded) or from numbers.md written values."""
import json, os, sys, shutil, re
EP = '/home/user/crux-lab/episodes/ep005'
mode = sys.argv[1]; root = sys.argv[2]
shutil.rmtree(root, ignore_errors=True); os.makedirs(root + '/out')
os.symlink(EP + '/data', root + '/data'); shutil.copy(EP + '/contract.json', root + '/contract.json'); shutil.copy(EP + '/out/model.json', root + '/out/model.json')
C = json.load(open(EP + '/contract.json')); raw = json.load(open(EP + '/out/model.json'))['raw']; P = C['model']['params']
ill = set(C['claims']['illustrative']); cond = {c: x['id'] for x in C['claims']['conditions'] for c in x['claims']}
stated = {}
if mode == 'stated':   # numbers.md written values (K's ep005-claims.py list, IDs renamed)
    src = open('/home/user/crux-lab/checks-runs/K39/ep005-claims.py').read()
    for o, n in (('fast', 'owen'), ('typical', 'grace'), ('slow', 'victor')):
        src = src.replace(f"('{o}',", f"('{n}',").replace(f"buyer_{o}_", f"buyer_{n}_")
    ns = {}; exec(src, ns)
    stated = {c: v for c, k, v in ns['CLAIMS']}
claims = []
for cid, key in C['model']['claims'].items():
    if mode == 'stated':
        v = stated[cid]
    elif key.startswith('fraction:'):
        v = raw[key[9:]] / 100
    else:
        v = raw[key] if key in raw else P[key]
    c = {'claimId': cid, 'value': v, 'illustrative': cid in ill}
    m = re.match(r'buyer_(owen|grace|victor)_', cid)
    if m: c['character'] = m.group(1)
    if cid in cond: c['conditional'] = cond[cid]
    claims.append(c)
json.dump({'claims': claims, '_about': f'SYNTHETIC for S05 only ({mode})'}, open(root + '/out/claims.json', 'w'), indent=1)
print(mode, len(claims))
