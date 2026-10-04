import csv, json, statistics
from decimal import Decimal, ROUND_HALF_UP
def load(f):
    d={}; order=[]
    for r in csv.reader(open(f)):
        if r[0]=='observation_date': continue
        order.append(r[0])
        v=r[1].strip()
        if v in ('','.'): continue
        d[r[0]]=float(v)
    return d,order
tb,tbord=load('TB3MS.csv'); cpi,_=load('CPIAUCNS.csv')
def idx(m): y,mo=int(m[:4]),int(m[5:7]); return y*12+mo-1
def key(i): return "%04d-%02d-01"%(i//12,i%12+1)
def rnd(x,p):
    q=Decimal(1).scaleb(-p) if False else Decimal(1).scaleb(-p)
    return float(Decimal(repr(x)).quantize(q,rounding=ROUND_HALF_UP)) if x>=0 else -float(Decimal(repr(-x)).quantize(q,rounding=ROUND_HALF_UP))
def Q(x,p): return {"value":x,"rounded":rnd(x,p)}
T={idx(k):v for k,v in tb.items()}
C={idx(k):v for k,v in cpi.items()}
first=idx('1934-01-01')
starts=[s for s in sorted(T) if s>=first and all((s+j) in T for j in range(240))]
M={}
for s in starts:
    p=1.0
    for j in range(240): p*=1+T[s+j]/1200
    M[s]=p
last=starts[-1]
def grp(a,b): return [s for s in starts if idx(a)<=s<=idx(b)]
def share(l,f): return 100*sum(1 for s in l if f(s))/len(l)
above=lambda s:M[s]>2.0
q={}
q['starts']=len(starts); q['first_start']=key(starts[0]); q['last_start']=key(last)
q['share_tbills_above_double_pct']=Q(share(starts,above),1)
vals=[M[s] for s in starts]
q['median_M']=Q(statistics.median(vals),3)
mn=min(vals); mx=max(vals)
q['min_M']=Q(mn,3); q['max_M']=Q(mx,3)
q['min_M_start']=key(next(s for s in starts if M[s]==mn))
q['max_M_start']=key(next(s for s in starts if M[s]==mx))
G={'g1934_1949':grp('1934-01-01','1949-12-01'),'g1950_1989':grp('1950-01-01','1989-12-01'),
   'g1990_last':[s for s in starts if s>=idx('1990-01-01')],'guarantee':[s for s in starts if s>=idx('2005-05-01')]}
for n,l in G.items():
    q['share_above_double_'+n]=Q(share(l,above),1) if l else None
    q['n_starts_'+n]=len(l)
q['latest_window_M']=Q(M[last],3)
gv=[M[s] for s in G['guarantee']]
q['guarantee_min_M']=Q(min(gv),3); q['guarantee_max_M']=Q(max(gv),3)
q['doubling_rate_pct_per_year']=Q(100*(2**(1/20)-1),2)
V={s:2.0*C[s]/C[s+240] for s in starts if s in C and (s+240) in C}
q['real_windows']=len(V)
vs=sorted(V)
q['share_V_ge_1_pct']=Q(share(vs,lambda s:V[s]>=1),1)
q['share_V_lt_1_pct']=Q(share(vs,lambda s:V[s]<1),1)
q['median_V_pct']=Q(100*statistics.median(V[s] for s in vs),1)
vm=min(V[s] for s in vs)
q['min_V_pct']=Q(100*vm,1); q['min_V_start']=key(next(s for s in vs if V[s]==vm))
q['latest_start_V_lt_1']=key(max(s for s in vs if V[s]<1))
q['starts_without_V']=[key(s) for s in starts if s not in V]
g=G['g1990_last']
q['share_1990plus_avg_below_start_rate_pct']=Q(share(g,lambda s:sum(T[s+j] for j in range(240))/240<T[s]),1)
q['mean_all_TB3MS']=Q(sum(T.values())/len(T),2)
q['n_starts_M_within_0.5pct_of_2']=sum(1 for s in starts if abs(M[s]/2-1)<0.005)
lm=max(T); q['last_TB3MS_month']=key(lm); q['last_TB3MS_value']=T[lm]
q['n_TB3MS_months']=len(T)
q['floor_months_div_240']=len(T)//240
json.dump({"quantities":q,"windows":[{"start":key(s),"M":M[s]} for s in starts],
 "choices":["Rounding: Decimal(repr(float)) quantized ROUND_HALF_UP (half away from zero)",
 "Blank/'.' cells treated as missing; a start requires 240 consecutive calendar months all present",
 "Starts only from 1934-01-01 onward; last start is last month with full 240 months ahead present",
 "Ties for min/max M: earliest start; M compared to 2.0 strictly in float",
 "V needs CPI at s and s+240 (calendar months); V>=1 and V<1 shares use real_windows as denominator",
 "Median of even count = mean of middle two; median V computed then x100",
 "Group shares use starts within group only; guarantee group 2005-05..last start",
 "Average-TB3MS test: mean of 240 months s..s+239 (includes start month) strictly < TB3MS at s",
 "Mean of all TB3MS = over all non-missing months in file (incl. pre-1934 if any)",
 "Last data month = latest non-missing TB3MS month",
 "|M/2-1|<0.005 strict"]},open('results.json','w'),indent=1)
print(json.dumps(q,indent=1))
