# Anavaratha Real-Data Exploration v0.1

## Scope and status

This is the first real-data exploration for the waste side of Anavaratha. It remains at the national and broad spatial level. It does not select a locality, construct a current national waste inventory, or claim that different sources are directly comparable without harmonization.

The analysis combines three real source groups: Sri Lanka’s Department of Census and Statistics 2024 provisional Grama Niladhari Division tables; the World Bank What a Waste 3.0 country dataset; and Sri Lanka’s National Action Plan on Plastic Waste Management 2021–2030. The first group supplies population and household denominators, the second supplies a standardized but source-heterogeneous MSW series, and the third documents policy goals and data-system gaps.[1] [2] [3]

## 1. Population and household denominator layer

The DCS 2024 portal provides provisional GN-level population, household, and occupied-housing tables. The retrieved workbooks were aggregated across 25 districts and 9 provinces. The resulting population sum is 21,781,800; the household sum is 6,111,315; and the occupied-housing-unit sum is 6,030,541. These are denominator results from the provisional tables, not waste quantities.[1]

| Province | Population 2024 | Households 2024 | Occupied housing units 2024 |
|---|---:|---:|---:|
| Western | 6,117,341 | 1,703,420 | 1,686,506 |
| Central | 2,714,045 | 749,019 | 730,925 |
| Southern | 2,606,679 | 728,288 | 722,971 |
| North Western | 2,586,972 | 745,193 | 738,403 |
| Sabaragamuwa | 2,015,899 | 571,682 | 566,880 |
| Eastern | 1,783,214 | 499,217 | 489,362 |
| North Central | 1,407,610 | 402,469 | 397,890 |
| Uva | 1,399,892 | 400,025 | 390,145 |
| Northern | 1,150,148 | 312,002 | 307,459 |

The Western Province accounts for approximately 28.1% of the aggregated provisional population. The ten largest districts in the retrieved aggregation begin with Gampaha at 2,436,142 and Colombo at 2,375,415, followed by Kurunegala, Kandy, Kalutara, Ratnapura, Galle, Anuradhapura, Badulla, and Kegalle. These rankings describe population pressure potential only; they do not rank waste burden or service failure.

The derived district persons-per-household measure ranges from approximately 3.46 to 3.83. The household and occupied-housing totals are not identical concepts and should not be treated as interchangeable. Apparent duplicate GN code/name combinations are resolved by retaining DS-division identifiers; they occur across different DS divisions and are not automatically duplicate observations.

## 2. MSW pressure series from What a Waste 3.0

The World Bank What a Waste 3.0 data portal covers 217 economies and 262 cities, with indicators across generation, composition, collection, treatment/disposal, institutional arrangements, plastics, and related topics. Its portal explicitly warns that data quality and definitions vary by observation and that sources and estimates are noted.[2]

For Sri Lanka, the extracted annual MSW generation rows are:

| Year | MSW tonnes/year | MSW tonnes/day, derived | kg/person/day | Dataset status |
|---|---:|---:|---:|---|
| 2021 | 2,971,830.0 | 8,142.0 | 0.359699 | Observed/estimated in dataset |
| 2022 | 2,847,753.7 | 7,802.1 | 0.342720 | Observed/estimated in dataset |
| 2030 | 3,155,836.8 | 8,646.1 | 0.364513 | Projection in dataset |
| 2040 | 3,797,570.7 | 10,404.3 | 0.424669 | Projection in dataset |
| 2050 | 4,362,359.9 | 11,951.7 | 0.481686 | Projection in dataset |

The dataset’s 2021 to 2022 mass values decrease by approximately 4.2%. From the 2022 row to the 2030 projection, the projected mass increases by approximately 10.8%. From 2030 to 2050, the projected mass increases by approximately 38.2%, while the per-capita rate increases by approximately 40.5% from 2022 to 2050. These are changes within the World Bank dataset’s own series; they are not a validated Sri Lankan time series and should not be presented as observed national trends.

The dataset contains multiple metadata dimensions, including urbanization, population group, waste product, treatment type, measurement point, source, and unit. The long-format extraction was therefore filtered to the MSW Generation indicator and checked for duplicate year–unit–value rows before producing the clean table. The projection values remain labeled as projections.

## 3. Policy and information-capacity layer

Sri Lanka’s National Action Plan on Plastic Waste Management 2021–2030 identifies a national need for an inventory and monitoring mechanism for plastic entries and exits. In its baseline table, it states that an inventory dataset was not available, that there was no national data on production, and that some relevant definitions were absent. It points to the 2012 census/statistics sources, JICA solid-waste surveys, beach analysis, and selected local studies as partial baseline sources.[3]

The plan also identifies low collection rates, low collection quality because of insufficient segregation, improper practices affecting waterways and marine litter, deficiencies in implementation, inadequate coordination, limited quality-control and R&D facilities, health and safety concerns, inadequate community participation, and deficiencies in data and information.[3]

This means that **information capacity is itself a national waste-system variable**. The first real-data finding is not only how much population or projected waste exists, but how difficult it remains to construct a compatible, current, nationally complete material-flow account.

## 4. What can and cannot be concluded now

| Can be concluded from the current evidence | Cannot yet be concluded |
|---|---|
| Sri Lanka has a usable provisional 2024 population and household denominator layer at district and GN scales | Current waste pressure by district or province |
| Western Province is the largest population denominator in the retrieved census aggregation | Western Province has the largest waste gap or worst service performance |
| The World Bank dataset provides a real Sri Lanka MSW series with 2021–2022 values and 2030–2050 projections | That the World Bank values are directly compatible with the 2024 DCS census totals |
| The national plastic action plan explicitly documents major data and implementation gaps | A complete national plastic inventory or current collection rate |
| Population, households, and waste data require separate metadata and denominator treatment | A single national “waste per person” figure that combines all sources without harmonization |

## 5. National analytical implications for Anavaratha

The data support four immediate analytical directions. First, build denominator layers before pressure layers: population, households, occupied housing, establishments, tourism activity, markets, and industrial activity should remain distinct. Second, use the World Bank MSW series as a comparative and scenario source, not as a substitute for a Sri Lankan current inventory. Third, treat missing inventory, missing production data, and inconsistent definitions as measurable information-capacity constraints. Fourth, design future waste-flow analysis around compatible periods and boundaries rather than attempting to produce a visually impressive but conceptually false national total.

The next data phase should therefore seek real Sri Lankan waste observations with explicit local-authority, province, or facility boundaries; historical and current collection and disposal records; waste composition and stream data; and capacity variables such as vehicles, staff, facilities, operating days, downtime, and usable capacity. Until those are found and audited, national waste pressure should remain represented through source-specific series and uncertainty bands rather than a single synthesized number.

## References

[1] Sri Lanka Department of Census and Statistics, “Census of Population and Housing 2024: Statistical Information.” https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024

[2] World Bank Data360, “What a Waste (3.0).” https://data360.worldbank.org/en/dataset/WB_WAW

[3] Ministry of Environment Sri Lanka, “National Action Plan on Plastic Waste Management 2021–2030.” https://www.ccet.jp/sites/default/files/2021-08/srilanka_report_web_fin_pw.pdf
