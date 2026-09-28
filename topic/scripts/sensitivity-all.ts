// Inventory measurement for gate input 3 (crux-lab, Phiên D1, 2026-09-28): run the Sensitivity Pass on every model
// of the library, every parameter over its validRange (1,000 grid steps), with a conclusion output per model, and
// report which models show a flip point. Written for the inventory; no output here was hand-edited.
//   node topic/scripts/sensitivity-all.ts [--write]
import { writeFileSync, mkdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { MODEL_IDS, loadModel, TOPIC_FORMULAS } from '../src/models.ts';
import { runSensitivityPass, sensitivityProblems } from '../src/sensitivity.ts';

// the output whose sign is the model's "conclusion"; the only output that can change sign where one exists
const CONCLUSION: Record<string, string> = {
  'M-001': 'totalFeeDragUsd', 'M-002': 'monthlySavingsUsd', 'M-003': 'apyPct', 'M-004': 'reductionUsd',
  'M-005': 'rmdUsd', 'M-006': 'compositeRatePct', 'M-007': 'taxableBenefitsUsd', 'M-008': 'iraDeductionUsd',
};
const RUN_AT = '2026-09-28T00:00:00Z';
const rows = [];
for (const id of MODEL_IDS) {
  const model = loadModel(id);
  const parameters = model.parameters.map((p) => ({ name: p.name, step: (p.validRange[1] - p.validRange[0]) / 1000 }));
  let result, error = null;
  try { result = runSensitivityPass(model, TOPIC_FORMULAS, { conclusionOutput: CONCLUSION[id]!, runAt: RUN_AT, parameters }); }
  catch (e) { error = String((e as Error).message ?? e); }
  const problems = result ? sensitivityProblems(result) : [];
  rows.push({ model: id, title: model.title, conclusionOutput: CONCLUSION[id], error, problems,
    flips: result ? result.flipPoints.map((f) => ({ parameter: f.parameter, value: +f.value.toFixed(6), before: f.conclusionBefore, after: f.conclusionAfter })) : [],
    stableConclusion: result?.stableConclusion ?? null, result });
}
for (const r of rows) console.log(`${r.model} ${r.conclusionOutput}: ${r.error ? 'ERROR ' + r.error : r.flips.length + ' flip(s)'} ${r.flips.map((f) => `${f.parameter}=${f.value}`).join(', ')}`);
if (process.argv.includes('--write')) {
  const dir = fileURLToPath(new URL('../data/sensitivity/', import.meta.url));
  mkdirSync(dir, { recursive: true });
  writeFileSync(dir + 'sensitivity-all-2026-09-28.json', JSON.stringify(rows, null, 1) + '\n');
}
