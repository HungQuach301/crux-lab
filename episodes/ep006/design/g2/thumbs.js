// Tập 6 · C5b: 3 thumbnail 1280×720 → out/package/thumb-N.png + thumb-N.json {texts:[{text,box,fontPx,claims}], graphics:{claims,what}} (mẫu: ep005/design/g2/thumbs.js).
//   NODE_PATH=$(npm root -g) node episodes/ep006/design/g2/thumbs.js
// Mọi chữ số lấy từ `display` của out/claims.json; cột 715 khung 20 năm lấy từ out/model.json raw.windows (cùng dữ liệu của đoạn thế giới d).
// Claim-risk (K-brief Tập 6): "kept up" = mua được ít nhất bằng séc đầu của chính nó (CPI-U); không số tiền, không "tổng", không khuyên chọn séc/mức tăng/công ty;
// ba người hưu có ILLUSTRATIVE; mọi khung có "US only · history, not a forecast". Màu: chỉ token design/tokens.json.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const EP = path.join(__dirname, '..', '..'), OUT = path.join(EP, 'out', 'package');
const FONTS = path.join(EP, '..', '..', 'toolkit', 'render', 'fonts');
const C = Object.fromEntries(JSON.parse(fs.readFileSync(path.join(EP, 'out', 'claims.json'))).claims.map((c) => [c.claimId, c]));
const d = (id) => { if (!C[id] || C[id].display == null) throw new Error('claim ' + id); return C[id].display; };
const TK = JSON.parse(fs.readFileSync(path.join(EP, 'design', 'tokens.json'))).colors;
const BG = TK.bg, INK = TK.ink, WARN = TK.warn, MUTE = TK['ink-muted'], GRID = TK.grid, KEPT = TK.cushion;
const RUTH = TK['char-ruth'], CARL = TK['char-carl'], EDNA = TK['char-edna'];
const RAW = JSON.parse(fs.readFileSync(path.join(EP, 'out', 'model.json'))).raw;
const WIN = RAW.windows;
if (WIN.length !== C.windows_20y.value) throw new Error('windows ≠ windows_20y');
if (WIN.filter((w) => w.real_2pct_pct >= 100).length !== C.windows_2pct_kept_up_20y.value) throw new Error('kept ≠ windows_2pct_kept_up_20y');
const at = (m) => { const w = WIN.find((x) => x.start === m); if (!w) throw new Error('window ' + m); return w.real_2pct_pct; };
const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
function T(id, x, y, px, s, claims, o = {}) { return { id, x, y, px, s, claims, w: o.w || 700, fill: o.fill || INK, anchor: o.anchor || 'start' }; }
const txt = (t) => `<text data-id="${t.id}" x="${t.x}" y="${t.y}" font-size="${t.px}" font-weight="${t.w}" fill="${t.fill}" text-anchor="${t.anchor}">${esc(t.s)}</text>`;
// checks P01: chữ nội dung ≥ 90 px; hai nhãn bắt buộc (ILLUSTRATIVE, "US only · history, not a forecast") nhỏ nhưng ĐẬM trên nền đặc (như Tập 5)
const badge = (x, y, claims) => ({ svg: `<rect x="${x}" y="${y}" width="300" height="64" rx="10" fill="${WARN}"/><text data-id="badge" x="${x + 150}" y="${y + 46}" font-size="40" font-weight="700" fill="${BG}" text-anchor="middle">ILLUSTRATIVE</text>`, claims });
const foot = () => T('foot', 1240, 700, 40, 'US only · history, not a forecast', [], { w: 700, fill: INK, anchor: 'end' });

// 715 cột khung 20 năm (chiều cao = séc tăng 2 %/năm sau 20 lần tăng, % sức mua của séc đầu), vạch 100 % = séc đầu; tô theo col(w)
function windowBars(x0, x1, yb, hTop, col) {
  const max = Math.max(...WIN.map((w) => w.real_2pct_pct)), w = (x1 - x0) / WIN.length, y100 = yb - hTop * 100 / max;
  return WIN.map((v, i) => `<rect x="${(x0 + i * w).toFixed(2)}" y="${(yb - hTop * v.real_2pct_pct / max).toFixed(2)}" width="${Math.max(0.6, w).toFixed(2)}" height="${(hTop * v.real_2pct_pct / max).toFixed(2)}" fill="${col(v)}"/>`).join('') +
    `<rect x="${x0}" y="${yb}" width="${x1 - x0}" height="3" fill="${MUTE}"/><rect x="${x0 - 8}" y="${(y100 - 2).toFixed(1)}" width="${x1 - x0 + 16}" height="4" fill="${INK}"/>`;
}

function thumb1() { // 17 of 715 kept up — the early cluster lit
  const body = windowBars(800, 1236, 600, 470, (w) => (w.real_2pct_pct >= 100 ? KEPT : GRID));
  const texts = [T('h1', 44, 200, 120, `${d('windows_2pct_kept_up_20y')} of ${d('windows_20y')}`, ['windows_2pct_kept_up_20y', 'windows_20y']),
    T('h2', 48, 320, 96, 'kept up', ['windows_2pct_kept_up_20y'], { fill: KEPT }),
    T('h3', 48, 440, 90, `${d('raise_2pct')} a year`, ['raise_2pct']), foot()];
  return { body, texts, graphics: { claims: ['windows_20y', 'windows_2pct_kept_up_20y', 'first_start_month', 'latest_start', 'main_years'],
    what: `${C.windows_20y.value} bars, one per 20-year stretch starting ${d('first_start_month')}–${d('latest_start')}, height = buying power of the 2%-a-year check after 20 raises vs its own first check (CPI-U); white line = 100% (its first check); the ${C.windows_2pct_kept_up_20y.value} bars at or above it in green, the rest dark. No axis numbers.` } };
}
function thumb2() { // typical stretch: 80.7% after 20 raises — first check vs the typical end, same scale
  const yb = 600, hTop = 440, bw = 150, xa = 900, xb = 1080, med = C.median_real_value_2pct_payment_after_20y_pct.value, hm = hTop * med / 100;
  const body = `<rect x="${xa}" y="${yb - hTop}" width="${bw}" height="${hTop}" fill="${MUTE}"/><rect x="${xb}" y="${yb - hm}" width="${bw}" height="${hm}" fill="${WARN}"/>` +
    `<rect x="${xa - 30}" y="${yb}" width="${xb + bw - xa + 60}" height="3" fill="${MUTE}"/>`;
  const texts = [T('h1', 44, 210, 150, d('median_real_value_2pct_payment_after_20y_pct'), ['median_real_value_2pct_payment_after_20y_pct'], { fill: WARN }),
    T('h2', 48, 330, 90, `after ${d('main_years_raises')}`, ['main_years_raises']),
    T('h3', 48, 450, 90, 'typically', ['median_real_value_2pct_payment_after_20y_pct']), foot()];
  return { body, texts, graphics: { claims: ['median_real_value_2pct_payment_after_20y_pct', 'main_years_raises', 'raise_2pct'],
    what: `two bars on one scale: grey = the first check's buying power (100%), amber = the typical (median) 2%-a-year check after 20 raises (${d('median_real_value_2pct_payment_after_20y_pct')}). No axis numbers.` } };
}
function thumb3() { // same 2% raise, three ILLUSTRATIVE start months: Edna kept up, Ruth 90.4%, Carl 43.1%
  const yb = 560, hTop = 380, bw = 110, xs = [880, 1010, 1140];
  const vals = [[at(C.kept_up_last_start_20y.value), EDNA], [C.guide_real_2pct_end_pct.value, RUTH], [C.worst_real_value_2pct_payment_after_20y_pct.value, CARL]];
  const max = Math.max(...vals.map((v) => v[0]));
  const bd = badge(48, 540, ['kept_up_last_start_20y', 'guide_real_2pct_end_pct', 'worst_real_value_2pct_payment_after_20y_pct']);
  const body = vals.map(([v, c], i) => `<rect x="${xs[i]}" y="${(yb - hTop * v / max).toFixed(1)}" width="${bw}" height="${(hTop * v / max).toFixed(1)}" fill="${c}"/>`).join('') +
    `<rect x="${xs[0] - 20}" y="${yb}" width="${xs[2] + bw - xs[0] + 40}" height="3" fill="${MUTE}"/>` + bd.svg;
  const texts = [T('h1', 44, 170, 96, `Same ${d('raise_2pct')} raise`, ['raise_2pct']),
    T('h2', 44, 290, 96, `Ruth: ${d('guide_real_2pct_end_pct')}`, ['guide_real_2pct_end_pct'], { fill: RUTH }),
    T('h3', 44, 410, 96, `Carl: ${d('worst_real_value_2pct_payment_after_20y_pct')}`, ['worst_real_value_2pct_payment_after_20y_pct'], { fill: CARL }), foot()];
  return { body, texts, badgeClaims: bd.claims, graphics: { claims: ['kept_up_last_start_20y', 'guide_real_2pct_end_pct', 'worst_real_value_2pct_payment_after_20y_pct', 'main_years_raises'],
    what: `three bars, same scale, buying power of the 2%-a-year check after 20 raises vs its own first check for the three ILLUSTRATIVE retirees, in their colours: Edna (start ${d('kept_up_last_start_20y')}, kept up), Ruth (start ${d('guide_start')}, ${d('guide_real_2pct_end_pct')}), Carl (start ${d('worst_window_start_year_20y')}, ${d('worst_real_value_2pct_payment_after_20y_pct')}). No axis numbers. ILLUSTRATIVE badge.` } };
}
(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const b = await chromium.launch({ args: ['--font-render-hinting=none', '--disable-lcd-text'] }); const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
  const ff = [400, 600, 700].map((w) => `@font-face{font-family:Inter;font-weight:${w};src:url(file://${FONTS}/inter-latin-${w}-normal.woff2) format('woff2')}`).join('');
  for (const [n, fn, chartX] of [[1, thumb1, 800], [2, thumb2, 870], [3, thumb3, 860]]) {
    const t = fn();
    const html = `<!doctype html><html><head><meta charset="utf-8"><style>${ff}html,body{margin:0;background:${BG}}svg{display:block;font-family:Inter}rect{shape-rendering:crispEdges}</style></head><body>` +
      `<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720"><rect width="1280" height="720" fill="${BG}"/>${t.body}${t.texts.map(txt).join('')}</svg></body></html>`;
    const f = path.join(OUT, `.thumb-${n}.html`); fs.writeFileSync(f, html);
    await p.goto('file://' + f); await p.evaluate(() => document.fonts.ready);
    const boxes = await p.evaluate(() => Object.fromEntries([...document.querySelectorAll('text[data-id]')].map((e) => { const r = e.getBBox(); return [e.dataset.id, [r.x, r.y, r.width, r.height].map((v) => Math.round(v * 10) / 10)]; })));
    await p.screenshot({ path: path.join(OUT, `thumb-${n}.png`) }); fs.unlinkSync(f);
    for (const [k, bx] of Object.entries(boxes)) {
      if (bx[0] < 0 || bx[1] < 0 || bx[0] + bx[2] > 1280 || bx[1] + bx[3] > 720) throw new Error(`thumb ${n} ${k} off canvas ${bx}`);
      if (/^h/.test(k) && bx[0] + bx[2] > chartX - 10) throw new Error(`thumb ${n} ${k} runs into the chart ${bx}`);
    }
    const texts = t.texts.map((x) => ({ text: x.s, box: boxes[x.id], fontPx: x.px, claims: x.claims }));
    if (boxes.badge) texts.push({ text: 'ILLUSTRATIVE', box: boxes.badge, fontPx: 40, claims: t.badgeClaims });
    fs.writeFileSync(path.join(OUT, `thumb-${n}.json`), JSON.stringify({ texts, graphics: t.graphics }, null, 1));
    console.log(n, texts.map((x) => x.text).join(' | '));
  }
  await b.close();
})();
