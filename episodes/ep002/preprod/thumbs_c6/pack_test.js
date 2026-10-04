'use strict';
// Episode 2 · C6 blind pair-test materials (REFERENCE only). Protocol: review-c6/pack-test/intent.md (written first).
// Search-result cards (thumbnail + duration + title + channel). Round T (titles): A1, A2, weak control WT, all on ONE fixed
// neutral thumbnail. Round M (thumbnails): thumb-1..3 + weak control WM, all under ONE fixed title (A1). Every unordered pair
// in both orders; file names random hex; key in key.json. Cards for the owner (not shown to readers): out/package/cards/.
//   NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node episodes/ep002/preprod/thumbs_c6/pack_test.js
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const { chromium } = require('playwright');
const HERE = __dirname, EP = path.resolve(HERE, '../..'), REPO = path.resolve(EP, '../..');
const PK = path.join(EP, 'out/package'), DEST = path.join(EP, 'review-c6/pack-test'), CARDS = path.join(PK, 'cards');
const DURATION = '9:45'; // out/video.mp4 585.6 s
const T = JSON.parse(fs.readFileSync(path.join(HERE, 'titles.json'), 'utf8'));
const titles = { A1: T.A1.title, A2: T.A2.title, WT: T['W-title'].title };
const NEUTRAL = path.join(HERE, 'work/thumb-neutral.png');
const FIXED_TITLE = T.A1.title;
const thumbs = { 'thumb-1': path.join(PK, 'thumb-1.png'), 'thumb-2': path.join(PK, 'thumb-2.png'), 'thumb-3': path.join(PK, 'thumb-3.png'), WM: path.join(HERE, 'work/thumb-control.png') };
const font = (w) => 'data:font/woff2;base64,' + fs.readFileSync(path.join(REPO, 'toolkit/render/fonts', `inter-latin-${w}-normal.woff2`)).toString('base64');
const img = (abs) => 'data:image/png;base64,' + fs.readFileSync(abs).toString('base64');
const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
const CW = 640;
const css = `@font-face{font-family:Inter;font-weight:400;src:url(${font(400)}) format('woff2')}
@font-face{font-family:Inter;font-weight:600;src:url(${font(600)}) format('woff2')}
html,body{margin:0;background:#0f0f0f;font-family:Inter;color:#f1f1f1}
.wrap{width:${CW + 96}px;padding:20px 0}
.row{display:flex;align-items:flex-start;gap:0;margin:0 0 22px}
.lab{width:72px;flex:0 0 72px;display:flex;justify-content:center;padding-top:8px}
.lab span{display:inline-flex;width:52px;height:52px;border-radius:26px;background:#3ea6ff;color:#0f0f0f;font-weight:600;font-size:32px;align-items:center;justify-content:center}
.card{width:${CW}px}
.th{position:relative;width:${CW}px;height:${CW * 9 / 16}px;border-radius:12px;overflow:hidden}
.th img{width:100%;height:100%;display:block}
.dur{position:absolute;right:8px;bottom:8px;background:rgba(0,0,0,0.8);color:#fff;font-size:15px;font-weight:600;padding:3px 6px;border-radius:4px}
.meta{display:flex;gap:12px;padding:12px 4px 0}
.av{flex:0 0 40px;width:40px;height:40px;border-radius:20px;background:#2a303b;color:#f2f4f7;font-weight:600;font-size:20px;display:flex;align-items:center;justify-content:center}
.ti{font-size:20px;line-height:28px;font-weight:600;max-height:56px;overflow:hidden}
.ch{font-size:15px;color:#aaa;margin-top:4px}`;
const card = (title, thumb) => `<div class="card"><div class="th"><img src="${img(thumb)}"><div class="dur">${DURATION}</div></div>
  <div class="meta"><div class="av">C</div><div><div class="ti">${esc(title)}</div><div class="ch">Crux</div></div></div></div>`;
const row = (n, inner) => `<div class="row"><div class="lab"><span>${n}</span></div>${inner}</div>`;
const hex = () => crypto.randomBytes(5).toString('hex');

(async () => {
  for (const f of fs.existsSync(DEST) ? fs.readdirSync(DEST) : []) if (/^[0-9a-f]{10}$/.test(f)) fs.rmSync(path.join(DEST, f), { recursive: true });
  fs.mkdirSync(DEST, { recursive: true }); fs.mkdirSync(CARDS, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: CW + 96, height: 600 }, deviceScaleFactor: 1 });
  const shot = async (html, file) => {
    await page.setContent(`<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body><div class="wrap">${html}</div></body></html>`);
    await page.evaluate(() => document.fonts.ready);
    const el = await page.$('.wrap'); await el.screenshot({ path: file });
  };
  // owner-facing single cards (not shown to readers)
  for (const [k, t] of Object.entries(titles)) await shot(card(t, NEUTRAL), path.join(CARDS, `card-title-${k}.png`));
  for (const [k, th] of Object.entries(thumbs)) await shot(card(FIXED_TITLE, th), path.join(CARDS, `card-${k}.png`));
  const rel = (p) => path.relative(EP, p);
  const key = { _: 'GIẢI MÃ — không mở trước khi đủ câu trả lời.', about: 'Pair images: card "1" on top, card "2" below. round T = titles on one fixed neutral thumbnail; round M = thumbnails under one fixed title.',
    roundT: { thumbnail: rel(NEUTRAL), titles }, roundM: { title: FIXED_TITLE, thumbs: Object.fromEntries(Object.entries(thumbs).map(([k, v]) => [k, rel(v)])) }, pairs: {} };
  const jobs = [];
  const pairsOf = (ks, round) => { for (let i = 0; i < ks.length; i++) for (let j = i + 1; j < ks.length; j++) jobs.push([round, ks[i], ks[j]], [round, ks[j], ks[i]]); };
  pairsOf(Object.keys(titles), 'T'); pairsOf(Object.keys(thumbs), 'M');
  for (let i = jobs.length - 1; i > 0; i--) { const j = crypto.randomInt(i + 1); [jobs[i], jobs[j]] = [jobs[j], jobs[i]]; }
  const used = new Set();
  for (const [round, A, B] of jobs) {
    const h = (x) => round === 'T' ? card(titles[x], NEUTRAL) : card(FIXED_TITLE, thumbs[x]);
    let id; do { id = hex(); } while (used.has(id)); used.add(id);
    fs.mkdirSync(path.join(DEST, id)); await shot(row(1, h(A)) + row(2, h(B)), path.join(DEST, id, `${id}.png`));
    key.pairs[id] = { round, 1: A, 2: B };
  }
  key.counts = { T: jobs.filter((j) => j[0] === 'T').length, M: jobs.filter((j) => j[0] === 'M').length };
  fs.writeFileSync(path.join(DEST, 'key.json'), JSON.stringify(key, null, 1));
  await browser.close();
  console.log('pairs', key.counts);
})().catch((e) => { console.error(e); process.exit(1); });
