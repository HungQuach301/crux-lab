"""Tập 3 · C3 r1: cuộn style frame tắt tiếng → dải 6 khung (strips.py) → manifest, rubric, khoá đầu vào (ý đồ `gates/C3-intent.md` v2).
    python3 episodes/ep003/review-c3/make_c3.py
Rubric "đúng nghĩa" chép nguyên văn cột muted read của story/beats.md (đọc thẳng từ file, không gõ lại)."""
import hashlib, json, os, re, subprocess

ROOT = '/home/user/crux-lab'; EP = f'{ROOT}/episodes/ep003'; WORK = f'{EP}/design/c3/work'; R1 = f'{EP}/review-c3/r1'
ORDER = [('KEY-1', 'KEY1'), ('KEY-2', 'KEY2'), ('KEY-3', 'KEY3'), ('KEY-4', 'KEY4'), ('KEY-5', 'KEY5'), ('KEY-6', 'KEY6'), ('KEY-7', 'KEY7'), ('ctrl:V4', 'CTRL')]
ROLE = ('You are an American in your 40s with savings you will not need for about 20 years; right now the money sits in a bank account '
        'or short-term Treasury bills. ')
Q = ROLE + ('The image shows six numbered frames, in order, taken from a short silent animation in a personal-finance video. '
            'Look only at the image. Answer in plain sentences:\n1. What idea is this animation showing?\n'
            '2. What changes over time across the frames?\n3. What does it mean?\n4. What advice, if any, would a viewer take from this?')
KEY3 = 'Not scored for meaning (illustration beat); only the advice flag counts.'
CTRL = 'One person is weighing two loans: one fixed, and one variable that starts lower.'
DESC = ('The answer only lists what is visible (dots, bars, lines, labels, numbers) or restates labels, without saying what they mean '
        'in the sense of the meaning sentence.')
RULES = ('Score each answer against the item\'s meaning sentence: 1 = states that meaning (any wording; every part present); '
         '0.5 = partly (right objects, one part of the meaning missing or wrong); 0 = only describes the picture, or a different meaning. '
         'advice = true when the answer gives any action advice, even conditional ("buy the bond", "lock in", "avoid T-bills", '
         '"the bond is safer", "if rates fall, choose ..."). "No advice / depends on the viewer / just information" is not advice.')


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def dur(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p],
                                capture_output=True, text=True, check=True).stdout)


def muted():
    out = {}
    for ln in open(f'{EP}/story/beats.md', encoding='utf-8'):
        m = re.match(r'^\| B\d\d · \*\*(KEY-\d)\*\* \|', ln)
        if m:
            cols = [c.strip() for c in ln.strip().strip('|').split('|')]
            out[m.group(1)] = cols[6].strip('"').strip('“”')
    return out


def main():
    os.makedirs(R1, exist_ok=True)
    lst = f'{WORK}/reel.txt'; spans, t = {}, 0.0
    with open(lst, 'w') as f:
        for sid, k in ORDER:
            p = f'{WORK}/{k}.mp4'; d = dur(p); f.write(f"file '{p}'\n"); spans[sid.replace(':', '-')] = [round(t, 3), round(t + d, 3)]; t += d
    reel = f'{WORK}/stylereel.mp4'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', '-an', reel], check=True)
    # spans: shrink 1 frame at both ends so no frame from a neighbouring clip is cut
    spans = {k: [a + 1 / 30, b - 1 / 30] for k, (a, b) in spans.items()}
    json.dump(spans, open(f'{R1}/spans.json', 'w'), indent=1)
    subprocess.run(['python3', f'{ROOT}/toolkit/blind/strips.py', reel, f'{R1}/spans.json', f'{R1}/strips'], check=True)
    cls = json.load(open(f'{EP}/story/beats-class.json'))
    samples = []
    for sid, k in ORDER:
        png = f'strips/{sid.replace(":", "-")}.png'
        if not os.path.exists(f'{R1}/{png}'):
            raise SystemExit('thiếu ' + png)
        samples.append({'id': sid, 'set': 'ctrl' if sid.startswith('ctrl') else 'ep003', 'kind': cls.get(sid, 'image'), 'file': png})
    json.dump({'question': Q, 'candidate_set': 'ep003', 'samples': samples}, open(f'{R1}/manifest.json', 'w'), indent=1, ensure_ascii=False)
    mr = muted(); assert len(mr) == 7, mr
    items = {k: {'meaning': v, 'description_only': DESC} for k, v in mr.items() if k != 'KEY-3'}
    items['KEY-3'] = {'meaning': KEY3, 'description_only': DESC}
    items['ctrl:V4'] = {'meaning': CTRL, 'description_only': DESC}
    json.dump({'rules': RULES, 'items': items}, open(f'{R1}/rubric.json', 'w'), indent=1, ensure_ascii=False)
    inp = {p: sha(f'{EP}/{p}') for p in ['design/c3/src/scenes.js', 'design/c3/ctrl/k1.js', 'story/beats-class.json',
                                          'review-c3/r1/spans.json', 'review-c3/r1/manifest.json', 'review-c3/r1/rubric.json']}
    inp['design/c3/work/stylereel.mp4 (không commit)'] = sha(reel)
    for s in samples:
        inp['review-c3/r1/' + s['file']] = sha(f"{R1}/{s['file']}")
    json.dump(inp, open(f'{R1}/inputs.json', 'w'), indent=1)
    print('reel', round(t, 2), 's;', len(samples), 'samples; KEY-3 rubric =', KEY3[:30])


if __name__ == '__main__':
    main()
