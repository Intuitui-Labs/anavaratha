# Anavaratha

## Verification queue and evidence ledger

**Sri Lanka regenerative-cultivation dimension — Working queue, Version 0.1**

## 1. Purpose

This queue converts the prototype’s research gaps into bounded desk tasks. It prioritises existing sources, records the expected output, and defines the condition for stopping or escalating a task.

## 2. Prioritised queue

| Queue ID | Task | Source route | Expected output | Priority | Stop or escalate when |
|---|---|---|---|---|---|
| **VQ-01** | Extract full medicinal-plant checklist fields | 2025 Ceylon Journal PDF and Appendix 1 [1] | Validated table fields for name, family, synonyms, Sinhala name, 2012 status, 2020 status, and page | P1 | Table alignment becomes unreliable; then batch-extract and spot-check visually |
| **VQ-02** | Cross-check medicinal taxonomy | National Herbarium and checklist [1] [2] | Accepted-name, synonym, and identity crosswalk | P1 | A record requires specimen or specialist confirmation |
| **VQ-03** | Clarify Osu Uyana | Ganewatta official garden, community study, and local-language sources [3] [4] | Terminology, sites, species, institutions, knowledge holders, and governance note | P1 | Source remains secondary or knowledge requires consent; record as unresolved lead |
| **VQ-04** | Locate current forest data pathways | Forest Department GIS, Forest Inventory, biodiversity, and watershed divisions [5] | Catalogue of available layers, contacts, dates, scale, and access conditions | P1 | Underlying data require a formal request |
| **VQ-05** | Verify protected-area and corridor resources | DWC protected-area page, permits, current maps [6] | Habitat, corridor, permit, and management crosswalk | P1 | Boundary or species-use evidence is unavailable |
| **VQ-06** | Inspect wetland resources | National Wetland Directory, CEA gateway, National Wetland Database [7] [8] | Wetland-source inventory with date, definition, format, spatial precision, and access | P1 | Directory is historical or database is inaccessible |
| **VQ-07** | Build seasonal calendar | Sri Lankan phenology, pollination, fruiting, seed-dispersal, and germination studies [9] | Relationship calendar by species, habitat, rainfall, flowering, fruiting, dispersal, and care | P2 | Evidence is too site-specific to generalise |
| **VQ-08** | Select seed-disperser anchor | Sri Lankan rainforest-restoration and dispersal studies [10] | One verified plant–animal pair with habitat and recruitment relation | P1 | Existing literature does not establish successful recruitment |
| **VQ-09** | Extend soil-life records | AMF, root, soil, and agroecological studies [11] | Comparable soil-life relationship fields and transferability limits | P2 | Experimental results cannot be transferred to target habitat |
| **VQ-10** | Build multilingual name crosswalk | Sinhala, Tamil, English, scientific names across sources | Attributed multilingual identity table | P1 | Names conflict or knowledge requires local verification |
| **VQ-11** | Build stewardship and access register | Forest Department, DWC, CEA, Herbarium, universities, communities | Responsibility, authority, permit, consent, and access map | P1 | Authority or knowledge ownership is unclear |
| **VQ-12** | Track existing restoration outcomes | UN, IUCN, IWMI, university, and community project sources | Activities, outputs, outcomes, maintenance, failure, and unintended-effects table | P2 | Only promotional/project-intent material is available |

## 3. Evidence ledger template

| Ledger ID | Queue ID | Source | Specific claim or field | Place | Time | Method | Status | Confidence | Limitation | Cross-link | Next action |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **EL-001** | VQ-01 | Ceylon Journal checklist | Appendix 1 fields include updated family, earlier Flora family, updated scientific name, earlier scientific name, homotypic synonyms, Sinhala name, 2012 status, and 2020 status | Sri Lanka | 2025 article; statuses 2012/2020 | Checklist compilation and taxonomic review | Extracted schema | High | Row alignment requires visual validation | Medicinal plant ↔ National Herbarium | Extract in page batches |
| **EL-002** | VQ-02 | National Herbarium | Institutional role includes plant authentication, taxonomic investigation, flora documentation, and threatened-plant surveys | Sri Lanka | Current page; record dates vary | Institutional service description | Inspected | High for role | Catalogue access not fully exposed | Plant identity ↔ medicinal checklist | Confirm access pathway |
| **EL-003** | VQ-03 | Ganewatta medicinal garden | Official garden has a large medicinal collection, native/endemic plants, ex situ conservation, nurseries, seed preservation, herbarium, and educational/research functions | Intermediate Zone; near Kurunegala | Current institutional page; dates not fully specified | Institutional garden description | Inspected | High for page content | Page does not define “Osu Uyana” | Medicinal garden ↔ Osu Uyana lead | Verify terminology and governance |
| **EL-004** | VQ-04 | Forest Department | Technical divisions include GIS and Forest Inventory, Biodiversity and Watershed Management, Social Forestry and Extension, and Research | National and administrative regions | Current institutional page | Institutional description | Inspected | High for stated structure | Underlying datasets not exposed | Forest ↔ tree ↔ watershed ↔ stewardship | Identify catalogues and contacts |
| **EL-005** | VQ-05 | DWC | Protected areas are described as species refuges, ecosystem-service areas, cultural/historical areas, and reference sites; corridors address fragmentation and movement | National protected-area system | Current page; counts and boundaries require checking | Institutional description | Inspected | High for stated logic | Does not prove local habitat integrity or movement | Species ↔ habitat ↔ corridor | Obtain current spatial layers |
| **EL-006** | VQ-06 | National Wetland Directory | Directory was created in response to national wetland-conservation information needs and policy development | Sri Lanka wetlands | Policy/report history | National report gateway | Inspected | High for existence and context | Currency and spatial detail require assessment | Wetland ↔ CEA ↔ local study | Inspect full directory |
| **EL-007** | VQ-07 | Seed Science Research | In a study of 42 lowland rainforest tree species, dormancy class related to forest stratum and dispersal time; non-dormant seeds were dispersed during the rainy season | Sri Lankan lowland rainforest | Published 2022; study period/source details in article | Seed biology study | Extracted | High within study scope | Cannot generalise to all habitats/species | Tree ↔ seed ↔ season ↔ disperser | Add species-level calendar fields |
| **EL-008** | VQ-08 | Rainforest restoration literature | Animal-mediated dispersal is a relevant restoration pathway and should be connected to recruitment rather than only seed removal | Sri Lankan rainforest restoration context | Historical and study-specific | Review/restoration research | Contextualised | Moderate until species pair verified | Specific pair and successful recruitment remain open | Fruiting plant ↔ animal ↔ forest recovery | Select and verify one pair |

## 4. Priority interpretation

The highest-value tasks are those that improve identity, responsibility, and relationship quality across many records. The medicinal checklist and National Herbarium crosswalk can improve a large number of plant records. Forest Department and DWC pathways can clarify where authority and habitat responsibilities lie. The wetland pathway can prevent the duplication of existing national catalogues. The seasonal and seed-dispersal tasks can turn static records into living relationships.

## 5. Required stopping discipline

A queue item should not remain open merely because more information might exist. It should stop when the relevant source has been inspected, the available claim extracted, the limitation recorded, and the next action identified. It should escalate when the missing information materially affects identity, safety, ethics, ecological fit, or field responsibility.

> **A well-managed gap is more valuable than an unsupported completion.**

## References

[1]: https://cjs.sljol.info/articles/10.4038/cjs.v53i4.8264 “Preserving Sri Lanka’s indigenous healing heritage: An updated checklist of medicinal plants and conservation priorities,” *Ceylon Journal of Science*.

[2]: https://botanicgardens.gov.lk/service/national-herbarium/ “National Herbarium,” Department of National Botanic Gardens, Sri Lanka.

[3]: https://botanicgardens.gov.lk/service/medicinal-plant-gardens-ganewatte/ “Medicinal Plant Garden,” Department of National Botanic Gardens, Sri Lanka.

[4]: https://jnsfsl.sljol.info/articles/3029/files/submission/proof/3029-1-10540-1-10-20110510.pdf H. M. Bandaratillake, “Community participation in the management in the Kanneliya-Dediyagala-Nakiyadeniya proposed biosphere reserve,” *Journal of the National Science Foundation of Sri Lanka*.

[5]: https://www.env.gov.lk/web/index.php/en/department-of-forest-conservation “Department of Forest Conservation,” Ministry of Environment, Sri Lanka.

[6]: https://www.dwc.gov.lk/?page_id=72 “Protected Areas,” Department of Wildlife Conservation, Sri Lanka.

[7]: https://lk.chm-cbd.net/documents/national-wetland-directory-sri-lanka “National Wetland Directory of Sri Lanka,” Sri Lanka Biodiversity/CBD.

[8]: https://www.cea.lk/web/?option=com_content&view=article&layout=edit&id=1564 “Special projects / programs,” Central Environment Authority, Sri Lanka.

[9]: https://www.cambridge.org/core/journals/seed-science-research/article/abs/seed-dormancy-and-germination-behaviour-of-tropical-rainforest-tree-species-from-sri-lanka/BCB15F1CB18A1B6A6B795E41C6ED1C9 B. R. Chandima P. Samarasinghe et al., “Seed dormancy and germination behaviour of tropical rainforest tree species from Sri Lanka,” *Seed Science Research*.

[10]: https://www.sciencedirect.com/science/article/abs/pii/S0378112701005126 M. S. Ashton et al., “Restoration pathways for rain forest in southwest Sri Lanka,” *Forest Ecology and Management*.

[11]: https://www.mdpi.com/2071-1050/14/24/16537 “Assessment of Community Dynamics of Arbuscular Mycorrhizal Fungi in the Rice (*Oryza sativa* L.) Rhizosphere and Potential Application as Biofertilizer,” *Sustainability*.
