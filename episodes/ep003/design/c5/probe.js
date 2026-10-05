// C5 self-check (bên dựng, không phải máy kiểm): mở trang 1080p qua window.CHECKS, quét mỗi `step` giây, liệt kê số mồ côi (S07),
// khung có claim ILLUSTRATIVE mà không có huy hiệu (S08), giả định hiện trên hình (S02) — dùng chính objrules.js của checks/ để đọc đối tượng.
//   NODE_PATH=$(npm root -g) node episodes/ep003/design/c5/probe.js [step=0.5] [from] [to]
const { chromium } = require('playwright');
const R = require('../../../../checks/page/objrules.js');
(async () => {
  const step = +(process.argv[2] || 0.5), from = +(process.argv[3] || 0);
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  p.on('pageerror', (e) => console.error('pageerror', e.message));
  await p.goto('http://127.0.0.1:8765/episodes/ep003/design/c3/page.html?k=ANIM&r=anim&res=1080');
  await p.waitForFunction('window.READY === true', null, { timeout: 30000 });
  const dur = await p.evaluate(() => APP.duration), to = +(process.argv[4] || dur);
  const orph = new Map(), s08 = [], texts = new Set(), asm = { 'what-if': [], tax: [] };
  for (let t = from; t < to; t += step) {
    await p.evaluate((t) => window.CHECKS.seek(t), t);
    const o = await p.evaluate(() => window.CHECKS.objects());
    for (const x of R.orphanNumbers(o)) { const k = x.text; if (!orph.has(k)) orph.set(k, { t: +t.toFixed(1), numbers: x.numbers }); }
    const st = R.illustrativeState(o, { illustrative: ['viewer_age_decade'] }); if (st.shown.length && !st.badge) s08.push(+t.toFixed(1));
    for (const x of o) if (x.kind === 'text' && x.opacity > 0.5) { texts.add(x.text); if (/IF today'?s guarantee had existed/i.test(x.text)) asm['what-if'].push(+t.toFixed(1)); if (/tax/i.test(x.text)) asm.tax.push(+t.toFixed(1)); }
  }
  console.log(JSON.stringify({ duration: dur, orphans: [...orph.entries()], s08Frames: s08.slice(0, 20), s08Count: s08.length,
    assumptions: { whatIf: asm['what-if'].length, tax: [...new Set(asm.tax.map(Math.floor))] }, nTexts: texts.size }, null, 1));
  await b.close();
})();
