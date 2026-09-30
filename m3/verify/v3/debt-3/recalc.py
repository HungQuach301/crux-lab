import csv, json
def load(p):
    d={}
    for row in csv.DictReader(open(p)):
        v=list(row.values())[1].strip()
        if v and v!='.': d[row['observation_date']]=float(v)
    return d
a=load('data/RIFLPBCIANM60NM.csv'); b=load('data/RIFLPBCIANM72NM.csv')
dates=sorted(k for k in a if k in b and k<='2026-05-01')
diffs=[b[k]-a[k] for k in dates]
n=len(dates)
m=sum(diffs)/n
le=sum(1 for k in dates if round(b[k]*100)<=round(a[k]*100))
def interest(r,nm,P=30000.0):
    i=r/1200; return nm*P*i/(1-(1+i)**-nm)-P
r60=a['2026-05-01']; r72=b['2026-05-01']
te=interest(7.14,72)-interest(7.14,60)
re=interest(7.14+m,72)-interest(7.14,72)
out={"n_months":n,"mean_premium_72_vs_60":round(m,3),
 "share_months_72_le_60":round(100*le/n,1),"max_premium":round(max(diffs),2),
 "latest_r60":r60,"latest_r72":r72,"term_effect_30k":round(te),
 "rate_effect_30k":round(re),"rate_share_of_extra_interest":round(100*re/(te+re),1),
 "_first_date":dates[0],"_last_date":dates[-1],"_mean_unrounded":m}
print(json.dumps(out,indent=1))
