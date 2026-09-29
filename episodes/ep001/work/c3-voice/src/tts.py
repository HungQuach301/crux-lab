import requests, json, base64, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from au import *
URL='https://api.elevenlabs.io/v1/text-to-speech/{}/with-timestamps?output_format=mp3_44100_128'
def synth(text, voice, model, path, seed=1, settings=None):
    if os.path.exists(path+'.json'): return json.load(open(path+'.json'))
    body={'text':text,'model_id':model,'seed':seed}
    if settings is not None: body['voice_settings']=settings
    for att in range(5):
        r=requests.post(URL.format(voice),json=body,timeout=180)
        if r.ok: break
        print('HTTP',r.status_code,r.text[:300],file=sys.stderr)
        if r.status_code in (401,403,422): raise SystemExit(1)
        import time; time.sleep(5*(att+1))
    d=r.json(); open(path+'.mp3','wb').write(base64.b64decode(d['audio_base64']))
    meta={'text':text,'voice':voice,'model':model,'seed':seed,'voice_settings':settings,'characterCost':int(r.headers.get('character-cost',0) or 0),'len':len(text),'requestId':r.headers.get('request-id')}
    json.dump(meta,open(path+'.json','w'),indent=1); return meta
_asr=None
def measure(path, text):
    global _asr
    from faster_whisper import WhisperModel
    if _asr is None: _asr=WhisperModel('small.en',device='cpu',compute_type='int8')
    sr,x=decode(path+'.mp3',16000); a,b=speech_span(x,sr)
    segs,_=_asr.transcribe(x[int(a*sr):int(b*sr)].astype('float32'),word_timestamps=True,language='en',beam_size=5,condition_on_previous_text=False)
    ws=[w for g in segs for w in g.words]; n=len([w for w in text.split() if any(c.isalnum() for c in w)])
    span=ws[-1].end-ws[0].start if ws else 0
    return {'words':n,'trim':round(b-a,3),'wpmTrim':round(60*n/(b-a),1),'wpmAsr':round(60*n/span,1) if span else None,'heard':' '.join(w.word.strip() for w in ws)}
