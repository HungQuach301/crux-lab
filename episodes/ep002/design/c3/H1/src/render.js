'use strict';
// C3 Tập 2 · H1 renderer: Chromium headless (Playwright) + SwiftShader (software WebGL, CPU only); raw RGBA -> encode.py
// (PyAV libx264, H.264 High yuv420p). 1280x720, 30 fps, no audio.
//   THREE_DIR=<tmp>/node_modules/three/build NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers \
//   node src/render.js K1 [--still 1,4.5 [--mask]] [--strips-only]
// Writes K1.mp4, K1-strip.png, K1-strip-masked.png, work/render-log-K1.json (timings, claims, strings, D2/D4/G-014 audit).
//   node src/render.js THUMB  -> thumb-concept.png + thumb-concept.json (+ work/thumb-concept-masked.png)
const fs = require('fs'), path = require('path'), http = require('http'), os = require('os'), { spawn } = require('child_process');
const { chromium } = require('playwright');
const HERE = __dirname, OUT = path.resolve(HERE, '..'), REPO = path.resolve(HERE, '../../../../../..');
const TOKENS = path.join(REPO, 'episodes/ep001/design/c3/final/tokens.json');
const THREE_DIR = process.env.THREE_DIR || path.join(process.cwd(), 'node_modules/three/build');
const args = process.argv.slice(2), F = args[0];
const opt = (k) => { const i = args.indexOf('--' + k); return i >= 0 ? args[i + 1] : null; };
const types = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json', '.woff2': 'font/woff2' };
const srv = http.createServer((q, r) => {
  const u = decodeURIComponent(q.url.split('?')[0]);
  const f = u === '/tokens.json' ? TOKENS : u.startsWith('/three/') ? path.join(THREE_DIR, u.slice(7)) : u.startsWith('/fonts/') ? path.join(REPO, 'toolkit/render/fonts', u.slice(7)) : path.join(OUT, u);
  fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); return; } r.writeHead(200, { 'content-type': types[path.extname(f)] || 'application/octet-stream' }); r.end(d); });
});
const lum = (h) => { const c = [1, 3, 5].map((i) => parseInt(h.slice(i, i + 2), 16) / 255).map((v) => (v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4))); return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]; };
const contrast = (a, b) => { const x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); };
(async () => {
  await new Promise((res) => srv.listen(0, res));
  const port = srv.address().port;
  const browser = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--disable-gpu', '--font-render-hinting=none'] });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
  page.on('pageerror', (e) => { console.error('pageerror', e.message); process.exit(1); });
  page.on('console', (m) => { if (m.type() === 'error' || m.type() === 'log') console.error('console', m.text()); });
  await page.goto(`http://127.0.0.1:${port}/src/page.html?f=${F.toLowerCase()}`);
  await page.waitForFunction(() => window.READY === true, null, { timeout: 180000 });
  const meta = await page.evaluate(() => ({ d: APP.duration, n: APP.frames, strip: APP.stripTimes, gpu: APP.info() }));
  console.error(F, meta);
  const savePng = (file, dataUrl) => { fs.mkdirSync(path.dirname(file), { recursive: true }); fs.writeFileSync(file, Buffer.from(dataUrl.split(',')[1], 'base64')); };
  if (opt('still')) {
    const mask = args.includes('--mask');
    for (const t of opt('still').split(',').map(Number)) savePng(path.join(OUT, 'work', `${F}-still-${t.toFixed(2)}${mask ? '-m' : ''}.png`), await page.evaluate(([t, m]) => APP.png(t, m), [t, mask]));
    await browser.close(); srv.close(); return;
  }
  // ---- audit (D2 contrast on plate, D4 spacing, G-014 size) every 1/6 s
  const audit = [];
  for (let t = 0; t <= meta.d - 1 / 30 + 1e-9; t += 1 / 6) for (const r of await page.evaluate((t) => APP.audit(t), t)) audit.push({ t: +t.toFixed(2), ...r, contrast: +contrast(r.color, r.plate).toFixed(2) });
  const minBy = (k) => audit.reduce((m, r) => (r[k] !== null && (m === null || r[k] < m[k]) ? r : m), null);
  const summary = audit.length ? { samples: audit.length, minToGraphics: minBy('toGraphics'), minToText: minBy('toText'), minContrast: minBy('contrast'), minPx: minBy('px') } : { samples: 0 };
  if (F === 'THUMB') {
    const t = meta.d - 1 / 30;
    savePng(path.join(OUT, 'thumb-concept.png'), await page.evaluate((t) => APP.png(t), t));
    savePng(path.join(OUT, 'work', 'thumb-concept-masked.png'), await page.evaluate((t) => APP.png(t, true), t));
    const boxes = await page.evaluate((t) => APP.boxes(t), t);
    fs.writeFileSync(path.join(OUT, 'thumb-concept.json'), JSON.stringify({ size: [1280, 720], texts: boxes, audit: summary }, null, 1));
    console.error(JSON.stringify(summary)); await browser.close(); srv.close(); return;
  }
  if (!args.includes('--strips-only')) {
    const N = meta.n;
    const enc = spawn('python3', [path.join(HERE, 'encode.py'), path.join(OUT, `${F}.mp4`), '1280', '720', '30', '20'], { stdio: ['pipe', 'inherit', 'inherit'] });
    const done = new Promise((res, rej) => enc.on('close', (c) => (c ? rej(new Error('encode ' + c)) : res())));
    const t0 = Date.now();
    for (let f = 0; f < N; f++) {
      const b64 = await page.evaluate((t) => APP.frame(t), f / 30);
      if (!enc.stdin.write(Buffer.from(b64, 'base64'))) await new Promise((r) => enc.stdin.once('drain', r));
      if (f % 60 === 0) console.error(`${F} frame ${f}/${N} ${((Date.now() - t0) / (f + 1)).toFixed(0)} ms/frame`);
    }
    enc.stdin.end(); await done;
    var wall = (Date.now() - t0) / 1000;
  }
  savePng(path.join(OUT, `${F}-strip.png`), await page.evaluate((ts) => APP.strip(ts, false), meta.strip));
  savePng(path.join(OUT, `${F}-strip-masked.png`), await page.evaluate((ts) => APP.strip(ts, true), meta.strip));
  const lg = await page.evaluate(() => APP.log());
  const logf = path.join(OUT, 'work', `render-log-${F}.json`);
  const prev = fs.existsSync(logf) ? JSON.parse(fs.readFileSync(logf)) : {};
  const log = { frame: F, frames: meta.n, filmSeconds: meta.n / 30, wallSeconds: wall ? +wall.toFixed(1) : prev.wallSeconds,
    machineSecPerFilmSec: wall ? +(wall / (meta.n / 30)).toFixed(2) : prev.machineSecPerFilmSec, stripTimes: meta.strip,
    renderer: meta.gpu, cpus: os.cpus().length, cpuModel: os.cpus()[0].model, date: new Date().toISOString(),
    claimsUsed: lg.used, texts: lg.texts, audit: summary };
  fs.mkdirSync(path.dirname(logf), { recursive: true }); fs.writeFileSync(logf, JSON.stringify(log, null, 1));
  console.error(F, 'wall', wall, 's; x', log.machineSecPerFilmSec, JSON.stringify(summary), 'out-of-safe:', lg.texts.filter((x) => x.out).map((x) => x.s));
  await browser.close(); srv.close();
})().catch((e) => { console.error(e); process.exit(1); });
