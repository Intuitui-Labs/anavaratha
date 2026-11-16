# ANAVARATHA — Visualisation Design Guide
## Making Invisible Flows Visible Across Multiple Audiences

> **The central principle:** A visualisation in Anavaratha is not decoration. It is symbolic technology — it creates categories that make witnessing possible. Wrong visualisation produces the same problem as wrong measurement: precise rendering of the wrong thing.

---

## Part 1: Design Philosophy

### The Visibility Gradient Problem in Visualisation

Every Anavaratha visualisation must ask the same three questions as the framework itself:
- Who *sees* this visualisation?
- Who *benefits* from what it reveals?
- Whose experience is *excluded* by its design?

A chart optimised for a Colombo policymaker may be illegible to the dry zone farmer whose land it describes. A participatory map drawn by community members may be unintelligible to international donors. The visibility gradient problem doesn't end with the data — it continues into the representation.

**Practical implication:** Design for *two audiences simultaneously* by using layered complexity — a simple headline reading that requires no background knowledge, with depth available for those who go further.

---

### The Five Visual Questions (matching Anavaratha's five modes)

| Mode | What to render visually | Visual form |
|---|---|---|
| **See it** | The flow itself — what's moving, where | Sankey, flow map, animated trace |
| **Name it** | What categories exist, what they're called | Legend, taxonomy diagram, concept map |
| **Map it** | Where things are in space and time | Geographic map, space-time cube |
| **Measure it** | How much, how fast, in what direction | Time series, gauge, bar/line chart |
| **Touch it** | Where intervention is possible | Leverage point map, decision tree |

---

## Part 2: Chart Type Selection

### When to use each chart type

#### Line Chart
**Use for:** Continuous change over time — reservoir levels, NDVI trends, air quality, economic indicators.

**Anavaratha rule:** Always show the *direction of concern* — add a reference line for baseline, a shaded region for acceptable range. The reader should immediately see whether the system is inside or outside safe territory.

**Avoid:** Multiple lines (>4) without clear hierarchy. For Sri Lankan water data with multiple stations, use small multiples instead.

---

#### Area Chart / Stacked Area
**Use for:** How composition of a whole changes over time — showing what fraction of total input is consumed output vs. dissipated vs. waste.

**Anavaratha's best use:** The central accounting identity visualised over time. Total material input area → divided into: formal GDP (one colour), informal economy (another), ecological services (another), dissipated/lost (red). The growing red area IS the story.

**Avoid:** More than 4 stacking categories. When order matters, put the most important layer at the bottom (it reads most accurately there).

---

#### Sankey Diagram
**Use for:** Flows between states — the Anavaratha accounting identity is inherently Sankey-shaped.

**Design rules:**
- Source nodes on left, sink nodes on right
- Width of flow = magnitude of energy/material
- Use colour to encode quality (high exergy = cool blue; degraded/waste = warm red/grey)
- Label the *unlabelled flows* — the dissipation that official accounts don't show. These should be visible but visually secondary to the labelled official output (until you want to invert the emphasis)

**Sri Lanka application:** Annual material flow for tea plantation economy: solar energy + rainfall + labour input → export revenue (narrow official ledger) + soil degradation + watershed disruption + estate worker health burden + atmospheric CO₂ (wide invisible output)

---

#### Choropleth Map
**Use for:** Value variation across geographic areas — district-level income, environmental exposure, reservoir condition.

**Anavaratha rule:** Use diverging colour scale when there's a meaningful midpoint (above/below national average, better/worse than baseline). Use sequential scale for pure magnitude (pollution concentration, deforestation rate).

**Critical caution:** Choropleth hides within-district variation. The estate sector within Badulla district is not represented by Badulla's district average. Always note this limitation explicitly.

**Better alternative for displacement zones:** Dot density maps or graduated circles that can show sub-district variation.

---

#### Small Multiples
**Use for:** Comparing the same pattern across multiple entities — all 25 districts, all major tank cascades, all ecological domains.

**Why this fits Anavaratha:** Small multiples are the visual equivalent of holarchic thinking — each unit complete in itself, comparable to all others, nested in a shared frame.

**Design rule:** Same scale, same axes, same visual encoding across all panels. The reader's eye compares position and shape — don't make them decode a legend for each panel.

---

#### Gauge / Indicator
**Use for:** Current status of a specific reservoir against a threshold — the early warning function.

**Design:** Three zones: green (functioning), amber (eroding), red (critical). The threshold between zones should be explicitly defined and justified — not arbitrary colour choice.

**Anavaratha application:** Pressure Reservoir Dashboard. One gauge per domain:
- Tank cascade storage: current vs. historical average
- Dry zone soundscape ACI: current vs. undisturbed baseline
- SOC in estate soil: current vs. 1950 baseline
- National Red List trend: improving / stable / declining

---

#### Network Graph
**Use for:** Connectivity, relationships, flow topology — the cascade system's native visual language.

**Design rules:**
- Node size = centrality (more central nodes appear larger)
- Edge width = flow magnitude or relationship strength
- Colour = status (functioning nodes green, degraded amber, failed red)
- Layout: force-directed for organic network topology; hierarchical for cascade flow direction

**Anavaratha application:** Dry zone tank cascade — nodes are tanks, edges are flow pathways. Silted tanks in red. Critical connector tanks (high betweenness) shown larger. The visual immediately reveals which tanks, if restored, would reconnect most of the network.

---

#### Spectrogram / Waveform Visualisation
**Use for:** Soundscape data — making the acoustic environment visible.

**Design:** Time on x-axis, frequency on y-axis, intensity as colour (dark = loud, light = quiet). Biophonic frequencies (birdsong, insect chorus, rain) vs. technophonic frequencies (engine noise, construction) visible as distinct horizontal bands.

**Anavaratha application:** Place Sinharaja dawn spectrogram beside Colombo rush hour spectrogram beside dry zone village evening. The visual difference IS the sensory carrying capacity difference, rendered visible to someone who has never heard either place.

---

## Part 3: Colour Design

### Anavaratha Colour Philosophy

Colour in Anavaratha is not decorative. It carries semantic meaning that should be consistent across all visualisations.

| Meaning | Colour | Hex | Usage |
|---|---|---|---|
| High exergy / functioning reservoir | Deep teal | `#1A7A7A` | Healthy ecosystems, functioning tanks, intact soundscapes |
| Moderate pressure / caution | Warm amber | `#E6A817` | Degrading but recoverable systems |
| Critical / stolen time | Deep red | `#C0392B` | Collapse, irreversible loss, displacement zones |
| Invisible / unaccounted | Mid grey | `#7F8C8D` | Dissipation not in official ledger |
| Official economy / formal | Navy | `#2C3E70` | What GDP counts |
| Natural / ecological flows | Soft green | `#2E8B57` | Ecosystem services, biomass, ecological processes |
| Human / cultural layer | Warm ochre | `#B8860B` | Cultural reservoirs, human exergy, care networks |

**Rule:** Use diverging palettes (teal → white → red) for change (getting better / getting worse). Use sequential palettes (white → deep colour) for magnitude only.

**Accessibility:** Always test colour combinations for colour-blind readability. Use `colorbrewer2.org` — all palettes are tested for accessibility.

---

## Part 4: Typography and Hierarchy

### For mixed-audience documents

**Headline layer (no background required):**
- One sentence summary of what this visualisation shows
- Should work for someone with zero context
- Example: *"Sri Lanka's dry zone tanks lost 23% of average water storage between 1990 and 2022"*

**Annotation layer (some context required):**
- Key data points labelled directly on the chart
- Specific threshold crossings named
- Example: *"2022 economic crisis"* annotated on nighttime lights chart

**Detail layer (for collaborators):**
- Methodology note
- Data source citation
- Known limitations
- Example: *"Water level data from Irrigation Dept — village tanks not included"*

---

## Part 5: Scrollytelling Structure

For narrative visualisations that walk a reader through an Anavaratha story:

### The arc of an Anavaratha scrollytelling piece

**Act 1: The official account**
Show what the formal ledger says — GDP, forest cover (according to government), air quality at the one Colombo station. Make it look normal.

**Act 2: What's missing**
Begin revealing the unaccounted flows. The informal economy. The ecosystem services. The silence degrading. Each scroll reveals another invisible layer.

**Act 3: The gap**
Show the gap between total input and official output. This IS the theft. Render it visually — a growing space between two lines, a widening crack.

**Act 4: The reservoir**
Show which reservoirs are absorbing the gap — tanks silting, communities bearing cost, cultural memory eroding.

**Act 5: The direction**
Not a solution. A direction. Where are the leverage points? What would slowing the dissipation look like? Leave the decisions where they belong — with the people.

### Tools
- `Scrollama.js` — scroll-triggered transitions (JavaScript)
- `Flourish` — no-code scrollytelling with maps and charts
- `Quarto` with `revealjs` — code-integrated scrollytelling for technical audiences

---

## Part 6: Participatory Visualisation Principles

When the visualisation is made *with* communities rather than *for* them:

### What changes
- The community defines the categories (naming comes before mapping)
- Visual language is locally legible, not globally standardised
- The output is owned by the community, not the researcher
- Incompleteness is acceptable — a partial map made with the community is worth more than a complete map made without them

### Methods
**Participatory mapping on paper first**
Before any digital tool, use large paper maps. Community members draw their own pressure reservoirs — which tanks they trust, which forests they use, which soundscapes matter to them. These hand-drawn maps often reveal what satellite data cannot.

**Photovoice**
Community members photograph what they see as ecological pressure and reservoir erosion. The photos become data; the captions become category names. Qualitative, powerful, politically significant.

**Seasonal calendars**
Community-drawn calendars showing ecological cycles — when fish used to run, when the forest was quiet, when rituals occurred. Time-depth that no sensor can provide.

**Digital layer (only after)**
Once categories are established participatorily, digitise them. Use `Felt.com` — drag and drop, shareable link, no GIS expertise needed.

---

## Part 7: Dashboard Design for the Reservoir Monitoring Function

The early detection function of Anavaratha requires an always-on dashboard view.

### Hierarchy of panels

**Level 1: Reservoir status (high-level)**
One indicator per major pressure reservoir. Colour-coded. Updates when new data arrives. Visible at a glance.

**Level 2: Domain trends (medium detail)**
Time series for each ecological domain over 5–10 years. Trend direction visible immediately.

**Level 3: Geographic view (spatial)**
Map of Sri Lanka showing which districts/cascades are in which status zone.

**Level 4: Data provenance**
When each data source was last updated. Where data is missing. The gap is information.

### Technology stack for the dashboard
`Streamlit` (Python) deployed free on Streamlit Community Cloud. Data from DuckDB + Parquet files updated via GitHub Actions. No server, no cost, fully open source.

---

## Quick Reference: Visualisation Decision Tree

```
What is the primary message?

├── Change over time → LINE CHART or AREA CHART
│   └── Multiple entities changing → SMALL MULTIPLES
│
├── Flow from one thing to another → SANKEY DIAGRAM
│   └── Flow across geography → FLOW MAP (Kepler.gl)
│
├── Distribution across space → CHOROPLETH or GRADUATED CIRCLES
│   └── With relationships between places → NETWORK MAP
│
├── Part-to-whole → PIE (if ≤4 parts) or STACKED BAR
│
├── Status against threshold → GAUGE / INDICATOR
│
├── Relationships and connectivity → NETWORK GRAPH
│
├── Sound/audio data → SPECTROGRAM
│
└── Narrative journey → SCROLLYTELLING
```

---

## The Governing Principle

> *The best Anavaratha visualisation is one that a person could not unsee — that makes a previously invisible flow so legible that looking away requires effort.*

Not beautiful for its own sake. Not complex for credibility. Legible for the specific person who needs to act, in the form they can receive.

---

*Version 0.1 — evolves as the visualisation practice develops*
*Part of the Anavaratha Data Infrastructure series*
