# Anavaratha Proportional Comparison Framework

## Purpose

The desk review should compare waste systems in a way that respects differences in population, activity, geography, capacity, and time. No synthetic values are inserted here. The formulas define what should be calculated once compatible source data are available.

## Core variables

| Symbol | Meaning |
|---|---|
| `P` | Population or relevant activity denominator |
| `G` | Waste generated during a defined period |
| `C` | Waste collected through the pathway being measured |
| `R` | Waste recovered, reused, recycled, or composted |
| `D` | Waste sent to controlled disposal |
| `U` | Uncontrolled disposal, burning, leakage, or unobserved remainder |
| `K` | Usable system capacity for the relevant function |
| `S` | Accumulated waste stock or remaining capacity stock |
| `T` | Time period represented |
| `A` | Area, route length, drainage catchment, or other spatial denominator |

## Recommended ratios

| Measure | Formula | Interpretation |
|---|---|---|
| Per-capita generation | `G / P / T` | Waste pressure relative to population and time |
| Collection rate | `C / G` | Share of generated waste collected under the stated definitions |
| Recovery rate | `R / G` | Share entering the specified recovery pathways |
| Controlled-disposal rate | `D / G` | Share sent to controlled disposal |
| Uncontrolled share | `U / G` | Residual, uncontrolled, leaked, burned, or unobserved share; define components separately |
| Capacity utilization | `inflow / K` | Pressure on a facility, route, workforce, or system capacity |
| Capacity gap | `demand − K` | Shortfall, only where demand and usable capacity are compatible |
| Service density | `served population / route or vehicle capacity` | Operational burden on collection infrastructure |
| Hotspot density | `hotspots / A` | Spatial concentration, with a meaningful area or network denominator |
| Persistence rate | `repeat-positive observations / total repeat observations` | Whether a condition remains over time |
| Recovery yield | `usable output / input received` | Actual output after contamination and processing losses |

## Denominator discipline

Use a denominator that matches the phenomenon. Household waste should not be normalized only by total population if household count is available. Market waste may be better compared per market day or stall. Tourism waste may require visitor or guest-night measures. Collection service can be compared per served household, route kilometre, or tonne, depending on the operational question.

A denominator must be recorded with its source, date, boundary, and definition. If the denominator is estimated, the uncertainty must be propagated into the interpretation.

## Capacity-adjusted interpretation

A high collection rate does not necessarily imply a healthy system if the rate is achieved by transferring residuals to an uncontrolled destination. A low collection rate may reflect dispersed settlements, long routes, seasonal roads, insufficient vehicles, or weak demand data. Always pair a ratio with the relevant capacity and spatial conditions.

Recommended paired views include:

| Pressure view | Capacity view |
|---|---|
| Waste per person or activity unit | Collection capacity per person or activity unit |
| Waste per square kilometre or route | Service assets per square kilometre or route |
| Facility inflow per day | Usable facility capacity per day |
| Accumulated stock over time | Remaining capacity or remediation capability |
| Recovery input | Recovery output after contamination and losses |

## Time comparison

Use a four-part time frame:

| Time view | Question |
|---|---|
| Snapshot | What was observed at one point? |
| Seasonal | How does the system change between wet/dry, peak/off-peak, or other relevant periods? |
| Intervention cycle | What changed before, during, and after a project or policy? |
| Structural trend | What changed over multiple years as population, income, land use, policy, or infrastructure changed? |

Do not compare a project target with a later observed outcome without recording the difference between target, implementation, and achieved result.

## Spatial comparison

Use both origin and receiving location. For each flow or burden, record where it begins, the pathway, the destination, and the receiving ecological or social context. A local authority may reduce internal visible waste while increasing burdens at a receiving site or neighboring jurisdiction.

Spatial comparisons should consider density, road access, distance to facilities, drainage, land use, proximity to homes or schools, and administrative boundaries. Exact coordinates should be generalized when publication could create safety, privacy, or stigmatization risks.

## Uncertainty rules

If `G`, `C`, `R`, or `D` come from different periods or definitions, do not calculate ratios as if they were compatible. Use ranges, scenarios, or a qualitative comparison. If uncontrolled waste is partly unobserved, do not equate it automatically with illegal dumping. Separate known open dumping, burning, leakage, self-disposal, and unknown remainder.

## Comparison output

The desk review should produce a table for each candidate location with: population/activity denominator; waste-stream scope; reference period; reported generation; collection; recovery; controlled disposal; uncontrolled or unknown share; facility and service capacity; capacity gap; spatial burden; time pattern; evidence quality; and unresolved contradictions. This table becomes the bridge between literature review and future data collection.
