"""Tập 9 · M2 animatic: TAKE KHÔ (0 ký tự EL) cho cảnh chưa có lời thật — giờ ước theo tốc độ đọc Eric 0,9 đo trên take thật của Tập 9
(review-g1, voice-takes/*.json), âm = im lặng. Chỉ dùng cho animatic xám tắt tiếng (cổng gốc); lời thật sinh sau vòng 2 `số dày` + kiểm EL.
    python3 episodes/ep009/prod/dry_takes.py            # voice-takes/dry-<key16>.{mp3,json} (không commit) + animatic.yaml (episode.yaml + voice_overrides take)
    python3 episodes/ep009/prod/dry_takes.py --calib    # so mô hình giờ với các take thật (sai số tổng độ dài mỗi take)
Cảnh nào TRÚNG take thật (băm như voice.py) thì giữ take thật; còn lại take khô. Mô hình: mỗi ký tự 1/RATE s; sau . ? ! thêm P_END, sau , ; : thêm
P_MID; thẻ cảm xúc [..] 0 s."""
import hashlib, json, os, re, subprocess, sys
import yaml
HERE = os.path.dirname(os.path.abspath(__file__)); EP = os.path.dirname(HERE); ROOT = os.path.abspath(os.path.join(EP, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'toolkit', 'factory')); sys.dont_write_bytecode = True
import voice as V  # noqa: E402
TAKES = os.path.join(EP, 'voice-takes')
RATE, P_END, P_MID = 14.4, 0.36, 0.16
LINE = re.compile(r'^(S\d\d)\.(\d+)\s+(?:\{(\w+)\}\s+)?(.+?)\s*<!--')


def align(text):
    st, en, t, i = [], [], 0.05, 0
    while i < len(text):
        if text[i] == '[':
            j = text.index(']', i)
            for _ in range(i, j + 1):
                st.append(t); en.append(t)
            i = j + 1; continue
        c = text[i]; d = 1 / RATE
        st.append(round(t, 3)); t += d; en.append(round(t, 3))
        if c in '.?!' and (i + 1 == len(text) or text[i + 1] == ' '): t += P_END
        elif c in ',;:': t += P_MID
        i += 1
    return {'characters': list(text), 'character_start_times_seconds': st, 'character_end_times_seconds': en}


def calib():
    for f in sorted(os.listdir(TAKES)):
        if f.endswith('.json') and not f.startswith('dry-') and f != 'voice-scenes.json':
            m = json.load(open(os.path.join(TAKES, f))); real = m['alignment']['character_end_times_seconds'][-1]
            est = align(m['text'])['character_end_times_seconds'][-1]
            print(f[:16], len(m['text']), f'real {real:.2f} est {est:.2f} ({100 * (est / real - 1):+.1f} %)')


def main():
    Y = yaml.safe_load(open(os.path.join(EP, 'episode.yaml')))
    rows = []
    for ln in open(os.path.join(EP, 'story', 'script.md'), encoding='utf-8'):
        m = LINE.match(ln)
        if m: rows.append((m[1], m[4].strip()))
    ov, real, dry = {}, [], []
    for s in Y['scenes']:
        cfg = V.scene_cfg(Y['voice'], Y.get('voice_overrides'), s['id'])
        text = ' '.join(V.to_spoken([t for sc, t in rows if sc == s['id']]))
        st = cfg.get('settings', {'stability': 0.5, 'speed': 0.9})
        key = hashlib.sha256(json.dumps([text, cfg['voice'], cfg['model'], cfg['seed'], st], sort_keys=True).encode()).hexdigest()
        if os.path.exists(os.path.join(TAKES, key[:16] + '.mp3')):
            real.append(s['id']); continue
        name = 'dry-' + key[:16]
        al = align(text); dur = al['character_end_times_seconds'][-1] + 0.3
        mp3 = os.path.join(TAKES, name + '.mp3')
        if not os.path.exists(mp3):
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=mono', '-t', f'{dur:.3f}', '-b:a', '64k', mp3], check=True)
        json.dump({'key': key, 'text': text, 'voice': cfg['voice'], 'model': cfg['model'], 'seed': cfg['seed'], 'settings': st, 'alignment': al,
                   'chars': 0, 'dry': True, '_about': 'TAKE KHÔ (prod/dry_takes.py): giờ ước, im lặng, 0 ký tự EL — chỉ animatic M2'},
                  open(os.path.join(TAKES, name + '.json'), 'w'))
        ov[s['id']] = {'take': name}; dry.append(s['id'])
    A = dict(Y); A['voice_overrides'] = {**(Y.get('voice_overrides') or {}), **ov}
    A['_animatic'] = 'SINH BỞI prod/dry_takes.py — episode.yaml + take khô (0 ký tự EL); không sửa tay'
    yaml.safe_dump(A, open(os.path.join(EP, 'animatic.yaml'), 'w'), sort_keys=False, allow_unicode=True, width=200)
    print('take thật:', real, '· take khô:', len(dry))


if __name__ == '__main__':
    calib() if '--calib' in sys.argv else main()
