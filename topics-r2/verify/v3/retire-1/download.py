import json, hashlib, time, requests, os
d=os.path.dirname(os.path.abspath(__file__))
inp=json.load(open(os.path.join(d,'input.json')))
for s in inp['series']:
    for i,w in enumerate([0,2,4,8,16]):
        time.sleep(w)
        try:
            r=requests.get(s['url'],timeout=60); r.raise_for_status(); break
        except Exception as e:
            print('retry',s['id'],e)
    p=os.path.join(d,s['file']); open(p,'wb').write(r.content)
    h=hashlib.sha256(r.content).hexdigest()
    print(s['id'],h,h==s['sha256'])
