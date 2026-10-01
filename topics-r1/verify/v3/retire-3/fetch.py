import requests, hashlib, json, time
inp=json.load(open('input.json'))
for s in inp['series']:
    for i,w in enumerate([0,2,4,8,16]):
        time.sleep(w)
        try:
            r=requests.get(s['url'],timeout=60); r.raise_for_status(); break
        except Exception as e:
            print('err',e)
    open('data/'+s['id']+'.csv','wb').write(r.content)
    h=hashlib.sha256(r.content).hexdigest()
    print(s['id'],h,h==s['sha256'])
