# Anavaratha Current Facility and Hidden-Disposal Verification Schema

**Purpose:** Provide a desk-first structure for verifying facility-capacity reality and hidden disposal in Sri Lanka, beginning with Western Province and later expanding nationally.

## Evidence hierarchy

| Grade | Evidence type | Permitted use |
|---|---|---|
| A | Primary official record, court finding, audit finding, signed inspection, raw weighbridge or monitoring record | Direct factual claim with source date and page/table |
| B | Peer-reviewed study, donor technical report, structured survey, named facility dataset | Detailed analytical claim with period and boundary caveat |
| C | Official project announcement, plan, public programme page, agency statement | Existence, intention, handover, target, or institutional claim; not outcome proof |
| D | Reputable journalism, technical proposal, NGO or practitioner report | Verification lead or conflicting account; never sole proof of illegality |
| E | Anecdote, unverified social media, uncited claim | Lead only; do not geocode or state as fact |

## Required status taxonomy

`current_operating_verified`, `current_operating_reported`, `current_status_unknown`, `planned`, `under_construction`, `commissioned_status_unknown`, `idle_or_suspended`, `temporarily_diverting_or_receiving`, `rehabilitation_or_upgrade`, `closed_verified`, `ceased_after_incident`, `abandoned_or_failed`, `conflicted_status`, and `historical_only`.

A site may have more than one status event across time. “Closed” requires explicit closure evidence. “Current operating” requires a recent dated observation or operational record. A project announcement, licence, equipment handover, or name on a plan cannot alone establish current operation.

## Facility record fields

| Field family | Required fields |
|---|---|
| Identity | record_id, official_name, alternate_names, facility_type, waste_stream, owner, operator, local_authority, province, district, GN/ward |
| Geometry | latitude, longitude, polygon_source, coordinate_precision, geocoding_method, geometry_confidence |
| Time | source_date, observation_period, last_verified_date, status_start, status_end, status_event |
| Capacity | design_capacity, installed_capacity, permitted_capacity, running_capacity, accepted_intake, actual_intake, throughput, product_output, reject_output, residual_output, units, measurement_method |
| Operation | operating_days, uptime, downtime, maintenance, breakdowns, staffing, attendance, vehicles, weighing, source_separation, contamination, process_controls |
| Environment | leachate, stormwater, gas, burning, odour, fire, water/soil monitoring, nearby waterbody, wetland, forest, protected area |
| Legal | licence_type, licence_number, permit_date, EIA/IEE, inspection_date, violation, enforcement_stage, closure_order, restoration_order |
| Pathway | source_generators, collection_route, transfer_point, treatment_route, product_market, reject_route, final_disposal, overflow_route |
| Evidence | source_id, page/table/line, evidence_grade, direct_or_inferred, contradiction_flag, uncertainty_note |

## Hidden-disposal indicators

The following indicators require separate coding rather than being absorbed into a facility label: waste deposited on unpaved ground; disposal beside a treatment plant; road-edge or seasonal overflow dumping; mixed waste at a compost facility; rejected or unsold product accumulation; residues without a named destination; uncontrolled leachate; open burning; access-road failure; waste stockpiles outside permitted polygons; facility label inconsistent with observed material practice; temporary emergency diversion; and lack of current weighing or status evidence.

## Minimum verification package per site

A site should not be treated as current and compliant until the evidence package contains a dated site polygon, operating status, accepted streams, current throughput or weighbridge record, licence/permit status, inspection or monitoring record, maintenance condition, residual destination, and recent independent or official observation. If any component is absent, the record remains explicitly incomplete.

## GIS interpretation rule

A facility point is not a disposal polygon. A treatment facility is not the same as its reject stockpile, adjacent temporary dump, leachate pond, access-road spill, or final-disposal destination. GIS layers must therefore distinguish `facility`, `operational_area`, `temporary_disposal_area`, `residual_destination`, `environmental_receiver`, and `uncertain_lead` geometries.

## Controlled descent rule

Desk research may prioritize sites for verification, but no current illegality, contamination, capacity failure, or causal spatial relationship should be claimed until the relevant source, date, geometry, and material pathway are independently matched. Fieldwork begins only after the register identifies a prior system hypothesis and a specific unresolved verification question.
