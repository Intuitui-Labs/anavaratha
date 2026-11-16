# Institution responsibility chain

```mermaid
flowchart LR
  NOTE["Dashed grey links = a keyword found in the actor's formal-role text<br/>(Enforcement Institution & Capacity Map v0.1).<br/>Inferred, not a judgement of what the actor does."]:::note
  classDef note fill:#f8fafc,stroke:#64748b,color:#0f172a,stroke-dasharray:2 2
  classDef link fill:#090d16,stroke:#090d16,color:#fff
  classDef inst fill:#fff,stroke:#334155,color:#090d16
  classDef gap fill:#fef2f2,stroke:#b91c1c,color:#7f1d1d,stroke-dasharray:4 3
  subgraph CH["Accountability chain · Core §3F"]
    direction TB
    D[duty]:::link --> CA[capacity]:::link --> DE[detection]:::link --> EN[enforcement]:::link --> RE[remedy]:::link --> PE[persistence]:::link
  end
  I1["CEA"]:::inst
  I2["Ministry of Environment"]:::inst
  I3["MC / UC / Pradeshiya Sabha"]:::inst
  I4["WMA Western Province"]:::inst
  I5["UDA + land authorities"]:::inst
  I6["District / divisional admin"]:::gap
  I7["Police"]:::inst
  I8["Magistrate's Courts"]:::inst
  I9["Forest · wildlife · wetland agencies"]:::inst
  I10["Informal + private operators"]:::inst
  I11["Courts · PIL · communities"]:::inst
  I1 -. "“administer”?" .-> D
  I1 -. "“inspect”?" .-> DE
  I1 -. "“directions”?" .-> EN
  I2 -. "“policy”?" .-> D
  I2 -. "“steering & monitoring”?" .-> PE
  I3 -. "“local waste”?" .-> D
  I3 -. "“transport”?" .-> CA
  I4 -. "“programs”?" .-> CA
  I5 -. "“permissions”?" .-> EN
  I7 -. "“investigate”?" .-> DE
  I7 -. "“criminal”?" .-> EN
  I8 -. "“summary trials”?" .-> EN
  I8 -. "“fines”?" .-> RE
  I9 -. "“monitoring”?" .-> DE
  I9 -. "“approvals”?" .-> EN
  I10 -. "“collection”?" .-> D
  I10 -. "“recovery”?" .-> CA
  I10 -. "“monitoring”?" .-> DE
  I11 -. "“complaints”?" .-> DE
  I11 -. "“litigation”?" .-> RE
  I6 -. "coordination only; no keyword" .-> CH
  linkStyle 0,1,2,3,4 stroke:#090d16,stroke-width:2.5px
  linkStyle 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24 stroke:#64748b,stroke-width:1.2px,stroke-dasharray:6 4
```

![render](d_responsibility_chain.png)

**Sources:** Chain: Core Package §3F "duty → capacity → detection → enforcement → remedy → persistence" (`…/ANAVARATHA_LEARNING_LEVERAGE_ACTION_ARCHITECTURE_V0_1.md`). Actors: 11 classes in `raw/waste_cycles_anavaratha/zip_entries/Anavaratha Enforcement Institution and Capacity Map v0.1.md`.

**Notes:** Edge labels are the **keyword found in each actor's "formal role" text**, not a judgement of what they actually do. District administration has no matching keyword (red dashed box). The 11-step compliance-production chain is in `data/flows.json`.
