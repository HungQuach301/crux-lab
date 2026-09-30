"""Card template check for Milestone-3 blind pairs (m3/DESIGN.md §3). Same rules for both sides.

normalize(): mechanical punctuation only (dashes -> comma, curly -> straight quotes, whitespace). No word is changed.
check(card) -> list of violations ([] = passes).
"""
import re

NUMBER_WORDS = {
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
    'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty',
    'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred', 'hundreds', 'thousand', 'thousands', 'million',
    'millions', 'billion', 'billions', 'trillion', 'trillions', 'half', 'halves', 'halved', 'halve', 'double',
    'doubles', 'doubled', 'doubling', 'twice', 'triple', 'triples', 'tripled', 'tripling', 'quadruple', 'quadrupled',
    'quarter', 'quarters', 'third', 'thirds', 'dozen', 'dozens', 'percent', 'percentage', 'percentages',
}
# names of data sources, datasets, series codes, statutes, code sections (would reveal the side that holds data)
SOURCE_PATTERNS = [
    r'\bFRED\b', r'\bBLS\b', r'\bBEA\b', r'\bIRS\b', r'\bSSA\b', r'\bCPI\b', r'\bHMDA\b', r'\bCFPB\b', r'\bFHFA\b',
    r'\bPMMS\b', r'\bFreddie\b', r'\bFannie\b', r'\bFederal Reserve\b', r'\bCensus\b', r'\bIRC\b', r'\bCFR\b',
    r'\bU\.?S\.?C\.?\b', r'\bSection\b', r'\bsection\b', r'§', r'\b[A-Z][A-Za-z]*\s+Act\b', r'\bAct\b', r'\bCode\b',
    r'\bRegulation\b', r'\bS&P\b', r'\bDow\b', r'\bNasdaq\b',
]
LIMITS = {'thesis': (20, 28), 'overturns': (10, 16)}


def normalize(text):
    t = text.replace('—', ', ').replace('–', ', ').replace(' -- ', ', ')
    t = t.replace('“', '"').replace('”', '"').replace('‘', "'").replace('’', "'")
    t = re.sub(r'\s+,', ',', t)
    t = re.sub(r',\s*,', ',', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def words(text):
    return [w for w in re.split(r'\s+', text.strip().strip('"').strip()) if re.search(r'[A-Za-z]', w)]


def check(card):
    v = []
    for field in ('thesis', 'overturns'):
        t = card.get(field, '')
        if not t:
            v.append(f'{field}: empty')
            continue
        n = len(words(t))
        lo, hi = LIMITS[field]
        if not lo <= n <= hi:
            v.append(f'{field}: {n} words (need {lo}-{hi})')
        if re.search(r'\d', t):
            v.append(f'{field}: digit')
        if re.search(r'[%$€£]', t):
            v.append(f'{field}: symbol % or $')
        for w in re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)*", t):
            for part in w.lower().split('-'):
                if part in NUMBER_WORDS:
                    v.append(f'{field}: number word "{w}"')
        for p in SOURCE_PATTERNS:
            if re.search(p, t):
                v.append(f'{field}: source/statute name /{p}/')
        body = re.sub(r'\b(U\.S|e\.g|i\.e|vs)\.', 'X', t.strip().strip('"'))
        if len(re.findall(r'[.!?](\s|$)', body)) > 1:
            v.append(f'{field}: more than one sentence')
    return v
