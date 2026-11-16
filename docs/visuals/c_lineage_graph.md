# Lineage: legacy → current

```mermaid
flowchart LR
  classDef dup fill:#fff7ed,stroke:#c2410c,color:#7c2d12
  classDef con fill:#fef2f2,stroke:#b91c1c,color:#7f1d1d
  classDef ext fill:#f0fdf4,stroke:#15803d,color:#14532d
  classDef ign fill:#f1f5f9,stroke:#64748b,color:#334155,stroke-dasharray:4 3
  classDef cur fill:#f0f9ff,stroke:#0369a1,color:#0c4a6e
  subgraph LEG["Legacy · Feb–Oct 2026"]
    direction TB
    L1["Premise (charter)"]:::dup
    L2["Name meaning"]:::con
    L3["Three domains"]:::ign
    L4["Use→residual→regen"]:::dup
    L5["Displacement test /<br/>accountable transition"]:::ext
    L6["Negentropy = metaphor"]:::con
    L7["Intervention typology"]:::con
    L8["Maturity model"]:::con
    L9["Capacity chain"]:::dup
    L10["WP compost 157/2,775"]:::con
    L11["11-actor responsibility<br/>chain [WC]"]:::dup
    L12["15-company list"]:::dup
    L13["Platform dashboard"]:::con
    L14["Afterlives evidence"]:::ext
    L15["Cultivation atlas"]:::ign
    L16["Exergy identity"]:::ign
  end
  subgraph CUR["Current · Phase 1"]
    direction TB
    C1["PROBLEM_FRAME"]:::cur
    C2["Name gate"]:::cur
    C3["(no domain tags)"]:::cur
    C4["Frame A"]:::cur
    C5["Frame B"]:::cur
    C6["Frame C syntropy-first"]:::cur
    C7["KILL_LOG"]:::cur
    C8["STAGE_EXIT_CRITERIA"]:::cur
    C9["LEDGER §3–4"]:::cur
    C10["LEDGER (b) compost gain"]:::cur
    C11["DIRECTORY 487 + LEDGER 41"]:::cur
    C13["household routes"]:::cur
  end
  L1 -- DUP --> C1
  L2 -- "DUP+CON" --> C2
  L3 -. IGN .-> C3
  L4 -- DUP --> C4
  L5 -- EXT --> C5
  L6 -- CON --> C6
  L7 -- CON --> C7
  L13 -- CON --> C7
  L8 -- "DUP+CON" --> C8
  L9 -- DUP --> C9
  L10 -- CON --> C10
  L11 -- DUP --> C11
  L12 -- DUP --> C11
  L14 -- EXT --> C13
  L15 -. IGN .-> C3
  L16 -. IGN .-> C3
```

![render](c_lineage_graph.png)

**Sources:** `anavaratha-legacy/OVERLAP_MAP.md` §2 codes. DUP = current redoes it unknowingly · EXT = current goes beyond · CON = conflict with a current lock · IGN = current ignores it.

**Notes:** 16 of the 27 rows in OVERLAP_MAP §2 are drawn; the rest are in `data/graph.json` (kind `legacy_concept`).
