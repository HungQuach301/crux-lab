// Ep002 C6 thumbnails. Every picture is a still of a SIGNED C3 final scene (design/c3/final/src: k1.js, k2.js on the H2
// engine; h3/scenes.js K3, K6 on the H3 engine), drawn graphics-only with the engine's own NOTEXT flag, at an optional
// zoom/offset (composition = an option for the owner, not a new style). On top: flat Inter text in the signed tier `hero`
// (150 px @1080 = 100 px @1280x720), colours ink / ink-muted only (D5), and the engine's own ILLUSTRATIVE badge
// (type.badge 48 px @1080 = 32 px) on every thumbnail that shows Leah's loan. Numbers only via claim display (CL()).
const S = 2 / 3;
let E, TOK, C, CLD, scenes = {};
export async function boot(fam) {
  if (fam === 'h3') {
    E = await import('/src/h3/engine.js');
    const sc = await import('/src/h3/scenes.js');
    scenes = { K3: sc.K3, K6: sc.K6, K5: sc.K5 };
    CLD = (id) => E.CL(id);
  } else {
    E = await import('/src/engine.js');
    scenes = { K1: await import('/src/k1.js'), K2: await import('/src/k2.js'), K7: await import('/src/k7.js') };
    CLD = (id) => E.CL(id);
  }
  TOK = E.TOK; C = E.C;
  const cv = document.createElement('canvas'); cv.width = 1280; cv.height = 720; document.body.appendChild(cv);
  const ctx = cv.getContext('2d', { willReadFrequently: true });
  const HERO = TOK.type.tiers.hero, PX = HERO.px * S; // 100 px at 1280
  const boxes = [];
  function word(s, x, y, o = {}) { // flat text, 1280 space; returns ink box
    ctx.save(); ctx.font = `${o.weight || HERO.weight} ${PX}px Inter`; ctx.fontVariantNumeric = 'tabular-nums'; ctx.textBaseline = 'alphabetic';
    const m = ctx.measureText(s), w = m.width;
    const x0 = o.align === 'right' ? x - w : o.align === 'center' ? x - w / 2 : x;
    const box = [x0 - m.actualBoundingBoxLeft + (o.align ? 0 : 0), y - m.actualBoundingBoxAscent, m.actualBoundingBoxLeft + m.actualBoundingBoxRight, m.actualBoundingBoxAscent + m.actualBoundingBoxDescent];
    if (!o.measure) { ctx.fillStyle = o.color || C.ink; ctx.fillText(s, x0, y); boxes.push({ text: s, box: box.map((v) => +v.toFixed(1)), fontPx: +PX.toFixed(1), fontPx1080: HERO.px, claim: o.claim || null, color: o.color || C.ink }); }
    ctx.restore(); return { w, box };
  }
  function badge() { // the engine's own badge function, drawn at the film's transform
    ctx.setTransform(S, 0, 0, S, 0, 0);
    let pill;
    if (fam === 'h3') { const b = E.text ? null : null; E.badge(ctx, undefined, undefined, 1); const bx = E.BOXES[E.BOXES.length - 1]; pill = [bx.x0, bx.y0, bx.x1 - bx.x0, bx.y1 - bx.y0]; var glyph = [bx.gx0, bx.gy0, bx.gx1 - bx.gx0, bx.gy1 - bx.gy0]; }
    else { E.badge(ctx, 1); const f = E.FRAME_TEXTS[E.FRAME_TEXTS.length - 1]; pill = f.pill.map((v) => v / S); var glyph = f.box.map((v) => v / S); }
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    boxes.push({ text: 'ILLUSTRATIVE', box: glyph.map((v) => +(v * S).toFixed(1)), plateBox: pill.map((v) => +(v * S).toFixed(1)), fontPx: +(TOK.type.badge.px * S).toFixed(1), fontPx1080: TOK.type.badge.px, role: 'ILLUSTRATIVE badge (S08)' });
  }
  function still(k, t, z = 1, ox = 0, oy = 0) { // graphics only (engine NOTEXT flag), zoom z about the top-left, offset in 1280 px
    if (fam === 'h3') { E.FLAGS.NOTEXT = true; E.resetFrame(); } else { E.FLAGS.notext = true; }
    ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.fillStyle = C.bg; ctx.fillRect(0, 0, 1280, 720);
    ctx.setTransform(S * z, 0, 0, S * z, ox, oy);
    scenes[k].draw(ctx, t);
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    if (fam === 'h3') E.FLAGS.NOTEXT = false; else E.FLAGS.notext = false;
  }
  const COMPS = {
    // thumb-1 "Two offers": KEY-1 final frame (one person, two cards, the 9% line across both, Leah's replay on the right card)
    offers() {
      still('K1', 7.85, 1, 0, 14);
      word(CLD('fixed_rate'), 87 + 30, 127 + 14 + 30 + 73, { claim: 'fixed_rate' });
      word(CLD('var_start'), 740 + 30, 127 + 14 + 30 + 73, { claim: 'var_start' });
      badge();
    },
    // thumb-2 "Every stretch since 1954": KEY-3 state after every cell has turned (ridge = T-bill history, amber tally, red = cost more)
    history() {
      still('K3', 6.48, 1, 0, 90);
      const n = word(CLD('share_all'), 64, 160, { claim: 'share_all' });
      word('cost more', 64 + n.w + 28, 160, { color: C.muted });
      badge();
    },
    // thumb-3 "The worst stretch": KEY-6 final frame (zoom on April 1977, the fixed pile and the red extra block)
    worst() {
      still('K6', 9.6, 1, 0, 82);
      word(CLD('worst_start'), 64, 160, { claim: 'worst_start' });
      word(CLD('worst_share_of_fixed'), 1216, 204, { align: 'right', claim: 'worst_share_of_fixed' });
      word('more', 1216, 306, { color: C.muted, align: 'right' });
      badge();
    },
    // thumb-2b (claim-risk compliant): same KEY-3 picture, no share number; text names the two halves (period claims)
    history_b() {
      still('K3', 6.48, 1, 0, -50);   // text sits UNDER the grid: the early label under the left half, the late label under the right half
      const a = word(CLD('period_early_label'), 64, 640, { claim: 'period_early_label' });
      const v = word('vs', 64 + a.w + 32, 640, { color: C.muted });
      word(CLD('period_late'), 64 + a.w + 32 + v.w + 32, 640, { claim: 'period_late' });
      badge();
    },
    // thumb-3b: KEY-6 worst stretch framed explicitly as the worst case, no "43% more"
    worst_b() {
      still('K6', 9.6, 0.88, 90, 165);
      word('Worst case:', 64, 130, { color: C.muted });
      word(CLD('worst_start'), 64, 240, { claim: 'worst_start' });
      badge();
    },
    // thumb-3c (proposal): KEY-7 final frame (head start widest; before-1981 column still red, from-1981 column clean), a question, no number
    head_c() {
      still('K7', 9.8, 1, 110, 30);
      word('How much', 64, 160);
      word('lower?', 64, 270);
      badge();
    },
    // neutral (title round only): the KEY-3 picture, no words, badge only
    neutral() { still('K3', 6.48, 1, 0, 70); badge(); },
    // weak control (thumbnail round only): a plain film frame, KEY-2 at 2.9 s, with the film's own small labels
    control() {
      ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.fillStyle = C.bg; ctx.fillRect(0, 0, 1280, 720); ctx.setTransform(S, 0, 0, S, 0, 0);
      scenes.K2.draw(ctx, 2.9); ctx.setTransform(1, 0, 0, 1, 0, 0);
      for (const f of E.FRAME_TEXTS) boxes.push({ text: f.s, box: f.box.map((v) => +v.toFixed(1)), fontPx: +(f.px * S).toFixed(1), fontPx1080: f.px, role: 'film label' });
    },
  };
  return {
    render(name) { boxes.length = 0; if (E.FRAME_TEXTS) E.FRAME_TEXTS.length = 0; COMPS[name](); return { png: cv.toDataURL('image/png'), texts: JSON.parse(JSON.stringify(boxes)) }; },
  };
}
