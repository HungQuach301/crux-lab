# Credits — Hướng B

- **House model (variant `?house=cc`)**: `obj_house1.dae` (+ `obj_house1_texture0.png`) from **"Mini Mike's Metro Minis"** by **Mike Judge** (@mikelovesrobots), https://github.com/mikelovesrobots/mmmm — licensed **CC BY 4.0** (https://creativecommons.org/licenses/by/4.0/). Used via `moc-v/proto/vendor/node_modules/mmmm-models/collada/`. Changes: re-materialed as MeshStandardMaterial with nearest-neighbour texture filtering, uniformly scaled to 1.6 world units wide; in the last beat (b11) scaled vertically ×3.79 to encode the price-index ratio. Also cloned as the 14 small "SOLD" houses in b1.
- **three.js** 0.186.1 (MIT) incl. `ColladaLoader` from three/examples/jsm.
- **Inter** font (SIL OFL 1.1), from `toolkit/render/fonts`.
- Everything else (code-built house, cash bundles, cap beam, calendar, figures) is original geometry in `b.js`.
- Data: FHFA all-transactions HPI, Phoenix-Mesa-Chandler (ATNHPIUS38060Q) via FRED (see `moc-v/proto/data.json`).
