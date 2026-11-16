# Western Province Open Dumping and Hidden-Disposal Audit

**Review date:** 22 August 2026. **Scope:** Western Province, Sri Lanka. **Purpose:** Test whether formal labels such as *disposal site*, *controlled dumpsite*, *waste park*, *compost facility*, *transfer station*, *rehabilitation*, or *waste-to-energy project* conceal open dumping, ground unloading, temporary disposal, uncontrolled leakage, or unresolved material conditions.

## Core finding

Yes: the available evidence shows that **formal facility labels and material disposal conditions are not interchangeable**. Western Province has real facilities, projects, and planning institutions, but the source record also documents open dumps, temporary diversion, ground handling at transfer stations, non-sanitary disposal, land scarcity, contamination, odour, leachate, and sites whose current status cannot be verified.[1] [2] [3] [4]

This does not justify saying that every facility is an illegal dump. It justifies a stricter audit rule: every named facility must be checked across at least four separate dimensions—**label, physical practice, legal/permit status, and current evidence**.

## The four-part classification rule

| Dimension | Question | Example of an unsafe shortcut |
|---|---|---|
| Formal label | What does the document call the place? | Treating “landfill” as proof of sanitary design |
| Material practice | What happens to waste physically? | Ignoring ground unloading or mixed disposal |
| Legal/administrative status | Is it licensed, approved, inspected, or ordered closed? | Treating a project or licence as compliance |
| Current evidence | When was the last independent observation or measurement? | Treating a 2018 or 2022 record as current in 2026 |

The register `ANAVARATHA_WESTERN_HIDDEN_DUMPING_REGISTER.csv` stores these distinctions explicitly. It does not mark a site “closed” merely because a source is old, and it does not mark a site “illegal” based on an unverified allegation.

## Verified open-dumping and concealed-disposal mechanisms

### Open dumps remain part of the documented baseline

The World Bank/Government of Sri Lanka Emergency Solid Waste Management Project framework states that open dumping was the most common disposal measure in Sri Lanka and reports approximately 250 operational open-dump sites nationally, including 25 in Western Province, during the project period.[1] This is historical project-period evidence, not a current 2026 count. It is nevertheless important because it establishes that “facility” records in Western Province must be interpreted against a documented open-dumping baseline.

### Temporary disposal can be hidden beside a formal treatment facility

After the Meethotamulla collapse, the same World Bank framework records that Colombo’s non-biodegradable waste was allowed to be dumped on land adjacent to the SLLRDC compost-plant site as a temporary measure, while biodegradable waste was diverted to the Kerawalapitiya Waste Park compost plant. The framework acknowledged the environmental consequences of this emergency decision for sensitive wetlands.[1]

This is a central Anavaratha mechanism: **the name of the receiving institution or nearby facility does not describe the material condition of the adjacent temporary disposal area**. A GIS point for “compost plant” could therefore miss the temporary dump beside it unless the project-period emergency pathway is separately mapped.

### “Controlled dumpsite” and “non-sanitary landfill” conflict at Karadiyana

The 2018 World Bank framework describes Karadiyana as a 500 t/day controlled dumpsite operated by the Western Province Waste Management Authority.[1] The WMA master plan later describes refurbishment of Karadiyana Site A to rehabilitate the biodegradable-waste dump yard, reduce odour and leachate, improve sieving, and strengthen staff management.[2] A 2024 Japanese Embassy report confirms that trommels and tractors were handed over for a Karadiyana pilot project.[3]

Against this, a 2026 technical proposal describes Karadiyana as a non-sanitary landfill/open dumpsite with mixed waste, no segregation, no leachate-treatment facility, surface- and groundwater-pollution concerns, and operation beyond designed capacity.[4] This proposal is not an official CEA compliance determination, so it cannot settle the dispute by itself. It does, however, create a high-priority **conflicted-status record**. The proper response is not to choose one label; it is to request current permits, inspection reports, measured intake, leachate data, site plans, and post-handover evidence.

### Transfer stations can be disposal points in practice

The WMA master plan reports that some urban transfer stations lacked proper facilities and that waste was dumped directly on the ground before being loaded into larger dump trucks with heavy machinery.[2] This means “transfer station” does not automatically mean enclosed, paved, contained, or environmentally controlled transfer. The material pathway must be coded as an **open-ground transfer interface** unless current site evidence shows otherwise.

### Rehabilitation is not closure

The Ministry of Environment/CCET 2021 guidelines define dumpsite rehabilitation broadly. It can include partial work aimed at reducing leachate contamination, uncontrolled gas emissions, waste burning, instability, and socioeconomic impacts.[5] The guidelines identify Moon Plains and Galapitayaya/Kataragama as rehabilitated-dumpsite case studies, but rehabilitation can be partial and does not itself prove permanent closure, sanitary operation, or the absence of residual pollution.

The same distinction applies to Karadiyana’s planned refurbishment and to any future dump-site closure programme. Anavaratha therefore separates `rehabilitation_or_upgrade`, `closed`, `post-closure monitoring`, and `current status unknown`.

### Formal composting can still produce disposal burdens

The WMA plan lists 28 composting facilities in Western Province but simultaneously reports contamination, insufficient maturation time, inadequate heap turning, limited space, sewage, and odour. It also states that approximately 70% of total waste disposed was directly landfilled and the remaining 30% was residue from composting and recycling facilities in its planning diagnosis.[2] A compost facility may therefore divert some material while still generating residuals that require disposal. Mapping only the compost facility hides the downstream residual pathway.

## Western Province hidden-dumping register

| Register record | Formal label | Material-reality evidence | Status used in audit |
|---|---|---|---|
| Karadiyana facility | Controlled dumpsite; non-sanitary landfill/open dumpsite | Conflicting accounts; mixed-waste, leachate, and beyond-capacity concerns in a 2026 technical proposal; refurbishment and equipment interventions documented | **Conflicted status** |
| Karadiyana Site A | Compost plant; dump yard; rehabilitation | Refurbishment intended to reduce odour/leachate and improve treatment; current persistence not shown | **Historical rehabilitation/upgrade** |
| Kerawalapitiya adjacent temporary area | Waste park; compost plant; emergency diversion | Non-biodegradable waste dumped adjacent to SLLRDC compost site after Meethotamulla; wetland damage acknowledged | **Historical temporary disposal** |
| Meethotamulla/Pothuvil Kumbura | Garbage dump; final-disposal site | Supreme Court found unlawful dumping from 2009–2017 and institutional failure; collapse followed | **Historical cessation after collapse; current status unresolved in this audit** |
| Dompe | CEA sanitary landfill; composting facility | Formal role identified in project/plan documents | **Formal label; current status unknown** |
| 22 LA disposal sites | Local-authority disposal sites | WMA plan states 22 LAs operated their own sites in 2022; names and present conditions are not exposed in the summary | **Province-wide count without named inventory** |
| Urban transfer stations | Transfer station | Some sites used open-ground unloading and heavy-machinery reloading | **Historical open-ground transfer condition** |
| 28 compost facilities | Composting facilities | Formal treatment label coexists with contamination, odour, sewage, space, and process-control problems | **Treatment label with operational risk** |

## What is genuinely hidden by current public data

The largest hidden component is not necessarily a secret site. It is the **unobserved transition between named facilities**: household or commercial source → collection vehicle → transfer station → treatment facility → reject/residual stock → final disposal or leakage. Public plans often expose the facility names but not the full daily pathway.

The following fields are therefore necessary for GIS and capacity analysis:

| Field | Why it matters |
|---|---|
| Exact receiving polygon, not only a facility point | A point can hide adjacent temporary dumping or multiple disposal areas |
| Material accepted and rejected | A compost label does not show what happens to mixed or contaminated feedstock |
| Daily intake and weighbridge method | Design capacity does not show actual disposal |
| Ground-unloading and containment status | Transfer facilities may function as open disposal points |
| Residual destination | Treatment can move rather than remove the burden |
| Licence, inspection, and enforcement stage | A plan or project is not legal-operational proof |
| Last observed operating date | Historical records must not be displayed as current |
| Closure and post-closure monitoring | Rehabilitation is not closure, and closure is not risk elimination |
| Complaint, fire, odour, leachate, and spill records | These reveal material conditions that formal labels omit |
| Seasonal access and overflow pathway | Rain, road failure, and capacity peaks can create temporary dumping |

## Final conclusion

The question’s suspicion is supported, but it must be expressed carefully. **Yes, open dumping and hidden disposal can be concealed under formal names in the public record.** In Western Province, this is demonstrated by historical open-dump counts, emergency dumping beside a compost facility, ground unloading at transfer stations, conflicting descriptions of Karadiyana, and the distinction between rehabilitation and closure.[1] [2] [4] [5]

The evidence does not prove that every current facility operates this way. It proves that a simple GIS inventory of named facilities would systematically under-detect hidden disposal unless it maps material pathways, temporary areas, residuals, status transitions, and evidence dates.

The next controlled descent should therefore prioritize a **Western Province disposal-status audit** of Karadiyana, Kerawalapitiya adjacent areas, Dompe, the 22 LA disposal sites, the 28 compost facilities, and urban transfer stations. It should request current polygons, licences, inspection records, weighbridge logs, maintenance records, residual destinations, complaints, fires, leachate monitoring, and closure/rehabilitation status before any claim about present illegality or contamination.

## References

[1] World Bank and Government of Sri Lanka. *Sri Lanka Emergency Solid Waste Management Project Environmental Management Framework*. 2018. https://documents1.worldbank.org/curated/en/445181516940824984/txt/SFG4010-EA-P163977-PUBLIC-Disclosed-1-25-2018.txt

[2] Western Province Waste Management Authority. *Western Province Solid Waste Management Master Plan in Sri Lanka*. Public download gateway: https://wma.wp.gov.lk/notice/8. Local archive: `WMA_Western_Province_Master_Plan_public_download.pdf`.

[3] Embassy of Japan in Sri Lanka. *Handing-over Ceremony for the JICA Pilot Project Conducted Under Technical Cooperation Project, Project for Formulation of Western Province Solid Waste Management Master Plan*. 4 July 2024. https://www.lk.emb-japan.go.jp/itpr_en/11_000001_00467.html

[4] GAP HQ / Indraji Madhushan Nayaka Bandara. *Comprehensive Remediation and Sustainable Waste Management Strategies for Karadiyana Dumpsite in Sri Lanka*. Accessed 22 August 2026. https://gaphq.lk/comprehensive-remediation-and-sustainable-waste-management-strategies-for-karadiyana-dumpsite-in-sri-lanka/

[5] Karunarathana, A., Rajapaksha, T., Singh, R. K., Premakumara, D. J., & Onogawa, K. *Guidelines for Safe Closure and Rehabilitation of Municipal Solid Waste Dumpsites in Sri Lanka*. Ministry of Environment, Sri Lanka / IGES CCET, February 2021. https://ccet.jp/publications/guidelines-safe-closure-and-rehabilitation-municipal-solid-waste-dumpsites-sri-lanka
