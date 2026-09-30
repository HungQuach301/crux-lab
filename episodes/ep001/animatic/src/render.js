'use strict';
// C5 final-picture renderer: the film page (../film.html, the same page the checker samples through window.CHECKS) in
// Chromium headless (Playwright) + SwiftShader (CPU WebGL) at 1920x1080; each frame leaves the page as a lossless PNG
// and is encoded by ffmpeg (libx264, High, yuv420p, BT.709 limited range, CRF 8: a near-lossless intermediate; the delivered
// picture is encoded once from these by assemble_c5.py).
//   NODE_PATH=/opt/node22/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node render.js S01 [S02 ...] [--force] [--still t1,t2]
// Scene S -> <ep>/work/c5/scenes/S.mp4 (video only, exactly round(end*30)-round(start*30) frames), <ep>/work/c5/logs/S.json
// (timings, claims, strings, anchors: read by check.py) and <ep>/work/c5/hard/S-hard.png (frame for the 25% check).
// Resumable: a scene whose mp4 + log are newer than build/film.js, src/data.js and timing.json, and whose log has the same
// basisMode, is skipped (unless --force). BASIS_MODE=near|corner (env, default corner) picks the basis-label variant (film.html?basis=...).
const fs = require('fs'), path = require('path'), os = require('os'), { spawn, execFileSync } = require('child_process');
const { chromium } = require('playwright');
const HERE = __dirname, AN = path.resolve(HERE, '..'), EP = path.resolve(AN, '..');
const OUT = path.join(EP, 'work', 'c5');
const args = process.argv.slice(2);
const opt = (k) => { const i = args.indexOf('--' + k); return i >= 0 ? args[i + 1] : null; };
const scenes = args.filter((a, i) => /^S\d\d$/.test(a) && args[i - 1] !== '--still');
const FFMPEG = process.env.FFMPEG || (() => { try { return execFileSync('python3', ['-c', 'import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())']).toString().trim(); } catch (e) { return 'ffmpeg'; } })();
const CRF = process.env.CRF || '8';
const BASIS_MODE = process.env.BASIS_MODE || 'corner'; // K3.3 default (engine.js BASIS_MODE)
for (const d of ['scenes', 'logs', 'hard', 'stills']) fs.mkdirSync(path.join(OUT, d), { recursive: true });
const mtime = (f) => { try { return fs.statSync(f).mtimeMs; } catch (e) { return 0; } };
const inputs = Math.max(...[path.join(AN, 'build/film.js'), path.join(HERE, 'data.js'), path.join(AN, 'timing.json'), path.join(AN, 'film.html')].map(mtime));

(async () => {
  const browser = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--font-render-hinting=none', '--disable-lcd-text'] });
  for (const F of scenes) {
    const mp4 = path.join(OUT, 'scenes', `${F}.mp4`), logf = path.join(OUT, 'logs', `${F}.json`);
    const modeOf = (f) => { try { return JSON.parse(fs.readFileSync(f, 'utf8')).basisMode || 'near'; } catch (e) { return null; } };
    if (!args.includes('--force') && !opt('still') && Math.min(mtime(mp4), mtime(logf)) > inputs && modeOf(logf) === BASIS_MODE) { console.error(F, 'up to date, skipped'); continue; }
    const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
    page.on('pageerror', (e) => { console.error('pageerror', F, e.message); process.exit(1); });
    page.on('console', (m) => { if (m.type() === 'error') console.error('console', F, m.text()); });
    await page.goto('file://' + path.join(AN, 'film.html') + '?basis=' + BASIS_MODE);
    await page.evaluate(() => window.APP.ready);
    const meta = await page.evaluate((F) => ({ ...APP.scene(F), gpu: APP.info() }), F);
    console.error(F, JSON.stringify(meta));
    const savePng = (file, dataUrl) => fs.writeFileSync(file, Buffer.from(dataUrl.split(',')[1], 'base64'));
    if (opt('still')) {
      for (const t of opt('still').split(',').map(Number)) savePng(path.join(OUT, 'stills', `${F}-${t.toFixed(2)}.png`), await page.evaluate(([f0, t]) => APP.png(f0 / 30 + t), [meta.f0, t]));
      await page.close(); continue;
    }
    const tmp = mp4 + '.part.mp4';
    const enc = spawn(FFMPEG, ['-v', 'error', '-y', '-f', 'image2pipe', '-framerate', '30', '-c:v', 'png', '-i', '-',
      '-vf', 'scale=out_color_matrix=bt709:out_range=tv:flags=accurate_rnd+full_chroma_int+bitexact,format=yuv420p',
      '-c:v', 'libx264', '-preset', 'medium', '-crf', CRF, '-profile:v', 'high', '-tune', 'animation', '-g', '60',
      '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-color_range', 'tv', '-movflags', '+faststart', tmp], { stdio: ['pipe', 'inherit', 'inherit'] });
    const done = new Promise((res, rej) => enc.on('close', (c) => (c ? rej(new Error('ffmpeg ' + c)) : res())));
    const t0 = Date.now(); let tb = 0, n3 = 0;
    for (let f = 0; f < meta.N; f++) {
      const s = Date.now();
      const [png, m] = await page.evaluate((g) => { const m = APP.frameMode(g); return [document.getElementById('film').toDataURL('image/png'), m]; }, meta.f0 + f);
      if (m === '3d') n3++;
      tb += Date.now() - s;
      if (!enc.stdin.write(Buffer.from(png.slice(png.indexOf(',') + 1), 'base64'))) await new Promise((r) => enc.stdin.once('drain', r));
      if (f % 150 === 0) console.error(`${F} frame ${f}/${meta.N} ${((Date.now() - t0) / (f + 1)).toFixed(0)} ms/frame`);
    }
    enc.stdin.end(); await done;
    fs.renameSync(tmp, mp4);
    const wall = (Date.now() - t0) / 1000;
    const hard = meta.hard ?? (meta.N - 1) / 30;
    savePng(path.join(OUT, 'hard', `${F}-hard.png`), await page.evaluate(([f0, t]) => APP.png(f0 / 30 + t), [meta.f0, Math.min(hard, (meta.N - 1) / 30)]));
    const lg = await page.evaluate((F) => APP.log(F), F);
    const log = { scene: F, frames: meta.N, frames3d: n3, filmSeconds: meta.N / 30, wallSeconds: +wall.toFixed(1), browserFrameSeconds: +(tb / 1000).toFixed(1),
      machineSecPerFilmSec: +(wall / (meta.N / 30)).toFixed(2), hardTime: hard, crf: +CRF, size: '1920x1080',
      basisMode: BASIS_MODE, renderer: meta.gpu, cpus: os.cpus().length, cpuModel: os.cpus()[0].model, date: new Date().toISOString(), ...lg, claimsUsed: lg.used };
    delete log.used;
    fs.writeFileSync(logf, JSON.stringify(log, null, 1));
    console.error(F, 'wall', wall, 's; x', log.machineSecPerFilmSec, '; out-of-safe:', lg.texts.filter((x) => x.out).map((x) => x.s), '; outV03:', lg.texts.filter((x) => x.outV03).map((x) => x.s), '; kw missing:', lg.anchorsKeywordMissing);
    await page.close();
  }
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
