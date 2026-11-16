# Anavaratha Nationwide Facility-Capacity Reality Research Protocol v0.1

**Scope:** Sri Lanka, all provinces and districts, all relevant material-management facility types. **Cut-off:** 22 August 2026. **Default author:** Manus AI.

## Research question

What facility and service capacity has existed, been planned, been commissioned, operated, failed, been suspended, closed, abandoned, rehabilitated, or remained unknown in Sri Lanka, and what evidence distinguishes nominal capacity from usable and environmentally safe capacity?

## Facility domains

The review will cover municipal solid-waste collection and transfer, composting, material recovery and recycling, sanitary landfills, controlled or engineered disposal sites, open dumps where source-verifiable, waste-to-energy and incineration, clinical and healthcare waste, hazardous and scheduled waste, e-waste, plastics, wastewater and sludge where relevant to waste pathways, and residual/ash management.

## Status taxonomy

| Status label | Meaning | Minimum evidence |
|---|---|---|
| `operating_current` | Evidence indicates operation during the latest verified period | Dated log, inspection, operator record, or recent independent observation |
| `operating_historical` | Operation is verified for a past period, but current status is unknown | Dated primary or strong secondary source |
| `planned` | Proposed, budgeted, approved, or announced but delivery is not verified | Plan, budget, announcement, or approval document |
| `under_construction` | Construction is explicitly documented but commissioning is not verified | Project/procurement/construction record |
| `commissioned_status_unknown` | Built or commissioned is documented, but current operation is unknown | Completion/commissioning record |
| `idle_or_suspended` | Explicitly reported idle, suspended, or not in use at a defined date | Audit, inspection, operator, or independent report |
| `closed` | Explicitly reported closed at a defined date | Closure notice, official record, or dated independent source |
| `abandoned_or_failed` | Explicitly reported abandoned or failed as a project/facility | Audit or strong source using that finding |
| `rehabilitation_or_upgrade` | Repair, expansion, or rehabilitation is documented | Project/contract/inspection record |
| `status_conflicted` | Credible sources disagree | At least two contradictory dated sources |
| `status_unknown` | Facility or site is identified but no reliable status evidence is available | Traceable site lead only |
| `unverified_lead` | Anecdote, map tag, or weak report requiring verification | Lead retained without factual claim |

A status is always paired with `status_as_of_date`, `status_source`, and `status_confidence`. “Closed” must never be inferred merely because a facility is old or absent from a newer list; “operating” must never be inferred merely because a facility was once commissioned.

## Capacity dimensions

Every capacity value must preserve the exact boundary, unit, period, and measurement basis. The register will distinguish:

1. **Design capacity:** intended engineering capacity.
2. **Installed capacity:** equipment or physical infrastructure installed.
3. **Permitted capacity:** capacity allowed under a licence or approval.
4. **Running capacity:** operator-reported or survey-defined capacity while the facility is functioning.
5. **Actual intake:** measured or reported material received.
6. **Accepted intake:** material accepted into the process after rejection/sorting.
7. **Actual throughput:** material processed per defined period.
8. **Product output:** compost, recovered materials, treated material, electricity, or other output.
9. **Residual output:** rejects, ash, sludge, leachate, or other residuals.
10. **Usable capacity:** a derived analytical concept calculated only when input, output, quality, operating time, and boundary definitions are compatible.
11. **Ecologically safe capacity:** not calculated until containment, monitoring, receiving environment, and residual pathway evidence exists.

No national total will be formed by adding incompatible streams or years. A design figure will never be presented as a measured outcome.

## Evidence grades

| Grade | Evidence basis |
|---|---|
| A | Primary government record, audit, licence, inspection, weighbridge/operating log, or court record with clear date and location |
| B | Independent peer-reviewed field study or institutional technical study with methods and defined period |
| C | Official plan, project document, budget, or programme announcement showing intention/design |
| D | Reputable media, NGO, or research report that identifies a source-verifiable claim or lead |
| E | OSM/map entry, anecdote, unsourced claim, or ambiguous secondary reference |

The grade measures evidentiary strength for the specific claim, not the quality of the institution or source generally. A Grade A licence may establish formal authorization but not actual operation; a Grade A audit may establish an observed failure but not national prevalence.

## Citation protocol

Every substantive claim will include an inline numeric citation linked to a References entry. Each register row will store: `source_id`, full title, issuing body/author, publication date, URL or local source file, page/table/section, access date, data period, geography, exact quoted or transcribed statement, evidence grade, status label, and interpretation caution.

Official PDFs will be archived locally where legally and technically available. Web pages will be stored with URL and access date. Sources that cannot be retrieved will be listed as access failures rather than treated as nonexistent. Closed, failed, idle, and abandoned records will remain in the register with explicit dates and evidence, not be deleted from the current-facility view.

## Analytical separation rules

Current, historical, planned, and closed evidence will be analysed in separate views. Facility names and aliases will be normalized without erasing original names. Where a facility changes operator, technology, site boundary, or function, status events will be recorded rather than overwriting the history. All contradictions will be preserved. No composite capacity score will be created until compatible variables and missingness thresholds are justified.

## National output set

The final package will contain: a source catalogue; a source-traceable facility register; a status-event register; a capacity-measurement table; service and catchment data; failure/persistence records; currentness and missingness audits; province/district coverage tables; facility-domain summaries; a list of closed/idle/abandoned sources; a current-data gap report; and a formal data-request template for agencies and local authorities.
