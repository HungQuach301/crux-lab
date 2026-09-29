'use strict';
// H2 renderer: headless Chromium (Playwright) screenshots every frame of stage.html?f=<F> at 1280x720, 30 fps;
// PyAV (encode.py) encodes H.264. Also writes the 6-frame strip (1920x220) and the poster PNG.
//   NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node render.js F1 [--frames-dir d] [--only-stills]
// Weekly rates are read at render time from the local FRED file (episodes/ep001/data/normalized/mortgage30_weekly.csv,
// rebuilt by fetch.py --verify); they are not stored in this directory (repo is public; RIGHTS.md D-FRED-1, DL: no).
const fs = require('fs');
const path = require('path');
const os = require('os');
const { execFileSync } = require('child_process');
const { chromium } = require('playwright');

const F = process.argv[2] || 'F1';
const argv = process.argv.slice(3);
const opt = (k, d) => { const i = argv.indexOf('--' + k); return i >= 0 ? argv[i + 1] : d; };
const ONLY_STILLS = argv.includes('--only-stills');
const HERE = __dirname;
const OUT = path.resolve(HERE, '..');
const REPO = path.resolve(HERE, '../../../../../..');
const FRAMES = opt('frames-dir', path.join(os.tmpdir(), 'h2-frames', F));
const FPS = 30;
// strip times (6 frames) and poster time, per frame — chosen at the meaning beats (intent.md)
const PLAN = {
  F1: { strip: [0.9, 2.6, 4.3, 5.8, 7.4, 8.8], poster: 8.8 },
  F2: { strip: [1.2, 2.6, 5.0, 6.2, 7.6, 9.6], poster: 9.6 },
  F3: { strip: [1.0, 2.6, 4.6, 6.6, 7.8, 9.3], poster: 9.3 },
};

function weekly() {
  const f = path.join(REPO, 'episodes/ep001/data/normalized/mortgage30_weekly.csv');
  if (!fs.existsSync(f)) throw new Error('missing ' + f + ' — run: python3 episodes/ep001/data/fetch.py --verify');
  return fs.readFileSync(f, 'utf8').trim().split('\n').slice(1).map((l) => l.split(','));
}

(async () => {
  const t0 = Date.now();
  const browser = await chromium.launch({ args: ['--disable-gpu', '--font-render-hinting=none', '--disable-lcd-text'] });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
  page.on('pageerror', (e) => console.error('pageerror', e.message));
  page.on('console', (m) => console.log('page:', m.text()));
  await page.goto('file://' + path.join(HERE, 'stage.html') + '?f=' + F);
  await page.waitForFunction(() => window.SCENE && window.SCENE.build);
  await page.evaluate(async (D) => {
    await document.fonts.load('700 40px Inter'); await document.fonts.load('600 40px Inter'); await document.fonts.load('400 40px Inter');
    await document.fonts.ready; window.SCENE.build(D);
  }, { weekly: weekly() });
  const dur = await page.evaluate(() => window.SCENE.dur);
  const shot = async (t, file) => { await page.evaluate((t) => window.setT(t), t); await page.screenshot({ path: file, type: 'png' }); };

  const plan = PLAN[F];
  const sdir = path.join(FRAMES, 'stills');
  fs.mkdirSync(sdir, { recursive: true });
  for (let i = 0; i < plan.strip.length; i++) await shot(plan.strip[i], path.join(sdir, `s${i + 1}.png`));
  await shot(plan.poster, path.join(OUT, `${F}-poster.png`));
  // strip: 6 frames of 320x180 on a 1920x220 sheet, numbered 1-6 with their time
  const sp = await browser.newPage({ viewport: { width: 1920, height: 220 }, deviceScaleFactor: 1 });
  const cells = plan.strip.map((t, i) => `<div class="c"><img src="data:image/png;base64,${fs.readFileSync(path.join(sdir, `s${i + 1}.png`)).toString('base64')}"><div class="n">${i + 1}</div><div class="l">${i + 1} · ${t.toFixed(1)} s</div></div>`).join('');
  await sp.setContent(`<html><head><style>
    @font-face{font-family:Inter;font-weight:700;src:url(data:font/woff2;base64,${fs.readFileSync(path.join(REPO, 'toolkit/render/fonts/inter-latin-700-normal.woff2')).toString('base64')})}
    body{margin:0;background:#0e1116;width:1920px;height:220px;display:flex;font-family:Inter}
    .c{position:relative;width:320px;height:220px}.c img{width:320px;height:180px;display:block}
    .n{position:absolute;left:8px;top:8px;width:34px;height:34px;border-radius:50%;background:#f2f4f7;color:#0e1116;font:700 22px Inter;text-align:center;line-height:34px}
    .l{color:#f2f4f7;font:700 20px Inter;text-align:center;line-height:40px}</style></head><body>${cells}</body></html>`);
  await sp.evaluate(async () => { await document.fonts.ready; await Promise.all([...document.images].map((i) => i.decode())); });
  await sp.screenshot({ path: path.join(OUT, `${F}-strip.png`) });
  await sp.close();
  if (ONLY_STILLS) { await browser.close(); console.log('stills done'); return; }

  const n = Math.round(dur * FPS);
  const fdir = path.join(FRAMES, 'seq');
  fs.rmSync(fdir, { recursive: true, force: true });
  fs.mkdirSync(fdir, { recursive: true });
  const tr0 = Date.now();
  for (let i = 0; i < n; i++) await shot(i / FPS, path.join(fdir, `f${String(i).padStart(4, '0')}.png`));
  const tCapture = (Date.now() - tr0) / 1000;
  await browser.close();
  const te0 = Date.now();
  execFileSync('python3', [path.join(HERE, 'encode.py'), fdir, path.join(OUT, `${F}.mp4`), String(FPS), '26'], { stdio: 'inherit' });
  const tEncode = (Date.now() - te0) / 1000;
  const total = (Date.now() - t0) / 1000;
  const rec = { frame: F, seconds: dur, frames: n, captureSec: +tCapture.toFixed(1), encodeSec: +tEncode.toFixed(1), totalSec: +total.toFixed(1),
    secPerFilmSecond: +(total / dur).toFixed(2), cpus: os.cpus().length, when: new Date().toISOString() };
  fs.writeFileSync(path.join(OUT, `src/timing-${F}.json`), JSON.stringify(rec, null, 1) + '\n');
  console.log(JSON.stringify(rec));
})().catch((e) => { console.error(e); process.exit(1); });
