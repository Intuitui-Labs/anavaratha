# Anavaratha Capacity and Action Exploration v0.1

## 1. What is What a Waste 3.0?

**What a Waste 3.0** is a World Bank global reference dataset and report on municipal solid waste management. The portal states that it covers 217 economies and 262 cities, with indicators for waste generation, composition, collection, treatment and disposal, legal and institutional arrangements, plastics management, and related topics.[1]

It is best understood as a **comparative evidence database**, not as a live operational control room for every country. The World Bank aggregates official statistics, public-sector publications, international-agency documents, academic studies, and estimates. The portal explicitly notes that definitions and data quality can vary across observations and that source and estimation information should be consulted.[1]

## 2. What is included for Sri Lanka

The raw Sri Lanka subset contains 38 rows across nine indicators. The observations cover different years and dimensions rather than one unified current inventory.

| Evidence area | Sri Lanka record | Reference year | Interpretation |
|---|---|---:|---|
| MSW generation | 2,971,830 tonnes/year and 0.359699 kg/person/day | 2021 | Observed/estimated in dataset |
| MSW generation | 2,847,753.7 tonnes/year and 0.342720 kg/person/day | 2022 | Observed/estimated in dataset |
| MSW generation projections | 3,155,836.8; 3,797,570.7; 4,362,359.9 tonnes/year | 2030, 2040, 2050 | Model projections |
| Collection coverage | 47.35% | 2021 | Source-specific collection indicator |
| Treatment/disposal | 52.65% uncollected; 24.81% open dump; 13.88% composting; 8.60% incineration; 0.06% sanitary landfill | 2016 | Pathway shares from a source-specific record |
| Management of uncollected waste | 59.402% open burned; 29.353% dumped on land; 9.713% recycled/composted; 1.11% aquatic environment; 0.425% other | 2012 | Shares of uncollected waste, not all generated waste |
| MSW composition | Food 62%; other 17%; paper/cardboard 7%; plastic 6%; wood 6%; glass 2% | 2018 | Composition record |
| Non-municipal waste | E-waste 175,000 tonnes/year | 2022 | Non-municipal generation record |
| Legal/institutional arrangements | Categorical records | 2026 label in dataset | Status categories, not service-performance measures |
| Plastic policy and EPR | Categorical records | 2026 label in dataset | Policy/action status categories, not verified outcomes |

The table demonstrates why the dataset is useful but must not be read as a single current national time series. The collection indicator, treatment/disposal indicator, uncollected-waste indicator, composition indicator, and generation series refer to different periods and denominators.

## 3. What is not included, or is not yet sufficient for Anavaratha

What a Waste 3.0 does not provide a complete, current, and locally consistent record of the following for Sri Lanka:

| Missing or insufficient area | Why it matters to Anavaratha |
|---|---|
| Local-authority-level current flows | The project needs descent from national structure to system types and places |
| Full material inflow inventory | Waste generation alone does not show upstream products, packaging, imports, or production |
| Reliable facility registry and usable capacity | A facility’s existence is not its operating capacity |
| Fleet, route, downtime, fuel, and maintenance records | Collection performance depends on daily operations |
| Staffing, worker conditions, and informal recovery | Capacity and burden are distributed through labor and hidden actors |
| Recurrent budgets, fees, contracts, and maintenance costs | Capital projects can fail without operating finance |
| Current stock and accumulation measures | Waste can disappear from flows while remaining in dumps, land, water, or storage |
| Destination and burden-transfer network | Management in one area may shift risk to another community or ecosystem |
| Project implementation and persistence | A policy or facility is not an outcome; Anavaratha needs before/after and post-support evidence |
| Harmonized current plastic inventory | Sri Lanka’s action plan identifies inventory and production-data gaps |
| Consistent national definitions | Conflicting boundaries and years prevent false precision |

The major missing feature is **operational context**. What a Waste 3.0 can indicate that collection or disposal is inadequate, but it usually cannot explain which binding constraint caused the failure, who controlled it, who bore the burden, or whether a response persisted.

## 4. Capacity-side evidence currently available

The current real-data evidence provides only partial capacity proxies. The 2021 collection coverage of 47.35% is an outcome or service indicator, not a vehicle or staffing inventory. The 2016 treatment/disposal shares show the pathway condition at that time, but they do not reveal facility age, operating hours, maintenance, route reliability, worker safety, or remaining usable capacity. The categorical institutional indicators show that legal or policy arrangements are recorded, but not whether institutions can enforce, coordinate, finance, or sustain them.

The Sri Lankan National Action Plan provides richer **action architecture** than capacity measurement. It includes goals for inventory, single-use-plastic reduction, collection and safe treatment, packaging reduction, and marine-pollution reduction, alongside proposed actions for steering committees, flow tracking, producer registration, facility audits, community collection, buyer–seller platforms, local-government by-laws, and local-authority waste profiles.[2]

These are valuable action-side records, but they must be classified correctly:

> **A target is an intention. An action is an input or activity. An output is a deliverable. An outcome is a measured change. Persistence is sustained change after support or attention changes.**

## 5. Anavaratha action-side data model

The next capacity/action database should contain one record per asset, operating condition, policy action, intervention, output, outcome, and persistence observation. Each record should include its owner, location, material stream, date, funding, boundary, denominator, evidence source, implementation status, and confidence.

| Record family | Example fields |
|---|---|
| Facility | Type, owner, coordinates, design capacity, usable capacity, downtime, input, output, residuals |
| Fleet and route | Vehicle type, count, availability, route, frequency, fuel, maintenance, missed service |
| Workforce | Staff, contractor, informal actors, hours, safety, pay, training, exposure |
| Finance | Budget, fees, contracts, grants, recurrent cost, maintenance, payment reliability |
| Governance | Mandate, institution, by-law, enforcement, coordination, data responsibility |
| Intervention | Problem, action, target group, start, end, funding, implementation status |
| Outcome | Baseline, indicator, change, comparison, independent verification |
| Persistence | Status after project/support/leadership change |
| Spillover | Spatial, social, ecological, financial, material, temporal, or data transfer |

## 6. Current conclusion

What a Waste 3.0 is a valuable first layer for **national comparison and source discovery**, but it is not the Anavaratha model. It gives pressure, composition, some pathways, and selected policy/institutional statuses. Anavaratha must add the missing capacity and action dimensions: what exists, what is usable, how it operates, who controls it, how it is financed, what interventions were attempted, what changed, what persisted, and where burden moved.

The immediate next step is to build the capacity/action evidence library from Sri Lankan official sources, project documents, facility records, local-government records, and evaluations. We should not yet calculate a single pressure–capacity score because the capacity variables are not sufficiently complete or harmonized.

## References

[1] World Bank Data360, “What a Waste (3.0).” https://data360.worldbank.org/en/dataset/WB_WAW

[2] Ministry of Environment Sri Lanka, “National Action Plan on Plastic Waste Management 2021–2030.” https://www.ccet.jp/sites/default/files/2021-08/srilanka_report_web_fin_pw.pdf
