# ANAVARATHA — Agent Context Document
## Read this first. Every session. Always.

> This document gives any coding agent the full context needed to build inside Anavaratha without re-explanation. It is compressed but complete. If something seems contradictory, ask. If something seems missing, check the linked documents before assuming it doesn't exist.

---

## 1. What Anavaratha Is (30 seconds)

Anavaratha is an ecological and human exergy accounting framework operating in Sri Lanka. It traces how life buys time under pressure — and where that time is being stolen.

**The central accounting identity:**
```
Total Input ≈ Consumed Output + Dissipated/Byproducts + Waste
```
The gap between left and right = what official economy doesn't see. Anavaratha's job is to make that gap visible, measurable, and actionable.

**Three ontological commitments:**
- Reality is dissipative (entropy is unavoidable — question is where, how fast, who pays)
- Reality is autopoietic (systems self-reproduce and resist external control)
- Reality is holarchic (nested wholes — damage propagates across scales)

**Anavaratha is an actor, not just an analyst.** It intervenes where the diagnostic shows a small action has a large negentropic effect.

---

## 2. The Document Stack

All documents live in `/outputs/`. Agent should read relevant docs before building in that domain.

| Document | What it contains | Read when... |
|---|---|---|
| `anavaratha_foundation.md` | Full ontology, methodology, core concepts | Anything touching core framework logic |
| `anavaratha_data_domain_map_v2.xlsx` | 10 sheets — domain map, data sources, Sri Lanka sources, engineering layer, analysis layer, viz layer, gaps | Anything touching data |
| `anavaratha_ml_guide.md` | ML model types mapped to Anavaratha questions | Building any analytical model |
| `anavaratha_algorithms_guide.md` | Specific algorithms — exergy, time series, spatial, network, sensory | Implementing specific analyses |
| `anavaratha_visualisation_guide.md` | Chart types, colour philosophy, design principles | Building any visualisation |
| `anavaratha_intervention_methodology.md` | Full intervention arc — Enter→Diagnose→Identify→Design→Act→Evaluate | Intervention planning tools |
| `anavaratha_intervention_typology.md` | Six intervention types with mechanisms | Intervention type selection |
| `anavaratha_leverage_points.md` | Leverage point hierarchy and identification methodology | Leverage point analysis tools |
| `anavaratha_evaluation_framework.md` | Evaluation indicators, displacement test, community protocol | Evaluation and monitoring tools |

---

## 3. The Tech Stack

**Rule: open source, free, no vendor lock-in, runs on a laptop.**

### Data Engineering
```
Ingestion:      Python (requests, httpx), Google Earth Engine API, 
                KoboToolbox (field), CKAN API (data.gov.lk)
Storage:        DuckDB (primary), Parquet/PyArrow (time series), 
                PostGIS (spatial, when needed)
Transformation: Pandas, Polars, GeoPandas, GDAL, dbt (transformations)
Pipelines:      GitHub Actions (scheduled runs), Prefect (orchestration)
Quality:        Great Expectations, Frictionless Data
Version control: Git + GitHub
```

### Data Analysis
```
Time series:    statsmodels, Prophet, ruptures (changepoint), EMD-signal
Spatial:        GeoPandas, rasterio, rasterstats, pysheds, QGIS
ML:             scikit-learn, XGBoost, NetworkX
Exergy:         CoolProp + custom scripts (Jørgensen method)
Bioacoustics:   librosa, opensoundscape
Causal:         statsmodels (DiD, Granger)
```

### Visualisation
```
Interactive:    Plotly, Streamlit (dashboards), Folium (maps)
Static:         Matplotlib, Seaborn
Geospatial:     Kepler.gl, Google Earth Engine Apps, QGIS + qgis2web
Narrative:      Quarto, Observable notebooks
No-code (community): RAWGraphs, Datawrapper, Felt.com
```

### File formats
```
Tabular:        Parquet (primary), CSV (exchange), DuckDB (analytical)
Spatial:        GeoJSON (primary), Shapefile (exchange), GeoPackage
Time series:    Parquet partitioned by domain/year
Config:         YAML
Docs:           Markdown
```

---

## 4. Data Source Index

### Sri Lanka Government Sources
| Domain | Source | URL | Data type |
|---|---|---|---|
| Water | Department of Irrigation | irrigation.gov.lk | Reservoir levels, rainfall — daily |
| Water | Mahaweli Authority | mahaweli.gov.lk | Basin statistics — annual |
| Air | Central Environmental Authority | cea.lk | Air quality, water quality |
| Biodiversity | Dept Wildlife Conservation | dwc.gov.lk | Protected areas, wildlife |
| Biodiversity | Forest Department | forestdept.gov.lk | Forest cover |
| Marine | NARA | nara.ac.lk | Fisheries, coral, mangrove |
| Socioeconomic | Dept Census & Statistics | statistics.gov.lk | HIES, census, LankaDatta |
| Economic | Central Bank Sri Lanka | cbsl.gov.lk | GDP, debt, trade — quarterly |
| Open data | Sri Lanka Open Data Portal | data.gov.lk | CKAN API v3 |

### Global Sources (Sri Lanka coverage)
| Domain | Source | Access |
|---|---|---|
| Satellite / NDVI / nighttime lights | Google Earth Engine | earthengine.google.com |
| Biodiversity occurrence | GBIF | gbif.org/api |
| Bird observations | eBird | ebird.org/api/v2 |
| Air quality | OpenAQ | api.openaq.org |
| Animal movement | Movebank | movebank.org |
| Soil (global) | SoilGrids | rest.isric.org |
| Climate | ERA5 via CDS | cds.climate.copernicus.eu |

### Critical Gaps (no data exists)
- Tank cascade network condition (14,000+ village tanks — no monitoring)
- Soundscape baselines (no acoustic monitoring anywhere in Sri Lanka)
- Human attentional ecology (no time-use or nature-contact data)
- Indigenous/estate community ecological knowledge

---

## 5. Directory Structure

```
anavaratha/
├── data/
│   ├── raw/                    # Ingested, unmodified source data
│   │   ├── irrigation/
│   │   ├── cea/
│   │   ├── gbif/
│   │   ├── earth_engine/
│   │   └── field/
│   ├── processed/              # Cleaned, transformed data
│   │   ├── water/
│   │   ├── air/
│   │   ├── soil/
│   │   ├── biosphere/
│   │   ├── sound/
│   │   └── human/
│   └── outputs/                # Analysis outputs, indicator values
├── ingestion/                  # Data ingestion scripts by source
├── transforms/                 # dbt models or pandas transform scripts
├── analysis/                   # Analysis scripts by domain
├── visualisation/              # Chart and dashboard code
├── dashboard/                  # Streamlit app
├── docs/                       # All markdown documentation
├── field/                      # KoboToolbox forms, field protocols
├── tests/                      # Data quality tests
├── .github/workflows/          # GitHub Actions pipelines
└── README.md
```

---

## 6. Naming Conventions

```python
# Files
raw__{source}__{domain}__{YYYYMMDD}.parquet
processed__{domain}__{resolution}__{YYYYMMDD}.parquet

# Variables
snake_case for all Python variables
domain__indicator__unit  for column names
e.g. water__tank_level__metres, air__pm25__ugm3

# Functions
verb_noun()  e.g. fetch_irrigation_levels(), compute_aci(), detect_changepoints()

# Constants
UPPER_SNAKE_CASE

# Configs
configs/sources.yaml      # All source URLs and API keys
configs/domains.yaml      # Domain definitions and indicators
configs/thresholds.yaml   # Reservoir condition thresholds
```

---

## 7. Core Data Models

### Observation (universal across domains)
```python
{
    "domain": str,          # water | air | soil | biosphere | sound | human
    "indicator": str,       # e.g. tank_level, pm25, soc, aci
    "value": float,
    "unit": str,
    "location_id": str,     # reference to locations table
    "timestamp": datetime,
    "source": str,          # data source identifier
    "quality_flag": str,    # good | suspect | missing
    "notes": str
}
```

### Location
```python
{
    "location_id": str,
    "name": str,
    "lat": float,
    "lon": float,
    "zone": str,            # dry_zone | wet_zone | estate | coastal | urban
    "admin_district": str,
    "ecological_unit": str  # watershed, cascade_id, protected_area etc
}
```

### Reservoir Condition (computed)
```python
{
    "reservoir_id": str,
    "domain": str,
    "condition": str,       # functioning | degrading | critical
    "current_value": float,
    "baseline_value": float,
    "trend_direction": str, # improving | stable | declining
    "trend_rate": float,    # per year
    "threshold_proximity": float,  # 0–1, where 1 = at threshold
    "last_updated": datetime
}
```

---

## 8. Web Data Collection Layer

### The need
Many Sri Lankan and global sources require scraping or API polling rather than bulk download. This layer handles automated, respectful, reliable web data collection.

### Tools
```
requests / httpx        — REST API calls
BeautifulSoup4          — HTML parsing when no API exists
Scrapy                  — structured scraping for multi-page sources
Playwright              — JavaScript-rendered pages (some government portals)
feedparser              — RSS/Atom feeds where available
ratelimit               — respect source rate limits
tenacity                — retry logic for unstable sources
```

### Source-specific collection notes

**irrigation.gov.lk**
- No official API — requires scraping reservoir status table
- Updates daily — schedule GitHub Action for 06:00 Sri Lanka time (UTC+5:30)
- Target: reservoir name, date, full supply level, current level, % storage
- Use BeautifulSoup4, store as Parquet partitioned by month

**cea.lk air quality**
- Limited public data — scrape available station readings
- Supplement with OpenAQ API (aggregates CEA data where available)
- `GET https://api.openaq.org/v3/locations?country=LK`

**data.gov.lk (CKAN)**
- Full CKAN API v3 available
- `GET https://data.gov.lk/api/3/action/package_list`
- `GET https://data.gov.lk/api/3/action/datastore_search?resource_id={id}`

**cbsl.gov.lk**
- Annual reports as PDFs — use `pdfplumber` for extraction
- Some time series available as Excel downloads
- Economic indicators: GDP, inflation, external debt, current account

**GBIF (biodiversity)**
- Full REST API: `https://api.gbif.org/v1/occurrence/search?country=LK`
- Paginated — handle `offset` and `limit` parameters
- Filter by `taxonKey` for specific species groups

**eBird**
- API v2 requires free key: `https://api.ebird.org/v2/`
- Recent observations: `GET /data/obs/LK/recent`
- Historical: use eBird Basic Dataset (bulk download, free for research)

**Google Earth Engine**
- Python API — authenticate once, then all satellite data accessible
- Key collections for Sri Lanka:
  - `COPERNICUS/S2_SR` — Sentinel-2 (10m, vegetation)
  - `NOAA/VIIRS/DNB/MONTHLY_V1/VCMSLCFG` — nighttime lights
  - `NASA/SRTM/003` — elevation/watershed delineation
  - `JRC/GSW1_4/GlobalSurfaceWater` — surface water extent (tanks)

**OpenAQ**
- `GET https://api.openaq.org/v3/measurements?country=LK&limit=1000`
- Free, no key required for basic access

### Collection principles
```python
# Always:
# 1. Check robots.txt before scraping
# 2. Rate limit all requests (minimum 1 second between requests)
# 3. Cache raw responses before parsing (never re-fetch what you have)
# 4. Log every collection run with timestamp, source, records collected
# 5. Flag missing data explicitly — don't silently skip
# 6. Store raw unmodified response alongside parsed output

import time
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=2, max=10))
def fetch_with_retry(url, params=None, headers=None):
    time.sleep(1)  # baseline rate limiting
    response = requests.get(url, params=params, headers=headers, timeout=30)
    response.raise_for_status()
    return response
```

### Scheduling (GitHub Actions)
```yaml
# .github/workflows/daily_collection.yml
on:
  schedule:
    - cron: '30 0 * * *'  # 06:00 Sri Lanka time (UTC+5:30)
jobs:
  collect:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run ingestion
        run: python ingestion/run_all.py
```

---

## 9. How to Work With This Codebase as an Agent

### Before building anything
1. Read this document fully
2. Check which domain you're working in — read that domain's section in the xlsx
3. Check if a script for this source already exists in `ingestion/`
4. Check if the data model already exists in `data/processed/`

### When building ingestion scripts
- One script per data source
- Always: fetch → validate → log → store raw → parse → store processed
- Never silently swallow errors — log them with source, timestamp, error type
- Always check rate limits and robots.txt first
- Store raw response before parsing — parsing logic will change, raw data is permanent

### When building analysis scripts
- Read the ML guide and algorithms guide for the relevant domain first
- One function per analytical operation — composable, testable
- Every analysis output includes: value, confidence/uncertainty, data quality flag, timestamp
- Document the assumption behind every analytical choice

### When building visualisations
- Read the visualisation guide — especially the colour philosophy
- Every chart has: headline (no background needed), annotation layer, data source note
- Test readability without colour (accessibility)
- Export as both interactive (HTML) and static (PNG/SVG)

### When something is unclear
Ask before building. A wrong assumption built into ingestion code propagates through the entire stack. The cost of asking is one message. The cost of wrong assumptions is a corrupted dataset.

---

## 10. Current State & What Needs Building

*(Update this section at the start of each working session)*

**Built:**
- [ ] Foundation documents (complete)
- [ ] Data domain map xlsx (complete)
- [ ] ML, algorithms, visualisation guides (complete)
- [ ] Intervention design documents (complete)

**To build next:**
- [ ] Directory structure initialisation
- [ ] Base data models (DuckDB schema)
- [ ] First ingestion script (irrigation.gov.lk reservoir levels)
- [ ] First analysis (tank level trend — STL decomposition)
- [ ] First visualisation (reservoir condition dashboard — Streamlit)
- [ ] GitHub Actions pipeline for daily collection

**Known issues:**
- None yet — greenfield

---

*This document is the agent's entry point. Keep it current. Every significant build decision that changes the architecture should be reflected here.*

*Version 0.1*
