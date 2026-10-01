import csv, json, statistics
from decimal import Decimal, ROUND_HALF_UP
def load(p):
    d={}
    for row in csv.DictReader(open(p)):
        k,v=list(row.values())
        if v not in ('','.'): d[k]=float(v)
    return d
gs1=load('data/GS1.csv'); gs5=load('data/GS5.csv')
def add(m,n):
    y,mo=int(m[:4]),int(m[5:7]); t=y*12+mo-1+n
    return f"{t//12:04d}-{t%12+1:02d}-01"
def rnd(x,q): return float(Decimal(repr(x)).quantize(Decimal(q),ROUND_HALF_UP))
starts=[]
for s in sorted(gs5):
    if s<'1953-04-01': continue
    if all(add(s,12*k) in gs1 for k in range(5)):
        lock=(1+gs5[s]/100)**5
        roll=1.0
        for k in range(5): roll*=1+gs1[add(s,12*k)]/100
        starts.append(dict(s=s,lock=lock,roll=roll,inv=gs1[s]>gs5[s],diff=100*(lock/roll-1)))
inv=[x for x in starts if x['inv']]
eps=[]; prev=None
for x in inv:
    if prev and add(prev,1)==x['s']: eps[-1].append(x)
    else: eps.append([x])
    prev=x['s']
diffs=[x['diff'] for x in inv]
r={
 'starts_all':len(starts),
 'first_start_year':int(starts[0]['s'][:4]),
 'last_start_year':int(starts[-1]['s'][:4]),
 'share_lock_ahead_all_pct':rnd(100*sum(x['lock']>x['roll'] for x in starts)/len(starts),'0.1'),
 'starts_inverted':len(inv),
 'share_lock_ahead_inverted_pct':rnd(100*sum(x['lock']>x['roll'] for x in inv)/len(inv),'0.1'),
 'inversion_episodes':len(eps),
 'episodes_lock_ahead_majority':sum(sum(x['lock']>x['roll'] for x in e)>len(e)/2 for e in eps),
 'median_lock_vs_roll_inverted_pct':rnd(statistics.median(diffs),'0.01'),
 'best_lock_vs_roll_inverted_pct':rnd(max(diffs),'0.01'),
 'worst_lock_vs_roll_inverted_pct':rnd(min(diffs),'0.01'),
 'gs1_latest_pct':gs1['2026-08-01'],
 'gs5_latest_pct':gs5['2026-08-01'],
}
json.dump(r,open('result.json','w'),indent=1)
print(r); print(starts[0]['s'],starts[-1]['s'])
print('ties',sum(x['lock']==x['roll'] for x in starts),'eq inv',sum(gs1[x['s']]==gs5[x['s']] for x in starts))
print('median raw',statistics.median(diffs),len(diffs))
for e in eps: print(e[0]['s'],e[-1]['s'],len(e),sum(x['lock']>x['roll'] for x in e))
