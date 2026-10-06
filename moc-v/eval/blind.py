"""Mốc V · chạy kiểm mù cổng gốc theo ROOT-intent.md (headless, không ngữ cảnh dự án).
  python3 moc-v/eval/blind.py deal <strips_root> <work>      # xáo: mỗi dải → tên hex; khoá ở <work>/key.json (không đọc trước khi chấm)
  python3 moc-v/eval/blind.py read <work> <hex> <n>           # người đọc thứ n cho dải hex
  python3 moc-v/eval/blind.py grade <work>                    # người chấm độc lập (nhãn ngẫu nhiên + rubric)
"""
import json, os, random, secrets, shutil, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
ROLE = "You are a 58-year-old US homeowner who bought a house in 2000."
Q = ("The image at {p} shows 6 frames, numbered 1-6 in time order, taken from a short MUTED video. Look at it with the Read tool. "
     "Answer in plain English, 4 short numbered answers:\n(1) What idea is this sequence trying to show?\n(2) What changes across frames 1 to 6?\n"
     "(3) What does it mean for someone like you?\n(4) What advice, if any, would a viewer take from this?")
RUB = {'K1': "Correct meaning (score 1) requires ALL of: the line/quantity is a GAIN or PROFIT on paper (not just the home's price or value); "
             "it rises over the years toward a fixed flat $500,000 cap/limit; it passes the cap around Q2 2022; it dips back below briefly; "
             "it has stayed above the cap since Q2 2023. Score 0.5: right direction but one element wrong or missing (e.g. reads it as home value, misses the dip or the dates). Score 0: otherwise.",
       'K2': "Correct meaning (score 1) requires BOTH: their gain on paper (about $558,100) is above / past the $500,000 cap; and Phoenix-area prices are about 3.8 times their 2000 level. "
             "Score 0.5: only one of the two. Score 0: otherwise."}
# đoạn khác (vd Tập 5): BLIND_RUBRIC=<file.json> {"role": ..., "rubric": {"E1": ..., "E2": ...}} — ghi TRƯỚC khi chạy (ROOT-intent-*.md)
if os.environ.get('BLIND_RUBRIC'):
    _r = json.load(open(os.environ['BLIND_RUBRIC'])); ROLE, RUB = _r['role'], _r['rubric']
ADV = ("Advice flag (count=yes) only if the answer recommends a concrete financial action: buy, sell, keep/hold, time a sale, wait to sell, choose a product. "
       "General caution such as 'check your own numbers', 'talk to a tax professional', 'be aware' does NOT count (count=no).")


def deal(src, work):
    os.makedirs(work, exist_ok=True); key = {}
    items = [(v, k) for v in sorted(os.listdir(src)) for k in RUB if os.path.exists(os.path.join(src, v, k + '.png'))]
    random.SystemRandom().shuffle(items)
    for v, k in items:
        h = secrets.token_hex(6); d = os.path.join(work, h); os.makedirs(d)
        shutil.copy(os.path.join(src, v, k + '.png'), os.path.join(d, h + '.png')); key[h] = {'version': v, 'beat': k}
    json.dump(key, open(os.path.join(work, 'key.json'), 'w'), indent=1)
    print(' '.join(key))


def read(work, h, n):
    d = os.path.join(work, h); p = os.path.join(d, h + '.png')
    pr = os.path.join(d, f'prompt-{n}.txt'); open(pr, 'w').write(ROLE + "\n\n" + Q.format(p=p))
    out = os.path.join(d, f'answer-{n}.json')
    subprocess.run(['bash', os.path.join(ROOT, 'toolkit/blind/headless.sh'), pr, out, '--read'], check=True)


def grade(work):
    key = json.load(open(os.path.join(work, 'key.json')))
    rows = []
    for h, k in key.items():
        for f in sorted(os.listdir(os.path.join(work, h))):
            if f.startswith('answer-'):
                rows.append({'id': secrets.token_hex(4), 'h': h, 'n': f, 'beat': k['beat'], 'answer': json.load(open(os.path.join(work, h, f)))['answer']})
    random.SystemRandom().shuffle(rows)
    lab = {r['id']: (r['h'], r['n']) for r in rows}
    json.dump(lab, open(os.path.join(work, 'grade-labels.json'), 'w'))
    txt = ["You grade answers from viewers who saw 6 muted frames of a short video. For EACH answer give: score (1, 0.5 or 0) per the rubric of its beat, "
           "and advice flag yes/no. " + ADV, "Rubrics:\n" + "\n".join(f"{k}: {v}" for k, v in RUB.items()),
           "Return ONLY a JSON list: [{\"id\":..., \"score\":..., \"advice\":\"yes\"|\"no\", \"why\":\"<12 words\"}].\n"]
    for r in rows:
        txt.append(f"--- id {r['id']} · beat {r['beat']} ---\n{r['answer']}\n")
    pr = os.path.join(work, 'grade-prompt.txt'); open(pr, 'w').write('\n'.join(txt))
    subprocess.run(['bash', os.path.join(ROOT, 'toolkit/blind/headless.sh'), pr, os.path.join(work, 'grade.json')], check=True)


if __name__ == '__main__':
    {'deal': lambda: deal(*sys.argv[2:4]), 'read': lambda: read(sys.argv[2], sys.argv[3], sys.argv[4]), 'grade': lambda: grade(sys.argv[2])}[sys.argv[1]]()
