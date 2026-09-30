import requests, time
for sid, url in [("MORTGAGE30US","https://fred.stlouisfed.org/graph/fredgraph.csv?id=MORTGAGE30US&coed=2026-09-24"),("USSTHPI","https://fred.stlouisfed.org/graph/fredgraph.csv?id=USSTHPI&coed=2026-04-01")]:
    for w in [0,2,4,8,16]:
        time.sleep(w)
        try:
            r=requests.get(url,timeout=90); r.raise_for_status()
            open(f"data/{sid}.csv","w").write(r.text); print(sid,"ok",len(r.text)); break
        except Exception as e: print(sid,"err",e)
