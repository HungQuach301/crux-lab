// Tập 6 · C5c: 3 thumbnail 1280×720 → out/package/thumb-N.png + thumb-N.json {texts:[{text,box,fontPx,claims}], graphics:{claims,what}} (luật: playbook/episode.md §5 "Thumbnail bằng hình thế giới 3D").
//   NODE_PATH=$(npm root -g) node toolkit/factory/world/render_shots.js episodes/ep006/world/c4/b-s04-s08 1080 /tmp/thumbs/b.mp4 --stills 70.2 --stills-dir /tmp/thumbs
//   NODE_PATH=$(npm root -g) node episodes/ep006/design/g2/thumbs.js [/tmp/thumbs/b-s04-s08-t70.20.png]
// thumb-1 = khung thế giới + 4 từ, thumb-2 = khung thế giới + 1 số "on paper", thumb-3 = đối chứng 2D (thumb-1 cũ của C5b, 17 of 715).
// Khung thế giới: đoạn b giây 70.2 (cuối S07.1 "her check grew … buys less": séc Ruth sau 20 lần tăng, thùng cuối tối), render 1080 rồi cắt.
// Mọi chữ số lấy từ `display` của out/claims.json; cột 715 khung 20 năm lấy từ out/model.json raw.windows (cùng dữ liệu của đoạn thế giới d).
// Claim-risk (K-brief Tập 6): "kept up" = mua được ít nhất bằng séc đầu của chính nó (CPI-U); không số tiền, không "tổng", không khuyên chọn séc/mức tăng/công ty;
// ba người hưu có ILLUSTRATIVE; mọi khung có "US only · history, not a forecast". Màu: chỉ token design/tokens.json.
const { chromium } = require('playwright');
const { pathToFileURL } = require('url');
const fs = require('fs'), path = require('path');
const EP = path.join(__dirname, '..', '..'), OUT = path.join(EP, 'out', 'package');
const FONTS = path.join(EP, '..', '..', 'toolkit', 'render', 'fonts');
const C = Object.fromEntries(JSON.parse(fs.readFileSync(path.join(EP, 'out', 'claims.json'))).claims.map((c) => [c.claimId, c]));
const d = (id) => { if (!C[id] || C[id].display == null) throw new Error('claim ' + id); return C[id].display; };
const TK = JSON.parse(fs.readFileSync(path.join(EP, 'design', 'tokens.json'))).colors;
const BG = TK.bg, INK = TK.ink, WARN = TK.warn, MUTE = TK['ink-muted'], GRID = TK.grid, KEPT = TK.cushion;
const RAW = JSON.parse(fs.readFileSync(path.join(EP, 'out', 'model.json'))).raw;
const WIN = RAW.windows;
if (WIN.length !== C.windows_20y.value) throw new Error('windows ≠ windows_20y');
if (WIN.filter((w) => w.real_2pct_pct >= 100).length !== C.windows_2pct_kept_up_20y.value) throw new Error('kept ≠ windows_2pct_kept_up_20y');
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

// Khung thế giới 1920×1080 cắt x 140–1780, y 158–1080 (Ruth + séc + hàng thùng ở y ≈ 88–417), dải BG đặc trên cùng (chân/nhãn của thumbnail),
// dải BG mờ dần ở dưới (che chân cảnh, nền cho chữ lớn). ILLUSTRATIVE vì có người; "US only · history, not a forecast" trên mọi khung.
const FRAME = process.argv[2] || '/tmp/thumbs/b-s04-s08-t70.20.png', FRAME_T = 70.2, CX = 140, CY = 158, CS = 1280 / 1640;
const RUTH_CLAIMS = ['guide_start', 'guide_real_2pct_end_pct', 'crates_ruth', 'crates_full', 'main_years_raises'];
function world() {
  const img = 'data:image/png;base64,' + fs.readFileSync(FRAME).toString('base64');
  const bd = badge(940, 8, RUTH_CLAIMS);
  return { bd, body: `<defs><linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${BG}" stop-opacity="0"/><stop offset="0.25" stop-color="${BG}" stop-opacity="0.95"/><stop offset="0.45" stop-color="${BG}"/></linearGradient></defs>` +
    `<image href="${img}" x="${-CX * CS}" y="${-CY * CS}" width="${1920 * CS}" height="${1080 * CS}"/><rect width="1280" height="78" fill="${BG}"/><rect y="425" width="1280" height="295" fill="url(#fade)"/>` + bd.svg,
  what: `world frame, segment b (b-s04-s08) at ${FRAME_T}s (end of S07.1 "her check grew … buys less"), rendered 1920×1080 and cropped: ILLUSTRATIVE Ruth (no face), her rising check after ${d('main_years_raises')}, her row of ${d('crates_full')} crates with the last one dark (buys ${d('crates_ruth')}). No numbers in the frame; scene chrome cropped/covered and redrawn as the badge and footer.` };
}
const footTop = () => T('foot', 40, 54, 40, 'US only · history, not a forecast', [], { w: 700, fill: INK });
function thumb1() { // world + 4 words: the check got bigger, it buys less
  const w = world();
  const texts = [T('h1', 40, 560, 120, 'Bigger check.', ['raise_2pct', 'two_pct_growth_20y_pct']),
    T('h2', 40, 682, 120, 'Buys less?', ['guide_real_2pct_end_pct', 'crates_ruth'], { fill: WARN }), footTop()];
  return { body: w.body, texts, badgeClaims: w.bd.claims, graphics: { claims: RUTH_CLAIMS, what: w.what } };
}
function thumb2() { // world + one "on paper" number: the 2% check grew 48.6% in 20 raises
  const w = world();
  const texts = [T('h1', 36, 596, 170, `+${d('two_pct_growth_20y_pct')}`, ['two_pct_growth_20y_pct']),
    T('h2', 44, 690, 96, 'on paper', ['two_pct_growth_20y_pct'], { fill: WARN }), footTop()];
  return { body: w.body, texts, badgeClaims: w.bd.claims, graphics: { claims: [...RUTH_CLAIMS, 'two_pct_growth_20y_pct'], what: w.what } };
}
function thumb3() { // đối chứng 2D (thumb-1 của C5b): 17 of 715 kept up — the early cluster lit
  const body = windowBars(800, 1236, 600, 470, (w) => (w.real_2pct_pct >= 100 ? KEPT : GRID));
  const texts = [T('h1', 44, 200, 120, `${d('windows_2pct_kept_up_20y')} of ${d('windows_20y')}`, ['windows_2pct_kept_up_20y', 'windows_20y']),
    T('h2', 48, 320, 96, 'kept up', ['windows_2pct_kept_up_20y'], { fill: KEPT }),
    T('h3', 48, 440, 90, `${d('raise_2pct')} a year`, ['raise_2pct']), foot()];
  return { body, texts, graphics: { claims: ['windows_20y', 'windows_2pct_kept_up_20y', 'first_start_month', 'latest_start', 'main_years'],
    what: `${C.windows_20y.value} bars, one per 20-year stretch starting ${d('first_start_month')}–${d('latest_start')}, height = buying power of the 2%-a-year check after 20 raises vs its own first check (CPI-U); white line = 100% (its first check); the ${C.windows_2pct_kept_up_20y.value} bars at or above it in green, the rest dark. No axis numbers.` } };
}
(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const b = await chromium.launch({ args: ['--font-render-hinting=none', '--disable-lcd-text'] }); const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
  const ff = [400, 600, 700].map((w) => `@font-face{font-family:Inter;font-weight:${w};src:url(${pathToFileURL(path.join(FONTS, `inter-latin-${w}-normal.woff2`)).href}) format('woff2')}`).join('');
  for (const [n, fn, chartX] of [[1, thumb1, 1280], [2, thumb2, 1280], [3, thumb3, 800]]) {
    const t = fn();
    const html = `<!doctype html><html><head><meta charset="utf-8"><style>${ff}html,body{margin:0;background:${BG}}svg{display:block;font-family:Inter}rect{shape-rendering:crispEdges}</style></head><body>` +
      `<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720"><rect width="1280" height="720" fill="${BG}"/>${t.body}${t.texts.map(txt).join('')}</svg></body></html>`;
    const f = path.join(OUT, `.thumb-${n}.html`); fs.writeFileSync(f, html);
    await p.goto(pathToFileURL(f).href); await p.evaluate(() => document.fonts.ready);
    const boxes = await p.evaluate(() => Object.fromEntries([...document.querySelectorAll('text[data-id]')].map((e) => { const r = e.getBBox(); return [e.dataset.id, [r.x, r.y, r.width, r.height].map((v) => Math.round(v * 10) / 10)]; })));
    await p.screenshot({ path: path.join(OUT, `thumb-${n}.png`) }); fs.unlinkSync(f);
    for (const [k, bx] of Object.entries(boxes)) {
      if (bx[0] < 0 || bx[1] < 0 || bx[0] + bx[2] > 1280 || bx[1] + bx[3] > 720) throw new Error(`thumb ${n} ${k} off canvas ${bx}`);
      if (/^h/.test(k) && bx[0] + bx[2] > chartX - 10) throw new Error(`thumb ${n} ${k} runs into the chart ${bx}`);
      if (n < 3 && /^h/.test(k) && bx[1] < 425) throw new Error(`thumb ${n} ${k} runs into the world frame ${bx}`);
    }
    const texts = t.texts.map((x) => ({ text: x.s, box: boxes[x.id], fontPx: x.px, claims: x.claims }));
    if (boxes.badge) texts.push({ text: 'ILLUSTRATIVE', box: boxes.badge, fontPx: 40, claims: t.badgeClaims });
    fs.writeFileSync(path.join(OUT, `thumb-${n}.json`), JSON.stringify({ texts, graphics: t.graphics }, null, 1));
    console.log(n, texts.map((x) => x.text).join(' | '));
  }
  await b.close();
})();
