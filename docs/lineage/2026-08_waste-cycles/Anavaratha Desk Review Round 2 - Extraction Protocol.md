# Anavaratha Desk Review Round 2: Extraction Protocol

## Purpose

Round 2 moves from broad source discovery to page-level evidence extraction. The aim is to identify exact claims, definitions, numbers, mechanisms, and limitations that can support a comparable waste-system baseline.

## Priority source set

| Priority | Source | Why it is included | Extraction focus |
|---|---|---|---|
| 1 | National Action Plan on Plastic Waste Management 2021–2030 | National lifecycle, goals, baseline estimates, actors, and Pilisaru lessons | Definitions, baseline methods, targets, implementation responsibilities, failures, monitoring |
| 2 | IWMI 20-city analysis | Cross-city comparison and resource-recovery context | Local-authority characteristics, population/activity denominators, flows, recovery, costs, constraints |
| 3 | Western Province database evaluation | Data-system operation over a year | Data fields, update cycles, institutional use, missingness, dashboard lessons |
| 4 | CEA policy recommendations on Western Province master plan | Policy principles and planning safeguards | 3R, circularity, EPR, cumulative impacts, technology choices, alternatives, governance |
| 5 | Southern Province problems/issues study | Historical structural constraints and policy–scale mismatch | Local-authority scale, household access, land, finance, skills, political commitment |
| 6 | Western Province implementation analysis | Implementation factors across local governments | Staff, leadership, social/business participation, land, vehicles, regulation, politics |
| 7 | Southeastern coastal-city study | Coastal operational and downstream-flow context | Composition, collection, segregation, destination transfers, local recycling capacity |
| 8 | Small local-authority case study | Small-authority intervention and planning logic | Home composting, awareness, planning, cost, technical and facility constraints |
| 9 | UN-Habitat WaCT/WFD | Standard measurement architecture | Definitions, assessment steps, leakage, facility control, stakeholder process |
| 10 | Recent provincial strategic plans | Contemporary implementation and scale context | Stated problems, targets, institutional arrangements, financing, monitoring |

## Page-level extraction fields

For every claim, record:

- `claim_id`
- `source_id`
- `page_or_section`
- `exact_claim_or_close_paraphrase`
- `claim_type`: definition, measured result, estimate, target, explanation, recommendation, or limitation
- `location`
- `spatial_scale`
- `population_or_activity_denominator`
- `reference_period`
- `waste_stream`
- `system_boundary`
- `actor`
- `capacity_type`
- `constraint`
- `failure_or_success_mechanism`
- `outcome`
- `unit_and_value_if_any`
- `method`
- `evidence_grade`
- `transferability`
- `alternative_explanation`
- `future_validation_need`

## Extraction rules

A number without a year, boundary, unit, and definition is incomplete. A target must be separated from an achieved outcome. A recommendation must be separated from an observed finding. A study-specific result must not be generalized to all Sri Lanka without an explicit basis. A source’s own estimate should be preserved even when another source disagrees; the contradiction becomes a separate record.

## Quality control

Each extracted claim should be checked twice: once against the source text and once against the coded interpretation. Quantitative claims should be reviewed for denominator and period. Causal claims should include at least one alternative explanation. All extracted material should preserve the source URL, citation, and retrieval date.

## Round 2 output

The round should produce a page-level claim register, definition register, contradiction register, evidence-quality register, source-by-context matrix, and a revised Desk Baseline v0.2. The output should remain desk-based and should end with a small number of high-value validation questions rather than a broad fieldwork wish list.
