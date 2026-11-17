> Public copy. Files under `draft/`, `_base/` and `_scripts/` named below are in the private archive. The public tables in this folder are the public-safe export described in README.md.

# MERGED_MODEL — canonical merged data model (DRAFT)

2026-11-16 (Asia/Colombo). Draft for Naveen / Anavaratha Lead review. Built by `_scripts/build_merge.py` (re-runnable; read-only on all sources). **The draft is PRIVATE (box only)**: it carries phone numbers, emails and personal names from the directory.

## 1. Design principles

1. **Keep every source value.** A merged row never overwrites a source value. Values live in a long table, one row per (source record, field), with the source file and its sha256.
2. **Dedupe only on confident matches.** Confident = same OSM id, or (operator-list tables only) token-set score ≥92 and core ratio ≥85 with no local-authority tier conflict (MC ≠ UC ≠ PS). Everything else stays a separate merged row and goes to `REVIEW_QUEUE.csv`.
3. **Provenance first.** sha256 comes from `anavaratha-legacy/MANIFEST.sha256` (or `derived/MANIFEST_derived.sha256`). Live phase1 files are byte-identical to the `current_snapshot_2026-11-16` copies in the MANIFEST, so they carry MANIFEST hashes too. The basis is stated per source in `draft/sources.csv`.
4. **Status, not deletion.** Legacy material that conflicts with a lock is kept and labelled. It is not dropped.

## 2. Files in `draft/`

| File | Grain | Key columns |
|---|---|---|
| `sources.csv` | one row per source file (68) | `source_id`, `path`, `layer` (C current · S site · WC Aug-25 waste-cycles · L1 Feb · L2 Aug · L3 Oct), `sha256`, `sha256_basis`, `rows` |
| `source_records.csv` | one row per source row (4,936) | `rec_id` = `source_id#row-key`, `entity_type`, `name`, `merged_id`, `mapping` (primary / same id / confident match … / attribute row of … / site node renders …) |
| `merged_entities.csv` / `.json` | one row per merged entity (3,091) | `merged_id`, `entity_type`, `canonical_name`, `status`, `primary_source_rec`, `members`, `conflict_notes`, `review_ids` |
| `values_long.csv` | one row per non-empty source cell (62,107) | `merged_id`, `rec_id`, `field`, `value` (verbatim), `source_file`, `source_sha256`, `privacy` |

## 3. Ids

`ANV-<TYPE>-<nnnn>`. Current rows are numbered first, in source order, so the crosswalk is stable on a re-run as long as sources don't change. Source ids are never replaced: `LK-WO-…`, `LK-DP-…`, `L01…L41`, legacy `WPF01`, `HD01`, `WPD01`, `SVC-/FAC-`, `S01…`, `WP01…`, case ids and OSM ids all stay in `rec_id`.

| Code | entity_type | Main sources |
|---|---|---|
| OP | operator | directory (456), L3 company list/profiles |
| FC | facility / facility_or_public_body / facility_or_project | directory councils & state sites (21), ledger facility rows (5), WC facility registers, IWMI, Manipura stations, OSM proximity, L3 dump sites |
| DP | drop_point | droppoints CSV (352) |
| PJ | project | ledger (29), L3 initiatives |
| LG | legal_item | ledger regulations/policy (6), WC enforcement cases (5), NAPPWM (20) |
| IN / IC | institution / institution_class | ledger L04 WMA; WC 11 actor classes; Core §3C actor list (9) |
| ID | institution_dataprovider | Feb xlsx sheet 07 (29) |
| SL | site_lead | WMA open-dump map leads (21) |
| PW | pathway | WC material pathway register (10) |
| PS / DR | process_step / data_request | WC compliance chain (11) / data request pack (6, **unsent**) |
| SR / CL / GE | source_doc / claim / geography | WC + Feb source catalogues, adversarial log, CPH2024 districts, OSM clusters |
| CO / QN / QK / EC / CT | concept / question / killed question / evidence class / call target | phase1 glossary, questions, evidence catalog, Colombo call sheet |
| SP | species_record | Project Package medicinal checklist (1,349; Domain III, see decision DN-07) |
| OB | observation | legacy table rows that are not entities (time series, summaries, xlsx design notes) |
| site_* | site-derived | site graph/timeline nodes with no separate source entity (136) |

## 4. Status vocabulary

| status | meaning |
|---|---|
| `current` | primary record is a current (Sep–Nov 2026) source row |
| `legacy-only` | no current counterpart found at any threshold |
| `legacy, near-match pending review` | candidate current entity exists; see `review_ids` |
| `site-derived (no separate source entity)` | exists only as a site visual node (lineage/graph/timeline) |

Proposed (not applied; needs DN-04): add an `evidence_status` per value using the charter vocabulary (observed · measured · estimated · reported · planned · historical · disputed · inaccessible · unknown). Map the current `verified_on_ground = not verified` → `reported`, and `not found` → `unknown` (never `absent`, per the WC rule).

Proposed lineage status per entity (as in `anavaratha-legacy` STATUS.md): `current` · `superseded` · `killed` · `lineage-only`. Pilot/candidate/site-selection rows (`pilot_scorecard`, Demo01 leverage matrix) = `lineage-only` pending DN-06.

## 5. Provenance per value

Every value carries `source_file` + `source_sha256`. Where two sources disagree on the same field of one entity, both rows stay in `values_long.csv`. The disagreement is recorded in `merged_entities.conflict_notes` and as a `REVIEW_QUEUE` row. No "winning" value is chosen in the draft.

## 6. Relationships (proposed, not yet populated)

| Relation | From → To | Basis available now |
|---|---|---|
| `member_of_class` | operator / facility / project → institution_class (IC01–IC11) | rule-based counts in GAP_AUDIT §1d; not yet written per row |
| `operates` | operator → drop_point | 267/352 drop points link by operator name to a directory row; 84 have operator "not found"; 1 unlinked ("Electricity Board Yard") |
| `same_site_as` | directory row ↔ ledger row | 21 candidate pairs (P1 for Meethotamulla, Kerawalapitiya, Aruwakkalu, Karadiyana) |
| `subject_of` | facility → legal_item | e.g. Meethotamulla ↔ SC/FR 311 & 318/2015 (MR-04) |
| `step_of` | evidence → compliance step | WC 11-step chain; nothing in current is coded to a step yet |
| `requested_via` | facility field → data_request | WC request pack (drafts only; never send without Naveen) |

## 7. Privacy and public fields

| Class | Fields | Count of values in draft | Public? |
|---|---|---|---|
| private | `contact_public` (directory), `Contact_Email`/`Contact_Phone` (L3) | 900 | **No.** Names of individuals + phone numbers |
| private (pattern) | any other field whose text contains a phone or email pattern | 130 | **No**, unless scrubbed (the site build already scrubs these) |
| restricted | `address`, `price` | 2,226 | Not now. The site drops them. Business addresses come from public CEA PDFs, but publishing them is DN-08 |
| public-ok | everything else (name, type, waste streams/types, district, coord_precision, CEA licence status, source URLs, evidence notes) | 58,851 | Yes. The same set the site already publishes |

Call sheets (phone numbers) and the data-request drafts stay private. The legacy `Claude` memory/conversation exports are not in this draft.

## 8. What a v1 would add (not done here)

- Write `member_of_class`, `same_site_as` and `subject_of` edges once P1 reviews are answered.
- Bring the 65 site-only atlas geocodes back into the directory as values tagged `geocoded_by_atlas` (GAP_AUDIT §2).
- Re-run `build_merge.py` after each weekly sweep, so the merge doesn't drift the way the site and directory headers did.

---

# v2 update (reconciled, 2026-11-17, Asia/Colombo). Where it differs from the sections above, v2 wins.

**Build.** `_scripts/build_merge.py` produces the v2 base in `_base/`. Ids are pinned to `_base/v1_frozen`, and the legal map is added as source A_WC_LEGALMAP. `_scripts/reconcile.py` (stdlib only) then applies Naveen's DN decisions and the agent's P1 decisions and writes `draft/`, `public/`, `REVIEW_QUEUE.csv`, `_scripts/stats_v2.json` and `_scripts/pins_v2.json`. `_scripts/lossless_check.py` writes `LOSSLESS_MERGE_CHECK.md`.

**Ids never renumber.**
- Base ids are pinned by `primary_source_rec`.
- New ids are pinned in `pins_v2.json`.
- Review ids are pinned by `stable_key` (sha1 of kind|rec|candidate|question), which is in `REVIEW_QUEUE.csv`.
- A merge does not delete anything. The retired id stays as a row with `alias_of` = the canonical id and `model_status` "retired → alias of X", and every member record and value is kept. Directory ids follow the same rule: retired `LK-WO-*` ids stay in the merged directory as `retired alias → <id>` rows, and `public/directory_id_aliases.csv` maps them.

**New entity types in v2:**
- `ANV-AC-*`: institution actors (DN-03), 73 live. That includes the existing WMA row `ANV-IN-0001`; the CEA L3 row is merged into `ANV-AC-0001`.
  - Columns: `institution_class` (one of the 11 classes; 4 actors left unclassified rather than guessed) and `la_tier` (MC/UC/PS), with the basis for each.
  - Local authorities by tier: 17 MC, 13 UC, 22 PS, 2 tier not stated.
- `ANV-ST-*`: site clusters for Karadiyana, Kerawalapitiya and Meethotamulla.
- `ANV-ES-0001`: CEA Pollution Source Inventory (evidence system, status `inaccessible`).
- `ANV-LG-0032…0040`: rows from the Legal and Enforcement Map. Provisions that belong to one instrument are merged into it as aliases: NEA = LM01+LM02; the 2026 Amendment Act = LM05+LM03+LM06+LM07; open burning LM04 → ANV-LG-0007.
- Proposed directory rows LK-WO-0492…0497: the 6 Oct-2026 L3 companies, all unverified, with scope flags on MAC Holdings and DAW.

**Relations** are in `draft/relations.csv` (1,162 rows). Columns: from, relation, to, confidence, basis, decision_ref, date. The main types are:

| Relation | Count |
|---|---|
| member_of_class | 525 |
| cea_registration_or_licence (→ CEA actor) | 396 |
| operated_by (→ local authority) | 50 |
| funder_or_implementer | 37 |
| role_in_chain_step (11-step chain) | 27 |
| service_context_of | 20 |

Legal links (amends, made_under, applied_in and others) and site links (located_at, same_facility, successor_site_of, probably_same_yard and others) make up the rest.

**Per-entity tags.**
- `evidence_status` uses the charter's 9-value vocabulary (DN-04). `n/a` means a non-empirical row such as a concept, source or class.
- `domain_primary`, `domain_secondary` and `domain_confidence` (confident / probable / uncertain) follow charter §5–6 (DN-05). Each tag carries a basis column.
- `district` and `district_basis` come from the primary source row or an address-evidence resolution.

**Derived values** are in `draft/values_derived.csv` (300 rows). This holds everything the reconciliation added: coordinate write-backs, rejected coordinates, district resolutions, LA tiers, chain stages, preferred and alternate values on conflicts, and gap-fills. Every row carries value_status, basis, source file, sha256 and decision ref. Base values in `values_long.csv` are byte-for-byte the same as in the base.

**Coordinates.**
- The 65 site-atlas geocodes are written back as `approximate (site atlas geocode; written back v2)`, with the source and sha recorded.
- LK-WO-0401 already had a CSV coordinate but was missing from the directory geojson; its feature is added.
- The 7 Oct L3 dump-site coordinates (68–93 km off) are stored only as `rejected — never import` and appear in no output.

**Privacy v2 (DN-08).**
- An `address` is public only for directory rows whose `dataset_origin` starts with `CEA_` (CEA-published business addresses).
- Other addresses and `price` are restricted.
- `contact_public`, Contact_Email and Contact_Phone are private.
- Any value that matches a phone or email pattern is private.
- `values_long.csv` keeps both `privacy` (v2) and `privacy_v1`.

**Merged directory.** `draft/DIRECTORY_WASTE_OPERATORS_LK.merged.csv` has 493 rows: all 487 source ids plus 6 proposed. Its extra columns are record_status, canonical_id, aliases, district_resolved and basis, coord_status and source, evidence and domain tags, actor_links, combined_cea_licences, combined_waste_types, premises and flags. The live phase1 files were not edited; this file and `draft/coordinate_writeback.csv` are the patch to apply once approved.

**Statuses added in v2:**
- `adopted actor (DN-03)`
- `adopted species record (DN-07)` (1,349 rows)
- `adopted legal item (legacy-sourced)`
- `adopted site cluster (v2)`
- `adopted evidence system (DN-03)`
- `adopted operator/facility/project (Oct L3; unverified)`
- `archived (DN-02, never send)`
- `history only (DN-06)`
- `retired → alias of X`
- suffix ` — near-match review open`

**Public export.** `public/` is described in its README. It is not published.
