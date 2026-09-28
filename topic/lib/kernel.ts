// The part of crux-studio's @crux/kernel that the topic assets use: the JSON-schema validator, stableHash and the
// model contract. Copied verbatim (validate.ts, hash.ts, contracts/model.schema.json) from crux-studio @ c7cadd7;
// the rest of the kernel (envelope, workshop runner, cassette, artifact store, packs, revenue, CLI) is factory
// infrastructure and is not brought over.
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import type { JsonSchema } from './validate.ts';

export * from './validate.ts';
export * from './hash.ts';

export const modelSchema: JsonSchema = JSON.parse(
  readFileSync(fileURLToPath(new URL('../contracts/model.schema.json', import.meta.url)), 'utf8'),
) as JsonSchema;
