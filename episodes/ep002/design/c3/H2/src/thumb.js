// Concept thumbnail (packaging.md §5): built from the H2 system. Hero = the rail, Leah's line climbing far above it
// (amber area) and the cushion tank sunk red. No result numbers; <= 4 words; ILLUSTRATIVE badge zone (32 px at 1280).
import { C, DATA, text, badge, line, rect, srect, negArea, plane, replay, FIXED } from './engine.js';
export const duration = 1 / 30;
export const stripTimes = [0, 0, 0, 0, 0, 0];
const d = DATA.detail['1977-04'];
const P = plane(110, 1480, 440, 1010, 3.2, 20.0, 120);
export function draw(ctx) {
  line(ctx, [[40, P.Y(FIXED)], [P.x0, P.Y(FIXED)]], C.ink, 18, { cap: 'butt' });
  replay(ctx, P, d.path, 119, { beadR: 40, lw: 10, railW: 18, aWarn: 0.85, aPos: 0.8 });
  const T = { x: 1600, w: 210, top: 300, yZero: 400, bottom: 1010, k: 560 / 11800 };
  srect(ctx, T.x, T.top, T.w, T.bottom - T.top, C.grid, 6);
  negArea(ctx, T.x + 3, T.yZero, T.w - 6, -d.cushion[119] * T.k, 1, 26);
  line(ctx, [[T.x - 20, T.yZero], [T.x + T.w + 20, T.yZero]], C.ink, 8, { cap: 'butt' });
  text(ctx, 'Fixed or', 96, 200, 'hero');
  text(ctx, 'variable?', 96, 352, 'hero');
  badge(ctx, 1);
}
