"""Builder-side key-word matcher (crux-lab toolkit, written for Episode 1; replaces the read-only import of the locked
checks functions that test D used). It is the builder's own pre-filter for choosing TTS takes, not the checker's rule:
the checker (A14) measures on the delivered master with its own ASR and its own definitions.

Key words of a sentence (from its written `text`):
  - every number, compared as a value with its unit ("18.63%" = "18.63 percent" = "eighteen point six three percent";
    "$4,500" = "4500 dollars"; "1971" = "nineteen seventy-one");
  - every proper name: a capitalised word that is not the first word of the sentence, plus the ALWAYS list;
  - every defined term of the episode (TERMS below + extra terms passed in).

A key word is heard when the ASR words of the take contain it, after both sides go through the same normal form
(`norm`): lower case, possessive dropped, one plural/inflection ending dropped, final "e" dropped. Tokens joined with
"&" or "-" also count by their parts.

    python3 toolkit/voice/keywords.py            # self-test
"""
import re

ALWAYS = ['US', 'U.S.', 'FRED', 'Freddie', 'Mac', 'HMDA', 'CFPB', 'America', 'American']
TERMS = ['refinance', 'refinancing', 'closing', 'costs', 'break-even', 'mortgage', 'rate', 'spread', 'points', 'payment',
         'principal', 'interest', 'nominal', 'real', 'history', 'forecast', 'illustrative', 'median']

ONES = {'zero': 0, 'oh': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
        'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
        'seventeen': 17, 'eighteen': 18, 'nineteen': 19}
TENS = {'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90}
SCALE = {'hundred': 100, 'thousand': 1000, 'million': 10 ** 6, 'billion': 10 ** 9}
UNIT_WORDS = {'percent': 'pct', 'dollars': 'usd', 'dollar': 'usd'}


def norm(w):
    w = w.lower().strip(".,;:!?\"()[]“”‘’'")
    w = re.sub(r"['’]s$", '', w)
    if re.fullmatch(r'[a-z](\s*\.\s*[a-z])+\.?', w):  # initialisms: "U.S." / ASR "U .S." = "US"
        return re.sub(r'[\s.]', '', w)
    for suf in ('ing', 'ies', 'es', 's', 'ed'):
        if len(w) > len(suf) + 2 and w.endswith(suf):
            w = w[: -len(suf)] + ('y' if suf == 'ies' else '')
            break
    if len(w) > 3 and w.endswith('e'):
        w = w[:-1]
    return w


def _num(s):
    return float(s.replace(',', ''))


def numbers_in_digits(text):
    """Numbers written with digits -> list of (value, unit) with unit in {'pct', 'usd', ''}."""
    out = []
    for m in re.finditer(r'(\$?)(\d{1,3}(?:,\d{3})+|\d+)(\.\d+)?\s?(%|percent\b)?(\s?(?:million|billion|thousand)\b)?', text):
        v = _num(m.group(2) + (m.group(3) or ''))
        if m.group(5):
            v *= SCALE[m.group(5).strip()]
        unit = 'pct' if m.group(4) else 'usd' if m.group(1) else ''
        if not unit and re.match(r'\s*dollars?\b', text[m.end():]):
            unit = 'usd'
        out.append((round(v, 6), unit))
    return out


def numbers_in_words(tokens):
    """Spoken number words (ASR tokens) -> list of (value, unit). Handles 'nineteen seventy-one' (years), 'eighteen point
    six three percent', 'four thousand five hundred dollars'."""
    toks = []
    for t in tokens:
        toks += [x for x in re.split(r'[-\s]', t.lower().strip('.,;:!?')) if x]
    out, i = [], 0
    for k, w in enumerate(toks):  # "half a point" / "a half" = 0.5 (script v2 says 0.5 on screen, "half a ... point" aloud)
        if w == 'half' and (k == 0 or toks[k - 1] not in ONES and toks[k - 1] not in TENS and toks[k - 1] != 'and'):
            out.append((0.5, ''))
    while i < len(toks):
        if toks[i] not in ONES and toks[i] not in TENS:
            i += 1
            continue
        j, parts = i, []
        while j < len(toks) and (toks[j] in ONES or toks[j] in TENS or toks[j] in SCALE or toks[j] in ('and', 'point')):
            parts.append(toks[j])
            j += 1
        while parts and parts[-1] in ('and', 'point'):
            parts.pop()
            j -= 1
        # year form: two two-digit groups ("nineteen seventy one", "twenty twenty five")
        def two(ws):
            v = 0
            for w in ws:
                v += ONES.get(w, 0) + TENS.get(w, 0)
            return v
        val = None
        if 'point' not in parts and not any(p in SCALE for p in parts):
            g, k = [], 0
            while k < len(parts):
                if parts[k] in TENS and k + 1 < len(parts) and parts[k + 1] in ONES and ONES[parts[k + 1]] < 10:
                    g.append(two(parts[k:k + 2])); k += 2
                else:
                    g.append(two(parts[k:k + 1])); k += 1
            if len(g) == 2 and 10 <= g[0] <= 20 and g[1] < 100:
                val = g[0] * 100 + g[1]
            elif len(g) == 1:
                val = g[0]
        if val is None:
            whole, frac, cur, total, seen_point = 0, '', 0, 0, False
            for w in parts:
                if w == 'point':
                    seen_point = True
                elif seen_point:
                    frac += str(ONES.get(w, 0))
                elif w in SCALE:
                    cur = max(cur, 1) * SCALE[w]
                    if SCALE[w] >= 1000:
                        total += cur; cur = 0
                elif w != 'and':
                    cur += ONES.get(w, 0) + TENS.get(w, 0)
            whole = total + cur
            val = whole + (float('0.' + frac) if frac else 0)
        unit = UNIT_WORDS.get(toks[j], '') if j < len(toks) else ''
        out.append((round(float(val), 6), unit))
        i = max(j, i + 1)
    return out


def key_words(sentences, extra_terms=()):
    """sentences: [{'text': ...}] -> per sentence {'numbers': [(v, unit)], 'words': [normal forms]}."""
    terms = {norm(t) for t in list(TERMS) + list(extra_terms)}
    always = {norm(t) for t in ALWAYS}
    res = []
    for s in sentences:
        text = s['text']
        words = []
        toks = re.findall(r"[A-Za-z][A-Za-z.&'’-]*", text)
        for k, t in enumerate(toks):
            n = norm(t)
            first = k == 0
            if n in terms or n in always or (not first and t[0].isupper() and t.upper() != 'I'):
                words.append(n)
        res.append({'numbers': numbers_in_digits(text), 'words': sorted(set(words))})
    return res


def match_keys(keys, asr_words):
    """keys: one element of key_words(); asr_words: [{'w': ...}] -> list of missing key words (as strings)."""
    toks = []
    for w in asr_words:  # Whisper splits "18.63%" into "18" ".63" "%" and "$4,500" into "$4" ",500": glue them back
        t = (w['w'] if isinstance(w, dict) else w).strip()
        if toks and (re.match(r'^[,.%](?!\.\.)', t) or re.match(r'^-\w', t) or toks[-1].endswith(('$', '&', '-'))):  # also "break" "-even"
            toks[-1] += t
        elif t:
            toks.append(t)
    heard = set()
    for t in toks:
        heard.add(norm(t))
        for part in re.split(r'[&-]', t):
            if part:
                heard.add(norm(part))
    joined = ' '.join(toks)
    nums = numbers_in_digits(joined) + numbers_in_words(toks)
    missing = []
    for v, unit in keys['numbers']:
        ok = any(abs(v - a) < 1e-6 and (not unit or not u or unit == u) for a, u in nums)
        if not ok:
            missing.append(f'{v:g}' + ('%' if unit == 'pct' else ' USD' if unit == 'usd' else ''))
    for w in keys['words']:
        if w not in heard:
            missing.append(w)
    return missing


if __name__ == '__main__':
    k = key_words([{'text': 'Since 1971, the rate peaked at 18.63% and fell to 2.65%, per Freddie Mac.'}])[0]
    assert match_keys(k, [{'w': x} for x in 'Since 1971, the rate peaked at 18.63% and fell to 2.65%, per Freddie Mac.'.split()]) == [], k
    spoken = 'Since nineteen seventy-one, the rate peaked at eighteen point six three percent and fell to two point six five percent, per Freddie Mac.'
    assert match_keys(k, [{'w': x} for x in spoken.split()]) == [], match_keys(k, [{'w': x} for x in spoken.split()])
    miss = match_keys(k, [{'w': x} for x in 'Since 1971 the rate peaked at 18.6% and fell to 2.65% per Freddy Mac'.split()])
    assert '18.63%' in miss and 'freddi' in miss, miss
    k2 = key_words([{'text': 'Closing costs of $4,500 on a $300,000 refinance.'}])[0]
    assert match_keys(k2, [{'w': x} for x in 'Closing costs of four thousand five hundred dollars on a three hundred thousand dollar refinance.'.split()]) == []
    assert match_keys(k2, [{'w': x} for x in 'Closing costs of $4,500 on a $300,000 refinancing.'.split()]) == []
    assert match_keys(k, [{'w': x} for x in 'Since 1971, the rate peaked at 18 .63 % and fell to 2 .65 %, per Freddie Mac.'.split()]) == []
    kb = key_words([{'text': 'The break-even is simple division.'}])[0]
    assert match_keys(kb, [{'w': x} for x in ['The', 'break', '-even', 'is', 'simple', 'division.']]) == []
    assert match_keys(key_words([{'text': 'Rates in the US only.'}])[0], [{'w': x} for x in ['Rates', 'in', 'the', 'U', '.S.', 'only.']]) == []
    print('keywords self-test: OK')
