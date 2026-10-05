"""Tập 3 · C4: artefact hợp đồng (`checks/CONTRACT.md`) từ animatic, cho checks đủ bộ lần 1. Không đổi hình/tiếng; chỉ khai báo.
    python3 episodes/ep003/animatic/artefacts.py
Ra (gốc tập): out/video.mp4 (animatic 720p, không commit), out/script.json, out/timeline.json, out/captions.srt,
out/audio/stems/*.wav (không commit), out/voice/takes.json, out/tempo-map.json, out/page.json."""
import json, os, re, shutil, sys
EP = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
A = f'{EP}/animatic'
sys.path.insert(0, f'{EP}/story')
import table_read as TR  # noqa: E402

tm = json.load(open(f'{A}/timing.json'))
rows = {r['id']: r for r in TR.rows()}
os.makedirs(f'{EP}/out/audio/stems', exist_ok=True); os.makedirs(f'{EP}/out/voice', exist_ok=True)
shutil.copyfile(f'{A}/work/animatic.mp4', f'{EP}/out/video.mp4')
for f in os.listdir(f'{A}/work/stems'):
    shutil.copyfile(f'{A}/work/stems/{f}', f'{EP}/out/audio/stems/{f}')
shutil.copyfile(f'{A}/work/tempo-map.json', f'{EP}/out/tempo-map.json')
sents = [{'id': s['id'], 'scene': s['scene'], 'text': s['text'], 'spoken': rows[s['id']]['tts'], 'start': s['start'], 'end': s['end']} for s in tm['sentences']]
json.dump({'sentences': sents}, open(f'{EP}/out/script.json', 'w'), indent=1, ensure_ascii=False)
ACT = {'S01': 'cold-open', 'S02': 'act1', 'S03': 'act1', 'S04': 'act2', 'S05': 'act2', 'S06': 'act2', 'S07': 'act3', 'S08': 'act3',
       'S09': 'method', 'S10': 'outro', 'S11': 'outro'}
LAY = {'S01': 'paths/dana', 'S02': 'card/bond', 'S03': 'paths/chain', 'S04': 'swarm/full', 'S05': 'swarm/eras', 'S06': 'dumbbell/eras',
       'S07': 'shadow/bars', 'S08': 'swarm/rate-scale', 'S09': 'card/method', 'S10': 'paths/dana', 'S11': 'card/end'}
total = 570.0
scenes = []
for k, s in enumerate(tm['scenes']):
    end = tm['scenes'][k + 1]['start'] if k + 1 < len(tm['scenes']) else total
    scenes.append({'id': s['id'], 'act': ACT[s['id']], 'start': s['start'], 'dur': round(end - s['start'], 3), 'layout': LAY[s['id']],
                   'shot': 'wide', 'panels': [s['id']], 'chart': LAY[s['id']].split('/')[0], 'move': 0})
acts = []
for sc in scenes:
    if acts and acts[-1]['id'] == sc['act']:
        acts[-1]['end'] = round(sc['start'] + sc['dur'], 3)
    else:
        acts.append({'id': sc['act'], 'start': sc['start'], 'end': round(sc['start'] + sc['dur'], 3)})
json.dump({'fps': 30, 'total': total, 'acts': acts, 'scenes': scenes, 'turns': [{'t': s['start'], 'what': s['id']} for s in scenes[1:]]},
          open(f'{EP}/out/timeline.json', 'w'), indent=1)


def ts(t):
    h, r = divmod(t, 3600); m, s = divmod(r, 60)
    return f'{int(h):02d}:{int(m):02d}:{s:06.3f}'.replace('.', ',')


with open(f'{EP}/out/captions.srt', 'w') as f:
    for i, s in enumerate(sents, 1):
        f.write(f"{i}\n{ts(s['start'])} --> {ts(s['end'])}\n{s['text']}\n\n")
rep = json.load(open(f'{A}/voice-report.json'))
takes = []
for sc, v in rep['scenes'].items():
    takes.append({'id': sc, 'raw': v.get('use') or v.get('take'), 'final': f'animatic/work/voice/{sc}.wav', 'model': TR.MODEL, 'voiceId': TR.VOICE, 'provider': 'elevenlabs'})
json.dump({'takes': takes, 'voice': {'provider': 'elevenlabs', 'voiceId': TR.VOICE, 'model': TR.MODEL}}, open(f'{EP}/out/voice/takes.json', 'w'), indent=1)
json.dump({'url': 'http://127.0.0.1:8765/episodes/ep003/design/c3/page.html?k=ANIM&r=anim', 'ready': 'window.READY'}, open(f'{EP}/out/page.json', 'w'), indent=1)
print(len(sents), 'sentences;', len(scenes), 'scenes; total', total)
