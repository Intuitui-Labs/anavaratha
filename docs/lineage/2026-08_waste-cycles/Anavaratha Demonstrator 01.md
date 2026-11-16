# Anavaratha Demonstrator 01

## A thermodynamic-material-cycle and usable-capacity audit of Western Province composting

**Date:** 22 August 2026  
**Status:** Desk-based demonstrator using a real 22-station dataset reported in a 2025 peer-reviewed study with January–December 2022 data. It is not a current 2026 operational audit and does not represent all Western Province facilities.

## Executive result

Demonstrator 01 tests whether a facility’s **reported design capacity, reported running capacity, and reported compost output can be interpreted as one continuous material transformation**. They cannot be assumed to be so. Across the 22 surveyed Western Province compost stations, the study reports design capacity of **2,775 t/month**, running capacity of **2,391.3 t/month**, and actual compost production of **157 t/month**. These values describe different reported fields. They do not establish that 2,391.3 t/month entered the process, that the difference should have become compost, or that the difference represents rejects, stock, moisture loss, downtime, unrecorded diversion, or any other particular process.

The defensible result is therefore a **partial-observation mismatch**: reported running capacity is much larger than reported useful output within the study’s definitions. Seventeen of 22 stations report production below 10% of running capacity. This is a reason to investigate the middle of the process, not a complete explanation of it. It does not prove illegality, non-function, current 2026 status, or a measured physical loss.

## 1. Boundary and control volume

The primary control volume is the composting station:

```text
Collected biodegradable waste
          ↓
Accepted input / contamination and rejects
          ↓
Composting operation
          ↓
Compost output / stock / sales or use
          ↓
Rejects and residuals → downstream disposal or unknown route
```

The study provides design capacity, running capacity, actual production, sales, staffing, and station-level diagnostic fields. It does not provide a complete accepted-input mass, reject mass, residual mass, opening stock, closing stock, maintenance history, equipment uptime, or final residual destination for every station. Accordingly, this demonstrator produces **partial material and capability diagnostics**, not a complete mass balance or thermodynamic entropy balance.

## 2. Material ledger

| Aggregate field | Reported value | Interpretation |
|---|---:|---|
| Surveyed stations | 22 | Study boundary |
| Design capacity | 2,775 t/month | Nominal capacity |
| Running capacity | 2,391.3 t/month | Reported running field, not independently audited uptime |
| Actual compost production | 157 t/month | Reported useful-output field |
| Compost sales | 142.4 t/month | Sales field; requires stock reconciliation |
| Employees | 254 | Reported headcount, not attendance or effective labour hours |
| Running/design | 86.17% | Reported operating-capacity relation |
| Production/running | 6.57% | Conversion-gap diagnostic |
| Sales/production | 90.70% | Not a pure current-period conversion without stock data |

The numerical difference between reported running capacity and reported actual production is **2,234.3 t/month**. This is not a measured quantity of waste, rejects, unprocessed input, thermodynamic loss, or missing compost. It is only a difference between two reported fields. The correct label is **reported capacity-output difference under a partial observation boundary**.

The numerical difference between reported design and reported running capacity is **383.7 t/month**. This is also not a measured downtime or unavailable capacity. It may reflect definitions, design revisions, operating assumptions, aggregation, or actual underuse; the available fields do not distinguish these possibilities.

## 3. Station-level distribution

The average station running/design ratio is 89.77%, with a median of 80.91% and a range of 33.33%–185.00%. Seven stations report running capacity above design capacity. These records are not evidence of extraordinary performance; they are data-quality, definition, or boundary warnings requiring reconciliation.

The average station production/running ratio is 7.19%, with a median of 7.29% and a range of 0.13%–18.53%. The lowest reported production/running values are associated with Minuwangoda, Mathugama, Millaniya, Kelaniya, Palindanuwara, Walallawita, Madurawala, Kotikawatte, Horana, and Seethawaka. The highest values in the study are associated with Ja-Ela, Divulapitiya, Seethawakapura, Agalawatte, Negombo, Ja-Ela PS, Katana, Beruwala, Bulathsinhala, and Meerigama.

These rankings are descriptive only. They should not be interpreted as rankings of current facility quality because the study period is 2022, the variables are self-reported or survey-reported, and the stations may differ in boundary, feedstock, operating schedule, and measurement practice.

Four stations report sales above current-period production. This is a direct warning that sales may include stock produced earlier, that production and sales periods may differ, or that the fields use different boundaries. Therefore:

\[
Sales \neq Current\ production
\]

unless opening stock, closing stock, and inventory movement are recorded.

## 4. Dissipation ledger

Anavaratha uses “dissipation” here as a layered operational concept rather than as a claim to have calculated physical entropy production.

| Dissipation form | Demonstrator evidence | Current status |
|---|---|---|
| Material dissipation | Large reported gap between running capacity and compost output | Descriptive proxy |
| Quality dissipation | Study and WMA plan document contamination and mixed feed | Documented constraint; station-level current quantities incomplete |
| Process dissipation | Insufficient maturation, process control, space, and equipment constraints | Documented constraint |
| Information dissipation | Missing accepted input, rejects, residuals, stock, uptime, and destination data | Explicit information gap |
| Institutional dissipation | Maintenance, staffing, procurement, coordination, and data weaknesses in planning evidence | Documented system constraint |
| Justice dissipation | Possible transfer through residuals, leachate, odour, ground handling, and receiving sites | Requires site-level verification; no unverified allegation |

The demonstrator’s most defensible diagnostic is:

\[
Reported\ capacity\text{-}output\ difference = Reported\ running\ capacity - Reported\ actual\ output
\]

This identifies a mismatch that requires investigation. It is not a measured flow, entropy production, exergy destruction, residual quantity, or national performance score. The middle process remains an explicit unknown.

## 5. Capability ledger

The station data report employees and production, but effective capability requires more than headcount. A facility may have workers and machinery but still lack usable capability if staff are absent, machines are down, inputs are contaminated, space is full, output has no market, or residuals have no safe route.

| Capability dimension | Evidence available | Missing evidence |
|---|---|---|
| Labour | Employees per station | Attendance, hours, task allocation, training, occupational safety |
| Time | Operating days field | Daily uptime, batch duration, maturation time, seasonal peaks |
| Equipment | Study constraints and facility descriptions | Machine-level condition, downtime, spare parts, maintenance records |
| Feedstock | Compost-station scope | Accepted mass, composition, contamination, rejected mass |
| Process | Actual production | Batch records, moisture, temperature, turning, quality tests |
| Market | Sales field | Buyer/use category, price, stock, rejected product, unsold inventory |
| Space | Study and WMA constraints | Occupied area, stockpile area, drainage, expansion limit |
| Residual control | Not fully available | Reject destination, leachate, overflow, final disposal |
| Information | Station table and supplementary questionnaire | Independent validation, data dictionary, audit trail, update persistence |

## 6. Thermodynamic interpretation

The demonstrator uses thermodynamics carefully.

The literal physical basis is conservation: a future complete station balance should account for accepted material, useful compost, rejects, residuals, stock change, moisture or process losses, and measurement error. The current dataset does not provide all of these terms.

The concept of exergy is potentially useful in a later bounded study comparing separated organic feedstock with contaminated mixed feedstock, or comparing process and transport alternatives. It cannot be calculated responsibly for this 22-station dataset without composition, moisture, chemical energy, reference states, and compatible process boundaries.

The concept of negentropy is used only as a metaphor for maintained organization: stream separation, measurement, feedback, repair, memory, and coordination. It is not treated as a physical substance or as a score assigned to a facility.

The project therefore distinguishes:

> **Physical balance → quality and recoverability → operational capability → institutional organization → social and ecological burden.**

## 7. Binding-bottleneck hypotheses

The data do not identify one universal bottleneck, and they do not reveal a complete input-to-output process. They support a set of testable possibilities for the unknown middle:

1. The production gap may arise from contaminated or poorly separated inputs.
2. Reported running capacity may include nominal availability rather than effective uptime.
3. Labour headcount may overstate effective labour-hours.
4. Space and maturation time may constrain throughput even when machinery exists.
5. Product quality or weak markets may cause stock accumulation and low output.
6. Unrecorded rejects and residuals may make the apparent cycle more closed than it is.
7. Missing weighing and stock records may create a data boundary rather than a purely physical gap.

These hypotheses should not be ranked by intuition. A current measurement campaign must distinguish them.

## 8. Low-resource intervention design

The first intervention should be **measurement before construction**. At one selected station or compatible station group, implement a three-month minimum ledger:

| Daily or batch field | Purpose |
|---|---|
| Incoming load and source | Defines input boundary |
| Accepted and rejected mass | Measures contamination and usable feedstock |
| Operating days and downtime | Converts asset into usable availability |
| Staff attendance and labour-hours | Measures effective labour |
| Batch start/end and maturation | Measures process time and space pressure |
| Product output | Measures useful transformation |
| Opening and closing stock | Prevents sales/output confusion |
| Sales or use destination | Tests actual product pathway |
| Reject/residual destination | Prevents hidden burden transfer |
| Maintenance and repair event | Measures persistence and capability reproduction |

The intervention should be judged by whether it improves data completeness, reveals a bottleneck, changes a measurable operational condition, and remains in use after the initial three months. It should not be judged only by tonnes of compost produced.

## 9. Burden-transfer safeguards

An intervention that increases compost production but sends more rejects to an unrecorded dump is not an unqualified success. The following downstream effects must be checked:

- rejected plastic and contaminated feedstock;
- unsold or low-quality compost stock;
- leachate from organic stockpiles;
- open-ground unloading during overflow;
- residual transport to another local authority;
- worker exposure during sorting and handling;
- fire, odour, and nuisance;
- ecological receiving areas near final disposal.

This is the operational form of the residuals constitution: no diversion claim without a residual account.

## 10. Persistence test

A practical persistence design is:

| Moment | Test |
|---|---|
| Baseline month | Record existing practice and data completeness |
| Month 1 | Introduce minimum ledger and identify first bottleneck |
| Month 2 | Adjust one process or measurement practice |
| Month 3 | Compare output, rejects, stock, downtime, and data completeness |
| Month 6 | Test whether the practice continues without special project support |
| Month 12 | Check whether the change became routine, was abandoned, or shifted burden elsewhere |

Persistence is not simply continuation of equipment operation. It includes the survival of routines, maintenance, data, worker protection, market relationships, and residual accountability.

## 11. What Demonstrator 01 establishes

The demonstrator establishes that the 22-station dataset can support a rigorous description of three reported fields and their numerical relationships. It does **not** establish a complete input-to-output conversion, a measured process loss, a quantity of unprocessed waste, or a causal explanation of the middle. It also establishes that current data are insufficient for a complete material balance, physical entropy calculation, current 2026 status claim, or facility-by-facility causal explanation.

It provides a reusable measurement grammar for the next stage:

> **input quality + effective labour + uptime + process time + space + market + residual route + information + maintenance = usable facility capability.**

This is not a national formula. It is a structured hypothesis about how capacity is produced.

## 12. Deliverables

The following files implement this demonstrator:

- `ANAVARATHA_DEMONSTRATOR_01_BOUNDARY_AND_AUDIT_DESIGN_V0_1.md`
- `ANAVARATHA_DEMO01_MATERIAL_LEDGER.csv`
- `ANAVARATHA_DEMO01_DISSIPATION_LEDGER.csv`
- `ANAVARATHA_DEMO01_CAPABILITY_LEDGER.csv`
- `ANAVARATHA_DEMO01_UNCERTAINTY_LEDGER.csv`
- `ANAVARATHA_DEMO01_BOTTLENECK_LEVERAGE_MATRIX.csv`
- `ANAVARATHA_WESTERN_STATION_DISTRIBUTION_SUMMARY.csv`
- `ANAVARATHA_WESTERN_STATION_ANALYTICS_FULL.csv`

## References

[1] Manipura, A., Drechsel, P., Jayawardhana, H. M. L. C., Shanmugapriya, R., Mannapperuma, N. R., & Jayatilleke, H. S. (2025). *Improved performance indicators and institutional setup for more viable compost production from municipal solid waste in Sri Lanka*. Waste Management Bulletin, 3(3), 100217. https://doi.org/10.1016/j.wmb.2025.100217

[2] Western Province Waste Management Authority. *Western Province Solid Waste Management Master Plan in Sri Lanka*. Public source gateway: https://wma.wp.gov.lk/notice/8

[3] Nielsen, S. N., Müller, F., Marques, J. C., Bastianoni, S., & Jørgensen, S. E. (2020). *Thermodynamics in Ecology—An Introductory Review*. Entropy, 22(8), 820. https://doi.org/10.3390/e22080820

[4] Valero, A., Usón, S., Torres, C., & Valero, A. (2010). *Application of Thermoeconomics to Industrial Ecology*. Entropy, 12(3), 591–612. https://doi.org/10.3390/e12030591

[5] Hammond, G. P., & Winnett, A. B. (2009). *The Influence of Thermodynamic Ideas on Ecological Economics: An Interdisciplinary Critique*. Sustainability, 1(4), 1195–1225. https://doi.org/10.3390/su1041195
