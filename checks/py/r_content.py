"""§1 and §2 — content, data, claims, language, script structure."""
import csv
import datetime
import re
from urllib.parse import urlparse

import numpy as np

from common import (asr_join, Missing, canon, canon_matches, metric, numbers_in_text, rule, sha256_file, spoken_numbers, verdict, words)
from r_audio import asr_master, silent_spans, master

def page(ctx):
    """Output of the page sampler (checks/page/sampler.js): text track, claims seen, page-rule results."""
    return ctx.json('out/checks/page.json')


def model_out(ctx):
    return ctx.json(ctx.cfield('model', 'output', kind=str))


@rule('S01', 'DX-H1', 'independent re-computation of the episode model (K2: read from the episode contract, contract.json `model`): `kind` names the checker\'s own '
      're-implementation (checks/py/r_model.py: "retirement-6040" = test D\'s 60/40 withdrawal model, "refinance-breakeven" = Episode 1: payment = P·r/(1 − (1 + r)^−n), '
      'r = annual %/1200, savings = payment(old) − payment(old − spread), break-even = ceil(cost / savings), spread for a target = smallest cut with savings ≥ cost / months); '
      '`params` its inputs; `output` the builder\'s model file, compared value by value. A part of the model output the kind does not re-compute is listed (not silently trusted). '
      'Contract without model.kind / output / params, or a kind without a re-implementation = MISSING',
      'every re-computed value within max($0.50, 1e-6 relative) (money), 0.005 (rates, payments), exactly (months); 0 mismatches; 0 model parts not re-computed; ≥ 1 value compared')
def s01_model(ctx):
    import r_model
    cmp_, _, _ = r_model.kind(ctx)
    params = ctx.cfield('model', 'params', kind=dict)
    checked, bad, unrec = cmp_(ctx, params, model_out(ctx))
    return verdict('S01', [metric('values compared', checked, '>=', 1), metric('mismatches', len(bad), '<=', 0),
                           metric('model parts not re-computed', len(unrec), '<=', 0)],
                   details=[{'kind': ctx.cfield('model', 'kind'), 'notRecomputed': unrec}, *bad[:20]])


def visible_texts(ctx, scene_filter=None):
    p = page(ctx)
    out = []
    for s in p['textTrack']:
        if scene_filter and not scene_filter(s['scene']):
            continue
        for it in s['items']:
            out.append((s['t'], s['scene'], it['text']))
    return out


def scene_acts(ctx):
    return {s['id']: s.get('act') for s in ctx.scenes()}


NO_TAX = re.compile(r'\bno (income )?tax(es)?\b|\bbefore tax(es)?\b|\btaxes? (are )?(not|ignored)', re.I)
NO_FEE = re.compile(r'\bno fees?\b|\bfees? (are )?(not|ignored)|\bwithout fees\b|\bno (fund )?costs?\b', re.I)


@rule('S02', 'DX-H1', 'visible on-screen text (page sampler text track, every 0.1 s): phrases for "no taxes" and "no fees" (regex NO_TAX / NO_FEE), '
      'looked for in the methodology card scenes (act "method") and in the rest of the video',
      'both phrases visible in the methodology card AND both visible outside it')
def s02_notax(ctx):
    acts = scene_acts(ctx)
    tx = visible_texts(ctx)
    inm = [x for x in tx if acts.get(x[1]) == 'method']
    out = [x for x in tx if acts.get(x[1]) != 'method']
    f = lambda xs, rx: any(rx.search(x[2]) for x in xs)
    return verdict('S02', [metric('no-tax in method card', f(inm, NO_TAX), '==', True), metric('no-fee in method card', f(inm, NO_FEE), '==', True),
                           metric('no-tax on screen elsewhere', f(out, NO_TAX), '==', True), metric('no-fee on screen elsewhere', f(out, NO_FEE), '==', True)])


@rule('S03', 'DX-H4', 'sources file named by the episode contract (contract.json data.sources, e.g. data/sources.json): per raw file path, url, sha256, downloaded (ISO date), '
      'terms {quote, url}; SHA-256 recomputed from the committed file; host of each file by role vs the hosts the contract declares (data.hosts.primary / data.hosts.crosscheck; '
      'test D: pages.stern.nyu.edu / fred.stlouisfed.org). Contract without data.sources or data.hosts = MISSING',
      'every file present with matching SHA-256, valid date, http(s) URL, terms quote ≥ 20 chars and terms URL; ≥ 1 primary file on a declared primary host; ≥ 1 cross-check file on a declared cross-check host')
def s03_provenance(ctx):
    src = ctx.json(ctx.cfield('data', 'sources', kind=str))
    want = {r: [h.lower() for h in ctx.cfield('data', 'hosts', r, kind=list)] for r in ('primary', 'crosscheck')}
    bad = []
    hosts = {'primary': set(), 'crosscheck': set()}
    for f in src.get('files', []):
        pid = f.get('path')
        if not pid or not ctx.has(pid):
            bad.append((pid, 'file missing'))
            continue
        if sha256_file(ctx.path(pid)) != f.get('sha256'):
            bad.append((pid, 'sha256 mismatch'))
        try:
            datetime.date.fromisoformat(str(f.get('downloaded'))[:10])
        except ValueError:
            bad.append((pid, 'bad date'))
        u = urlparse(f.get('url') or '')
        if u.scheme not in ('http', 'https') or not u.netloc:
            bad.append((pid, 'bad url'))
        t = f.get('terms') or {}
        if len(t.get('quote') or '') < 20 or urlparse(t.get('url') or '').scheme not in ('http', 'https'):
            bad.append((pid, 'terms quote/url missing'))
        hosts.setdefault(f.get('role'), set()).add(u.netloc.lower())
    on = lambda role: any(h == w or h.endswith('.' + w) for h in hosts.get(role, ()) for w in want[role])
    ms = [metric('files', len(src.get('files', [])), '>=', 2), metric('file problems', len(bad), '<=', 0),
          metric('primary on a declared host', on('primary'), '==', True), metric('cross-check on a declared host', on('crosscheck'), '==', True)]
    return verdict('S03', ms, details=[{'declaredHosts': want, 'seenHosts': {k: sorted(v) for k, v in hosts.items()}}, *bad])


def _series(ctx, spec):
    """{file, key, column, scale?}: key -> value × scale (e.g. scale 100 turns a fraction into percentage points)."""
    for k in ('file', 'key', 'column'):
        if not spec.get(k):
            raise Missing(f'contract.json: data.crosscheck[].{{primary|crosscheck}}.{k}')
    sc = float(spec.get('scale', 1))
    out = {}
    for r in csv.DictReader(open(ctx.need(spec['file']))):
        v = r.get(spec['column'])
        if v not in (None, ''):
            out[str(r[spec['key']]).strip()] = float(v) * sc
    return out


def _keys(spec, prim, cross):
    """Keys used by the episode: `used: {"from": a, "to": b}` (integer years, inclusive) or `used: "crosscheck"` (every key of the cross-check
    series inside the primary series' span, the overlap the episode declares it checked)."""
    u = spec.get('used')
    if isinstance(u, dict) and 'from' in u and 'to' in u:
        return [str(y) for y in range(int(u['from']), int(u['to']) + 1)]
    if u == 'crosscheck':
        lo, hi = min(prim), max(prim)
        return sorted(k for k in cross if lo <= k <= hi)
    raise Missing('contract.json: data.crosscheck[].used ({"from","to"} or "crosscheck")')


@rule('S04', 'DX-H5', 'series pairs the episode contract declares (contract.json data.crosscheck[]: series, primary {file, key, column, scale}, crosscheck {file, key, column, scale}, '
      'tolerance, used); per used key |primary − cross-check| (after scale) vs the declared tolerance; mismatches listed in the sources file (data.sources) "mismatches" '
      '[{year|key, series}]. Test D: annual.csv vs fred_inflation.csv (inflation) and stocks2.csv (stocks), 1928–2025. Contract without data.crosscheck = MISSING',
      '≥ 1 pair; every declared tolerance ≤ 0.5 (pp); every used key present in both series; every key outside tolerance listed in "mismatches" (reported, not silently resolved)')
def s04_crosscheck(ctx):
    pairs = ctx.cfield('data', 'crosscheck', kind=list)
    src = ctx.json(ctx.cfield('data', 'sources', kind=str))
    listed = {(str(m.get('key', m.get('year'))), m.get('series')) for m in src.get('mismatches', [])}
    ms, rows = [metric('series pairs', len(pairs), '>=', 1)], []
    unreported, missing = [], []
    for sp in pairs:
        name, tol = sp.get('series'), sp.get('tolerance')
        if name is None or tol is None:
            raise Missing('contract.json: data.crosscheck[].series / tolerance')
        prim, cross = _series(ctx, sp.get('primary') or {}), _series(ctx, sp.get('crosscheck') or {})
        over = 0
        for k in _keys(sp, prim, cross):
            if k not in prim or k not in cross:
                missing.append((name, k))
                continue
            d = abs(prim[k] - cross[k])
            if d > float(tol) + 1e-12:
                over += 1
                if (k, name) not in listed:
                    unreported.append((name, k, round(d, 3)))
        ms.append(metric(f'{name} tolerance', float(tol), '<=', 0.5, 'pp'))
        rows.append({'series': name, 'overTolerance': over})
    ms += [metric('used keys missing in a source', len(missing), '<=', 0), metric('out-of-tolerance keys not reported', len(unreported), '<=', 0)]
    return verdict('S04', ms, details=[{'pairs': rows, 'unreported': unreported[:15], 'missing': missing[:15]}])


def _mapped_claims(ctx):
    """contract.json model.claims: {claimId: key} or [{where: {field: value}, key}] (a claim matched by its fields, e.g. kind + character)."""
    spec = ctx.cfield('model', 'claims')
    cl = ctx.claims()
    out = []
    if isinstance(spec, dict):
        by = {c['claimId']: c for c in cl}
        for cid, key in spec.items():
            out.append((cid, by.get(cid), key))
    elif isinstance(spec, list):
        for m in spec:
            hit = [c for c in cl if all(c.get(k) == v for k, v in (m.get('where') or {}).items())]
            out += [(c['claimId'], c, m['key']) for c in hit] or [(str(m.get('where')), None, m['key'])]
    else:
        raise Missing('contract.json: model.claims')
    return out


@rule('S05', 'DX-H1, DX-H2', 'claims the episode contract maps to model quantities (contract.json model.claims) compared with the checker\'s own re-computation of that '
      'quantity (r_model value(): e.g. "geomean:1966", "breakEven:0.5", "spreadFor:36"); the model kind\'s thesis invariants from model.params (test D: sameGeomean '
      '1966/mirror within 0.01 pp); ILLUSTRATIVE flags: every claim listed in contract claims.illustrative, and every claim of a character the contract marks illustrative, '
      'carries illustrative=true in out/claims.json',
      '≥ 1 mapped claim; each mapped claim present and within its tolerance (0.005 pp for rates and means, exact for months, $0.50 for money); every invariant holds; 0 claims missing their ILLUSTRATIVE flag')
def s05_model_claims(ctx):
    import r_model
    _, value, inv = r_model.kind(ctx)
    params = ctx.cfield('model', 'params', kind=dict)
    ill = ctx.cfield('claims', 'illustrative', kind=list)
    chars = ctx.cfield('characters', kind=dict)
    cl = ctx.claims()
    by = {c['claimId']: c for c in cl}
    off, absent = [], []
    mapped = _mapped_claims(ctx)
    for cid, c, key in mapped:
        if c is None:
            absent.append(cid)
            continue
        mine, tol = value(ctx, params, key)
        if abs(float(c['value']) - mine) > tol + 1e-9:
            off.append((cid, key, c['value'], round(mine, 4)))
    ill_chars = {k for k, v in chars.items() if isinstance(v, dict) and v.get('illustrative')}
    noflag = [cid for cid in ill if cid in by and not by[cid].get('illustrative')] + [c['claimId'] for c in cl if c.get('character') in ill_chars and not c.get('illustrative')]
    noflag += [f'{cid} (not in claims)' for cid in ill if cid not in by]
    ms = [metric('mapped claims', len(mapped), '>=', 1), metric('mapped claims absent', len(absent), '<=', 0), metric('claims off their re-computation', len(off), '<=', 0),
          *inv(ctx, params), metric('claims missing their ILLUSTRATIVE flag', len(noflag), '<=', 0)]
    return verdict('S05', ms, details=[{'off': off, 'absent': absent, 'missingIllustrative': noflag}])


@rule('S06', 'DX-H6', 'every case the episode promises to show (contract.json coverage[]: attribute "year" or "case", act, values [..] or range [a, b]): page sampler objects '
      'carrying that attribute, visible (opacity > 0.5, on frame) in frames of that act; union over the act. Test D: year, act 3, 1928–1996. Contract without coverage = MISSING',
      'every declared value shown (e.g. 69 of 69 start years), including cases where the thesis did not hold')
def s06_allcases(ctx):
    cov = ctx.cfield('coverage', kind=list)
    p = page(ctx)
    acts = scene_acts(ctx)
    ms, det = [metric('coverage statements', len(cov), '>=', 1)], []
    for c in cov:
        attr, act = c.get('attribute'), c.get('act')
        if attr not in ('year', 'case') or not act:
            raise Missing('contract.json: coverage[].attribute ("year"|"case") / act')
        if c.get('values') is not None:
            want = {str(v) for v in c['values']}
        elif c.get('range'):
            want = {str(y) for y in range(int(c['range'][0]), int(c['range'][1]) + 1)}
        else:
            raise Missing('contract.json: coverage[].values or range')
        track = p.get('yearsTrack' if attr == 'year' else 'casesTrack')
        if track is None:
            raise Missing(f'out/checks/page.json {"yearsTrack" if attr == "year" else "casesTrack"}')
        shown = set()
        for s in track:
            if acts.get(s['scene']) == act:
                shown |= {str(v) for v in s.get('years' if attr == 'year' else 'cases', [])}
        ms.append(metric(f'{attr} values shown in {act}', len(want & shown), '>=', len(want)))
        det.append({'attribute': attr, 'act': act, 'missing': sorted(want - shown)[:30]})
    return verdict('S06', ms, details=det)


def claim_canons(c):
    got = [x for x, _ in numbers_in_text(str(c.get('display', '')))]
    return got


@rule('S07', 'DX-H1, DX-H2', 'claims registry out/claims.json vs what is shown and said. On screen: every number in visible text (page sampler) must sit inside a '
      'claim span (data-claim). Narration: every number in out/script.json text must equal (value+unit) the display of a claim listed for that sentence\'s scene. '
      'Every claim: formula; source or illustrative; historical (source) claims carry dataYear',
      '0 orphan numbers on screen; 0 unregistered numbers in narration; 0 claims without formula; 0 unsourced non-illustrative claims; 0 sourced claims without dataYear')
def s07_claims(ctx):
    cl = ctx.claims()
    p = page(ctx)
    orphans = p.get('orphanNumbers', [])
    by_scene = {}
    for c in cl:
        for sc in c.get('shownIn', []) + [s.get('scene') for s in c.get('spoken', [])]:
            by_scene.setdefault(sc, []).extend(claim_canons(c))
    unreg = []
    for s in ctx.sentences():
        have = by_scene.get(s['scene'], [])
        for cn, span in numbers_in_text(s['text']):
            if not canon_matches(cn, have):
                unreg.append((s.get('id'), span))
    nof = [c['claimId'] for c in cl if not (c.get('formula') or '').strip()]
    unsrc = [c['claimId'] for c in cl if not c.get('source') and not c.get('illustrative')]
    noyear = [c['claimId'] for c in cl if c.get('source') and c.get('historical', True) and not (c.get('dataYear') or c.get('dataYears'))]
    ms = [metric('orphan numbers on screen', len(orphans), '<=', 0), metric('unregistered numbers in narration', len(unreg), '<=', 0),
          metric('claims without formula', len(nof), '<=', 0), metric('unsourced non-illustrative claims', len(unsrc), '<=', 0),
          metric('sourced claims without dataYear', len(noyear), '<=', 0)]
    return verdict('S07', ms, details=[{'orphans': orphans[:10], 'unregistered': unreg[:10], 'noFormula': nof[:10], 'unsourced': unsrc[:10], 'noYear': noyear[:10]}])


@rule('S08', 'DX-H2', 'page sampler, every 0.1 s and every frame in ±0.5 s around each first appearance: frames where an illustrative claim span is visible '
      '(opacity > 0.5, on frame) but no ILLUSTRATIVE badge is visible; and badge lag = first frame the claim is visible − first frame a badge is visible in that scene',
      '0 frames without badge; badge never later than the number (lag ≤ 0 frames)')
def s08_badge(ctx):
    r = page(ctx)['rules'].get('S08')
    if r is None:
        raise Missing('page rule S08 in out/checks/page.json')
    return verdict('S08', [metric('frames without badge', r['framesWithout'], '<=', 0), metric('max badge lag frames', r['maxLagFrames'], '<=', 0)],
                   details=r.get('examples', [])[:10])


BASIS = {'real': re.compile(r"\breal\b|inflation[- ]adjusted|today'?s dollars|\b(19|20)\d\d dollars\b|after inflation", re.I),
         'nominal': re.compile(r'\bnominal\b|before inflation|dollars of the day|then-year', re.I)}


@rule('S09', 'DX-H3', 'claims whose display contains "$" must declare basis nominal|real. Screen (page sampler): whenever a $ claim is visible, a visible text in the same '
      'text block or within 300 px carries its basis word (BASIS regex). Narration: the sentence with the $ number, or the one before it in the same scene, carries the basis word',
      '0 money claims without basis; 0 frames missing the on-screen basis; 0 narration sentences missing it')
def s09_basis(ctx):
    cl = ctx.claims()
    money = [c for c in cl if '$' in str(c.get('display', ''))]
    nob = [c['claimId'] for c in money if c.get('basis') not in ('nominal', 'real')]
    r = page(ctx)['rules'].get('S09', {'framesMissing': None})
    sents = ctx.sentences()
    miss = []
    basis_of = {}
    for c in money:
        for cn in claim_canons(c):
            basis_of.setdefault(cn, set()).add(c.get('basis'))
    for i, s in enumerate(sents):
        for cn, span in numbers_in_text(s['text']):
            if not cn.startswith('usd:'):
                continue
            bs = basis_of.get(cn, {None})
            prev = sents[i - 1]['text'] if i and sents[i - 1]['scene'] == s['scene'] else ''
            if not any(b and (BASIS[b].search(s['text']) or BASIS[b].search(prev)) for b in bs):
                miss.append((s.get('id'), span))
    return verdict('S09', [metric('money claims without basis', len(nob), '<=', 0), metric('frames missing basis on screen', r.get('framesMissing'), '<=', 0),
                           metric('narration $ without basis', len(miss), '<=', 0)], details=[{'noBasis': nob[:10], 'narration': miss[:10], 'screen': r.get('examples', [])[:5]}])


ADVICE = [r"\byou (should|must|need to|ought to|have to|'d better)\b", r'\b(we|i) (recommend|suggest|advise)\b', r'\b(should|must) (you|retirees|investors|everyone)\b',
          r'^(consider|make sure|don\'t|do not|avoid|invest|buy|sell|choose|pick|keep|start|stop|never|always|talk to|plan)\b',
          r'\b(the right|a safe|the safe) (withdrawal )?(rate|amount)\b', r'\bsafe withdrawal rate\b']
FORECAST = [r'\b(will|is going to|are going to)\b[^.]{0,40}\b(rise|fall|crash|return|grow|drop|outperform|underperform|recover|beat)\b',
            r'\b(next|coming) (year|decade|few years|ten years|30 years)\b', r'\bthe market will\b', r'\b(we|i) (expect|predict|forecast)\b',
            r'\bfuture returns (will|are likely)\b']
FOUR = [r'\b4(\.0)?%[^.]{0,30}\b(is|was) (safe|right|enough|the rule|recommended)\b', r'\b4(\.0)?% rule\b', r'\bfour percent rule\b']
WE_BAD = [r'\bwe (all|should|need|must|retire|save|invest|spend|can\'t afford|want to retire)\b', r'\bour (retirement|savings|portfolio|money|future|nest egg)\b',
          r'\blet\'?s (retire|invest|save)\b', r'\bus (retirees|investors|savers)\b']


@rule('S10', 'DX-I1, DX-I2', 'every narration sentence (out/script.json text) and every visible on-screen text, lower-cased, against locked regex lists: ADVICE, FORECAST, FOUR (4% as a recommendation), '
      'WE_BAD ("we/our/us" used for the viewer); required phrases "US only" and "history, not a forecast" (narration or screen)',
      '0 matches of ADVICE, FORECAST, FOUR, WE_BAD; both required phrases present')
def s10_identity(ctx):
    texts = [('narration', s.get('id'), s['text']) for s in ctx.sentences()]
    if ctx.has('out/checks/page.json'):
        seen = set()
        for t, sc, tx in visible_texts(ctx):
            if tx not in seen:
                seen.add(tx)
                texts.append(('screen', sc, tx))
    hits = {'advice': [], 'forecast': [], 'four': [], 'we': []}
    for src, sid, tx in texts:
        low = tx.lower().replace('’', "'")
        low_nf = re.sub(r"(not|n't|never|isn't|is not) a forecast", '', low)
        for k, pats in (('advice', ADVICE), ('forecast', FORECAST), ('four', FOUR), ('we', WE_BAD)):
            for p in pats:
                if re.search(p, low_nf if k == 'forecast' else low, re.M):
                    hits[k].append((src, sid, tx[:90]))
                    break
    alltext = ' '.join(t[2] for t in texts)
    us = bool(re.search(r'\bU\.?S\.? only\b', alltext, re.I))
    hist = bool(re.search(r'history,? not a forecast', alltext, re.I))
    ms = [metric('advice sentences', len(hits['advice']), '<=', 0), metric('forecast sentences', len(hits['forecast']), '<=', 0),
          metric('4% as recommendation', len(hits['four']), '<=', 0), metric('"we" for the viewer', len(hits['we']), '<=', 0),
          metric('"US only" stated', us, '==', True), metric('"history, not a forecast" stated', hist, '==', True)]
    return verdict('S10', ms, details=[{k: v[:5] for k, v in hits.items()}])


@rule('S11', 'DX-S6', 'claims with core=true. Appearances = distinct scenes where the claim is visible (page sampler) or spoken (heard by own ASR in that scene\'s narration window). '
      'Declared callbacks[] each need scene + distinct non-empty meaning, and must be real appearances',
      '≥ 1 core claim; each core claim appears in ≥ 3 distinct scenes spanning ≥ 2 acts; ≥ 3 declared callbacks with distinct meanings, all verified')
def s11_callback(ctx):
    core = [c for c in ctx.claims() if c.get('core')]
    p = page(ctx)
    seen = p.get('claimScenes', {})
    asr = asr_master(ctx)
    acts = scene_acts(ctx)
    ms = [metric('core claims', len(core), '>=', 1)]
    det = []
    for c in core:
        scenes = set(seen.get(c['claimId'], []))
        want = claim_canons(c)
        for s in ctx.sentences():
            if any(canon_matches(w, [x for x, _ in numbers_in_text(s['text'])]) for w in want):
                heard = spoken_numbers(asr_join([w for w in asr if s['start'] - 1 <= w['start'] <= s['end'] + 1]))
                if any(canon_matches(w, heard) for w in want):
                    scenes.add(s['scene'])
        cb = c.get('callbacks', [])
        meanings = [x.get('meaning', '').strip().lower() for x in cb]
        verified = [x for x in cb if x.get('scene') in scenes]
        ms += [metric(f'{c["claimId"]} scenes', len(scenes), '>=', 3), metric(f'{c["claimId"]} acts', len({acts.get(s) for s in scenes}), '>=', 2),
               metric(f'{c["claimId"]} callbacks w/ distinct meaning', len({m for m in meanings if m}), '>=', 3),
               metric(f'{c["claimId"]} callbacks unverified', len(cb) - len(verified), '<=', 0)]
        det.append({'claim': c['claimId'], 'scenes': sorted(scenes)})
    return verdict('S11', ms, details=det)


def first_appearance(ctx):
    """claimId -> first time shown (page sampler) or said (sentence start of the first narration sentence carrying its value)."""
    p = page(ctx)
    first = {k: v for k, v in p.get('claimFirst', {}).items()}
    for c in ctx.claims():
        want = claim_canons(c)
        for s in ctx.sentences():
            if any(canon_matches(w, [x for x, _ in numbers_in_text(s['text'])]) for w in want):
                first[c['claimId']] = min(first.get(c['claimId'], 1e9), s['start'])
                break
    return first


@rule('S12', 'DX-S7', 'new number = first appearance (screen or narration) of a claim; axis-role claims (role "axis", only ever shown as axis labels/anchors per the page sampler) excluded. '
      'Scene of a new number = scene containing its first-appearance time',
      'new numbers ≤ duration / 8 s; no scene with > 2 new numbers; 0 claims marked axis but shown outside axis labels')
def s12_density(ctx):
    first = first_appearance(ctx)
    cl = {c['claimId']: c for c in ctx.claims()}
    p = page(ctx)
    misuse = [k for k, roles in p.get('claimRoles', {}).items() if cl.get(k, {}).get('role') == 'axis' and any(r not in ('axis-label', 'anchor') for r in roles)]
    news = [(t, k) for k, t in first.items() if k in cl and cl[k].get('role') != 'axis' and t < 1e9]
    scenes = ctx.scenes()
    per = {}
    for t, k in news:
        sc = next((s['id'] for s in scenes if s['start'] <= t < s['start'] + s['dur']), scenes[-1]['id'])
        per.setdefault(sc, []).append(k)
    worst = max((len(v) for v in per.values()), default=0)
    total = ctx.total()
    return verdict('S12', [metric('new numbers', len(news), '<=', total / 8), metric('max new numbers in a scene', worst, '<=', 2),
                           metric('axis claims shown outside axes', len(misuse), '<=', 0)],
                   details=[{'limit': round(total / 8, 1), 'crowded': {k: v for k, v in per.items() if len(v) > 2}}])


S13_SHORT = 6      # words: a short sentence
S13_RUN = 3        # this many short sentences in a row = a staccato passage (sổ gu G-009: "không cụt lủn")
S13_MINW = 4       # words: sentences shorter than this do not count toward the length variation


@rule('S13', 'DX-S8 (sổ gu G-009)', 'K2 redefinition. Sentence length = words in each out/script.json sentence text (in script order). (a) Variation: coefficient of variation '
      '(population std / mean) over the sentences of ≥ 4 words: long and short sentences alternate, and fragments cannot buy the variation. (b) Flow: a staccato passage '
      '= ≥ 3 consecutive sentences of ≤ 6 words each (a single short sentence for emphasis is allowed; a string of them is choppy). Narration without numbers is never penalised',
      'PROVISIONAL: CV (sentences ≥ 4 words) ≥ 0.35; 0 staccato passages')
def s13_sentence_flow(ctx):
    ss = ctx.sentences()
    n = np.array([len(words(s['text'])) for s in ss], float)
    m = n[n >= S13_MINW]
    cv = float(m.std() / m.mean()) if len(m) else None
    runs, cur = [], []
    for s, k in zip(ss, n):
        if k <= S13_SHORT:
            cur.append(s)
            continue
        if len(cur) >= S13_RUN:
            runs.append(cur)
        cur = []
    if len(cur) >= S13_RUN:
        runs.append(cur)
    return verdict('S13', [metric('sentence length CV (≥ 4 words)', cv, '>=', 0.35), metric('staccato passages', len(runs), '<=', 0)],
                   details=[{'sentences': len(n), 'mean': round(float(n.mean()), 1) if len(n) else None, 'cvAllSentences': round(float(n.std() / n.mean()), 3) if len(n) else None},
                            *[{'from': r[0].get('id'), 'texts': [x['text'] for x in r]} for r in runs[:10]]])


@rule('S14', 'DX-S10', 'out/adbreaks.json times; act boundaries from out/timeline.json acts; natural silence = span where the master RMS (50 ms/10 ms) stays ≤ −40 dBFS',
      '2 … 3 breaks; each within ±1.0 s of a boundary between two acts (not inside cold open/ident); each inside a silence ≥ 1.0 s')
def s14_adbreaks(ctx):
    br = ctx.json('out/adbreaks.json')['breaks']
    br = [b['t'] if isinstance(b, dict) else b for b in br]
    acts = ctx.acts()
    bounds = [a['start'] for a in acts if a['id'] not in ('cold-open', 'ident', 'act1')]
    sp = silent_spans(master(ctx))
    bad_b = [b for b in br if not bounds or min(abs(b - x) for x in bounds) > 1.0]
    bad_s = [b for b in br if not any(a <= b <= e and e - a >= 1.0 for a, e in sp)]
    return verdict('S14', [metric('ad breaks', len(br), 'in', [2, 3]), metric('breaks off an act boundary', len(bad_b), '<=', 0),
                           metric('breaks without ≥1 s silence', len(bad_s), '<=', 0)], details=[{'breaks': br, 'boundaries': bounds}])


ORDER = ['cold-open', 'ident', 'act1', 'act2', 'act3', 'method', 'outro']


@rule('S15', 'DX-S1', 'out/timeline.json acts[] (id, start, end) and scenes[].act; acts contiguous and in the brief\'s order',
      'order cold-open, ident, act1, act2, act3, method, outro; cold open ≤ 15 s; ident ≤ 3 s; outro ≥ 20 s; timeline total ≥ 600 s; every scene inside its act')
def s15_structure(ctx):
    acts = ctx.acts()
    ids = [a['id'] for a in acts]
    d = {a['id']: a['end'] - a['start'] for a in acts}
    gaps = [(a['id'], b['id']) for a, b in zip(acts, acts[1:]) if abs(a['end'] - b['start']) > 1e-3]
    by = {a['id']: a for a in acts}
    outside = [s['id'] for s in ctx.scenes() if s.get('act') not in by or s['start'] < by[s['act']]['start'] - 1e-3 or s['start'] + s['dur'] > by[s['act']]['end'] + 1e-3]
    ms = [metric('act order', ids, '==', ORDER), metric('cold open s', d.get('cold-open'), '<=', 15.0, 's'), metric('ident s', d.get('ident'), '<=', 3.0, 's'),
          metric('outro s', d.get('outro'), '>=', 20.0, 's'), metric('total s', ctx.total(), '>=', 600.0, 's'), metric('act gaps', len(gaps), '<=', 0),
          metric('scenes outside their act', len(outside), '<=', 0)]
    return verdict('S15', ms, details=[{'gaps': gaps, 'outside': outside[:10]}])


# ---- S16 (K2, sổ gu G-008, PROVISIONAL): decisive numbers tied to the viewer's situation ---------------------------------
S16_SHARE = 0.75  # provisional; no owner-scored episode to calibrate on yet (checks/README.md "Ngưỡng tạm")


def _anchors(ctx):
    """contract.json characters[k].words and scenarios[k].words: the words and phrases by which the script names that character or scenario
    ("the median borrower", "36 months"). A character or scenario without `words` = MISSING (the checker does not guess how the script names it)."""
    out = {}
    for group in ('characters', 'scenarios'):
        for k, v in (ctx.contract().get(group) or {}).items():
            if not isinstance(v, dict):
                continue
            ws = v.get('words')
            if not ws or not isinstance(ws, list):
                raise Missing(f'contract.json: {group}.{k}.words')
            out[f'{group}.{k}'] = [w.lower() for w in ws]
    if not out:
        raise Missing('contract.json: characters or scenarios (with words)')
    return out


def _says(text, phrase):
    """Whole-word, case-insensitive; a one-word phrase also matches its plural ("retiree" / "retirees")."""
    norm = lambda x: ' ' + ' '.join(re.findall(r"[a-z0-9$%]+(?:[.,][0-9]+)*", x.lower())) + ' '
    t, p = norm(text), norm(phrase)
    return p in t or (len(p.split()) == 1 and p[:-1] + 's ' in t)


@rule('S16', 'DX-S3, RUBRIC H4 (sổ gu G-008)', 'decisive numbers = displays of the claims with decisive=true in out/claims.json or listed in contract.json claims.decisive; a decisive '
      'sentence = an out/script.json sentence whose text says one of them (numbers compared as values). It is tied to the viewer\'s situation when that sentence, or any sentence '
      'before it in the same scene (the story has already put the viewer with that person or scenario; sổ gu G-009: a story does not repeat the name in every sentence), names a character or a scenario the episode contract declares (characters.<k>.words, scenarios.<k>.words; whole-word match, case-insensitive). '
      'Contract without the words of its characters/scenarios = MISSING',
      'PROVISIONAL: ≥ 1 decisive sentence; ≥ 75% of decisive sentences tied to a declared character or scenario')
def s16_situation(ctx):
    anchors = _anchors(ctx)
    dec_ids = set(ctx.cfield('claims', 'decisive', kind=list))
    dec = [c for c in ctx.claims() if c.get('decisive') or c.get('claimId') in dec_ids]
    want = {c['claimId']: [x for x, _ in numbers_in_text(str(c.get('display', '')))] for c in dec}
    sents = sorted(ctx.sentences(), key=lambda s: s['start'])
    rows = []
    for i, s in enumerate(sents):
        have = [x for x, _ in numbers_in_text(s['text'])]
        hit = [cid for cid, cs in want.items() if any(canon_matches(c, have) for c in cs)]
        if not hit:
            continue
        j = i
        while j and sents[j - 1].get('scene') == s.get('scene'):
            j -= 1
        ctx_text = ' '.join(x['text'] for x in sents[j:i + 1])
        tied = sorted(k for k, ws in anchors.items() if any(_says(ctx_text, w) for w in ws))
        rows.append({'sentence': s.get('id'), 'claims': hit, 'tiedTo': tied, 'text': s['text'][:120]})
    tied = sum(1 for r in rows if r['tiedTo'])
    share = tied / len(rows) if rows else None
    return verdict('S16', [metric('decisive sentences', len(rows), '>=', 1), metric('share tied to a character or scenario', share, '>=', S16_SHARE)],
                   details=[{'decisiveClaims': sorted(want), 'anchors': sorted(anchors)}, *[r for r in rows if not r['tiedTo']][:15]])
