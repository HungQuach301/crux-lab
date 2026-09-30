import csv, json
from collections import defaultdict
def load(n):
    with open(f"data/{n}.csv") as f:
        r=csv.reader(f); next(r)
        return [(d,float(v)) for d,v in r if v not in ('.','')]
ms=dict(load("MSPUS")); cs=load("CSUSHPINSA"); cp=load("CPIAUCSL")
csd=dict(cs); cs_latest=cs[-1][1]
EXCL_SINGLE=250000; EXCL_JOINT=500000; RATE=0.15  # 26 USC 121(b)(1),(2); 1(h)(1)(C)
gain={}
for d,p in sorted(ms.items()):
    y,m=int(d[:4]),int(d[5:7])
    mons=[f"{y}-{m+k:02d}-01" for k in range(3)]
    if all(x in csd for x in mons):
        idx=sum(csd[x] for x in mons)/3
        gain[d]=p*(cs_latest/idx-1)
over250=[d for d,g in gain.items() if g>EXCL_SINGLE]
last=max(over250)
g97=gain["1997-07-01"]; tx=max(0,g97-EXCL_SINGLE)
# Window Sep 2025-Aug 2026; Oct 2025 is blank on FRED (no BLS release), so mean of available values in window (11)
cpi_last12=[v for d,v in cp if "2025-09-01"<=d<="2026-08-01"]
cpi97=[v for d,v in cp if d.startswith("1997")]; assert len(cpi97)==12
ms97=[v for d,v in ms.items() if d.startswith("1997")]; assert len(ms97)==4
ms_last=ms[max(ms)]
out={
 "last_purchase_year_gain_over_250k": int(last[:4]),
 "last_purchase_quarter_of_that_year": (int(last[5:7])-1)//3+1,
 "quarters_gain_over_500k": sum(g>EXCL_JOINT for g in gain.values()),
 "gain_median_bought_1997q3_usd": round(g97),
 "gain_median_bought_2000q1_usd": round(gain["2000-01-01"]),
 "taxable_gain_single_bought_1997q3_usd": round(tx),
 "tax_at_15pct_single_bought_1997q3_usd": round(RATE*tx),
 "quarters_gain_over_250k": len(over250),
 "quarters_total": len(gain),
 "max_gain_any_quarter_usd": round(max(gain.values())),
 "exclusion_250k_in_current_prices_usd": round(EXCL_SINGLE*(sum(cpi_last12)/len(cpi_last12))/(sum(cpi97)/12)),
 "exclusion_to_median_price_1997": round(EXCL_SINGLE/(sum(ms97)/4),2),
 "exclusion_to_median_price_latest": round(EXCL_SINGLE/ms_last,2),
}
print(json.dumps(out,indent=1))
