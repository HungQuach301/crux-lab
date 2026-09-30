'use strict';
// H3 driver: headless Chromium (Playwright, CPU) draws each frame on a 2D canvas; raw RGBA goes to encode.py (PyAV).
//   NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node render.js [F1 F2 F3]
const fs = require('fs'), path = require('path'), { spawn } = require('child_process');
const { chromium } = require('playwright');
const OUT = path.resolve(__dirname, '..'), FPS = 30;
// strip times (s) chosen to show each beat named in intent.md
const STRIP = { F1: [0.9, 1.9, 3.0, 4.4, 6.9, 8.6], F2: [1.0, 2.3, 4.0, 5.4, 6.3, 9.3], F3: [1.3, 2.3, 4.2, 5.6, 6.4, 9.5] };
const POSTER = { F1: 8.6, F2: 9.3, F3: 9.5 };
(async () => {
  const ids = process.argv.slice(2).length ? process.argv.slice(2) : ['F1', 'F2', 'F3'];
  const browser = await chromium.launch({ args: ['--disable-gpu', '--font-render-hinting=none'] });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
  page.on('pageerror', (e) => { console.error('pageerror', e.message); process.exit(1); });
  await page.goto('file://' + path.join(__dirname, 'frames.html'));
  await page.evaluate(async () => { for (const w of [400, 600, 700]) await document.fonts.load(`${w} 20px Inter`); await document.fonts.ready; });
  const log = {};
  for (const id of ids) {
    const dur = await page.evaluate((id) => window.H3.SCENES[id].dur, id);
    const n = Math.round(dur * FPS), file = path.join(OUT, id + '.mp4');
    const t0 = Date.now();
    const enc = spawn('python3', [path.join(__dirname, 'encode.py'), file, '1280', '720', String(FPS)], { stdio: ['pipe', 'inherit', 'inherit'] });
    const done = new Promise((res, rej) => enc.on('close', (c) => (c ? rej(new Error('encode ' + c)) : res())));
    for (let f = 0; f < n; f++) {
      const b64 = await page.evaluate(([id, t]) => window.H3.frameB64(id, t), [id, f / FPS]);
      if (!enc.stdin.write(Buffer.from(b64, 'base64'))) await new Promise((r) => enc.stdin.once('drain', r));
    }
    enc.stdin.end(); await done;
    const wall = (Date.now() - t0) / 1000;
    const save = async (name, url) => fs.writeFileSync(path.join(OUT, name), Buffer.from(url.split(',')[1], 'base64'));
    await save(id + '-strip.png', await page.evaluate(([id, ts]) => window.H3.strip(id, ts), [id, STRIP[id]]));
    await save(id + '-poster.png', await page.evaluate(([id, t]) => window.H3.png(id, t), [id, POSTER[id]]));
    log[id] = { seconds: dur, frames: n, wallSeconds: +wall.toFixed(1), secPerFilmSec: +(wall / dur).toFixed(2), bytes: fs.statSync(file).size, strip: STRIP[id], poster: POSTER[id] };
    console.log(id, JSON.stringify(log[id]));
  }
  await browser.close();
  const lf = path.join(OUT, 'render-log.json');
  const prev = fs.existsSync(lf) ? JSON.parse(fs.readFileSync(lf, 'utf8')) : {};
  fs.writeFileSync(lf, JSON.stringify({ ...prev, ...log, machine: `${require('os').cpus().length} CPU, no GPU, Chromium headless + PyAV libx264` }, null, 1));
})().catch((e) => { console.error(e); process.exit(1); });
