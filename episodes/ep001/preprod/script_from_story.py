"""Episode 1: the approved script (story/script.md, v2) -> pipeline inputs. The ONLY source of narration from Stage 4b on;
the old template script (script/script.tpl.md, script/script.md) is retired.

    python3 episodes/ep001/preprod/script_from_story.py

Row format of story/script.md: `<scene>.<n> | on-screen/subtitle text | spoken text (empty = same as col. 2; "(silent)" = not read)
| claim IDs | delivery`, under `## Sxx · <act> · Bnn` headings, with the picture note in `*...*` after the rows.

Writes
  out/script-draft.json    every row: {id, scene, act, beat, kind: line|pause|card|hold, text, spoken, claims, delivery, pause}
                           + scenes [{id, act, beat, picture}] (the storyboard/shot list read these)
  out/voice/sentences.json the rows that are read aloud: {id, scene, act, text, spoken} (toolkit/voice/d_el_voice.py input)
Rules: `text` keeps digits (subtitles, key words); `spoken` has numbers in words (TTS). A spoken row whose column 3 is empty
must not contain digits (asserted). Method-card rows whose card block differs from what is read (S32.2, S32.3) keep the block
as `card` and use the spoken sentence, with numbers as digits, as the subtitle `text`.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.join(HERE, '..')
SRC = os.path.join(EP, 'story', 'script.md')
# subtitle text for card rows (the spoken sentence written with digits)
SUBTITLE = {'S32.3': lambda sp: sp.replace('twenty twenty-five', '2025')}


def parse():
    scenes, rows, cur = [], [], None
    for line in open(SRC, encoding='utf-8'):
        line = line.rstrip('\n')
        m = re.match(r'^## (S\d+) · ([\w-]+) · (B\d+)', line)
        if m:
            cur = {'id': m.group(1), 'act': m.group(2), 'beat': m.group(3), 'picture': ''}
            scenes.append(cur)
            continue
        if line.startswith('## '):
            cur = None  # self-check section
            continue
        if cur is None:
            continue
        if line.startswith('*') and line.endswith('*'):
            cur['picture'] = line.strip('*').strip()
            continue
        m = re.match(r'^(S\d+\.\d+) \| (.*)$', line)
        if not m:
            continue
        cols = [c.strip() for c in m.group(2).split('|')]
        assert len(cols) == 4, (m.group(1), cols)
        text, spoken, claims, delivery = cols
        rid = m.group(1)
        row = {'id': rid, 'scene': cur['id'], 'act': cur['act'], 'beat': cur['beat'], 'text': text, 'claims': [] if claims == '-' else [c.strip() for c in claims.split(',')],
               'delivery': delivery}
        p = re.match(r'^\[pause ([\d.]+)\]', text)
        if p:
            row.update(kind='pause', pause=float(p.group(1)), spoken='', adBreak='AD BREAK' in text)
        elif text.startswith('[end screen'):
            row.update(kind='hold', pause=float(re.search(r'(\d+) s', text).group(1)), spoken='')
        elif spoken == '(silent)':
            row.update(kind='card', spoken='')
        else:
            if rid in SUBTITLE:
                row.update(kind='line', card=text, spoken=spoken, text=SUBTITLE[rid](spoken))
            elif spoken and len(spoken.split()) < 0.6 * len(text.split()):
                row.update(kind='line', card=text, spoken=spoken, text=spoken)  # card block on screen, a short sentence read
            else:
                row.update(kind='line', spoken=spoken or text)
            assert spoken or not re.search(r'\d', text), f'{rid}: digits in text but no spoken form'
        rows.append(row)
    return scenes, rows


def main():
    scenes, rows = parse()
    os.makedirs(os.path.join(EP, 'out', 'voice'), exist_ok=True)
    json.dump({'source': 'story/script.md (v2, approved)', 'scenes': scenes, 'sentences': rows}, open(os.path.join(EP, 'out', 'script-draft.json'), 'w'), indent=1, ensure_ascii=False)
    spoken = [{k: r[k] for k in ('id', 'scene', 'act', 'text', 'spoken')} for r in rows if r['kind'] == 'line']
    json.dump({'source': 'out/script-draft.json', 'sentences': spoken}, open(os.path.join(EP, 'out', 'voice', 'sentences.json'), 'w'), indent=1, ensure_ascii=False)
    words = sum(len([w for w in s['spoken'].split() if any(c.isalnum() for c in w)]) for s in spoken)
    print(f'{len(scenes)} scenes, {len(rows)} rows, {len(spoken)} spoken, {words} spoken words, {sum(len(s["spoken"]) for s in spoken)} characters')


if __name__ == '__main__':
    main()
