# Anavaratha Data Dictionary and Field Template

## Data principles

All records must be traceable to a measurement event, source document, interview, or observation. Do not overwrite original values. Store corrected values with a correction note and date. Use kilograms and tonnes consistently, and record whether a number was weighed, counted and converted, reported by an operator, surveyed, or modelled.

## Core identifiers

| Field | Type | Description | Example |
|---|---|---|---|
| `record_id` | text | Unique identifier for the row | `FLOW-0001` |
| `event_id` | text | Links the row to a measurement or observation event | `EVT-2026-001` |
| `date` | date | Date of measurement or observation | `2026-09-01` |
| `time_start` | time | Start time where relevant | `07:30` |
| `time_end` | time | End time where relevant | `10:15` |
| `observer_id` | text | Field observer or team code | `TEAM-A` |
| `source_id` | text | Document, interview, photo, facility log, or direct measurement reference | `SRC-004` |
| `status` | category | `observed`, `reported`, `estimated`, or `unknown` | `observed` |
| `confidence` | category | `high`, `medium`, or `low` | `medium` |
| `notes` | text | Context, assumptions, anomalies, or limitations | `Rain during final 20 minutes` |

## Material-flow fields

| Field | Type | Description |
|---|---|---|
| `origin_id` | text | Generator, route, facility, or hotspot where flow begins |
| `destination_id` | text | Facility, buyer, disposal point, waterway, or other endpoint |
| `origin_type` | category | `household`, `commercial`, `institutional`, `market`, `public_space`, `route`, `facility`, `hotspot`, `other` |
| `destination_type` | category | `reuse`, `recycler`, `aggregator`, `compost`, `transfer`, `landfill`, `open_dump`, `burning`, `waterway`, `unknown`, `other` |
| `material` | category | `food_organic`, `other_organic`, `paper_cardboard`, `plastic`, `glass`, `metal`, `textile`, `sanitary`, `inert_fines`, `other_unknown` |
| `mass_value` | number | Quantity moved or accumulated |
| `mass_unit` | category | `kg`, `tonne`, `count`, `m3`, or `unknown` |
| `mass_basis` | category | `weighed`, `count_converted`, `facility_record`, `survey`, `visual_estimate`, `modelled`, `unknown` |
| `coverage_period` | text | Period represented by the number | `single load`, `one day`, `weekly average`, `monthly total` |
| `geographic_scope` | text | Boundary represented by the record | `Route R-03` |

## Location fields

| Field | Type | Description |
|---|---|---|
| `location_id` | text | Stable location identifier |
| `latitude` | decimal | WGS84 latitude where safe and appropriate |
| `longitude` | decimal | WGS84 longitude where safe and appropriate |
| `location_precision` | category | `exact`, `facility`, `street_segment`, `grid_250m`, `grid_1km`, `unknown` |
| `administrative_area` | text | Local authority, DS division, district, or province |
| `land_use` | category | `residential`, `commercial`, `institutional`, `industrial`, `market`, `agricultural`, `wetland`, `road`, `other` |

## Hotspot fields

| Field | Type | Description |
|---|---|---|
| `hotspot_type` | category | `illegal_dump`, `roadside_pile`, `open_burning`, `drain_entry`, `waterway_litter`, `wetland_litter`, `overflow`, `other` |
| `repeat_visit_count` | integer | Number of visits confirming persistence |
| `estimated_extent` | text | Approximate area, length, volume, or visual class |
| `nearby_receptor` | category | `households`, `school`, `health_facility`, `waterway`, `wetland`, `farm`, `workplace`, `none_known`, `other` |
| `risk_observed` | text | Smoke, sharp objects, animals, flooding, odor, exposure, or other visible risk |

## Data-quality rules

A flow cannot be marked `high` confidence unless its source, date, boundary, unit, and measurement basis are present. A reported facility total must identify the reporting organization and reporting period. Estimates must include the assumption or conversion factor used. Unknown destinations must remain unknown until validated. Personal names, phone numbers, household-level coordinates, and worker-sensitive information must be kept in a restricted table and must not be published in the public atlas.

## Field-event checklist

Before each event, record team, permissions, route or site, weather, equipment, and safety conditions. During the event, record every load or sample using the same categories and photograph only with permission. After the event, reconcile totals, flag anomalies, upload source evidence, and write a short field note while observations are still fresh.
