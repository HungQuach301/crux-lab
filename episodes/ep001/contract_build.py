"""Episode 1 contract (checks/CONTRACT.md): characters, colours, claims, model, artefacts to deliver at M2/M3.

    python3 episodes/ep001/contract_build.py   # writes episodes/ep001/contract.json and design/tokens.json
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.join(HERE, '..', '..')
T = json.load(open(os.path.join(REPO, 'genre-spec', 'channel', 'visual-tokens.json')))['colors']
lc = lambda k: T[k].lower()


def main():
    colors = {'bg': lc('bg'), 'surface': lc('surface'), 'text': lc('ink'), 'text-dim': lc('ink-muted'), 'muted': lc('ink-muted'), 'grid': lc('grid'),
              'accent': lc('accent'), 'warn': lc('warn'), 'positive': lc('positive'), 'negative': lc('negative'),
              'csmall': lc('warn'), 'clarge': lc('accent'), 'cmedian': lc('ink'), 'old-payment': lc('ink-muted'), 'new-payment': lc('accent'),
              'bill': lc('negative'), 'saved': lc('positive'), 'badge-bg': lc('warn'), 'badge-text': lc('bg')}
    os.makedirs(os.path.join(HERE, 'design'), exist_ok=True)
    json.dump({'colors': colors, 'series': {'rate': lc('accent'), 'small': lc('warn'), 'large': lc('accent'), 'median': lc('ink')},
               'seriesOf': {'rate': lc('accent'), 'small': lc('warn'), 'large': lc('accent'), 'median': lc('ink')},
               'source': 'genre-spec/channel/visual-tokens.json: every value is a channel token (aliases only)'},
              open(os.path.join(HERE, 'design', 'tokens.json'), 'w'), indent=1)
    claims = json.load(open(os.path.join(HERE, 'out', 'claims.json')))['claims']
    contract = {
        'episode': 'ep001',
        'question': 'At what rate spread does a refinance pay back its closing costs?',
        'thesis': 'most calculators divide the bill by the monthly saving; counting what is still owed on each loan, break-even comes later for a loan that is already some years old (Maya: 24 -> 30 months)',
        'line': 'content line 1 (borrowing and debt), housing decision',
        'targetDurationSec': [600, 660],
        'persona': {'we': 'the analysts only', 'advice': 'none', 'scope': 'US only', 'history': 'history, not a forecast (act 1, once each)'},
        'characters': {
            'maya': {'what': 'ILLUSTRATIVE: borrowed the HMDA 2025 median rate-and-term refinance amount ($375,000) in October 2023 at that month\'s average rate; bill = median ($5,124)', 'color': 'cmedian', 'shape': 'solid', 'side': 'centre'},
            'dan': {'what': 'ILLUSTRATIVE: same month and rate; median loan and bill of loans under $150,000', 'color': 'csmall', 'shape': 'solid', 'side': 'left'},
            'priya': {'what': 'ILLUSTRATIVE: same month and rate; median loan and bill of loans of $750,000 and more', 'color': 'clarge', 'shape': 'dashed', 'side': 'right'},
            'note': 'the locked rules V04/V09 look for characters "1966"/"mirror" (test D); this episode tags its character shapes with char "maya"/"dan"/"priya". Session K to confirm how V04/V09 read a new episode.'},
        'colors': 'design/tokens.json (all channel tokens)',
        'claims': {'file': 'out/claims.json', 'count': len(claims), 'core': [c['claimId'] for c in claims if c.get('core')],
                   'decisive': [c['claimId'] for c in claims if c.get('decisive')], 'illustrative': [c['claimId'] for c in claims if c['illustrative']],
                   'rule': 'every number in narration and on screen is a claim; narration numbers are filled from claims by build.py (script/script.tpl.md)'},
        'model': {'code': 'model/refi.py', 'tests': 'model/test_refi.py', 'output': 'out/model.json',
                  'recompute': ['payment = P*r/(1-(1+r)^-n), r = annual%/1200; old loan P0 at r_old over 360 with k payments made; balance B = balance after k; new loan B at r_new over 360',
                                'MAIN break-even (counting what is still owed): first month m with (payment_old - payment_new) x m + (balance_old(k+m) - balance_new(m)) >= C',
                                'simple break-even (shown as the contrast): ceil(C / (payment_old - payment_new))',
                                'history: monthly means of MORTGAGE30US; drop episodes = zig-zag swings >= 1.00 point; refinance in the first month >= spread under the peak; cost = HMDA median share of that year (fixed median share before 2018, ILLUSTRATIVE)'],
                  'note': 'S01/S05/S06 of the locked checks re-compute test D\'s retirement model; this episode needs its own independent re-computation (K session).'},
        'data': {'rates': 'data/sources.json (FRED MORTGAGE30US primary, OBMMIC30YF cross-check, tolerance 0.5 pp)',
                 'costs': 'data/hmda-sources.json + data/normalized/hmda_refi_costs.csv (HMDA 2018-2025, streamed, raw not stored)',
                 'terms': {'fred': 'display with attribution; the data file is NOT re-published; the description links to the FRED/Freddie Mac source pages (owner decision 2026-09-28)',
                           'hmda': 'OPEN: no terms-of-use sentence could be quoted from a reachable page (consumerfinance.gov blocked); see data/hmda-sources.json'}},
        'artefacts': {
            'M1 (this milestone)': ['out/claims.json', 'out/model.json', 'script/script.md', 'out/script-draft.json', 'out/voice/ (table read takes)', 'review-m1/',
                                    'preprod/shotlist.json', 'preprod/storyboard.md + storyboard/*.png', 'preprod/color-script.md', 'preprod/cue-sheet.md', 'edit/cues.json',
                                    'preprod/tension-map.json + .png (planned)', 'contract.json', 'design/tokens.json'],
            'M2/M3 (per checks/CONTRACT.md)': ['out/video.mp4', 'out/captions.srt', 'out/package/description.md', 'out/timeline.json', 'out/script.json', 'out/claims.json',
                                               'out/audio/stems/{voice,music,sfx,whoosh,room,sonify}.flac', 'out/voice/takes.json', 'out/camera.json', 'out/sfx-events.json',
                                               'out/sonify-events.json', 'out/tempo-map.json', 'out/transitions.json', 'out/cues.json', 'out/tension-map.json + .png', 'out/adbreaks.json',
                                               'out/model.json', 'data/sources.json', 'data/normalized/*', 'preprod/shotlist.json', 'preprod/storyboard.*', 'preprod/color-script.*',
                                               'design/tokens.json', 'out/package/thumb-{1,2,3}.png + .json', 'out/page.json'],
            'contract gaps to settle with the K session': ['S03/S04 expect a Damodaran primary + FRED cross-check and data/normalized/annual.csv (test D); this episode: FRED primary + Optimal Blue cross-check + HMDA',
                                                           'S01/S05/S06/V04/V09 are tied to test D\'s model and characters']},
    }
    json.dump(contract, open(os.path.join(HERE, 'contract.json'), 'w'), indent=1, ensure_ascii=False)
    print('contract.json:', len(claims), 'claims')


if __name__ == '__main__':
    main()
