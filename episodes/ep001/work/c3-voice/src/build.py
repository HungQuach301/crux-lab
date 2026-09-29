import sys,json,secrets,os; sys.path.insert(0,'.')
from au import *
import pyloudnorm as pyln, av, numpy as np
SR=48000
pick={g:[f'takes/{g}.s{i}.seed11' for i in range(7)] for g in ('G1','G2','G3')}
pick['G1'][6]='takes/G1.s6.seed12'; pick['G3'][6]='takes/G3.s6.seed12'
gaps=[0.45,0.45,1.0,1.0,1.4,0.45]
meas={}
for f in os.listdir('.'):
    if f.startswith('measure.seed11'): meas.update(json.load(open(f)))
texts=[json.load(open(f'/home/user/crux-lab/episodes/ep001/work/c2-voice/c00{i}.s1.json'))['text'] for i in range(7)]
nw=sum(len([w for w in t.split() if any(c.isalnum() for c in w)]) for t in texts)
res={}; audio={}
for g,ps in pick.items():
    parts=[np.zeros(int(0.5*SR))]; speak=0; cost=0; sent=0
    for i,p in enumerate(ps):
        sr,x=decode(p+'.mp3',SR); a,b=speech_span(x,sr)
        seg=x[max(0,int((a-0.03)*sr)):int((b+0.03)*sr)]; speak+=len(seg)/sr; parts.append(seg)
        m=json.load(open(p+'.json')); cost+=m['characterCost']; sent+=m['len']
        if i<6: parts.append(np.zeros(int(gaps[i]*SR)))
    parts.append(np.zeros(int(1.0*SR))); y=np.concatenate(parts); audio[g]=y
    res[g]=dict(duration=round(len(y)/SR,2),speech=round(speak,2),words=nw,wpmSpeaking=round(60*nw/speak,1),wpmWithPauses=round(60*nw/(len(y)/SR-1.5),1),takes=ps)
# common loudness
meter=pyln.Meter(SR)
L={g:meter.integrated_loudness(y) for g,y in audio.items()}
pk={g:20*np.log10(np.abs(y).max()) for g,y in audio.items()}
target=min(-19.0, min(-1.0-(pk[g]-L[g]) for g in audio))
print('raw',L,pk,'target',target)
for g,y in audio.items():
    z=y*10**((target-L[g])/20); audio[g]=z
    res[g].update(lufs=round(meter.integrated_loudness(z),2),peakDbfs=round(20*np.log10(np.abs(z).max()),2))
labels=['A','B','C']; order=list(res); 
rng=secrets.SystemRandom(); rng.shuffle(order)
os.makedirs('out',exist_ok=True)
def enc(y,path):
    c=av.open(path,'w',format='mp4'); s=c.add_stream('aac',rate=SR); s.layout='mono'; s.bit_rate=192000
    fr=av.AudioFrame.from_ndarray(y.astype(np.float32).reshape(1,-1),format='flt',layout='mono'); fr.sample_rate=SR
    rs=av.AudioResampler(format=s.codec_context.format.name if s.codec_context.format else 'fltp',layout='mono',rate=SR)
    for f in rs.resample(fr):
        for pkt in s.encode(f): c.mux(pkt)
    for pkt in s.encode(None): c.mux(pkt)
    c.close()
key={}
for lab,g in zip(labels,order):
    enc(audio[g],f'out/voice-{lab}.m4a'); key[lab]=g
json.dump({'key':key,'res':res,'target':target,'raw':{'lufs':L,'peak':pk}},open('build.json','w'),indent=1,default=float)
for lab in labels:
    sr,z=decode(f'out/voice-{lab}.m4a',SR); print(lab, round(len(z)/SR,2), round(meter.integrated_loudness(z),2), round(20*np.log10(np.abs(z).max()),2), res[key[lab]]['wpmSpeaking'], res[key[lab]]['wpmWithPauses'])
