import csv, json, os, math
D=os.path.dirname(os.path.abspath(__file__))
rows=[]
for r in csv.DictReader(open(os.path.join(D,'data/SP500.csv'))):
    v=r['SP500'].strip()
    if v in ('','.'): continue
    rows.append((r['observation_date'],float(v)))
V,G,C=50000.0,10000.0,40000.0
n=len(rows); W=n-21
xs=[rows[i+21][1]/rows[i][1] for i in range(W)]
def d_list(t):
    A0=V-t*G; out=[]
    for x in xs:
        V1=V*x
        A1=V1-0.15*(V1-C) if V1-C>0 else V1
        out.append(A1-A0)
    return out
def be(t):
    A0=V-t*G; x=(A0-0.15*C)/(0.85*V); return round(100*(1-x),3)
res={}
res['tax_saving_if_flat_usd_24']=round((0.24-0.15)*10000,2)
res['after_tax_sell_now_usd_24']=round(50000-0.24*10000,2)
res['breakeven_drop_pct_24']=be(0.24)
res['windows_n']=W
res['first_window_start']=rows[0][0]
res['last_window_start']=rows[W-1][0]
d24=d_list(0.24); d22=d_list(0.22)
res['share_wait_worse_pct_24']=round(100*sum(d<0 for d in d24)/W,2)
s=sorted(d24)
med=s[W//2] if W%2 else (s[W//2-1]+s[W//2])/2
res['median_wait_minus_now_usd_24']=round(med,2)
res['p05_wait_minus_now_usd_24']=round(s[math.floor(0.05*(W-1))],2)
res['worst_wait_minus_now_usd_24']=round(min(d24),2)
iw=min(range(W),key=lambda i:xs[i])
res['worst_window_start']=rows[iw][0]
res['worst_window_index_change_pct']=round(100*(xs[iw]-1),2)
res['breakeven_drop_pct_22']=be(0.22)
res['share_wait_worse_pct_22']=round(100*sum(d<0 for d in d22)/W,2)
res['share_index_down_pct']=round(100*sum(x<1 for x in xs)/W,2)
json.dump(res,open(os.path.join(D,'result.json'),'w'),indent=1)
print(json.dumps(res,indent=1)); print('n closes',n,'ties x==1',sum(x==1 for x in xs))
