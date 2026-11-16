# Western Province Satellite and Remote-Sensing Screening Protocol

**Purpose:** Screen verified and historical waste-site leads for visible spatial change before field validation. This protocol is not a method for declaring illegality, contamination, or current operation from imagery alone.

## Screening targets

Priority targets are Karadiyana and Site A, Kerawalapitiya and adjacent emergency-disposal areas, Dompe, the 21 numbered WMA Figure 2-10 map leads, the 22 local-authority disposal-site count, and any transfer or treatment facility for which current polygons are obtained.

## Required imagery record

Every image observation must preserve provider, product, acquisition date, processing level, spatial resolution, cloud cover, tile/path, coordinate reference system, downloaded filename, and exact polygon or point screened. Images from different dates must not be described as one continuous observation.

## Visible indicators to code

| Indicator | What may be visible | What it cannot prove |
|---|---|---|
| Waste footprint | Expansion of bare or irregular stockpile area | Waste type, quantity, legality, or contamination |
| Burn scar/smoke evidence | Darkened ground or active smoke on image date | Cause, frequency, or illegal burning |
| Leachate-like pond | Dark or discoloured pond near waste area | Chemical composition or hydrological connection |
| Drainage/stream relation | Relative location of waste footprint and water feature | Pollution or causal flow without sampling |
| Road/access change | New tracks, widened roads, wet-season damage | Whether waste vehicles use them or why |
| Facility structures | Roofs, pads, tanks, sorting structures, cells | Operational status or capacity |
| Stockpile change | Increase or reduction in visible material | Throughput without calibrated volume and density |

## Method

First, obtain or digitize a defensible facility or dump polygon. Second, select at least three dated images where cloud and resolution permit. Third, compare the footprint, access, drainage, structures, and stockpiles using identical map extent and coordinate system. Fourth, record only visible changes and uncertainty. Fifth, match the observation against facility logs, permits, inspection records, and reported flows. Sixth, classify the result as `screening_consistent`, `screening_conflict`, `screening_inconclusive`, or `not_screenable`.

## Prohibited inferences

The screening must not infer current illegality, hazardousness, contamination, facility capacity, or causal ecological damage from spectral appearance, proximity, or a single image. An apparent footprint may be soil, construction, agriculture, or legacy waste. A clean image does not prove absence of waste. Cloud, vegetation, resolution, and image-date mismatch must be recorded.

## GIS output fields

`screen_id`, `facility_record_id`, `image_provider`, `image_date`, `resolution_m`, `cloud_or_quality`, `screen_polygon`, `visible_indicator`, `change_direction`, `confidence`, `comparison_image`, `source_url`, `ground_or_document_check`, `status_result`, and `unresolved_question`.

## Current stage

The current WMA map leads do not yet have defensible coordinates or polygons. They must therefore remain map leads and should not be submitted to satellite screening as if they were exact sites. The first actionable satellite screen begins after WMA, CEA, or local-authority records provide current coordinates or after a clearly documented georeferencing exercise produces uncertainty-bounded candidate polygons.
