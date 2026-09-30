"""Milestone-3 blind pairs (m3/DESIGN.md §3): pair machine and control cards within each pillar at random, put the
machine card on side A in exactly 10 of 20 pairs, shuffle pair order, strip every origin label.

Writes m3/blind/cards.json (no labels; committed), m3/blind/key.json (labels + salt; NOT committed until the owner has
graded) and m3/blind/key.sha256 (committed before grading). Randomness: secrets.SystemRandom. Refuses to overwrite an
existing key.json.
Usage: python3 m3/blind/make_blind.py
"""
import hashlib, json, os, secrets

M3 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(M3, 'blind')
PILLARS = [('debt', 7, 'Borrowing and debt'), ('retire', 7, 'Retirement and long-term investing'),
           ('tax', 6, 'Taxes and policy')]
rng = secrets.SystemRandom()


def main():
    if os.path.exists(os.path.join(HERE, 'key.json')):
        raise SystemExit('key.json exists; refusing to reshuffle')
    pairs = []
    for pillar, n, title in PILLARS:
        mach = []
        for k in range(1, n + 1):
            th = json.load(open(os.path.join(M3, 'machine', f'{pillar}-{k}', 'thesis.json')))
            mach.append({'origin': 'machine', 'ref': f'machine/{pillar}-{k}', 'card': th['card']})
        ctl = [{'origin': 'control', 'ref': f'control/out/{pillar}.json#kept[{i}]', 'card': c['card']}
               for i, c in enumerate(json.load(open(os.path.join(M3, 'control', 'out', f'{pillar}.json')))['kept'])]
        assert len(mach) == n and len(ctl) == n, (pillar, len(mach), len(ctl))
        rng.shuffle(ctl)
        pairs += [{'pillar': pillar, 'title': title, 'm': m, 'c': c} for m, c in zip(mach, ctl)]
    rng.shuffle(pairs)
    machine_a = set(rng.sample(range(len(pairs)), len(pairs) // 2))
    cards, key = [], {'salt': secrets.token_hex(16), 'pairs': []}
    for i, p in enumerate(pairs):
        a, b = (p['m'], p['c']) if i in machine_a else (p['c'], p['m'])
        no = f'{i + 1:02d}'
        cards.append({'pair': no, 'pillar': p['title'], 'A': a['card'], 'B': b['card']})
        key['pairs'].append({'pair': no, 'pillar': p['pillar'], 'machine': 'A' if i in machine_a else 'B',
                             'A': a['ref'], 'B': b['ref']})
    json.dump({'question': 'Which thesis would make the better episode for this channel — more surprising, more '
                           'useful to the viewer, and more defensible with data?', 'pairs': cards},
              open(os.path.join(HERE, 'cards.json'), 'w'), indent=1, ensure_ascii=False)
    raw = json.dumps(key, indent=1, ensure_ascii=False).encode()
    open(os.path.join(HERE, 'key.json'), 'wb').write(raw)
    open(os.path.join(HERE, 'key.sha256'), 'w').write(hashlib.sha256(raw).hexdigest() + '  key.json\n')
    print('pairs', len(cards), 'machine on A:', len(machine_a), 'key sha256', hashlib.sha256(raw).hexdigest())


if __name__ == '__main__':
    main()
