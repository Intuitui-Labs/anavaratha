# Western Province Full Facility-Capacity Reality Review

**Review date:** 22 August 2026. **Scope:** Western Province, Sri Lanka. **Purpose:** Analyze the Western-related evidence fully, rather than treating the existence of a database or master plan as proof of realized capacity.

## Executive finding

Western Province has the most developed publicly documented waste-management planning and data architecture located in this review. The evidence includes a 2019–2023 JICA master-planning project, a database reportedly introduced to 49 local authorities, a publicly downloadable WMA master plan, a publicly downloadable Karadiyana waste-to-energy project document, a 2024 equipment handover, and a 2025 report of a pilot real-time monthly database initiative.[1] [2] [3] [4]

The evidence also demonstrates why **formal capacity is not the same as facility-capacity reality**. The WMA plan records 28 composting facilities, 22 local authorities operating their own disposal sites, and 10 outsourcing disposal because of land constraints. It also records old and frequently breaking collection vehicles, poor maintenance, high absenteeism, inadequate resources, transfer stations where waste is dumped on the ground before reloading, contamination, insufficient maturation, odour, sewage, and incomplete local-authority data management.[5]

The newest measured station-level evidence located is the 2025 peer-reviewed study using January–December 2022 data from 22 Western Province compost stations. Across those 22 stations, reported design capacity was 2,775 t/month, running capacity was 2,391.3 t/month, and actual compost production was only 157 t/month. Thus, aggregate running capacity was 86.17% of design capacity, but actual production was 6.57% of running capacity. Seventeen of 22 stations produced below 10% of their reported running capacity. These are not province-wide totals and should not be added to the WMA’s province-wide plan figures.[6]

## Evidence architecture and status

| Evidence component | Period | Coverage | Evidence status | What it can support |
|---|---:|---|---|---|
| JICA Western Province master-planning project | 2019–2023 | 49 local authorities | Completed planning/data-system project | Existence of regional planning and database architecture |
| WMA Western Province Master Plan | 2020 baseline; 2022–2042 plan series | Western Province | Public plan and scenario document | Formal flow model, facility counts, targets, costs, planned capacity |
| JICA/Sato database account | Published 2024; database project 2019–2023 | Western Province | Secondary/peer-reviewed description | Reported database modules and data fields |
| SACEP/PLEASE database page | 16 April 2025 | Western Province, intended replication | Public programme description | Reported pilot real-time monthly database initiative |
| Japanese Embassy handover | 4 July 2024 | Karadiyana | Official event record | Equipment handover and pilot intervention |
| Manipura et al. operational study | Published 2025; data January–December 2022 | 22 compost stations | Peer-reviewed observed/reported station dataset | Station-level design, running, production, sales, labour, and constraints |
| WMA public notice | Accessed 22 August 2026 | Western Province | Public source gateway | Plan and project downloads |

The database architecture is important but must be interpreted precisely. Sato et al. state that the database was introduced to 49 Western Province local authorities and collected amounts of collection, intermediate treatment, transfer, final disposal, and recycling at daily, weekly, and monthly intervals. The 2025 SACEP/PLEASE page describes a pilot real-time monthly database and says it could be replicated across the country.[1] [2] However, this review did not locate a public raw export, data dictionary, completeness report, validation protocol, user/audit log, or current facility-level dashboard. The public description therefore verifies an architecture and reported implementation, not a publicly auditable capacity dataset.

## What the WMA plan says about the existing system

The plan’s own baseline diagnosis is unusually useful because it combines a formal flow architecture with explicit operational criticism. It reports approximately 3,730–3,732 t/day of Western Province MSW generation in its 2020/2022 context. For the 2022 base-year destination shares, the plan reports 16% of collected waste to composting, 6% to recycling-related facilities, 38% to thermal-recovery facilities, and 40% to disposal sites. It separately reports that, in its 2020 current-condition section, 46% of collected waste went to composting, 6% to recycling-related facilities, and 48% to disposal sites.[5]

These percentages are both internally coherent within their respective statements, but they are not identical. The plan does not provide enough reconciliation in the extracted passages to treat them as one time series. Anavaratha therefore codes the 46/6/48 values as a 2020 current-condition figure and the 16/6/38/40 values as a 2022 base-year figure. The accompanying consistency audit is `ANAVARATHA_WESTERN_SOURCE_CONSISTENCY_AUDIT.csv`.

The plan lists 28 composting facilities: 23 managed by local authorities; three managed by WMA—Karadiyana, Dikkowita, and Kalutara; one at Dompe managed by CEA; and Kerawalapitiya managed by SLLRDC. It states that 22 local authorities operated their own disposal sites and 10 outsourced disposal to private actors because they could not secure land.[5] These counts are a valuable province-wide facility denominator, but the plan does not by itself provide current 2026 operating status for each facility.

## The formal 2020 flow model

The WMA plan’s 2020 flow diagram reports 3,732 t/day of MSW generation, 1,785 t/day from households, 1,900 t/day of waste discharge/self-disposal, 1,732 t/day collected, 289 t/day transferred, 791 t/day treated in compost facilities, 100 t/day treated in material-recycling facilities, 509 t/day of compost/material flow, 347 t/day of residues, and 740 t/day total recyclable material. It also reports 30 t/day of on-site recycling and 168 t/day of informal recycling.[5]

These figures should not be treated as a fully weighed mass balance. The plan explicitly states that some fields use previous survey results, weighbridge data, vehicle-operation information, or local-authority waste-management data. The appropriate interpretation is a **formal mixed-evidence planning flow model**. Its value is that it makes the system boundary visible; its limitation is that its measurement and estimation bases are not uniform.

## Master-plan capacity trajectory: plan architecture, not realized outcome

The WMA Table 4-21 series reports collected biodegradable waste increasing from 896 t/day in 2022 to 2,226 t/day in 2042. It shows total composting capacity rising from 324 t/day in 2022 to 1,330 t/day in 2042, while direct transport to final disposal is projected at 334 t/day in 2022, zero in many years from 2028 onward, and 26 t/day in 2042. The plan also projects thermal-recovery treatment in the table from zero in 2022 to 400 t/day in later years.[5]

A mechanical calculation produces a 2022 total planned-compost-capacity-to-collected-biodegradable-waste ratio of 36.16%, rising to 61.95% in the 2026 plan year and 59.75% in 2042. This is **capacity coverage under the plan**, not utilization. The plan’s listed treatment totals also exceed collected biodegradable waste in later years because the table combines categories and scenario assumptions whose boundaries are not equivalent to one simple input-output identity. No realized-capacity conclusion should be drawn from those ratios.

The saved file `ANAVARATHA_WMA_WESTERN_CAPACITY_SERIES.csv` contains every year and derived field. `ANAVARATHA_WMA_WESTERN_CAPACITY_SERIES.png` visualizes the series and clearly labels it as a master-plan trajectory.

## 22-station operational reality

The 2025 study is the strongest recent operational dataset located, but its boundary is 22 compost stations, not all Western Province waste facilities and not necessarily all 28 facilities listed in the WMA plan.[6]

| Indicator | 22-station result | Interpretation |
|---|---:|---|
| Stations | 22 | Surveyed station subset |
| Reported design capacity | 2,775 t/month | Nominal station design field |
| Reported running capacity | 2,391.3 t/month | Reported running field, not independently audited uptime |
| Actual compost production | 157 t/month | Reported production field |
| Compost sales | 142.4 t/month | Sales may include stock carried from earlier periods |
| Employees | 254 | Reported staffing count, not attendance or effective labour hours |
| Running/design | 86.17% aggregate | Nominal running-to-design relation |
| Production/running | 6.57% aggregate | Strongest operational bottleneck signal in this dataset |
| Production below 10% of running | 17 of 22 stations | Broad station-level low-output pattern |
| Sales/production | 90.70% aggregate | Requires stock reconciliation before being interpreted as current conversion |

The station distribution is also important. Mean station running/design was 89.77%, median 80.91%, and the range was 33.33%–185.00%. Seven stations reported running capacity above design capacity, which is a source-data or boundary-quality flag rather than evidence of superior performance. Mean production/running was 7.19%, median 7.29%, and the range was 0.13%–18.53%. Four stations reported sales above current-period production, demonstrating why sales cannot be treated as production without opening-stock and closing-stock data.

The study and supplementary questionnaire identify constraints around weighing, SOPs, operating days, segregation, contamination, space, machinery, leachate, process monitoring, cycle time, quality testing, finance, training, occupational safety, marketing, and customer demand.[6] These fields make the study highly valuable for the next national data request.

## Compatibility audit: what can and cannot be combined

| Dataset pair | Direct combination allowed? | Reason |
|---|---|---|
| 22 stations and WMA 2022 Table 4-21 | **No** | 22 surveyed stations versus province-wide categories; monthly versus daily units; compost subset versus LA, waste-park, and TRF categories |
| 22 stations and WMA 28-facility count | **No, not yet** | Facility identities and one-to-one correspondence are not reconciled |
| WMA 2020 and WMA 2022 percentages | **No** | Internal percentage discrepancy and different period labels |
| WMA plan targets and current operation | **No** | Requires commissioning, uptime, measured throughput, maintenance, and validation evidence |
| JICA database description and actual capacity | **No** | Architecture description does not provide public validated records |
| 2024 equipment handover and current performance | **No** | Handover verifies inputs, not persistence, uptime, or output |

The derived `ANAVARATHA_WESTERN_DATA_COMPATIBILITY_MATRIX.csv` preserves these decisions. This is not pedantry: adding incompatible values would create a false provincial capacity total and conceal the difference between plans, facilities, flows, and outcomes.

## Paper-versus-reality chain

Western Province now provides a useful chain for Anavaratha’s central question:

> policy and master plan → database architecture → facility and equipment inputs → reported flows → observed operation → product quality and market → residual burden → persistence.

The evidence is strong at the first four links. The plan, database architecture, equipment handover, and facility counts are documented. The evidence becomes weaker at the operational links. The 22-station dataset shows a large production gap despite reported running capacity, while the plan itself reports contamination, missing process controls, land scarcity, vehicle breakdown, absenteeism, transfer-station ground handling, and insufficient local-authority data management.[5] [6]

The public record is weakest for the final links: current facility status, downtime, maintenance, quality, residual destination, licence and inspection history, environmental monitoring, complaints, and persistence after handover or project completion.

## Final answer to the question of whether Western data were properly analyzed

The answer is now **yes for the publicly obtainable evidence, with explicit boundaries**. We have analyzed:

1. The JICA database architecture and its 49-local-authority Western Province scope.
2. The 2025 report of a pilot real-time monthly database.
3. The 2024 official equipment handover at Karadiyana.
4. The WMA public master-plan and Karadiyana project downloads.
5. The WMA plan’s 2020 flow model and 2022–2042 capacity trajectory.
6. The WMA’s province-wide facility counts and disposal arrangements.
7. The full available 22-station 2022 operational dataset.
8. Station-level distributions, production gaps, sales-stock warnings, and design-boundary anomalies.
9. Source-period and geographic compatibility.
10. The remaining gaps in public accessibility, validation, and current operation.

What we have **not** done—and cannot honestly claim to have done—is analyze the raw 49-LA database records, because the public source descriptions do not expose those records. That absence is now explicitly documented as an access and verification gap.

## Revised conclusion

The correct conclusion is not that Western Province lacks capacity data. It has more capacity-related evidence than the rest of Sri Lanka located in this review. The correct conclusion is:

> **Western Province has a comparatively advanced planning and waste-data architecture, with a 49-local-authority database initiative, formal flow modelling, documented facility counts, public project materials, and recent equipment interventions. Yet the publicly obtainable evidence still does not demonstrate a fully auditable facility-capacity reality system: current facility status, complete raw database records, validated throughput, downtime, maintenance, quality, residual pathways, and post-project persistence remain incompletely visible. The 22-station operational dataset shows why this distinction matters: reported running capacity can coexist with very low realized compost production.**

This is a qualified conclusion, not a blanket negative claim. It recognizes genuine institutional capacity while keeping the material-reality question open.

## References

[1] Sato, N., Kondo, T., Cherki, M. H., Kalyanasundaram, M., & Kawamoto, K. (2024). *Current Condition of Solid Waste Management and JICA Support in Sri Lanka*. Global Environmental Research, 28, 53–61. https://airies.wikiplus.net/attach.php/6a6f75726e616c5f32382d31656e67/save/0/0/28-1_08.pdf

[2] South Asia Co-operative Environment Programme / PLEASE Project. *Solid Waste Management Database*. 16 April 2025. https://please-project.org/sar-initiative/solid-waste-management-database-2/

[3] Embassy of Japan in Sri Lanka. *Handing-over Ceremony for the JICA Pilot Project Conducted Under Technical Cooperation Project, Project for Formulation of Western Province Solid Waste Management Master Plan*. 4 July 2024. https://www.lk.emb-japan.go.jp/itpr_en/11_000001_00467.html

[4] Western Province Waste Management Authority. *Solid Waste Management Plan* notice with Western Province Master Plan and Karadiyana Waste-to-Energy project downloads. https://wma.wp.gov.lk/notice/8

[5] Western Province Waste Management Authority. *Western Province Solid Waste Management Master Plan in Sri Lanka*. Public download via [4]. Local archive: `WMA_Western_Province_Master_Plan_public_download.pdf`; extracted text references include lines 2704–2805, 7322–7400.

[6] Manipura, A., Drechsel, P., Jayawardhana, H. M. L. C., Shanmugapriya, R., Mannapperuma, N. R., & Jayatilleke, H. S. (2025). *Improved performance indicators and institutional setup for more viable compost production from municipal solid waste in Sri Lanka*. Waste Management Bulletin, 3(3), 100217. https://doi.org/10.1016/j.wmb.2025.100217

[7] Japan International Cooperation Agency. *Project for Formulation of Western Province Solid Waste Management Master Plan*. Completion notice, 19 May 2023. https://www.jica.go.jp/english/overseas/srilanka/information/press/2023/20230519.html

[8] Central Environmental Authority. *Recommendations on the Strategic Environmental Assessment and proposed master plan for Solid Waste Management for Western Province*. https://www.cea.lk/web/images/pdf/2024/SEA/Recommendations_of_the_Central_Environmental_Authority.pdf
