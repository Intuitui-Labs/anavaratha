# Anavaratha GIS Package — How to Use and Source Register

## What this package is

This folder contains real, usable GIS files for Anavaratha’s first Sri Lanka national waste-system exploration. The files are supplied in **GeoJSON**, **CSV**, and **ESRI Shapefile** formats so they can be opened without proprietary software. The package deliberately separates measured or official denominators from exploratory OpenStreetMap mapping and from derived analytical outputs.

## Easiest way to open the files

The recommended free desktop application is [QGIS](https://qgis.org/). Install QGIS, open a new project, and drag any `.geojson` or `.shp` file into the map canvas. For a CSV containing longitude and latitude, use **Layer → Add Layer → Add Delimited Text Layer**, select the longitude field as X and latitude as Y, and set the coordinate reference system to **EPSG:4326 — WGS 84**. The CSV analytical tables can also be opened in LibreOffice Calc or Excel.

For a quick browser preview, upload a GeoJSON file to [geojson.io](https://geojson.io/). Do not upload sensitive or unpublished field data to a public website. The PNG files are static maps for visual reference; they are not editable spatial layers.

## Files to start with

| File | What it contains | How to use it |
|---|---|---|
| `CPH2024_district_denominators.geojson` | 25 Sri Lankan district polygons joined to 2024 population, household, and occupied-housing denominators | Base district map and denominator layer |
| `OSM_Sri_Lanka_waste_sites.geojson` | 118 OSM waste-related points/centroids from the 22 Aug 2026 snapshot | Exploratory mapped-feature review only |
| `OSM_Sri_Lanka_receiving_environments.geojson` | 30,208 OSM water, wetland, forest, and protected-area point/centroid features | Exploratory receiving-environment context only |
| `lka_admin_boundaries_unzipped/lka_admin2.*` | Original Admin2 Shapefile components from the boundary source | Alternative district-boundary format |
| `ANAVARATHA_OSM_WASTE_RECEIVING_PROXIMITY_V0_1.csv` | Nearest-feature distances and threshold flags | Audit individual OSM points and their nearest mapped environments |
| `ANAVARATHA_OSM_WASTE_CLUSTERS_V0_1.csv` | DBSCAN labels from the OSM point layer | Explore mapped-tag density, not actual waste clusters |
| `ANAVARATHA_NSDI_SEWER_FEATURES_BY_DISTRICT_V0_1.csv` | District summary of official NSDI sanitary-sewer feature counts | Utility context; not solid-waste capacity |

## Important interpretation rules

The OSM waste layer is **not** a complete facility registry. A mapped point does not prove that a facility is active, legal, permitted, safe, or has usable capacity. A missing point does not prove that no facility exists. The receiving-environment layer is also incomplete and uses point/centroid representations for proximity screening; it does not establish contamination, illegal disposal, hydrological connection, or ecological impact.

The district population layer is a denominator, not a waste-generation measurement. World Bank What a Waste 3.0 country series is maintained separately because its years, definitions, and denominators are not compatible with a district-level facility inventory. The NSDI sanitary-sewer layer describes wastewater infrastructure and must not be relabeled as solid-waste capacity.

## Source register

| Package layer | Original source | Access or snapshot date | Source URL | License/usage note |
|---|---|---:|---|---|
| 2024 population, households, occupied housing | Sri Lanka Department of Census and Statistics, Census of Population and Housing 2024 | 2026-08-22 | https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024 | Confirm DCS terms before redistribution beyond research use |
| District boundaries | HDX/OCHA COD-AB, sourced from Survey Department of Sri Lanka | 2026-08-22 package audit | https://data.humdata.org/dataset/cod-ab-lka | Check HDX and Survey Department attribution/terms |
| Original Admin2 Shapefile | Same HDX/OCHA COD-AB source | 2026-08-22 package audit | https://data.humdata.org/dataset/cod-ab-lka | Keep source attribution with derived files |
| Waste-related mapped features | OpenStreetMap contributors via Overpass API | 2026-08-22 06:08 UTC | https://www.openstreetmap.org/ ; https://overpass-api.de/ | ODbL attribution required; see https://www.openstreetmap.org/copyright |
| Receiving-environment mapped features | OpenStreetMap contributors via Overpass API | 2026-08-22 06:12 UTC | https://www.openstreetmap.org/ ; https://overpass-api.de/ | ODbL attribution required; see https://www.openstreetmap.org/copyright |
| Sanitary-sewer utility layers | Sri Lanka NSDI ArcGIS REST service, Utilities_Communications | 2026-08-22 | https://gisapps.nsdi.gov.lk/server/rest/services/SLNSDI/Utilities_Communications/MapServer | Preserve NSDI/Survey Department attribution and service terms |
| World Bank waste series | World Bank, What a Waste 3.0 / Data360 | 2026-08-22 package audit | https://data360.worldbank.org/en/dataset/WB_WAW | Check World Bank data terms and cite the relevant series year |

## Coordinate systems and joins

The GeoJSON files use **EPSG:4326 / WGS 84**. Distance calculations in the proximity CSV were performed in an appropriate projected coordinate system, **EPSG:32644 / UTM Zone 44N**, before results were returned with longitude and latitude identifiers. The district join uses the district code retained in the boundary layer; spelling normalization between `Monaragala` and `Moneragala` was explicitly documented.

## Suggested first QGIS workflow

Load `CPH2024_district_denominators.geojson` first. Apply graduated colour to `population_2024`. Add `OSM_Sri_Lanka_waste_sites.geojson` as a point layer and style it by its raw OSM category. Add `OSM_Sri_Lanka_receiving_environments.geojson` only after setting a light, transparent style. Use the proximity CSV as a table for review, not as a pollution layer. Save the project as a `.qgz` file so the layer paths and styling are retained.

## Citation and attribution

When sharing maps made from this package, include: “Contains information from OpenStreetMap contributors, which is available under the Open Database License (ODbL).” Also cite the DCS 2024 Census, HDX/OCHA COD-AB, and Sri Lanka NSDI as applicable. Derived filenames should not be presented as official government inventories.
