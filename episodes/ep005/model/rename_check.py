"""Tập 5 — kiểm đổi tên người mua (fast/typical/slow → owen/grace/victor) không đổi số nào.
So out/model.before-rename.json (bản trước khi đổi tên) với out/model.json (sau khi đổi tên):
  - raw và rounded: cùng số khoá; mọi khoá không phải người mua giống hệt (giá trị và kiểu);
    buyer_fast_X == buyer_owen_X, buyer_typical_X == buyer_grace_X, buyer_slow_X == buyer_victor_X, chính xác;
    không khoá nào thêm, bớt hay khác ngoài phép đổi tên đó.
  - params, data: giống hệt.
  - buyers: fast→owen, typical→grace, slow→victor; mọi trường giống hệt trừ `name` (Nora/Ben/Carla → Owen/Grace/Victor, khai rõ).
  python3 episodes/ep005/model/rename_check.py   → in PASS (thoát 0) hoặc FAIL kèm danh sách khác biệt (thoát 1)"""
import json, os, sys

EP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OLD = json.load(open(os.path.join(EP, 'out', 'model.before-rename.json')))
NEW = json.load(open(os.path.join(EP, 'out', 'model.json')))
MAP = {'fast': 'owen', 'typical': 'grace', 'slow': 'victor'}
NAMES = {'owen': 'Owen', 'grace': 'Grace', 'victor': 'Victor'}
problems = []


def same(a, b):
    return type(a) is type(b) and json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)


def renamed(k):
    for o, n in MAP.items():
        if k.startswith(f'buyer_{o}_'):
            return f'buyer_{n}_' + k[len(f'buyer_{o}_'):]
    return k


for block in ('raw', 'rounded'):
    old, new = OLD[block], NEW[block]
    if len(old) != len(new):
        problems.append(f'{block}: {len(old)} keys before, {len(new)} after')
    nb = nr = 0
    expected = {renamed(k): k for k in old}
    for k_new, k_old in expected.items():
        if k_new not in new:
            problems.append(f'{block}: {k_old} → {k_new} missing after rename')
        elif not same(old[k_old], new[k_new]):
            problems.append(f'{block}: {k_old}={old[k_old]!r} but {k_new}={new[k_new]!r}')
        elif k_new != k_old:
            nr += 1
        else:
            nb += 1
    for k in new:
        if k not in expected:
            problems.append(f'{block}: extra key after rename {k}')
    left = [k for k in new if any(k.startswith(f'buyer_{o}_') for o in MAP)]
    if left:
        problems.append(f'{block}: old buyer keys still present {left}')
    print(f'{block}: {len(old)} → {len(new)} keys; {nb} non-buyer keys identical; {nr} buyer keys equal under fast→owen, typical→grace, slow→victor')

for block in ('params', 'data'):
    if not same(OLD.get(block), NEW.get(block)):
        problems.append(f'{block}: differs')
print('params, data: identical' if not any(p.startswith(('params', 'data')) for p in problems) else 'params/data: DIFFER')

ob, nbuy = OLD['buyers'], NEW['buyers']
if sorted(MAP[k] for k in ob) != sorted(nbuy):
    problems.append(f'buyers: keys {sorted(ob)} → {sorted(nbuy)}')
for o, n in MAP.items():
    a, b = dict(ob.get(o, {})), dict(nbuy.get(n, {}))
    if b.get('name') != NAMES[n]:
        problems.append(f'buyers.{n}.name = {b.get("name")!r}, expected {NAMES[n]!r}')
    print(f'buyers.{o} → buyers.{n}: name {a.pop("name", None)!r} → {b.pop("name", None)!r} (intended)')
    if not same(a, b):
        problems.append(f'buyers.{o} vs buyers.{n}: fields differ')
for k in set(OLD) ^ set(NEW):
    problems.append(f'top-level key only on one side: {k}')

if problems:
    print('FAIL'); [print('  ' + p) for p in problems]; sys.exit(1)
print('PASS')
