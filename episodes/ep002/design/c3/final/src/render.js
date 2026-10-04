'use strict';
// Ep002 C3 final renderer (canvas 2D, CPU only): Chromium headless (Playwright) -> raw RGBA -> encode.py (PyAV libx264).
//   NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node render.js K1 [--still t1,t2] [--mask]
// Writes ../K1.mp4, ../K1-strip.png, ../K1-strip-masked.png (MASK flag in the build), ../work/render-log-K1.json
// (timings, claim IDs, every on-screen string, self-check on every 3rd frame).
const fs = require('fs'), path = require('path'), http = require('http'), os = require('os'), { spawn } = require('child_process');
const { chromium } = require('playwright');
const HERE = __dirname, OUT = path.resolve(HERE, '..'), REPO = path.resolve(HERE, '../../../../../..');
const args = process.argv.slice(2), F = args[0];
const opt = (k) => { const i = args.indexOf('--' + k); return i >= 0 ? args[i + 1] : null; };
const types = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json', '.woff2': 'font/woff2' };
const srv = http.createServer((q, r) => {
  const u = decodeURIComponent(q.url.split('?')[0]);
  const f = u.startsWith('/fonts/') ? path.join(REPO, 'toolkit/render/fonts', u.slice(7)) : path.join(OUT, u);
  fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); return; } r.writeHead(200, { 'content-type': types[path.extname(f)] || 'application/octet-stream' }); r.end(d); });
});
(async () => {
  await new Promise((res) => srv.listen(0, res));
  const port = srv.address().port;
  const browser = await chromium.launch({ args: ['--disable-gpu', '--font-render-hinting=none'] });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
  page.on('pageerror', (e) => { console.error('pageerror', e.message); process.exit(1); });
  page.on('console', (m) => { if (m.type() === 'error') console.error('console', m.text()); });
  await page.goto(`http://127.0.0.1:${port}/src/page.html?f=${F.toLowerCase()}`);
  await page.waitForFunction(() => window.READY === true, null, { timeout: 120000 });
  const meta = await page.evaluate(() => ({ d: APP.duration, n: APP.frames, strip: APP.stripTimes }));
  const savePng = (file, dataUrl) => { fs.mkdirSync(path.dirname(file), { recursive: true }); fs.writeFileSync(file, Buffer.from(dataUrl.split(',')[1], 'base64')); };
  if (opt('still')) {
    for (const t of opt('still').split(',').map(Number)) savePng(path.join(OUT, 'work', `${F}-still-${t.toFixed(2)}${args.includes('--mask') ? '-m' : ''}.png`), await page.evaluate(([t, m]) => APP.png(t, { mask: m }), [t, args.includes('--mask')]));
    await browser.close(); srv.close(); return;
  }
  const N = meta.n;
  const enc = spawn('python3', [path.join(HERE, 'encode.py'), path.join(OUT, `${F}.mp4`), '1280', '720', '30', '18'], { stdio: ['pipe', 'inherit', 'inherit'] });
  const done = new Promise((res, rej) => enc.on('close', (c) => (c ? rej(new Error('encode ' + c)) : res())));
  const t0 = Date.now();
  for (let f = 0; f < N; f++) {
    const b64 = await page.evaluate((t) => APP.frame(t), f / 30);
    if (!enc.stdin.write(Buffer.from(b64, 'base64'))) await new Promise((r) => enc.stdin.once('drain', r));
  }
  enc.stdin.end(); await done;
  const wall = (Date.now() - t0) / 1000;
  savePng(path.join(OUT, `${F}-strip.png`), await page.evaluate((ts) => APP.strip(ts, false), meta.strip));
  savePng(path.join(OUT, `${F}-strip-masked.png`), await page.evaluate((ts) => APP.strip(ts, true), meta.strip));
  // self-check every 3rd frame + every strip frame
  const agg = new Map();
  const times = [...new Set([...Array.from({ length: Math.ceil(N / 3) }, (_, i) => (3 * i) / 30), ...meta.strip])];
  for (const t of times) {
    for (const r of await page.evaluate((t) => APP.check(t), t)) {
      const e = agg.get(r.s) || { s: r.s, px: r.px, dGraphicMin: 99, dTextMin: 99, contrastMin: 99, at: {} };
      if (r.dGraphic < e.dGraphicMin) { e.dGraphicMin = r.dGraphic; e.at.dGraphic = +t.toFixed(2); }
      if (r.dText < e.dTextMin) { e.dTextMin = r.dText; e.at.dText = +t.toFixed(2); }
      if (r.contrast < e.contrastMin) { e.contrastMin = r.contrast; e.at.contrast = +t.toFixed(2); }
      agg.set(r.s, e);
    }
  }
  const sc = [...agg.values()];
  const lg = await page.evaluate(() => APP.log());
  const log = { frame: F, frames: N, filmSeconds: N / 30, wallSeconds: +wall.toFixed(1), machineSecPerFilmSec: +(wall / (N / 30)).toFixed(2),
    stripTimes: meta.strip, cpus: os.cpus().length, date: new Date().toISOString(),
    summary: { minDistTextToGraphicPx720: Math.min(99, ...sc.map((x) => x.dGraphicMin)), minDistTextToTextPx720: Math.min(99, ...sc.map((x) => x.dTextMin)),
      minContrast: Math.min(99, ...sc.map((x) => x.contrastMin)), minFontPx1080: Math.min(...lg.texts.map((x) => x.px)), outOfSafe: lg.texts.filter((x) => x.out).map((x) => x.s) },
    claimsUsed: lg.used, texts: lg.texts, selfCheck: sc };
  fs.mkdirSync(path.join(OUT, 'work'), { recursive: true });
  fs.writeFileSync(path.join(OUT, 'work', `render-log-${F}.json`), JSON.stringify(log, null, 1));
  console.error(F, 'wall', wall, 's', JSON.stringify(log.summary), 'claims', lg.used.join(','));
  await browser.close(); srv.close();
})().catch((e) => { console.error(e); process.exit(1); });
