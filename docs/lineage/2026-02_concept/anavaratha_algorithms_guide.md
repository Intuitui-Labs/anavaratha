# ANAVARATHA — Algorithms & Statistical Methods Guide
## The Right Analytical Tool for Each Ecological Dynamic

> This guide goes one level deeper than model families. Within each domain, there are specific algorithms and statistical methods that match Anavaratha's particular questions — sparse data, monsoon seasonality, network topology, entropy measurement. This is a reference for *choosing within* a model family, not just choosing the family.

---

## Part 1: Entropy & Exergy Computation

### Why this comes first
Exergy is Anavaratha's epistemic anchor. Before any ML, the foundational computation is: *how much quality has this system lost?*

### Ecological Exergy Index (Jørgensen's method)
**What it is:** Combines biomass with genetic information content to compute the thermodynamic quality of an ecosystem.

**Formula logic:**
```
Ex = Σ (βᵢ × Cᵢ)
```
Where `βᵢ` is the weighting factor (genetic complexity) for species `i` and `Cᵢ` is its concentration/biomass.

**Anavaratha application:** Compute ecological exergy for dry zone watershed before and after cascade degradation. The decline in exergy *is* the stolen time, made quantitative.

**Data needed:** Species biomass surveys (University of Peradeniya research data), IUCN Red List weighting for genetic complexity.

**Tool:** Implement in Python with pandas. No dedicated library — hand-code from Jørgensen (2000) reference values.

---

### Thermodynamic Exergy of Water Systems
**What it is:** Chemical exergy of water at a given quality compared to reference state (seawater or dead state).

**Key insight for tanks:** A tank with high turbidity, high BOD, and low dissolved oxygen has lower exergy than a clear tank — even if they contain the same volume of water. Volume without quality is not a pressure reservoir.

**Anavaratha application:** Combine Irrigation Dept water level data with CEA water quality parameters to compute *exergy-corrected tank storage* — a truer measure of cascade reservoir capacity than volume alone.

**Tool:** `CoolProp` for thermodynamic properties; manual chemical exergy calculation from CEA BOD/DO readings.

---

## Part 2: Time Series Algorithms

### Seasonal-Trend decomposition using LOESS (STL)
**What it is:** Separates a time series into three additive components: trend + seasonal + residual.

**Why it fits Sri Lanka:** The island has multiple overlapping seasonal signals — Yala season (April–September), Maha season (October–March), NE monsoon, SW monsoon. STL handles this better than classical decomposition.

**Output:** The trend component reveals long-run direction. The residual component reveals anomalies. The seasonal component confirms whether the system is still following its natural rhythm or decoupling from it — *decoupling from ecological memory* is a core Anavaratha indicator.

**Key parameter:** `seasonal` window length — set longer (13–23) for Sri Lankan agricultural data to capture inter-annual variation.

---

### Dynamic Time Warping (DTW)
**What it is:** Measures similarity between two time series that may be shifted or stretched in time. Unlike Euclidean distance, DTW aligns sequences optimally before comparing.

**Anavaratha application:**
- Compare tank water level patterns across different cascades — which tanks behave similarly? Which have decoupled from the network rhythm?
- Compare NDVI seasonality before and after plantation conversion — has the ecosystem lost its seasonal memory?
- Compare biophonic index across dry zone sites — are some soundscapes converging toward urban patterns?

**Tool:** `pip install dtaidistance`

---

### Empirical Mode Decomposition (EMD)
**What it is:** Decomposes a non-linear, non-stationary signal into Intrinsic Mode Functions (IMFs). Unlike Fourier decomposition, it's data-driven — doesn't assume sinusoidal components.

**Why this matters for ecological data:** Ecological signals (tank water levels, species counts, soil moisture) are not sinusoidal. They have irregular amplitudes and frequencies driven by monsoon variability. EMD respects this.

**Anavaratha application:** Decompose long-run (20+ year) tank level time series into fast oscillations (seasonal) + slow oscillations (multi-year drought cycles) + trend (structural degradation). The trend IMF = the stolen time.

**Tool:** `pip install EMD-signal`

---

## Part 3: Changepoint Algorithms

### PELT (Pruned Exact Linear Time)
**What it is:** Finds the globally optimal set of changepoints in a time series by minimising a cost function with a penalty for complexity.

**Key parameter:** The penalty `β` controls how many changepoints are detected. Too low → noise detected as changepoints. Too high → real transitions missed. Use BIC penalty — it balances fit and parsimony honestly.

**Anavaratha application:**
```python
import ruptures as rpt

model = rpt.Pelt(model="rbf").fit(signal)
breakpoints = model.predict(pen=10)
```
Detected breakpoints are hypotheses about when a cascade crossed a threshold. Each requires field validation — combining data witnessing with ground witnessing.

---

### BOCPD (Bayesian Online Changepoint Detection)
**What it is:** A sequential, probabilistic algorithm that computes the posterior probability of a changepoint at each new observation. Produces a probability distribution over changepoint locations.

**Why it fits Anavaratha's epistemic position:** Anavaratha is honest about uncertainty. BOCPD produces "here is our probability that a threshold was crossed" — not false certainty. Better for communication with communities and policymakers.

**Anavaratha application:** Real-time monitoring — as new monthly data arrives, update the probability that the cascade has entered a declining regime. An early warning function that knows what it doesn't know.

---

## Part 4: Spatial Algorithms

### Moran's I (Spatial Autocorrelation)
**What it is:** Measures whether nearby locations tend to have similar values.

**Anavaratha application:**
- Do ecologically degraded tanks cluster spatially? (Yes → systematic pressure, not random failures)
- Does income inequality cluster with environmental exposure by district? (Tests the visibility gradient hypothesis geographically)
- Do high-noise areas cluster around industrial zones?

**Tool:** `geopandas` + `libpysal`

---

### Getis-Ord Gi* (Hot Spot Analysis)
**What it is:** Identifies statistically significant spatial clusters of high values (hot spots) and low values (cold spots), accounting for spatial autocorrelation.

**Anavaratha application:**
- Hot spots of forest loss → extraction zone identification
- Cold spots of nighttime lights → displacement zone darkness (electricity poverty and ecological darkness — same metric, two readings)
- Hot spots of elephant conflict incidents → corridor fragmentation pressure zones

**Tool:** `esda` library

---

### Watershed Delineation
**What it is:** From a Digital Elevation Model (DEM), computes which areas drain to which points — defining hydrological catchments.

**Anavaratha application:** Define catchment boundaries for each tank in the cascade system. Creates the network topology — which catchments feed which tanks, where flow enters, where it exits.

**Tools:** `pysheds` (Python), QGIS SAGA, Google Earth Engine SRTM DEM

---

### Zonal Statistics
**What it is:** Computes summary statistics of raster values within vector polygon zones.

**Anavaratha application:** For each tank catchment polygon, compute mean NDVI, total rainfall, forest cover percentage, slope distribution. Links satellite data to tank-level quality data — building the accounting identity one spatial join at a time.

**Tool:** `rasterstats` + `rasterio`

---

## Part 5: Network Algorithms

### Betweenness Centrality
**What it is:** For each node, counts how many shortest paths between all other pairs pass through it. High betweenness = node controls many flows.

**Anavaratha application:** A tank with high betweenness is a critical pressure reservoir. If it silts, it disconnects large portions of the cascade network. These are the first tanks to monitor and restore.

---

### Percolation Analysis
**What it is:** Asks: at what fraction of removed nodes does the network stop functioning as a connected whole? The percolation threshold is a computable tipping point.

**Anavaratha application:** How many tanks in a cascade can silt before the remaining tanks lose meaningful connectivity? The reservoir erosion threshold — the point where invisible erosion becomes visible collapse.

**Tool:** NetworkX — iteratively remove nodes and compute size of giant connected component.

---

### Community Detection (Louvain / Leiden)
**What it is:** Partitions a network into communities — groups more densely connected internally than externally.

**Anavaratha application:**
- Natural sub-systems within the dry zone cascade network
- Communities within cultural knowledge networks — who shares which ecological knowledge?
- Species co-occurrence networks — which species groups are ecologically coupled?

**Tool:** `python-louvain` or `leidenalg`

---

## Part 6: Ecological Indices

### Acoustic Complexity Index (ACI)
**What it is:** Measures the ratio of differences in amplitude between adjacent time steps in an audio recording. High ACI = complex, biologically rich soundscape.

**Why it matters:** ACI distinguishes biotic sounds from anthropogenic noise. It is the closest existing measure to soundscape exergy.

**Anavaratha application:** Compute ACI for dawn recordings at Sinharaja interior → edge → nearby village → highway. The ACI gradient = the acoustic visibility gradient made measurable.

```python
from opensoundscape.audio import Audio
from opensoundscape.spectrogram import Spectrogram

audio = Audio.from_file("sinharaja_dawn.wav")
spec = Spectrogram.from_audio(audio)
aci = spec.aci()
```

---

### NDVI & Derivatives by Ecological Zone

| Zone | Best Index | Why |
|---|---|---|
| Wet zone dense forest (Sinharaja) | EVI | Less saturation at high canopy density |
| Dry zone sparse scrub + cascade catchments | SAVI | Corrects for exposed soil background |
| Estate plantation zones | NDVI trend | Decadal change more important than absolute value |
| Coastal mangroves | NDVI + NIR/SWIR ratio | Distinguishes mangrove from other coastal vegetation |

All available free from Google Earth Engine, 1984–present.

---

## Part 7: Human Exergy — Proposed Approaches

This is genuinely unmapped territory. What follows is Anavaratha's proposed approach, to be developed in the field.

### Composite Human Exergy Index (proposed)
**Components:**
- Ecological knowledge score (community survey)
- Ritual participation rate
- Hours of silence experienced daily
- Nature contact frequency
- Community governance participation
- Generational knowledge transfer rate

**Aggregation:** Principal Component Analysis (PCA) — lets the data reveal whether these form one unified factor or distinct dimensions of human exergy.

**Tool:** `sklearn.decomposition.PCA`

---

### Network Analysis of Cultural Knowledge Transmission
**Method:**
1. Survey who holds which ecological knowledge and who they learned it from
2. Build directed graph: nodes = people, edges = knowledge transmission
3. Compute betweenness centrality of knowledge holders
4. Model: what happens to the network when elders die or migrate?

**Anavaratha insight:** Cultural reservoir capacity is not stored in individuals — it's distributed across a social network. Network fragmentation IS cultural exergy loss, even if all individuals still live.

---

## Decision Framework

```
START: What is the data structure?

├── Time series
│   ├── Find trend direction      → STL decomposition
│   ├── Find when it changed      → PELT or BOCPD  
│   ├── Find unusual readings     → Isolation Forest / Z-score
│   └── Compare two series        → DTW

├── Spatial data
│   ├── Values clustering?         → Moran's I
│   ├── Find hot spots             → Getis-Ord Gi*
│   ├── Define drainage areas      → Watershed delineation
│   └── Summarise raster in zones  → Zonal statistics

├── Network data
│   ├── Critical nodes             → Betweenness centrality
│   ├── Tipping point              → Percolation analysis
│   └── Natural sub-systems        → Community detection

├── Survey / categorical
│   ├── Hidden structure           → PCA / clustering
│   ├── Test hypotheses            → t-test, ANOVA, chi-square
│   └── Build composite index      → PCA or weighted sum

└── Audio / image
    ├── Soundscape health           → ACI
    ├── Species from audio          → CNN classifier
    └── Visual ecology              → NDVI / Green View Index
```

---

## The Guiding Principle

> *Direction matters more than magnitude. A trend in the wrong direction at low confidence is more important than a precise measurement of something you already knew.*

Don't optimise for R² or accuracy. Optimise for: does this algorithm tell me which way things are moving and who is paying?

---

*Version 0.1 — evolves as methods are applied in the field*
*Part of the Anavaratha Data Infrastructure series*
