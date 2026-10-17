// Ảnh bìa R1-AI · bước 2: ghép BẰNG MÃ trên nền ảnh AI (không chữ): chữ, số cách điệu, vector SVG (mũi tên), nhận diện kênh.
//   NODE_PATH=/opt/node-tools/node_modules node packaging/r1/ai/compose.js <jobs.json>
// jobs.json: [{bg, out, outBare, cropY, l1, l1Size, num, numSize, pillar, arrow:[x0,y0,x1,y1]|null}] — outBare = cùng ảnh không chữ (để đo tương phản).
// Bố cục cố định cho mọi tập: logo "M." trên trái · dòng ngữ cảnh trắng ≤ 96 px · số màu trụ ≤ 150 px viền tối (co theo bề rộng ≤ 620 px) · mũi tên màu trụ tới chủ thể ·
// chân "US only · history, not a forecast". Không nhãn ILLUSTRATIVE trên ảnh bìa (D-015).
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '../../..');
const PILLAR = { debt: '#F2B441', retire: '#3FBF7F', tax: '#4C8DFF' }, BG = '#0E1116', INK = '#F2F4F7', MUTED = '#C9D1DB';
const font = 'data:font/woff2;base64,' + fs.readFileSync(path.join(ROOT, 'toolkit/render/fonts/inter-latin-700-normal.woff2')).toString('base64');
const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
function svg(j, bare) {
  const img = (j.bg.endsWith('.jpg') ? 'data:image/jpeg;base64,' : 'data:image/png;base64,') + fs.readFileSync(path.resolve(j.bg)).toString('base64');
  const c = PILLAR[j.pillar];
  // nền 1536×1024 → cắt 1536×864 từ cropY → 1280×720
  const s = 1280 / 1536, y = -(j.cropY || 80) * s;
  let t = `<image href="${img}" x="0" y="${y}" width="1280" height="${1024 * s}"/>
  <defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="${BG}" stop-opacity="0.82"/><stop offset="0.42" stop-color="${BG}" stop-opacity="0.45"/><stop offset="0.6" stop-color="${BG}" stop-opacity="0"/></linearGradient>
  <linearGradient id="b" x1="0" x2="0" y1="0" y2="1"><stop offset="0.55" stop-color="${BG}" stop-opacity="0"/><stop offset="1" stop-color="${BG}" stop-opacity="0.75"/></linearGradient>
  <marker id="h" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="4" markerHeight="4" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="${c}"/></marker>
  <filter id="sh" x="-10%" y="-10%" width="120%" height="130%"><feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000" flood-opacity="0.55"/></filter></defs>
  <rect width="1280" height="720" fill="url(#g)"/><rect width="1280" height="720" fill="url(#b)"/>
  <rect x="32" y="28" width="80" height="80" rx="14" fill="${c}"/><text x="72" y="88" font-size="52" text-anchor="middle" fill="${BG}">M.</text>
  <text x="1240" y="696" font-size="22" text-anchor="end" fill="${MUTED}" opacity="0.85">US only · history, not a forecast</text>`;
  if (bare) return t;
  if (j.arrow) {
    const [x0, y0, x1, y1] = j.arrow, mx = (x0 + x1) / 2, my = Math.min(y0, y1) - 70;
    t += `<path d="M${x0},${y0} Q${mx},${my} ${x1},${y1}" fill="none" stroke="${BG}" stroke-width="24" stroke-linecap="round" opacity="0.6"/>
    <path d="M${x0},${y0} Q${mx},${my} ${x1},${y1}" fill="none" stroke="${c}" stroke-width="14" stroke-linecap="round" marker-end="url(#h)"/>`;
  }
  t += `<g filter="url(#sh)"><text x="48" y="${Math.round(652 - j.numSize * 0.8 - 22)}" font-size="${j.l1Size}" fill="${INK}" stroke="${BG}" stroke-width="8" paint-order="stroke" letter-spacing="1">${esc(j.l1)}</text>`;
  if (j.num) t += `<text x="44" y="652" font-size="${j.numSize}" fill="${c}" stroke="${BG}" stroke-width="12" paint-order="stroke" letter-spacing="-2">${esc(j.num)}</text>`;
  return t + '</g>';
}
(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2]));
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
  for (const j of jobs) for (const [bare, out] of [[false, j.out], [true, j.outBare]]) {
    if (!out) continue;
    await p.setContent(`<html><head><style>@font-face{font-family:I;src:url(${font})}body{margin:0}text{font-family:I;font-weight:700}</style></head>
      <body><svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720">${svg(j, bare)}</svg></body></html>`);
    await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: out, clip: { x: 0, y: 0, width: 1280, height: 720 } });
  }
  await b.close();
})();
