# Anavaratha GIS Data Inventory v0.1

## Current real spatial layers

| Layer | Source | Snapshot or date | Coverage | Current use | Limitation |
|---|---|---|---|---|---|
| District boundaries | HDX/OCHA COD-AB, sourced from Survey Department of Sri Lanka | Dataset reviewed 30 Oct 2025; modified 26 Jan 2026 | 25 Admin2 districts | Join 2024 census denominators; national choropleths | HDX notes Admin4 name conflicts; stable codes required |
| National spatial services | Sri Lanka NSDI | Page last updated 14 Jul 2026 | WMS categories for boundaries, environment, inland waters, transport, utilities, biota, climate, economy, society, and earth cover | Identify official spatial-service endpoints and possible overlays | Layer access and metadata must be checked service by service |
| Census denominators | Department of Census and Statistics 2024 census workbooks | 2024 | 25 districts; 2024 population and household denominators | Pressure denominator layer | Population is not waste generation; district-only join at this stage |
| Waste-related facilities and sites | OpenStreetMap Overpass extract | OSM snapshot 22 Aug 2026 06:08 UTC | 118 geocoded features in Sri Lanka | Exploratory points for landfill, waste disposal, recycling, transfer, and wastewater categories | Crowdsourced and incomplete; tags can be misclassified; not a national inventory |

## First join result

The HDX Admin2 boundary file contains 25 districts. A spelling difference between `Monaragala` in the boundary source and `Moneragala` in the census source was explicitly normalized. All 25 districts now match the 2024 census denominators. The normalization is recorded in `join_census_boundaries.py` and the output in `census_boundary_join_audit.txt`.

## OSM extract result

The Overpass query returned 118 geocoded features at the 22 August 2026 OSM snapshot. The categories were: 39 `landuse=landfill`, 30 `man_made=wastewater_plant`, 28 `amenity=recycling`, 14 `amenity=waste_disposal`, and 4 `amenity=waste_transfer_station`, with 3 wastewater features carrying both `industrial` and `man_made` tags. Some names appear potentially misclassified or ambiguous, such as `Fishing Cat`, `empty land`, and `Pothuvil yard`; these must be manually reviewed and not automatically interpreted as active legal waste facilities.

## Immediate analytical consequence

The first GIS layer can reliably show population denominators by district and an exploratory map of mapped waste-related features. It cannot yet show actual national waste-generation surfaces, complete facility capacity, current open-dumpsite prevalence, or legal compliance. Those require additional official records, facility verification, or carefully labeled remote-sensing and field evidence.

## Next GIS steps

1. Validate each OSM feature category and remove obviously unrelated or ambiguous features from the active facility layer while retaining them in a raw layer.
2. Retrieve official or authoritative waste-facility and land-use layers through NSDI, CEA, WMA, Survey Department, and project records.
3. Add hydrology, forests, reserves, wetlands, protected areas, roads, settlements, and activity proxies.
4. Join compatible population and waste observations at the same geographic unit and period.
5. Calculate only transparent distance, proximity, density, coverage, and gap indicators before attempting spatial correlation or clustering.
