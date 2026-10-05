"""C2 kiểm mù: lời thuần ứng viên (story/script.md) + đối chứng yếu (M1b Tập 1). Ghi samples + manifest + rubric.
  python3 episodes/ep003/review-c2/make_c2.py [rN]"""
import hashlib, json, os, re, sys
EP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(EP))
R = sys.argv[1] if len(sys.argv) > 1 else 'r1'
OUT = os.path.join(EP, 'review-c2', R)
os.makedirs(OUT, exist_ok=True)
scenes, cur = [], None
for ln in open(os.path.join(EP, 'story', 'script.md'), encoding='utf-8'):
    m = re.match(r'^(S\d{2})\.\d+[a-z]?\s*\|\s*(.*?)\s*\|', ln)
    if m:
        if m.group(1) != cur:
            scenes.append([]); cur = m.group(1)
        scenes[-1].append(re.sub(r'\[[a-z\- ]+\]\s*', '', m.group(2)))
cand = '\n\n'.join(' '.join(s) for s in scenes) + '\n'
ctrl = [re.sub(r'^- `[^`]+` ', '', l).strip() for l in open(os.path.join(ROOT, 'archive/ep001-v1/script-m1b.md'), encoding='utf-8')
        if l.startswith('- `')]
ctrl = ' '.join(ctrl) + '\n'
T = "You are an American in your 40s with savings you will not need for about 20 years; right now the money sits in a bank account or short-term Treasury bills."
C = "You are an American homeowner with a mortgage who is wondering whether to refinance."
Q = """The file below gives you a role (if any) and the full narration transcript of a YouTube video. Read it once, as that viewer. Answer in English:
1. Summarize the video in 3–4 sentences: who is it about, what decision, and how it unfolds.
2. What is the video's answer to its main question? Be specific.
3. Quote any sentence or passage that confused you, and say why (or "nothing").
4. Quote, word for word, the place where your attention dropped most, if anywhere, and say why (or "nowhere").
5. Does the video tell you which option to pick, or predict what interest rates will do? Yes or no, and why.
6. What advice, if any, would a viewer take from this?
Answer only from the file. Do not open any other file. Reply with your six numbered answers only."""
files = {'cand-T': (f"Role for you as reader: {T}\n\nTranscript:\n{cand}", 'ep003', 'cand'),
         'cand-G': ("Role for you as reader: Read it once, as an ordinary YouTube viewer.\n\nTranscript:\n" + cand, 'ep003', 'cand'),
         'ctrl-T': (f"Role for you as reader: {C}\n\nTranscript:\n{ctrl}", 'ctrl', 'M1b')}
man = {}
for k, (txt, st, sid) in files.items():
    p = os.path.join(OUT, f'{k}.txt'); open(p, 'w', encoding='utf-8').write(txt)
    man[k] = {"question": Q, "candidate_set": "ep003", "samples": [{"id": sid, "set": st, "kind": "script", "file": p}]}
    json.dump(man[k], open(os.path.join(OUT, f'manifest-{k}.json'), 'w'), indent=1, ensure_ascii=False)
json.dump({'cand_sha256': hashlib.sha256(cand.encode()).hexdigest(), 'script_sha256': hashlib.sha256(open(os.path.join(EP, 'story', 'script.md'), 'rb').read()).hexdigest(),
           'scenes': len(scenes), 'cand_words': len(cand.split())}, open(os.path.join(OUT, 'sample-sha.json'), 'w'), indent=1)
json.dump({"rules": "Each item is a reader's answer to six questions about a video narration transcript. Score answers 1–2 with the meaning rule. "
           "Set advice=true if answer 5 says 'yes' because the reader believes the video tells viewers which option to pick or forecasts interest rates, "
           "OR answer 6 states ANY action advice, including conditional advice ('if you expect rates to fall, buy the bond'), e.g. buy, hold, lock in, avoid, "
           "'bonds are safer', 'use the bond as a hedge'. 'No advice / it depends on the viewer' is not advice. Also return \"hyp\": true if the reader notes "
           "that the doubling guarantee is applied to years before 2005 as an assumption; \"confused\": true if answer 3 quotes something; "
           "\"attention\": the reader's answer-4 quote copied verbatim, or \"\" if none.",
           "items": {"cand": {"meaning": "Three ideas: (Q) a choice between a US savings bond (EE) guaranteed to double in 20 years and rolling Treasury bills, for money left alone about 20 years; "
                              "(A1) the answer depends on the era: rolling bills usually ended above double for starts from 1950 to 1989 but almost never for starts from 1990 on; "
                              "(A2) at least one of: about half of all starts overall; double did not always keep its buying power; the 17 months when the guarantee really existed (a small sample) did not reach double. "
                              "Q + A1 + A2, AND the answer does not claim the doubling guarantee really existed for years before 2005 (e.g. 'savings bonds beat T-bills since 1990' stated as fact) = 1; "
                              "Q + one of A1/A2 = 0.5; otherwise 0.",
                              "description_only": "Retells surface details or numbers without the choice and the era-dependent answer."},
                     "ctrl:M1b": {"meaning": "The reader states the video's answer: the rate drop needed for a refinance (Maya's) to pay back its closing costs within a set time, and that smaller loans need a bigger drop.",
                                  "description_only": "Only lists numbers or people without the answer."}}},
          open(os.path.join(OUT, 'rubric.json'), 'w'), indent=1, ensure_ascii=False)
print(OUT, len(scenes), 'cảnh', len(cand.split()), 'từ')
