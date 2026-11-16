# Anavaratha Capacity and Facility Dimensions v0.1

## Purpose

The first GIS layer identifies population denominators, mapped waste-related features, receiving-environment context, and important data gaps. This report adds the **capacity and facility side** of the waste system. It asks not merely whether a compost plant, vehicle, landfill, recycling centre, or local-authority service exists, but whether it has a defined input boundary, usable throughput, recurrent support, ecological safeguards, and persistence.

The historical evidence base is the open-access IWMI report *Solid and Liquid Waste Management and Resource Recovery in Sri Lanka: A 20 city analysis* (published 2020, using information available in 2019, site visits, and expert interviews). The report provides city-level service and facility observations but warns that the information changes over time.[1] It is therefore used as a **historical baseline**, not as a current national inventory.

## Capacity is multidimensional

> **A facility is an asset. Capacity is the ability of a functioning system to receive, transform, transfer, recover, contain, monitor, and sustain material under actual conditions.**

| Dimension | Core question | Variables Anavaratha must record |
|---|---|---|
| Demand and pressure | How much material must the system handle? | Population, households, activity, seasonal population, generation estimate, stream composition, reference period |
| Collection/capture | How much material enters an organized pathway? | Collection quantity, geographic coverage, frequency, route length, source separation, missed service, informal recovery |
| Asset capacity | What infrastructure and equipment exists? | Facility type, owner, location, design specification, vehicle class, nominal volume, land area |
| Usable capacity | What can operate now? | Downtime, fuel, maintenance, staffing, access, contamination, weather, public acceptance, operating hours |
| Throughput | What quantity and quality is processed? | Inflow, accepted feed, processed output, recovery, reject, residual, unit, period, input/output boundary |
| Residual/disposal capacity | Where does non-recovered material go? | Disposal site, remaining life, containment, leachate, drainage, slope, receiving environment, transport distance |
| Recurrent capacity | Can the pathway persist? | Budget, revenue, user fees, fuel, repair, replacement, contracts, salary, market price, buyer demand |
| Institutional capacity | Who can decide, coordinate, enforce, and report? | Mandate, staff, procurement, data system, inspections, complaints, legal status, inter-agency coordination |
| Worker and social capacity | Can people participate and work safely? | OHS equipment, training, injury exposure, labour conditions, trust, complaints, source-separation behaviour |
| Market capacity | Can recovered materials leave the facility? | Buyer, material grade, price, transport, storage, rejection, seasonal demand |
| Ecological receiving capacity | What happens if the pathway fails or leaks? | Water, wetland, forest, protected area, flood, soil, groundwater, catchment, restoration limit |
| Persistence and spillover | Does improvement last and where does burden move? | Baseline, post-intervention outcome, operating continuity, residual destination, displaced burden |

## Historical city service register

The register contains **20 local-authority service-context records** and **13 explicit facility-capacity records**. The service values are not harmonized into one national rate because their periods, sources, and boundaries differ. Values such as “generation,” “collection,” and “processed” must remain source-specific.

| City | Generation reported | Collection reported | Historical service/facility reality | Source-period caution |
|---|---:|---:|---|---|
| Anuradhapura | 72 MT/day estimated | 31 MT/day | Keerikkulama compost facility; adjacent open dump | Mixed waste received and biodegradable processed are different boundaries |
| Badulla | 36 MT/day estimated | 13–15 MT/day | Composting with adjacent open dumping | Seasonal collection rises were separately reported |
| Batticaloa | 69 tons/day estimated | 52.5 tons/day | Composting, recycling, open dumping | Only part of collected waste reported segregated; 2016 plant throughput |
| Colombo | 800 MT/day | 450–500 MT/day degradable | Large collection fleet; open-dumping/composting context | Exact denominator and reference period are not uniform |
| Galle | 84 MT/day estimated | 32 MT/day; 40–42 in December | Rathgama regional compost facility and disposal sites | Plant accepts material from beyond Galle MC |
| Jaffna | 104.87 tons/day | 82.3 tons/day | Kakkaithivu compost facility; Kallundai disposal context | JICA 2016 values |
| Kalutara | 30 tons/day | 26 tons/day in 2014 | Pohorawatta compost facility and controlled-landfill context | Current status not established |
| Kandy | 179 tons/day | 150 tons/day | Large fleet; open dumping and controlled-landfill context | UDA 2019 values; fleet nominal capacity is not service capacity |
| Kilinochchi | 46 tons/day estimated | 8 tons/day | Open-dumping system | Total-collection value is source-reported and historical |
| Kurunegala | 48 MT/day | 44 MT/day | Sundarapola compost/disposal system | Approximately 40 tons/day disposed; worker attendance disrupted plant operation |
| Mannar | 28 MT/day | 25 MT/day | Small compost/recycling activity; multiple dumping locations | No source segregation; difficult by-roads |
| Matale | 38 MT/day estimated | 28 MT/day | Composting, landfilling, recycling | Collection-route and plant observations are source-period values |
| Matara | 58 MT/day estimated | 30–35 MT/day in 2019 | Kotawila compost facility and recycling plant | 18–20 MT/day biodegradable output is not the same as mixed-waste input |
| Mullaithivu | 16.6 MT/day estimated | 2 MT/day in 2013 | Open disposal into forest area reported | Historical condition; current legality and site condition unknown |
| Negombo | 110 MT/day estimated | 110 MT/day; 100% in profile | Kurana compost plant, recycling centres, Ovitiyawatta disposal | Tourism seasonality and public objections affect usable intake |
| Nuwara Eliya | 32 MT/day | 21 MT/day in JICA 2016 context | Moonplains semi-aerobic engineered landfill and plastic recycling | Historical facility baseline, not current compliance proof |
| Puttalam | 27 MT/day estimated | 10 MT/day | Compost facility at dump-site complex | Design capacity reported unknown |
| Ratnapura | 37 MT/day estimated | 30 MT/day in 2013 | Kanadola compost/recycling and open-dumping context | Downstream agricultural burden reported; denominators need verification |
| Trincomalee | 62.09 MT/day | 39 MT/day in JICA 2016 | Kinniya disposal site approximately 14 km away | Long transport distance is a pathway variable, not capacity itself |
| Vavuniya | 75 MT/day estimated | 20 MT/day | Pampaimadu disposal; small compost plant reported abandoned | Abandonment is historical reported status and needs current verification |

The full source-traceable dataset is `ANAVARATHA_IWMI_HISTORICAL_CAPACITY_FACILITY_REGISTER_V0_1.csv`.

## Design capacity versus observed throughput

Only seven facility records provide sufficiently compatible design and processed-throughput values to calculate a transparent utilization range. The calculation is not a performance score; it is a source-period comparison between two reported quantities with the same facility boundary and daily mass unit.

| Facility | Design capacity | Processed throughput | Source-period utilization comparison |
|---|---:|---:|---:|
| Badulla compost plant | 25–30 MT/day | 4.5 MT/day | 15–18% |
| Batticaloa compost plant | 12 MT/day mixed waste | 2.6 MT/day | 21.7% |
| Galle/Rathgama compost plant | 50 MT/day | 46 MT/day | 92% |
| Kalutara compost plant | 40 tons/day | 30 tons/day | 75% |
| Kurunegala compost plant | 40 MT/day | 2 MT/day | 5% |
| Matale compost plant | 5 MT/day | 5 MT/day | 100% |
| Negombo compost plant | 10 MT/day | 8 MT/day | 80% |

These values show why “capacity exists” is too weak a variable. A nominally large plant can process little material because of mixed feed, labour absence, contamination, maintenance, or social opposition. A high source-period utilization comparison also does not demonstrate durable operation, product quality, legal compliance, or ecological safety. The complete audit is `ANAVARATHA_IWMI_CAPACITY_UTILIZATION_AUDIT_V0_1.csv`.

## Facility-specific lessons

Anuradhapura’s reported plant received about 24 MT/day of mixed waste but processed about 8 MT/day of biodegradable material, while the adjacent residual stream was openly dumped. The source therefore provides at least three separate variables: mixed-waste inflow, biodegradable processing, and residual disposal. They must not be collapsed into “plant capacity.”

Badulla and Kurunegala illustrate a design-to-operation gap. Badulla’s reported 25–30 MT/day design capacity corresponded to about 4.5 MT/day processed. Kurunegala’s reported 40 MT/day design capacity corresponded to about 2 MT/day, with worker absence cited as an operational disruption. These are capacity-realization questions, not evidence that the plants were legally noncompliant at present.

Galle’s Rathgama plant illustrates regional aggregation. Its reported 46 MT/day processed included approximately 18 MT/day from Galle MC, so the plant’s throughput cannot be compared directly with Galle’s generation without origin shares. Matara similarly reports 35 MT/day mixed-waste handling and 18–20 MT/day biodegradable processing, requiring input/output-boundary separation.

Negombo illustrates **socially constrained usable capacity**. The open UNEP/IGES assessment reports a nominal 10 MT/day compost facility whose intake was limited to 6–8 MT/day because of public complaints and objections related to flies and odour.[2] The same assessment reports approximately 2.37 +/- 3.9 MT/month recovery at the city recycling facility. This is a strong example of nominal design capacity being reduced by social acceptance, nuisance, and quality constraints.

Jaffna’s 5 tons/day design value and 9–10 tons/week processed value are intentionally not converted into daily utilization. The units and period do not support a precise daily comparison. Puttalam, Matara, Ratnapura, and Vavuniya show other forms of uncertainty: unknown design capacity, mismatched input/output boundaries, or no usable throughput reported.

## What the next national capacity inventory must contain

A current facility register should be built as a **facility-event table**, not a static list. Each observation should identify the facility, the date, the source, the observer, and whether the value is design, installed, available, operating, measured, estimated, planned, or unknown.

| Field group | Required fields |
|---|---|
| Identity | Stable facility ID, name, aliases, local authority, district, owner, operator, coordinates/boundary |
| Legal status | Land status, environmental licence, permit, approval, licence date, expiry, inspection date, enforcement stage |
| Material boundary | Stream accepted, source, mixed/separated, hazardous exclusions, moisture/quality restrictions |
| Physical capacity | Design MT/day, installed equipment, land area, cell/stock volume, storage, remaining life |
| Operational capacity | Actual inflow, accepted feed, processed output, rejects, residuals, operating days, downtime, reason for downtime |
| Collection interface | Catchment, route count, collection frequency, vehicles, payload, vehicle availability, transfer points |
| Human capacity | Staff establishment, staff present, skill, attendance, contractor, OHS equipment, injuries/training |
| Recurrent finance | Annual operating budget, fuel, repair, maintenance, salaries, revenue, grants, contract terms |
| Market interface | Product, quality test, buyer, price, storage, rejection, sales volume, seasonal demand |
| Environmental safeguards | Leachate, drainage, groundwater, odour, dust, fire, slope, flood, buffer, receiving water, monitoring results |
| Institutional reality | Complaints, inspections, notices, court matters, corrective action, restoration, monitoring, persistence |
| Evidence | Source URL/document, page/table, date observed, evidence grade, confidence, unresolved contradiction |

## Evidence hierarchy

For a current capacity map, the preferred hierarchy is: audited facility operating records or weighbridge data; dated government inspection or licence records; signed local-authority records with facility coordinates; independent field observations with photographs and measurements; engineering design documents; multi-source assessments with site visits; credible research using explicit methods; official project or policy claims; media reports; and unverified anecdotes.

Lower-ranked sources remain valuable as leads. They must be coded as **reported**, **historical**, **planned**, or **unverified**, not promoted into operational fact. The register therefore includes `evidence_grade`, `currentness`, `status_as_reported`, and `notes` fields.

## Immediate next acquisition priorities

The most important missing spatial layer is a current, comparable registry of solid-waste facilities and disposal sites. The acquisition request should be directed to the Central Environmental Authority, Waste Management Authority of Western Province, National Solid Waste Management Support Center, provincial/local authorities, and relevant ministries. The requested fields should follow the table above, with special emphasis on coordinates, licence status, design versus actual throughput, operating dates, residual destinations, and inspection records.

The second priority is current transport/service data: collection zones, routes, frequency, fleet availability, staff, maintenance, and transfer stations. Without this, population-to-facility proximity can be mistaken for service access.

The third priority is authoritative ecological and pathway layers: hydrology and catchments, roads, forest/reserve boundaries, protected areas, wetlands, flood-prone areas, and land cover. OSM can remain a discovery and screening layer, but it must not substitute for these authoritative layers in legal or ecological exposure analysis.

## GIS integration rule

The facility register should join to GIS only after each facility record has a stable location and evidence state. Suggested GIS fields are `facility_id`, `facility_type`, `legal_status`, `operating_status`, `design_capacity_mt_day`, `actual_throughput_mt_day`, `capacity_period`, `source_separation_status`, `residual_destination`, `inspection_status`, `complaint_count`, `enforcement_stage`, `restoration_status`, `source_grade`, and `location_confidence`.

A future map may show verified facilities, historical facilities, planned facilities, ambiguous mapped points, and excluded records in different symbology. It must never show them all as one undifferentiated “waste facility” layer.

## References

[1] Jayathilake, N., Kumara, I. U., & Fernando, S. (2020). *Solid and Liquid Waste Management and Resource Recovery in Sri Lanka: A 20 city analysis*. International Water Management Institute. https://cgspace.cgiar.org/bitstreams/b61bc962-4184-4f5b-9526-fe97c7384625/download

[2] United Nations Environment Programme / IGES. *State of Municipal Solid Waste Management in Negombo City, Sri Lanka*. https://www.unep.org/ietc/resources/report/state-municipal-solid-waste-management-negombo-city-sri-lanka

[3] Madusanka, K. H. P., Matsuto, T., Tojo, Y., et al. (2017). Questionnaire and onsite survey on municipal solid waste composting in Sri Lanka. *Journal of Material Cycles and Waste Management*, 19, 804–814. https://doi.org/10.1007/s10163-016-0479-y

[4] Sri Lanka Department of Census and Statistics. Census of Population and Housing 2024. https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024

[5] Sri Lanka NSDI, Utilities_Communications ArcGIS REST service. https://gisapps.nsdi.gov.lk/server/rest/services/SLNSDI/Utilities_Communications/MapServer
