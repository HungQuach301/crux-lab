'use strict';
// H1 renderer: Chromium headless + SwiftShader (software WebGL, CPU only) renders three.js frames; PyAV encodes.
//   THREE_DIR=<node_modules/three/build> node render.js F1 [--still t] [--frames a:b]
// Writes ../F1.mp4, ../F1-strip.png, ../F1-poster.png and ../render-log-F1.json (timings).
const fs = require('fs'), path = require('path'), http = require('http'), { spawn } = require('child_process');
const { chromium } = require('playwright');
const HERE = __dirname, OUT = path.resolve(HERE, '..'), REPO = path.resolve(HERE, '../../../../../..');
const THREE_DIR = process.env.THREE_DIR || path.join(process.cwd(), 'node_modules/three/build');
const args = process.argv.slice(2), F = args[0];
const opt = (k) => { const i = args.indexOf('--' + k); return i >= 0 ? args[i + 1] : null; };
const types = { '.html': 'text/html', '.js': 'text/javascript', '.woff2': 'font/woff2' };
const srv = http.createServer((q, r) => {
  const u = decodeURIComponent(q.url.split('?')[0]);
  let f = u.startsWith('/three/') ? path.join(THREE_DIR, u.slice(7)) : u.startsWith('/fonts/') ? path.join(REPO, 'toolkit/render/fonts', u.slice(7)) : path.join(HERE, u.replace(/^\/src\//, '/'));
  fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); return; } r.writeHead(200, { 'content-type': types[path.extname(f)] || 'application/octet-stream' }); r.end(d); });
});
(async () => {
  await new Promise((res) => srv.listen(0, res));
  const port = srv.address().port;
  const browser = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--disable-gpu'] });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  page.on('pageerror', (e) => console.error('pageerror', e.message));
  page.on('console', (m) => { if (m.type() === 'error' || m.type() === 'warning') console.error('console', m.text()); });
  await page.goto(`http://127.0.0.1:${port}/src/page.html?f=${F.toLowerCase()}`);
  await page.waitForFunction(() => window.READY === true, null, { timeout: 60000 });
  const meta = await page.evaluate(() => ({ d: APP.duration, strip: APP.stripTimes, poster: APP.posterTime, gpu: APP.info() }));
  console.error(F, meta);
  const savePng = (file, dataUrl) => fs.writeFileSync(file, Buffer.from(dataUrl.split(',')[1], 'base64'));
  if (opt('still')) {
    for (const t of opt('still').split(',').map(Number)) savePng(path.join(process.env.STILL_DIR || OUT, `${F}-still-${t.toFixed(2)}.png`), await page.evaluate((t) => APP.png(t), t));
    await browser.close(); srv.close(); return;
  }
  if (args.includes('--strip-only')) {
    savePng(path.join(OUT, `${F}-strip.png`), await page.evaluate((ts) => APP.strip(ts), meta.strip));
    await browser.close(); srv.close(); return;
  }
  const N = Math.round(meta.d * 30);
  const [a, b] = opt('frames') ? opt('frames').split(':').map(Number) : [0, N];
  const enc = spawn('python3', [path.join(HERE, 'encode.py'), path.join(OUT, `${F}.mp4`)], { stdio: ['pipe', 'inherit', 'inherit'] });
  const done = new Promise((res) => enc.on('close', res));
  const t0 = Date.now(); let tb = 0;
  for (let f = a; f < b; f++) {
    const s = Date.now();
    const b64 = await page.evaluate((t) => APP.frame(t), f / 30);
    tb += Date.now() - s;
    const buf = Buffer.from(b64, 'base64');
    if (!enc.stdin.write(buf)) await new Promise((r) => enc.stdin.once('drain', r));
    if (f % 30 === 0) console.error(`${F} frame ${f}/${N} ${((Date.now() - t0) / (f - a + 1)).toFixed(0)} ms/frame`);
  }
  enc.stdin.end(); await done;
  const wall = (Date.now() - t0) / 1000;
  savePng(path.join(OUT, `${F}-strip.png`), await page.evaluate((ts) => APP.strip(ts), meta.strip));
  savePng(path.join(OUT, `${F}-poster.png`), await page.evaluate((t) => APP.png(t), meta.poster));
  const log = { frames: b - a, filmSeconds: (b - a) / 30, wallSeconds: wall, browserFrameSeconds: tb / 1000, machineSecPerFilmSec: wall / ((b - a) / 30), renderer: meta.gpu, cpus: require('os').cpus().length, cpuModel: require('os').cpus()[0].model, date: new Date().toISOString() };
  fs.writeFileSync(path.join(OUT, `render-log-${F}.json`), JSON.stringify(log, null, 1));
  console.error(log);
  await browser.close(); srv.close();
})().catch((e) => { console.error(e); process.exit(1); });
