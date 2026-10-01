"""topics-r1 blind set (topics-r1/DESIGN.md "Trộn và chấm"): 12 machine + 6 control cards, one random order, numbered
01-18, every origin label stripped. Writes cards.json (committed), key.json (NOT committed until the owner has graded),
key.sha256 (committed before grading). Randomness: secrets.SystemRandom. Refuses to overwrite an existing key.json.
Usage: python3 topics-r1/blind/make_blind.py
"""
import hashlib, json, os, re, secrets, sys

R1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(R1, 'blind')
sys.path.insert(0, os.path.join(R1, 'tools'))
import cardcheck  # noqa: E402

PILLARS = [('debt', 'Borrowing and debt'), ('retire', 'Retirement and investing'), ('tax', 'Taxes and policy')]
QUESTION = 'Would you approve this as a future episode for this channel?'
rng = secrets.SystemRandom()


def main():
    if os.path.exists(os.path.join(HERE, 'key.json')):
        raise SystemExit('key.json exists; refusing to reshuffle')
    items = []
    for pillar, title in PILLARS:
        for k in range(1, 5):
            card = json.load(open(os.path.join(R1, 'machine', f'{pillar}-{k}', 'card.json')))
            items.append({'origin': 'machine', 'ref': f'machine/{pillar}-{k}', 'pillar': pillar, 'title': title, 'card': card})
        ctl = json.load(open(os.path.join(R1, 'control', 'out', f'{pillar}.json')))['kept']
        assert len(ctl) == 2, (pillar, len(ctl))
        for j, c in enumerate(ctl):
            items.append({'origin': 'control', 'ref': f'control/out/{pillar}.json#kept[{j}]', 'pillar': pillar,
                          'title': title, 'card': c['card']})
    assert len(items) == 18
    for it in items:
        assert not cardcheck.check(it['card']), (it['ref'], cardcheck.check(it['card']))
    rng.shuffle(items)
    cards, key = [], {'salt': secrets.token_hex(16), 'cards': []}
    for n, it in enumerate(items, 1):
        c = cardcheck.normalize_card(it['card'])
        obj, txt = cardcheck.split_thumb(c['thumbnail'])
        no = f'{n:02d}'
        cards.append({'no': no, 'pillar': it['title'], 'viewer': c['viewer'], 'decision': c['decision'],
                      'promise': c['promise'], 'title': c['title'], 'thumbObject': obj, 'thumbText': txt})
        key['cards'].append({'no': no, 'pillar': it['pillar'], 'origin': it['origin'], 'ref': it['ref']})
    json.dump({'question': QUESTION, 'cards': cards}, open(os.path.join(HERE, 'cards.json'), 'w'), indent=1,
              ensure_ascii=False)
    raw = json.dumps(key, indent=1, ensure_ascii=False).encode()
    open(os.path.join(HERE, 'key.json'), 'wb').write(raw)
    open(os.path.join(HERE, 'key.sha256'), 'w').write(hashlib.sha256(raw).hexdigest() + '  key.json\n')
    print('cards', len(cards), 'key sha256', hashlib.sha256(raw).hexdigest())


if __name__ == '__main__':
    main()
