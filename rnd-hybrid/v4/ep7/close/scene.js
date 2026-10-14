// R&D v4 · cảnh THẬT Tập 7 (đoạn a, t = 27 s: Tessa cận, tay chỉ tấm giấy vay) bọc lớp ánh sáng điện ảnh (opt-in). Cảnh gốc không sửa: import boot và bọc.
import { wrap } from '/rnd-hybrid/v4/light/cine.js';
import { boot as inner } from '/episodes/ep007/world/c4/a-s01-s03/scene.js';
export const boot = wrap(inner, { look: 'day', focus: 'char', aperture: 0.9, override: { keyAz: 160, keyEl: 30 } });
