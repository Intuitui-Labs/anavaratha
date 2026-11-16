# Household hazardous waste: where the route breaks

```mermaid
flowchart LR
  classDef ok fill:#f0fdf4,stroke:#15803d,color:#14532d
  classDef paper fill:#fff7ed,stroke:#c2410c,color:#7c2d12
  classDef broken fill:#fef2f2,stroke:#b91c1c,color:#7f1d1d,stroke-width:2px
  classDef sink fill:#1e293b,stroke:#090d16,color:#fff
  H(["Household: spray can,<br/>paint, medicines, CFL"]) --> R["By-law: separate<br/>hazardous waste (c) [S1]"]:::paper
  R --> C["Council collector<br/>or council bins [S1]"]:::paper
  C --> X1{{"CMC asks 3 streams only:<br/>recyclable · non-recyclable · food<br/>no hazardous stream found [S2][S3]"}}:::broken
  R -. "national route?" .-> SW["CEA Scheduled Waste licence<br/>= industrial generators only [S15]"]:::broken
  R -. "MSW route?" .-> MG["CEA MSW guideline:<br/>hazardous out of scope [S16]"]:::broken
  X1 --> M["Mixed into non-degradables<br/>Negombo ≈200 kg/day [S6]"]:::paper
  SW -. "route missing" .-> M
  MG -. "'somewhere else' not found" .-> M
  M --> D[("Open dump<br/>≈63% of disposal [S7]")]:::sink
  M --> W[("WtE / landfill<br/>(Colombo) [S13]")]:::sink
  P["Recyclables: PET, glass, metal<br/>→ collectors / resource banks"]:::ok
  H --> P
  B["Frame B refusal case:<br/>rule exists, route does not"]:::broken
  X1 --- B
```

![render](e_household_route.png)

**Sources:** `neevsk-research/anavaratha/phase1/DESK_HOUSEHOLD_WASTE_STREAMS_LK.md` §1–§4, §6. [S#] tags are that note's source keys.

**Notes:** Frame B refusal *candidate*, not a verified-on-ground finding. "≈63%" is UNDP Sri Lanka 2 Oct 2026 (primary story).
