# Hướng B — vật thể thật 3D (69.6 s prototype)

Files: `page.html` (importmap three + Inter), `b.js` (whole scene; `?house=code|cc`), `CREDITS.md`.
Render: `NODE_PATH=$(npm root -g) node moc-v/proto/render.js "moc-v/proto/B/page.html[?house=cc]" <out.mp4> --webgl --workers 4`.
Outputs: `moc-v/work/B-code.mp4`, `moc-v/work/B-cc.mp4`, stills in `moc-v/work/B-stills/`.

## World / encoding
- 1 world unit = $100,000. Cash bundles are $25,000 each (pitch 0.25), so the $500,000 beam = exactly 20 bundles and the $200,000 paid = exactly 8 bundles.
- x = time: X(q) = −7 + 14·q/105 (2000 Q1 … 2026 Q2). The house rides along x on its stack; a ribbon trail (z = −0.7, behind the stack) traces the stack top.
- Calendar page (3D, canvas texture) shows the year; flips when q crosses a year; final page "2026 Q2".
- All text is a 2D overlay (≥ 40 px), anchored to projected 3D points. Numbers printed: only claim displays ($500,000, $200,000, ≈ $558,100, ×3.8, Q2 2022, Q2 2023, 2000, 2026 Q2) and axis years 2000/2010/2020. No intermediate values.
- Chrome from `lib2d.chrome()` (illus always; hist from b1.t0; src from cue src; counterweight from b4.t0, swapped at b10.t1). A dark gradient scrim under the bottom footer row and above the source line keeps chrome legible when 3D objects pass behind it.

## Beats (cue → what happens)
- **b0** close shot: house on a $200,000-ish stack, Rosa & Frank (faceless capsules) + label. cap_hint 1.52: faint beam fades in above. q 3.18: warn "?" pops between roof and beam.
- **b1** blur 4.96: house + stack go translucent (ghost), figures and beam hint fade; camera dollies back to a district plate behind. "Phoenix area" at 8.98 (word "Phoenix"). src 11.21: source line. 14 small houses with SOLD sign-plates (plates are blank — no small text) pop exactly on the 14 `tick` events 11.93–13.49. many 13.53: "many sales". avg 14.453: houses shrink and converge into one accent orb ("Phoenix-area average"); orb flies into the stack top (14.95–15.6), house re-solidifies.
- **b2** camera widens; draw keyframes drive q 0→105 (15.846→21.206): stack = value[q], house moves along x, calendar flips 2000→2026, trail "home value" drawn behind.
- **b3** cap 23.36: beam falls from above, locks at y = $500,000 at 23.71 (= sound thud) with a small camera shake. lbl 25.368: "$500,000 cap". flat 27.176: accent pulse sweeps along the beam's 106 quarter segments + "same in every quarter".
- **b4** gain 30.0: counterweight footer. 33.94 ("two hundred thousand"): bottom 8 bundles tint accent + "$200,000". less 37.064: label → "$200,000 paid" and the slab starts sliding out sideways (ease-out, 0.7 s); the upper stack and the whole trail then fall exactly 2 units (finished at less+1.6). Label becomes "gain on paper". 39.3–40.5: house rewinds along the (now dim) gain line to 2000.
- **b5–b8** ride keyframes drive q. Lit part of the gain line = accent, part above the beam = warn, not-yet-ridden = dim. under 43.227: faint cushion panel under the beam + cushion bracket from stack top to beam. b6.q 45.446: thin warn marker at Q2 2022. cross 47.88: stack top touches the beam exactly at 47.88 (eased approach) then pushes through in 0.35 s; spark at the crossing, beam core turns warn near the house, bundles above the beam warn, "Over: Q2 2022". slip ≈ 49.34 (data crossing; cue 49.28): back under, label fades. b8 stack re-crosses ≈ 51.41, lbl 51.526: "Stayed over since Q2 2023"; warn top bundles to 2026.
- **b9** 55.2–59.4 push-in to the house top; 56.84 ("paper"): tag "≈ $558,100" next to the stack top. fly 59.752: tag starts flying immediately (ease-out), lands as the big number at land 60.73 with a warn underline tick. Older part of the gain line dims so it does not cut through the footer.
- **b10** 61.25–62.3 camera pushes in further; 61.958 impact shake + spark; past 62.008: warn bracket on the part above the beam + "past the cap". Footer swaps to "A measurement, not a tax bill or a next step" at b10.t1.
- **b11** 62.89: beam/trail/calendar fade, stack sinks into the floor, house lands; a 2000 twin pops at its left; labels "2000" / "2026 Q2". x 65.373: today's house grows in height to ×3.79 (ease-out, 2.2 s = `rise` event) with a height bracket + dashed reference line + "×3.8"; camera pulls back with it. lvl 67.693: caption "Phoenix-area prices since 2000". Final state held 67.6–69.6.

## Deviations / known limits
- b11: height ∝ index is done by stretching the house vertically only (width constant) so the visual ratio is height, not volume. Reads as a "tall house" (code) / "tower" (cc) rather than a bigger house.
- SOLD tags carry no lettering (any lettering would be < 40 px at that scale); "many sales" is the overlay label instead.
- The b6 crossing is time-shaped: the stack meets the beam exactly at cue cross, while the quarterly interpolation alone would cross ≈ 0.4 s earlier. The trail head follows the stack in that window.
- Counterweight footer: drawn through `chrome()` flags (`cw`, `cwA`); lib2d.js and spine.json untouched.
- CC model (obj_house1) is a flat-roofed voxel bungalow: reads as "a building" more than "a home" at small size; texture is a tiny palette PNG (nearest filtering). Collada Z-up warning is harmless.
- No randomness except a seeded LCG for neighbourhood layout; frame(t) is pure in t (camera, objects, labels).

## v2 (director pass `moc-v/eval/director-B.md`, code variant only; B-cc.mp4 stays v1)
- Year sweep follows new `draw` keys (2000 @ 17.70, 2026 @ 19.69); 12 SOLD houses pop exactly on the 12 `tick` events (8.98–13.23); ghost house re-solidifies only during the sweep (15.85 → 17.70).
- b1.rise 7.18: accent arrow grows up beside the ghost stack + "value rises with the index".
- Trail now runs along the stack's left edge (x − 0.68) so the index orb visibly becomes the line head.
- Value trail dimmed to ~25 % from beam lock (23.71) until b4.grow; at grow it re-brightens left→right ("$200,000, grown with the index" at the value top). b4.gain 30.0: "their gain on paper = ?". b4.two 33.94: bottom 8 bundles + "$200,000". less: slab slides out (ease-out from cue), stack + line fall exactly 2 units over 1.6 s; a 30 % ghost of the value line stays at the old height with a bracket showing the $200,000 gap. paid 39.58: "$200,000 paid". Calendar hidden 29.7–39.7 (it is static there).
- No rewind jump: house glides back along the full, bright gain line over [39.69, 40.59]; the not-yet-ridden part dims only after the ride starts.
- b5.under: thick cushion bracket + "well under". b6.cross: double warn ring burst + spark. "Over: Q2 2022" (dimmed slightly at slip) and "Stayed over since Q2 2023" both stay until b9.fly.
- b9: Rosa & Frank stand on the beam next to their stack from b9.t0; number appears only at fly (ease-out), lands with "gain on paper" above it. Calendar/axis fade at 55.0; "$500,000 cap" label re-anchors to the visible beam segment during the push-in.
- b10.past: stack bumps up through the beam (+0.28 u, 0.6 s) with spark + shake.
- b11: whole chart hidden by 63.29; title at 63.2; today's house grows 63.8 → cue x (ease-out); 2000 twin pops 63.75; labels from 64.2; Rosa & Frank beside today's house.

## Render times
(see `moc-v/work/B-code.mp4.render.json`, `moc-v/work/B-cc.mp4.render.json`)
