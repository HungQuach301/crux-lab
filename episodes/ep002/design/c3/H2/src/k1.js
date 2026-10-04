// KEY-1 (S01.2-S01.3): a level rail vs a bead that starts lower on a track whose future wavers.
import { C, W, H, DATA, CL, text, numWord, badge, line, poly, diamond, plane, pathPts, bandFill, ease, back, inout, clamp, mix, lin, FIXED } from './engine.js';
export const duration = 8.0;
export const stripTimes = [0.7, 1.7, 2.9, 4.3, 5.9, 7.7];
const P = plane(560, 1760, 230, 910, 4.8, 13.2, 36);
const GH = ['1962-03', '1958-06', '1985-02', '1968-09', '2004-06', '1954-01', '1988-07', '1999-05'].map((k) => DATA.detail[k].path.slice(0, 37));
export function draw(ctx, t) {
  const yR = P.Y(FIXED), bx = P.X(0), by = P.Y(7.5);
  // rail draws left -> right, then stays level
  const rx = mix(P.x0 - 200, P.x1, ease(t, 0.15, 1.3));
  line(ctx, [[P.x0 - 200, yR], [rx, yR]], C.ink, 12, { cap: 'butt' });
  // gap glow between bead and rail (it starts lower = cheaper now)
  const ga = ease(t, 1.6, 2.2) * (0.55 + 0.25 * Math.sin(t * 4.2));
  poly(ctx, [[bx - 44, yR + 5], [bx + 44, yR + 5], [bx + 44, by], [bx - 44, by]], C.positive, ga);
  // possible futures: thin tracks fan out ahead of the bead, each brightens then fades, replaced by the next
  ctx.save(); ctx.beginPath(); ctx.rect(P.x0, P.y0 - 20, P.x1 - P.x0 + 20, P.y1 - P.y0 + 40); ctx.clip();
  GH.forEach((p, i) => {
    const t0 = 2.0 + i * 0.6, a = inout(t, t0, t0 + 0.5, t0 + 1.5, t0 + 2.3);
    if (a <= 0) return;
    const n = 36 * ease(t, t0, t0 + 1.3);
    line(ctx, pathPts(P, p, n), C.accent, 7, { alpha: 0.9 * a });
  });
  // the committed short track under the bead (first months, known): solid
  ctx.restore();
  line(ctx, [[bx - 200, by], [bx, by]], C.accent, 8, { alpha: ease(t, 1.2, 1.7) });
  // bead (Leah) pops in, small idle bob along its start position
  const pop = back(t, 1.0, 1.6);
  if (t > 1.0) diamond(ctx, bx + 6 * Math.sin(t * 2.1) * ease(t, 2, 2.5), by, 38 * clamp(pop, 0, 1.4));
  // labels (number ink, word ink-muted)
  numWord(ctx, CL('fixed_rate'), 'fixed', P.x0 - 230, yR - 34, 'label', { alpha: ease(t, 1.0, 1.4) });
  numWord(ctx, CL('var_start'), 'variable', bx - 30, by + 110, 'label', { align: 'right', alpha: ease(t, 1.7, 2.1) });
  badge(ctx, ease(t, 1.0, 1.4));
}
