'use strict';
// Episode 1 · packaging v2 thumbnails (H = houses, L = letter, W = window), 1280x720.
// Stage 1: each 3D still is rendered with the SIGNED C3 final engine (design/c3/final/src/engine.js: tokens, house(),
//          woodTable(), owedTex(), canvasTex; three.js via SwiftShader, CPU) at 1920x1080, no text; the scene module
//          publishes screen anchors (window.ANCHORS).
// Stage 2: compose at 1280x720 (still scaled 2/3) + flat Inter text in token colours; boxes measured in the page.
//   NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node episodes/ep001/preprod/thumbs_v2/render.js [H L W]
// Writes out/package/v2/thumb-{H,L,W}.png + .json {texts:[{text, box, fontPx, claim?}], ...}; stills in work/thumbs_v2/.
const fs = require('fs'), path = require('path'), http = require('http');
const { chromium } = require('playwright');
const HERE = __dirname, EP = path.resolve(HERE, '../..'), REPO = path.resolve(EP, '../..');
const C3 = path.join(EP, 'design/c3/final'), THREE_DIR = process.env.THREE_DIR || path.join(EP, 'animatic/node_modules/three/build');
const OUT = path.join(EP, 'out/package/v2'), WORK = path.join(EP, 'work/thumbs_v2');
const tok = JSON.parse(fs.readFileSync(path.join(EP, 'design/tokens.json'), 'utf8')).colors;
const claims = Object.fromEntries(JSON.parse(fs.readFileSync(path.join(EP, 'out/claims.json'), 'utf8')).claims.map((c) => [c.claimId, c]));
const CL = (id) => claims[id].display;
const MINUS = '−';
const types = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json', '.woff2': 'font/woff2' };
const srv = http.createServer((q, r) => {
  const u = decodeURIComponent(q.url.split('?')[0]);
  const f = u.startsWith('/three/') ? path.join(THREE_DIR, u.slice(7)) : u.startsWith('/fonts/') ? path.join(REPO, 'toolkit/render/fonts', u.slice(7))
    : u.startsWith('/v2/') ? path.join(HERE, u.slice(4)) : u === '/tokens.json' ? path.join(C3, 'tokens.json') : path.join(C3, u);
  fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); return; } r.writeHead(200, { 'content-type': types[path.extname(f)] || 'application/octet-stream' }); r.end(d); });
});
const font = (w) => 'data:font/woff2;base64,' + fs.readFileSync(path.join(REPO, 'toolkit/render/fonts', `inter-latin-${w}-normal.woff2`)).toString('base64');
const css = `@font-face{font-family:Inter;font-weight:600;src:url(${font(600)}) format('woff2')}
@font-face{font-family:Inter;font-weight:700;src:url(${font(700)}) format('woff2')}
html,body{margin:0;width:1280px;height:720px;overflow:hidden;background:${tok.bg};font-family:Inter;color:${tok.text};font-variant-numeric:tabular-nums}
.bg{position:absolute;left:0;top:0;width:1280px;height:720px}
.t{position:absolute;white-space:nowrap;line-height:1;font-weight:700;letter-spacing:-0.01em}
.pl{padding:14px 22px 16px;border-radius:14px;background:rgba(14,17,22,0.86)}`;
const PLATE = 'rgba(14,17,22,0.86)';
// T(id, x, y, px, text, {color, anchor:'l'|'c'|'r', plate, extra}) ; (x,y) = top of the text box
const T = (id, x, y, px, text, o = {}) => {
  const tx = o.anchor === 'c' ? 'translateX(-50%)' : o.anchor === 'r' ? 'translateX(-100%)' : 'none';
  return `<div class="t${o.plate ? ' pl' : ''}" data-t="${id}" data-px="${px}" style="left:${Math.round(x)}px;top:${Math.round(y)}px;font-size:${px}px;color:${o.color || tok.text};transform:${tx};${o.plate ? `background:${o.plate};` : ''}${o.extra || ''}">${text}</div>`;
};
// Badge size = signed type token (design/c3/final/tokens.json type.badge, 48 px at 1080) scaled 2/3 like the still: 32 px
// (owner, 30/09: keep ILLUSTRATIVE on L, sized by the token; P01's 90 px floor is waived for the badge, THAM KHẢO).
const BADGE_TOK = JSON.parse(fs.readFileSync(path.join(C3, 'tokens.json'), 'utf8')).type.badge;
const BADGE = (px = Math.round(BADGE_TOK.px * 2 / 3)) => `<div class="t" data-t="badge" data-px="${px}" style="right:36px;top:30px;font-size:${px}px;font-weight:${BADGE_TOK.weight};color:${tok['badge-text']};background:${tok['badge-bg']};padding:${Math.round(px * 0.3)}px ${Math.round(px * 0.47)}px ${Math.round(px * 0.32)}px;border-radius:${Math.round(px * 0.26)}px">ILLUSTRATIVE</div>`;
const s = (p) => ({ x: p.x * 2 / 3, y: p.y * 2 / 3 });

const THUMBS = {
  H: { hook: 'a', claims: { walt: 'cut36_small', anj: 'cut36_large' }, illustrative: true,
    html: (A) => {
      const w = s(A.waltTop), a = s(A.anjTop);
      return `${T('walt', w.x, w.y - 150, 104, `${MINUS}${CL('cut36_small')} pts`, { anchor: 'c', color: tok.warn, plate: PLATE })}
        ${T('anj', a.x, Math.max(96, a.y - 150), 104, `${MINUS}${CL('cut36_large')} pts`, { anchor: 'c', color: tok['negative-light'], plate: PLATE })}
        ${BADGE()}`;
    } },
  L: { hook: 'b', claims: { bill: 'cost_median', gap: 'gap24' }, illustrative: true,
    html: (A) => {
      const c = s(A.billC), l = s(A.billL), r = s(A.billR), sl = s(A.slabC);
      const px = 108;
      return `${T('bill', c.x, c.y - px * 0.6, px, CL('cost_median'), { anchor: 'c', color: tok['paper-ink'] })}
        ${T('gap', 1280 - 40, Math.max(sl.y - 250, 150), 110, '+' + CL('gap24'), { anchor: 'r', color: tok['negative-light'], plate: PLATE })}
        ${BADGE()}`;
    } },
  W: { hook: 'c', claims: { low: 'low2026' }, illustrative: false,
    html: (A) => {
      const lo = s(A.low), top = s(A.winTop);
      return `<div style="position:absolute;left:${Math.round(lo.x) - 2}px;top:${Math.round(top.y) + 190}px;width:4px;height:${Math.round(lo.y - top.y - 190 - 14)}px;background:${tok.text}"></div>
        ${T('low', lo.x, top.y + 22, 150, CL('low2026'), { anchor: 'c', color: tok.text, plate: PLATE })}
        ${T('q', 1280 - 48, 720 - 140, 100, 'Missed it?', { anchor: 'r', color: tok.warn, plate: PLATE })}`;
    } },
};

(async () => {
  const want = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(THUMBS);
  fs.mkdirSync(OUT, { recursive: true }); fs.mkdirSync(WORK, { recursive: true });
  await new Promise((res) => srv.listen(0, res));
  const port = srv.address().port;
  const browser = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--disable-gpu', '--font-render-hinting=none'] });
  for (const k of want) {
    const th = THUMBS[k];
    const p3 = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
    p3.on('pageerror', (e) => { console.error('pageerror', e.message); process.exit(1); });
    await p3.goto(`http://127.0.0.1:${port}/v2/page.html?f=th${k}`);
    await p3.waitForFunction(() => window.READY === true, null, { timeout: 120000 });
    const t0 = Date.now();
    const png = await p3.evaluate(() => APP.png(0));
    const A = await p3.evaluate(() => window.ANCHORS);
    await p3.close();
    const still = path.join(WORK, `still-${k}.png`);
    fs.writeFileSync(still, Buffer.from(png.split(',')[1], 'base64'));
    const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
    await page.setContent(`<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body><img class="bg" src="${png}">${th.html(A)}</body></html>`);
    await page.evaluate(() => document.fonts.ready);
    const texts = await page.evaluate(() => [...document.querySelectorAll('[data-t]')].map((e) => {
      const r = e.getBoundingClientRect();
      return { id: e.dataset.t, text: e.textContent, box: [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)], fontPx: Number(e.dataset.px) };
    }));
    for (const t of texts) { if (th.claims[t.id]) t.claim = th.claims[t.id]; if (t.id === 'badge') t.role = 'ILLUSTRATIVE badge (rule S08)'; delete t.id; }
    await page.screenshot({ path: path.join(OUT, `thumb-${k}.png`) });
    await page.close();
    const meta = { option: `thumb-${k}`, hook: th.hook, illustrative: th.illustrative, texts, anchors1080: A, stillMs: Date.now() - t0,
      source: 'preprod/thumbs_v2/render.js; 3D = design/c3/final/src/engine.js (signed C3 H1 objects); numbers = out/claims.json display' };
    fs.writeFileSync(path.join(OUT, `thumb-${k}.json`), JSON.stringify(meta, null, 1));
    console.log(k, texts.map((t) => `${t.text}@${t.fontPx}`).join(' | '));
  }
  await browser.close(); srv.close();
})().catch((e) => { console.error(e); process.exit(1); });
