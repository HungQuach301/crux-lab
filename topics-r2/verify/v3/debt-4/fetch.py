import json,hashlib,time,requests
inp=json.load(open('input.json'))
for s in inp['series']:
    for i,w in enumerate([2,4,8,16,None]):
        try:
            r=requests.get(s['url'],timeout=60); r.raise_for_status(); break
        except requests.RequestException as e:
            print('err',e)
            if w is None: raise
            time.sleep(w)
    open(s['file'],'wb').write(r.content)
    h=hashlib.sha256(r.content).hexdigest()
    print(s['id'],h,h==s['sha256'])
