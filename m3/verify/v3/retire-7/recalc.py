import csv, json
def load(p):
    d={}
    for row in csv.DictReader(open(p)):
        k=list(row.keys())[1]; v=row[k].strip()
        if v in ("",".") : continue
        y,m,_=row["observation_date"].split("-"); d[(int(y),int(m))]=float(v)
    return d
gs=load("data/GS10.csv"); tb=load("data/TB3MS.csv")
def add(ym,k):
    i=ym[0]*12+ym[1]-1+k; return (i//12,i%12+1)
rows=[]
for s in sorted(gs):
    ms=[add(s,k) for k in range(120)]
    if not all(m in tb for m in ms): continue
    b=1.0
    for m in ms: b*=1+tb[m]/1200
    n=(1+gs[s]/200)**20
    rows.append((s,b/n))
def share(rs): return 100*sum(r>1 for _,r in rs)/len(rs)
r6079=[x for x in rows if (1960,1)<=x[0]<=(1979,12)]
r80=[x for x in rows if x[0]>=(1980,1)]
out={"purchase_months":len(rows),
"first_purchase_yyyymm":rows[0][0][0]*100+rows[0][0][1],
"last_purchase_yyyymm":rows[-1][0][0]*100+rows[-1][0][1],
"share_bills_won_pct":share(rows),
"share_bills_won_1960_1979_pct":share(r6079),
"share_bills_won_since_1980_pct":share(r80),
"best_bills_advantage_pct":(max(r for _,r in rows)-1)*100,
"best_note_advantage_pct":(1/min(r for _,r in rows)-1)*100}
print(json.dumps(out,indent=1))
