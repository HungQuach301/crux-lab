"""Tập 9 · M3 (Editor: độ dài lặng, không đổi lời): LẶNG TRƯỚC SỐ NEO giữa cảnh (episode.md §5b: 0,7–0,9 s trước mỗi số neo). Ba số neo của Tập 9
(S04.3, S14.3, S15.2) nằm GIỮA cảnh nên take một-cảnh của EL không có khe đủ dài. Ở đây: take gốc (voice-takes/<key16>) → take dẫn xuất
voice-takes/gap-<key16>.{mp3,json}: chèn im lặng để khe giữa chữ cuối câu trước và chữ đầu câu số neo = GAP s; căn chỉnh ký tự sau điểm chèn dời theo.
Chữ (text) giữ nguyên → episode.yaml voice_overrides {Sxx: {take: gap-<key16>}} (voice.py kiểm chữ take == chữ cảnh). 0 ký tự EL.
    python3 episodes/ep009/prod/anchor_gap.py      # ghi take dẫn xuất + in khối voice_overrides cần có (tự chèn vào episode.yaml)"""
import hashlib, json, os, re, subprocess, sys
import yaml
HERE = os.path.dirname(os.path.abspath(__file__)); EP = os.path.dirname(HERE); ROOT = os.path.abspath(os.path.join(EP, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'toolkit', 'factory')); sys.dont_write_bytecode = True
import voice as V  # noqa: E402
ANCHORS, GAP = ['S04.3', 'S14.3', 'S15.2'], 0.95   # khe chữ → chữ; lặng nhạc 0,75 s + 0,05 nằm trọn trong khe (kit.anchor_windows)
LINE = re.compile(r'^(S\d\d)\.(\d+)\s+(?:\{(\w+)\}\s+)?(.+?)\s*<!--')
TK = os.path.join(EP, 'voice-takes')


def main():
    Y = yaml.safe_load(open(os.path.join(EP, 'episode.yaml')))
    rows = [(f'{m[1]}.{m[2]}', m[1], m[4].strip()) for m in (LINE.match(l) for l in open(os.path.join(EP, 'story', 'script.md'), encoding='utf-8')) if m]
    ov = {}
    for sc in sorted({a[:3] for a in ANCHORS}):
        base = {**Y['voice']}; o = (Y.get('voice_overrides') or {}).get(sc) or {}
        base.update({k: v for k, v in o.items() if k != 'take'})
        sp = V.to_spoken([t for i, s, t in rows if s == sc]); text = ' '.join(sp)
        key = hashlib.sha256(json.dumps([text, base['voice'], base['model'], base['seed'], base.get('settings', {'stability': 0.5, 'speed': 0.9})], sort_keys=True).encode()).hexdigest()[:16]
        meta = json.load(open(os.path.join(TK, key + '.json'))); al = meta['alignment']; st, en = list(al['character_start_times_seconds']), list(al['character_end_times_seconds'])
        ids = [i for i, s, t in rows if s == sc]; pos, cuts = 0, []
        for sid, s in zip(ids, sp):
            if sid in ANCHORS and pos > 0:
                j = pos   # ký tự đầu của câu số neo; bỏ qua thẻ cảm xúc / khoảng trắng
                while text[j] in ' [' or (text[j - 1] != ' ' and j > pos):
                    if text[j] == '[': j = text.index(']', j) + 1
                    else: j += 1
                prev = max(en[k] for k in range(pos - 1) if text[k].strip())
                need = GAP - (st[j] - prev)
                if need > 0: cuts.append((prev + 0.02, need, pos))
            pos += len(s) + 1
        if not cuts: continue
        name = 'gap-' + key; src = os.path.join(TK, key + '.mp3')
        x = subprocess.run(['ffmpeg', '-v', 'error', '-i', src, '-ac', '1', '-ar', '44100', '-f', 's16le', '-'], capture_output=True, check=True).stdout
        out, last, shift = b'', 0, 0.0
        for t, d, p in cuts:
            i = int(t * 44100) * 2; out += x[last:i] + b'\0\0' * int(d * 44100); last = i
            for k in range(p, len(text)): st[k] += d; en[k] += d
        out += x[last:]
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 's16le', '-ar', '44100', '-ac', '1', '-i', '-', '-b:a', '128k', os.path.join(TK, name + '.mp3')], input=out, check=True)
        json.dump({**meta, 'alignment': {**al, 'character_start_times_seconds': [round(v, 3) for v in st], 'character_end_times_seconds': [round(v, 3) for v in en]},
                   'chars': 0, 'derived_from': key, 'gap_inserted': [[round(t, 3), round(d, 3)] for t, d, p in cuts],
                   '_about': 'prod/anchor_gap.py: take gốc + im lặng trước câu số neo (0 ký tự EL, chữ không đổi)'}, open(os.path.join(TK, name + '.json'), 'w'))
        ov[sc] = {'take': name}; print(sc, name, [(round(t, 2), round(d, 2)) for t, d, p in cuts])
    p = os.path.join(EP, 'episode.yaml'); s = open(p).read()
    s = re.sub(r'\nvoice_overrides:.*?(?=\n\S)', '', s, flags=re.S)
    blk = 'voice_overrides:   # prod/anchor_gap.py: take dẫn xuất có lặng trước số neo giữa cảnh (chữ không đổi, 0 ký tự EL)\n' + ''.join(f'  {k}: {{take: {v["take"]}}}\n' for k, v in ov.items())
    s = s.replace('\naudio:\n', '\n' + blk + 'audio:\n', 1); open(p, 'w').write(s)


if __name__ == '__main__':
    main()
