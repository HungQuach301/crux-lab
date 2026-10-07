// Tập 5 · G2: 3 thumbnail 1280×720 → out/package/thumb-N.png + thumb-N.json {texts:[{text,box,fontPx,claims}], graphics:{claims,what}} (mẫu: ep004/design/g2/thumbs.js).
//   NODE_PATH=$(npm root -g) node episodes/ep005/design/g2/thumbs.js
// Mọi chữ số lấy từ `display` của out/claims.json; cột 307 tháng mua lấy từ work/world-data/derived.json (cùng dữ liệu của đoạn thế giới c).
// Claim-risk (topics-r2/machine/debt-2/claim-risk.md): số "tới 80 %" luôn kèm "on paper" (điều kiện on-paper của contract.json); không nói "PMI off";
// ba người mua có ILLUSTRATIVE; mọi khung có "US only · history, not a forecast". REVIEWER R1: KHÔNG số tiền phí bảo hiểm nào. Màu: chỉ token design/tokens.json.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const EP = path.join(__dirname, '..', '..'), OUT = path.join(EP, 'out', 'package');
const FONTS = path.join(EP, '..', '..', 'toolkit', 'render', 'fonts');
const C = Object.fromEntries(JSON.parse(fs.readFileSync(path.join(EP, 'out', 'claims.json'))).claims.map((c) => [c.claimId, c]));
const d = (id) => { if (!C[id] || C[id].display == null) throw new Error('claim ' + id); return C[id].display; };
const TK = JSON.parse(fs.readFileSync(path.join(EP, 'design', 'tokens.json'))).colors;
const BG = TK.bg, INK = TK.ink, WARN = TK.warn, MUTE = TK['ink-muted'], BLUE = TK.accent, GRID = TK.grid;
const BARS = JSON.parse(fs.readFileSync(path.join(EP, 'work', 'world-data', 'derived.json'))).bars;
if (BARS.length !== C.nB.value) throw new Error('bars ≠ nB');
const BUY = JSON.parse(fs.readFileSync(path.join(EP, 'work', 'world-data', 'derived.json'))).buyers;
const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
function T(id, x, y, px, s, claims, o = {}) { return { id, x, y, px, s, claims, params: o.params, w: o.w || 700, fill: o.fill || INK, anchor: o.anchor || 'start' }; }   // params: model.params of contract.json behind a number that is a set-up, not a result
const txt = (t) => `<text data-id="${t.id}" x="${t.x}" y="${t.y}" font-size="${t.px}" font-weight="${t.w}" fill="${t.fill}" text-anchor="${t.anchor}">${esc(t.s)}</text>`;
const badge = (x, y, claims) => ({ svg: `<rect x="${x}" y="${y}" width="196" height="44" rx="8" fill="${WARN}"/><text data-id="badge" x="${x + 98}" y="${y + 31}" font-size="26" font-weight="700" fill="${BG}" text-anchor="middle">ILLUSTRATIVE</text>`, claims });
const foot = () => T('foot', 1240, 694, 26, 'US only · history, not a forecast', [], { w: 400, fill: MUTE, anchor: 'end' });
const months = (id) => `${d(id)} months`;

// 307 cột tháng mua (chiều cao = số tháng tới 80 % trên giấy), như S11–S13; tô theo hàm col(bar, i)
function barChart(x0, x1, yb, hTop, col) {
  const max = Math.max(...BARS.map((b) => b.hit)), w = (x1 - x0) / BARS.length;
  return BARS.map((b, i) => `<rect x="${(x0 + i * w).toFixed(2)}" y="${(yb - hTop * b.hit / max).toFixed(2)}" width="${Math.max(1, w - 0.4).toFixed(2)}" height="${(hTop * b.hit / max).toFixed(2)}" fill="${col(b, i)}"/>`).join('') +
    `<rect x="${x0}" y="${yb}" width="${x1 - x0}" height="3" fill="${MUTE}"/>`;
}

function thumb1() { // 23 months on paper — not removal; median line over the 307 purchase months
  const x0 = 690, x1 = 1236, yb = 600, hTop = 470, max = Math.max(...BARS.map((b) => b.hit)), med = C.medianB_months_to80.value, ym = yb - hTop * med / max;
  const body = barChart(x0, x1, yb, hTop, (b) => (b.hit <= med ? INK : GRID)) + `<rect x="${x0 - 8}" y="${ym - 3}" width="${x1 - x0 + 16}" height="6" fill="${WARN}"/>`;
  const texts = [T('h1', 44, 210, 150, months('medianB_months_to80'), ['medianB_months_to80']),
    T('h2', 48, 315, 92, 'on paper', ['medianB_months_to80'], { fill: WARN }),
    T('s1', 52, 395, 40, 'is not the same as removed', [], { w: 600 }),
    T('s2', 52, 470, 32, `typical of ${d('nB')} purchase months,`, ['nB', 'medianB_months_to80'], { w: 600, fill: MUTE }),
    T('s3', 52, 512, 32, `${d('firstB')} to ${d('lastB')}, 10% down`, ['firstB', 'lastB'], { w: 600, fill: MUTE, params: ['downShare'] }),
    T('s4', x1, ym - 16, 28, 'median', ['medianB_months_to80'], { w: 600, fill: WARN, anchor: 'end' }), foot()];
  return { body, texts, graphics: { claims: ['nB', 'medianB_months_to80', 'maxB_months_to80', 'firstB', 'lastB'],
    what: `${C.nB.value} bars, one per purchase month ${d('firstB')}–${d('lastB')}, height = months to 80% on paper (national index); bars at or under the median white, the rest dark; amber median line at ${med} months. No axis numbers.` } };
}
function thumb2() { // 1 in 7 took over 5 years on paper — the slow stretch lit in accent
  const x0 = 690, x1 = 1236, yb = 600, hTop = 470;
  const body = barChart(x0, x1, yb, hTop, (b) => (b.hit > 60 ? BLUE : GRID));
  const texts = [T('h1', 44, 210, 150, d('shareB_over60'), ['shareB_over60']),
    T('h2', 48, 300, 64, 'took over 5 years', ['shareB_over60'], { params: ['slowCutMonths'] }),
    T('h3', 48, 380, 64, 'on paper', ['shareB_over60'], { fill: WARN }),
    T('s1', 52, 462, 32, `${d('slowB_n')} purchase months, ${d('slowB_first')}`, ['slowB_n', 'slowB_first'], { w: 600, fill: MUTE }),
    T('s2', 52, 504, 32, `to ${d('slowB_last')}: the price slump`, ['slowB_last'], { w: 600, fill: MUTE }), foot()];
  return { body, texts, graphics: { claims: ['nB', 'shareB_over60', 'slowB_n', 'slowB_first', 'slowB_last', 'maxB_months_to80'],
    what: `${C.nB.value} bars (months to 80% on paper per purchase month); bars over 60 months in blue (${C.slowB_n.value}, ${d('slowB_first')}–${d('slowB_last')}), the rest dark. No axis numbers.` } };
}
function thumb3() { // Owen 13 vs Victor 112 months on paper — ILLUSTRATIVE buyers, bought 21 months apart
  const yb = 570, hTop = 400, max = C.buyer_victor_monthsTo80Index.value, bw = 150, xo = 820, xv = 1040;
  const ho = hTop * C.buyer_owen_monthsTo80Index.value / max, hv = hTop * C.buyer_victor_monthsTo80Index.value / max;
  const bd = badge(52, 540, ['buyer_owen_monthsTo80Index', 'buyer_victor_monthsTo80Index', 'buyer_owen_purchaseMonth', 'buyer_victor_purchaseMonth']);
  const body = `<rect x="${xo}" y="${yb - ho}" width="${bw}" height="${ho}" fill="${INK}"/><rect x="${xv}" y="${yb - hv}" width="${bw}" height="${hv}" fill="${BLUE}"/>` +
    `<rect x="${xo - 30}" y="${yb}" width="${xv + bw - xo + 60}" height="3" fill="${MUTE}"/>` + bd.svg;
  const texts = [T('h1', 44, 170, 96, `Owen: ${months('buyer_owen_monthsTo80Index')}`, ['buyer_owen_monthsTo80Index']),
    T('h2', 44, 290, 96, months('buyer_victor_monthsTo80Index').replace(/^/, 'Victor: '), ['buyer_victor_monthsTo80Index'], { fill: BLUE }),
    T('h3', 48, 380, 64, 'on paper, 10% down', ['buyer_owen_monthsTo80Index', 'buyer_victor_monthsTo80Index'], { fill: WARN, params: ['downShare'] }),
    T('s1', 52, 462, 32, `bought ${d('buyer_owen_purchaseMonth')} and ${d('buyer_victor_purchaseMonth')}`, ['buyer_owen_purchaseMonth', 'buyer_victor_purchaseMonth'], { w: 600, fill: MUTE }),
    T('s2', xo + bw / 2, yb + 46, 32, 'Owen', ['buyer_owen_monthsTo80Index'], { w: 600, anchor: 'middle' }),
    T('s3', xv + bw / 2, yb + 46, 32, 'Victor', ['buyer_victor_monthsTo80Index'], { w: 600, anchor: 'middle', fill: BLUE }), foot()];
  return { body, texts, badgeClaims: bd.claims, graphics: { claims: ['buyer_owen_monthsTo80Index', 'buyer_victor_monthsTo80Index'],
    what: 'two bars, height = months to 80% on paper for the two ILLUSTRATIVE buyers (Owen 13, Victor 112, same scale, no axis numbers). ILLUSTRATIVE badge.' } };
}
(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const b = await chromium.launch({ args: ['--font-render-hinting=none', '--disable-lcd-text'] }); const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
  const ff = [400, 600, 700].map((w) => `@font-face{font-family:Inter;font-weight:${w};src:url(file://${FONTS}/inter-latin-${w}-normal.woff2) format('woff2')}`).join('');
  for (const [n, fn] of [[1, thumb1], [2, thumb2], [3, thumb3]]) {
    const t = fn();
    const html = `<!doctype html><html><head><meta charset="utf-8"><style>${ff}html,body{margin:0;background:${BG}}svg{display:block;font-family:Inter}rect{shape-rendering:crispEdges}</style></head><body>` +
      `<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720"><rect width="1280" height="720" fill="${BG}"/>${t.body}${t.texts.map(txt).join('')}</svg></body></html>`;
    const f = path.join(OUT, `.thumb-${n}.html`); fs.writeFileSync(f, html);
    await p.goto('file://' + f); await p.evaluate(() => document.fonts.ready);
    const boxes = await p.evaluate(() => Object.fromEntries([...document.querySelectorAll('text[data-id]')].map((e) => { const r = e.getBBox(); return [e.dataset.id, [r.x, r.y, r.width, r.height].map((v) => Math.round(v * 10) / 10)]; })));
    await p.screenshot({ path: path.join(OUT, `thumb-${n}.png`) }); fs.unlinkSync(f);
    for (const [k, bx] of Object.entries(boxes)) if (bx[0] < 0 || bx[1] < 0 || bx[0] + bx[2] > 1280 || bx[1] + bx[3] > 720) throw new Error(`thumb ${n} ${k} off canvas ${bx}`);
    const texts = t.texts.map((x) => ({ text: x.s, box: boxes[x.id], fontPx: x.px, claims: x.claims, ...(x.params ? { params: x.params } : {}) }));
    if (boxes.badge) texts.push({ text: 'ILLUSTRATIVE', box: boxes.badge, fontPx: 26, claims: t.badgeClaims });
    fs.writeFileSync(path.join(OUT, `thumb-${n}.json`), JSON.stringify({ texts, graphics: t.graphics }, null, 1));
    console.log(n, texts.map((x) => x.text).join(' | '));
  }
  await b.close();
})();
