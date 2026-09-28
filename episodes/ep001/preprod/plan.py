"""Episode 1 pre-production plan: one row per scene (= one narration sentence), the single source of the shot list,
storyboard, colour script, cue sheet and planned tension map.

    python3 episodes/ep001/preprod/plan.py      # needs out/script-draft.json (+ out/voice/takes.json for real timing)

Row: scene -> (layout family/variant, shot size, camera move, reason for the move, what the picture shows,
data-sound elements that change in the scene: bar / line / dot / counter).
Characters (ILLUSTRATIVE, numbers from the data): DAN (loan under $150k) = warn amber, solid, left; PRIYA ($750k+) =
accent blue, dashed, right; MAYA (the median loan) = ink white, centre. Old loan = ink-muted, new loan = accent.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.join(HERE, '..')

S = {
    # cold open (G-007): one person, one moment. Picture before words (1.2 s): Maya's front door, a mortgage statement
    'co-maya': ('person/maya', 'close', 'push-in 1.2 s', 'come close to one household before any chart', 'Maya\'s card, shown before the first word: a house icon, loan $375,000; rate 7.62% lands on the word (ILLUSTRATIVE badge); October 2023 is said in act 1', ['counter']),
    'co-today': ('line/today', 'medium', 'track right 1.4 s', 'from her month to this week along the rate line', 'rate line Oct 2023 -> this week; today\'s dot 7.03%', ['line', 'dot']),
    'co-cost': ('stack/bill', 'close', 'none', 'the bill lands beside her card', 'closing-cost bill $5,124 drops next to Maya\'s card', ['bar']),
    'co-question': ('title/question', 'wide', 'pull-out 1.4 s', 'reveal the empty month counter under the question', 'question "When does that money come back?"; month counter at 0', ['counter']),
    'ident': ('ident/logo', 'wide', 'none', 'no move on the 3 s ident', 'channel ident, 3 s, no narration', []),
    'a1-lab': ('title/lab', 'wide', 'drift 8 px/s', 'slow drift keeps the title card alive', 'lab card: data -> model -> number', []),
    'a1-scope': ('title/scope', 'medium', 'none', 'hold on the two scope badges', '"US only" and "history, not a forecast" badges', []),
    'a1-rehook': ('ruler/rehook', 'medium', 'track right 1.5 s', 'the marker sweeps the ruler; the answer is not placed yet', 'ONE object: a ruler of rate cut (0 to 2 points) with Maya\'s card at its left end; a marker sweeps it and one "?" hangs over the 36-month line (ILLUSTRATIVE badge); 13 ticks under it = every drop since 1971', ['dot']),
    'a1-maya': ('person/maya2', 'medium', 'none', 'Maya\'s card again, now with the month on the rate line', 'Maya\'s card beside the October 2023 peak of the rate line', ['dot']),
    'a1-you': ('person/you', 'medium', 'push-in 1.2 s', 'turn the question to the viewer', 'a blank statement with a rate field "7.__%" next to Maya\'s', []),
    'a1-q': ('title/act1', 'wide', 'none', 'hold on the act question', 'act 1 question: is Maya\'s bill unusual?', []),
    'a1-median': ('hist/median', 'medium', 'push-in 1.3 s', 'land on the median line', 'the middle half of 2025 bills; the median line reaches Maya\'s bill', ['bar', 'dot']),
    'a1-hmda': ('ledger/hmda', 'medium', 'none', 'hold on the disclosure record', 'one loan record, field "total loan costs" highlighted', []),
    'a1-count': ('ledger/count', 'medium', 'none', 'hold while the count rolls', 'counter rolls to 488,241', ['counter']),
    'a1-spread': ('hist/iqr', 'medium', 'none', 'hold: the band opens from the median', 'IQR band $3,443-$8,270 opens', ['bar']),
    'a1-terms': ('stack/parts', 'close', 'tilt down 1.2 s', 'read the bill top to bottom', 'the bill splits into labelled layers', ['bar']),
    'a1-turn': ('bands/intro', 'wide', 'push-in 1.2 s', 'move into the loan-size bands', 'three cards: Dan (left, amber), Maya (centre), Priya (right, blue)', ['bar']),
    'a1-dan': ('person/dan', 'medium', 'track left 1.3 s', 'go to Dan', 'Dan\'s card: $115,000, same month, same rate (ILLUSTRATIVE)', []),
    'a1-dan2': ('bands/small', 'medium', 'none', 'hold on his band', 'band "under $150,000": 3.4% of the loan', ['bar']),
    'a1-dan3': ('stack/dan', 'close', 'push-in 1.2 s', 'his bill against his loan', 'Dan\'s bill $3,667 as a slice of his loan column', ['bar']),
    'a1-priya': ('person/priya', 'medium', 'track right 1.6 s', 'cross to Priya', 'Priya\'s card: $1,005,000 (ILLUSTRATIVE)', []),
    'a1-priya2': ('bands/large', 'medium', 'none', 'hold on her band', 'band "$750,000 and more": 0.5%', ['bar']),
    'a1-priya3': ('stack/priya', 'close', 'pull-out 1.3 s', 'her bill beside Maya\'s', 'Priya\'s $5,034 next to Maya\'s $5,124, on a loan column three times as tall', ['bar']),
    'a1-save': ('bars/payments', 'medium', 'none', 'hold: the new payment bar drops', 'Maya\'s old vs new monthly payment; the new bar drops $221', ['bar']),
    'a1-rule': ('title/formula', 'medium', 'push-in 1.2 s', 'land on the division', '$5,124 / $221 = 24 months (what most calculators give)', ['counter']),
    'a1-payoff': ('stack/fill', 'medium', 'none', 'the bill fills, then a doubt mark', 'monthly savings fill the bill in 24 months; a "?" appears', ['bar', 'counter']),
    'a2-q': ('title/act2', 'wide', 'none', 'hold on the act question', 'act 2 question: what does the division leave out?', []),
    'a2-old': ('person/maya35', 'medium', 'none', 'hold: her payment calendar', 'Maya\'s calendar with 35 payments ticked', ['counter']),
    'a2-reset': ('bars/timeline', 'wide', 'track right 1.5 s', 'follow the new schedule to its end, 30 years out', 'two payment timelines: the old one ends in 2053, the new one 30 years from today', ['line']),
    'a2-why': ('bars/split', 'medium', 'none', 'hold on the interest/principal split', 'one payment split: interest vs principal, old loan month 36 vs new loan month 1', ['bar']),
    'a2-owe': ('balance/two', 'medium', 'push-in 1.2 s', 'the two balance lines start to draw', 'balance still owed: old loan (grey) and new loan (blue), month by month', ['line']),
    'a2-gap': ('balance/gap', 'close', 'push-in 1.3 s', 'go to the gap at month 24', 'the gap between the two lines at month 24: $1,133', ['dot']),
    'a2-real': ('balance/real', 'medium', 'track right 1.2 s', 'move from 24 to 30 on the month axis', 'savings + balance gap crosses the bill at month 30 (not 24)', ['line', 'dot']),
    'a2-thesis': ('title/thesis', 'wide', 'none', 'hold on the two answers', '"most calculators: 24" / "counting what is owed: 30"', []),
    'a2-small': ('curve/intro', 'medium', 'none', 'the two curves appear', 'break-even months against the cut, two curves: simple (dashed grey) and balance (solid)', ['line']),
    'a2-s025': ('curve/025', 'medium', 'track left 1.2 s', 'move to the smallest cut', 'at 0.25 points: simple 38 months', ['dot']),
    'a2-s025b': ('curve/never', 'close', 'tilt up 1.3 s', 'the balance curve leaves the chart', 'the balance curve goes off the top: never', ['line']),
    'a2-cliff': ('curve/cliff', 'medium', 'pull-out 1.2 s', 'show the steep part below 0.5', 'the steep region below 0.5 points shaded', ['line']),
    'a2-s10': ('curve/10', 'medium', 'track right 1.3 s', 'move along to 1 point', 'the two curves close in at 1 point', []),
    'a2-s10b': ('curve/10m', 'medium', 'none', 'hold on the two values', '16 vs 18 months', ['dot']),
    'a2-dan': ('person/dan2', 'medium', 'track left 1.3 s', 'back to Dan', 'Dan\'s payment bars: -$68', ['bar']),
    'a2-dan2': ('balance/dan', 'medium', 'none', 'his two answers', 'Dan: 55 (division) vs 75 (balance) months', ['dot']),
    'a2-dan3': ('ledger/dan3', 'close', 'push-in 1.2 s', 'Dan sells after 3 years', 'Dan\'s position after 3 years: -$1,777 (red)', ['counter']),
    'a2-dan4': ('ledger/dan7', 'close', 'none', 'hold', 'after 7 years: +$386', ['counter']),
    'a2-priya': ('person/priya2', 'medium', 'track right 1.6 s', 'across to Priya', 'Priya: -$593 a month, even after 11 months', ['bar', 'dot']),
    'a2-priya2': ('ledger/priya', 'medium', 'none', 'hold on her two horizons', 'Priya after 3 years +$11,482; after 7 +$30,387', ['counter']),
    'a2-maya': ('ledger/maya', 'medium', 'track left 1.3 s', 'back to the middle', 'Maya after 3 years +$1,039; after 7 +$8,093', ['counter']),
    'a2-sell': ('balance/sell', 'wide', 'none', 'hold: before / after the break-even month', 'a "sell here" slider across Maya\'s timeline: red before month 30, green after', []),
    'a2-payoff': ('person/three', 'wide', 'pull-out 1.3 s', 'the three households together', 'Dan, Maya, Priya side by side: loan size, loan age, time kept', []),
    'a3-q': ('title/act3', 'wide', 'none', 'hold on the act question', 'act 3 question: what happened in the real drops?', []),
    'a3-all': ('episodes/strip', 'wide', 'pull-out 1.5 s', 'the full history with all 13 drops marked', '13 drop episodes shaded on the rate line', ['line', 'dot']),
    'a3-rules': ('episodes/rule', 'medium', 'push-in 1.3 s', 'go to one episode to show the rule', 'one episode: peak, 1 point lower, refinance marker', ['dot']),
    'a3-costs': ('episodes/costs', 'medium', 'none', 'hold: pre-2018 bills badged', 'bill icons per episode, pre-2018 badged ILLUSTRATIVE', []),
    'a3-range': ('episodes/grid', 'wide', 'none', 'all 13 break-evens (balance method)', '13 bars, months to break even counting the balance (every case shown)', ['bar']),
    'a3-simple': ('episodes/grid2', 'wide', 'none', 'the simple answers appear as ticks', 'a tick per bar for the simple division', ['dot']),
    'a3-young': ('episodes/young', 'medium', 'push-in 1.2 s', 'the loans were months old', 'months on the old loan at refinance (1-4) vs Maya\'s 35', ['bar']),
    'a3-81': ('episodes/1981', 'medium', 'track left 1.5 s', 'travel back to 1981', '1981 peak 18.63%', ['dot']),
    'a3-81b': ('episodes/1981be', 'medium', 'none', 'hold while the counter runs', 'refinance 2 months later, paid back in 13', ['counter']),
    'a3-priya': ('episodes/priya', 'medium', 'none', 'Priya\'s lens on the 13 drops', 'the 13 bars shrink to Priya\'s cost share', ['bar']),
    'a3-dan': ('episodes/dan', 'medium', 'none', 'Dan\'s lens on the 13 drops', 'the 13 bars grow to Dan\'s cost share (18-39 months)', ['bar']),
    'a3-turn': ('episodes/further', 'wide', 'none', 'hold: 3 bars get a second marker', '3 bars marked "next point before break-even"', ['dot']),
    'a3-twice': ('stack/second', 'medium', 'push-in 1.2 s', 'a second bill lands on the first', 'a second bill; the counter restarts', ['bar', 'counter']),
    'a3-example': ('episodes/1984', 'medium', 'track right 1.4 s', 'to the 1984 drop', 'July 1984 peak, refinance November 1984', ['dot']),
    'a3-example2': ('episodes/1984be', 'medium', 'none', 'two clocks', 'break-even clock 19 vs next-drop clock 7', ['counter']),
    'a3-quiet': ('episodes/quiet', 'wide', 'pull-out 1.2 s', 'the other drops settle', 'the remaining 10 bars', []),
    'a3-23': ('episodes/2023', 'medium', 'track right 1.4 s', 'to Maya\'s own drop', 'October 2023 peak (Maya\'s month), 1 point lower in August 2024', ['line', 'dot']),
    'a3-23be': ('episodes/2023be', 'medium', 'none', 'hold while the counter runs', 'would have paid back in 19 months', ['counter']),
    'a3-answer': ('ruler/answer', 'medium', 'none', 'the rehook ruler returns: same object, same place', 'the ruler and Maya\'s card; the "?"', []),
    'a3-answer2': ('ruler/answer2', 'close', 'push-in 1.2 s', 'land on the answer', 'marker lands on 0.5 at the 36-month line', ['dot']),
    'a3-answer3': ('ruler/answer3', 'medium', 'pull-out 1.2 s', 'Dan and Priya get their own marks', 'Dan 1.12 (amber), Priya 0.2 (blue)', ['dot']),
    'a3-today': ('ruler/today', 'medium', 'none', 'today\'s cut on the same ruler', 'today\'s cut 0.59 marked; Maya ahead after 30 months', ['dot']),
    'a3-limit': ('title/limits', 'medium', 'none', 'hold on the limits', 'limits: taxes, return on cash, bill not rolled into the loan', []),
    'a3-median': ('hist/limit', 'medium', 'none', 'callback to the distribution', 'the cost distribution: right half shaded (paid more than $5,124)', []),
    'a3-history': ('title/history', 'wide', 'none', 'hold: the line stops at this week', 'rate line ends at the last week; nothing beyond', []),
    'a3-close': ('stack/close', 'wide', 'pull-out 1.5 s', 'the bill against savings and balance', 'bill on the left; savings and balance settling month by month on the right', ['counter']),
    'm-rates': ('card/method-rates', 'medium', 'none', 'method card: static, readable', 'sources: PMMS via FRED, Optimal Blue check', []),
    'm-drops': ('card/method-drops', 'medium', 'none', 'static', 'zig-zag rule diagram', []),
    'm-costs': ('card/method-costs', 'medium', 'none', 'static', 'HMDA filter list', []),
    'm-chars': ('card/method-chars', 'medium', 'none', 'static', 'the three characters and their medians (ILLUSTRATIVE)', []),
    'm-assume': ('card/method-assume', 'medium', 'none', 'static', 'break-even definition: savings + balance difference >= bill', []),
    'o-recap': ('title/recap', 'wide', 'none', 'hold on the three lines', 'three recap lines with the three households', []),
    'o-you': ('person/you2', 'medium', 'none', 'the blank statement returns', 'the viewer\'s blank statement "7.__%" and the three questions', []),
    'o-close': ('title/close', 'wide', 'drift 8 px/s', 'slow drift to the end', 'closing line', []),
    'o-sources': ('end/screen', 'wide', 'none', 'end screen space (>= 20 s outro)', 'end-screen layout, empty areas for the platform', []),
}

SONIFY = [
    # timbre: S2 = palette 'minimal' of toolkit/audio/sonify_palettes.py, chosen by the owner in the blind test (sổ gu G-005, 2026-09-28)
    {'element': 'bar', 'sound': "S2 (owner's pick, 2026-09-28): a soft low pulse at the value's pitch (MIDI 36-60, D minor pentatonic) with a soft filtered tick (4.5-7 kHz) at the start", 'mapping': 'pitch = bar value on one fixed scale for the film, snapped to the music key; lasts while the bar grows',
     'pan': 'x of the bar', 'timing': 'starts when the bar starts to grow (moved into the nearest syllable gap if the voice is sounding)'},
    {'element': 'line', 'sound': 'S2: soft low pulses on eighth notes of the music tempo while the tip moves, pitch following the slope, each with a faint filtered tick', 'mapping': 'pitch follows the slope at the drawing tip (rising line = higher), snapped to the music key',
     'pan': 'x of the tip', 'timing': 'while the tip moves; discrete notes of a run land in syllable gaps'},
    {'element': 'dot', 'sound': 'S2: one deeper pulse, pitch from the dot height, plus a soft filtered tick', 'mapping': 'pitch from the dot height on screen (higher = higher)',
     'pan': 'x of the dot', 'timing': 'on the frame the dot appears (nearest syllable gap, -60..+120 ms, when the voice is sounding)'},
    {'element': 'counter', 'sound': 'S2: a soft filtered tick per value change; above 8 changes/s the ticks merge into a soft roll', 'mapping': 'one soft event per value change; > 8 changes/s merge into one roll whose density follows the rate of change',
     'pan': 'x of the counter', 'timing': 'on the digit change'},
]

SEPARATION = [
    'Owner, 2026-09-28 (sổ gu G-006): the voice comes first; the data sounds must not cover it; never solved by raising the level (no +10 dB).',
    'Side-chain: the whole data layer ducks 8 dB while the voice is active (20 ms attack, 250 ms release).',
    'Band: while the voice is active the data layer loses 1-4 kHz (the speech band) almost entirely; its energy there stays 31-56 dB under the voice on the sample.',
    'Timing: notes that would start while a syllable sounds move to the quietest instant within -60..+120 ms (a gap between syllables); '
    'decisive numbers still appear on the frame they are spoken (C13 +-250 ms); line draws start in the breath before the sentence.',
    'Level: loudness-matched at -16 dB under the voice (before the side-chain), about -21 dB overall on the sample; final level set by the owner\'s ear.',
    'Conflict noted: rule T1 (>= 1 dB lift in 1.5-8 kHz inside spoken-number windows) is not met this way; for Episode 1 the owner\'s taste wins (episodes/ep001/checks-notes.md).',
]


def main():
    draft = json.load(open(os.path.join(EP, 'out', 'script-draft.json')))
    sents = draft['sentences']
    missing = [s['scene'] for s in sents if s['scene'] not in S]
    extra = [k for k in S if k != 'ident' and k not in {s['scene'] for s in sents}]
    assert not missing and not extra, (missing, extra)
    shots = []
    for i, s in enumerate([{'scene': 'ident'}] if False else []):
        pass
    order = []
    for s in sents:
        if s['scene'] == 'a1-lab' and 'ident' not in order:
            order.append('ident')
        order.append(s['scene'])
    for i, sc in enumerate(order):
        lay, size, move, why, what, son = S[sc]
        shots.append({'id': f'sh{i + 1:03d}', 'scene': sc, 'layout': lay, 'size': size, 'move': move, 'moveReason': why, 'picture': what, 'sonify': son})
    os.makedirs(HERE, exist_ok=True)
    json.dump({'shots': shots, 'characters': {'dan': {'color': 'warn', 'shape': 'solid', 'side': 'left'}, 'priya': {'color': 'accent', 'shape': 'dashed', 'side': 'right'},
                                            'maya': {'color': 'ink', 'shape': 'solid', 'side': 'centre'}},
               'sonification': SONIFY, 'separation': SEPARATION}, open(os.path.join(HERE, 'shotlist.json'), 'w'), indent=1)
    print(len(shots), 'shots; layouts', len({s['layout'] for s in shots}), '| families', sorted({s['layout'].split('/')[0] for s in shots}))


if __name__ == '__main__':
    main()
