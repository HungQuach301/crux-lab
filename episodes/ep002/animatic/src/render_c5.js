'use strict';
// C5 final picture: the film page (../film.html, the same page the checker samples through window.CHECKS) in Chromium headless,
// canvas 2D at 1920x1080; each frame leaves the page as raw RGBA and is encoded by ffmpeg (libx264 High, yuv420p, BT.709 limited
// range, CRF 8: a near-lossless intermediate; the delivered picture is encoded once from these by assemble_c5.py).
//   NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node render_c5.js S01 [S02 ...]
// Scene S -> work/c5/scenes/S.mp4 (exactly round(end*30)-round(start*30) frames), work/c5/logs/S.json.
const fs = require('fs'), path = require('path'), os = require('os'), { spawn } = require('child_process');
const { chromium } = require('playwright');
const AN = path.resolve(__dirname, '..'), WK = path.join(AN, 'work', 'c5');
for (const d of ['scenes', 'logs']) fs.mkdirSync(path.join(WK, d), { recursive: true });
const scenes = process.argv.slice(2).filter((a) => /^S\d\d$/.test(a));
(async () => {
  const browser = await chromium.launch({ args: ['--font-render-hinting=none', '--disable-lcd-text'] });
  for (const S of scenes) {
    const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
    page.on('pageerror', (e) => { console.error('pageerror', S, e.message); process.exit(1); });
    await page.goto('file://' + path.join(AN, 'film.html'));
    await page.waitForFunction(() => window.READY === true, null, { timeout: 120000 });
    const sc = await page.evaluate((S) => APP.scenes.find((x) => x.id === S), S);
    const N = sc.f1 - sc.f0, tmp = path.join(WK, 'scenes', S + '.part.mp4');
    const enc = spawn('ffmpeg', ['-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgba', '-s', '1920x1080', '-r', '30', '-i', '-',
      '-vf', 'scale=out_color_matrix=bt709:out_range=tv:flags=accurate_rnd+full_chroma_int+bitexact,format=yuv420p',
      '-c:v', 'libx264', '-preset', 'medium', '-crf', '8', '-profile:v', 'high', '-tune', 'animation', '-g', '60',
      '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-color_range', 'tv', tmp], { stdio: ['pipe', 'inherit', 'inherit'] });
    const done = new Promise((res, rej) => enc.on('close', (c) => (c ? rej(new Error('ffmpeg ' + c)) : res())));
    const t0 = Date.now();
    for (let f = sc.f0; f < sc.f1; f++) {
      const b64 = await page.evaluate((f) => APP.frame(f), f);
      if (!enc.stdin.write(Buffer.from(b64, 'base64'))) await new Promise((r) => enc.stdin.once('drain', r));
      if ((f - sc.f0) % 300 === 0) console.error(`${S} ${f - sc.f0}/${N} ${((Date.now() - t0) / (f - sc.f0 + 1)).toFixed(0)} ms/frame`);
    }
    enc.stdin.end(); await done; fs.renameSync(tmp, path.join(WK, 'scenes', S + '.mp4'));
    const wall = (Date.now() - t0) / 1000;
    fs.writeFileSync(path.join(WK, 'logs', S + '.json'), JSON.stringify({ scene: S, frames: N, f0: sc.f0, f1: sc.f1, wallSeconds: +wall.toFixed(1), machineSecPerFilmSec: +(wall / (N / 30)).toFixed(2),
      cpus: os.cpus().length, date: new Date().toISOString(), size: '1920x1080', crf: 8 }, null, 1));
    console.error(S, 'done', wall.toFixed(0), 's');
    await page.close();
  }
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
