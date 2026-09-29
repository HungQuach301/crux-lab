'use strict';
// A-M0 step 0: the 10-second end-to-end sample. Builds the contract files and the render data for one sentence of
// narration over the weekly 30-year rate (FRED MORTGAGE30US), from the voice take chosen by toolkit/voice/d_el_voice.py.
//   node episodes/ep001/m0-sample/build.js
// One-off code for the sample (CHARTER §3.1); the episode will write its own.
const fs = require('fs');
const path = require('path');
const R = __dirname;
const EP = path.join(R, '..');
const J = (p) => JSON.parse(fs.readFileSync(path.join(R, p), 'utf8'));
const W = (rel, o) => { const p = path.join(R, rel); fs.mkdirSync(path.dirname(p), { recursive: true }); fs.writeFileSync(p, typeof o === 'string' ? o : JSON.stringify(o, null, 1)); };

const TOTAL = 10.0, START = 1.2, FPS = 30;
const sents = J('out/voice/sentences.json').sentences;
const take = J('out/voice/takes.json').takes[0];
const rec = J('out/voice/el-takes.json')[path.basename(take.raw, '.mp3')];
const clipDur = rec.speech[1] - rec.speech[0] + 0.06;
const s0 = sents[0];
const script = { sentences: [{ id: s0.id, scene: 'm0-rates', text: s0.text, spoken: s0.spoken, start: START, end: +(START + clipDur).toFixed(3) }] };
W('out/script.json', script);

// word cues (video time) from the take's own ASR: final clip = raw from speech[0] - 0.03 s
const cues = {};
const words = rec.words.map((w) => ({ w: w.w, t: +(START + 0.03 + w.start).toFixed(3), e: +(START + 0.03 + w.end).toFixed(3) }));
for (const w of words) cues[s0.id + '|' + w.w.replace(/[.,]$/, '')] = w.t;
const at = (w) => { const x = words.find((y) => y.w.replace(/[.,]$/, '') === w); if (!x) throw new Error('no word ' + w); return x; };
cues[s0.id + '|18.63%'] = at('18').t; // Whisper splits "18.63%" into "18" ".63" "%"

// data: render/data.js carries the full FRED series, so it is NOT tracked (public repo, amendments.md E1-A2; .gitignore
// episodes/*/*/render/data.js). It is rebuilt here from the fetched CSV: run `python3 episodes/ep001/data/fetch.py --verify` first.
const CSV = path.join(EP, 'data', 'normalized', 'mortgage30_weekly.csv');
if (!fs.existsSync(CSV)) throw new Error('missing ' + CSV + ': run python3 episodes/ep001/data/fetch.py --verify (FRED data is not in the repo)');
const rows = fs.readFileSync(CSV, 'utf8').trim().split('\n').slice(1).map((l) => l.split(','));
const series = rows.map(([d, v]) => [d, +v]);
const peak = series.reduce((a, b) => (b[1] > a[1] ? b : a));
const src = { id: 'fred-MORTGAGE30US', url: 'https://fred.stlouisfed.org/series/MORTGAGE30US' };
const claims = [
  { claimId: 'y1971', value: 1971, display: '1971', formula: 'first observation of MORTGAGE30US (week ending 1971-04-02)', source: src, dataYear: 1971, historical: true, illustrative: false, callbacks: [], shownIn: ['m0-rates'], spoken: [{ sentence: s0.id }] },
  { claimId: 'y2026', value: 2026, display: '2026', formula: 'last observation of MORTGAGE30US (week ending ' + series[series.length - 1][0] + ')', source: src, dataYear: 2026, historical: true, illustrative: false, role: 'axis', callbacks: [], shownIn: ['m0-rates'], spoken: [] },
  { claimId: 'term30', value: 30, display: '30', formula: 'loan term of the series (30-year fixed-rate mortgage), series definition', source: src, dataYear: 2026, historical: false, illustrative: false, callbacks: [], shownIn: ['m0-rates'], spoken: [{ sentence: s0.id }] },
  { claimId: 'peak', value: peak[1], display: peak[1].toFixed(2) + '%', formula: 'max over all weeks of MORTGAGE30US (week ending ' + peak[0] + ')', source: src, dataYear: 1981, historical: true, illustrative: false, decisive: true, core: false, callbacks: [], shownIn: ['m0-rates'], spoken: [{ sentence: s0.id }] },
  { claimId: 'y1981', value: 1981, display: '1981', formula: 'calendar year of the week of the maximum', source: src, dataYear: 1981, historical: true, illustrative: false, callbacks: [], shownIn: ['m0-rates'], spoken: [{ sentence: s0.id }] },
];
W('out/claims.json', { claims });

const timeline = { fps: FPS, total: TOTAL, acts: [{ id: 'cold-open', start: 0, end: TOTAL }], scenes: [{ id: 'm0-rates', act: 'cold-open', start: 0, dur: TOTAL, layout: 'line/full', shot: 'wide', panels: ['m0'], chart: 'rates', move: 2.0 }], turns: [{ t: at('18').t, what: 'the line reaches its peak' }] };
W('out/timeline.json', timeline);

const tokens = JSON.parse(fs.readFileSync(path.join(EP, '..', '..', 'genre-spec', 'channel', 'visual-tokens.json'), 'utf8')).colors;
const lc = (h) => h.toLowerCase();
const colors = {
  bg: lc(tokens.bg), surface: lc(tokens.surface), 'surface-2': lc(tokens.surface), text: lc(tokens.ink), 'text-dim': lc(tokens['ink-muted']), muted: lc(tokens['ink-muted']),
  grid: lc(tokens.grid), accent: lc(tokens.accent), warn: lc(tokens.warn), positive: lc(tokens.positive), negative: lc(tokens.negative),
  'key-light': lc(tokens.accent), 'rim-light': lc(tokens.warn), 'badge-bg': lc(tokens.warn), 'badge-text': lc(tokens.bg), loss: lc(tokens.negative), gain: lc(tokens.positive),
  inflation: lc(tokens.warn), c1966: lc(tokens.warn), cmirror: lc(tokens.accent), rate: lc(tokens.accent),
  'bg-cold': lc(tokens.bg), 'bg-act1': lc(tokens.bg), 'bg-act2-early': lc(tokens.bg), 'bg-act3': lc(tokens.bg), 'bg-method': lc(tokens.bg), 'bg-outro': lc(tokens.bg),
};
W('design/tokens.json', { colors, series: { rate: colors.rate }, seriesOf: { rate: colors.rate }, source: 'genre-spec/channel/visual-tokens.json (aliases only: every value is a channel token)' });

W('render/data.js', 'window.DATA = ' + JSON.stringify({ timeline, tokens: { colors }, claims: Object.fromEntries(claims.map((c) => [c.claimId, c])), cues, sentences: script.sentences,
  model: { series, peak }, subframes: 8 }) + ';\n');

W('preprod/shotlist.json', { shots: [{ id: 'm0-1', scene: 'm0-rates', size: 'wide', move: 'slow push-in on the chart plane (z +300) at 0.6-2.0 s', moveReason: 'the line starts to draw: bring the viewer onto the chart plane before the climb' }] });
W('preprod/storyboard.md', '# m0 sample storyboard\n\nOne shot: the weekly rate line draws from 1971; the camera eases in; the peak dot and "18.63%" land on the spoken number; the line runs on to 2026.\n');
W('preprod/color-script.md', '# m0 sample colour script\n\nbg token, rate line accent, peak dot warn. One grade for the whole sample.\n');

// edit decisions for toolkit/finish/m3-glue.js
W('edit/glue.json', { bpm: { 'cold-open': 84 }, match: {}, silences: [], accents: [], adBreaksAfter: [], impacts: ['m0-peak-l'] });
W('edit/cues.json', { cues: [{ t: 0, end: TOTAL, function: 'underscore the climb of the rate line', key: 'D minor', tempo: 84, layer: 'music' }], silences: [] });
W('edit/description.md', '# m0 sample (not for release)\n\nChapters\n0:00 Sample\n\nSource: Freddie Mac, 30-Year Fixed Rate Mortgage Average in the United States [MORTGAGE30US], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/MORTGAGE30US (data years 1971-2026). History, not a forecast. US only. Not financial advice. Narration: synthetic voice (ElevenLabs).\n');
W('out/page.json', { url: 'file://' + path.resolve(R, '..', '..', '..', 'toolkit', 'render', 'page.html') + '?root=' + encodeURIComponent(R) });
W('out/adbreaks.json', { breaks: [] });
console.log('script', script.sentences[0].start, script.sentences[0].end, '| peak', peak, '| cue 18.63%', cues[s0.id + '|18.63%']);
