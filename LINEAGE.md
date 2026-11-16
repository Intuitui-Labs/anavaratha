# LINEAGE: where Anavaratha came from, and how it maps to the current work

Added 2026-11-16 (Asia/Colombo). This PR adds files only; no existing file is moved or modified. Legacy documents are verbatim copies under `docs/lineage/`. Each folder has a `STATUS.md` giving every file a status: current, superseded, killed or lineage-only. Raw originals, contacts and personal material live in a **private** archive, not here.

**Current locks (these win over any legacy text)**
- Frame C, syntropy-primary.
- Anavaratha and Peace Valley are separate peer tracks.
- Sensemaking stage: no intervention claims and no site selection.
- Name wording: Charter v0.1, "draws from Sinhala" (Naveen, 2026-11-16; see `docs/identity/NAME_NOTES.md`).

## Timeline (short)

| When (Asia/Colombo) | Layer | Folder |
|---|---|---|
| 2026-02-20 | Claude project "Anavaratha": **Concept Doc**. Entropy/negentropy/care; "reveals… does not prescribe solutions". | `docs/lineage/2026-02_concept/ANAVARATHA_CONCEPT_DOC_2026-02-20.md` |
| 2026-02-24 | Framework docs: exergy, nine ecologies, leverage points, **intervention typology** (superseded), data domain map v2 | `docs/lineage/2026-02_concept/` |
| ≤2026-08-22 → 25 | Manus waste layer: desk reviews, Demonstrator 01 (WP compost: 157 of 2,775 t/month), facility registers, GIS capacity package, Documentation Index | `docs/lineage/2026-08_waste-cycles/` |
| ≈2026-08-22 → 25 | **Institution and enforcement layer**: 11-actor responsibility map, 11-step compliance chain, Meethotamulla template, legal map, case register, NAPPWM register, **unsent** data-request drafts | `docs/lineage/2026-08_institution-enforcement/` |
| 2026-08-22 → 27 | Core Package: three-domain architecture, thermodynamics, Learning-Leverage-Action (§3C "translate between institutions") | `docs/lineage/2026-08_core-package/` |
| ≤2026-08-25 | Project Package: cultivation, Osu Uyana, cultivation atlas, circulation | `docs/lineage/2026-08_project-package/` |
| 2026-08-27 → 29 | **Charter v0.1** draft → final: Freedom from Waste · Material Afterlives · Ecological Flourishing | `docs/identity/charter/` |
| 2026-09-22 | Phase 1 Sensemaking pack (this repo) | `docs/phase1/` (unchanged) |
| 2026-10-04 | Name research; waste dataset / platform idea (killed) | `docs/lineage/2026-10_name-research/`, `docs/lineage/2026-10_waste-dataset/` |
| 2026-10-16 | intuitui-web initiative page | `docs/lineage/web/` |

## What the current Phase 1 work re-derived (read the lineage before redoing it)

1. Premise, glossary and boundaries → Charter v0.1 (§ shared grammar, boundary rules, "what it does not claim").
2. Institution/actor mapping → `2026-08_institution-enforcement/` + Core Package §3C.
3. Facility claims vs reality / no national evidence series → `2026-08_waste-cycles/` (IWMI, WMA, Manipura registers).
4. Desk-first method, evidence status, stage exit → the charter's maturity model and evidence-status vocabulary.
5. The name question → `docs/identity/NAME_NOTES.md` (decided).

## Hard rules for this lineage

- **The Data Request Pack letters are unsent drafts.** Never send them without Naveen's explicit decision.
- No contact data (phone numbers, emails, call sheets), no personal transcripts and no third-party PDFs in this public repo. The PR diff was scanned for phone numbers, emails, personal markers and third-party binaries before pushing.
- Superseded and killed files stay for lineage. Do not act on them.

**Proposed root `.gitignore` additions, for a reviewer to apply** (not applied here, because this PR modifies no existing file):

```
private/
archive/
CALL_SHEET_*
*_backup/
*contacts*
*.pdf
```
