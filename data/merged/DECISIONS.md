# Anavaratha merge — decisions log

Public-safe copy of the merge decisions log (2026-11-17). Times are Asia/Colombo. The review queue, draft tables and per-value provenance it refers to are kept in the private archive, not in this repo.

## Project-lead decisions (Naveen, 2026-11-16) — final

| ID | Decision | How it is applied in the merge (v2) |
|---|---|---|
| DN-01 | Keep "draws from Sinhala" (already ruled). | Lock unchanged. The Aug-research claim that the name is a Sanskrit proper name (*anavarata*) is recorded as a **lineage note only**; nothing public changes. |
| DN-02 | Archive the 6 data-request letters; never send. | ANV-DR-0001…0006 → `model_status = archived / history only — never send (DN-02)`. They are not in the public export. |
| DN-03 | Adopt the 11 institution classes + 11-step compliance chain as the institution model; add institutions as actors and link rows to them. | Classes ANV-IC-0001…0011 and steps ANV-PS-* adopted. Actor entities added: national bodies, courts, police, administration, conservation agencies, and local authorities with tier. WMA reuses ledger L04's id. Links: directory CEA licence/registration → CEA; operators → class IC10; council rows → their LA; ledger rows → named actors; legal items → actors; Manipura/IWMI records → LAs. The class ↔ chain-step mapping is agent-derived from each class's role text and is marked `model (agent-derived)`. |
| DN-04 | Adopt the charter's 9-value evidence-status vocabulary. | Every non-retired entity gets `evidence_status` ∈ {observed, measured, estimated, reported, planned, historical, disputed, inaccessible, unknown}, plus `evidence_basis`. Non-empirical rows (concepts, model nodes, documents, archived drafts) get `n/a`. Rows no rule covers get `not assessed` (not guessed). |
| DN-05 | Tag rows by charter domain; mark uncertain tags. | `domain_primary`, `domain_secondary`, `domain_confidence` ∈ {confident, probable, uncertain}, and `domain_basis` citing charter §5/§6. Recyclable collectors and drop points are tagged Freedom from Waste (primary) / Material Afterlives (secondary) at **probable** confidence: the charter puts collection and treatment under Domain I and the afterlife under Domain II, so this is a judgement. |
| DN-06 | Pilot scorecard, candidate ranking, intervention typology and leverage scoring stay history only. | pilot_scorecard (3 rows) and the Demo01 bottleneck/leverage matrix (10 rows, incl. `possible_low_resource_intervention`) → `lineage-only (DN-06)`. Intervention typology and candidate ranking exist only as legacy md narrative, not rows; they are not carried into the model. |
| DN-07 | Include the 1,349-row medicinal checklist. | All 1,349 rows → `adopted species record (DN-07)`, domain Ecological Flourishing (confident), evidence `reported` (the source's own flag "machine_extracted_visual_validation_required" is kept). |
| DN-08 | CEA-published business addresses can be public; phones and emails stay private. | `address` is public only for directory rows whose `dataset_origin` starts with `CEA_` (380 rows). Other addresses stay restricted. `contact_public`, L3 email/phone and any phone/email pattern stay private. `price` stays restricted (not covered by DN-08). |

## Agent decisions (2026-11-16 / 17)

- All 59 P1 items, the 13 directory duplicate pairs (10 were P2), RV-0001/0002/0005 (P2) and RV-1001/1002 (new P3) are decided in `REVIEW_QUEUE.csv` (`decided_by=agent`), each with a rationale and evidence.
- Conflict rule: both values are always kept with provenance. One value is marked `preferred` only when the evidence is clearly stronger (for example IATI vs an uncited value). Otherwise the conflict is flagged.
- Duplicates: rows merge only on a shared address or a same-registered-company signal. Same-name rows at different addresses with different CEA registrations are kept separate; see GAP_AUDIT "Resolved" for why 5 of the 13 pairs were not merged.
- Coordinates in the Oct 2026 L3 dump-site table are rejected and never imported.
- Ids: `_scripts/build_merge.py` now writes `_base/` and pins merged ids and review ids to the frozen v1 build. New entities are pinned in `_scripts/pins_v2.json`, so re-runs do not renumber.

## Desk verification round — 2026-11-17 (approved by Naveen: "Yes, run the full desk verification round")

Desk only: public sources, no contact, nothing submitted. Full report: `VERIFICATION_2026-11-17.md`.

| Ref | Decision |
|---|---|
| RV-0169 | **Merge** LK-WO-0332 → LK-WO-0061 (Vass Enterprises): same contact person and shared phone in the public CEA lists; two premises kept. |
| RV-0166/0176/0171/0177 | Keep separate (desk-verified: different contact persons, no shared phone/email). |
| MR-02 | EUR 8,000,000 = EU financing-agreement amount (preferred); IATI/contract amounts kept as alternates. |
| MR-03 | L3 "2024" start refuted; Kattankudy UC MRF works began 23 Sep 2025. |
| RV-0015/0029 | Badulla MC compost plant ≠ Badulla PS compost yard (0425); ≈3.3 km apart. |
| RV-0031 | Batticaloa MC compost plant = LK-WO-0426 (same_facility). |
| RV-0127 | Kerawalapitiya yard period Apr 2017 – present; no conflict. |
| RV-0159/0126 | 0395 ↔ L22 same_facility (linked, not merged). |
| RV-0028 | Trincomalee UC disposes_at LK-WO-0427 (Kanniya/Kannaya dump). |
| RV-0071 | Hospital wastewater plant ≠ plastic drop bin (co-located). |
| 0492–0497 | Desk-checked: 0493/0494 out of operator scope, 0492 marginal; 0495 renamed Abans Environmental Services (medium); 0496/0497 in scope. |
| LK-WO-0498–0508 | 11 **unverified candidate** rows (Badulla MC plant + Nuwara Eliya, Kilinochchi, Mullaitivu, Mannar, Vavuniya). |
| Coordinates | 65 write-backs checked (48 independent: median 1.16 km, p90 2.82 km, max 5.05 km); 9 corrections proposed, **not applied**; see `coord_check` column. |
