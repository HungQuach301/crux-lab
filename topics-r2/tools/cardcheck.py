"""Topic-card check v2 (decisions/D-004.md §2, topics-r2/BRIEF.md (giống hệt topics-r1)). Same rules for both sides.

Card = {viewer, decision, promise, title, thumbnail}. Identity numbers (year, rate paid, term, age, balance, income) are
allowed only in viewer and decision; promise, title and thumbnail may only repeat numbers already present there.
normalize(): mechanical punctuation only (dashes -> comma, curly -> straight quotes, whitespace). No word is changed.
check(card) -> list of violations ([] = passes).
Usage: python3 cardcheck.py card.json [...]   (prints violations; exit 1 if any card fails)
"""
import json, re, sys

FIELDS = ('viewer', 'decision', 'promise', 'title', 'thumbnail')
IDENTITY_FIELDS = ('viewer', 'decision')
WORD_LIMITS = {'viewer': 25, 'decision': 20, 'promise': 25}
TITLE_MAX_CHARS = 60
THUMB_OBJECT_MAX_WORDS = 12
THUMB_TEXT_MAX_WORDS = 4

NUMBER_WORDS = {
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
    'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty',
    'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred', 'hundreds', 'thousand', 'thousands', 'million',
    'millions', 'billion', 'billions', 'trillion', 'trillions', 'half', 'halves', 'halved', 'halve', 'double',
    'doubles', 'doubled', 'doubling', 'twice', 'triple', 'triples', 'tripled', 'tripling', 'quadruple', 'quadrupled',
    'quarter', 'quarters', 'third', 'thirds', 'dozen', 'dozens', 'percent', 'percentage', 'percentages',
}
# names of data sources, agencies, datasets, series codes, statutes, code sections (would reveal the side holding data)
SOURCE_PATTERNS = [
    r'\bFRED\b', r'\bBLS\b', r'\bBEA\b', r'\bIRS\b', r'\bSSA\b', r'\bCPI\b', r'\bHMDA\b', r'\bCFPB\b', r'\bFHFA\b',
    r'\bPMMS\b', r'\bFreddie\b', r'\bFannie\b', r'\bFederal Reserve\b', r'\bFed\b', r'\bCensus\b', r'\bIRC\b',
    r'\bCFR\b', r'\bU\.?S\.?C\.?\b', r'\bSection\b', r'\bsection\b', r'§', r'\b[A-Z][A-Za-z]*\s+Act\b', r'\bAct\b',
    r'\bCode\b', r'\bRegulation\b', r'\bS&P\b', r'\bDow\b', r'\bNasdaq\b', r'\bSECURE\b', r'\bCARES\b', r'\bTCJA\b',
    r'\bOBBBA?\b', r'\bBill\b', r'\bTreasury\b', r'\bSocial Security Administration\b',
    r'\b[A-Z]{2,}[0-9]+[A-Z0-9]*\b',  # series-code shapes such as MORTGAGE30US, DGS10
]
# common account names are allowed and are not numbers
ACCOUNT_NAMES = re.compile(r'\b(?:401|403|457)\s*\(\s*[a-z]\s*\)|\b529\b(?=\s*(?:plans?|accounts?|savings)\b)', re.I)
NUMBER_TOKEN = re.compile(r'(?<![A-Za-z])\$?\d+(?:,\d{3})*(?:\.\d+)?(?:\s*(?:k|K|m|M)\b)?')
RESULT_WORDS = re.compile(r"\b(save|saves|saved|lose|loses|lost|break[- ]even|breakeven|payback|pays back|"
                          r"comes? out ahead|wins|beats)\b", re.I)


def normalize(text):
    t = (text or '').replace('—', ', ').replace('–', ', ').replace(' -- ', ', ')
    t = t.replace('“', '"').replace('”', '"').replace('‘', "'").replace('’', "'")
    t = re.sub(r'\s+,', ',', t)
    t = re.sub(r',\s*,', ',', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def normalize_card(card):
    return {f: normalize(card.get(f, '')) for f in FIELDS}


def words(text):
    return [w for w in re.split(r'\s+', text.strip().strip('"').strip()) if re.search(r'[A-Za-z0-9]', w)]


def numbers(text):
    """Set of number tokens (digits normalized: no $, no commas, lower-case k/m) and number words."""
    t = ACCOUNT_NAMES.sub(' ', text)
    out = set()
    for m in NUMBER_TOKEN.findall(t):
        out.add(re.sub(r'[\s$,]', '', m).lower())
    for w in re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)*", t):
        for part in w.lower().split('-'):
            if part in NUMBER_WORDS:
                out.add(part)
    if '%' in t:
        out.add('%')
    return out


def split_thumb(t):
    m = re.fullmatch(r'(.+?)\s*/\s*"([^"]+)"\s*', t)
    return (m.group(1), m.group(2)) if m else (None, None)


def sentences(text):
    body = re.sub(r'\b(U\.S|e\.g|i\.e|vs|Jr|Sr|Dr|Mr|Ms|Mrs)\.', 'X', text.strip().strip('"'))
    body = re.sub(r'\d\.\d', '0', body)
    return len(re.findall(r'[.!?](\s|$)', body))


def check(card):
    v = []
    c = normalize_card(card)
    for f in FIELDS:
        if not c[f]:
            v.append(f'{f}: empty')
    extra = set(card) - set(FIELDS)
    if extra:
        v.append(f'extra fields: {sorted(extra)}')
    if v:
        return v
    for f, lim in WORD_LIMITS.items():
        n = len(words(c[f]))
        if n > lim:
            v.append(f'{f}: {n} words (max {lim})')
        if sentences(c[f]) > 1:
            v.append(f'{f}: more than one sentence')
    if not c['decision'].rstrip().endswith('?'):
        v.append('decision: must be a question ending with "?"')
    if len(c['title']) > TITLE_MAX_CHARS:
        v.append(f'title: {len(c["title"])} characters (max {TITLE_MAX_CHARS})')
    if '\n' in card.get('title', '') or '\n' in card.get('thumbnail', ''):
        v.append('title/thumbnail: must be one line')
    obj, txt = split_thumb(c['thumbnail'])
    if obj is None:
        v.append('thumbnail: format must be <object> / "<text>"')
    else:
        if len(words(obj)) > THUMB_OBJECT_MAX_WORDS:
            v.append(f'thumbnail: object {len(words(obj))} words (max {THUMB_OBJECT_MAX_WORDS})')
        if len(words(txt)) > THUMB_TEXT_MAX_WORDS:
            v.append(f'thumbnail: text {len(words(txt))} words (max {THUMB_TEXT_MAX_WORDS})')
    allowed = set().union(*(numbers(c[f]) for f in IDENTITY_FIELDS))
    for f in ('promise', 'title', 'thumbnail'):
        bad = sorted(numbers(c[f]) - allowed)
        if bad:
            v.append(f'{f}: number not in viewer/decision {bad}')
    for f in IDENTITY_FIELDS:
        t = ACCOUNT_NAMES.sub(' ', c[f])
        for m in RESULT_WORDS.finditer(t):
            window = t[max(0, m.start() - 40):m.end() + 40]
            if NUMBER_TOKEN.search(window) or numbers(window) - {'%'}:
                v.append(f'{f}: result word "{m.group(0)}" next to a number')
    for f in FIELDS:
        for p in SOURCE_PATTERNS:
            if re.search(p, ACCOUNT_NAMES.sub(' ', c[f])):
                v.append(f'{f}: source/statute name /{p}/')
    return v


if __name__ == '__main__':
    bad = 0
    for path in sys.argv[1:]:
        card = json.load(open(path))
        card = card.get('card', card)
        viol = check(card)
        print(path, 'OK' if not viol else viol)
        bad += bool(viol)
    sys.exit(1 if bad else 0)
