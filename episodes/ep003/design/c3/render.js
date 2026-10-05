// Tập 3 C3: render style frame (canvas 1280x720, 30 fps) → work/<K>.mp4 (H.264, tắt tiếng), ảnh tĩnh, tự kiểm chữ.
//   node episodes/ep003/design/c3/render.js KEY1 [KEY2 …] [--stills t1,t2] [--check]
// Cần server tĩnh ở gốc repo: python3 -m http.server 8765 (chạy từ /home/user/crux-lab).
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const fs = require('fs'), path = require('path');
const OUT = path.join(__dirname, 'work');
const R2 = process.argv.includes('--r2');
const FI = process.argv.indexOf('--from'), TI = process.argv.indexOf('--to');
const FROM = FI > 0 ? +process.argv[FI + 1] : null, TO = TI > 0 ? +process.argv[TI + 1] : null;
const SUF = (R2 ? '-r2' : '') + (FROM !== null ? `-${String(FROM).padStart(4, '0')}` : '');
(async () => {
  const args = process.argv.slice(2), keys = args.filter((a) => !a.startsWith('--') && !/^[\d.,]+$/.test(a));
  const si = args.indexOf('--stills'), stills = si >= 0 ? args[si + 1].split(',').map(Number) : null;
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  page.on('console', (m) => { if (m.type() === 'error') console.error('page:', m.text()); });
  page.on('pageerror', (e) => console.error('pageerror:', e.message));
  for (const k of keys) {
    await page.goto(k.startsWith('C4') ? `http://127.0.0.1:8765/episodes/ep003/design/c4/ctrl/page.html?k=${k === 'C4POS' ? 'K5POS' : 'K5'}` : k === 'CTRL' ? 'http://127.0.0.1:8765/episodes/ep003/design/c3/ctrl/page.html' : `http://127.0.0.1:8765/episodes/ep003/design/c3/page.html?k=${k}${k === 'ANIM' ? '&r=anim' : R2 ? '&r=2' : ''}`);
    await page.waitForFunction('window.READY === true', null, { timeout: 30000 });
    const info = await page.evaluate(() => ({ d: APP.duration, n: APP.frames, st: APP.stripTimes }));
    if (stills) {
      for (const t of stills) { const u = await page.evaluate((t) => APP.png(t), t); fs.writeFileSync(path.join(OUT, `${k}${SUF}-t${t.toFixed(2)}.png`), Buffer.from(u.split(',')[1], 'base64')); }
      continue;
    }
    if (args.includes('--check') && k !== 'CTRL' && !k.startsWith('C4')) { // REVIEWER C3-intent #6: check at the frames strips.py will cut (centres of 6 equal slices of [0, duration])
      const res = []; const ts = [0, 1, 2, 3, 4, 5].map((i) => +((i + 0.5) * info.d / 6).toFixed(3));
      for (const t of ts) { const c = await page.evaluate((t) => APP.check(t), t); for (const b of c) if (b.clear < 4 || b.contrast < 4.5 || b.tclear < 4) res.push({ t, ...b }); }
      fs.writeFileSync(path.join(OUT, `${k}${SUF}-check.json`), JSON.stringify({ times: ts, issues: res }, null, 1)); console.log(k, 'check at strip times', ts.join(','), 'issues', res.length);
    }
    const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgba', '-s', '1280x720', '-r', '30', '-i', '-',
      '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium', path.join(OUT, `${k}${SUF}.mp4`)], { stdio: ['pipe', 'inherit', 'inherit'] });
    const f0 = FROM !== null ? Math.round(FROM * 30) : 0, f1 = TO !== null ? Math.min(info.n, Math.round(TO * 30)) : info.n;
    for (let i = f0; i < f1; i++) {
      const b64 = await page.evaluate((t) => APP.frame(t), i / 30);
      if (!ff.stdin.write(Buffer.from(b64, 'base64'))) await new Promise((r) => ff.stdin.once('drain', r));
    }
    ff.stdin.end(); await new Promise((r) => ff.on('close', r));
    const log = await page.evaluate(() => APP.log());
    fs.writeFileSync(path.join(OUT, `${k}${SUF}-log.json`), JSON.stringify({ duration: info.d, stripTimes: info.st, ...log }, null, 1));
    console.log(k, info.d + ' s', info.n, 'frames; claims', log.used.join(','));
  }
  await browser.close();
})();
