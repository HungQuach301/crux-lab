import requests, time, hashlib, json
inp=json.load(open('input.json'))
for s in inp['series']:
    for i,d in enumerate([0,2,4,8,16]):
        time.sleep(d)
        try:
            r=requests.get(s['url'],timeout=60); r.raise_for_status(); break
        except requests.RequestException as e:
            print('err',e)
    open(s['file'],'wb').write(r.content)
    h=hashlib.sha256(r.content).hexdigest()
    print(s['id'],h,h==s['sha256'])
