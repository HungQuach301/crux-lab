// node render.mjs <clip> <seconds> <outdir> — chụp từng khung 30 fps qua window.seek(t) (máy chủ tĩnh gốc repo ở :8765)
import { createRequire } from 'module';
const { chromium } = createRequire(import.meta.url)('playwright');
import fs from 'fs';
const [clip, secs, out] = process.argv.slice(2);
fs.mkdirSync(out, { recursive: true });
const b = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
const p = await b.newPage({ viewport: { width: 960, height: 540 } });
p.on('console', (m) => { if (m.type() === 'error') console.error('page:', m.text()); });
await p.goto(`http://127.0.0.1:8765/episodes/ep008/preprod/objclip/page.html?clip=${clip}`);
await p.waitForFunction(() => window.ready === true, null, { timeout: 60000 });
const n = Math.round(Number(secs) * 30);
for (let i = 0; i < n; i++) {
  await p.evaluate((t) => window.seek(t), i / 30);
  await p.screenshot({ path: `${out}/f${String(i).padStart(4, '0')}.png` });
}
await b.close();
console.log(clip, n, 'khung');
