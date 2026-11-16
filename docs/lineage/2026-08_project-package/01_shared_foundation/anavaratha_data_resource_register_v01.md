# Anavaratha

## Data-resource register

**Sri Lanka regenerative-cultivation dimension — Working register, Version 0.1**

This register translates the wider source map into possible data resources for future atlas work. It distinguishes public discovery from confirmed data reuse. No resource should be downloaded, republished, or transformed without checking its current terms.

| Resource ID | Resource | Data or knowledge held | Resolution | Immediate use | Main caution |
|---|---|---|---|---|---|
| **DR-01** | National Herbarium | Authenticated plant identity, flora documentation, taxonomic investigation, threatened-plant surveys, and herbarium knowledge | Plant, specimen, national and survey levels | Verify names, synonyms, threatened plants, and candidate trees | Collection access and specimen use may require contact; verify current procedures |
| **DR-02** | Updated medicinal-plant checklist | Taxonomically verified list, synonyms, conservation status, commonly used species, and practitioner-survey context | Plant and national level | Build the medicinal-plant and Osu Uyana baseline | Cite the 2025 publication; protect traditional knowledge and sensitive locations |
| **DR-03** | Forest Department GIS and forest inventory functions | Forest regions, divisions, ranges, GIS, forest inventory, biodiversity, watershed, silviculture, and research resources | National to forest-range level | Identify responsible units and locate forest and tree data | Public institutional description does not guarantee public dataset access |
| **DR-04** | DWC protected-area network | Protected-area categories, reserves, parks, corridors, sanctuaries, habitats, permits, and conservation responsibilities | National, protected-area, habitat, and corridor levels | Add habitat protection and movement context | Research in protected areas may require permits; sensitive species locations need protection |
| **DR-05** | CEA wetland and information gateways | National Wetland Directory, National Wetland Database, Red List gateway, information centre, publications, and environmental agencies | National, wetland, site, and document levels | Discover wetland and environmental-information sources | Age, format, spatial resolution, and access differ; pollution-specific materials remain outside this workstream |
| **DR-06** | National Wetland Directory | Existing national wetland catalogue and conservation-policy context | National wetland level | Compare existing entries with later local studies and maps | It is not automatically current or spatially complete |
| **DR-07** | Sri Lanka Biodiversity/CBD Clearing-House | National reports, projects, indicators, protected areas, species, ecosystems, and wetland documents | National, project, species, and ecosystem levels | Use as a discovery and policy gateway | Individual documents have different dates, methods, and reuse conditions |
| **DR-08** | IUCN Red List spatial data | Species ranges, points, polygons, Red List categories, taxonomic information, sources, and freshwater HydroBASIN tables | Global, species, and catchment levels | Add threatened-species and freshwater-basin context | Ranges may be incomplete; non-commercial terms apply; cross-check with Sri Lankan records |
| **DR-09** | FAO GAEZ Sri Lanka agro-ecological regions | Dry, Intermediate, and Wet zone orientation layer based on rainfall, soil, and terrain | National; three feature records | Establish a first spatial orientation | Source is old, no licence is provided, and the layer is too coarse for final ecological fit |
| **DR-10** | University of Jaffna homegarden study | Flora, fauna, shade, food, medicinal plants, pollinators, soil, water, and household ecosystem services | Jaffna Peninsula; homegarden level | Compare cultivated living systems and relationship fields | One regional study should not be generalised nationally |
| **DR-11** | World Agroforestry Kandyan homegarden study | Perennial trees, fruit-tree diversity, soil, rainfall, culture, and wet/intermediate-zone context | Kandy and adjacent districts; homegarden level | Study tree–food–culture relationships | Definitions of Kandyan homegarden vary; retain the study’s own scope |
| **DR-12** | Sri Lankan AMF rice study | Root–fungus colonisation, growth stage, fertilizer treatment, and soil-condition relations | Rice rhizosphere and experimental treatment level | Build a soil-life evidence layer | Experimental findings should not be projected automatically to forests or all farms |
| **DR-13** | IUCN Sri Lanka project portfolio | Species surveys, habitat studies, conservation projects, coastal work, freshwater fish, and community activities | Species, habitat, basin, coast, and project levels | Find case studies and responsible institutions | Project pages may summarise rather than provide raw data |
| **DR-14** | UN Decade restoration cases | Mangrove and ecosystem-restoration methods, science, community participation, and natural-regeneration lessons | Site and project level | Compare restoration approaches | Case-study framing may foreground successes; seek full evaluation where possible |
| **DR-15** | University and journal repositories | Local theses, articles, species surveys, pollinator studies, forest studies, soil studies, and community research | Site to national level | Fill local evidence gaps and cross-check official sources | Metadata, access, copyright, and methods vary |

## 2. Data-joining opportunities

The first synthesis layer should explore how existing resources can be connected without pretending that they were designed as one database.

| Join | Potential value | Required check |
|---|---|---|
| Plant checklist ↔ National Herbarium | Verified names, synonyms, and specimen authority | Taxonomic version, authority, and access |
| Medicinal checklist ↔ conservation status | Identify medicinal plants requiring conservation attention | Status date, definitions, and sensitive species handling |
| Forest regions ↔ protected areas ↔ habitats | Connect administrative responsibility with ecological space | Boundary versions and overlapping mandates |
| Wetland directory ↔ spatial layers ↔ local studies | Compare national entries with mapped and observed conditions | Date, spatial precision, wetland definition, and update history |
| IUCN ranges ↔ Sri Lankan records | Cross-check global and national species-distribution evidence | Taxonomy, incomplete ranges, and licence |
| GAEZ zones ↔ soil, rainfall, watershed, and habitat data | Add ecological context to cultivation hypotheses | Coarse orientation layer, old source, and no licence |
| Homegarden studies ↔ medicinal, food, and pollinator records | Compare cultivated living networks | Regional scope and sampling differences |
| Forest studies ↔ tree and regeneration records | Link canopy, habitat, succession, and tree candidates | Study design, site, disturbance, and transferability |

## 3. Source maturity

| Maturity | Meaning |
|---|---|
| **Discovered** | The source or institution has been located |
| **Inspected** | The original page or document has been opened and its scope recorded |
| **Extractable** | Relevant records or claims can be extracted in a structured manner |
| **Cross-checked** | The information has been compared with another source or method |
| **Atlas-ready** | The data can be linked to an atlas record with clear provenance, uncertainty, and reuse permission |

Most resources in this first register are **inspected** or **discovered**, not atlas-ready.

## 4. First extraction priorities

The first extraction effort should prioritise sources with high authority, high relevance, and reasonable accessibility:

1. the 2025 medicinal-plant checklist for plant identity, synonyms, conservation status, and biocultural research leads;
2. National Herbarium information for taxonomic verification and threatened flora;
3. DWC protected-area and corridor information for habitat and movement context;
4. the National Wetland Directory and CEA gateways for wetland discovery;
5. IUCN spatial data for threatened species and freshwater catchment context;
6. FAO GAEZ as a coarse orientation layer only;
7. locally grounded university studies for pollination, homegardens, soil life, and ecological relationships.

## 5. Anti-duplication decision tree

| Question | If yes | If no |
|---|---|---|
| Does a catalogue already contain the required identity or status? | Link and cite it | Search adjacent institutions |
| Does it contain the required geography or season? | Reuse with scope noted | Record the gap |
| Is the format usable? | Extract with provenance | Create a translation or synthesis layer only if justified |
| Is reuse permitted? | Follow the licence and attribution | Request permission or use for reference only |
| Is the data current enough? | Record update date | Cross-check or mark historical |
| Is it socially or ecologically sensitive? | Apply access controls | Publish only appropriate aggregated information |

## 6. Working principle

> **The new contribution should be the connection, interpretation, and responsible findability of existing knowledge—not unnecessary duplication of its original labour.**

## References

[1]: https://botanicgardens.gov.lk/service/national-herbarium/ “National Herbarium,” Department of National Botanic Gardens, Sri Lanka.

[2]: https://cjs.sljol.info/articles/10.4038/cjs.v53i4.8264 “Preserving Sri Lanka’s indigenous healing heritage: An updated checklist of medicinal plants and conservation priorities,” *Ceylon Journal of Science*.

[3]: https://www.env.gov.lk/web/index.php/en/department-of-forest-conservation “Department of Forest Conservation,” Ministry of Environment, Sri Lanka.

[4]: https://www.dwc.gov.lk/?page_id=72 “Protected Areas,” Department of Wildlife Conservation, Sri Lanka.

[5]: https://www.cea.lk/web/?option=com_content&view=article&layout=edit&id=1564 “Special projects / programs,” Central Environment Authority, Sri Lanka.

[6]: https://lk.chm-cbd.net/documents/national-wetland-directory-sri-lanka “National Wetland Directory of Sri Lanka,” Sri Lanka Biodiversity/CBD.

[7]: https://lk.chm-cbd.net/ “Sri Lanka Biodiversity,” National Clearing-House Mechanism.

[8]: https://www.iucnredlist.org/resources/spatial-data-download “Spatial Data Download,” IUCN Red List of Threatened Species.

[9]: https://gaez.fao.org/datasets/agro-ecological-regions-of-sri-lanka/about “Agro Ecological Regions of Sri Lanka,” FAO Global Agro-Ecological Zones.

[10]: http://repo.lib.jfn.ac.lk/ujrr/handle/123456789/1458 “Ecosystem Services of Homegarden Agroforestry in Jaffna Peninsula,” University of Jaffna repository.

[11]: https://worldagroforestry.org/publication/kandyan-home-gardens-time-tested-good-practice-sri-lanka-conserving-tropical-fruit-tree “Kandyan home gardens: a time-tested good practice from Sri Lanka for conserving tropical fruit tree diversity,” World Agroforestry.

[12]: https://www.mdpi.com/2071-1050/14/24/16537 “Assessment of Community Dynamics of Arbuscular Mycorrhizal Fungi in the Rice (*Oryza sativa* L.) Rhizosphere and Potential Application as Biofertilizer,” *Sustainability*.

[13]: https://iucn.org/our-work/region/asia/countries/sri-lanka/our-work “Our Work — Sri Lanka,” IUCN.

[14]: https://www.decadeonrestoration.org/sri-lankan-initiative-expand-its-mangrove-forests-over-50-cent-recognized-one-seven-un-world “Sri Lankan initiative to expand its mangrove forests by over 50 per cent recognized as one of seven UN World Restoration Flagships,” UN Decade on Ecosystem Restoration.
