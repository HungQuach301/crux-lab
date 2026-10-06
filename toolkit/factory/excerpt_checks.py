"""Run the checks/ rules that apply to a factory excerpt (no page sampler, no full-episode artefacts) on what build.py made.

  python3 toolkit/factory/excerpt_checks.py episodes/epNNN/episode.yaml [--rules F01,...]

Builds <episode>/work/factory/checkroot/ (video, script with the new sentence times, captions, takes, voice stem, claims, contract)
and calls checks/py/run.py --only <rules> --first. checks/ is not modified; its LOCK is verified first.
Rules by default: file (F01–F06, F08), captions (F09), loudness/peak/clip/phase/mono (A01, A02, A04–A06), ASR key words (A14),
spoken vs text (A16), one voice (A18); with a music bed also A07 (voice over music) and A08 (music under voice onsets). Length (F07) and page rules need a full episode.
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys

import yaml

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
RULES = 'F01,F02,F03,F04,F05,F06,F08,F09,A01,A02,A04,A05,A06,A14,A16,A18'


def lock():
    d = os.path.join(ROOT, 'checks')
    files = sorted(os.path.relpath(os.path.join(a, f), d) for a, _, fs in os.walk(d) for f in fs
                   if f != 'LOCK' and '__pycache__' not in a)
    lines = ''.join(f"{hashlib.sha256(open(os.path.join(d, f), 'rb').read()).hexdigest()}  ./{f}\n" for f in files)
    return hashlib.sha256(lines.encode()).hexdigest()


def main():
    yml = os.path.abspath(sys.argv[1])
    ep = os.path.dirname(yml)
    S = yaml.safe_load(open(yml))
    rules = sys.argv[sys.argv.index('--rules') + 1] if '--rules' in sys.argv else RULES
    L = lock()
    assert L == open(os.path.join(ROOT, 'checks/LOCK')).read().strip(), f'checks LOCK mismatch {L}'
    W = os.path.join(ep, 'work', 'factory')
    tl = json.load(open(os.path.join(ep, 'out', 'factory', 'timeline.json')))
    R = os.path.join(W, 'checkroot')
    shutil.rmtree(R, ignore_errors=True)
    for d in ('out/voice', 'out/audio/stems'):
        os.makedirs(os.path.join(R, d))
    shutil.copy(os.path.join(W, 'video.mp4'), os.path.join(R, 'out/video.mp4'))
    shutil.copy(os.path.join(ep, 'out/factory/captions.srt'), os.path.join(R, 'out/captions.srt'))
    shutil.copy(os.path.join(ep, S['claims']), os.path.join(R, 'out/claims.json'))
    for st in os.listdir(os.path.join(W, 'stems')):  # voice.flac, and music.flac when the build had a bed
        shutil.copy(os.path.join(W, 'stems', st), os.path.join(R, 'out/audio/stems', st))
    if os.path.exists(os.path.join(W, 'stems/music.flac')) and '--rules' not in sys.argv:
        rules += ',A07,A08'
    if os.path.exists(os.path.join(ep, 'contract.json')):
        shutil.copy(os.path.join(ep, 'contract.json'), os.path.join(R, 'contract.json'))
    json.dump({'sentences': [{k: s[k] for k in ('id', 'scene', 'text', 'spoken', 'start', 'end')} for s in tl['sentences']]},
              open(os.path.join(R, 'out/script.json'), 'w'), indent=1, ensure_ascii=False)
    meta = sorted(f for f in os.listdir(os.path.join(W, 'voice')) if f.endswith('.json'))
    takes = []
    for sc in tl['scenes']:
        m = json.load(open(os.path.join(W, 'voice', meta[0])))
        mp3 = os.path.join(W, 'voice', meta[0][:-5] + '.mp3')
        shutil.copy(mp3, os.path.join(R, 'out/voice', os.path.basename(mp3)))
        takes.append({'id': sc['id'], 'raw': os.path.basename(mp3), 'final': 'out/audio/stems/voice.flac', 'model': m['model'],
                      'voiceId': m['voice'], 'provider': 'elevenlabs'})
    json.dump({'takes': takes}, open(os.path.join(R, 'out/voice/takes.json'), 'w'), indent=1)
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'checks/py/run.py'), R, '--only', rules, '--first'], capture_output=True, text=True)
    print(r.stdout[-3000:], r.stderr[-2000:])
    rep = json.load(open(os.path.join(R, 'out/checks/report-partial.json')))
    rows = [{'id': x['id'], 'status': x['status'], 'tier': x.get('tier'), 'note': (x.get('note') or '')[:160]} for x in rep['results']]
    out = {'lock': L, 'rules': rules, 'results': rows}
    json.dump(out, open(os.path.join(ep, 'out', 'factory', 'checks-excerpt.json'), 'w'), indent=1, ensure_ascii=False)
    for x in rows:
        print(f"{x['id']:4} {x['status']:8} {x['tier'] or '':9} {x['note']}")


if __name__ == '__main__':
    main()
