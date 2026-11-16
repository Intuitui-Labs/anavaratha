# Anavaratha

## Crosswalk protocol

**Sri Lanka regenerative-cultivation dimension — Working protocol, Version 0.1**

## 1. Purpose

A crosswalk connects records from different catalogues or institutions when they refer to the same organism, habitat, place, relationship, or responsibility. It must preserve the origin and limits of each record.

The crosswalk is not a process of forcing different systems into false agreement. It is a controlled translation layer that shows matches, partial matches, conflicts, and gaps.

> **Match carefully, preserve difference, and never hide uncertainty.**

## 2. Crosswalk entities

| Entity | Examples |
|---|---|
| **Organism** | Tree, medicinal plant, fish, bird, pollinator, soil organism |
| **Habitat** | Forest, wetland, mangrove, homegarden, river, tank, coast |
| **Place** | District, ecological zone, watershed, protected area, site |
| **Relationship** | Pollination, seed dispersal, shade, water, soil, medicine, food, stewardship |
| **Status** | Native, endemic, threatened, protected, recovering, uncertain |
| **Institution** | National Herbarium, Forest Department, DWC, CEA, university, community |
| **Evidence** | Catalogue entry, study, observation, map, report, testimony, project record |

## 3. Matching levels

| Level | Meaning | Allowed use |
|---|---|---|
| **Exact match** | Same entity, same name or stable identifier, and compatible scope | Merge as linked records with provenance |
| **Probable match** | Strong evidence of same entity but identifier, spelling, or taxonomy differs | Link provisionally; require verification |
| **Related record** | Different entity with a documented ecological, spatial, or institutional relation | Connect through a relationship, not merge |
| **Partial overlap** | Records overlap in geography, time, or subject but are not equivalent | Link with boundary and scope notes |
| **Conflict** | Sources disagree in identity, status, range, date, or interpretation | Preserve both records and investigate |
| **No match** | No responsible link can be established | Keep separate |
| **Unknown** | Insufficient information to assess | Create a gap record |

## 4. Required crosswalk fields

| Field | Required content |
|---|---|
| **Crosswalk ID** | Unique identifier |
| **Source A record** | Original source and record reference |
| **Source B record** | Comparison source and record reference |
| **Entity type** | Organism, habitat, place, relationship, institution, status, or evidence |
| **Match level** | Exact, probable, related, partial, conflict, no match, or unknown |
| **Matching basis** | Name, taxonomy, geography, coordinates, habitat, date, relationship, or institution |
| **Original values** | Values as presented by each source |
| **Normalised value** | Working value used by Anavaratha, if justified |
| **Scope** | Spatial, temporal, taxonomic, and thematic limits |
| **Confidence** | High, moderate, low, or unknown |
| **Provenance** | How the match was made and by whom |
| **Reuse condition** | Licence, attribution, consent, privacy, or sensitive-location condition |
| **Conflict or gap** | What remains unresolved |
| **Atlas record** | Linked living-sector record or relationship |
| **Next action** | Verify, request, extract, map, interview, or leave open |

## 5. Identity rules

Scientific names should be recorded with source-specific names and synonyms preserved. A normalised name should not overwrite the original name. Sinhala and Tamil names should be attributed to the source or knowledge holder and should not be silently standardised.

A name match alone is insufficient when taxonomy, geography, habitat, or date is inconsistent. A crosswalk should never merge two records merely because their common names are similar.

## 6. Spatial rules

Spatial matches should state whether the overlap is exact, approximate, administrative, ecological, hydrological, or inferred. A district is not a habitat. A protected area is not necessarily the same as a forest type. A three-zone agro-ecological layer is not a substitute for local soil, watershed, elevation, or habitat data.

Exact locations of sensitive species, medicinal plants, or community knowledge should be generalised or withheld as appropriate.

## 7. Temporal rules

Every crosswalk must preserve the source date, observation period, assessment date, and update date where available. A historical record may be valuable without being current. A current status may not invalidate historical distribution evidence. Differences should be represented as temporal change, not automatically treated as error.

## 8. Relationship rules

A source that establishes identity does not automatically establish ecological function. A source that documents presence does not automatically establish reproduction. A source that records visitation does not automatically establish effective pollination. A source that records seed removal does not automatically establish successful seed dispersal.

Each relationship must be linked to the evidence that supports that relationship specifically.

## 9. Institutional rules

Institutional responsibility should be crosswalked without erasing overlap. The Forest Department, DWC, CEA, National Herbarium, universities, and communities may hold different parts of the same living-system record. Institutional mandate, data ownership, field authority, knowledge authority, and stewardship responsibility should be recorded separately.

## 10. Crosswalk outputs

The first crosswalk pass should produce:

| Output | Purpose |
|---|---|
| **Plant identity crosswalk** | Connect medicinal checklist, National Herbarium, local names, and atlas records |
| **Medicinal status crosswalk** | Connect use, native/endemic status, threat, habitat, and knowledge fields |
| **Species–habitat crosswalk** | Connect species records to protected areas, wetlands, forests, watersheds, and corridors |
| **Tree–source crosswalk** | Connect tree candidates to forest, homegarden, herbarium, and restoration records |
| **Wetland–spatial crosswalk** | Connect directory entries to ecological zones, watersheds, maps, and local studies |
| **Stewardship crosswalk** | Connect mandates, permits, institutions, communities, and care practices |
| **Gap and conflict register** | Preserve missing, inaccessible, inconsistent, or contested records |

## 11. Crosswalk review

A crosswalk should be reviewed for taxonomic accuracy, spatial fit, temporal fit, claim scope, institutional interpretation, consent, access, and sensitive information. It should be possible for another researcher to reconstruct why two records were linked.

> **The crosswalk is trustworthy only when it makes its reasoning visible.**
