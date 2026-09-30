import csv, json
def load(p):
    d={}
    for row in csv.reader(open(p)):
        if len(row)<2 or row[0].startswith('observation') or row[0]=='DATE': continue
        try: d[row[0][:7]]=float(row[1])
        except ValueError: pass  # missing ('.' or empty)
    return d
gs=load('data/GS10.csv'); cpi=load('data/CPIAUCNS.csv')
def add(m,k):
    y,mo=map(int,m.split('-')); t=y*12+mo-1+k; return f"{t//12:04d}-{t%12+1:02d}"
r={}
for s in sorted(gs):
    e=add(s,120)
    if e>'2026-08' or s not in cpi or e not in cpi: continue
    r[s]=((1+gs[s]/200)**20/(cpi[e]/cpi[s]))**0.1-1
late=[v for s,v in r.items() if '2014-02'<=s<='2016-08']
since=[v for s,v in r.items() if s>='2008-01']
out={
 "purchase_months":len(r),
 "share_negative_pct":100*sum(v<0 for v in r.values())/len(r),
 "late_lowrate_months":len(late),
 "late_lowrate_negative":sum(v<0 for v in late),
 "late_lowrate_worst_real_pct_per_year":100*min(late),
 "late_lowrate_mean_real_pct_per_year":100*sum(late)/len(late),
 "share_negative_since_2008_pct":100*sum(v<0 for v in since)/len(since),
 "worst_real_pct_per_year":100*min(r.values()),
}
print(json.dumps(out,indent=1))
import sys
if '-v' in sys.argv: print(min(r,key=r.get), min(r), max(r), [s for s in gs if add(s,120)<='2026-08' and s not in r])
