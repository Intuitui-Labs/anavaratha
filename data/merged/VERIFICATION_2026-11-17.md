# Anavaratha — desk verification round, 2026-11-17

**Scope:** desk only. Public web sources (CEA lists, council and provincial pages, Auditor-General reports, company sites and registries, EU/IATI documents, news, OSM and Nominatim). Nobody was called, emailed or messaged, no forms were submitted, and the data-request letters were not sent.
**Approved by:** Naveen (chat widget answer: "Yes, run the full desk verification round").
**Date:** sources accessed 2026-11-17 (Asia/Colombo).
**Machine-readable files:**
- `verification.csv`: 95 items, one row each, with columns vid, verdict_class, verdict, evidence, evidence_urls, accessed, confidence and evidence_status (the charter label).
- `candidates.csv`: 11 candidate rows.
- `coord_spotcheck.csv`: all 65 coordinate write-backs.
- `progress.json`: the raw item log.

**Verdict classes:** confirmed, refuted, or still unresolved.
**Evidence-status labels:** charter DN-04 vocabulary. Personal names, phones and emails are left out of this file. Contact-level comparisons were done locally against the private draft.

## 1. Headline verdicts

| Item | Verdict | Confidence | Evidence status | Applied to draft |
|---|---|---|---|---|
| MR-02 EU grant amount | **confirmed**: same programme. EUR 8,000,000 is the EU financing-agreement amount (signed 23 Sep 2025, AAP 2024 Action 1, implemented by UNOPS with GIZ support). | high (amount); medium (why IATI 8,722,456 and the contract 9,400,639 differ) | reported | EUR 8M preferred. IATI and contract figures kept as alternates. L3 period 2025–27 marked unconfirmed. Flag resolved. |
| MR-03 Kattankudy recycling centre | **refuted**: the legacy 2024 start is wrong. Works on the Kattankudy UC MRF (LKR 50.8M) began 23 Sep 2025. | high (year); medium (status) | reported | start_date 2025-09-23 preferred. 2024 rejected and kept as an alternate. Operational status unknown. |
| RV-0015/0029 Badulla | **confirmed**: two different facilities, so no tier conflict. The MC compost plant is at Riverside/Badulupitiya Rd (≈6.990, 81.064). The PS compost yard, LK-WO-0425 (OSM way 1110168300, Udawela/Viyadiguna), is ≈3.3 km away. | medium-high | reported | possibly_same link replaced by distinct_facility_same_town. Badulla MC plant added as candidate LK-WO-0498. |
| RV-0031 Batticaloa | **confirmed**: the BMC compost plant is at the Thirupperunthurai SWM centre = LK-WO-0426. | medium-high | reported | Link upgraded to same_facility. |
| RV-0127 Kerawalapitiya period | **confirmed, no conflict**: HD03's "2017–18" is its source window. The yard has been in use from Apr 2017 to the present (Jul 2026). | high | reported | Period Apr 2017 – present preferred. Flag resolved. |
| 0395 ↔ L22 (RV-0159, RV-0126) | **confirmed**: same SLLRDC-owned Kerawalapitiya yard. | medium | reported | Link upgraded to same_facility. Not merged, because the operators are named differently. |
| RV-0028 Trincomalee | **confirmed**: Trincomalee UC disposes at the Kanniya/Kannaya open dump (LK-WO-0427). IWMI's "Kinniya" is probably a misspelling. | medium-high | reported | disposes_at link added. |
| RV-0071 Apeksha Hospital | **refuted**: OSM way 577617941 is the hospital's wastewater plant; LK-DP-0099 is a plastic drop bin. They are co-located but different things. | high | observed (OSM tags) / reported | Kept separate; co_located_distinct link added. |
| Vass (RV-0169) 0061/0332 | **confirmed: same business**. Same contact person and a shared phone across the two CEA-list rows; two premises. | high | reported | **Merged**: 0332 is now a retired alias of 0061, with both premises kept. |
| Green Lanka (RV-0166) 0002/0107 | **confirmed: different businesses** | high | reported | Kept separate (desk-verified). |
| C.K. Enterprises (RV-0176) 0174/0242 | **confirmed: different businesses** | high | reported | Kept separate. |
| Ruwan Enterprises (RV-0171) 0103/0141 | **confirmed: different businesses** | high | reported | Kept separate. |
| Wasana Enterprises (RV-0177) 0212/0360 | **confirmed: different businesses** | medium | reported | Kept separate. |

For the four "different" pairs: they have different contact persons, no shared phone or email, and different addresses and registrations.

### Proposed rows LK-WO-0492–0497

| id | Exists | Active | In scope | Verdict |
|---|---|---|---|---|
| 0492 MAC Holdings | yes | yes (current corporate site) | **marginal**: ship-generated waste only, through its port-agency arm. District Colombo. | confirmed |
| 0493 Success Environmental Engineering Solutions | yes (sees.lk; CEA consultants list) | **unresolved** (site footer © 2017) | **no**: engineering contractor. District Matara. | still unresolved |
| 0494 DAW Corporation | yes | yes | **no**: engineering supplier. District Colombo. | confirmed |
| 0495 "Antes Environmental Services" | **not as named** | n/a | n/a | **refuted** as named. Most likely Abans Environmental Services (Pvt) Ltd, which is real, active and the CMC District 4 solid-waste contractor. Renamed with medium confidence; the L3 name is kept as an alternate. |
| 0496 Sewn Export | yes | yes (EDB exporter profile; own site) | yes: paper-waste collector and exporter. Colombo. Address stays private (EDB-published, not CEA). | confirmed |
| 0497 Eko Plasco | yes | probable (counter dated 2022; started May 2021) | yes: plastic. Kalutara. | confirmed (exists) |

Recommendation for Naveen: 0493 and 0494 are out of operator scope. 0492 is marginal. All three are kept as *proposed* rows with flags; none was deleted.

## 2. New candidate rows (all UNVERIFIED, desk sources only)

| Proposed id | Name | District | Evidence status | Coordinates | Key source |
|---|---|---|---|---|---|
| LK-WO-0498 | Badulla MC compost plant (Badulupitiya) | Badulla | reported | ≈6.9897, 81.0636 | IWMI 2020; Badulla MC SDG plan |
| LK-WO-0499 | Nuwara Eliya MC: Moon Plains (Sandathenna) landfill and plastic/polythene recycling centre | Nuwara Eliya | reported | ≈6.9505, 80.8068 (area) | Sunday Times 6 Aug 2017; PADEM baseline Jan 2025 |
| LK-WO-0500 | BLUECAP MRF Kilinochchi (woman-owned) | Kilinochchi | reported | none | PLEASE Project (opened 20 Aug 2025) |
| LK-WO-0501 | BLUECAP MRF Mullaitivu (youth-owned) | Mullaitivu | reported | none | PLEASE Project (opened 21 Aug 2025) |
| LK-WO-0502 | Karachchi PS compost plant, Umayalpuram (built 2017, idle) | Kilinochchi | reported | ≈9.4654, 80.3971 (village) | Auditor-General 2024 |
| LK-WO-0503 | Maritimepattu PS compost and recycling centre, Mullivaikkal | Mullaitivu | historical | ≈9.3069, 80.7840 (locality) | Auditor-General 2018 |
| LK-WO-0504 | Mannar UC solid-waste facility, Kurusunagar–Chinnakkadai | Mannar | reported | none | NPC Governor visit, 25 Sep 2026 |
| LK-WO-0505 | Vavuniya: Pampaimadu disposal site / KOICA-UNOPS ISWM site | Vavuniya | planned | ≈8.7889, 80.4214 (village) | NPC 2026; Univ. Vavuniya; UNOPS vacancy |
| LK-WO-0506 | Vavuniya UC compost plant, Veppankulam (abandoned) | Vavuniya | historical | ≈8.7608, 80.4719 (OSM road) | ADB IEE 2012; Springer 2013 |
| LK-WO-0507 | Eco Spindles material recovery centre, SFHQ-Vanni | Vavuniya | historical | none (military site, not geocoded) | Eco Spindles posts, 2019 |
| LK-WO-0508 | Give Back Life PET collection centre (Vavuniya MC) | Vavuniya | historical | none | Sunday Times 26 Jan 2020; Asia Foundation 2020 |

Notes on what was not added:
- Not added as rows: the PADEM/PALM Nuwara Eliya biowaste project (2026–31), which is a project, not an operator; and the Mannar PS compost machines (equipment bought in 2023 and unused, per AG 2024).
- Before this round, the directory had **no** canonical operator rows in these five districts. The only nearby entry was drop point LK-DP-0319 (eKunu, Vavuniya). The rows above are council and project facilities found in public sources.
- The full URL list is in `candidates.csv`.

## 3. Coordinate spot-check (all 65 approximate write-backs)

**Checks run:**
- 48 independent checks: 27 entities and 21 drop points. Each compares the written point with a Nominatim/OSM reference for the street, landmark or locality in the row's address.
- 14 consistency-only checks: the reference is the same locality name the geocoder used, so they are not an independent test.
- 3 unscored:
  - 0032: street not found.
  - 0288: ambiguous Maragahawewa.
  - DP-0314: the reference hit the wrong place.

**Error statistics (independent checks, n = 48):**

| | km |
|---|---|
| Median | 1.16 |
| Mean | 1.42 |
| p90 | 2.82 |
| Max | 5.05 |
| Entity median | 1.37 |
| Drop-point median | 0.77 |

**Distribution:**

| Error | Rows |
|---|---|
| ≤ 0.5 km | 10 |
| 0.5–1 km | 11 |
| 1–2 km | 12 |
| 2–5 km | 14 |
| > 5 km | 1 |

**Corrections proposed (not applied).** In these rows the reference point is a locality or landmark, so it is a better guess, though still approximate:
- 0164 Kalagedihena: 5.05 km
- DP-0345 Bambalapitiya: 4.07 km
- 0472 and DP-0332 (Kollupitiya): 2.85 km each
- 0456: 2.82 km
- 0027 Puwakpitiya: 2.42 km
- DP-0329: 2.31 km
- 0448 Ulahitiwala: 2.28 km
- 0473 Dangedara: 2.02 km

**Pattern:** most large errors are Colombo postal-zone rows (Colombo 03/04/02). The geocoder put them on the generic Colombo centroid at 6.9389, 79.8542.

**Flag only.** Here the reference is a single point on a long road, so no better point exists: 0018 and 0023 (2.46 km), 0061 (3.98 km), 0442 (2.30 km), 0444 (2.11 km) and DP-0346 (2.07 km).

**Where the results are recorded:**
- The private draft holds each check as a `coord_check (desk)` derived value, and each proposed fix as a `lat/lon (proposed correction, not applied)` derived value.
- The public directory and drop-point exports have a new `coord_check` column.

## 4. Still unresolved, and why

- **0493 SEES:** it is unclear whether the firm is still active. The only date on its site is a © 2017 footer, and no recent public record was found. Settling it needs a registry extract or direct contact, which is out of scope.
- **0495 identity:** "Antes" → Abans Environmental Services is an inference (one-letter OCR/typing error plus the same trade). It has medium confidence; no source spells "Antes".
- **0497 Eko Plasco:** recent activity is not dated after 2022.
- **MR-02:** why the IATI (8,722,456) and contract (9,400,639) figures differ from EUR 8M. It is likely contract-level versus agreement-level, but not documented. The L3 2025–27 period is unconfirmed.
- **MR-03:** whether the Kattankudy MRF is operating now. Only the construction start is documented.
- **Coordinates:**
  - 0032, 0288 and DP-0314 could not be scored.
  - The 14 consistency-only rows have no independent reference.
  - Proposed fixes are themselves approximate, so ground or official addresses are needed.
- **Northern candidates:** current operation is unknown for 0503, 0507 and 0508, which only have 2018–2020 evidence. 0502 is idle per AG 2024. No candidate has been verified on the ground.
- **Overpass** (OSM area queries) timed out on three endpoints, so the Northern OSM sweep used Nominatim instead. Its only hit was the Vepankulam compost road.

## 5. What changed in the data

**Private draft:**
- 15 review items moved to `decided — desk-verified`, each with a verification_id, class, confidence, evidence label and date.
- 1 new merge (0332 → 0061).
- Relations updated:
  - 3 unresolved links replaced: Badulla and Batticaloa possibly_same_facility, and Vass possibly_same_business, which became the merge.
  - same_facility ×3: 0395↔L22 (upgraded from probable), FAC-03↔0426, and candidate 0498↔FAC-02.
  - Added: disposes_at (SVC-19→0427), distinct_facility_same_town (FAC-02 vs 0425) and co_located_distinct (RV-0071).
  - The 4 name-collision links were re-labelled desk-verified.
  - RV-0126 is covered by the RV-0159 link, because HD03 is merged into L22.
- 11 candidate entities and directory rows (LK-WO-0498–0508, pinned in `pins_v2.json`).
- Resolved flags on 4 entities.
- 185 new derived values, each citing a VF id and `verification/verification.csv` (or `candidates.csv`) with its sha256.

**Lossless checks:** `lossless_check.py` and `lossless_applied.py` both PASS.

**Not changed:** the applied phase1 research directory. Phase1 still has 0332 as a canonical row and no candidates. Applying this round there needs a separate OK.
