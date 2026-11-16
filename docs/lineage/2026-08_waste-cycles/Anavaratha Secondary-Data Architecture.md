# Anavaratha Secondary-Data Architecture

## 1. Purpose

Before fieldwork, Anavaratha should assemble a structured evidence base from existing documents, statistics, maps, administrative records, research papers, satellite-derived layers, and publicly available datasets. The purpose is not to create a definitive national estimate immediately. It is to identify what is known, what can be compared, what can be mapped, what remains uncertain, and what fieldwork would most efficiently resolve.

## 2. Evidence layers

| Layer | Main question | Candidate source types | Desk-stage output |
|---|---|---|---|
| Administrative geography | What are the boundaries and jurisdictions? | Official boundary files, local-authority records, gazetteers | Boundary register and map |
| Population and activity | Where do people and economic activities concentrate? | Census, household statistics, business or land-use data | Denominator and activity map |
| Waste generation | How much waste is reported or estimated? | CEA, local authorities, studies, facility records | Source-comparison table |
| Collection and transport | Which areas and routes are served? | Authority schedules, route documents, contractor records | Service-coverage hypothesis |
| Recovery | What formal and informal recovery exists? | Facility lists, recycler interviews, studies, directories | Recovery-chain inventory |
| Disposal and accumulation | Where are final-disposal and persistent-burden locations? | Facility records, reports, imagery, complaint records, news | Risk and hotspot candidate list |
| Ecological condition | What ecological assets and pressures exist? | Land cover, forest, wetland, water, rainfall, elevation, satellite imagery | Ecological baseline layers |
| Social capability | What can people and communities access or use? | Public-space, road, school, health, livelihood, hazard data | Capability proxy layer |
| Governance and policy | Which rules, plans, and institutions shape outcomes? | Laws, policies, plans, budgets, agency mandates | Institutional map and policy matrix |

## 3. Dataset register

Every candidate dataset should be recorded in a register before use.

| Field | Description |
|---|---|
| `dataset_id` | Stable internal identifier |
| `title` | Official dataset or document title |
| `publisher` | Organization responsible for publication |
| `url_or_file` | Direct source link or local file path |
| `publication_date` | Date published or released |
| `reference_period` | Date or period represented by the data |
| `geographic_extent` | National, provincial, district, local authority, site, or route |
| `spatial_resolution` | Exact point, boundary, grid, raster resolution, or unknown |
| `unit` | Tonnes/day, households, hectares, index, etc. |
| `definition` | What the variable includes and excludes |
| `method` | Census, survey, administrative report, remote sensing, model, interview, etc. |
| `update_frequency` | One-off, annual, monthly, real-time, or unknown |
| `license_access` | Open, restricted, permission required, or unclear |
| `quality_grade` | A, B, C, or D based on evidence rules |
| `known_bias` | Missingness, outdated boundary, estimation, selection bias, or other issue |
| `intended_use` | Descriptive, denominator, spatial screening, hypothesis, or field sampling |

## 4. Evidence-quality grading

| Grade | Meaning | Permitted use |
|---|---|---|
| A | Primary official or directly measured source with clear method, period, boundary, and unit | Baseline input and public citation |
| B | Credible study or administrative source with mostly clear method but limited coverage or age | Supporting input and comparison |
| C | Secondary compilation, media report, model estimate, or partial record with meaningful limitations | Hypothesis generation or range only |
| D | Unverifiable, undated, unclear, or conflicting source | Do not use quantitatively; retain as lead to investigate |

A higher grade does not mean the dataset is universally better. A local route log may be more useful for a pilot route than a national estimate. The grade describes evidence quality for the intended use.

## 5. Data-harmonization rules

Never combine values until the team confirms that their definitions, reference periods, units, and geographic boundaries are compatible. If two sources disagree, preserve both values, explain the difference, and use a range or scenario rather than selecting one silently.

The desk model should distinguish four layers of information:

1. **Observed or recorded facts:** directly measured or officially recorded values.
2. **Derived values:** calculations based on documented inputs and formulas.
3. **Proxy variables:** indicators that stand in for a concept but do not measure it directly.
4. **Hypotheses:** plausible relationships requiring future validation.

## 6. Desk-based indicator matrix

| Indicator | Direction | Desk data possible? | Unit or representation | Main limitation |
|---|---|---|---|---|
| Reported waste generated | Freedom from Waste | Often, but definition-sensitive | tonnes/day or tonnes/month | Different boundaries and years |
| Collection coverage | Freedom from Waste | Sometimes | % of population, area, or generated mass | Coverage definitions vary |
| Uncontrolled-disposal candidates | Freedom from Waste | Partly | Count, area, persistence class | Incomplete and politically sensitive |
| Plastic-leakage risk | Freedom from Waste | Proxy only initially | Relative risk class | Needs field validation |
| Wetland or waterway proximity | Freedom to Flourish | Yes | Distance, intersect, area | Dataset date and resolution |
| Tree or vegetation cover | Freedom to Flourish | Yes, as a proxy | % cover, hectares, change | Cover is not survival or ecological function |
| Flood or heat exposure | Freedom to Flourish | Yes, as a proxy | Hazard class or exposure | Must distinguish hazard from lived impact |
| Public ecological access | Freedom to Flourish | Partly | Distance/accessibility class | Quality and safety not captured |
| Restoration potential | Freedom to Flourish | Modelled hypothesis | Opportunity class | Requires ground truth and community context |
| Ecological capability | Freedom to Flourish | Not directly at first | Composite only after validation | Risk of arbitrary weighting |

## 7. Desk analysis workflow

Begin by collecting the official boundary, population, policy, and waste-system records for the candidate pilot. Then create a source inventory and compare definitions. Next, add spatial layers for land use, waterways, wetlands, tree or vegetation cover, roads, settlements, and known facilities. After that, create a provisional flow model showing known nodes and unknown links. Finally, identify the smallest set of field observations that would most reduce uncertainty.

The output of the desk phase should be a **questioned map**, not a final map. Every layer should state what it can and cannot establish. For example, satellite-derived tree cover may identify vegetation presence but cannot prove tree survival, public access, ecological quality, or community benefit. A reported landfill inflow may describe facility receipts but cannot by itself reveal uncollected waste or informal diversion.

## 8. Causal reasoning protocol

For every proposed relationship, write a short causal statement using the following format:

> **Condition → mechanism → expected change → observable indicator → alternative explanation**

Example:

> **Irregular collection → household self-disposal or open burning → increased uncontrolled-disposal pressure → hotspot reports and repeat observations → seasonal flooding or temporary event may explain the observation instead.**

This format prevents the desk analysis from turning correlation into causation. It also creates a direct bridge from conceptual reasoning to future fieldwork.

## 9. Deliverables before fieldwork

The desk phase is complete only when the team has a pilot boundary file, dataset register, evidence-quality matrix, source-comparison table, initial waste-flow model, ecological-capability hypothesis map, uncertainty register, causal-hypothesis log, stakeholder and permission plan, and a field-priority list. Fieldwork should be designed to test specific unresolved claims rather than to collect data without a decision purpose.
