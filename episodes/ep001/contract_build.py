"""Episode 1 contract (checks/CONTRACT.md, section "Hợp đồng tập", lock K3.1 81cf3997; C5: script v3.2, final timing).

    python3 episodes/ep001/preprod/script_from_v32.py   # out/script.json, out/script-draft.json (v3.2)
    python3 episodes/ep001/build.py            # out/model.json, out/claims.json
    python3 episodes/ep001/preprod/dossier_c5.py        # out/timeline.json (acts) and the rest of the dossier
    python3 episodes/ep001/contract_build.py   # writes episodes/ep001/contract.json only

Every field the K2 rules read is filled from the episode's own files (out/model.json, out/claims.json, design/tokens.json,
preprod/cue-sheet.md, data/sources.json), never typed by hand. Fields whose final value depends on the script, the render or the voice
(not written yet) carry the best value known now and are listed in `todo`; the checker ignores `todo` and the per-entry `todo` notes.
design/tokens.json is NOT written here any more (it is edited in design/; an older version of this script overwrote it).
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
J = lambda *p: json.load(open(os.path.join(HERE, *p)))

# checks/CONTRACT.md, first table: the release files (F11 needs each of them declared in artefacts.M3)
RELEASE = ['out/video.mp4', 'out/captions.srt', 'out/package/description.md', 'out/timeline.json', 'out/script.json', 'out/claims.json',
           'out/audio/stems/voice.*', 'out/audio/stems/music.*', 'out/audio/stems/sfx.*', 'out/audio/stems/whoosh.*', 'out/audio/stems/room.*',
           'out/audio/stems/sonify.*', 'out/voice/takes.json', 'out/camera.json', 'out/sfx-events.json', 'out/sonify-events.json', 'out/tempo-map.json',
           'out/transitions.json', 'out/cues.json', 'out/tension-map.json', 'out/tension-map.png', 'out/adbreaks.json', 'preprod/shotlist.json',
           'design/tokens.json', 'out/package/thumb-1.png', 'out/package/thumb-2.png', 'out/package/thumb-3.png', 'out/page.json']
# model files and the data the rules re-compute from (S01, S03, S04), plus the rest of the CONTRACT.md table the builder delivers
EXTRA_M3 = ['out/model.json', 'data/sources.json', 'data/normalized/mortgage30_weekly.csv', 'data/normalized/crosscheck_weekly.csv',
            'data/normalized/hmda_refi_costs.csv', 'data/normalized/hmda_refi31_conforming.csv', 'contract.json', 'out/package/thumb-1.json',
            'out/package/thumb-2.json', 'out/package/thumb-3.json', 'preprod/storyboard.*', 'preprod/color-script.*',
            'out/rights.json', 'out/visual-assets.json', 'out/voice/takes.json']
LOCK = '81cf3997737724314346c49254c26c2b1018bc545d95fb3d3f5edf8106f766f8 (K3.1)'
# model assumptions that must be on screen (S02, K3): in the method act (S19, or a method card after S20) AND elsewhere. Case-insensitive regex.
# Where each is on screen now (animatic/src): offer-average S06 source line; fees-in-cash S07 label, S11 source, S18 footnote;
# payback-3y and oct2023-rate and median-bill S18 footnote (median bill also S02 source); new-loan-30y S10 head "A mortgage is a 30-year clock".
ASSUMPTIONS = [
    {'id': 'offer-average', 'pattern': r'matches the national average|national average rate', 'what': 'the offered rate = the national weekly average (MORTGAGE30US) of the date anchor'},
    {'id': 'fees-in-cash', 'pattern': r'paid in cash', 'what': 'closing costs are paid in cash, not added to the loan'},
    {'id': 'payback-3y', 'pattern': r'within (3|three) years|(3|three)-year (payback|stay|test)', 'what': 'worth it = fees paid back within 3 years (analyst choice)'},
    {'id': 'oct2023-rate', 'pattern': r'oct(ober|\.)? 2023 (average )?rate', 'what': 'the old loan was taken out at the October 2023 average rate'},
    {'id': 'median-bill', 'pattern': r'median (\d{4} )?(refinance )?bills?', 'what': 'the bill is the HMDA 2025 median for the loan size'},
    {'id': 'new-loan-30y', 'pattern': r'30-year (term|clock|loan)', 'what': 'the new loan is a fresh 30-year fixed loan'}]
FIELDS = {'loan': 'loan', 'cost': 'cost', 'sav': 'monthlySavings', 'be_simple': 'simple', 'be_bal': 'withBalance', 'net36': 'net36', 'net84': 'net84', 'cut36': 'cut36'}


def main():
    model = J('out', 'model.json')
    claims = J('out', 'claims.json')['claims']
    by = {c['claimId']: c for c in claims}
    tok = J('design', 'tokens.json')
    sc, ch = model['scenario'], model['characters']
    names = list(ch)  # median, small, large: the model's character keys = the page's `char` = claims' `character`
    # names the approved script (story/script.md v2) gives the characters: Nora = median, Walt = small, Anjali = large
    words = {'median': ['Nora'], 'small': ['Walt'], 'large': ['Anjali']}
    side = {'small': 'left', 'median': 'centre', 'large': 'right'}
    what = {'median': 'HMDA 2025 median rate-and-term refinance (all sizes)', 'small': 'HMDA 2025 median, loans under $150,000',
            'large': 'HMDA 2025 median, conforming (flag C) loans of $600,000 to under $720,000'}
    characters = {n: {'color': n, 'shape': tok['shapes'][n], 'side': side[n], 'illustrative': True, 'words': words[n],
                      'what': f"ILLUSTRATIVE: borrowed {model['scenario']['borrowed']} at that month's mean rate ({sc['oldRate']}%), "
                              f"{sc['paymentsMade']} payments made; loan ${ch[n]['loan']:,.0f}, bill ${ch[n]['cost']:,.2f} = {what[n]}",
                      'wordsFrom': 'story/script-v3.2.md (out/script.json)'} for n in names}
    mapped = {}
    for n in names:
        for pre, f in FIELDS.items():
            cid = f'{pre}_{n}'
            if cid in by:
                mapped[cid] = f'{n}.{f}'
    for c in claims:  # spoken forms of a mapped claim carry the parent's value
        if c.get('spokenForm') and c.get('parent') in mapped:
            mapped[c['claimId']] = mapped[c['parent']]
    hist = model['history']
    contract = {
        'episode': 'ep001',
        'lock': LOCK,
        'question': 'At what rate spread does a refinance pay back its closing costs?',
        'thesis': 'most calculators divide the bill by the monthly saving; counting what is still owed on each loan, break-even comes later for a loan that is already some years old',
        'targetDurationSec': [480, 900],
        'characters': characters,
        'scenarios': {'hold36': {'what': 'sell or refinance again after 3 years (36 months): the payback target of the question', 'words': ['three years', 'three-year', '36 months'],
                                 'wordsFrom': 'story/script-v3.2.md: "a stay of three years" (S08), "after three years" (S16, S17, S20), "the three-year test" (S13)'},
                      'hold84': {'what': 'keep the loan 7 years (84 months)', 'words': ['stays seven', 'seven years', '84 months'],
                                 'wordsFrom': 'story/script-v3.2.md: "if she stays seven" (S20)'}},
        'claims': {'file': 'out/claims.json', 'count': len(claims),
                   'core': [c['claimId'] for c in claims if c.get('core')],
                   'decisive': [c['claimId'] for c in claims if c.get('decisive')],
                   'illustrative': [c['claimId'] for c in claims if c.get('illustrative')],
                   'assumptions': ASSUMPTIONS},
        'model': {
            'kind': 'refinance-breakeven',
            'output': 'out/model.json',
            'code': 'model/refi.py', 'tests': 'model/test_refi.py',
            'params': {
                'scenario': {'oldRate': sc['oldRate'], 'paymentsMade': sc['paymentsMade'], 'todayRate': sc['todayRate'], 'termMonths': 360,
                             'netHorizons': [36, 84], 'byCutOf': 'median'},
                'characters': {n: {'loan': ch[n]['loan'], 'cost': ch[n]['cost']} for n in names},
                'history': {'series': {'file': 'data/normalized/mortgage30_weekly.csv', 'dateColumn': 'date', 'rateColumn': 'rate'},
                            'swingPoints': 1.0, 'spreads': sorted({c['spread'] for e in hist for c in e['cases']}), 'loan': 300000.0, 'termMonths': 360,
                            'costShares': {'file': 'data/normalized/hmda_refi_costs.csv', 'filter': {'purpose': 'refinance (31)', 'loanSize': 'all sizes'},
                                           'yearColumn': 'year', 'shareColumn': 'cost_p50_pct'}},
                'notModel': ['dateAnchor', 'largeBand', 'conformingLimits'],
                'paramsFrom': {'oldRate': 'mean of the weekly MORTGAGE30US values dated October 2023 (claim r_old)', 'todayRate': f"MORTGAGE30US, week ending {sc['todayWeek']} (claim r_today)",
                               'paymentsMade': 'months from 2023-10 to the date anchor month (claim k35)', 'characters': 'HMDA 2025 medians (claims loan_*, cost_*)',
                               'notModel': 'metadata copied into model.json, not computed: date anchor text, the large band label, FHFA limits (data/cll.json)'}},
            'claims': mapped,
            'recompute': ['payment = P*r/(1-(1+r)^-n), r = annual%/1200; old loan P0 at r_old over 360 with k payments made; balance B = balance after k; new loan B at r_new over 360',
                          'MAIN break-even (counting what is still owed): first month m with (payment_old - payment_new) x m + (balance_old(k+m) - balance_new(m)) >= C',
                          'simple break-even (shown as the contrast): ceil(C / (payment_old - payment_new))',
                          'history: monthly means of MORTGAGE30US; drop episodes = zig-zag swings >= 1.00 point; refinance in the first month >= spread under the peak; cost = HMDA median share of that year (fixed median share before 2018, ILLUSTRATIVE)']},
        'data': {
            'sources': 'data/sources.json',
            'hosts': {'primary': ['fred.stlouisfed.org'], 'crosscheck': ['fred.stlouisfed.org']},
            'crosscheck': [{'series': 'mortgage30', 'tolerance': 0.5, 'used': 'crosscheck',
                            'primary': {'file': 'data/normalized/mortgage30_weekly.csv', 'key': 'date', 'column': 'rate'},
                            'crosscheck': {'file': 'data/normalized/crosscheck_weekly.csv', 'key': 'week', 'column': 'obmmic30yf_weekmean'},
                            'what': 'Freddie Mac PMMS weekly (MORTGAGE30US) vs the mean of the Optimal Blue daily rates (OBMMIC30YF) of the 7 days ending that Thursday, every week since 2017-01-06'}],
            'fetch': 'python3 episodes/ep001/data/fetch.py --verify (the FRED files are not in the public repo: amendments.md E1-A2; run this before the checks)',
            'other': {'hmda': 'data/hmda-sources.json + data/normalized/hmda_refi_costs.csv, hmda_refi31_conforming.csv (HMDA 2018-2025, ffiec.cfpb.gov, public domain, streamed; not in data/sources.json because S03 reads FRED-style raw files)',
                      'fhfa': 'data/cll.json (2026 limit owner-verified 2026-09-29)'}},
        'coverage': [{'attribute': 'case', 'act': 'act3', 'values': names,
                      'what': 'the three characters\' answers (rate cut for a 36-month break-even), all three shown: the promise of S02 answered for each loan size',
                      'where': 'S18 three-mark ruler (act3), script v3.2; page objects of each column/marker carry case = character key (median, small, large)'}],
        'sonification': {'stem': 'sonify', 'bandsHz': [[60, 270], [4500, 7000]],
                         'from': 'preprod/cue-sheet.md, palette S2 (owner pick 2026-09-28): low pulse MIDI 36-60 (65-262 Hz) + filtered tick 4.5-7 kHz; same bands as SON_BANDS of the C5 mix (work/audio/src/mix.py)',
                         'todo': 'T1 measures that these bands hold >= 50% of the sonify stem energy once the stem is rendered'},
        'artefacts': {
            'M1': ['out/claims.json', 'out/model.json', 'out/script-draft.json', 'script/script.md', 'preprod/shotlist.json', 'preprod/storyboard.md',
                   'preprod/color-script.md', 'preprod/cue-sheet.md', 'preprod/tension-map.json', 'preprod/tension-map.png', 'edit/cues.json',
                   'contract.json', 'design/tokens.json', 'data/sources.json'],
            'M2': ['out/script.json', 'out/timeline.json', 'out/voice/takes.json', 'out/page.json', 'out/camera.json', 'out/cues.json', 'out/tempo-map.json',
                   'out/transitions.json', 'out/sonify-events.json', 'out/sfx-events.json'],
            'M3': RELEASE + EXTRA_M3},
    }
    tl = os.path.join(HERE, 'out', 'timeline.json')
    if os.path.exists(tl):
        t = json.load(open(tl))
        ab = os.path.join(HERE, 'out', 'adbreaks.json')
        contract['timeline'] = {'source': 'out/timeline.json (final sentence times: animatic/timing.json, narration v3.2)', 'total': t['total'],
                                'acts': {a['id']: [a['start'], a['end']] for a in t['acts']},
                                'climax': {a['id']: a['climax'] for a in t['acts'] if a.get('climax') is not None},
                                'adBreaks': json.load(open(ab))['breaks'] if os.path.exists(ab) else None,
                                'note': 'cold open S01-S02 = 55.7 s (E1-A1 accepted a long cold open; S15 is REFERENCE); no ident rendered; method = S19 unless a method card is added after S20'}
    contract['todo'] = [
        'rights: out/rights.json voice entry waits for the verbatim ElevenLabs quote (owner): F12 fails until then',
        'claims.assumptions: every pattern must also be on screen in the method act (S19 or a method card), see out/timeline.json acts',
        'coverage: the S18 columns/markers must carry case = median/small/large on the page (window.CHECKS objects)',
        'sonification.bandsHz: T1 checks the >= 50% energy share on the rendered sonify stem']
    json.dump(contract, open(os.path.join(HERE, 'contract.json'), 'w'), indent=1, ensure_ascii=False)
    print('contract.json:', len(claims), 'claims,', len(mapped), 'mapped to model quantities,', len(contract['artefacts']['M3']), 'M3 artefacts')


if __name__ == '__main__':
    main()
