import { cpSync, mkdirSync } from 'node:fs';
mkdirSync('src/data', { recursive: true }); mkdirSync('public/data', { recursive: true }); mkdirSync('public/diagrams', { recursive: true });
for (const f of ['graph.json', 'timeline.json', 'flows.json', 'matrix.json']) { cpSync(`../data/${f}`, `src/data/${f}`); cpSync(`../data/${f}`, `public/data/${f}`); }
for (const f of ['operators_public.geojson', 'operators_unmapped.json']) cpSync(`../data/${f}`, `public/data/${f}`);
for (const f of ['a_concept_mindmap','b_chronology_timeline','c_lineage_graph','d_responsibility_chain','e_household_route','f_ledger_timeline','g_route_sankey']) cpSync(`../mermaid/${f}.png`, `public/diagrams/${f}.png`);
console.log('data copied');
import { readFileSync, writeFileSync } from 'node:fs';
const gm = JSON.parse(readFileSync('../data/operators_public.geojson', 'utf8')).meta;
writeFileSync('src/data/geo_meta.json', JSON.stringify({ ...gm.counts, features: gm.counts.entities_mapped + gm.counts.drop_points_mapped }, null, 1));
