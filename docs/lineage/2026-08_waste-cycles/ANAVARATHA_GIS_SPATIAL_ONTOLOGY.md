# Anavaratha GIS Spatial Ontology v0.1

## Purpose

The GIS layer of Anavaratha will not begin by mapping individual dumping points. It will first represent the waste system as a set of spatially connected pressures, pathways, capacities, and receiving environments. Local sites will be selected only after the broad layers are complete and comparable.

## Core spatial questions

1. Where are people, households, economic activities, visitors, markets, institutions, and industries concentrated?
2. Where is waste pressure likely to be generated, and which denominators support that inference?
3. Where are formal collection, transfer, treatment, recycling, composting, incineration, and disposal capacities located?
4. What pathways connect sources to facilities, receiving sites, water bodies, forests, wetlands, protected areas, and communities?
5. Where do pressure and usable capacity appear mismatched?
6. Where can burdens accumulate, leak, or be transferred across administrative boundaries?
7. Which clusters are data-supported, and which are only hypotheses requiring validation?

## Spatial layers

| Layer | Unit or geometry | Core variables | Main caution |
|---|---|---|---|
| Administrative | Province, district, DS division, local authority, GN division | Boundary, code, jurisdiction, date | Boundaries and codes may change over time |
| Population and households | District, DS, GN, settlement or grid where available | Population, households, housing, density | Census denominator is not equal to waste-generation denominator |
| Activity pressure | Point, polygon, grid, or proxy | Markets, tourism, industry, institutions, roads, daily visitors | Activity is often seasonal and incompletely recorded |
| Waste generation | Point, route, area, or administrative unit | Reported tonnes/day, composition, source type, year | Generation, collection, and disposal are different quantities |
| Collection and transport | Route, road network, transfer station, service area | Coverage, frequency, vehicle, route, destination | Service access does not prove route completion or final disposal |
| Facilities | Point/polygon | Type, legal status, capacity, operating status, licence, date | Nominal capacity may not be usable capacity |
| Disposal and leakage | Point/polygon, hotspot, corridor | Dump, burn site, litter, leachate, accumulation, evidence date | Public reports and remote sensing require verification |
| Ecological receptors | River, lake, wetland, forest, protected area, coastline | Distance, hydrology, land cover, ecological status | Proximity is not proof of causal contamination |
| Receiving burden | Site, downstream corridor, community, ecosystem | Accumulation, exposure, remediation liability, complaints | Burden may be displaced beyond the source jurisdiction |
| Time | Date, month, season, year, project phase | Trend, seasonality, event, policy effective date | Datasets may appear comparable while measuring different periods |

## Analytical units

The same waste system should be examined at several nested scales:

> **Island → province → district → administrative authority → service area → route → facility → receiving environment → specific site.**

The project must not infer a local condition from a national average, or a national pattern from one striking local site. Every result should state its geographic unit and the scale at which it is valid.

## Pressure and capacity variables

A provisional spatial pressure variable may combine only compatible measures such as population, households, documented economic activity, tourism or seasonal activity, and reported waste generation. Capacity should be represented through usable service and facility variables: collection frequency, route reliability, vehicle availability, facility operating status, treatment or disposal throughput, staff, maintenance, and legal authorization.

The first spatial mismatch measure is conceptual rather than a fabricated score:

> **Spatial system gap = pressure within or entering an area − usable capacity available to that pressure, adjusted for pathway distance, season, and receiving-site constraints.**

Until compatible data exist, the gap should be shown as a classified evidence layer—high, medium, low, or unknown—with the classification rule disclosed.

## Correlation and cluster discipline

A spatial correlation between population and waste reports does not establish causality. It may reflect reporting intensity, road accessibility, administrative boundaries, facility placement, tourism, or the fact that more people create more observation opportunities. Likewise, a cluster of reported dumping may be a cluster of complaints rather than a cluster of all dumping.

Anavaratha will therefore distinguish:

- **Observed cluster:** repeated geocoded evidence with comparable dates and definitions.
- **Reported cluster:** multiple reports but incomplete independent verification.
- **Modelled cluster:** pattern inferred from compatible data and an explicit method.
- **Hypothesized cluster:** plausible location requiring targeted validation.
- **Unknown:** insufficient evidence.

## Spatial descent gate

A place can descend to local analysis only when:

1. Its boundary and code are stable or time-adjusted.
2. The pressure denominator is defined.
3. The waste pathway is documented or explicitly hypothesized.
4. At least one capacity layer is available.
5. Receiving environments and possible burden transfer are mapped.
6. Dates and spatial resolutions are compatible.
7. The unresolved question is specific enough for later validation.

## Output sequence

The GIS work should first deliver a national data inventory, then broad pressure and capacity surfaces, then pathway and receiving-environment overlays, then uncertainty and cluster hypotheses, and only afterward a controlled descent into selected systems or localities.
