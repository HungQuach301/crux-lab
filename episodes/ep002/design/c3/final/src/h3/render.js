'use strict';
// Ep002 final renderer for the H3-based beats (copied from ../../../H3/src/render.js; output to final/): Chromium headless (Playwright), canvas 2D, CPU only; raw RGBA -> ffmpeg (libx264, yuv420p, BT.709).
//   NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node render.js K1 [--still t1,t2] [--no-video]
// Writes ../K1.mp4, ../K1-strip.png, ../K1-strip-masked.png, ../work/render-log-K1.json (timing, claims, texts, self-check).
const fs = require('fs'), path = require('path'), http = require('http'), os = require('os'), { spawn } = require('child_process');
const { chromium } = require('playwright');
const HERE = __dirname, OUT = path.resolve(HERE, '../..'), REPO = path.resolve(HERE, '../../../../../../..');
const args = process.argv.slice(2), K = args[0];
const opt = (k) => { const i = args.indexOf('--' + k); return i >= 0 ? args[i + 1] : null; };
const types = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json', '.woff2': 'font/woff2' };
const srv = http.createServer((q, r) => {
  const f = path.join(REPO, decodeURIComponent(q.url.split('?')[0]));
  if (!f.startsWith(REPO)) { r.writeHead(403); r.end(); return; }
  fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); return; } r.writeHead(200, { 'content-type': types[path.extname(f)] || 'application/octet-stream' }); r.end(d); });
});
const savePng = (file, dataUrl) => { fs.mkdirSync(path.dirname(file), { recursive: true }); fs.writeFileSync(file, Buffer.from(dataUrl.split(',')[1], 'base64')); };
(async () => {
  await new Promise((res) => srv.listen(0, res));
  const browser = await chromium.launch({ args: ['--disable-gpu', '--font-render-hinting=none'] });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
  page.on('pageerror', (e) => { console.error('pageerror', e.message); process.exit(1); });
  page.on('console', (m) => { if (m.type() === 'error') console.error('console', m.text()); });
  await page.goto(`http://127.0.0.1:${srv.address().port}/episodes/ep002/design/c3/final/src/h3/page.html?k=${K}`);
  await page.waitForFunction(() => window.READY === true, null, { timeout: 120000 });
  const meta = await page.evaluate(() => ({ d: APP.duration, n: APP.frames, strip: APP.stripTimes }));
  if (args.includes('--thumb')) { // concept thumbnail 1280x720 + text boxes in 1280 px
    savePng(path.join(OUT, 'thumb-concept.png'), await page.evaluate(() => APP.png(0)));
    const bx = await page.evaluate(() => APP.boxes(0));
    const r = (a) => a.map((x) => +(x * 2 / 3).toFixed(1));
    fs.writeFileSync(path.join(OUT, 'thumb-concept.json'), JSON.stringify({ size: [1280, 720], texts: bx.map((b) => ({ text: b.s, box: r(b.glyph), fontPx: +(b.px * 2 / 3).toFixed(1), ...(b.box[2] !== b.glyph[2] ? { plateBox: r(b.box) } : {}) })) }, null, 1));
    const chk = await page.evaluate(() => APP.check(0)); console.error(JSON.stringify(chk));
    await browser.close(); srv.close(); return;
  }
  if (opt('still')) {
    for (const t of opt('still').split(',').map(Number)) {
      savePng(path.join(OUT, 'work', `${K}-still-${t.toFixed(2)}.png`), await page.evaluate((t) => APP.png(t), t));
      if (args.includes('--masked')) { await page.evaluate(() => APP.setMask(true)); savePng(path.join(OUT, 'work', `${K}-still-${t.toFixed(2)}-m.png`), await page.evaluate((t) => APP.png(t), t)); await page.evaluate(() => APP.setMask(false)); }
    }
    await browser.close(); srv.close(); return;
  }
  const N = meta.n, t0 = Date.now();
  if (!args.includes('--no-video')) {
    const enc = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgba', '-s', '1280x720', '-r', '30', '-i', '-',
      '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-profile:v', 'high',
      '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', '-movflags', '+faststart', '-an', path.join(OUT, `${K}.mp4`)], { stdio: ['pipe', 'inherit', 'inherit'] });
    const done = new Promise((res, rej) => enc.on('close', (c) => (c ? rej(new Error('ffmpeg ' + c)) : res())));
    for (let f = 0; f < N; f++) {
      const b64 = await page.evaluate((t) => APP.frame(t), f / 30);
      if (!enc.stdin.write(Buffer.from(b64, 'base64'))) await new Promise((r) => enc.stdin.once('drain', r));
    }
    enc.stdin.end(); await done;
  }
  const wall = (Date.now() - t0) / 1000;
  savePng(path.join(OUT, `${K}-strip.png`), await page.evaluate((ts) => APP.strip(ts, false), meta.strip));
  savePng(path.join(OUT, `${K}-strip-masked.png`), await page.evaluate((ts) => APP.strip(ts, true), meta.strip));
  // self-check every 3rd frame
  const chk = [];
  for (let f = 0; f < N; f += 3) chk.push(...(await page.evaluate((t) => APP.check(t), f / 30)).map((r) => ({ t: +(f / 30).toFixed(2), ...r })));
  const lg = await page.evaluate(() => APP.log());
  const minOf = (k) => chk.reduce((m, r) => (r[k] < m[k] ? r : m), chk[0] || { [k]: null });
  const log = { clip: K, frames: N, filmSeconds: N / 30, wallSeconds: +wall.toFixed(1), machineSecPerFilmSec: +(wall / (N / 30)).toFixed(2),
    cpus: os.cpus().length, cpuModel: os.cpus()[0].model, date: new Date().toISOString(), stripTimes: meta.strip,
    claimsUsed: lg.used, texts: lg.texts, minPx1080: Math.min(...lg.texts.map((x) => x.px)),
    checkSamples: chk.length, worstClear: minOf('clear'), worstTextClear: minOf('tclear'), worstContrast: minOf('contrast') };
  fs.mkdirSync(path.join(OUT, 'work'), { recursive: true });
  fs.writeFileSync(path.join(OUT, 'work', `render-log-${K}.json`), JSON.stringify(log, null, 1));
  console.error(K, 'wall', wall.toFixed(1), 's; x', log.machineSecPerFilmSec, '; clear', log.worstClear, '; tclear', log.worstTextClear, '; contrast', log.worstContrast);
  await browser.close(); srv.close();
})().catch((e) => { console.error(e); process.exit(1); });
