import json, hashlib, time, requests, os
base = os.path.dirname(os.path.abspath(__file__))
inp = json.load(open(os.path.join(base, "input.json")))
res = {}
for s in inp["series"]:
    for i, d in enumerate([2, 4, 8, 16, None]):
        try:
            r = requests.get(s["url"], timeout=60); r.raise_for_status(); break
        except requests.RequestException as e:
            if d is None: raise
            time.sleep(d)
    p = os.path.join(base, s["file"]); open(p, "wb").write(r.content)
    h = hashlib.sha256(r.content).hexdigest()
    res[s["id"]] = (h, h == s["sha256"])
    print(s["id"], h, h == s["sha256"])
json.dump(res, open(os.path.join(base, "data/sha.json"), "w"), indent=1)
