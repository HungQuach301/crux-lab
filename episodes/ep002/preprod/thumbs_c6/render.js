'use strict';
// Ep002 C6 thumbnails: Chromium headless (Playwright), canvas 2D, CPU. Reads the signed engines in design/c3/final/src (read only).
//   NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node episodes/ep002/preprod/thumbs_c6/render.js
// Writes out/package/thumb-1..3.png + .json (text boxes at 1280x720) and work/ (neutral + control stills for the pair test).
const fs = require('fs'), path = require('path'), http = require('http');
const { chromium } = require('playwright');
const HERE = __dirname, EP = path.resolve(HERE, '../..'), REPO = path.resolve(EP, '../..'), FIN = path.join(EP, 'design/c3/final');
const PK = path.join(EP, 'out/package'), WORK = path.join(HERE, 'work');
const types = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json', '.woff2': 'font/woff2' };
const srv = http.createServer((q, r) => {
  const u = decodeURIComponent(q.url.split('?')[0]);
  let f;
  if (u.startsWith('/fonts/')) f = path.join(REPO, 'toolkit/render/fonts', u.slice(7));
  else if (u.startsWith('/thumbs/')) f = path.join(HERE, u.slice(8));
  else if (u === '/tokens.json' || u.startsWith('/src/') || u.startsWith('/work/')) f = path.join(FIN, u);
  else f = path.join(REPO, u);
  if (!f.startsWith(REPO)) { r.writeHead(403); r.end(); return; }
  fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); return; } r.writeHead(200, { 'content-type': types[path.extname(f)] || 'application/octet-stream' }); r.end(d); });
});
const JOBS = [
  { fam: 'h2', name: 'offers', out: path.join(PK, 'thumb-1'), id: 'thumb-1', hook: 'two offers (KEY-1)', illustrative: true },
  { fam: 'h3', name: 'history', out: path.join(PK, 'thumb-2'), id: 'thumb-2', hook: 'every stretch since 1954 (KEY-3)', illustrative: true },
  { fam: 'h3', name: 'worst', out: path.join(PK, 'thumb-3'), id: 'thumb-3', hook: 'the worst stretch, April 1977 (KEY-6)', illustrative: true },
  { fam: 'h3', name: 'neutral', out: path.join(WORK, 'thumb-neutral'), id: 'neutral', hook: 'pair test only: fixed neutral thumbnail for the title round', illustrative: true },
  { fam: 'h2', name: 'control', out: path.join(WORK, 'thumb-control'), id: 'control', hook: 'pair test only: weak control (a plain KEY-2 film frame)', illustrative: true },
];
(async () => {
  await new Promise((res) => srv.listen(0, res));
  fs.mkdirSync(WORK, { recursive: true });
  const browser = await chromium.launch({ args: ['--disable-gpu', '--font-render-hinting=none'] });
  for (const fam of ['h2', 'h3']) {
    const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
    page.on('pageerror', (e) => { console.error('pageerror', e.message); process.exit(1); });
    page.on('console', (m) => { if (m.type() === 'error') console.error('console', m.text()); });
    await page.goto(`http://127.0.0.1:${srv.address().port}/thumbs/page.html?fam=${fam}`);
    await page.waitForFunction(() => window.READY === true, null, { timeout: 120000 });
    for (const j of JOBS.filter((x) => x.fam === fam)) {
      const r = await page.evaluate((n) => APP.render(n), j.name);
      fs.writeFileSync(j.out + '.png', Buffer.from(r.png.split(',')[1], 'base64'));
      const scene = { offers: 'design/c3/final/src/k1.js t=7.85 s', history: 'design/c3/final/src/h3/scenes.js K3 t=6.48 s', worst: 'design/c3/final/src/h3/scenes.js K6 t=9.6 s',
        neutral: 'design/c3/final/src/h3/scenes.js K3 t=6.48 s', control: 'design/c3/final/src/k2.js t=2.9 s (with its film labels)' }[j.name];
      fs.writeFileSync(j.out + '.json', JSON.stringify({ option: j.id, hook: j.hook, size: [1280, 720], illustrative: j.illustrative, texts: r.texts,
        source: `preprod/thumbs_c6/render.js + thumbs.js; picture = ${scene} drawn graphics-only by the signed engine (NOTEXT flag); text = Inter 700, tier hero (150 px @1080 = 100 px @720), tokens ink / ink-muted; numbers = out/claims.json display` }, null, 1));
      console.error(j.id, r.texts.map((t) => `${t.text}@${t.fontPx}`).join(' | '));
    }
    await page.close();
  }
  await browser.close(); srv.close();
})().catch((e) => { console.error(e); process.exit(1); });
