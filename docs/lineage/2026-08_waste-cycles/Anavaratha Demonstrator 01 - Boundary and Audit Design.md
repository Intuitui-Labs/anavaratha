# Anavaratha Demonstrator 01: Boundary and Audit Design

**Subject:** Western Province composting pathway. **Dataset:** 22 compost stations, January–December 2022, reported in a 2025 peer-reviewed study. **Status:** Desk-based demonstrator; no current operational claim.

## 1. Aim

Demonstrator 01 tests whether a facility’s nominal or reported running capacity corresponds to useful material transformation once feed quality, labour, equipment, time, market, stock, and residual pathways are considered.

## 2. Control volume

The primary control volume is the **compost-station process boundary**:

```text
Collected biodegradable waste
          ↓
Accepted input / rejected contamination
          ↓
Composting operation
          ↓
Compost output / stock / sales or use
          ↓
Rejects and residuals → downstream disposal or unknown route
```

The surrounding collection system, transfer points, generators, and ecological receivers remain contextual boundaries. They must not be pulled into a numerical mass balance unless compatible records exist.

## 3. Three linked ledgers

| Ledger | Purpose | Current data availability |
|---|---|---|
| Material ledger | Track design, running capacity, production, sales, rejects, stock, and residuals | Partially available; production, sales, design, running, and staffing are available for 22 stations |
| Capability ledger | Track labour, operating days, machinery, weighing, separation, maintenance, quality control, markets, and data systems | Constraints are reported; complete station-by-station operational fields are not all available |
| Burden ledger | Track contamination, odour, leachate, unsafe work, residual disposal, fire, ecological receiver, and burden transfer | Qualitative study evidence and planning evidence; current site-level burden measurements unavailable |

## 4. Core variables

| Variable | Meaning | Rule |
|---|---|---|
| Design capacity | Nominal stated monthly capacity | Never treat as actual intake or output |
| Running capacity | Reported monthly capacity during operation | Treat as reported operational field, not independently audited uptime |
| Actual production | Reported compost output per month | Primary useful-output field |
| Sales | Reported compost sold per month | Do not equate with current production without stock reconciliation |
| Production/running | Actual production divided by running capacity | Diagnostic of transformation realization within the reported boundary |
| Running/design | Running capacity divided by design capacity | Diagnostic of reported operating relation |
| Sales/production | Sales divided by production | Stock warning when above 100%; not a pure conversion metric |
| Production per employee | Actual production divided by reported employees | Descriptive staffing-productivity proxy only |

## 5. Minimum mass-balance form

For a future current survey, use:

\[
Accepted\ input = product\ output + reject\ output + residual\ output + closing\ stock - opening\ stock + measurement\ error
\]

The present 22-station dataset does not expose all terms. Therefore the demonstrator reports **partial balance diagnostics**, not a complete mass balance.

## 6. Main audit questions

1. How large is the gap between design capacity, reported running capacity, and actual compost production?
2. Is the gap widespread or concentrated in a few stations?
3. Which station records exceed design capacity or report sales above production, indicating data-quality or stock-boundary issues?
4. What operational constraints are documented, and which variables are missing for causal testing?
5. What downstream residual, leachate, contamination, and burden pathways remain invisible?
6. What minimum additional data would convert the demonstrator from descriptive diagnosis into an auditable facility balance?
7. Which low-resource intervention could plausibly increase usable capacity without creating downstream burden?
8. How would persistence be checked after the intervention or project period?

## 7. Interpretation boundary

The demonstrator does not estimate national compost capacity, current 2026 station status, facility legality, contamination levels, environmental pollution, or causality. It does not add the 22 stations to the WMA’s province-wide capacity series because their facility boundary, period, and units are not reconciled.

The demonstrator’s central result is a **conversion-gap diagnosis**: how much of reported running capacity appears as reported useful compost output under the study’s own definitions. The result must be paired with uncertainty, source period, and missing-field documentation.
