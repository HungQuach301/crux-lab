"""Episode 1 contract (checks/CONTRACT.md, section "Hợp đồng tập", lock K2 f9e24c91).

    python3 episodes/ep001/build.py            # first: out/model.json, out/claims.json
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
            'out/package/thumb-2.json', 'out/package/thumb-3.json', 'preprod/storyboard.*', 'preprod/color-script.*']
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
                      'wordsFrom': 'story/script.md v2 (out/script.json)'} for n in names}
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
        'lock': 'f9e24c91a464b1948f6eabb08d6da05d5867f78d2fe7ce1f818ec92009f0dcdd (K2)',
        'question': 'At what rate spread does a refinance pay back its closing costs?',
        'thesis': 'most calculators divide the bill by the monthly saving; counting what is still owed on each loan, break-even comes later for a loan that is already some years old',
        'targetDurationSec': [600, 660],
        'characters': characters,
        'scenarios': {'hold36': {'what': 'sell or refinance again after 3 years (36 months): the payback target of the question', 'words': ['three years', '36 months'],
                                 'wordsFrom': 'story/script.md v2: "within three years", "after three years"'},
                      'hold84': {'what': 'keep the loan 7 years (84 months)', 'words': ['seven years', '84 months'],
                                 'wordsFrom': 'story/script.md v2: "stays seven years" (S31)'}},
        'claims': {'file': 'out/claims.json', 'count': len(claims),
                   'core': [c['claimId'] for c in claims if c.get('core')],
                   'decisive': [c['claimId'] for c in claims if c.get('decisive')],
                   'illustrative': [c['claimId'] for c in claims if c.get('illustrative')]},
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
        'coverage': [{'attribute': 'case', 'act': 'method', 'values': [e['peak'] for e in hist],
                      'what': f'every drop episode of the history simulation ({len(hist)}, keyed by peak month), including those where the rate fell another point before break-even',
                      'where': 'S33 history card (act method), script v2; page objects carry case = peak month'},
                     {'attribute': 'case', 'act': 'act3', 'values': names,
                      'what': 'the three characters\' answers (cut for a 36-month break-even)', 'where': 'S29, the three markers on the ruler (act3), script v2; page objects carry case = character key'}],
        'sonification': {'stem': 'sonify', 'bandsHz': [[60, 270], [4500, 7000]],
                         'from': 'preprod/cue-sheet.md, palette S2 (owner pick 2026-09-28): low pulse MIDI 36-60 (65-262 Hz) + filtered tick 4.5-7 kHz',
                         'todo': 'T1 measures that these bands hold >= 50% of the sonify stem energy once the stem is rendered'},
        'artefacts': {
            'M1': ['out/claims.json', 'out/model.json', 'out/script-draft.json', 'script/script.md', 'preprod/shotlist.json', 'preprod/storyboard.md',
                   'preprod/color-script.md', 'preprod/cue-sheet.md', 'preprod/tension-map.json', 'preprod/tension-map.png', 'edit/cues.json',
                   'contract.json', 'design/tokens.json', 'data/sources.json'],
            'M2': ['out/script.json', 'out/timeline.json', 'out/voice/takes.json', 'out/page.json', 'out/camera.json', 'out/cues.json', 'out/tempo-map.json',
                   'out/transitions.json', 'out/sonify-events.json', 'out/sfx-events.json'],
            'M3': RELEASE + EXTRA_M3},
    }
    tp = os.path.join(HERE, 'preprod', 'timeline-plan.json')
    if os.path.exists(tp):
        mk = json.load(open(tp))['marks']
        contract['timeline'] = {'source': 'preprod/timeline-plan.json (animatic, V8 takes); the render re-times at M2', 'coldOpenEnd': mk['coldOpenEnd'],
                                'rehook': mk['rehook'], 'acts': mk['acts'], 'adBreaks': mk['adBreaks'], 'total': mk['total'],
                                'amendments': ['E1-A1: cold open ~20 s accepted for Episode 1 (S15 cold open <= 15 s fails by approval)']}
    contract['todo'] = [
        'characters.*.shape / side and coverage[] `case` on page objects: must match the rendered page (V04, V09, S06 need the page)',
        'sonification.bandsHz: from the cue sheet; T1 checks the >= 50% energy share only on the rendered sonify stem',
        'artefacts.M3: every release file is declared; video, stems, page and package files do not exist yet (F11 fails "not delivered" until M3)',
        'timeline: planned from the animatic; out/timeline.json and out/script.json are re-timed by the render at M2']
    json.dump(contract, open(os.path.join(HERE, 'contract.json'), 'w'), indent=1, ensure_ascii=False)
    print('contract.json:', len(claims), 'claims,', len(mapped), 'mapped to model quantities,', len(contract['artefacts']['M3']), 'M3 artefacts')


if __name__ == '__main__':
    main()
