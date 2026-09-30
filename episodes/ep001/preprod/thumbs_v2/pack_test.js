'use strict';
// Episode 1 · packaging v2: blind pairwise materials for P2 (REFERENCE only, like the C1 pairwise). Search-result cards
// (thumbnail + duration + title + channel), 7 packages: 6 new titles, each with the thumbnail of its hook (a->H, b->L,
// c->W), plus the current package (T1 + thumb-3) as control. Every unordered pair in both orders (42 images), plus a
// thumbnail-only set (H, L, W with the SAME title; 6 images). File names are random hex; the key is key.json.
//   NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node episodes/ep001/preprod/thumbs_v2/pack_test.js
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const { chromium } = require('playwright');
const EP = path.resolve(__dirname, '../..'), REPO = path.resolve(EP, '../..');
const PK = path.join(EP, 'out/package'), DEST = path.join(EP, 'review-c6/pack-test'), CARDS = path.join(PK, 'v2/cards');
const DURATION = '9:51'; // out/video.mp4 591.3 s
const CONTROL_TITLE = 'How Big a Rate Cut Makes a Refinance Worth It?';
const packages = {
  a1: { title: 'Why a Smaller Loan Needs a Bigger Rate Cut to Be Worth It', thumb: 'v2/thumb-H.png' },
  a2: { title: 'Same Rate Cut, Opposite Results for a Small and Big Mortgage', thumb: 'v2/thumb-H.png' },
  b1: { title: "The Refinance Cost That Isn't in the Fees", thumb: 'v2/thumb-L.png' },
  b2: { title: 'Refinance Break-Even: The $1,133 That Simple Division Misses', thumb: 'v2/thumb-L.png' },
  c1: { title: 'Got a 2023 Mortgage? The 1-Point Rule May Not Fit Your Loan', thumb: 'v2/thumb-W.png' },
  c2: { title: 'Borrowed Over 7% in 2023? The Rate Cut a Refinance Needs', thumb: 'v2/thumb-W.png' },
  control: { title: CONTROL_TITLE, thumb: 'thumb-3.png' },
};
const thumbOnly = { H: 'v2/thumb-H.png', L: 'v2/thumb-L.png', W: 'v2/thumb-W.png' };
const font = (w) => 'data:font/woff2;base64,' + fs.readFileSync(path.join(REPO, 'toolkit/render/fonts', `inter-latin-${w}-normal.woff2`)).toString('base64');
const img = (rel) => 'data:image/png;base64,' + fs.readFileSync(path.join(PK, rel)).toString('base64');
const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
const CW = 640; // card width: a search-result thumbnail is shown at roughly this size or smaller
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
  fs.rmSync(DEST, { recursive: true, force: true }); fs.mkdirSync(DEST, { recursive: true }); fs.mkdirSync(CARDS, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: CW + 96, height: 600 }, deviceScaleFactor: 1 });
  const shot = async (html, file) => {
    await page.setContent(`<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body><div class="wrap">${html}</div></body></html>`);
    await page.evaluate(() => document.fonts.ready);
    const el = await page.$('.wrap'); await el.screenshot({ path: file });
  };
  for (const [k, p] of Object.entries(packages)) await shot(card(p.title, p.thumb), path.join(CARDS, `card-${k}.png`));
  const key = { _: 'GIẢI MÃ — không mở trước khi chọn.', about: 'Pair images: card "1" on top, card "2" below. set = package (title + thumbnail) or thumbnail (same title on both).',
    packages, thumbnailOnly: { title: CONTROL_TITLE, thumbs: thumbOnly }, pairs: {} };
  const used = new Set();
  const make = async (set, A, B, htmlA, htmlB) => {
    let id; do { id = hex(); } while (used.has(id)); used.add(id);
    fs.mkdirSync(path.join(DEST, id)); await shot(row(1, htmlA) + row(2, htmlB), path.join(DEST, id, `${id}.png`));
    key.pairs[id] = { set, 1: A, 2: B };
  };
  const jobs = [];
  const ks = Object.keys(packages);
  for (let i = 0; i < ks.length; i++) for (let j = i + 1; j < ks.length; j++) jobs.push(['package', ks[i], ks[j]], ['package', ks[j], ks[i]]);
  const ts = Object.keys(thumbOnly);
  for (let i = 0; i < ts.length; i++) for (let j = i + 1; j < ts.length; j++) jobs.push(['thumbnail', ts[i], ts[j]], ['thumbnail', ts[j], ts[i]]);
  // shuffle job order so that directory creation order does not follow the pair order
  for (let i = jobs.length - 1; i > 0; i--) { const j = crypto.randomInt(i + 1); [jobs[i], jobs[j]] = [jobs[j], jobs[i]]; }
  for (const [set, A, B] of jobs) {
    const h = (x) => set === 'package' ? card(packages[x].title, packages[x].thumb) : card(CONTROL_TITLE, thumbOnly[x]);
    await make(set, A, B, h(A), h(B));
  }
  key.counts = { package: jobs.filter((j) => j[0] === 'package').length, thumbnail: jobs.filter((j) => j[0] === 'thumbnail').length };
  fs.writeFileSync(path.join(DEST, 'key.json'), JSON.stringify(key, null, 1));
  await browser.close();
  console.log('pairs', key.counts);
})().catch((e) => { console.error(e); process.exit(1); });
