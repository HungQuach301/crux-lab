"""Crux factory voice (Mốc B): one ElevenLabs `with-timestamps` request per scene, cached by SHA-256, characters aligned to words.

  voice_scene(cfg, sentences, cache_dir) -> {'wav': path, 'duration': s, 'sentences': [{id, start, end}], 'words': [{w, s, e, sid}], 'cached': bool, 'chars': n}

- Text sent = the scene's sentences, each normalised by toolkit/voice/normalize.js toSpoken() (numbers, US, …), joined by one space.
- Cache key = SHA-256 of (spoken text, voice id, model, seed, voice settings): the same key never calls the API twice.
- Key: injected by the environment proxy (xi-api-key); never read, sent or printed here.
"""
import base64
import hashlib
import json
import os
import re
import subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
URL = 'https://api.elevenlabs.io/v1/text-to-speech/{}/with-timestamps?output_format=mp3_44100_128'


def to_spoken(texts):
    js = ("const n=require(process.argv[1]);let s='';process.stdin.on('data',d=>s+=d).on('end',()=>"
          "console.log(JSON.stringify(JSON.parse(s).map(t=>n.toSpoken(t)))))")
    r = subprocess.run(['node', '-e', js, os.path.join(ROOT, 'toolkit/voice/normalize.js')], input=json.dumps(texts),
                       capture_output=True, text=True, check=True)
    return json.loads(r.stdout)


def words_of(text, chars, starts, ends):
    """Words (runs of non-space) of `text` with times from the character alignment (same string as sent)."""
    assert ''.join(chars) == text, 'alignment text differs from the text sent'
    out = []
    for m in re.finditer(r'\S+', text):
        out.append({'w': m.group(0), 'i0': m.start(), 'i1': m.end(), 's': round(starts[m.start()], 3), 'e': round(ends[m.end() - 1], 3)})
    return out


def voice_scene(cfg, sentences, cache_dir):
    spoken = to_spoken([s['text'] for s in sentences])
    text = ' '.join(spoken)
    settings = cfg.get('settings', {'stability': 0.5, 'speed': 0.9})
    key = hashlib.sha256(json.dumps([text, cfg['voice'], cfg['model'], cfg['seed'], settings], sort_keys=True).encode()).hexdigest()
    os.makedirs(cache_dir, exist_ok=True)
    mp3, meta_p, wav = (os.path.join(cache_dir, key[:16] + x) for x in ('.mp3', '.json', '.wav'))
    cached = os.path.exists(meta_p) and os.path.exists(mp3)
    if not cached:
        import requests
        r = requests.post(URL.format(cfg['voice']), timeout=300, json={
            'text': text, 'model_id': cfg['model'], 'seed': cfg['seed'], 'voice_settings': settings})
        if r.status_code != 200:
            raise SystemExit(f'ElevenLabs {r.status_code}: {r.text[:300]}')
        d = r.json()
        open(mp3, 'wb').write(base64.b64decode(d['audio_base64']))
        json.dump({'key': key, 'text': text, 'voice': cfg['voice'], 'model': cfg['model'], 'seed': cfg['seed'], 'settings': settings,
                   'alignment': d['alignment'], 'chars': len(text)}, open(meta_p, 'w'))
    meta = json.load(open(meta_p))
    if not os.path.exists(wav):
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', mp3, '-ar', '48000', '-ac', '1', wav], check=True)
    al = meta['alignment']
    words = words_of(text, al['characters'], al['character_start_times_seconds'], al['character_end_times_seconds'])
    # sentence of each word: by character offset of the joined text
    bounds, pos = [], 0
    for s, sp in zip(sentences, spoken):
        bounds.append((s['id'], pos, pos + len(sp), sp)); pos += len(sp) + 1
    out_s = []
    for sid, a, b, sp in bounds:
        ws = [w for w in words if a <= w['i0'] < b]
        for w in ws:
            w['sid'] = sid
        out_s.append({'id': sid, 'spoken': sp, 'start': ws[0]['s'], 'end': ws[-1]['e']})
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', wav],
                               capture_output=True, text=True, check=True).stdout)
    return {'wav': wav, 'mp3': mp3, 'key': key, 'duration': round(dur, 3), 'sentences': out_s,
            'words': [{k: w[k] for k in ('w', 's', 'e', 'sid')} for w in words], 'cached': cached, 'chars': len(text),
            'take': {'provider': 'elevenlabs', 'voiceId': cfg['voice'], 'model': cfg['model'], 'seed': cfg['seed'], 'raw': os.path.relpath(mp3, ROOT)}}
