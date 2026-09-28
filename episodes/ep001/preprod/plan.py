"""Episode 1 pre-production plan: one row per scene (= one narration sentence), the single source of the shot list,
storyboard, colour script, cue sheet and planned tension map.

    python3 episodes/ep001/preprod/plan.py      # needs out/script-draft.json (+ out/voice/takes.json for real timing)

Row: scene -> (layout family/variant, shot size, camera move, reason for the move, what the picture shows,
data-sound elements that change in the scene: bar / line / dot / counter).
Characters: SMALL loan (< $150k) = warn amber, solid, left; LARGE loan ($750k+) = accent blue, dashed, right;
the MEDIAN loan = ink white, centre. Old payment = ink-muted, new payment = accent.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
EP = os.path.join(HERE, '..')

S = {
    # cold open: picture before words (1.5 s lead): two payment bars, the new one drops; a bill slides in; a month counter
    'co-bars': ('bars/payments', 'medium', 'none', 'hold still: the eye must read the two bar heights', 'two monthly-payment bars side by side; the right one drops', ['bar']),
    'co-bill': ('stack/bill', 'close', 'push-in 1.2 s', 'close in on the closing-cost bill as it lands', 'a stack (the closing-cost bill) drops beside the bars; coins start moving from the bar gap to the stack', ['bar', 'counter']),
    'co-question': ('title/question', 'wide', 'pull-out 1.4 s', 'reveal the empty month counter under the question', 'question text; below it a month counter at 0 and an empty progress rail', ['counter']),
    'ident': ('ident/logo', 'wide', 'none', 'no move on the 3 s ident', 'channel ident, 3 s, no narration', []),
    'a1-lab': ('title/lab', 'wide', 'drift 8 px/s', 'slow drift keeps the title card alive', 'lab card: data -> model -> number, three icons', []),
    'a1-scope': ('title/scope', 'medium', 'none', 'hold on the two scope badges', '"US only" and "history, not a forecast" badges', []),
    'a1-rehook': ('ruler/rehook', 'medium', 'track right 1.5 s', 'follow the marker along the ruler to the 36-month line', 'ONE object: a horizontal ruler of rate cut (0 to 2 points); a marker sweeps it and one "?" hangs over it, the answer is not placed until act 3 (hold36 ILLUSTRATIVE badge); 13 small ticks under the ruler = the drops since 1971', ['dot']),
    'a1-rates': ('line/history', 'wide', 'push-in 1.5 s', 'bring the viewer onto the rate line as it starts to draw', 'weekly 30-year rate 1971-2026 draws left to right', ['line']),
    'a1-peak': ('line/peak', 'medium', 'track to peak 1.3 s', 'go to the maximum the line names', 'peak dot 18.63% (1981)', ['dot']),
    'a1-low': ('line/low', 'medium', 'track to low 1.4 s', 'travel along the line to its minimum', 'low dot 2.65% (2021)', ['dot']),
    'a1-drops': ('line/drops', 'wide', 'pull-out 1.5 s', 'show the whole line again to count the falls', '13 falling segments highlight one after another', ['line']),
    'a1-q': ('title/act1', 'wide', 'none', 'hold on the act question', 'act 1 question card', []),
    'a1-hmda': ('ledger/hmda', 'medium', 'push-in 1.2 s', 'approach the disclosure record', 'one loan record card with the field "total loan costs" highlighted', []),
    'a1-terms': ('stack/parts', 'close', 'tilt down 1.2 s', 'read the stack from top to bottom', 'the bill splits into labelled layers: origination, points, appraisal, title, other', ['bar']),
    'a1-points': ('stack/points', 'close', 'none', 'hold: the points layer detaches', 'the points layer slides out (optional)', ['bar']),
    'a1-cashout': ('bars/cashout', 'medium', 'track left 1.2 s', 'move from the cash-out bar back to the rate-and-term bar', 'two median bars: cash-out vs rate-and-term', ['bar']),
    'a1-count': ('ledger/count', 'medium', 'none', 'hold on the count', 'counter rolls to 488,241', ['counter']),
    'a1-median': ('hist/median', 'medium', 'push-in 1.3 s', 'land on the median line of the distribution', 'distribution of total loan costs; median line $5,124', ['bar', 'dot']),
    'a1-spread': ('hist/iqr', 'medium', 'none', 'hold: the middle-half band spreads from the median', 'IQR band $3,443-$8,270 opens', ['bar']),
    'a1-boom': ('line/count', 'wide', 'pull-out 1.4 s', 'widen to the yearly counts 2018-2025', 'yearly refinance counts as bars, 2021 towers', ['bar']),
    'a1-boomcost': ('ledger/2021', 'medium', 'none', 'hold on the 2021 median', '2021 median bill next to its bar', ['counter']),
    'a1-turn': ('bands/intro', 'wide', 'push-in 1.2 s', 'move into the size bands', 'five loan-size bands appear, dollar bars nearly equal', ['bar']),
    'a1-small': ('bands/small', 'medium', 'track left 1.3 s', 'go to the SMALL loan (left, amber)', 'SMALL band: cost as a share of the loan, 3.4%', ['bar']),
    'a1-big': ('bands/large', 'medium', 'track right 1.5 s', 'cross to the LARGE loan (right, blue)', 'LARGE band: 0.5%', ['bar']),
    'a1-keep': ('bands/both', 'wide', 'pull-out 1.2 s', 'both characters in one frame', 'SMALL and LARGE side by side, shares labelled', []),
    'a1-rule': ('title/formula', 'medium', 'none', 'hold on the division', 'formula: bill / monthly drop = months', ['counter']),
    'a1-payoff': ('stack/fill', 'medium', 'push-in 1.2 s', 'watch the savings fill the bill', 'monthly savings fill the bill stack; counter of months', ['bar', 'counter']),
    'a1-after': ('stack/green', 'medium', 'none', 'hold: past break-even the fill turns positive', 'after break-even the fill spills over in positive colour', ['bar']),
    'a2-q': ('title/act2', 'wide', 'none', 'hold on the act question', 'act 2 question card', []),
    'a2-loan': ('ledger/loan', 'medium', 'push-in 1.2 s', 'approach the median loan card', 'MEDIAN loan card: $375,000 balance, $5,124 bill', []),
    'a2-old': ('line/2023', 'medium', 'track to 2023 1.4 s', 'find October 2023 on the rate line', 'rate line zoomed to 2023-2026, October 2023 dot 7.62%', ['line', 'dot']),
    'a2-s025': ('curve/025', 'medium', 'none', 'hold: the first point of the curve', 'axes: rate cut (x) vs months to break even (y); payment bars inset drop $64', ['bar', 'dot']),
    'a2-be025': ('curve/025m', 'medium', 'push-in 1.2 s', 'stress the height of the first point', 'first point at 80 months', ['dot']),
    'a2-s05': ('curve/05', 'medium', 'track right 1.2 s', 'move along the cut axis to 0.5', 'second point; inset bars drop $128', ['bar', 'dot']),
    'a2-be05': ('curve/05m', 'medium', 'none', 'hold on the value', '41 months', ['dot']),
    'a2-s10': ('curve/10', 'medium', 'track right 1.2 s', 'move along to 1 point', 'third point; bars drop $253', ['bar', 'dot']),
    'a2-be10': ('curve/10m', 'medium', 'none', 'hold on the value', '21 months', ['dot']),
    'a2-s20': ('curve/20', 'medium', 'track right 1.2 s', 'move along to 2 points', 'fourth point 11 months', ['dot']),
    'a2-curve': ('curve/full', 'wide', 'pull-out 1.5 s', 'see the whole curve', 'the full curve draws through the points', ['line']),
    'a2-cliff': ('curve/cliff', 'close', 'push-in 1.4 s', 'go to the steep part below 0.5', 'the steep segment glows; years ticks on the y axis', ['line']),
    'a2-thumb': ('curve/thumb', 'medium', 'pull-out 1.2 s', 'compare the two named points', 'points at 1 and 0.5 highlighted together', []),
    'a2-turn': ('bands/return', 'wide', 'none', 'callback to the size bands', 'the SMALL / MEDIAN / LARGE bands return', []),
    'a2-mid': ('curve/median36', 'medium', 'push-in 1.2 s', 'the 36-month line meets the median curve', 'horizontal 36-month line (ILLUSTRATIVE badge), crossing at 0.56', ['line', 'dot']),
    'a2-small': ('curve/small36', 'medium', 'track left 1.3 s', 'the SMALL curve crosses further right', 'SMALL curve (amber solid) crossing at 1.32', ['line', 'dot']),
    'a2-big': ('curve/large36', 'medium', 'track right 1.3 s', 'the LARGE curve crosses near zero', 'LARGE curve (blue dashed) crossing at 0.2', ['line', 'dot']),
    'a2-hold60': ('curve/60', 'medium', 'tilt up 1.2 s', 'raise the target line to 60 months', '60-month line, crossing at 0.33', ['dot']),
    'a2-hold84': ('curve/84', 'medium', 'tilt up 1.2 s', 'raise it to 84 months', '84-month line, crossing at 0.24', ['dot']),
    'a2-flip': ('curve/flip', 'wide', 'pull-out 1.3 s', 'show both sides of the flip point', 'area left of the crossing shaded "bill outlasts the stay", right shaded "savings win"', []),
    'a2-payoff': ('ledger/two', 'medium', 'none', 'hold on the two drivers', 'two dials: loan size, time kept', []),
    'a2-hold': ('ledger/unknown', 'close', 'push-in 1.2 s', 'close on the unknown dial', 'the time-kept dial shows "?"', []),
    'a2-reset': ('bars/timeline', 'wide', 'track right 1.5 s', 'follow the payment timeline to its new end', 'two payment timelines: old ends earlier, new ends 30 years out', ['line']),
    'a2-reset2': ('title/firstq', 'medium', 'none', 'hold on the question the division answers', 'the division card again, only "when" is lit', []),
    'a3-q': ('title/act3', 'wide', 'none', 'hold on the act question', 'act 3 question card', []),
    'a3-all': ('episodes/strip', 'wide', 'pull-out 1.5 s', 'the full history with all 13 drops marked', '13 drop episodes shaded on the rate line', ['line', 'dot']),
    'a3-rules': ('episodes/rule', 'medium', 'push-in 1.3 s', 'go to one episode to show the rule', 'one episode: peak dot, 1-point-lower dot, refinance marker', ['dot']),
    'a3-costs': ('episodes/costs', 'medium', 'none', 'hold: pre-2018 bills get the ILLUSTRATIVE badge', 'bill icons on each episode, pre-2018 badged ILLUSTRATIVE', []),
    'a3-80s': ('episodes/1980s', 'wide', 'track left 1.5 s', 'travel back to the 1980s', 'the three 1980s drops glow', ['line']),
    'a3-81': ('episodes/1981', 'medium', 'push-in 1.3 s', 'into the 1981 drop', '1981 peak, refinance 2 months later', ['dot']),
    'a3-81be': ('episodes/1981be', 'medium', 'none', 'hold while the counter runs', 'break-even counter to 13; the next-point dot lands at 9', ['counter', 'dot']),
    'a3-short': ('episodes/1987', 'medium', 'track right 1.3 s', 'jump to the brief 1987 drop', '1987 drop, 4 months, refinance at the bottom', ['dot']),
    'a3-06': ('episodes/2006', 'medium', 'track right 1.5 s', 'jump to the long 2006-2012 drop', 'slow fall; refinance January 2008; break-even before the next point', ['line', 'dot']),
    'a3-range': ('episodes/grid', 'wide', 'pull-out 1.2 s', 'all 13 break-evens at once', '13 bars of break-even months (every case shown, DX-H6)', ['bar']),
    'a3-turn': ('episodes/further', 'wide', 'none', 'hold: 5 bars get a second marker', '5 bars marked "next point before break-even"', ['dot']),
    'a3-twice': ('stack/second', 'medium', 'push-in 1.2 s', 'a second bill lands on the first', 'a second bill drops; the counter restarts', ['bar', 'counter']),
    'a3-example': ('episodes/2018', 'medium', 'track right 1.5 s', 'go to the 2018-2020 drop', 'November 2018 peak, refinance June 2019', ['dot']),
    'a3-example2': ('episodes/2020', 'medium', 'none', 'hold while the two clocks run', 'break-even clock 18 vs next-drop clock 17', ['counter']),
    'a3-quiet': ('episodes/quiet', 'wide', 'pull-out 1.2 s', 'the other 8 bars settle', 'the 8 remaining bars', []),
    'a3-23': ('episodes/2023', 'medium', 'track right 1.4 s', 'to the latest drop', 'October 2023 peak, August 2024 cut', ['line', 'dot']),
    'a3-23be': ('episodes/2023be', 'medium', 'none', 'hold while the counter runs', 'break-even 21 months (HMDA 2024 cost share)', ['counter']),
    'a3-answer': ('ruler/answer', 'medium', 'none', 'the rehook ruler returns: same object, same place', 'the ruler of the rehook; the "?" marker', []),
    'a3-answer2': ('ruler/answer2', 'close', 'push-in 1.2 s', 'land on the answer', 'marker lands on 0.56 at the 36-month line', ['dot']),
    'a3-answer3': ('ruler/answer3', 'medium', 'track right 1.2 s', 'follow the marker to 1 point', 'second mark at 1 point / 21 months', ['dot']),
    'a3-limit': ('title/limits', 'medium', 'none', 'hold on the three limits', 'three limit lines: taxes, return on cash, term reset', []),
    'a3-median': ('hist/limit', 'medium', 'none', 'callback to the distribution', 'the cost distribution: right half shaded (paid more than $5,124)', []),
    'a3-history': ('title/history', 'wide', 'none', 'hold: the forecast line stops at today', 'rate line ends at the last week; nothing beyond', []),
    'a3-close': ('stack/close', 'wide', 'pull-out 1.5 s', 'the bill and the months side by side', 'bill on the left, months arriving on the right', ['counter']),
    'm-rates': ('card/method-rates', 'medium', 'none', 'method card: static, readable', 'sources: PMMS via FRED, Optimal Blue check', []),
    'm-drops': ('card/method-drops', 'medium', 'none', 'static', 'zig-zag rule diagram', []),
    'm-costs': ('card/method-costs', 'medium', 'none', 'static', 'HMDA filter list', []),
    'm-assume': ('card/method-assume', 'medium', 'none', 'static', 'assumptions list', []),
    'o-recap': ('title/recap', 'wide', 'none', 'hold on the three lines', 'three recap lines', []),
    'o-close': ('title/close', 'wide', 'drift 8 px/s', 'slow drift to the end', 'closing line', []),
    'o-bill': ('stack/end', 'wide', 'none', 'hold', 'bill and months, final image', []),
    'o-sources': ('end/screen', 'wide', 'none', 'end screen space (>= 20 s outro)', 'end-screen layout, empty areas for the platform', []),
}

SONIFY = [
    # timbre ("sound") left EMPTY until the owner picks a palette from the blind test (review-m1/sonify-S1/S2/S3.mp4, sổ gu G-005)
    {'element': 'bar', 'sound': '', 'mapping': 'pitch = bar value on one fixed scale for the film, snapped to the music key; lasts while the bar grows',
     'pan': 'x of the bar', 'timing': 'starts when the bar starts to grow (moved into the nearest syllable gap if the voice is sounding)'},
    {'element': 'line', 'sound': '', 'mapping': 'pitch follows the slope at the drawing tip (rising line = higher), snapped to the music key',
     'pan': 'x of the tip', 'timing': 'while the tip moves; discrete notes of a run land in syllable gaps'},
    {'element': 'dot', 'sound': '', 'mapping': 'pitch from the dot height on screen (higher = higher)',
     'pan': 'x of the dot', 'timing': 'on the frame the dot appears (nearest syllable gap, -60..+120 ms, when the voice is sounding)'},
    {'element': 'counter', 'sound': '', 'mapping': 'one soft event per value change; > 8 changes/s merge into one roll whose density follows the rate of change',
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
    json.dump({'shots': shots, 'characters': {'small': {'color': 'warn', 'shape': 'solid', 'side': 'left'}, 'large': {'color': 'accent', 'shape': 'dashed', 'side': 'right'},
                                            'median': {'color': 'ink', 'shape': 'solid', 'side': 'centre'}},
               'sonification': SONIFY, 'separation': SEPARATION}, open(os.path.join(HERE, 'shotlist.json'), 'w'), indent=1)
    print(len(shots), 'shots; layouts', len({s['layout'] for s in shots}), '| families', sorted({s['layout'].split('/')[0] for s in shots}))


if __name__ == '__main__':
    main()
