'use strict';
// Episode 1 (C5, stream D): three thumbnail options, 1280x720, in the signed visual system (design/c3/final/system.md: tokens, Inter 600/700,
// one idea per frame). Every number is the `display` of a claim in out/claims.json; the owner picks one (taste), see out/package/options.md.
//   NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node episodes/ep001/preprod/thumbs_c5.js
// Writes out/package/thumb-{1,2,3}.png and thumb-{1,2,3}.json {texts:[{text, box:[x,y,w,h], fontPx, claim?}]} (boxes measured in the page).
const fs = require('fs'), path = require('path');
const { chromium } = require('playwright');
const EP = path.resolve(__dirname, '..'), REPO = path.resolve(EP, '../..');
const OUT = path.join(EP, 'out', 'package');
const tok = JSON.parse(fs.readFileSync(path.join(EP, 'design', 'tokens.json'), 'utf8')).colors;
const claims = Object.fromEntries(JSON.parse(fs.readFileSync(path.join(EP, 'out', 'claims.json'), 'utf8')).claims.map((c) => [c.claimId, c]));
const CL = (id) => claims[id].display;
const font = (w) => 'data:font/woff2;base64,' + fs.readFileSync(path.join(REPO, 'toolkit/render/fonts', `inter-latin-${w}-normal.woff2`)).toString('base64');
// NOTE: the fonts are embedded as data: URLs only in this offline thumbnail page (not the render page); the thumbnails are PNGs, and
// the font is the declared Inter (RIGHTS.md F-INTER, OFL 1.1), so quality-framework §8 (no undeclared third-party data: assets) holds.

const css = `@font-face{font-family:Inter;font-weight:600;src:url(${font(600)}) format('woff2')}
@font-face{font-family:Inter;font-weight:700;src:url(${font(700)}) format('woff2')}
html,body{margin:0;width:1280px;height:720px;overflow:hidden;background:${tok.bg};font-family:Inter;color:${tok.text};font-variant-numeric:tabular-nums}
.t{position:absolute;white-space:nowrap;line-height:1;font-weight:700}`;

const T = (id, x, y, px, text, color = tok.text, extra = '') =>
  `<div class="t" data-t="${id}" data-px="${px}" style="left:${x}px;top:${y}px;font-size:${px}px;color:${color};${extra}">${text}</div>`;

const thumbs = [
  { // 1: the bill in the letter
    name: 'thumb-1', claims: { price: 'cost_median' },
    html: () => `
      ${Array.from({ length: 9 }, (_, i) => `<div style="position:absolute;left:${840 + (i % 2) * 14}px;top:${560 - i * 44}px;width:340px;height:36px;background:${i % 2 ? tok.muted : tok.text};border-radius:3px"></div>`).join('')}
      ${T('price', 80, 150, 190, CL('cost_median'))}
      ${T('fees', 84, 360, 100, 'in fees.', tok.muted)}
      ${T('q', 84, 500, 110, 'Worth it?', tok.warn)}`,
  },
  { // 2: three loans, three cuts (heights = cut36_small / cut36_median / cut36_large; no numbers printed)
    name: 'thumb-2', claims: {},
    html: () => {
      const v = [['small', claims.cut36_small.value, tok.csmall, 'tri'], ['median', claims.cut36_median.value, tok.cmedian, 'dot'], ['large', claims.cut36_large.value, tok.clarge, 'sq']];
      const base = 640, k = 330 / v[0][1];
      const cols = v.map(([n, val, col, sh], i) => {
        const x = 830 + i * 150, h = Math.round(val * k);
        const mark = sh === 'dot' ? `border-radius:50%` : '';
        const shape = sh === 'tri'
          ? `<div style="position:absolute;left:${x + 10}px;top:${base - h - 110}px;width:0;height:0;border-left:50px solid transparent;border-right:50px solid transparent;border-bottom:86px solid ${col}"></div>`
          : `<div style="position:absolute;left:${x + 18}px;top:${base - h - 104}px;width:84px;height:84px;background:${col};${mark}"></div>`;
        return `<div style="position:absolute;left:${x}px;top:${base - h}px;width:120px;height:${h}px;background:${col}"></div>${shape}`;
      }).join('');
      return `${cols}<div style="position:absolute;left:790px;top:${base}px;width:470px;height:6px;background:${tok.muted}"></div>
        ${T('l1', 70, 170, 110, 'Smaller loan,')}
        ${T('l2', 70, 320, 110, 'bigger cut.', tok.warn)}
        ${T('l3', 74, 500, 90, 'Why?', tok.muted, 'font-weight:600')}`;
    },
  },
  { // 3: the window that closed (real weekly rates: the 2026 low and the rate of the date anchor)
    name: 'thumb-3', claims: { low: 'low2026', now: 'r_today' },
    html: () => `
      ${T('low', 80, 120, 150, CL('low2026'), tok.accent)}
      ${T('arrow', 575, 120, 150, '→', tok.muted)}
      ${T('now', 760, 120, 150, CL('r_today'), tok.negative)}
      <div style="position:absolute;left:80px;top:330px;width:1120px;height:6px;background:${tok.grid}"></div>
      ${T('h1', 80, 420, 110, 'The window closed.')}
      ${T('h2', 80, 560, 100, 'Still worth it?', tok.warn, 'font-weight:600')}`,
  },
];

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
  for (const th of thumbs) {
    await page.setContent(`<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body>${th.html()}</body></html>`);
    await page.evaluate(() => document.fonts.ready);
    const texts = await page.evaluate(() => [...document.querySelectorAll('[data-t]')].map((e) => {
      const r = e.getBoundingClientRect();
      return { id: e.dataset.t, text: e.textContent, box: [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)], fontPx: Number(e.dataset.px) };
    }));
    for (const t of texts) { if (th.claims[t.id]) t.claim = th.claims[t.id]; delete t.id; }
    await page.screenshot({ path: path.join(OUT, `${th.name}.png`) });
    fs.writeFileSync(path.join(OUT, `${th.name}.json`), JSON.stringify({ texts, source: 'preprod/thumbs_c5.js; numbers = out/claims.json display', option: th.name }, null, 1));
    console.log(th.name, texts.map((t) => t.text).join(' | '));
  }
  await browser.close();
})();
