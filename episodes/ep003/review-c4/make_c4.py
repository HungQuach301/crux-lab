"""Tập 3 · C4: mẫu cổng gốc trên animatic (ý đồ `gates/C4-intent.md` v2 §B).
Khoảng nhịp = từ mốc bắt đầu câu đầu tới mốc kết thúc câu cuối của nhịp (+0,5 s), theo `animatic/timing.json` (ASR trên lời animatic).
NGHĨA: dải tắt tiếng 6 khung (`strips.py`), 6 nhịp loại 1, câu 1–3 của C3 (bỏ câu 4 theo quyết định (c)), rubric nghĩa = muted read `beats.md`
(giống C3 r1), lượt nghĩa không chấm khuyên. KHUYÊN: dải + nguyên văn lời các câu có mốc bắt đầu trong khoảng (`withnarration.py`), 7 nhịp,
câu hỏi trùng từng ký tự `review-c4/cal/manifest.json`, rubric = rubric hiệu chuẩn.
    python3 episodes/ep003/review-c4/make_c4.py VIDEO --round N [--only KEY-1,KEY-4]
"""
import hashlib, json, os, subprocess, sys
ROOT = '/home/user/crux-lab'; EP = f'{ROOT}/episodes/ep003'
BEATS = {'KEY-1': ('S01.1', 'S01.5'), 'KEY-2': ('S01.6', 'S01.7'), 'KEY-3': ('S03.5', 'S03.8'), 'KEY-4': ('S05.1', 'S05.4'),
         'KEY-5': ('S05.5', 'S05.7'), 'KEY-6': ('S07.1', 'S07.7'), 'KEY-7': ('S08.1', 'S08.8')}
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()


def main():
    video = sys.argv[1]; rnd = sys.argv[sys.argv.index('--round') + 1]
    only = sys.argv[sys.argv.index('--only') + 1].split(',') if '--only' in sys.argv else list(BEATS)
    R = f'{EP}/review-c4/r{rnd}'; os.makedirs(f'{R}/mean', exist_ok=True); os.makedirs(f'{R}/adv', exist_ok=True)
    tm = json.load(open(f'{EP}/animatic/timing.json')); S = {s['id']: s for s in tm['sentences']}
    order = [s['id'] for s in tm['sentences']]
    spans, narr = {}, {}
    for k in only:
        a, b = BEATS[k]
        t0, t1 = S[a]['start'], S[b]['end'] + 0.5
        spans[k] = [round(t0, 3), round(t1, 3)]
        narr[k] = ' '.join(S[i]['text'] for i in order[order.index(a):order.index(b) + 1] if t0 - 1e-6 <= S[i]['start'] <= t1)
    json.dump(spans, open(f'{R}/spans.json', 'w'), indent=1)
    subprocess.run(['python3', f'{ROOT}/toolkit/blind/strips.py', video, f'{R}/spans.json', f'{R}/strips'], check=True)
    cls = json.load(open(f'{EP}/story/beats-class.json'))
    c3 = json.load(open(f'{EP}/review-c3/r1/manifest.json')); c3r = json.load(open(f'{EP}/review-c3/r1/rubric.json'))
    cal = json.load(open(f'{EP}/review-c4/cal/manifest.json')); calr = json.load(open(f'{EP}/review-c4/cal/rubric.json'))
    qmean = c3['question'][:c3['question'].index('\n4. ')]
    assert qmean.endswith('3. What does it mean?'), qmean[-60:]
    mean_s, adv_s = [], []
    for k in only:
        if cls[k] == 'image':
            mean_s.append({'id': k, 'set': 'ep003', 'kind': 'image', 'file': f'../strips/{k}.png'})
        open(f'{R}/adv/{k}.txt', 'w').write(narr[k])
        subprocess.run(['python3', f'{EP}/review-c4/withnarration.py', f'{R}/strips/{k}.png', f'{R}/adv/{k}.txt', f'{R}/adv/{k}-sound.png'], check=True)
        adv_s.append({'id': k, 'set': 'ep003', 'kind': cls[k], 'file': f'{k}-sound.png'})
    json.dump({'question': qmean, 'candidate_set': 'ep003', 'samples': mean_s}, open(f'{R}/mean/manifest.json', 'w'), indent=1, ensure_ascii=False)
    json.dump({'question': cal['question'], 'candidate_set': 'ep003', 'samples': adv_s}, open(f'{R}/adv/manifest.json', 'w'), indent=1, ensure_ascii=False)
    mrules = c3r['rules'].split(' advice = true')[0] + ' advice: always false, not judged here (advice is measured separately).'
    json.dump({'rules': mrules, 'items': {k: v for k, v in c3r['items'].items() if k in [s['id'] for s in mean_s]}},
              open(f'{R}/mean/rubric.json', 'w'), indent=1, ensure_ascii=False)
    item = calr['items']['NEG']
    json.dump({'rules': calr['rules'], 'items': {k: item for k in only}}, open(f'{R}/adv/rubric.json', 'w'), indent=1, ensure_ascii=False)
    files = ['spans.json', 'mean/manifest.json', 'mean/rubric.json', 'adv/manifest.json', 'adv/rubric.json'] + \
            [f'strips/{k}.png' for k in only] + [f'adv/{k}-sound.png' for k in only] + [f'adv/{k}.txt' for k in only]
    inp = {f: sha(f'{R}/{f}') for f in files}
    inp.update({'video (không commit)': sha(video), 'animatic/timing.json': sha(f'{EP}/animatic/timing.json'),
                'review-c4/cal/manifest.json': sha(f'{EP}/review-c4/cal/manifest.json'), 'story/beats-class.json': sha(f'{EP}/story/beats-class.json'),
                'review-c4/fix_packet.py': sha(f'{EP}/review-c4/fix_packet.py'), 'review-c4/judge-prompt.md': sha(f'{EP}/review-c4/judge-prompt.md')})
    assert json.load(open(f'{R}/adv/manifest.json'))['question'] == cal['question']
    json.dump(inp, open(f'{R}/inputs.json', 'w'), indent=1)
    print('spans', spans); print({k: len(v) for k, v in narr.items()})


if __name__ == '__main__':
    main()
