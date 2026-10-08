"""K4.0 (lô checks-appeal nhóm 2, chỉ thêm luật; D-008 §2). Mỗi luật ghi mục khiếu nại nguồn (checks-appeal A13–A26).
Không luật cũ nào đọc file này; luật ở đây không đổi định nghĩa, ngưỡng hay cấp của luật cũ."""
import re

from common import Missing, canon, canon_matches, metric, numbers_in_text, rule, spoken_numbers, verdict


def _claim_usd(c):
    """Canonical $ values a claim stands for: its display (numbers_in_text) and, for a numeric value, usd:<value>."""
    out = [x for x, _ in numbers_in_text(str(c.get('display', '')))]
    v = c.get('value')
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        out.append(canon(v, 'usd'))
    return out


def _amounts(text, spoken=False):
    """Dollar amounts in a text: '$150', '$1.2 million' (digits) or 'a hundred fifty dollars' (spoken words)."""
    if spoken:
        return [(c, c) for c in spoken_numbers(text) if c.startswith('usd:')]
    out = [(c, s) for c, s in numbers_in_text(text) if c.startswith('usd:')]
    out += [(canon(float(m.group(1).replace(',', '')), 'usd'), m.group(0)) for m in re.finditer(r'(?<![$\d])(\d[\d,]*(?:\.\d+)?)\s+dollars?\b', text, re.I)]
    return out


def _page_texts(ctx):
    """Visible texts per page sample from the page sampler's text track (opacity > 0.5, on frame): [(t, scene, [text, …])]."""
    tt = ctx.json('out/checks/page.json').get('textTrack')
    if tt is None:
        raise Missing('out/checks/page.json: textTrack')
    return [(e['t'], e.get('scene'), [i.get('text') or '' for i in e.get('items', [])]) for e in tt]


# ---- A20 → S19 ------------------------------------------------------------------------------------------------------------------
@rule('S19', 'DX-H1, DX-H4 (claim-risk), checks-appeal A20', 'contract.json claims.forbiddenAmounts[{id, terms[], window?: "sentence"|"frame"|"both"}] (default both): '
      'amounts the episode has no source for (Tập 5: the PMI premium). A unit is one narration sentence (out/script.json text, and spoken read as words) or one '
      'page sample (every visible text together, page sampler text track). A unit violates when it holds a term (word match, case-insensitive) and a dollar amount '
      '($ digits or "<n> dollars") that equals no claim of out/claims.json with a source (display or value). No forbiddenAmounts declared = nothing to check',
      '0 units with a term and an unsourced dollar amount')
def s19_forbidden_amounts(ctx):
    fa = ctx.contract().get('claims', {}) or {}
    fa = fa.get('forbiddenAmounts') if isinstance(fa, dict) else None
    if not fa:
        return verdict('S19', [metric('units with an unsourced forbidden amount', 0, '<=', 0)], note='contract.json declares no claims.forbiddenAmounts: nothing to check')
    sourced = [x for c in ctx.claims() if c.get('source') for x in _claim_usd(c)]
    bad, units = [], 0
    for f in fa:
        terms = [re.compile(r'\b' + re.escape(t) + r'\b', re.I) for t in f.get('terms') or []]
        if not terms:
            raise Missing(f'contract.json: claims.forbiddenAmounts[{f.get("id")}].terms')
        win = f.get('window') or 'both'
        cand = []
        if win in ('sentence', 'both'):
            for s in ctx.sentences():
                cand.append(('sentence', s.get('id'), s.get('text') or '', _amounts(s.get('text') or '')))
                if s.get('spoken'):
                    cand.append(('sentence', s.get('id'), s['spoken'], _amounts(re.sub(r'\[[^\]]*\]', ' ', s['spoken']), spoken=True)))
        if win in ('frame', 'both'):
            for t, sc, texts in _page_texts(ctx):
                joined = ' · '.join(texts)
                cand.append(('frame', f'{t:.1f}s {sc}', joined, [a for tx in texts for a in _amounts(tx)]))
        for kind, uid, text, amts in cand:
            if not any(r.search(text) for r in terms):
                continue
            units += 1
            orphan = [s for c, s in amts if not canon_matches(c, sourced)]
            if orphan:
                bad.append({'id': f.get('id'), 'unit': kind, 'where': uid, 'amounts': orphan, 'text': text[:140]})
    # one sentence read twice (text + spoken) or one label over many samples is one finding
    seen, uniq = set(), []
    for b in bad:
        k = (b['id'], b['unit'], b['where'] if b['unit'] == 'sentence' else b['text'])
        if k not in seen:
            seen.add(k)
            uniq.append(b)
    return verdict('S19', [metric('units with an unsourced forbidden amount', len(uniq), '<=', 0)],
                   details=[{'unitsWithTerm': units}, *uniq[:20]])
