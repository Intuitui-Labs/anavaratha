# Anavaratha National Spatial Exploration v0.1

## Purpose

This report establishes the first real GIS layer for Anavaratha’s waste-focused eagle-view analysis. It tests whether population denominators, mapped waste-related features, public-utility context, and receiving-environment proximity can be brought into one spatial workflow without pretending that incomplete maps represent the full waste system.

## Sources and spatial layers

| Layer | Source and date | Coverage | Status in analysis |
|---|---|---|---|
| District population and households | Sri Lanka Department of Census and Statistics, 2024 census workbooks | 25 districts | Real denominator layer |
| District boundaries | HDX/OCHA COD-AB version 03, sourced from Survey Department; reviewed 30 Oct 2025 and modified 26 Jan 2026 | 25 Admin2 districts | Reproducible boundary layer |
| Waste-related mapped features | OpenStreetMap Overpass extract, 22 Aug 2026 | 118 geocoded features | Exploratory mapped-feature layer |
| Receiving environments | OpenStreetMap Overpass extract, 22 Aug 2026 | 30,208 geocoded point/centroid features | Exploratory proximity context |
| Utility context | Sri Lanka NSDI Utilities_Communications ArcGIS REST service, accessed 22 Aug 2026 | 118 interceptor manholes, 61 manholes, 35 force-main lines, 89 gravity-main lines, 119 lateral-pipeline lines | Official wastewater-network proxy, not solid-waste capacity |
| National waste pressure | World Bank What a Waste 3.0 | Sri Lanka country series | Country-level pressure series, not a spatial surface |

## Data-integrity results

The 25 district polygons, 118 waste-related features, and 30,208 receiving-environment features have valid geometries, no duplicate IDs in the active layers, and EPSG:4326 coordinates. The census-to-boundary join matches all 25 districts after explicitly recording the source spelling normalization from `Monaragala` to the census spelling `Moneragala`.

The main uncertainty is not geometry validity but **semantic and coverage validity**. Ninety-four of the 118 waste-related OSM features do not have a name tag. The OSM layers are crowdsourced, potentially incomplete, and occasionally ambiguous. For example, `landuse=landfill`, `amenity=recycling`, and `amenity=waste_disposal` do not by themselves prove legal status, active operation, usable capacity, or current disposal practice.

## Population and mapped-feature relationship

Across 25 districts, mapped OSM waste-related feature count has Pearson correlation of 0.803 with the 2024 population denominator and rank correlation of 0.687. Colombo and Gampaha are high on both population and mapped-feature count; Batticaloa and Badulla have relatively high mapped-feature counts for their populations.

This is not evidence that population causes mapped waste infrastructure, nor that high population produces more waste burden in those districts. It may partly reflect urban mapping intensity, accessibility, tagging practices, and the fact that more populous places receive more attention. It is a useful diagnostic result: mapped-feature coverage appears structured rather than random, so any future GIS model must include a mapping-coverage or observation-intensity control.

## Proximity to receiving environments

Of 118 mapped waste-related points, 53 are within 1 km of a mapped waterway and 107 within 5 km. Eighty-two are within 1 km of a mapped waterbody or wetland, and all 118 are within 5 km. Four are within 1 km of a mapped protected area and 31 within 5 km. Forty-two are within 1 km of mapped forest and 92 within 5 km.

These results do not establish contamination, illegality, hydrological connection, or ecological impact. They are nearest-feature proximity indicators using OSM point/centroid representations. The high waterbody/wetland proximity is partly expected because Sri Lanka has dense mapped inland-water features and because the analysis uses nearest mapped points rather than flow-connected catchments. The result is therefore a candidate-receptor screening layer, not a risk map.

## Mapped-feature clusters

Using DBSCAN with a 5 km neighbourhood and minimum three mapped features, 60 of 118 waste-related features fall into 11 exploratory clusters, while 58 are noise under that rule. The largest cluster contains 19 mapped features near approximately 6.9042, 79.9188 and combines landfill, recycling, and wastewater tags. Other clusters are distributed across several urban, coastal, and interior locations.

These are clusters of mapped tags, not clusters of illegal dumping, actual waste generation, usable capacity, or environmental burden. The clustering is useful for prioritizing data-quality checks and later testing whether mapped infrastructure clusters correspond to population, roads, activity, facilities, or observation intensity.

## Capacity interpretation

The present GIS package does not yet contain a compatible national solid-waste capacity layer. The NSDI sewer records are an official and useful contextual infrastructure layer, but they describe wastewater-network assets and are concentrated in Colombo in the retrieved service response. They cannot be used as solid-waste treatment or disposal capacity.

The next real capacity layers must include, where obtainable: facility type and legal status; design and usable capacity; actual throughput; collection vehicles and uptime; route and frequency; staff; operating budget; maintenance; leachate and monitoring; transfer points; recycling and composting outputs; and receiving-site condition. Each should carry a date, geographic unit, source, and status such as measured, reported, planned, or unknown.

## National spatial interpretation

The first GIS result is not “where Sri Lanka has the most waste.” It is a layered diagnosis:

> **Population pressure is spatially concentrated; mapped waste-related features are unevenly recorded; receiving environments are widely proximate; official utility mapping is domain-specific and geographically incomplete; and current national solid-waste capacity remains unmeasured in a compatible spatial form.**

This is exactly why the GIS work must remain an eagle-view system rather than a premature local case map.

## Outputs

- `CPH2024_district_denominators.geojson`
- `ANAVARATHA_GIS_POPULATION_OSM_WASTE_V0_1.png`
- `ANAVARATHA_GIS_POPULATION_OSM_RELATIONSHIP_V0_1.png`
- `ANAVARATHA_GIS_WASTE_RECEIVING_PROXIMITY_V0_1.png`
- `ANAVARATHA_OSM_FEATURES_BY_DISTRICT_V0_1.csv`
- `ANAVARATHA_OSM_WASTE_RECEIVING_PROXIMITY_V0_1.csv`
- `ANAVARATHA_OSM_WASTE_CLUSTERS_V0_1.csv`
- `ANAVARATHA_NSDI_SEWER_FEATURES_BY_DISTRICT_V0_1.csv`
- `ANAVARATHA_GIS_LAYER_INTEGRITY_AUDIT_V0_1.csv`

## References

[1] Sri Lanka Department of Census and Statistics, 2024 Census of Population and Housing. https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024

[2] HDX/OCHA, Sri Lanka - Subnational Administrative Boundaries, sourced from Survey Department of Sri Lanka. https://data.humdata.org/dataset/cod-ab-lka

[3] Sri Lanka Survey Department, Geographical Information System and digital topographic data layers. https://survey.gov.lk/sdweb/pages_service_geo_information.php?id=df658590a4cbb1f955f5d386b242b6be8d5cadc0&l=s

[4] Sri Lanka NSDI, Spatial Data Services. https://nsdi.gov.lk/spatial-data-services

[5] World Bank, What a Waste 3.0 data portal. https://data360.worldbank.org/en/dataset/WB_WAW

[6] OpenStreetMap, map data and Overpass API extract accessed 22 August 2026. https://www.openstreetmap.org/ and https://overpass-api.de/
