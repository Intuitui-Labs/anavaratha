# ANAVARATHA — ML Model Types Guide
## Choosing the Right Model for the Right Ecological Question

> **How to use this guide:** Every ML model answers a specific *type of question*. Anavaratha's questions are about flows, thresholds, asymmetries, and reservoir erosion. This guide maps those questions to model families — not abstractly, but concretely for Sri Lankan ecological and human exergy data.

---

## The Fundamental Question Before Any Model

Before choosing a model, ask:

> *What kind of answer does Anavaratha need here?*

| If you need to know... | The question type is... | Model family |
|---|---|---|
| Is this getting better or worse? | Trend / direction | Time series analysis |
| Has something irreversibly changed? | Structural break | Changepoint detection |
| Is this unusual? | Anomaly | Anomaly detection |
| Which category does this belong to? | Label | Classification |
| What value will this be? | Number | Regression |
| What patterns exist without prior labels? | Structure | Clustering / unsupervised |
| What caused what? | Mechanism | Causal inference |
| How connected are things? | Topology | Graph / network models |

The most common mistake: reaching for prediction when what you need is detection. Anavaratha rarely needs to *predict* the future — it needs to *detect the present* that official accounts are missing.

---

## 1. Time Series Models
*For data that changes over time — reservoir levels, NDVI, air quality, nighttime lights, HIES income trends*

### What it does
Decomposes a signal into trend + seasonality + residual. Reveals whether something is improving, declining, or oscillating within a range.

### When to use in Anavaratha
- Tank water levels over decades → is the reservoir actually silting?
- NDVI in estate plantation zones → is soil-supporting vegetation declining?
- Nighttime lights 2015–2024 → where did the 2022 crisis land hardest?
- Air quality trend at Colombo Fort station → is urban air entropy accelerating?

### Model options (conceptual)

**LOESS / Seasonal Decomposition (STL)**
Simple, interpretable. Separates trend from monsoon seasonality. Good first step for any Sri Lankan ecological time series — because everything in LK has strong seasonal signal (Yala/Maha cycles, NE/SW monsoon).

**Prophet (Facebook)**
Handles missing data, irregular holidays, multiple seasonality. Ideal for government data that has gaps (CEA monitoring stops and starts). Produces confidence intervals — honest about uncertainty.

**ARIMA / SARIMA**
Classical. Good for stationary-ish series. Requires more data than Prophet. Use when you have long, complete time series (GRDC river discharge, CBSL economic data going back decades).

**When NOT to use:** When you have fewer than ~50 time points, or when you care more about *when* something changed than the trend itself (use changepoint detection instead).

### Sri Lanka specifics
Sri Lankan ecological data has two dominant seasonal patterns: the **southwest monsoon (May–September)** affecting wet zone, and the **northeast monsoon (October–January)** affecting dry zone. Any time series model must account for both, or it will confuse seasonal dips with actual decline.

---

## 2. Changepoint Detection
*For detecting when a system irreversibly crossed a threshold*

### What it does
Scans a time series for moments where the statistical properties fundamentally shift — mean changes, variance changes, trend direction reverses. Finds the moment the system changed, not just that it changed.

### When to use in Anavaratha
This is perhaps the most important model family for Anavaratha. The core insight — *collapse often begins with reservoir erosion, not visible damage* — is exactly what changepoint detection reveals: the invisible threshold crossing before the visible collapse.

- **Kelani River BOD (water quality)** → when did pollution cross from manageable to chronic?
- **Nighttime lights** → precise date of 2022 crisis impact by district
- **Forest cover** → when did deforestation in a specific watershed accelerate?
- **HIES income data** → when did estate sector income diverge from national trend?
- **Tank water levels** → when did a cascade system stop recovering between monsoons?

### Model options

**PELT (Pruned Exact Linear Time) — via `ruptures` Python library**
Fast, handles multiple changepoints, works with any cost function. Best general-purpose changepoint detector. Start here.

**BOCPD (Bayesian Online Changepoint Detection)**
Probabilistic. Gives probability of changepoint at each timestep. Better when you want uncertainty quantified — important when making claims about ecological thresholds.

**Structural Break Tests (Chow test, Bai-Perron)**
Classical econometric approach. Good for economic time series (CBSL data). Produces p-values familiar to policy audiences.

### Sri Lanka specifics
The 2022 collapse is a known changepoint — use it as a validation case before applying to ecological data. If your model correctly detects April 2022 in CBSL data, it's working. Then apply to environmental data to find *when ecological thresholds were crossed before the economic crisis became visible*.

---

## 3. Anomaly Detection
*For flagging unusual observations that don't fit the pattern — early warning signals*

### What it does
Learns the normal behaviour of a system and flags deviations. Unlike changepoints (permanent shifts), anomalies are transient unusual events.

### When to use in Anavaratha
- Air quality spike events (MV X-Press Pearl chemical contamination, 2021)
- Unusual tank level drop outside monsoon cycle → possible illegal extraction
- Species count anomalies in eBird data → population crash signal
- Nighttime light anomaly in a specific district → localised crisis

### Model options

**Isolation Forest**
Unsupervised. Works well with tabular ecological data. Doesn't need labelled anomalies to learn from. Good for multi-variable anomaly detection (water quality with multiple parameters).

**LSTM Autoencoder**
Learns normal sequence patterns, flags sequences that don't compress well. More powerful for time series anomalies — but needs more data. Use when you have at least 2–3 years of regular readings.

**Statistical methods (Z-score, IQR, MAD)**
Simple and interpretable. Often sufficient for Anavaratha's sparse data reality. A reading 3 standard deviations from the seasonal mean is almost always worth investigating.

**When to prefer simple over complex:** Anavaratha's Sri Lankan data is often sparse and irregular. A simple statistical threshold will outperform a complex neural network when you have only 12–24 monthly readings. Complexity requires data. Start simple.

---

## 4. Classification Models
*For assigning categories — reservoir health status, land use type, threat level*

### What it does
Learns from labelled examples to assign new observations to categories.

### When to use in Anavaratha
- Classify satellite pixels as: forest / degraded forest / agriculture / bare soil (land use mapping)
- Classify tank cascade condition as: functioning / degraded / failed (if field survey labels exist)
- Classify community knowledge vitality as: high / medium / eroding / lost
- Classify bird call recordings as species (bioacoustic identification)

### Model options

**Random Forest**
Robust, interpretable (feature importance), handles mixed data types (numerical + categorical). Good for ecological classification where you have field survey labels. First choice for most Anavaratha classification tasks.

**XGBoost / LightGBM**
More powerful than Random Forest when you have enough data. Better for tabular data competitions. Use when you need maximum accuracy on structured ecological datasets.

**Convolutional Neural Networks (CNN)**
For image data — satellite imagery classification, spectrogram classification (bird species from audio). Requires substantial labelled training data. Partner with University of Peradeniya or DWC for existing labelled datasets.

**Support Vector Machine (SVM)**
Works well with small datasets and clear decision boundaries. Sometimes the right choice when you have few field survey samples (common in Sri Lankan ecological research).

### Sri Lanka specifics
Labelled training data is scarce. Leverage existing datasets: IUCN Red List assessments, DWC protected area wildlife surveys, National Red List species assessments. These are labelled ecological data — potentially usable as training sets.

---

## 5. Clustering / Unsupervised Models
*For finding structure in data without pre-existing labels*

### What it does
Groups observations by similarity, revealing natural structure that official categories may obscure.

### When to use in Anavaratha
This is where the visibility gradient becomes computational. Clustering reveals groupings that the official accounting doesn't see.

- **Cluster Sri Lankan districts** by combined ecological pressure profile (air + water + soil + sound) → reveals which districts are true displacement zones regardless of official categorisation
- **Cluster tank cascade systems** by hydrological behaviour → which cascades are most connected? Most vulnerable?
- **Cluster HIES household expenditure patterns** × CEA pollution exposure → does environmental cost cluster with poverty?
- **Cluster species by threat trajectory** → which groups of species are declining together? What ecological process connects them?

### Model options

**K-Means**
Simple, fast, interpretable. Use when you want a fixed number of groups and data is roughly spherical in distribution. Start here for district-level ecological profiling.

**DBSCAN**
Finds clusters of arbitrary shape, identifies outliers as their own category. Better for spatial clustering (tank locations, species occurrence) where clusters aren't round. Handles the irregular geography of Sri Lanka's ecological zones.

**Hierarchical Clustering**
Produces a dendrogram — a tree of similarity. Good when you want to see the whole spectrum of similarity, not just discrete groups. Useful for comparing dry zone cascade systems at multiple scales.

**UMAP / t-SNE**
Dimensionality reduction for visualisation — compress high-dimensional ecological data into 2D to see structure. Use for exploring multi-domain datasets before formal analysis.

---

## 6. Regression Models
*For estimating magnitudes — how much? how fast?*

### What it does
Predicts a continuous value from input features. In Anavaratha, more often used for *attribution* than prediction — understanding what drives the magnitude of a flow or reservoir condition.

### When to use in Anavaratha
- What predicts SOC (soil organic carbon) loss rate in estate regions? (rainfall? slope? crop type?)
- What predicts nighttime light level by district? (economic activity? electricity access? governance?)
- What drives HIES income inequality by district? Does environmental degradation correlate?
- How much tank water storage can be predicted from satellite NDVI of the catchment?

### Model options

**Linear / Ridge / Lasso Regression**
Start here. Interpretable coefficients — each variable's contribution is readable. Lasso performs feature selection (identifies which variables matter). Good for Anavaratha because *direction* matters more than precision.

**Gradient Boosting Regression (XGBoost)**
When relationships are non-linear and you have reasonable data. Feature importance plots reveal which ecological variables drive outcomes — a form of witnessing.

**Geographically Weighted Regression (GWR)**
Fits separate regression coefficients for each location. Reveals that the same variable (say, rainfall) has different relationships to soil erosion in the wet zone vs. dry zone. Critical for Sri Lanka's highly variable geography.

---

## 7. Causal Inference Models
*For understanding mechanism — not just correlation but direction of causation*

### What it does
Distinguishes correlation from causation. Essential for Anavaratha's asymmetry mapping — not just that poverty and pollution co-occur, but that pollution is imposed on communities that didn't choose it.

### When to use in Anavaratha
- Did colonial land tenure disruption *cause* cascade system degradation? (Difference-in-differences using historical maps)
- Does nighttime light reduction *cause* downstream ecological improvement, or do both respond to a common cause?
- Does estate sector income inequality *cause* lower soil stewardship, or is it the other way?

### Model options

**Difference-in-Differences (DiD)**
Compares change in treated vs. untreated groups before and after an intervention. Classic quasi-experimental design. Could apply to tank restoration programmes — did restored cascades perform differently?

**Granger Causality**
Tests whether one time series predicts another beyond its own past. Does air quality Granger-cause health complaint rates in Colombo? Does elephant corridor fragmentation Granger-cause HEC incidents?

**Propensity Score Matching**
Matches similar units that received different treatments. Useful for comparing estate districts vs. similar non-estate districts on ecological outcomes.

**Note:** Causal inference is hard with observational data. Be honest about limitations. Anavaratha's boundary ethic — *the framework reveals, it does not prescribe* — applies here. Causal evidence supports witnessing; it doesn't determine local decisions.

---

## 8. Graph / Network Models
*For understanding connectivity and flow topology — the cascade system's native language*

### What it does
Treats entities as nodes and relationships as edges. Computes connectivity, centrality, vulnerability.

### When to use in Anavaratha
The tank cascade system is literally a network — this is perhaps the most natural model family for Anavaratha's core Sri Lankan subject.

- **Model the cascade as a graph** — tanks are nodes, water flow paths are edges. Compute: which tanks are most central? Which, if removed (silted or broken), would fragment the cascade most?
- **Map elephant corridors as a network** — which corridor segments are bottlenecks?
- **Map cultural knowledge networks** — which community members hold most ecological knowledge? What happens when they are lost?
- **Map trade flow asymmetries** — directed graph of who exports entropy to whom

### Model options

**NetworkX (Python)**
Full-featured graph analysis library. Compute: degree centrality, betweenness centrality, connected components, shortest paths, community detection. Free, open source, well-documented.

**Graph Neural Networks (GNNs)**
For learning on graph-structured data when you have labels. Advanced — only relevant when cascade network data is rich enough. Future horizon for Anavaratha.

**Key metrics for cascade analysis:**
- *Betweenness centrality* — which tank most controls flow through the system?
- *Connected components* — how many isolated fragments does the cascade split into if key links are removed?
- *Percolation threshold* — at what fraction of tank failures does the cascade become non-functional?

---

## Quick Reference: Question → Model

| Anavaratha Question | Model Family | Specific Tool |
|---|---|---|
| Is this reservoir silting over decades? | Time series | STL decomposition + Prophet |
| When did this system cross a threshold? | Changepoint detection | PELT (ruptures) |
| Is this reading anomalous? | Anomaly detection | Isolation Forest / Z-score |
| What land use type is this pixel? | Classification | Random Forest / CNN |
| Which districts share ecological pressure profiles? | Clustering | K-Means / DBSCAN |
| What drives soil erosion rates? | Regression | GWR (geographically weighted) |
| Did restoration actually cause improvement? | Causal inference | Difference-in-Differences |
| Which tank is most critical to the cascade? | Network analysis | Betweenness centrality (NetworkX) |
| What is the soundscape health of this site? | Signal processing | Acoustic Complexity Index (librosa) |

---

## A Note on Data Poverty and Model Humility

Sri Lankan ecological data is sparse. The most important question for many Anavaratha domains isn't *which model to use* but *do we have enough data for any model at all?*

**When data is sparse:**
- Prefer simple models (linear regression > neural networks)
- Prefer interpretable models (Random Forest > black-box ensembles)
- Quantify uncertainty explicitly (Prophet's confidence intervals > point predictions)
- Use proxy data honestly (VOC as olfactory proxy, NDVI as visual greenness proxy)
- Document gaps as data (the absence of soundscape monitoring is itself information)

The framework's incompleteness clause applies to models too. A model that honestly says "I don't know" is more valuable than one that confidently says the wrong thing.

---

*Version 0.1 — evolves as data grows*
*Part of the Anavaratha Data Infrastructure series*
