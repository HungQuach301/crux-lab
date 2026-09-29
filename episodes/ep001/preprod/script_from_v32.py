"""Episode 1 (C5): the final narration (story/script-v3.2.md) + its timing -> out/script.json and out/script-draft.json.

    python3 episodes/ep001/preprod/script_from_v32.py      # then: python3 episodes/ep001/build.py (claims), contract_build.py

Inputs (all final, C4 decision "không đổi lời, không đổi thời điểm câu"):
  story/script-v3.2.md          spoken lines of S01-S20 with claim IDs `[id]` and 8 emotion tags `[softly]` etc.
  out/voice-v32/sentences.json  the 105 sentences as generated: text (digits), tts_text (sent to eleven_v3, numbers in words),
                                tag, start/end on the narration track (= animatic/timing.json = the final video; asserted)

Writes
  out/script.json        {sentences:[{id, n, scene, text, spoken, tag, start, end, claims}]} (checks/CONTRACT.md)
                         text   = subtitle / on-screen wording, digits as in the script (F09, S07, S09, S10 read it)
                         spoken = exactly the words sent to TTS for that sentence, WITHOUT the emotion tag: the tag is an
                                  instruction to eleven_v3, not a word and not a pause. A16 compares spoken with text for
                                  pause marks ([pause]/[beat]/ellipsis/extra commas): a tag in `spoken` would neither be a
                                  pause nor a word of the ASR, and it would inflate the word counts A14/A15 read from spoken.
                                  The tag is kept in its own field `tag`.
  out/script-draft.json  rows {id, scene, act, kind:"line", text, spoken, claims} for build.py (spoken/shownIn/callbacks of claims)
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.join(HERE, '..')
SRC = os.path.join(EP, 'story', 'script-v3.2.md')
# numbers the narration says without a claim ID in script-v3.2.md (the writer tagged their first use elsewhere): the claim of that number
UNTAGGED = {'S01.1': ['term30'],   # "30-year fixed mortgage rate": the loan term of the series (claim term30, tagged at S10)
            'S15.1': ['y2025']}    # "In the 2025 data": the HMDA data year (claim y2025, tagged at S07)
TAGS = {'softly', 'curious', 'thoughtful', 'serious', 'warmly', 'matter-of-fact'}
# scenes -> act (out/timeline.json; beats-v3.md sequences; see dossier_c5.py for the method/outro choice)
ACT = {**{f'S{i:02d}': 'cold-open' for i in (1, 2)}, **{f'S{i:02d}': 'act1' for i in range(3, 9)}, **{f'S{i:02d}': 'act2' for i in range(9, 14)},
       **{f'S{i:02d}': 'act3' for i in range(14, 19)}, 'S19': 'method', 'S20': 'outro'}


def script_lines():
    """[(scene, raw line)] of the spoken lines of script-v3.2.md, in order."""
    out, sc = [], None
    body = open(SRC, encoding='utf-8').read().split('\n## Tự kiểm')[0]
    for line in body.split('\n'):
        s = line.strip()
        m = re.match(r'^### (S\d\d) ', s)
        if m:
            sc = m.group(1)
            continue
        if s.startswith('**— thẻ phương pháp'):
            sc = None  # method card bullets: on screen, not read
        if not s or sc is None or s.startswith(('#', '*', '---', '>', '- ')) or s == '[beat]':
            continue
        out.append((sc, s))
    return out


def main():
    V = json.load(open(os.path.join(EP, 'out', 'voice-v32', 'sentences.json')))['sentences']
    T = json.load(open(os.path.join(EP, 'animatic', 'timing.json')))
    tt = [x for s in T['scenes'] for x in s['sentences']]
    assert len(V) == len(tt) == 105
    for a, b in zip(V, tt):
        assert (a['n'], a['text'], a['start'], a['end']) == (b['n'], b['text'], b['start'], b['end']), a['n']
    rows, vi = [], 0
    for sc, raw in script_lines():
        tag = None
        m = re.match(r'^\[([a-z-]+)\]\s+', raw)
        if m and m.group(1) in TAGS:
            tag, raw = '[' + m.group(1) + ']', raw[m.end():]
        # strip claim IDs, remembering where each one sits in the plain line
        plain, marks, i = '', [], 0
        for m in re.finditer(r'\s*\[([a-z0-9_]+)\]', raw):
            plain += raw[i:m.start()]
            marks.append((len(plain), m.group(1)))
            i = m.end()
        plain += raw[i:]
        # the sentences of this line, consecutive in sentences.json
        pos = 0
        while pos < len(plain):
            v = V[vi]
            assert v['scene'] == sc, (sc, v['n'], plain)
            k = plain.find(v['text'], pos)
            assert k == pos or plain[pos:k].strip() == '', (v['n'], v['text'], plain[pos:])
            end = k + len(v['text'])
            cl = [cid for p, cid in marks if k < p <= end]
            assert (v['tag'] or None) == (tag if pos == 0 else None), (v['n'], v['tag'], tag)  # a tag colours the first sentence of its line
            rows.append({'_raw': raw, 'n': v['n'], 'scene': sc, 'text': v['text'], 'spoken': v['tts_text'], 'tag': v['tag'], 'start': v['start'], 'end': v['end'],
                         'claims': cl})
            vi += 1
            pos = end
            while pos < len(plain) and plain[pos] == ' ':
                pos += 1
    assert vi == len(V), (vi, len(V))
    per = {}
    for r in rows:
        per[r['scene']] = per.get(r['scene'], 0) + 1
        r['id'] = f"{r['scene']}.{per[r['scene']]}"
        r.pop('_raw')
        r['claims'] += [c for c in UNTAGGED.get(r['id'], []) if c not in r['claims']]
    order = ['id', 'n', 'scene', 'text', 'spoken', 'tag', 'start', 'end', 'claims']
    rows = [{k: r[k] for k in order} for r in rows]
    json.dump({'source': 'story/script-v3.2.md + out/voice-v32/sentences.json (times = animatic/timing.json = final video)',
               'spokenRule': 'spoken = tts_text sent to eleven_v3 without the emotion tag (tag kept in `tag`): a tag is an instruction, not a word or a pause',
               'sentences': rows}, open(os.path.join(EP, 'out', 'script.json'), 'w'), indent=1, ensure_ascii=False)
    draft = [{'id': r['id'], 'scene': r['scene'], 'act': ACT[r['scene']], 'kind': 'line', 'text': r['text'], 'spoken': r['spoken'], 'claims': r['claims']} for r in rows]
    json.dump({'source': 'story/script-v3.2.md (C4 final; generated by preprod/script_from_v32.py)', 'sentences': draft},
              open(os.path.join(EP, 'out', 'script-draft.json'), 'w'), indent=1, ensure_ascii=False)
    print(f'{len(rows)} sentences, {sum(1 for r in rows if r["tag"])} tagged, {sum(len(r["claims"]) for r in rows)} claim marks')


if __name__ == '__main__':
    main()
