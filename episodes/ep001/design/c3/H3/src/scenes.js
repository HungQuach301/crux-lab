'use strict';
// H3 "Hình học của tiền": height/area = dollars, x = time. Three motions only: draw (time passes), fill (money
// accumulates), grow/shrink (an amount appears or goes away). Colours: episode tokens (design/tokens.json).
(function () {
  const D = window.DATA;
  const CL = (id) => D.claims[id].display; // every on-screen number goes through here
  const C = {
    bg: '#0e1116', surface: '#171b22', ink: '#f2f4f7', dim: '#9aa4b2', grid: '#2a303b',
    accent: '#4c8dff', warn: '#f2b441', pos: '#3fbf7f', neg: '#e5484d',
  };
  const W = 1280, H = 720;
  const cv = document.getElementById('c');
  const g = cv.getContext('2d');

  // ---------- helpers ----------
  const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
  const seg = (t, a, b) => clamp((t - a) / (b - a));
  const ease = (x) => (x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2);
  const eOut = (x) => 1 - Math.pow(1 - x, 3);
  const lerp = (a, b, x) => a + (b - a) * x;
  function rgba(hex, a) {
    const n = parseInt(hex.slice(1), 16);
    return `rgba(${n >> 16},${(n >> 8) & 255},${n & 255},${a})`;
  }
  function text(s, x, y, o = {}) {
    const a = o.alpha === undefined ? 1 : o.alpha;
    if (a <= 0.001) return 0;
    g.save();
    g.globalAlpha = a;
    g.font = `${o.weight || 400} ${o.size || 20}px Inter`;
    g.fillStyle = o.color || C.ink;
    g.textAlign = o.align || 'left';
    g.textBaseline = o.base || 'alphabetic';
    g.fillText(s, x, y);
    const w = g.measureText(s).width;
    g.restore();
    return w;
  }
  function tw(s, size, weight) { g.save(); g.font = `${weight || 400} ${size}px Inter`; const w = g.measureText(s).width; g.restore(); return w; }
  function badge(x, y, a = 1) { // ILLUSTRATIVE pill; (x, y) = left, vertical centre
    if (a <= 0.001) return 0;
    const s = 'ILLUSTRATIVE', w = tw(s, 11, 700) + 12;
    g.save(); g.globalAlpha = a; g.fillStyle = C.warn;
    g.beginPath(); g.roundRect(x, y - 9, w, 18, 4); g.fill();
    g.restore();
    text(s, x + 6, y + 4, { size: 11, weight: 700, color: C.bg, alpha: a });
    return w;
  }
  function line(pts, color, lw, o = {}) {
    g.save(); g.globalAlpha = o.alpha === undefined ? 1 : o.alpha;
    g.strokeStyle = color; g.lineWidth = lw; g.lineJoin = 'round'; g.lineCap = o.cap || 'round';
    if (o.dash) g.setLineDash(o.dash);
    g.beginPath(); pts.forEach((p, i) => (i ? g.lineTo(p[0], p[1]) : g.moveTo(p[0], p[1]))); g.stroke();
    g.restore();
  }
  function rect(x, y, w, h, fill, a = 1) { if (a <= 0.001 || h === 0) return; g.save(); g.globalAlpha = a; g.fillStyle = fill; g.fillRect(x, y, w, h); g.restore(); }
  function strokeRect(x, y, w, h, color, lw, a = 1, dash) { if (a <= 0.001) return; g.save(); g.globalAlpha = a; g.strokeStyle = color; g.lineWidth = lw; if (dash) g.setLineDash(dash); g.strokeRect(x, y, w, h); g.restore(); }
  function hatch(x, y, w, h, color, a, step = 9) { // diagonal hatch = "hidden / owed" pattern
    if (a <= 0.001 || h <= 0) return;
    g.save(); g.globalAlpha = a; g.beginPath(); g.rect(x, y, w, h); g.clip();
    g.strokeStyle = color; g.lineWidth = 2;
    g.beginPath();
    for (let k = -h; k < w + h; k += step) { g.moveTo(x + k, y + h); g.lineTo(x + k + h, y); }
    g.stroke(); g.restore();
  }
  function tri(cx, cy, r, color, a = 1) { g.save(); g.globalAlpha = a; g.fillStyle = color; g.beginPath(); g.moveTo(cx, cy - r); g.lineTo(cx + r * 0.95, cy + r * 0.7); g.lineTo(cx - r * 0.95, cy + r * 0.7); g.closePath(); g.fill(); g.restore(); }
  function sq(cx, cy, r, color, a = 1) { rect(cx - r * 0.8, cy - r * 0.8, r * 1.6, r * 1.6, color, a); }
  function dot(cx, cy, r, color, a = 1) { g.save(); g.globalAlpha = a; g.fillStyle = color; g.beginPath(); g.arc(cx, cy, r, 0, 7); g.fill(); g.restore(); }
  function clear() { g.fillStyle = C.bg; g.fillRect(0, 0, W, H); }
  // savings slices: green fill with a dark seam between months (the pattern that separates "saved" from a character colour)
  function slices(x, yBase, w, n, hPer, color, a = 1) {
    if (n <= 0) return;
    const full = Math.floor(n), frac = n - full;
    rect(x, yBase - hPer * n, w, hPer * n, color, a);
    g.save(); g.globalAlpha = a * 0.55; g.fillStyle = C.bg;
    for (let k = 1; k <= full; k++) if (hPer > 3) g.fillRect(x, yBase - hPer * k, w, hPer > 8 ? 2 : 1);
    g.restore();
    return frac;
  }

  // ============ F1 · the missed window ============
  function F1(t) {
    clear();
    const F = D.f1, wk = F.weeks, N = wk.length;
    const X0 = 96, X1 = 860, YB = 600, R0 = 5.5, R1 = 7.8;
    const xOf = (i) => X0 + (i / (N - 1)) * (X1 - X0);
    const yOf = (r) => YB - ((r - R0) / (R1 - R0)) * 490;
    const iLow = wk.findIndex((w) => w.d === F.low), iLast = wk.findIndex((w) => w.d === F.lastIn), iEnd = N - 1;
    // head position (fractional week index) along time
    let hd;
    if (t < 1.8) hd = 0;
    else if (t < 3.8) hd = ease(seg(t, 1.8, 3.8)) * iLow;
    else if (t < 4.6) hd = iLow;
    else if (t < 6.4) hd = lerp(iLow, iLast + 1, ease(seg(t, 4.6, 6.4)));
    else hd = lerp(iLast + 1, iEnd, ease(seg(t, 6.4, 7.6)));
    const out = hd > iLast + 0.5; // line has climbed out of the window
    const tOut = 5.7 + 0.0; // approximate time the head leaves (used only for fades)
    const kOut = clamp((hd - (iLast + 0.5)) / 0.5);

    // title + axis
    const a0 = eOut(seg(t, 0, 0.6));
    text('US 30-year fixed mortgage rate, weekly average', X0, 58, { size: 20, weight: 600, color: C.ink, alpha: a0 });
    text('Freddie Mac PMMS via FRED', X0, 82, { size: 16, color: C.dim, alpha: a0 });
    line([[X0, YB], [X1, YB]], C.grid, 2, { alpha: a0 });
    const months = ['Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'];
    months.forEach((m, j) => {
      const i = wk.findIndex((w) => +w.d.slice(5, 7) === [12, 1, 2, 3, 4, 5, 6, 7, 8, 9][j]);
      text(m, xOf(i), YB + 26, { size: 16, color: C.dim, alpha: a0 });
    });

    // Nora's rate (reference line)
    const aN = eOut(seg(t, 0.3, 1.0));
    const yN = yOf(F.rOld);
    line([[X0, yN], [X0 + (X1 - X0) * aN, yN]], C.dim, 2, { dash: [8, 7] });
    dot(X0, yN, 7, C.pos, aN);
    let w = text("Nora's loan: " + CL('r_old'), X0 + 16, yN - 14, { size: 20, weight: 600, alpha: aN });
    badge(X0 + 26 + w, yN - 20, aN);

    // the window: below Nora's rate minus 1 point
    const yT = yOf(F.thr);
    const aW = eOut(seg(t, 1.0, 1.7));
    const closed = kOut;
    rect(X0, yT, (X1 - X0), YB - yT, lerp(1, 0, closed) > 0 ? C.accent : C.dim, aW * lerp(0.16, 0.05, closed));
    line([[X0, yT], [X0 + (X1 - X0) * aW, yT]], closed > 0.5 ? C.dim : C.accent, 2, { alpha: aW * lerp(1, 0.6, closed) });
    text(CL('r_old') + ' −', X1 + 10, yT - 3, { size: 16, color: C.dim, alpha: aW });
    text(CL('s10') + ' point', X1 + 10, yT + 17, { size: 16, color: C.dim, alpha: aW });
    text('window: refinancing pays', X0 + 12, yT + 28, { size: 20, weight: 600, color: C.accent, alpha: aW * (1 - closed) });
    text('window closed', X0 + 12, yT + 28, { size: 20, weight: 600, color: C.dim, alpha: aW * closed });
    text('after week ending ' + CL('cut1_last_2026'), X0 + 12, yT + 52, { size: 16, color: C.dim, alpha: aW * closed });

    // rate line draws itself
    if (hd > 0 || t >= 1.8) {
      const pts = [];
      const full = Math.floor(hd);
      for (let i = 0; i <= full; i++) pts.push([xOf(i), yOf(wk[i].r)]);
      if (hd > full && full + 1 < N) { const f = hd - full; pts.push([lerp(xOf(full), xOf(full + 1), f), lerp(yOf(wk[full].r), yOf(wk[full + 1].r), f)]); }
      if (pts.length === 1) pts.push(pts[0]);
      line(pts, C.accent, 4, { alpha: eOut(seg(t, 1.8, 2.0)) });
      const h = pts[pts.length - 1];
      dot(h[0], h[1], 6, C.accent, eOut(seg(t, 1.8, 2.0)));
    }

    // low callout
    const aL = eOut(seg(t, 3.7, 4.2));
    const xl = xOf(iLow), yl = yOf(wk[iLow].r);
    dot(xl, yl, 9, C.ink, aL);
    line([[xl, yl + 12], [xl, yl + 30]], C.dim, 1.5, { alpha: aL });
    text(CL('low2026'), xl, yl + 58, { size: 30, weight: 700, align: 'center', alpha: aL });
    text('week ending ' + CL('low2026_date'), xl, yl + 80, { size: 16, color: C.dim, align: 'center', alpha: aL });
    text('lowest since ' + CL('low2026_since'), xl, yl + 100, { size: 16, color: C.dim, align: 'center', alpha: aL });

    // right panel: Nora's monthly saving if she refinanced that week (bar height = dollars)
    const BX = 990, BW = 130, SC = 330 / 459.1;
    const aP = eOut(seg(t, 1.6, 2.2));
    text('If Nora refinanced', BX + BW / 2, 150, { size: 18, weight: 600, align: 'center', alpha: aP });
    text('that week, she would', BX + BW / 2, 172, { size: 18, weight: 600, align: 'center', alpha: aP });
    text('pay less each month', BX + BW / 2, 194, { size: 18, weight: 600, align: 'center', alpha: aP });
    text('nominal $', BX + BW / 2, YB + 26, { size: 16, color: C.dim, align: 'center', alpha: aP });
    line([[BX - 20, YB], [BX + BW + 20, YB]], C.grid, 2, { alpha: aP });
    const iH = clamp(hd, 0, N - 1), i0 = Math.floor(iH), i1 = Math.min(N - 1, i0 + 1);
    const sav = lerp(wk[i0].sav, wk[i1].sav, iH - i0) * eOut(seg(t, 1.8, 2.3));
    // ghost of the best week (appears when the line reaches the low)
    const aG = eOut(seg(t, 3.8, 4.3));
    const hMax = wk[iLow].sav * SC;
    const inWin = !out;
    const barCol = inWin ? C.pos : C.dim;
    const hb = sav * SC;
    rect(BX, YB - hb, BW, hb, barCol, 1);
    if (aG > 0) {
      strokeRect(BX, YB - hMax, BW, hMax, C.ink, 2, aG * (t > 4.6 ? 0.9 : 0), [6, 5]);
      hatch(BX, YB - hMax, BW, hMax - hb, C.dim, 0.35 * closed);
      const ly = YB - hMax - 16;
      w = text(CL('sav_low2026_median') + '/mo', BX + BW / 2 - 40, ly, { size: 30, weight: 700, align: 'center', alpha: aG });
      badge(BX + BW / 2 - 40 + w / 2 + 8, ly - 10, aG);
      text('missed', BX + BW / 2, YB - hMax + 30, { size: 20, weight: 600, color: C.ink, align: 'center', alpha: closed * eOut(seg(t, 6.0, 6.6)) });
    }

    // end: back above 7%
    const aE = eOut(seg(t, 7.5, 8.0));
    const xe = xOf(iEnd), ye = yOf(wk[iEnd].r);
    dot(xe, ye, 9, C.ink, aE);
    text(CL('r_today'), xe - 16, ye - 76, { size: 30, weight: 700, align: 'right', alpha: aE });
    text('week ending ' + CL('anchor_date'), xe - 16, ye - 54, { size: 16, color: C.dim, align: 'right', alpha: aE });
    text('above ' + CL('seven') + '% for the first time since ' + CL('first7_since'), xe - 16, ye - 32, { size: 16, color: C.dim, align: 'right', alpha: aE });
  }

  // ============ F2 · break-even moves from 24 to 30 ============
  function F2(t) {
    clear();
    const M = D.median;
    const BX = 420, BW = 220, YB = 600, SC = 0.075; // px per $
    const RX0 = 120, RX1 = 1160, RY = 668; // month ruler 0..36
    const rx = (m) => RX0 + (m / 36) * (RX1 - RX0);
    // month (fractional) as a function of time
    let m;
    if (t < 1.4) m = 0;
    else if (t < 5.2) m = 24 * seg(t, 1.4, 5.2);
    else if (t < 6.4) m = 24;
    else if (t < 8.6) m = lerp(24, 30, seg(t, 6.4, 8.6));
    else m = 30;
    const mi = Math.floor(m + 1e-6), mf = m - mi;
    const gapAt = (x) => { const a = Math.floor(x), b = Math.min(36, a + 1); return lerp(M.gap[a], M.gap[b], x - a); };

    const a0 = eOut(seg(t, 0, 0.8));
    text('Nora', 96, 70, { size: 26, weight: 700, alpha: a0 });
    badge(96 + tw('Nora', 26, 700) + 12, 62, a0);
    text('Does refinancing pay back the bill?', 96, 98, { size: 18, color: C.dim, alpha: a0 });
    text('nominal $', 1184, 70, { size: 16, color: C.dim, align: 'right', alpha: a0 });

    // the bill: grey outline block, rises from the base
    const hBill = M.cost * SC * ease(seg(t, 0.1, 0.9));
    const yBill = YB - hBill;
    line([[BX - 40, YB], [BX + BW + 40, YB]], C.grid, 2, { alpha: a0 });
    rect(BX, yBill, BW, hBill, C.surface, 1);
    // hidden part: extra balance owed, grows from month 1; faint until month 24, then solid amber
    const reveal = ease(seg(t, 5.55, 6.15));
    const hGap = gapAt(m) * SC;
    const yTop = yBill - hGap;
    if (t > 1.4) {
      rect(BX, yTop, BW, hGap, C.surface, 1);
      hatch(BX, yTop, BW, hGap, C.warn, lerp(0.18, 1, reveal), 10);
      strokeRect(BX, yTop, BW, hGap, C.warn, 2, lerp(0.15, 1, reveal), reveal < 0.5 ? [3, 5] : null);
    }
    // savings: one $221 slice per month, stacked from the bottom; the newest slice drops in
    const hS = M.sav * SC;
    const nDone = mi + (mf > 0 ? eOut(clamp(mf / 0.6)) : 0);
    slices(BX, YB, BW, nDone, hS, C.pos);
    // bill outline on top of the fill (rim = what must be paid back); hidden part outline stays visible over the fill
    strokeRect(BX, yBill, BW, hBill, C.dim, 2, 1);
    if (t > 1.4) strokeRect(BX, yTop, BW, hGap, C.warn, 2, lerp(0.15, 1, reveal), reveal < 0.5 ? [3, 5] : null);
    // labels for the bill
    const aB = eOut(seg(t, 0.5, 1.1));
    text('Loan costs', BX - 24, yBill + 26, { size: 18, color: C.dim, align: 'right', alpha: aB });
    text(CL('cost_median'), BX - 24, yBill + 58, { size: 32, weight: 700, align: 'right', alpha: aB });
    const TX = 704;
    // legend: one slice = one month of savings (fixed place, never collides)
    const aS = eOut(seg(t, 1.4, 2.0));
    rect(TX, 540, 30, 12, C.pos, aS); rect(TX, 552, 30, 2, C.bg, aS); rect(TX, 554, 30, 12, C.pos, aS);
    let w = text('+' + CL('sav_median') + ' saved', TX + 42, 556, { size: 22, weight: 700, color: C.pos, alpha: aS });
    badge(TX + 50 + w, 549, aS);
    text('each slice = one month', TX + 42, 580, { size: 16, color: C.dim, alpha: aS });

    // month 24: the simple division says "full"
    const a24 = eOut(seg(t, 5.2, 5.5));
    const eqY = 170;
    w = text(CL('cost_median') + ' ÷ ' + CL('sav_median') + ' = ' + CL('be_simple_median') + ' months', TX, eqY, { size: 24, weight: 600, alpha: a24 * (1 - 0.55 * reveal) });
    badge(TX + 8 + w, eqY - 8, a24 * (1 - 0.55 * reveal));
    if (reveal > 0) line([[TX - 4, eqY - 8], [TX - 4 + (w + 8) * reveal, eqY - 8]], C.warn, 3, { alpha: 0.9 });
    // revealed hidden part
    const aR = reveal;
    const gy = yBill - M.gap[24] * SC / 2;
    line([[BX + BW + 8, gy], [TX - 12, 243]], C.warn, 1.5, { alpha: aR });
    w = text('+ ' + CL('gap24') + ' still owed', TX, 250, { size: 24, weight: 700, color: C.warn, alpha: aR });
    badge(TX + 8 + w, 242, aR);
    text('at month ' + CL('be_simple_median') + ': the new loan pays down more slowly', TX, 274, { size: 16, color: C.dim, alpha: aR });

    // month 30: truly full
    const a30 = eOut(seg(t, 8.5, 8.9));
    if (a30 > 0) strokeRect(BX - 3, yTop - 3, BW + 6, YB - yTop + 3, C.pos, 3, a30);
    w = text('break-even: month ' + CL('be_bal_median'), TX, 350, { size: 32, weight: 700, color: C.pos, alpha: a30 });
    badge(TX + 8 + w, 340, a30);

    // month ruler: a tick lights per month; only claimed months are numbered
    const aRu = eOut(seg(t, 0.6, 1.2));
    line([[RX0, RY], [RX1, RY]], C.grid, 2, { alpha: aRu });
    for (let k = 1; k <= 36; k++) {
      const lit = k <= m + 1e-6;
      line([[rx(k), RY - (lit ? 12 : 6)], [rx(k), RY]], lit ? (k > 24 ? C.warn : C.pos) : C.grid, 2, { alpha: aRu });
    }
    text('months after refinancing', RX0, RY + 30, { size: 16, color: C.dim, alpha: aRu });
    text(CL('hold36'), rx(36), RY + 30, { size: 16, color: C.dim, align: 'center', alpha: aRu });
    text(CL('be_simple_median'), rx(24), RY + 30, { size: 18, weight: 700, align: 'center', color: reveal > 0.5 ? C.dim : C.ink, alpha: a24 });
    if (reveal > 0) line([[rx(24) - 14, RY + 24], [rx(24) - 14 + 28 * reveal, RY + 24]], C.warn, 2.5);
    text(CL('be_bal_median'), rx(30), RY + 30, { size: 18, weight: 700, align: 'center', color: C.pos, alpha: a30 });
    // month cursor
    if (t > 1.4) dot(rx(m), RY, 6, C.ink, 1);
  }

  // ============ F3 · Walt and Anjali ============
  function F3(t) {
    clear();
    const S = D.small, Lg = D.large;
    const YB = 540, SC = 0.026, BW = 150;
    const cols = [
      { d: S, cx: 350, name: 'Walt', color: C.warn, shape: tri, loan: 'loan_small', cost: 'cost_small', sav: 'sav_small', cut: 'cut36_small' },
      { d: Lg, cx: 930, name: 'Anjali', color: C.neg, shape: sq, loan: 'loan_large', cost: 'cost_large', sav: 'sav_large', cut: 'cut36_large_words' },
    ];
    // shared month clock
    let m;
    if (t < 2.6) m = 0; else m = 36 * ease(seg(t, 2.6, 6.2));
    const clockFade = 1 - eOut(seg(t, 6.4, 6.9));

    text('nominal $', 1184, 50, { size: 16, color: C.dim, align: 'right', alpha: eOut(seg(t, 0, 0.6)) });
    cols.forEach((c, j) => {
      const a0 = eOut(seg(t, 0 + j * 0.12, 0.6 + j * 0.12));
      const x0 = c.cx - 240;
      c.shape(x0 + 10, 62, 11, c.color, a0);
      const wn = text(c.name, x0 + 30, 72, { size: 28, weight: 700, alpha: a0 });
      badge(x0 + 42 + wn, 63, a0);
      // loan bar, to scale (655k -> 480 px)
      const aL = ease(seg(t, 0.4 + j * 0.1, 1.3 + j * 0.1));
      const len = (c.d.loan / 655000) * 480 * aL;
      rect(x0, 92, len, 16, C.dim, 0.85);
      text('loan ' + CL(c.loan), x0, 132, { size: 18, color: C.dim, alpha: eOut(seg(t, 1.0, 1.4)) });
      // fee block (outline) rises
      const bx = c.cx - BW / 2;
      const hB = c.d.cost * SC * ease(seg(t, 1.4 + j * 0.1, 2.2 + j * 0.1));
      const yBill = YB - hB;
      line([[bx - 30, YB], [bx + BW + 30, YB]], C.grid, 2, { alpha: a0 });
      rect(bx, yBill, BW, hB, C.surface, 1);
      // hidden extra balance (grey hatch, grows with months)
      const mm = Math.min(36, m), a = Math.floor(mm), b = Math.min(36, a + 1);
      const hGap = lerp(c.d.gap[a], c.d.gap[b], mm - a) * SC;
      if (m > 0) { hatch(bx, yBill - hGap, BW, hGap, C.dim, 0.7, 7); strokeRect(bx, yBill - hGap, BW, hGap, C.dim, 1.5, 0.7); }
      // savings slices
      const hS = c.d.sav * SC;
      slices(bx, YB, BW, m, hS, C.pos);
      strokeRect(bx, yBill, BW, hB, C.dim, 2, 1);
      const aC = eOut(seg(t, 1.8 + j * 0.1, 2.3 + j * 0.1));
      text('loan costs', bx - 16, yBill + 22, { size: 16, color: C.dim, align: 'right', alpha: aC });
      text(CL(c.cost), bx - 16, yBill + 50, { size: 28, weight: 700, align: 'right', alpha: aC });
      // saving speed label
      const aS = eOut(seg(t, 2.5, 3.0));
      const yF = Math.min(YB - 14, YB - m * hS + 8);
      const ws = text('+' + CL(c.sav) + '/mo', bx + BW + 16, Math.max(170, yF), { size: 22, weight: 700, color: C.pos, alpha: aS });
      badge(bx + BW + 24 + ws, Math.max(170, yF) - 8, aS);
      // full?
      if (c.d.be <= 36) {
        const tFull = 2.6 + 3.6 * invEase(c.d.be / 36);
        const aF = eOut(seg(t, tFull, tFull + 0.35));
        const yTopF = YB - (c.d.cost + c.d.gap[c.d.be]) * SC;
        if (aF > 0) strokeRect(bx - 3, yTopF - 3, BW + 6, YB - yTopF + 3, C.pos, 3, aF);
        const wf = text('paid back: month ' + CL('be_bal_large'), bx - 16, yTopF - 20, { size: 20, weight: 700, color: C.pos, align: 'right', alpha: aF });
        badge(bx - 16 - wf - 8 - tw('ILLUSTRATIVE', 11, 700) - 12, yTopF - 27, aF);
      } else {
        const aF = eOut(seg(t, 6.2, 6.6));
        const yTopF = YB - (c.d.cost + c.d.gap[36]) * SC;
        text('not paid back', bx - 16, yTopF - 34, { size: 20, weight: 700, color: C.ink, align: 'right', alpha: aF });
        text('after ' + CL('y3') + ' years', bx - 16, yTopF - 12, { size: 16, color: C.dim, align: 'right', alpha: aF });
      }
    });

    // month clock (shared)
    const RY = 590, RX0 = 170, RX1 = 1110;
    const aK = eOut(seg(t, 2.4, 2.8)) * clockFade;
    line([[RX0, RY], [RX1, RY]], C.grid, 2, { alpha: aK });
    for (let k = 1; k <= 36; k++) { const lit = k <= m + 1e-6; line([[RX0 + (k / 36) * (RX1 - RX0), RY - (lit ? 10 : 5)], [RX0 + (k / 36) * (RX1 - RX0), RY]], lit ? C.pos : C.grid, 2, { alpha: aK }); }
    text('same months for both', RX0, RY + 26, { size: 16, color: C.dim, alpha: aK });
    text(CL('y3') + ' years', RX1, RY + 26, { size: 16, color: C.dim, align: 'right', alpha: aK });
    if (m > 0) dot(RX0 + (m / 36) * (RX1 - RX0), RY, 6, C.ink, aK);

    // ruler: rate cut needed to break even within 3 years
    const aU = eOut(seg(t, 6.6, 7.1));
    const UX0 = 170, UX1 = 1110, UY = 650, maxCut = 1.25;
    const ux = (v) => UX0 + (v / maxCut) * (UX1 - UX0);
    text('Rate cut needed to break even within ' + CL('y3') + ' years', UX0, 606, { size: 20, weight: 600, alpha: aU });
    line([[UX0, UY], [UX0 + (UX1 - UX0) * aU, UY]], C.dim, 2);
    line([[ux(1), UY - 14], [ux(1), UY + 14]], C.ink, 2, { alpha: aU, dash: [4, 4] });
    text(CL('s10') + ' point', ux(1), UY + 34, { size: 16, color: C.dim, align: 'center', alpha: aU });
    line([[UX0, UY - 8], [UX0, UY + 8]], C.dim, 2, { alpha: aU });
    text('no cut', UX0, UY + 34, { size: 16, color: C.dim, align: 'center', alpha: aU });
    const vals = [1.1179, 0.3165];
    cols.forEach((c, j) => {
      const p = ease(seg(t, 7.1 + j * 0.25, 8.4 + j * 0.25));
      const x = ux(vals[j] * p);
      c.shape(x, UY - 20, 11, c.color, aU);
      const lab = j === 0 ? CL(c.cut) : CL(c.cut);
      const aT = eOut(seg(t, 8.4 + j * 0.25, 8.8 + j * 0.25));
      const wl = text(lab, x + (j === 0 ? 18 : 18), UY - 14, { size: j === 0 ? 24 : 20, weight: 700, color: C.ink, alpha: aT });
      badge(x + 26 + wl, UY - 22, aT);
    });
  }
  function invEase(y) { // inverse of ease() on [0,1] (bisection) — time at which the clock shows a given month
    let lo = 0, hi = 1;
    for (let k = 0; k < 40; k++) { const mid = (lo + hi) / 2; if (ease(mid) < y) lo = mid; else hi = mid; }
    return lo;
  }

  const SCENES = { F1: { f: F1, dur: 9.0 }, F2: { f: F2, dur: 10.0 }, F3: { f: F3, dur: 10.0 } };

  // ---------- render API for the driver ----------
  function frameB64(id, t) {
    SCENES[id].f(t);
    const px = g.getImageData(0, 0, W, H).data;
    let s = '';
    const CH = 0x8000;
    for (let i = 0; i < px.length; i += CH) s += String.fromCharCode.apply(null, px.subarray(i, i + CH));
    return btoa(s);
  }
  function png(id, t) { SCENES[id].f(t); return cv.toDataURL('image/png'); }
  function strip(id, times) { // 1920x220: six numbered frames in time order
    const sc = document.createElement('canvas'); sc.width = 1920; sc.height = 220;
    const s = sc.getContext('2d');
    s.fillStyle = C.bg; s.fillRect(0, 0, 1920, 220);
    times.forEach((tt, k) => {
      SCENES[id].f(tt);
      s.drawImage(cv, k * 320 + 2, 38, 316, 178);
      s.strokeStyle = C.grid; s.lineWidth = 2; s.strokeRect(k * 320 + 2, 38, 316, 178);
      s.fillStyle = C.ink; s.font = '700 22px Inter'; s.fillText(String(k + 1), k * 320 + 8, 28);
      s.fillStyle = C.dim; s.font = '400 16px Inter'; s.fillText(`t = ${tt.toFixed(1)} s`, k * 320 + 34, 27);
    });
    return sc.toDataURL('image/png');
  }
  window.H3 = { SCENES, frameB64, png, strip };
})();
