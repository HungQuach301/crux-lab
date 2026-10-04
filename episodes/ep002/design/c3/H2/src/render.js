'use strict';
// H2 renderer: Chromium headless (Playwright), canvas 2D only (CPU), raw RGBA -> ffmpeg libx264 (yuv420p, BT.709).
//   NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node src/render.js K1 [--still t1,t2] [--strip-only] [--thumb]
// Writes ../K1.mp4, ../K1-strip.png, ../K1-strip-masked.png, ../render-log-K1.json (timing, claim IDs, every string,
// self-check over every 3rd frame: text-to-graphics distance, text-to-text distance, local contrast, min font px).
const fs = require('fs'), path = require('path'), http = require('http'), os = require('os'), { spawn } = require('child_process');
const { chromium } = require('playwright');
const HERE = __dirname, OUT = path.resolve(HERE, '..'), REPO = path.resolve(HERE, '../../../../../..');
const args = process.argv.slice(2), F = args[0];
const opt = (k) => { const i = args.indexOf('--' + k); return i >= 0 ? args[i + 1] : null; };
const types = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json', '.woff2': 'font/woff2' };
const srv = http.createServer((q, r) => {
  const u = decodeURIComponent(q.url.split('?')[0]);
  const f = u === '/tokens.json' ? path.join(REPO, 'episodes/ep001/design/c3/final/tokens.json') : u.startsWith('/fonts/') ? path.join(REPO, 'toolkit/render/fonts', u.slice(7)) : path.join(OUT, u);
  fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); return; } r.writeHead(200, { 'content-type': types[path.extname(f)] || 'application/octet-stream' }); r.end(d); });
});
const savePng = (file, dataUrl) => { fs.mkdirSync(path.dirname(file), { recursive: true }); fs.writeFileSync(file, Buffer.from(dataUrl.split(',')[1], 'base64')); };
(async () => {
  await new Promise((res) => srv.listen(0, res));
  const port = srv.address().port;
  const browser = await chromium.launch({ args: ['--disable-gpu', '--font-render-hinting=none'] });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
  page.on('pageerror', (e) => { console.error('pageerror', e.message); process.exit(1); });
  page.on('console', (m) => { if (m.type() === 'error') console.error('console', m.text()); });
  await page.goto(`http://127.0.0.1:${port}/src/page.html?f=${F.toLowerCase()}`);
  await page.waitForFunction(() => window.READY === true, null, { timeout: 120000 });
  const meta = await page.evaluate(() => ({ d: APP.duration, n: APP.frames, strip: APP.stripTimes, json: APP.json ? APP.json : null }));
  console.error(F, meta);
  if (opt('still')) {
    for (const t of opt('still').split(',').map(Number)) {
      savePng(path.join(OUT, 'work', `${F}-still-${t.toFixed(2)}.png`), await page.evaluate((t) => APP.png(t), t));
      if (args.includes('--masked')) savePng(path.join(OUT, 'work', `${F}-still-${t.toFixed(2)}-m.png`), await page.evaluate((t) => APP.png(t, { mask: true }), t));
    }
    await browser.close(); srv.close(); return;
  }
  if (args.includes('--thumb')) {
    savePng(path.join(OUT, 'thumb-concept.png'), await page.evaluate(() => APP.png(0)));
    savePng(path.join(OUT, 'work', 'thumb-masked.png'), await page.evaluate(() => APP.png(0, { mask: true })));
    const tx = await page.evaluate(() => APP.texts(0));
    const chk = await page.evaluate(() => APP.check(0));
    fs.writeFileSync(path.join(OUT, 'thumb-concept.json'), JSON.stringify({ size: [1280, 720], texts: tx.map((x) => ({ text: x.s, box: x.box, fontPx: +(x.px * 2 / 3).toFixed(1), fontPx1080: x.px })), selfCheck: chk }, null, 1));
    await browser.close(); srv.close(); return;
  }
  const strips = async () => {
    savePng(path.join(OUT, `${F}-strip.png`), await page.evaluate((ts) => APP.strip(ts, false), meta.strip));
    savePng(path.join(OUT, `${F}-strip-masked.png`), await page.evaluate((ts) => APP.strip(ts, true), meta.strip));
  };
  if (args.includes('--strip-only')) { await strips(); await browser.close(); srv.close(); return; }
  if (args.includes('--badge-check')) { // distance from the ILLUSTRATIVE pill to any graphic, every 3rd frame
    let m = 99, at = 0;
    for (let f = 0; f < meta.n; f += 3) for (const c of await page.evaluate((t) => APP.check(t), f / 30)) if (c.s === 'ILLUSTRATIVE' && c.dGraphic < m) { m = c.dGraphic; at = f / 30; }
    console.log(F, 'badge pill min distance to graphics (px @720):', m, 'at', at.toFixed(2)); await browser.close(); srv.close(); return;
  }
  const N = meta.n;
  const enc = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgba', '-s', '1280x720', '-r', '30', '-i', '-', '-an',
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709',
    '-movflags', '+faststart', path.join(OUT, `${F}.mp4`)], { stdio: ['pipe', 'inherit', 'inherit'] });
  const done = new Promise((res, rej) => enc.on('close', (c) => (c ? rej(new Error('encode ' + c)) : res())));
  const t0 = Date.now();
  for (let f = 0; f < N; f++) {
    const b64 = await page.evaluate((t) => APP.frame(t), f / 30);
    if (!enc.stdin.write(Buffer.from(b64, 'base64'))) await new Promise((r) => enc.stdin.once('drain', r));
  }
  enc.stdin.end(); await done;
  const wall = (Date.now() - t0) / 1000;
  await strips();
  // self-check on every 3rd frame
  const checks = {};
  for (let f = 0; f < N; f += 3) {
    for (const c of await page.evaluate((t) => APP.check(t), f / 30)) {
      const e = checks[c.s] || { s: c.s, px: c.px, dGraphicMin: 99, dTextMin: 99, contrastMin: 99, at: {} };
      if (c.dGraphic < e.dGraphicMin) { e.dGraphicMin = c.dGraphic; e.at.dGraphic = +(f / 30).toFixed(2); }
      if (c.dText < e.dTextMin) { e.dTextMin = c.dText; e.at.dText = +(f / 30).toFixed(2); }
      if (c.contrast < e.contrastMin) { e.contrastMin = c.contrast; e.at.contrast = +(f / 30).toFixed(2); }
      checks[c.s] = e;
    }
  }
  const lg = await page.evaluate(() => APP.log());
  const cv = Object.values(checks);
  const log = { frame: F, frames: N, filmSeconds: N / 30, wallSeconds: +wall.toFixed(1), machineSecPerFilmSec: +(wall / (N / 30)).toFixed(2),
    stripTimes: meta.strip, cpus: os.cpus().length, cpuModel: os.cpus()[0].model, date: new Date().toISOString(),
    summary: { minDistTextToGraphicPx720: Math.min(...cv.map((x) => x.dGraphicMin)), minDistTextToTextPx720: Math.min(...cv.map((x) => x.dTextMin)),
      minContrast: Math.min(...cv.map((x) => x.contrastMin)), minFontPx1080: Math.min(...lg.texts.map((x) => x.px)), outOfSafe: lg.texts.filter((x) => x.out).map((x) => x.s) },
    claimsUsed: lg.used, texts: lg.texts, selfCheck: cv };
  fs.writeFileSync(path.join(OUT, `render-log-${F}.json`), JSON.stringify(log, null, 1));
  console.error(F, 'wall', wall, 's; x', log.machineSecPerFilmSec, JSON.stringify(log.summary));
  await browser.close(); srv.close();
})().catch((e) => { console.error(e); process.exit(1); });
