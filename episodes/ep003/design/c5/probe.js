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
  const orph = new Map(), s08 = [], texts = new Set(), asm = { 'what-if': [], tax: [] }, shown = {}, boxes = [];
  const TL = JSON.parse(require('fs').readFileSync(__dirname + '/../../animatic/timing.json')).scenes;
  for (let t = from; t < to; t += step) {
    await p.evaluate((t) => window.CHECKS.seek(t), t);
    const o = await p.evaluate(() => window.CHECKS.objects());
    for (const x of R.orphanNumbers(o)) { const k = x.text; if (!orph.has(k)) orph.set(k, { t: +t.toFixed(1), numbers: x.numbers }); }
    const sc = [...TL].reverse().find((x) => t >= x.start) || TL[0];
    for (const x of o) if (x.kind === 'text' && x.opacity > 0.5) for (const c of x.claims || []) if (c.opacity > 0.5 && R.onFrame({ l: c.box[0], t: c.box[1], r: c.box[2], b: c.box[3] })) (shown[c.id] ||= new Set()).add(sc.id);
    // box-level self-check (approximate; checks measure pixels): text outside the safe area, text boxes overlapping
    const T = o.filter((x) => x.kind === 'text' && x.opacity > 0.9);
    for (const x of T) if (x.box[0] < 96 || x.box[1] < 54 || x.box[2] > 1824 || x.box[3] > 1026) boxes.push(['safe', +t.toFixed(1), x.text.slice(0, 40), x.box.map(Math.round)]);
    for (let i = 0; i < T.length; i++) for (let j = i + 1; j < T.length; j++) { const a = T[i].box, b = T[j].box; if (a[0] < b[2] - 2 && b[0] < a[2] - 2 && a[1] < b[3] - 2 && b[1] < a[3] - 2) boxes.push(['overlap', +t.toFixed(1), T[i].text.slice(0, 30), T[j].text.slice(0, 30)]); }
    const st = R.illustrativeState(o, { illustrative: ['viewer_age_decade'] }); if (st.shown.length && !st.badge) s08.push(+t.toFixed(1));
    for (const x of o) if (x.kind === 'text' && x.opacity > 0.5) { texts.add(x.text); if (/IF today'?s guarantee had existed/i.test(x.text)) asm['what-if'].push(+t.toFixed(1)); if (/tax/i.test(x.text)) asm.tax.push(+t.toFixed(1)); }
  }
  console.log(JSON.stringify({ duration: dur, orphans: [...orph.entries()], s08Frames: s08.slice(0, 20), s08Count: s08.length,
    assumptions: { whatIf: asm['what-if'].length, tax: [...new Set(asm.tax.map(Math.floor))].length }, nTexts: texts.size,
    boxIssues: [...new Map(boxes.map((b) => [b[0] + b[2] + (b[3] || ''), b])).values()] }, null, 1));
  require('fs').writeFileSync(__dirname + '/shown.json', JSON.stringify(Object.fromEntries(Object.entries(shown).map(([k, v]) => [k, [...v].sort()])), null, 1));
  await b.close();
})();
