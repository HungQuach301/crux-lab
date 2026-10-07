"""Mốc V: sinh lời đoạn thử (S04.5 → S07.3 của Tập 4) bằng đúng cấu hình giọng đã phát hành, theo cảnh (G-015).
Take commit ở moc-v/proto/voice-takes/ (không sinh lại khi đổi container)."""
import json, os, sys, subprocess
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'toolkit', 'factory'))
from voice import voice_scene
import yaml
cfg = yaml.safe_load(open(os.path.join(ROOT, 'episodes/ep004/episode.yaml')))['voice']
sents = {s['id']: s for s in json.load(open(os.path.join(ROOT, 'episodes/ep004/design/c4/gen/script.json')))['sentences']}
groups = [['S04.5'], ['S05.1', 'S05.2'], ['S06.1', 'S06.2', 'S06.3', 'S06.4', 'S06.5', 'S06.6'], ['S07.1', 'S07.2', 'S07.3']]
out = []
for g in groups:
    r = voice_scene(cfg, [{'id': i, 'text': sents[i]['text']} for i in g], os.path.join(ROOT, 'moc-v/proto/voice-takes'),
                    '/tmp/claude-0/-home-user-crux-lab/5c10649a-e778-5ed3-96c3-8e6c801ad82f/scratchpad/wav')
    print(g[0], r['duration'], r['chars'], 'cached' if r['cached'] else 'NEW')
    out.append(r)
json.dump(out, open(os.path.join(ROOT, 'moc-v/proto/voice.json'), 'w'), indent=1)
