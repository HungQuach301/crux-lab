"""Episode 2 (C5, stream D): release dossier from the final script v5 and its timing. Never edits a claim value: every figure comes from
out/claims.json (build_numbers.py) and animatic/timing.json (sentence times = the final voice track).

    python3 episodes/ep002/preprod/dossier_c5.py        # then: python3 episodes/ep002/contract_build.py; python3 episodes/ep002/preprod/rights_c5.py

Writes
  out/script.json            {sentences:[{id, n, scene, text, spoken, tag, start, end, claims}]} (text = script.md v5 = timing.json text, asserted)
  out/claims.json            SAME claims and values; adds shownIn / spoken / callbacks, and the helper claims of HELPERS (numbers the narration
                             or the description says in another form than a claim display: "about 1 in 7", "3-month", "2 points", "1954 to 1980").
                             Idempotent: helpers and added fields are rebuilt on every run (re-run after build_numbers.py).
  out/timeline.json, out/captions.srt, out/adbreaks.json, out/transitions.json, out/tension-map.json + .png,
  preprod/shotlist.json, preprod/storyboard.md, preprod/color-script.md,
  out/package/description.md (+ out/package/description-claims.json: every number of the description -> claim ID)

Re-run after: a new timing.json (voice/pause change), the final mix (A: tension map is then measured from the stems), the render (P: in-scene
dips are re-read from animatic/src/anchors/*.json).

Acts (checks/CONTRACT.md order cold-open, ident, act1, act2, act3, method, outro; story/beats.md):
  cold-open S01 (CO-A: the dated context line, Leah's two offers, the question) · act1 S02-S05 (why private loans, the loan and the head start,
  the promise, the first result = the contradiction; climax S05.4) · act2 S06-S08 (the cushion, two kinds of history, the worst stretch;
  climax S08.7) · act3 S09-S10 (moving the head start, the answer in two halves; climax S10.6) · method S11 (method card) ·
  outro S12-S13 (where an offer falls, history not a forecast, end-screen tail). No ident is rendered; the timeline does not invent one.
"""
import importlib.util
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.normpath(os.path.join(HERE, '..'))
REPO = os.path.normpath(os.path.join(EP, '..', '..'))
P = lambda *p: os.path.join(EP, *p)
J = lambda *p: json.load(open(P(*p), encoding='utf-8'))

# captions(): the cue splitter of Episode 1 (same rules: <= 2 lines x <= 42 chars, 1.0-7.0 s, no overlap, text = script text). Reused, not copied.
_spec = importlib.util.spec_from_file_location('ep1_dossier', os.path.join(REPO, 'episodes', 'ep001', 'preprod', 'dossier_c5.py'))
_ep1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_ep1)
captions, fmt_t = _ep1.captions, _ep1.fmt_t


def dump(obj, *p):
    os.makedirs(os.path.dirname(P(*p)), exist_ok=True)
    json.dump(obj, open(P(*p), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)


ACT = {'S01': 'cold-open', **{f'S{i:02d}': 'act1' for i in range(2, 6)}, **{f'S{i:02d}': 'act2' for i in range(6, 9)},
       'S09': 'act3', 'S10': 'act3', 'S11': 'method', 'S12': 'outro', 'S13': 'outro'}
# per scene: layout family/variant, shot size, chart, look (design/c3/final/system.md: H2 = geometry of interest, H3 = history timeline;
# animatic/README.md scene table), working title
SCENE = {
    'S01': ('offer/two-cards', 'medium', 'card', 'H2', 'Two offers'),
    'S02': ('cost/federal-limit', 'wide', 'bar', 'H2', 'Why private loans'),
    'S03': ('offer/head-start', 'medium', 'card', 'H2', "Leah's loan and the head start"),
    'S04': ('ridge/replay', 'wide', 'line', 'H3', 'Every stretch since January 1954'),
    'S05': ('ridge/bins', 'wide', 'cells', 'H3', 'The contradiction'),
    'S06': ('jar/cushion', 'medium', 'line', 'H2', 'The cushion'),
    'S07': ('ridge/two-halves', 'wide', 'line', 'H3', 'Two kinds of history'),
    'S08': ('ridge/worst-window', 'medium', 'line', 'H3', 'The worst stretch: April 1977'),
    'S09': ('columns/head-start', 'wide', 'bar', 'H3', 'Moving the head start'),
    'S10': ('columns/answer', 'wide', 'bar', 'H3', 'Other offers, and the answer'),
    'S11': ('card/method', 'wide', 'card', 'H3', 'How we know this'),
    'S12': ('columns/offer-line', 'wide', 'bar', 'H3', 'Where an offer falls'),
    'S13': ('card/end-screen', 'wide', 'card', 'H3', 'End screen'),
}
JOIN = {
    'S02': ('semantic', 'the question -> why the two offers are private ones'),
    'S03': ('geometric', 'same two offer cards; the loan and the head start are put on them'),
    'S04': ('semantic', 'the head start can be anything -> the promise: replay it through history'),
    'S05': ('geometric', 'same ridge; the replays drop their results into the two halves'),
    'S06': ('semantic', 'act boundary (ad break): "the head start" explains it -> the cushion it builds'),
    'S07': ('semantic', 'a falling stretch keeps the cushion -> the two kinds of history'),
    'S08': ('geometric', 'same ridge; the frame lands on the worst start, April 1977'),
    'S09': ('semantic', 'act boundary (ad break): the worst case of one pair of rates -> other pairs'),
    'S10': ('geometric', 'same two columns; the head start keeps moving'),
    'S11': ('semantic', 'the answer -> how it was built (method card)'),
    'S12': ('semantic', 'the method -> where an offer falls on the line'),
    'S13': ('semantic', 'history, not a forecast -> end screen'),
}
TENSION = {'S01': 0.55, 'S02': 0.33, 'S03': 0.40, 'S04': 0.50, 'S05': 0.62, 'S06': 0.42, 'S07': 0.55, 'S08': 0.70, 'S09': 0.50,
           'S10': 0.62, 'S11': 0.28, 'S12': 0.40, 'S13': 0.20}
CLIMAX = {'act1': ('S05.4', 0.86), 'act2': ('S08.7', 0.92), 'act3': ('S10.6', 0.88)}
# releases after each climax (valleys): the act boundary that follows (ad break) and the method card
RELEASE = [('S06.1', 0.34), ('S09.1', 0.34), ('S11.1', 0.24)]
TURNS = [('S01.3', 'the question: how much lower must a variable rate start'),
         ('S04.6', 'history, not a forecast (US only, S04.2)'),
         ('S05.1', 'act 1 turn: the first result looks like a contradiction'),
         ('S05.4', 'act 1 climax: 1 in 7 is two very different halves, plus the worst stretch'),
         ('S06.3', 'the cushion has to be used up before the variable loan costs more'),
         ('S07.5', 'act 2 turn: the climbing half vs the falling half'),
         ('S08.7', 'act 2 climax: the worst stretch charges 43% more interest'),
         ('S09.5', 'at 2 points the later half clears; the earlier half does not'),
         ('S10.3', 'at every head start tested, some 1954-to-1980 starts still cost more'),
         ('S10.6', 'act 3 climax: the answer in two halves'),
         ('S12.4', 'the line does not say which offer is better')]
# in-scene dips (picture changes inside a scene) = the "dip"/"cut" anchors of the animatic (animatic/src/anchors/Sxx.json, actions "dip ...")

# ---- helper claims: numbers said in another form than a claim display (Episode 1 pattern: k35 / y3 / cut36_large_words) ----------------------
FRED = {'id': 'fred-tb3ms', 'url': 'https://fred.stlouisfed.org/series/TB3MS'}


def helpers(by):
    v = lambda k: by[k]['value']
    H = [
        {'claimId': 'share_all_words', 'value': 1 / 7, 'display': 'about 1 in 7', 'parent': 'share_all',
         'formula': f'spoken form of share_all ({by["share_all"]["display"]}): |share_all - 100/7| <= 0.5 point', 'check': abs(v('share_all') - 100 / 7) <= 0.5},
        {'claimId': 'share_early_words', 'value': 1 / 4, 'display': 'more than 1 in 4', 'parent': 'share_early',
         'formula': f'spoken form of share_early ({by["share_early"]["display"]}): share_early > 25', 'check': v('share_early') > 25},
        {'claimId': 'share_late_words', 'value': 1 / 30, 'display': 'about 1 in 30', 'parent': 'share_late',
         'formula': f'spoken form of share_late ({by["share_late"]["display"]}): |share_late - 100/30| <= 0.5 point', 'check': abs(v('share_late') - 100 / 30) <= 0.5},
        {'claimId': 'share_rate_above_fixed_words', 'value': 3 / 4, 'display': 'about 3 in 4', 'parent': 'share_rate_above_fixed',
         'formula': f'spoken form of share_rate_above_fixed ({by["share_rate_above_fixed"]["display"]}): |x - 75| <= 2 points',
         'check': abs(v('share_rate_above_fixed') - 75) <= 2},
        {'claimId': 'first_payment_gap_words', 'value': 40, 'display': 'about $40', 'parent': 'first_payment_gap', 'basis': 'nominal',
         'formula': f'spoken form of first_payment_gap ({by["first_payment_gap"]["display"]}) rounded to the nearest $10', 'check': round(v('first_payment_gap'), -1) == 40},
        {'claimId': 'best_diff_words', 'value': -v('best_diff'), 'display': '$15,295 less', 'parent': 'best_diff', 'basis': 'nominal',
         'formula': f'spoken form of best_diff ({by["best_diff"]["display"]}): the same amount said as "less than the fixed loan"',
         'check': round(-v('best_diff')) == 15295},
    ]
    for k, lab in (('m1', 'minus 1 point'), ('0', '0 points'), ('1', '1 point'), ('2', '2 points'), ('3', '3 points')):
        x = -1.0 if k == 'm1' else float(k)
        H.append({'claimId': f'hs_{k}', 'value': x, 'display': lab,
                  'formula': f'head start tested = fixed_rate - variable start rate = {x:g} point(s) (contract model.params.spreads; sensitivity key)',
                  'check': x in [float(s) for s in J('contract.json')['model']['params']['spreads']]})
    for h in H:
        h.update({'source': None, 'historical': False, 'illustrative': True, 'kind': 'words' if h['claimId'].endswith('_words') else 'param',
                  'helper': 'stream D (preprod/dossier_c5.py)'})
    H += [
        {'claimId': 'tbill_3month', 'value': 3, 'display': '3-month', 'formula': 'maturity of the index series: TB3MS = 3-Month Treasury Bill Secondary Market Rate (data/sources.json)',
         'source': FRED, 'dataYears': [1954, 2026], 'historical': True, 'illustrative': False, 'kind': 'data', 'check': True},
        {'claimId': 'tb_peak_date', 'value': '1981-05', 'display': 'May 1981', 'parent': 'tb_peak', 'formula': 'month of tb_peak (max TB3MS 1934-01..2026-08)',
         'source': FRED, 'dataYear': 1981, 'historical': True, 'illustrative': False, 'kind': 'data', 'check': 'May 1981' in str(by['tb_peak'].get('words', ''))},
        {'claimId': 'period_early', 'value': '1954-01..1980-12', 'display': '1954 to 1980', 'parent': 'n_early',
         'formula': 'start months of the first period: model.params firstStart 1954-01 to the month before periodBreaks[0] 1981-01 (n_early)',
         'source': FRED, 'dataYears': [1954, 1980], 'historical': True, 'illustrative': False, 'kind': 'model', 'check': '1954-01..1980-12' in by['n_early']['formula']},
        {'claimId': 'period_late', 'value': '1981-01..2016-09', 'display': '1981 on', 'parent': 'n_late',
         'formula': 'start months of the second period: periodBreaks[0] 1981-01 to the last start (n_late)',
         'source': FRED, 'dataYears': [1981, 2016], 'historical': True, 'illustrative': False, 'kind': 'model', 'check': '1981-01' in by['n_late']['formula']},
    ]
    for h in H:
        h['helper'] = 'stream D (preprod/dossier_c5.py)'
        assert h.pop('check') is True, h['claimId']
    return H


# per sentence: helper claims it says (numbers not in the display of a script-listed claim)
SAYS = {'S03.2': ['first_payment_gap_words'], 'S04.2': ['tbill_3month'], 'S04.4': ['hs_3', 'hs_m1'], 'S05.2': ['share_rate_above_fixed_words'],
        'S05.3': ['share_all_words'], 'S05.4': ['share_all_words', 'share_early_words', 'share_late_words', 'period_early', 'period_late'],
        'S07.2': ['period_early'], 'S07.3': ['tb_peak_date'], 'S07.6': ['best_diff_words'], 'S09.5': ['hs_2', 'period_early', 'period_late'],
        'S09.6': ['hs_3', 'period_early', 'period_late'], 'S10.3': ['period_early'], 'S10.6': ['period_late', 'hs_2', 'period_early', 'hs_3'],
        'S11.1': ['tbill_3month'], 'S12.1': ['hs_2']}
# callbacks of the core claims: (scene, meaning). Only scenes where the claim is shown or said (animatic claimsUsed + narration); S11 checks them.
CALLBACKS = {
    'share_early': [('S05', 'stated once: the 1954-to-1980 share of the first result'),
                    ('S07', 'recalled on screen under the climbing half of the history')],
    'share_late': [('S05', 'stated once: the from-1981 share of the first result')],
    'worst_diff': [('S05', 'stated once: the worst stretch, from April 1977')],
}


def script_rows():
    rows = {}
    for line in open(P('story', 'script.md'), encoding='utf-8'):
        m = re.match(r'^(S\d\d\.\d+) \| (.*?) \| (.*?) \| (.*)$', line.rstrip('\n'))
        if m:
            tag = re.match(r'^\[(\w+)\]\s*', m.group(2))
            ids = [i.strip(' `') for i in m.group(3).split(',') if i.strip(' `') not in ('—', '')]
            rows[m.group(1)] = {'text': m.group(2)[tag.end():] if tag else m.group(2), 'tag': tag.group(1) if tag else None, 'claims': ids, 'picture': m.group(4)}
    return rows


def checks_common():
    """numbers_in_text / canon_matches of the checker (for the self-checks only); from the checks copy in K_CHECKS or the repo."""
    for d in (os.environ.get('K_CHECKS'), os.path.join(REPO, 'checks', 'py')):
        if d and os.path.exists(os.path.join(d, 'common.py')):
            sys.path.insert(0, d)
            import common
            return common
    raise SystemExit('checks common.py not found')


def build_script(T, rows):
    sents, n = [], 0
    for sc in T['scenes']:
        for x in sc['sentences']:
            r = rows[x['id']]
            assert r['text'] == x['text'], (x['id'], r['text'], x['text'])
            assert (r['tag'] or None) == (x.get('tag') or None), x['id']
            n += 1
            sents.append({'id': x['id'], 'n': n, 'scene': sc['id'], 'text': x['text'], 'spoken': x['spoken'], 'tag': x.get('tag'),
                          'start': round(x['start'], 3), 'end': round(x['end'], 3), 'claims': r['claims'] + SAYS.get(x['id'], [])})
    assert len(sents) == len(rows), (len(sents), len(rows))
    dump({'source': 'story/script.md (v5) + animatic/timing.json (sentence times on the narration track = the final video; asserted text-equal)',
          'spokenRule': 'spoken = the words sent to eleven_v3 without the emotion tag (tag kept in `tag`): a tag is an instruction, not a word or a pause',
          'sentences': sents}, 'out', 'script.json')
    return sents


def build_claims(sents, C):
    data = J('out', 'claims.json')
    cl = [c for c in data['claims'] if not c.get('helper')]
    for c in cl:
        for k in ('shownIn', 'spoken', 'callbacks'):
            c.pop(k, None)
    by = {c['claimId']: c for c in cl}
    before = {c['claimId']: c['value'] for c in cl}
    H = helpers(by)
    cl += H
    by = {c['claimId']: c for c in cl}
    rep = J('animatic', 'check-report.json')['scenes']
    shown = {}
    for sc, r in rep.items():
        for cid in r['claimsUsed']:
            shown.setdefault(cid, []).append(sc)
    for c in cl:
        c['shownIn'] = sorted(set(shown.get(c['claimId'], [])))
        c['spoken'] = []
    # spoken: a claim listed for the sentence whose display number is in the sentence text
    for s in sents:
        have = [x for x, _ in C.numbers_in_text(s['text'])]
        for cid in s['claims']:
            c = by[cid]
            want = [x for x, _ in C.numbers_in_text(str(c['display']))]
            if want and all(C.canon_matches(w, have) for w in want):
                c['spoken'].append({'sentence': s['id'], 'scene': s['scene']})
    for cid, cbs in CALLBACKS.items():
        by[cid]['callbacks'] = [{'scene': s, 'meaning': m} for s, m in cbs]
    for c in cl:
        c.setdefault('callbacks', [])
    assert all(by[k]['value'] == v for k, v in before.items())          # no claim value changed
    data['claims'] = cl
    data['_dossier'] = ('stream D (preprod/dossier_c5.py, C5): shownIn = animatic/check-report.json claimsUsed (the page sampler re-measures on the '
                        'final render); spoken = sentences of out/script.json whose text says the claim display; callbacks of core claims; helper '
                        'claims (field helper) for numbers said in another form. No value of build_numbers.py changed (asserted).')
    dump(data, 'out', 'claims.json')
    # self-check (S07 narration): every number of every sentence matches a claim of that scene
    per = {}
    for c in cl:
        for sc in c['shownIn'] + [x['scene'] for x in c['spoken']]:
            per.setdefault(sc, []).extend(x for x, _ in C.numbers_in_text(str(c['display'])))
    unreg = [(s['id'], span) for s in sents for cn, span in C.numbers_in_text(s['text']) if not C.canon_matches(cn, per.get(s['scene'], []))]
    assert not unreg, unreg
    return cl


def anchors_dips(T):
    """In-scene dips: anchors whose action starts with 'dip' (animatic/src/anchors/Sxx.json), resolved on the current timing like build_anchors.py."""
    st = {x['id']: x for sc in T['scenes'] for x in sc['sentences']}
    out = []
    for sc in T['scenes']:
        f = P('animatic', 'src', 'anchors', f'{sc["id"]}.json')
        if not os.path.exists(f):
            continue
        A = json.load(open(f, encoding='utf-8'))
        for a in A.get('anchors', A if isinstance(A, list) else []):
            if not str(a.get('action', '')).startswith('dip'):
                continue
            s = st[a['sentence']]
            if a.get('at') == 'start':
                t = s['start'] + float(a.get('dt', 0))
            elif a.get('at') == 'end':
                t = s['end'] + float(a.get('dt', 0))
            else:
                ra = next((x for x in J('animatic', 'anchors.json')['anchors'] if x['scene'] == sc['id'] and x['id'] == a['id']), None)
                t = ra['resolved_s'] if ra else None
            if t is not None and t - sc['start'] > 0.5:
                out.append((sc['id'], round(t, 3), a['id'], a['action']))
    return out


def main():
    C = checks_common()
    T = J('animatic', 'timing.json')
    rows = script_rows()
    sents = build_script(T, rows)
    build_claims(sents, C)
    sid = {s['id']: s for s in sents}
    fps = T['fps']
    scenes = [{'id': s['id'], 'start': round(s['start'], 3), 'end': round(s['end'], 3)} for s in T['scenes']]
    total = round(scenes[-1]['end'], 3)
    rows_t = []
    for s in scenes:
        lay, shot, chart, look, title = SCENE[s['id']]
        rows_t.append({'id': s['id'], 'act': ACT[s['id']], 'start': s['start'], 'dur': round(s['end'] - s['start'], 3), 'layout': lay, 'shot': shot,
                       'panels': ['*'], 'chart': chart, 'move': 0.0, 'look': look, 'title': title})
    acts = []
    for r in rows_t:
        if acts and acts[-1]['id'] == r['act']:
            acts[-1]['end'] = round(r['start'] + r['dur'], 3)
        else:
            acts.append({'id': r['act'], 'start': r['start'], 'end': round(r['start'] + r['dur'], 3)})
    for a in acts:
        if a['id'] in CLIMAX:
            a['climax'] = sid[CLIMAX[a['id']][0]]['start']
    turns = [{'t': sid[k]['start'], 'scene': sid[k]['scene'], 'sentence': k, 'what': w} for k, w in TURNS]
    dump({'fps': fps, 'total': total, 'acts': acts, 'scenes': rows_t, 'turns': turns,
          'source': f'animatic/timing.json (sentence times, {total} s narration incl. the S13 end-screen tail) + preprod/dossier_c5.py; a scene starts at its first sentence',
          'note': 'no ident is rendered; move = 0 (2D H2/H3 frames, picture changes inside a scene are dips, see out/transitions.json); out/camera.json (P) overrides it. '
                  'Acts: cold-open S01, act1 S02-S05, act2 S06-S08, act3 S09-S10, method S11 (method card), outro S12-S13'},
         'out', 'timeline.json')
    # ---- ad breaks: act boundaries act1|act2 and act2|act3, in the middle of the voice gap before the boundary
    br = []
    for aid in ('act2', 'act3'):
        b = next(a['start'] for a in acts if a['id'] == aid)
        prev = max(s['end'] for s in sents if s['end'] <= b + 1e-6)
        nxt = min(s['start'] for s in sents if s['start'] >= b - 1e-6)
        assert nxt - prev >= 1.0, (aid, prev, nxt)
        br.append(round((prev + nxt) / 2, 3))
    dump({'breaks': br, 'voiceGaps': [], 'why': 'act boundaries: end of act 1 (after S05.5 "The reason both are true is the head start.") and end of act 2 '
                                              '(after S08.8 "... would have made this worst case smaller."); each break is the middle of the voice gap (>= 1.1 s) '
                                              'at the scene cut, within 1 s of the act start. The mix must keep >= 1 s under -40 dBFS around it (S14)'},
         'out', 'adbreaks.json')
    gaps = []
    for b in br:
        prev = max(s['end'] for s in sents if s['end'] <= b)
        nxt = min(s['start'] for s in sents if s['start'] >= b)
        gaps.append([prev, nxt])
    ab = J('out', 'adbreaks.json')
    ab['voiceGaps'] = gaps
    dump(ab, 'out', 'adbreaks.json')
    # ---- transitions
    dips = anchors_dips(T)
    cuts = []
    for prev, s in zip(scenes, scenes[1:]):
        m, why = JOIN[s['id']]
        cuts.append({'t': s['start'], 'from': prev['id'], 'to': s['id'], 'type': 'dip', 'match': m, 'audio': None, 'reason': why})
    for sc, t, aid, act in dips:
        cuts.append({'t': t, 'from': f'{sc}', 'to': f'{sc}/{aid}', 'type': 'dip', 'match': 'semantic', 'audio': None,
                     'reason': 'picture change inside the scene (animatic anchor "' + aid + '": ' + act[:90] + ')'})
    cuts.sort(key=lambda c: c['t'])
    dump({'cuts': cuts, 'source': 'scene cuts from animatic/timing.json; in-scene picture changes from the "dip" anchors of animatic/src/anchors/Sxx.json. '
                                  'type "dip" = the animatic\'s 0.44 s dip through the background (animatic/README.md "Giới hạn"); P re-declares if the render '
                                  'uses hard cuts. audio = null: J/L cuts belong to the mix (stream A) and are not claimed here'}, 'out', 'transitions.json')
    # ---- captions
    cues = captions(sents)
    with open(P('out', 'captions.srt'), 'w', encoding='utf-8') as f:
        for i, c in enumerate(cues, 1):
            f.write(f"{i}\n{fmt_t(c['start'])} --> {fmt_t(c['end'])}\n" + '\n'.join(c['lines']) + '\n\n')
    tension_map(rows_t, acts, sents, cuts, total, sid)
    shotlist(rows_t, dips, rows)
    description(rows_t, total, C)
    print(f'script {len(sents)} sentences; timeline {len(rows_t)} scenes, acts {[a["id"] for a in acts]}; {len(cuts)} cuts; {len(cues)} cues; breaks {br}; total {total}')


def tension_map(rows, acts, sents, cuts, total, sid):
    import numpy as np
    pts = [(r['start'] + 0.5 * r['dur'], TENSION[r['id']]) for r in rows]
    peaks = []
    for a in acts:
        if a.get('climax') is not None:
            pts.append((a['climax'], CLIMAX[a['id']][1]))
            peaks.append(a['climax'])
    rel = [(sid[k]['start'], v) for k, v in RELEASE]
    pts += rel
    pts.sort()
    valleys = [min([(t, v) for t, v in pts if p < t <= p + 45], key=lambda x: x[1])[0] for p in peaks]
    ts = np.arange(0.0, math.floor(total) + 1.0, 1.0)
    ten = np.interp(ts, [0.0] + [t for t, _ in pts] + [total], [pts[0][1]] + [v for _, v in pts] + [pts[-1][1]])
    peaks = [float(ts[np.argmin(abs(ts - p))]) for p in peaks]
    valleys = [float(ts[np.argmin(abs(ts - v))]) for v in valleys]
    ct = np.array([c['t'] for c in cuts])
    cut_rate = [int(np.sum((ct > t - 5) & (ct <= t + 5))) for t in ts]
    stems = {n: P('out', 'audio', 'stems', f'{n}.wav') for n in ('voice', 'music', 'sfx', 'whoosh')}
    measured = all(os.path.exists(p) for p in stems.values())
    if measured:
        import soundfile as sf
        lv = {}
        for n, p in stems.items():
            x, sr = sf.read(p, always_2d=True)
            x = x.mean(axis=1)
            lv[n] = np.array([20 * np.log10(np.sqrt(np.mean(x[int(max(0, t - 0.5) * sr):int((t + 0.5) * sr)] ** 2)) + 1e-9) for t in ts])
        music = lv['music']
        dens = np.convolve(sum((lv[n] > -45).astype(float) for n in lv), np.ones(5) / 5, mode='same')
    else:
        speaking = np.array([any(s['start'] <= t <= s['end'] for s in sents) for t in ts], float)
        music = -34.0 + 14.0 * ten
        dens = np.convolve(1.0 + speaking + (ten > 0.5), np.ones(5) / 5, mode='same')
    samples = [{'t': float(t), 'cutRate': c, 'audioDensity': round(float(d), 3), 'musicLevel': round(float(m), 2), 'tension': round(float(v), 3)}
               for t, c, d, m, v in zip(ts, cut_rate, dens, music, ten)]
    dump({'samples': samples, 'peaks': [{'t': p} for p in peaks], 'valleys': [{'t': v} for v in valleys],
          'audio': 'measured from out/audio/stems (1 s RMS dB; stems above -45 dBFS, 5 s mean)' if measured else
                   'planned (no stems yet): musicLevel = -34 + 14 x tension dB, audioDensity = voice + music + 1 when tension > 0.5; re-run after the mix (stream A)',
          'tension': 'planned: story/beats.md feeling per scene (midpoints) + act climaxes (timeline acts[].climax: S05.4, S08.7, S10.6) + releases at the '
                     'two ad breaks and the method card (S06.1, S09.1, S11.1); linear between points',
          'cutRate': 'cuts and dips per 10 s window from out/transitions.json'}, 'out', 'tension-map.json')
    from PIL import Image, ImageDraw
    W, H, L, R, TOP, BOT = 1600, 500, 60, 20, 30, 60
    im = Image.new('RGB', (W, H), '#0e1116')
    d = ImageDraw.Draw(im)
    X = lambda t: L + (W - L - R) * t / total
    Y = lambda v: TOP + (H - TOP - BOT) * (1 - v)
    for a in acts:
        d.line([(X(a['start']), TOP), (X(a['start']), H - BOT)], fill='#2a303b', width=1)
        d.text((X(a['start']) + 4, H - BOT + 8), a['id'], fill='#9aa4b2')
    cmax = max(cut_rate) or 1
    d.line([(X(t), Y(c / cmax * 0.3)) for t, c in zip(ts, cut_rate)], fill='#2a303b', width=2)
    mm = (music - music.min()) / (music.max() - music.min() + 1e-9)
    d.line([(X(t), Y(0.1 + 0.8 * m)) for t, m in zip(ts, mm)], fill='#4c8dff', width=1)
    d.line([(X(t), Y(v)) for t, v in zip(ts, ten)], fill='#f2f4f7', width=3)
    for p, col in [(p, '#e5484d') for p in peaks] + [(v, '#3fbf7f') for v in valleys]:
        v = float(np.interp(p, ts, ten))
        d.ellipse([X(p) - 6, Y(v) - 6, X(p) + 6, Y(v) + 6], fill=col)
    for m in range(0, int(total) + 1, 60):
        d.text((X(m) - 8, H - 24), f'{m // 60}:00', fill='#9aa4b2')
    d.text((L, 6), 'Tension (white), music level (blue, ' + ('measured' if measured else 'planned') + '), cut rate (grey); peaks red, valleys green', fill='#f2f4f7')
    im.save(P('out', 'tension-map.png'))


def shotlist(rows, dips, srows):
    shots = []
    for r in rows:
        ds = sorted((t, aid, act) for sc, t, aid, act in dips if sc == r['id'])
        bounds = [(r['start'], 'scene start', SCENE[r['id']][4])] + ds + [(r['start'] + r['dur'], None, None)]
        for k in range(len(bounds) - 1):
            t0, aid, act = bounds[k]
            shots.append({'id': f'sh{len(shots) + 1:03d}', 'scene': r['id'], 'act': r['act'], 'start': round(t0, 3), 'dur': round(bounds[k + 1][0] - t0, 3),
                          'look': r['look'], 'layout': r['layout'], 'size': r['shot'], 'move': 'static',
                          'what': act if k else r['title'],
                          'moveReason': ('a 2D frame read against its fixed scale: the frame holds still while the marks move, and a change of picture is a '
                                         'dip through the background, not a camera move')})
    dump({'source': 'out/timeline.json + in-scene dips (animatic/src/anchors/Sxx.json); 2.5D: no simulated focal length, no 3D camera angle. '
                    'Storyboard: preprod/storyboard.md (animatic strips); colour script: preprod/color-script.md',
          'shots': shots}, 'preprod', 'shotlist.json')
    # storyboard: the animatic strips per scene and the key-beat strips, with the script's picture note
    lines = ['# Tập 2 — Storyboard (C5, stream D; from the C4 animatic)', '',
             'Frames: `animatic/strips/Sxx.png` (6 frames per scene, evenly spaced in the scene\'s sentences) and `animatic/strips/KEY-n.png` (+ `-masked`). '
             'Picture notes: `story/script.md` v5 (picture column), adapted in C4 as listed in `animatic/README.md` ("Cần chủ dự án xem").', '']
    for r in rows:
        lines += [f'## {r["id"]} — {r["title"]} ({r["act"]}, {r["layout"]}, {r["look"]})', '', f'![{r["id"]}](../animatic/strips/{r["id"]}.png)', '']
        for k, v in srows.items():
            if k.startswith(r['id'] + '.') and v['picture'].strip() not in ('—', ''):
                lines.append(f'- {k}: {v["picture"]}')
        lines.append('')
    lines += ['## Key beats', ''] + [f'- KEY-{n}: ![KEY-{n}](../animatic/strips/KEY-{n}.png) · masked: `animatic/strips/KEY-{n}-masked.png`' for n in range(1, 8)]
    open(P('preprod', 'storyboard.md'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    tok = json.load(open(P('design', 'c3', 'final', 'tokens.json'), encoding='utf-8'))
    roles = tok['roles']
    cs = ['# Tập 2 — Colour script (C5, stream D)', '',
          'One colour set for the whole episode: `design/c3/final/tokens.json` (Episode 1 channel tokens + E2 aliases `costlier` #C72323, `cushion` #269783). '
          'Background `bg` #0E1116 throughout; one meaning per colour (story/beats.md "Visual vocabulary").', '', '| role | colour | use |', '|---|---|---|']
    for k in ('tbill', 'fixed', 'leah', 'above-fixed', 'costlier', 'not-costlier', 'cushion', 'head-start', 'badge'):
        cs.append(f'| {k} | {roles[k].split(":")[0].split(" ")[0]} | {roles[k]} |')
    cs += ['', '| scene | dominant colours (in order of area) | mood |', '|---|---|---|']
    MOOD = {'S01': ('ink, ink-muted, cushion', 'quiet, one person'), 'S02': ('ink-muted, grid, ink', 'plain, orienting'),
            'S03': ('ink, cushion, warn (reversed gap)', 'clarity'), 'S04': ('accent (ridge), grid', 'anticipation'),
            'S05': ('warn (amber tally), costlier, grid', 'surprise'), 'S06': ('cushion (jar), warn, costlier', '"aha"'),
            'S07': ('accent, cushion, costlier', 'perspective'), 'S08': ('accent, warn, costlier', 'weight (darkest moment)'),
            'S09': ('cushion (gap), costlier, grid', 'locating an offer'), 'S10': ('costlier then grid, warn (reversed)', 'sober clarity'),
            'S11': ('ink, ink-muted on bg', 'trust, calm'), 'S12': ('ink-muted, costlier (both halves)', 'warm close'), 'S13': ('accent (quiet band), grid', 'release')}
    for r in rows:
        cs.append(f'| {r["id"]} | {MOOD[r["id"]][0]} | {MOOD[r["id"]][1]} |')
    open(P('preprod', 'color-script.md'), 'w', encoding='utf-8').write('\n'.join(cs) + '\n')


def description(rows, total, C):
    cl = {c['claimId']: c for c in J('out', 'claims.json')['claims']}
    d = lambda k: cl[k]['display']
    CH = [('S01', 'Two offers'), ('S02', 'Why private loans'), ('S03', "Leah's loan and the head start"), ('S04', 'Every stretch since January 1954'),
          ('S05', 'The contradiction'), ('S06', 'The cushion'), ('S07', 'Two kinds of history'), ('S08', 'The worst stretch: April 1977'),
          ('S09', 'Moving the head start'), ('S10', 'Other offers, and the answer'), ('S11', 'How we know this'), ('S12', 'Where an offer falls')]
    start = {r['id']: r['start'] for r in rows}
    ch = [(0 if sc == 'S01' else int(math.floor(start[sc])), t) for sc, t in CH]
    lens = [b[0] - a[0] for a, b in zip(ch, ch[1:])] + [total - ch[-1][0]]
    assert ch[0][0] == 0 and min(lens) >= 10, lens
    chap = '\n'.join(f'{s // 60}:{s % 60:02d} {t}' for s, t in ch)
    # S10.1 steps (owner, C4): per half and worst for 1 point, 0 and -1 point; and the head starts the narration states (3, 2, Leah's 1.5)
    step = lambda hs, k, sp: (f'- {d(hs)}: {d(sp)} of all starts cost more in total interest; {d(k + "_early")} of starts from {d("period_early")}, '
                              f'{d(k + "_late")} of starts from {d("period_late")}; worst stretch {d(k + "_worst")} ({d("gap_worst_start_all")}).')
    text = f"""<!-- out/package/description.md · generated by preprod/dossier_c5.py (stream D, C5). Every number -> claim ID: out/package/description-claims.json. Title: C6. -->

From {d('ctx_plus_end')}, new graduate students in the US can no longer borrow federal Grad PLUS loans, so more of them will compare private loans. Leah, an illustrative student, has two private offers: {d('fixed_rate')} fixed, or variable starting lower, at {d('var_start')}. This video replays her illustrative loan, {d('loan')} over {d('term')}, through every 10-year stretch of US interest rates since {d('first_start')}, to see how much lower a variable rate has had to start before the risk was worth it, in history.

"Worth it" has one plain meaning here: how often the variable loan cost more in total interest than the {d('fixed_rate')} fixed loan, and how much more at worst.

Chapters
{chap}

What the replay found (history, not a forecast; US only; ILLUSTRATIVE: Leah's pair of rates and her loan are not a real lender's offer)
- Leah's head start is {d('gap_start')} ({d('fixed_rate')} fixed minus {d('var_start')} variable). At some point her variable rate rose above {d('fixed_rate')} in {d('share_rate_above_fixed')} of stretches, yet it cost more in total interest in {d('share_all')}: {d('share_early')} of starts from {d('period_early')} and {d('share_late')} of starts from {d('period_late')}. The worst stretch, from {d('worst_start')}, cost {d('worst_diff')} more, {d('worst_share_of_fixed')} more interest than the fixed loan's {d('fixed_int')}.
- The best stretch began in {d('best_start')} and cost {d('best_diff_words')} than the fixed loan.
The same replay with the fixed rate held at {d('fixed_rate')} and other variable starting rates:
{step('hs_3', 'gap30', 'spread3_share')}
{step('hs_2', 'gap20', 'spread2_share')}
{step('hs_1', 'gap10', 'spread1_share')}
{step('hs_0', 'gap00', 'spread0_share')}
- {d('hs_m1').capitalize()} (the variable rate starts above the fixed rate): {d('spreadm1_share')} of all starts cost more in total interest; {d('gapm10_early')} of starts from {d('period_early')}, {d('gapm10_late')} of starts from {d('period_late')}; worst stretch {d('gapm10_worst')} ({d('gap_worst_start_all')}).
- At every head start tested, the worst stretch began in {d('gap_worst_start_all')}, and some of the starts from {d('period_early')} still cost more (at least {d('min_gap_early')}).

How the replay was built (method card)
- A variable rate is a lender's index plus a fixed margin. Here the {d('tbill_3month')} Treasury bill rate stands in for the lender's index ({d('index_today')} in August 2026), with a margin of {d('margin')}, set so that Leah's variable rate starts at {d('var_start')}.
- Each replay moves her rate up and down exactly as much as the Treasury bill rate moved in that stretch of history; the index is never taken below zero.
- {d('n_starts')} start months: the first replay starts in {d('first_start')}, then one every month to {d('last_start')}; each runs {d('term')} against {d('fixed_rate')} fixed.
- Neighbouring stretches overlap, so the {d('n_starts')} starts are not independent tests.
- No grace period, no fees, no rate cap: repayment starts at once, with no deferment and no discounts. A real loan's cap, if low enough, would have made the worst case smaller.
- Every dollar amount is in dollars of the day (nominal, not adjusted for inflation).

What this is and is not
- History, not a forecast. Which kind of history comes next is something no replay can show.
- US only: US Treasury bill rates and US federal student loan rules.
- Not advice. The line does not say which offer is better; it shows what each head start meant in each kind of history. A real offer has its own two rates, its own head start, and what this replay leaves out: the lender's real index, a rate cap, a grace period, fees, and the borrower's own budget.
- ILLUSTRATIVE: Leah, her two rates and her loan are illustrative, not a real lender's offer. The Treasury bill history is real data.

Federal loan context
- From {d('ctx_plus_end')}, new graduate students can no longer borrow federal Grad PLUS loans. Students already enrolled and borrowing before July 2026 keep Grad PLUS for up to 3 more academic years, or for the time left in their program if that is shorter.
- New students still have the Direct Unsubsidized loan: up to {d('ctx_unsub_annual')} and {d('ctx_unsub_aggregate')}, with higher limits in professional programs such as medicine or law.

Sources
- 3-Month Treasury Bill Secondary Market Rate, monthly (TB3MS), Board of Governors of the Federal Reserve System (H.15), via FRED, Federal Reserve Bank of St. Louis: https://fred.stlouisfed.org/series/TB3MS · cross-checked against the daily series DTB3: https://fred.stlouisfed.org/series/DTB3
- Grad PLUS end and the exception for enrolled students: Code of Federal Regulations, Direct Loan Program, eCFR: https://www.ecfr.gov/current/title-34/subtitle-B/chapter-VI/part-685/subpart-B/section-685.200
- Direct Unsubsidized limits: Federal Register: https://www.federalregister.gov/documents/2026/01/30/2026-01912/reimagining-and-improving-student-education · Federal Student Aid, loan limits FAQ: https://fsapartners.ed.gov/sites/default/files/2026-05/FrequentlyAskedQuestionsLoanLimits.pdf

Narration: synthetic voice (ElevenLabs). Music and data sounds are generated in code for this video.
"""
    os.makedirs(P('out', 'package'), exist_ok=True)
    open(P('out', 'package', 'description.md'), 'w', encoding='utf-8').write(text)
    # ---- self-checks: every number of the body has a claim (chapters: times; URLs: addresses; "10-year": term; "August 2026": index_today date)
    body = re.sub(r'https?://\S+', ' ', text.split('-->', 1)[1])
    body = '\n'.join(l for l in body.split('\n') if not re.match(r'^\s*\d+:\d{2}\s', l))
    alias = {'num:10': 'term', 'num:2026': 'index_today (last observation 2026-08; formula) / ctx_plus_end', 'num:3': 'ctx_plus_exception ("up to 3 more years") / tbill_3month'}
    cmap, orphans = [], []
    disp = [(k, [x for x, _ in C.numbers_in_text(str(c['display']))]) for k, c in cl.items()]
    for cn, span in C.numbers_in_text(body):
        hit = [k for k, ws in disp if any(C.canon_matches(cn, [w]) and cn.split(':')[0] == w.split(':')[0] for w in ws)] or \
              [k for k, ws in disp if C.canon_matches(cn, ws)]
        if not hit and cn not in alias:
            orphans.append(span)
        cmap.append({'number': span, 'canon': cn, 'claims': hit[:6] or [alias.get(cn)]})
    assert not orphans, orphans
    low = text.lower()
    for need in ('history, not a forecast', 'us only', 'illustrative', 'nominal'):
        assert need in low, need
    for bad in (r"\byou (should|must|need to|ought to|have to)\b", r'^\s*-?\s*(consider|avoid|choose|pick|take|lock)\b', r'\byour loan will\b',
                r'\b(will|is going to)\b[^.]{0,40}\b(rise|fall|grow|drop)\b', r'\b(we|i) (recommend|suggest|advise|expect|predict|forecast)\b'):
        assert not re.search(bad, low, re.M), bad
    dump({'about': 'every number of out/package/description.md (outside chapter times and URLs) -> the claims whose display carries it (generated)',
          'numbers': cmap}, 'out', 'package', 'description-claims.json')


if __name__ == '__main__':
    main()
