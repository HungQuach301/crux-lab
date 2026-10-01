'use strict';
// Thẻ kết quả tìm kiếm cho so cặp tiêu đề C1: thumbnail trung tính CỐ ĐỊNH (không chữ), cùng thời lượng, cùng kênh.
const fs = require('fs'), path = require('path');
const { chromium } = require('playwright');
const REPO = path.resolve(__dirname, '../../..');
const font = (w) => 'data:font/woff2;base64,' + fs.readFileSync(path.join(REPO, 'toolkit/render/fonts', `inter-latin-${w}-normal.woff2`)).toString('base64');
const CW = 640, DUR = '11:04';
// thumbnail trung tính: nền token bg, lưới, một đường giá trị chung chung + một đường ngang; không chữ, không số
const thumb = `<svg viewBox="0 0 1280 720" width="${CW}" height="${CW * 9 / 16}"><rect width="1280" height="720" fill="#0E1116"/>
${[1,2,3,4,5].map(i => `<line x1="80" x2="1200" y1="${i*120}" y2="${i*120}" stroke="#2A303B" stroke-width="3"/>`).join('')}
<line x1="80" x2="1200" y1="330" y2="330" stroke="#9AA4B2" stroke-width="10"/>
<polyline fill="none" stroke="#4C8DFF" stroke-width="12" stroke-linejoin="round" points="80,420 200,400 300,430 420,300 520,220 600,260 700,180 800,320 900,380 1000,450 1100,470 1200,440"/></svg>`;
const css = `@font-face{font-family:Inter;font-weight:400;src:url(${font(400)})}@font-face{font-family:Inter;font-weight:600;src:url(${font(600)})}
html,body{margin:0;background:#0f0f0f;font-family:Inter;color:#f1f1f1}.wrap{width:${CW + 96}px;padding:20px 0}
.row{display:flex;align-items:flex-start;margin:0 0 22px}.lab{width:72px;flex:0 0 72px;display:flex;justify-content:center;padding-top:8px}
.lab span{display:inline-flex;width:52px;height:52px;border-radius:26px;background:#3ea6ff;color:#0f0f0f;font-weight:600;font-size:32px;align-items:center;justify-content:center}
.th{position:relative;width:${CW}px;height:${CW * 9 / 16}px;border-radius:12px;overflow:hidden}.th svg{display:block}
.dur{position:absolute;right:8px;bottom:8px;background:rgba(0,0,0,.8);color:#fff;font-size:15px;font-weight:600;padding:3px 6px;border-radius:4px}
.meta{display:flex;gap:12px;padding:12px 4px 0}.av{flex:0 0 40px;width:40px;height:40px;border-radius:20px;background:#2a303b;color:#f2f4f7;font-weight:600;font-size:20px;display:flex;align-items:center;justify-content:center}
.ti{font-size:20px;line-height:28px;font-weight:600}.ch{font-size:15px;color:#aaa;margin-top:4px}`;
const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
const card = (t) => `<div><div class="th">${thumb}<div class="dur">${DUR}</div></div><div class="meta"><div class="av">C</div><div><div class="ti">${esc(t)}</div><div class="ch">Crux</div></div></div></div>`;
const row = (n, inner) => `<div class="row"><div class="lab"><span>${n}</span></div>${inner}</div>`;
(async () => {
  const cards = JSON.parse(fs.readFileSync(process.argv[2]));
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: CW + 96, height: 600 } });
  for (const c of cards) {
    await p.setContent(`<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body><div class="wrap">${row(1, card(c.t1)) + row(2, card(c.t2))}</div></body></html>`);
    await p.evaluate(() => document.fonts.ready);
    await (await p.$('.wrap')).screenshot({ path: c.out });
  }
  await b.close();
})().catch((e) => { console.error(e); process.exit(1); });
