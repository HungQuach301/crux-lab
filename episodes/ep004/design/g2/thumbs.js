// Tập 4 · G2: 3 thumbnail 1280x720 → out/package/thumb-N.png + thumb-N.json {texts:[{text,box,fontPx,claims}], graphics:{claims,what}}.
//   NODE_PATH=$(npm root -g) node episodes/ep004/design/g2/thumbs.js
// Mọi chữ số lấy từ `display` của out/claims.json; đường US lấy từ data/USSTHPI.csv (cùng công thức model: giá × chỉ số/TB 2000 − giá).
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const EP = path.join(__dirname, '..', '..'), OUT = path.join(EP, 'out', 'package');
const FONTS = path.join(EP, '..', '..', 'toolkit', 'render', 'fonts');
const C = Object.fromEntries(JSON.parse(fs.readFileSync(path.join(EP, 'out', 'claims.json'))).claims.map((c) => [c.claimId, c]));
const d = (id) => { if (!C[id] || C[id].display == null) throw new Error('claim ' + id); return C[id].display; };
const BG = '#090f11', INK = '#f2f3f5', WARN = '#ecb03c', MUTE = '#9aa3ad', BLUE = '#5b8def';
const METROS = ['chicago', 'san_francisco', 'san_jose', 'denver', 'boston', 'dallas', 'new_york', 'seattle', 'phoenix', 'san_diego', 'los_angeles', 'miami'];
const NAME = { chicago: 'Chicago', san_francisco: 'San Francisco', san_jose: 'San Jose', denver: 'Denver', boston: 'Boston', dallas: 'Dallas', new_york: 'New York', seattle: 'Seattle', phoenix: 'Phoenix', san_diego: 'San Diego', los_angeles: 'Los Angeles', miami: 'Miami' };
const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
// t(id, x, y, px, text, claims, opts) → logged hero/support text
function T(id, x, y, px, s, claims, o = {}) { return { id, x, y, px, s, claims, w: o.w || 700, fill: o.fill || INK, anchor: o.anchor || 'start' }; }
const txt = (t) => `<text data-id="${t.id}" x="${t.x}" y="${t.y}" font-size="${t.px}" font-weight="${t.w}" fill="${t.fill}" text-anchor="${t.anchor}">${esc(t.s)}</text>`;
const badge = (x, y) => `<rect x="${x}" y="${y}" width="196" height="44" rx="8" fill="${WARN}"/><text data-id="badge" x="${x + 98}" y="${y + 31}" font-size="26" font-weight="700" fill="#111" text-anchor="middle">ILLUSTRATIVE</text>`;
const foot = T('foot', 1240, 694, 26, `US only · ${d('ctx_history')}`, ['ctx_us_only', 'ctx_history'], { w: 400, fill: MUTE, anchor: 'end' });
const num = (id) => C[id].value;

function thumb1() { // 11 of 12 past the cap — bars of gains, $300,000 bought in 2000
  const cap = num('excl_joint_limit_usd'), max = Math.max(...METROS.map((m) => num('gain_at_300k_' + m)));
  const x0 = 700, x1 = 1230, y0 = 110, bh = 32, g = 12, sc = (v) => x0 + (x1 - x0) * v / max;
  let g1 = METROS.map((m, i) => { const v = num('gain_at_300k_' + m), y = y0 + i * (bh + g); return `<rect x="${x0}" y="${y}" width="${sc(v) - x0}" height="${bh}" fill="${v > cap ? WARN : INK}"/>`; }).join('');
  g1 += `<line x1="${sc(cap)}" y1="${y0 - 14}" x2="${sc(cap)}" y2="${y0 + 12 * (bh + g)}" stroke="${INK}" stroke-width="5" stroke-dasharray="12 8"/>`;
  const texts = [T('h1', 48, 250, 150, `${d('metros_crossed_at_300k')} of ${d('metro_count')}`, ['metros_crossed_at_300k', 'metro_count']),
    T('h2', 52, 345, 60, 'metros past the cap', ['excl_joint_limit_usd']),
    T('s1', 52, 440, 34, `${d('illustrative_price_300k_usd')} home bought in ${d('buy_year')}`, ['illustrative_price_300k_usd', 'buy_year'], { w: 600 }),
    T('s2', 52, 484, 34, 'that rose like its metro average', [], { w: 600 }),
    T('s3', sc(cap), y0 - 24, 30, `${d('excl_joint_limit_usd')} cap`, ['excl_joint_limit_usd'], { w: 600, anchor: 'middle' }), foot];
  return { body: g1 + badge(52, 520), texts, graphics: { claims: METROS.map((m) => 'gain_at_300k_' + m).concat(['excl_joint_limit_usd', 'metros_crossed_at_300k', 'sale_quarter', 'illustrative_price_300k_usd']),
    what: '12 metro bars: gain to 2026 Q2 of a $300,000 2000 purchase that rose like the metro index; amber = past the dashed $500,000 cap line (11), white = Chicago (under). ILLUSTRATIVE badge.' } };
}
function thumb2() { // Cap fixed, prices x3.1 — US $300,000 gain line crossing the $500,000 cap
  const rows = fs.readFileSync(path.join(EP, 'data', 'USSTHPI.csv'), 'utf8').trim().split('\n').slice(1).map((l) => l.split(',')).map(([dt, v]) => [dt, +v]).filter(([dt]) => dt >= '2000');
  const base = rows.filter(([dt]) => dt < '2001').reduce((a, [, v]) => a + v, 0) / 4, P = 300000, cap = num('excl_joint_limit_usd');
  const gain = rows.map(([dt, v]) => [dt, P * v / base - P]), last = gain[gain.length - 1][1];
  if (Math.abs(last - num('gain_at_300k_us')) > 1000) throw new Error('US gain mismatch ' + last);
  const xa = 660, xb = 1230, ya = 600, yb = 150, top = 700000, X = (i) => xa + (xb - xa) * i / (gain.length - 1), Y = (v) => ya - (ya - yb) * v / top;
  const pts = gain.map(([, v], i) => `${X(i).toFixed(1)},${Y(v).toFixed(1)}`).join(' ');
  const ic = gain.findIndex(([, v]) => v > cap);
  const body = `<line x1="${xa}" y1="${ya}" x2="${xb}" y2="${ya}" stroke="${MUTE}" stroke-width="2"/>` +
    `<line x1="${xa}" y1="${Y(cap)}" x2="${xb}" y2="${Y(cap)}" stroke="${INK}" stroke-width="6"/>` +
    `<polyline points="${pts}" fill="none" stroke="${BLUE}" stroke-width="7" stroke-linejoin="round"/>` +
    `<polyline points="${gain.slice(ic - 1).map(([, v], j) => `${X(ic - 1 + j).toFixed(1)},${Y(v).toFixed(1)}`).join(' ')}" fill="none" stroke="${WARN}" stroke-width="8" stroke-linejoin="round"/>` + badge(1034, 520);
  const texts = [T('h1', 48, 200, 96, `Cap: ${d('excl_joint_limit_usd')}`, ['excl_joint_limit_usd']),
    T('h2', 48, 320, 96, `Prices: ${d('growth_us')}`, ['growth_us']),
    T('s1', 52, 400, 36, `US average, ${d('buy_year')} → ${d('sale_quarter')}`, ['buy_year', 'sale_quarter', 'growth_us'], { w: 600 }),
    T('s2', 52, 446, 36, `cap since ${d('exclusion_effective_month')}`, ['exclusion_effective_month'], { w: 600 }),
    T('s3', xa, Y(cap) - 16, 30, `${d('excl_joint_limit_usd')} cap`, ['excl_joint_limit_usd'], { w: 600 }),
    T('s4', xb, 640, 26, `gain: ${d('illustrative_price_300k_usd')} home that rose like the US average`, ['illustrative_price_300k_usd', 'gain_at_300k_us'], { w: 400, fill: MUTE, anchor: 'end' }),
    T('x0', xa, ya + 0, 1, '', []), foot].filter((t) => t.s);
  return { body, texts, graphics: { claims: ['gain_at_300k_us', 'cross_quarter_at_300k_us', 'excl_joint_limit_usd', 'illustrative_price_300k_usd', 'buy_year', 'sale_quarter'],
    what: 'gain path 2000 → 2026 Q2 of a $300,000 2000 purchase that rose like the US (FHFA USSTHPI) index; flat $500,000 cap line; amber from the first quarter over (2023 Q2). No axis numbers. ILLUSTRATIVE badge.' } };
}
function thumb3() { // threshold range: Miami ≈ $114,700 … Chicago ≈ $373,400 — dot strip of 12 metro thresholds
  const vals = METROS.map((m) => [m, num('threshold_joint_' + m)]), lo = 80000, hi = 400000, xa = 80, xb = 1200, X = (v) => xa + (xb - xa) * (v - lo) / (hi - lo), yl = 470;
  if (d('threshold_joint_min_metro') !== 'Miami' || d('threshold_joint_max_metro') !== 'Chicago') throw new Error('min/max metro');
  let body = `<line x1="${xa}" y1="${yl}" x2="${xb}" y2="${yl}" stroke="${MUTE}" stroke-width="3"/>`;
  body += vals.map(([m, v]) => `<circle cx="${X(v).toFixed(1)}" cy="${yl}" r="${m === 'miami' || m === 'chicago' ? 20 : 13}" fill="${m === 'miami' ? WARN : m === 'chicago' ? INK : '#6b7480'}"/>`).join('');
  const texts = [T('h1', 48, 150, 92, `Miami ${d('threshold_joint_min')}`, ['threshold_joint_min_metro', 'threshold_joint_min'], { fill: WARN }),
    T('h2', 48, 260, 92, `Chicago ${d('threshold_joint_max')}`, ['threshold_joint_max_metro', 'threshold_joint_max']),
    T('s1', 52, 340, 38, `${d('buy_year')} price where the gain passes ${d('excl_joint_limit_usd')}`, ['buy_year', 'excl_joint_limit_usd', 'threshold_joint_min', 'threshold_joint_max'], { w: 600 }),
    T('s2', 52, 388, 38, 'home that rose like its metro average', [], { w: 600 }),
    T('s3', X(num('threshold_joint_min')), yl + 62, 32, 'Miami', ['threshold_joint_min_metro'], { w: 600, anchor: 'middle', fill: WARN }),
    T('s4', X(num('threshold_joint_max')), yl + 62, 32, 'Chicago', ['threshold_joint_max_metro'], { w: 600, anchor: 'middle' }),
    T('s5', 640, yl + 120, 28, `${d('metro_count')} metros · lower dot = cap reached at a lower ${d('buy_year')} price`, ['metro_count', 'buy_year'], { w: 400, fill: MUTE, anchor: 'middle' }), foot];
  return { body, texts, graphics: { claims: METROS.map((m) => 'threshold_joint_' + m).concat(['threshold_joint_min', 'threshold_joint_max', 'threshold_joint_min_metro', 'threshold_joint_max_metro', 'metro_count']),
    what: 'dot strip of the 12 metro thresholds (2000 purchase price above which an index-typical gain passes $500,000) on a $80k–$400k scale, no axis numbers; Miami (lowest, amber) and Chicago (highest, white) enlarged.' } };
}
(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const b = await chromium.launch({ args: ['--font-render-hinting=none', '--disable-lcd-text'] }); const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
  const ff = [400, 600, 700].map((w) => `@font-face{font-family:Inter;font-weight:${w};src:url(file://${FONTS}/inter-latin-${w}-normal.woff2) format('woff2')}`).join('');
  for (const [n, fn] of [[1, thumb1], [2, thumb2], [3, thumb3]]) {
    const t = fn();
    const html = `<!doctype html><html><head><meta charset="utf-8"><style>${ff}html,body{margin:0;background:${BG}}svg{display:block;font-family:Inter}</style></head><body>` +
      `<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720"><rect width="1280" height="720" fill="${BG}"/>${t.body}${t.texts.map(txt).join('')}</svg></body></html>`;
    const f = path.join(OUT, `.thumb-${n}.html`); fs.writeFileSync(f, html);
    await p.goto('file://' + f); await p.evaluate(() => document.fonts.ready);
    const boxes = await p.evaluate(() => Object.fromEntries([...document.querySelectorAll('text[data-id]')].map((e) => { const r = e.getBBox(); return [e.dataset.id, [r.x, r.y, r.width, r.height].map((v) => Math.round(v * 10) / 10)]; })));
    await p.screenshot({ path: path.join(OUT, `thumb-${n}.png`) }); fs.unlinkSync(f);
    for (const [k, bx] of Object.entries(boxes)) if (bx[0] < 0 || bx[1] < 0 || bx[0] + bx[2] > 1280 || bx[1] + bx[3] > 720) throw new Error(`thumb ${n} ${k} off canvas ${bx}`);
    const texts = t.texts.map((x) => ({ text: x.s, box: boxes[x.id], fontPx: x.px, claims: x.claims }));
    texts.push({ text: 'ILLUSTRATIVE', box: boxes.badge || null, fontPx: 26, claims: ['illustrative_price_300k_usd'] });
    if (!boxes.badge) texts.pop();
    fs.writeFileSync(path.join(OUT, `thumb-${n}.json`), JSON.stringify({ texts, graphics: t.graphics }, null, 1));
    console.log(n, texts.map((x) => x.text).join(' | '));
  }
  await b.close();
})();
