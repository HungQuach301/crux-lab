// Crux factory renderer (Mốc B). Renders the segments of one job in parallel: one Chromium, one page per worker, each segment → its own
// H.264 file (concat-copy-ready: same encoder settings, keyframe at the start). build.py writes the job and lists only changed segments.
//   NODE_PATH=$(npm root -g) node toolkit/factory/render.js <job.json> [--workers 4] [--fmt jpeg|rgba] [--stills t1,t2 --stills-dir D]
// Intermediate frame: JPEG q 0.95 from canvas.toDataURL (default) or raw RGBA via getImageData (the Tập 2–3 path, kept for SPEED.md).
// Every 6th frame (global index) the engine log is kept → <segment>.log.json for qc.py.
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '../..');
const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json', '.woff2': 'font/woff2' };
const arg = (k, d) => { const i = process.argv.indexOf(k); return i > 0 ? process.argv[i + 1] : d; };

function encoder(job, out, fmt) {
  const [w, h] = job.size, e = job.encode || {};
  const input = fmt === 'rgba' ? ['-f', 'rawvideo', '-pix_fmt', 'rgba', '-s', `${w}x${h}`, '-r', String(job.fps), '-i', '-']
    : ['-f', 'image2pipe', '-c:v', 'mjpeg', '-framerate', String(job.fps), '-i', '-'];
  const rate = e.cbr ? ['-b:v', e.cbr, '-minrate', e.cbr, '-maxrate', e.cbr, '-bufsize', e.cbr, '-x264-params', 'nal-hrd=cbr:force-cfr=1']
    : ['-crf', String(e.crf ?? 16)];
  return spawn('ffmpeg', ['-y', '-loglevel', 'error', ...input, '-c:v', 'libx264', '-profile:v', 'high', '-preset', e.preset || 'fast', ...rate,
    '-pix_fmt', 'yuv420p', '-vf', 'scale=out_color_matrix=bt709:out_range=tv', '-color_primaries', 'bt709', '-color_trc', 'bt709',
    '-colorspace', 'bt709', '-color_range', 'tv', '-r', String(job.fps), '-video_track_timescale', '15360', out], { stdio: ['pipe', 'inherit', 'inherit'] });
}

(async () => {
  const jobPath = path.resolve(process.argv[2]), job = JSON.parse(fs.readFileSync(jobPath, 'utf8'));
  const workers = +arg('--workers', 4), fmt = arg('--fmt', job.fmt || 'jpeg'), quality = +(job.quality || 0.95);
  const browser = await chromium.launch({ args: ['--font-render-hinting=none', '--disable-lcd-text'] });
  const open = async () => {
    const ctx = await browser.newContext({ viewport: { width: job.size[0], height: job.size[1] }, deviceScaleFactor: 1 });
    await ctx.route('http://factory.local/**', (r) => {
      const p = path.join(ROOT, decodeURIComponent(new URL(r.request().url()).pathname));
      if (!p.startsWith(ROOT) || !fs.existsSync(p)) return r.fulfill({ status: 404, body: '' });
      r.fulfill({ status: 200, body: fs.readFileSync(p), contentType: MIME[path.extname(p)] || 'application/octet-stream' });
    });
    const page = await ctx.newPage();
    page.on('pageerror', (e) => { console.error('pageerror:', e.message); process.exitCode = 1; });
    page.on('console', (m) => { if (m.type() === 'error') console.error('page:', m.text()); });
    await page.goto(`http://factory.local/toolkit/factory/page.html?job=${encodeURIComponent(path.relative(ROOT, jobPath))}`);
    await page.waitForFunction('window.READY === true', null, { timeout: 30000 });
    return page;
  };
  const stills = arg('--stills');
  if (stills) { // PNG stills at given times (comparison sheets, review)
    const page = await open(), dir = arg('--stills-dir', path.dirname(jobPath)); fs.mkdirSync(dir, { recursive: true });
    for (const t of stills.split(',').map(Number)) fs.writeFileSync(path.join(dir, `${job.name}-t${t.toFixed(2)}.png`), Buffer.from(await page.evaluate((t) => APP.png(t), t), 'base64'));
    await browser.close(); return;
  }
  const queue = [...job.segments], t0 = Date.now(); let frames = 0;
  const work = async () => {
    const page = await open();
    for (let seg; (seg = queue.shift());) {
      const tmp = seg.out + '.part.mp4', ff = encoder(job, tmp, fmt), logs = [];
      for (let i = seg.f0; i < seg.f1; i++) {
        const r = await page.evaluate(([t, f, q, l, sh]) => APP.frame(t, f, q, l, sh), [i / job.fps, fmt, quality, i % 6 === 0, seg.shot || null]);
        if (r.log) logs.push({ f: i, ...r.log });
        if (!ff.stdin.write(Buffer.from(r.img, 'base64'))) await new Promise((res) => ff.stdin.once('drain', res));
        frames++;
      }
      ff.stdin.end(); const code = await new Promise((res) => ff.on('close', res)); if (code) throw new Error('ffmpeg failed on ' + seg.id);
      fs.renameSync(tmp, seg.out); fs.writeFileSync(seg.out + '.log.json', JSON.stringify({ id: seg.id, f0: seg.f0, f1: seg.f1, logs }));
      console.log(`segment ${seg.id} frames ${seg.f0}-${seg.f1} done`);
    }
  };
  await Promise.all(Array.from({ length: Math.min(workers, job.segments.length) }, work));
  const s = (Date.now() - t0) / 1000;
  console.log(JSON.stringify({ render: { frames, seconds: +s.toFixed(2), fps: +(frames / s).toFixed(2), workers, fmt } }));
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
