import json, hashlib, time, requests, os
d = json.load(open('input.json'))
for s in d['series']:
    for i, w in enumerate([0, 2, 4, 8, 16]):
        if w: time.sleep(w)
        try:
            r = requests.get(s['url'], timeout=60); r.raise_for_status(); break
        except Exception as e:
            print('err', s['id'], e)
    p = os.path.join('data', s['id'] + '.csv'); open(p, 'wb').write(r.content)
    h = hashlib.sha256(r.content).hexdigest()
    print(s['id'], h, h == s['sha256'])
