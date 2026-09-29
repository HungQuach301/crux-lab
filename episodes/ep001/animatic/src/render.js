'use strict';
// C4 animatic renderer (from C3 final render.js): Chromium headless (Playwright) + SwiftShader (CPU WebGL) for H1,
// canvas 2D for H3; raw RGBA 1280x720 -> encode.py (PyAV libx264). No ffmpeg binary.
//   THREE_DIR=<node_modules/three/build> NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers \
//   node render.js S01 [--still t1,t2] [--strip-only]
// Writes ../work/scenes/S01.mp4 (video only), ../strips/S01.png (blind strip, no sentence captions),
// ../work/S01-hard.png (frame for the 25% check) and ../work/logs/S01.json (timings, claims, strings, anchors).
const fs = require('fs'), path = require('path'), http = require('http'), os = require('os'), { spawn } = require('child_process');
const { chromium } = require('playwright');
const HERE = __dirname, AN = path.resolve(HERE, '..'), REPO = path.resolve(HERE, '../../../..');
const THREE_DIR = process.env.THREE_DIR || path.join(process.cwd(), 'node_modules/three/build');
const args = process.argv.slice(2), F = args[0];
const opt = (k) => { const i = args.indexOf('--' + k); return i >= 0 ? args[i + 1] : null; };
const types = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json', '.woff2': 'font/woff2' };
const srv = http.createServer((q, r) => {
  const u = decodeURIComponent(q.url.split('?')[0]);
  const f = u.startsWith('/three/') ? path.join(THREE_DIR, u.slice(7)) : u.startsWith('/fonts/') ? path.join(REPO, 'toolkit/render/fonts', u.slice(7)) : path.join(AN, u);
  fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); return; } r.writeHead(200, { 'content-type': types[path.extname(f)] || 'application/octet-stream' }); r.end(d); });
});
(async () => {
  await new Promise((res) => srv.listen(0, res));
  const port = srv.address().port;
  const browser = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--disable-gpu', '--font-render-hinting=none'] });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
  page.on('pageerror', (e) => { console.error('pageerror', F, e.message); process.exit(1); });
  page.on('console', (m) => { if (m.type() === 'error') console.error('console', F, m.text()); });
  await page.goto(`http://127.0.0.1:${port}/src/page.html?s=${F}`);
  await page.waitForFunction(() => window.READY === true, null, { timeout: 120000 });
  const meta = await page.evaluate(() => ({ d: APP.duration, n: APP.frames, strip: APP.stripTimes, hard: APP.hardTime, gpu: APP.info() }));
  console.error(F, JSON.stringify(meta));
  const savePng = (file, dataUrl) => { fs.mkdirSync(path.dirname(file), { recursive: true }); fs.writeFileSync(file, Buffer.from(dataUrl.split(',')[1], 'base64')); };
  if (opt('still')) {
    for (const t of opt('still').split(',').map(Number)) savePng(path.join(AN, 'work', 'stills', `${F}-${t.toFixed(2)}.png`), await page.evaluate((t) => APP.png(t), t));
    await browser.close(); srv.close(); return;
  }
  if (args.includes('--strip-only')) {
    savePng(path.join(AN, 'strips', `${F}.png`), await page.evaluate((ts) => APP.strip(ts), meta.strip));
    savePng(path.join(AN, 'work', `${F}-hard.png`), await page.evaluate((t) => APP.png(t), meta.hard));
    await browser.close(); srv.close(); return;
  }
  const N = meta.n;
  fs.mkdirSync(path.join(AN, 'work', 'scenes'), { recursive: true });
  const enc = spawn('python3', [path.join(HERE, 'encode.py'), path.join(AN, 'work', 'scenes', `${F}.mp4`), '1280', '720', '30', '18'], { stdio: ['pipe', 'inherit', 'inherit'] });
  const done = new Promise((res, rej) => enc.on('close', (c) => (c ? rej(new Error('encode ' + c)) : res())));
  const t0 = Date.now(); let tb = 0, n3 = 0;
  for (let f = 0; f < N; f++) {
    const s = Date.now();
    const [b64, m] = await page.evaluate((t) => [APP.frame(t), APP.modeAt(t)], f / 30);
    if (m === '3d') n3++;
    tb += Date.now() - s;
    if (!enc.stdin.write(Buffer.from(b64, 'base64'))) await new Promise((r) => enc.stdin.once('drain', r));
    if (f % 150 === 0) console.error(`${F} frame ${f}/${N} ${((Date.now() - t0) / (f + 1)).toFixed(0)} ms/frame`);
  }
  enc.stdin.end(); await done;
  const wall = (Date.now() - t0) / 1000;
  savePng(path.join(AN, 'strips', `${F}.png`), await page.evaluate((ts) => APP.strip(ts), meta.strip));
  savePng(path.join(AN, 'work', `${F}-hard.png`), await page.evaluate((t) => APP.png(t), meta.hard));
  const lg = await page.evaluate(() => APP.log());
  const log = { scene: F, frames: N, frames3d: n3, filmSeconds: N / 30, wallSeconds: +wall.toFixed(1), browserFrameSeconds: +(tb / 1000).toFixed(1),
    machineSecPerFilmSec: +(wall / (N / 30)).toFixed(2), hardTime: meta.hard, stripTimes: meta.strip,
    renderer: meta.gpu, cpus: os.cpus().length, cpuModel: os.cpus()[0].model, date: new Date().toISOString(), ...lg, claimsUsed: lg.used };
  delete log.used;
  fs.mkdirSync(path.join(AN, 'work', 'logs'), { recursive: true });
  fs.writeFileSync(path.join(AN, 'work', 'logs', `${F}.json`), JSON.stringify(log, null, 1));
  console.error(F, 'wall', wall, 's; x', log.machineSecPerFilmSec, '; out-of-safe:', lg.texts.filter((x) => x.out).map((x) => x.s), '; kw missing:', lg.anchorsKeywordMissing);
  await browser.close(); srv.close();
})().catch((e) => { console.error(e); process.exit(1); });
