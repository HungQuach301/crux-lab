import sys, json, os; sys.path.insert(0,'.')
from tts import *
C2='/home/user/crux-lab/episodes/ep001/work/c2-voice'
S=[json.load(open(f'{C2}/c00{i}.s1.json'))['text'] for i in range(7)]
E='cjVigY5qzO86Huf0OWal'; F='4EQ2DsnrRPyxtdEYc43b'
G={'G1':(E,'eleven_v3',None),'G2':(E,'eleven_multilingual_v2',{'stability':0.5,'similarity_boost':0.75,'style':0.0,'use_speaker_boost':True,'speed':0.72}),'G3':(F,'eleven_v3',None)}
which=sys.argv[1:] or list(G)
seed=int(os.environ.get('SEED',11))
os.makedirs('takes',exist_ok=True)
out={}
for g in which:
    v,m,st=G[g]; rows=[]
    for i,t in enumerate(S):
        p=f'takes/{g}.s{i}.seed{seed}'; meta=synth(t,v,m,p,seed,st); r=measure(p,t); r.update(cost=meta['characterCost'],sent=len(t))
        rows.append(r); print(g,i,r['wpmTrim'],r['cost'],'|',r['heard'],flush=True)
    out[g]=rows
json.dump(out,open(f'measure.seed{seed}.{"-".join(which)}.json','w'),indent=1,default=float)
