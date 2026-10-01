'use strict';
// Tập 2 · C4 animatic renderer (canvas 2D, CPU only): Chromium headless (Playwright) -> raw RGBA -> ffmpeg libx264.
//   NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node render.js S01 [S02 ...] [--still t1,t2] [--mask]
//   ... node render.js --strips          (compose strips/KEY-n(-masked).png and strips/Sxx.png from work/stills)
// Scene S -> work/scenes/S.mp4 (exactly round(end*30)-round(start*30) frames), work/logs/S.json (claims, strings, anchors,
// self-check on every 6th frame + every strip frame), work/hard/S.png (frame with the most text, for the 25% check),
// work/stills/ (the scene's own 6 strip frames, and every KEY strip frame that falls inside the scene, plain + masked).
const fs = require('fs'), path = require('path'), http = require('http'), os = require('os'), { spawn } = require('child_process');
const { chromium } = require('playwright');
const HERE = __dirname, AN = path.resolve(HERE, '..'), REPO = path.resolve(AN, '../../..'), WK = path.join(AN, 'work');
const args = process.argv.slice(2), opt = (k) => { const i = args.indexOf('--' + k); return i >= 0 ? args[i + 1] : null; };
const scenes = args.filter((a, i) => /^S\d\d$/.test(a));
const types = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json', '.woff2': 'font/woff2', '.png': 'image/png' };
const srv = http.createServer((q, r) => {
  const u = decodeURIComponent(q.url.split('?')[0]);
  const f = u === '/tokens.json' ? path.join(REPO, 'episodes/ep002/design/c3/final/tokens.json') : u.startsWith('/fonts/') ? path.join(REPO, 'toolkit/render/fonts', u.slice(7)) : path.join(REPO, u);
  if (!f.startsWith(REPO)) { r.writeHead(403); r.end(); return; }
  fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); return; } r.writeHead(200, { 'content-type': types[path.extname(f)] || 'application/octet-stream' }); r.end(d); });
});
const timing = JSON.parse(fs.readFileSync(path.join(AN, 'timing.json'), 'utf8'));
// key beats (story/beats.md): sentence span of each KEY; 6 strip frames = centres of 6 equal slices of the span
const KEYS = { 'KEY-1': ['S01.2', 'S01.3'], 'KEY-2': ['S03.5', 'S03.8'], 'KEY-5': ['S04.1', 'S04.2'], 'KEY-3': ['S05.2', 'S05.4'], 'KEY-4': ['S06.1', 'S06.5'], 'KEY-6': ['S08.1', 'S08.7'], 'KEY-7': ['S09.4', 'S10.3'] };
const sentById = new Map(timing.scenes.flatMap((s) => s.sentences.map((x) => [x.id, x])));
const keyTimes = Object.fromEntries(Object.entries(KEYS).map(([k, [a, b]]) => { const t0 = sentById.get(a).start, t1 = sentById.get(b).end; return [k, { t0, t1, times: [0, 1, 2, 3, 4, 5].map((i) => +(t0 + (i + 0.5) * (t1 - t0) / 6).toFixed(3)) }]; }));
fs.mkdirSync(WK, { recursive: true }); fs.writeFileSync(path.join(WK, 'key-times.json'), JSON.stringify(keyTimes, null, 1));
for (const d of ['scenes', 'logs', 'hard', 'stills']) fs.mkdirSync(path.join(WK, d), { recursive: true });
const savePng = (file, dataUrl) => { fs.mkdirSync(path.dirname(file), { recursive: true }); fs.writeFileSync(file, Buffer.from(dataUrl.split(',')[1], 'base64')); };

async function renderScene(browser, port, S) {
  const sc = timing.scenes.find((x) => x.id === S);
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
  page.on('pageerror', (e) => { console.error('pageerror', S, e.message); process.exit(1); });
  page.on('console', (m) => { if (m.type() === 'error') console.error('console', S, m.text()); });
  await page.goto(`http://127.0.0.1:${port}/episodes/ep002/animatic/src/page.html?s=${S}`);
  await page.waitForFunction(() => window.READY === true, null, { timeout: 120000 });
  if (opt('still')) {
    for (const t of opt('still').split(',').map(Number)) savePng(path.join(WK, 'try', `${S}-${t.toFixed(2)}${args.includes('--mask') ? '-m' : ''}.png`), await page.evaluate(([t, m]) => APP.png(t, m), [t, args.includes('--mask')]));
    await page.close(); return;
  }
  const N = Math.round(sc.end * 30) - Math.round(sc.start * 30);
  const t0 = Date.now();
  const tmp = path.join(WK, 'scenes', `${S}.part.mp4`);
  const enc = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgba', '-s', '1280x720', '-r', '30', '-i', '-',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '16', '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-g', '60',
    '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', '-an', tmp], { stdio: ['pipe', 'inherit', 'inherit'] });
  const done = new Promise((res, rej) => enc.on('close', (c) => (c ? rej(new Error('ffmpeg ' + c)) : res())));
  for (let f = 0; f < N; f++) {
    const b64 = await page.evaluate((t) => APP.frame(t), f / 30);
    if (!enc.stdin.write(Buffer.from(b64, 'base64'))) await new Promise((r) => enc.stdin.once('drain', r));
  }
  enc.stdin.end(); await done; fs.renameSync(tmp, path.join(WK, 'scenes', `${S}.mp4`));
  const wall = (Date.now() - t0) / 1000;
  // stills: own 6 frames + KEY frames inside this scene
  const own = [0, 1, 2, 3, 4, 5].map((i) => +((i + 0.5) * sc.dur / 6).toFixed(3));
  for (const [i, t] of own.entries()) savePng(path.join(WK, 'stills', `${S}-own-${i + 1}.png`), await page.evaluate((t) => APP.png(t, false), t));
  const keyHere = [];
  for (const [k, v] of Object.entries(keyTimes)) v.times.forEach((ta, i) => { if (ta >= sc.start && ta < sc.end) keyHere.push([k, i, ta - sc.start]); });
  for (const [k, i, t] of keyHere) {
    savePng(path.join(WK, 'stills', `${k}-${i + 1}.png`), await page.evaluate((t) => APP.png(t, false), t));
    savePng(path.join(WK, 'stills', `${k}-${i + 1}-m.png`), await page.evaluate((t) => APP.png(t, true), t));
  }
  // self-check
  const times = [...new Set([...Array.from({ length: Math.ceil(N / 6) }, (_, i) => +((6 * i) / 30).toFixed(3)), ...own, ...keyHere.map((x) => +x[2].toFixed(3))])].sort((a, b) => a - b);
  const agg = new Map(); const badge = []; let hard = { t: 0, n: -1 };
  for (const t of times) {
    const r = await page.evaluate((t) => APP.check(t), t);
    if (r.badgeMissing) badge.push({ t, s: r.badgeMissing });
    const nch = r.res.reduce((a, x) => a + x.s.length, 0); if (nch > hard.n) hard = { t, n: nch };
    for (const x of r.res) {
      const e = agg.get(x.s) || { s: x.s, px: x.px, dGraphicMin: 99, dTextMin: 99, contrastMin: 99, at: {} };
      if (x.dGraphic < e.dGraphicMin) { e.dGraphicMin = x.dGraphic; e.at.dGraphic = t; }
      if (x.dText < e.dTextMin) { e.dTextMin = x.dText; e.at.dText = t; }
      if (x.contrast < e.contrastMin) { e.contrastMin = x.contrast; e.at.contrast = t; }
      agg.set(x.s, e);
    }
  }
  savePng(path.join(WK, 'hard', `${S}.png`), await page.evaluate((t) => APP.png(t, false), hard.t));
  const lg = await page.evaluate(() => APP.log());
  const sc2 = [...agg.values()];
  const log = { scene: S, frames: N, filmSeconds: N / 30, wallSeconds: +wall.toFixed(1), machineSecPerFilmSec: +(wall / (N / 30)).toFixed(2), checkFrames: times.length, hardTime: hard.t,
    cpus: os.cpus().length, cpuModel: os.cpus()[0].model, date: new Date().toISOString(),
    summary: { minDistTextToGraphicPx720: Math.min(99, ...sc2.map((x) => x.dGraphicMin)), minDistTextToTextPx720: Math.min(99, ...sc2.map((x) => x.dTextMin)),
      minContrast: Math.min(99, ...sc2.map((x) => x.contrastMin)), minFontPx1080: Math.min(...lg.texts.map((x) => x.px)), outOfSafe: lg.texts.filter((x) => x.out).map((x) => x.s), badgeMissing: badge.length },
    ...lg, selfCheck: sc2, badgeMissing: badge.slice(0, 20), ownStripTimes: own, keyStripTimes: keyHere };
  fs.writeFileSync(path.join(WK, 'logs', `${S}.json`), JSON.stringify(log, null, 1));
  console.error(S, 'wall', wall.toFixed(0), 's x', log.machineSecPerFilmSec, JSON.stringify(log.summary), 'kwMissing', lg.anchorsKeywordMissing, 'claims', lg.claimsUsed.join(','));
  await page.close();
}

async function strips(browser) {
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  await page.goto(`http://127.0.0.1:${srv.address().port}/episodes/ep002/animatic/src/strip.html`);
  await page.waitForFunction(() => window.READY === true);
  const url = (f) => 'data:image/png;base64,' + fs.readFileSync(f).toString('base64');
  const jobs = [];
  for (const k of Object.keys(KEYS)) { jobs.push([`${k}.png`, [1, 2, 3, 4, 5, 6].map((i) => path.join(WK, 'stills', `${k}-${i}.png`))]); jobs.push([`${k}-masked.png`, [1, 2, 3, 4, 5, 6].map((i) => path.join(WK, 'stills', `${k}-${i}-m.png`))]); }
  for (const s of timing.scenes) jobs.push([`${s.id}.png`, [1, 2, 3, 4, 5, 6].map((i) => path.join(WK, 'stills', `${s.id}-own-${i}.png`))]);
  for (const [name, files] of jobs) {
    if (!files.every((f) => fs.existsSync(f))) { console.error('missing stills for', name); continue; }
    savePng(path.join(AN, 'strips', name), await page.evaluate((u) => window.compose(u), files.map(url)));
  }
  await page.close();
}

(async () => {
  await new Promise((res) => srv.listen(0, res));
  const browser = await chromium.launch({ args: ['--disable-gpu', '--font-render-hinting=none'] });
  if (args.includes('--strips')) await strips(browser);
  for (const S of scenes) await renderScene(browser, srv.address().port, S);
  await browser.close(); srv.close();
})().catch((e) => { console.error(e); process.exit(1); });
