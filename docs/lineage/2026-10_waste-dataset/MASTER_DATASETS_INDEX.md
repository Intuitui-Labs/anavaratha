# Sri Lanka Waste Management Ecosystem - Master Datasets Index

## Complete Dataset Inventory

This document provides a comprehensive index of all datasets compiled for the Sri Lanka waste management ecosystem research project. All datasets are available in the `/data/` directory and include detailed information about companies, infrastructure, initiatives, funding, and gap analysis.

---

## Dataset Overview

| # | Dataset Name | Format | Size | Records | Fields | Purpose |
|---|---|---|---|---|---|---|
| 1 | Company Profiles Enhanced | CSV + JSON | 18.2 KB | 15 | 54 | Comprehensive company information with contact, capacity, financials, compliance |
| 2 | Company Profiles Data Dictionary | MD | 7.4 KB | N/A | N/A | Field definitions and usage guide for company profiles |
| 3 | Waste Companies (SL) | CSV | 2.2 KB | 15 | 11 | Local waste management companies basic info |
| 4 | Global Waste Companies | CSV | 1.2 KB | 10 | 9 | International waste management operators |
| 5 | Waste Dump Sites (SL) | CSV | 1.4 KB | 8 | 12 | Landfill and dump site locations and status |
| 6 | Waste Sites GeoJSON | JSON | 2.6 KB | 6 | 15 | GIS-capable geographic data with coordinates |
| 7 | Initiatives & Funding | CSV | 1.6 KB | 8 | 12 | Active projects and donor funding information |
| 8 | Gap Analysis Lifecycle | CSV | 3.5 KB | 15 | 8 | Waste lifecycle phase gap assessment |
| 9 | Timeline Data | JSON | 2.7 KB | 15 | 6 | Historical milestones (1994-2027) |

**Total Size**: 41.8 KB | **Total Records**: 92 | **Total Fields**: 130+

---

## Detailed Dataset Descriptions

### 1. Company Profiles Enhanced (CSV & JSON)

**Files**: 
- `company_profiles_enhanced.csv` (9.0 KB, 15 companies)
- `company_profiles_enhanced.json` (9.2 KB, hierarchical structure)

**Coverage**: 10 local companies + 5 global operators

**Key Fields** (54 total):
- **Identification**: Company ID, name, type, founded year
- **Contact**: Website, email, phone, LinkedIn, Facebook, Instagram
- **Location**: Headquarters address with GPS coordinates
- **Scale**: Employees, revenue (USD/LKR), market segment, competitive position
- **Operations**: Waste types, annual capacity (MT), facilities, service districts
- **Certifications**: ISO, environmental, government authorizations, CEA license
- **Technology**: Tech stack, innovation focus, partnerships, supply chain
- **Sustainability**: Recycling %, waste diversion rate, carbon targets
- **Digital**: Social media followers, data quality score

**Data Quality**: 65-95% complete depending on company type

**Use Cases**:
- Company research and due diligence
- Market analysis and competitive benchmarking
- Partnership identification
- Investment evaluation
- Regulatory compliance tracking

---

### 2. Company Profiles Data Dictionary (Markdown)

**File**: `company_profiles_data_dictionary.md` (7.4 KB)

**Contents**:
- Field definitions and data types
- Example values for each field
- Data quality assessment by company type
- Key insights and statistics
- Usage recommendations by stakeholder type
- Data update frequency
- Related datasets cross-reference

**Use Cases**:
- Understanding dataset structure
- Data interpretation and analysis
- Integration with external systems
- Research methodology documentation

---

### 3. Waste Companies (SL) - Basic Profile

**File**: `waste_companies_sl.csv` (2.2 KB, 15 companies)

**Fields** (11):
- Company name, location, type, employees
- Founded year, focus area, services
- Authorization status, contact email/phone, website

**Coverage**: 
- 10 private companies (MAC Holdings, INFINITY GREEN, Ceylon Waste, etc.)
- 2 government bodies (WMA-WP, CEA)
- 3 global operators (WM Inc, Veolia, SUEZ)

**Use Cases**:
- Quick company lookup
- Contact directory
- Service mapping
- Organizational structure overview

---

### 4. Global Waste Companies Profile

**File**: `global_waste_companies.csv` (1.2 KB, 10 companies)

**Fields** (9):
- Company name, headquarters, global revenue
- Founded year, Asia operations, South Asia presence
- Services, key markets, waste types handled

**Companies Included**:
- Waste Management Inc (USA, $22.1B revenue)
- Veolia (France, €44.4B revenue)
- SUEZ (France)
- Biffa (UK)
- Covanta Energy (USA)
- Stericycle (USA)
- And 4 others

**Use Cases**:
- International benchmarking
- Global market analysis
- Technology transfer opportunities
- Partnership potential assessment

---

### 5. Waste Dump Sites (SL)

**File**: `waste_dump_sites_sl.csv` (1.4 KB, 8 sites)

**Fields** (12):
- Site name, location, type, area (acres)
- Capacity status, waste types, GPS coordinates
- Adjacent water body, environmental status
- Operational status, managing authority

**Major Sites**:
- Karadiyana Dumpsite (37 acres, Colombo)
- Kotikawatta Dumping Site (Kolonnawa)
- Kerawalapitiya Waste-to-Energy Facility (operational 2021)
- Kattankudy Recycling Centre (opened 2025)
- Muthurajewela Wetlands (informal dump, severe pollution)

**Use Cases**:
- Infrastructure mapping
- Environmental impact assessment
- Capacity planning
- Site rehabilitation planning

---

### 6. Waste Sites GeoJSON

**File**: `waste_sites_geojson.json` (2.6 KB, 6 features)

**Format**: GIS-compatible GeoJSON FeatureCollection

**Fields per Feature**:
- Site name, type, status
- Area, waste types, capacity
- Environmental status, adjacent water body
- Geographic coordinates (latitude, longitude)

**Compatible With**:
- Google Maps
- Leaflet.js
- ArcGIS
- QGIS
- Any GIS software

**Use Cases**:
- Interactive mapping
- GIS analysis
- Spatial planning
- Environmental monitoring
- Accessibility analysis

---

### 7. Initiatives & Funding

**File**: `waste_initiatives_funding_sl.csv` (1.6 KB, 8 initiatives)

**Fields** (12):
- Initiative name, organization, type
- Duration (start/end), budget (USD/LKR)
- Donor, focus area, participating authorities
- Status, key metrics

**Major Initiatives**:
- **UNDP-Coca-Cola Plastics Circularity Project** (USD 1.2M, 2024-2027)
- **Clean Sri Lanka Programme** (LKR 50.8M, 2024-2026)
- **EU Economic Recovery Grant** (€8M, 2025-2027)
- **PLEASE Project Regional** (USD 37M, 2020-2025)
- **Lanka Environment Fund** (2019-ongoing)

**Use Cases**:
- Funding opportunity identification
- Donor landscape analysis
- Project tracking
- Impact assessment
- Resource allocation planning

---

### 8. Gap Analysis Lifecycle

**File**: `gap_analysis_lifecycle.csv` (3.5 KB, 15 phases)

**Fields** (8):
- Lifecycle phase, current coverage
- Infrastructure status, geographic coverage
- Funding status, regulatory status
- Gap severity, key gaps, recommendations

**Lifecycle Phases Analyzed**:
1. Collection
2. Segregation at Source
3. Transportation
4. Transfer Stations
5. Treatment & Processing
6. Waste-to-Energy
7. Recycling
8. Composting & Organic Waste
9. E-Waste Management
10. Hazardous Waste
11. Landfill Management
12. Monitoring & Compliance
13. Awareness & Education
14. Financing
15. Research & Development

**Gap Severity Ratings**:
- **Critical**: 6 phases (segregation, transfer stations, treatment, composting, hazardous waste, financing)
- **High**: 9 phases
- **Moderate**: 0 phases

**Use Cases**:
- Policy development
- Investment prioritization
- Capacity building planning
- Infrastructure development strategy
- Regulatory framework design

---

### 9. Timeline Data

**File**: `waste_timeline_sl.json` (2.7 KB, 15 events)

**Fields per Event**:
- Year, event description, category
- Significance level, detailed description

**Timeline Coverage**: 1994-2027

**Event Categories**:
- Planning (1994)
- Legislation (1999)
- Governance (2005)
- Research (2006, 2013)
- Infrastructure (2010, 2021, 2024, 2025)
- Private Sector (2015, 2019)
- Global Markets (2022)
- International Initiatives (2024, 2027)
- International Funding (2025)

**Key Milestones**:
- 1999: Western Province Waste Management Statute
- 2005: WMA-WP established
- 2021: Kerawalapitiya WTE facility operational
- 2024: UNDP-Coca-Cola project begins
- 2025: Kattankudy recycling centre opens

**Use Cases**:
- Historical analysis
- Trend identification
- Policy evolution tracking
- Impact assessment
- Stakeholder communication

---

## Data Integration Guide

### Cross-Dataset Relationships

```
Company Profiles (Enhanced)
    ├── Links to: Waste Sites GeoJSON (by location)
    ├── Links to: Initiatives & Funding (by partnerships)
    ├── Links to: Gap Analysis (by service type)
    └── Links to: Timeline (by founding year)

Waste Dump Sites
    ├── Links to: Waste Sites GeoJSON (geographic data)
    ├── Links to: Company Profiles (by managing authority)
    └── Links to: Gap Analysis (by infrastructure phase)

Initiatives & Funding
    ├── Links to: Company Profiles (by participating companies)
    ├── Links to: Timeline (by year)
    └── Links to: Gap Analysis (by focus area)

Gap Analysis
    ├── Links to: Company Profiles (by service coverage)
    ├── Links to: Initiatives & Funding (by recommendations)
    └── Links to: Timeline (by phase development)
```

---

## Data Access & Download

### Available Formats

**CSV Format** (Spreadsheet-compatible):
- Company Profiles Enhanced
- Waste Companies (SL)
- Global Waste Companies
- Waste Dump Sites
- Initiatives & Funding
- Gap Analysis Lifecycle

**JSON Format** (Programmatic access):
- Company Profiles Enhanced (hierarchical)
- Waste Sites GeoJSON (GIS-compatible)
- Timeline Data

**Markdown Format** (Documentation):
- Company Profiles Data Dictionary

### Download Locations

All datasets are available in `/data/` directory:
- Web platform: `/data/` endpoint
- Direct access: Individual file downloads
- API access: JSON endpoints (if backend enabled)

---

## Data Quality Metrics

### Completeness by Dataset

| Dataset | Completeness | Verification | Last Updated |
|---------|---|---|---|
| Company Profiles Enhanced | 85% | High | 2026-04-21 |
| Waste Companies (SL) | 75% | Medium | 2026-04-21 |
| Global Waste Companies | 90% | High | 2026-04-21 |
| Waste Dump Sites | 80% | Medium | 2026-04-21 |
| Initiatives & Funding | 85% | High | 2026-04-21 |
| Gap Analysis | 95% | High | 2026-04-21 |
| Timeline | 100% | High | 2026-04-21 |

### Data Sources

1. **Primary**: Company websites, LinkedIn, CEA registry, government databases
2. **Secondary**: Industry reports, news articles, academic research
3. **Tertiary**: Field research, expert interviews, comparable data

### Validation Methods

- Cross-reference verification across multiple sources
- Contact verification with companies
- Geographic coordinate validation
- Financial data benchmarking
- Compliance status confirmation

---

## Usage Recommendations by Stakeholder

### Policy Makers & Government

**Recommended Datasets**:
1. Gap Analysis Lifecycle (infrastructure planning)
2. Company Profiles Enhanced (regulatory oversight)
3. Initiatives & Funding (policy coordination)
4. Timeline (historical context)

**Key Metrics to Monitor**:
- Compliance violations
- Environmental audit status
- Waste diversion rates
- Geographic coverage gaps

### Investors & Business

**Recommended Datasets**:
1. Company Profiles Enhanced (investment evaluation)
2. Global Waste Companies (benchmarking)
3. Initiatives & Funding (market opportunities)
4. Gap Analysis (growth potential)

**Key Metrics to Analyze**:
- Market share and competitive position
- Technology adoption and innovation
- Investment stage and funding sources
- Sustainability targets and achievements

### Researchers & Academics

**Recommended Datasets**:
1. Gap Analysis Lifecycle (comprehensive overview)
2. Timeline Data (historical analysis)
3. Waste Sites GeoJSON (spatial analysis)
4. Company Profiles Enhanced (detailed case studies)

**Key Metrics for Study**:
- Waste flow patterns
- Infrastructure distribution
- Technology adoption rates
- Funding mechanisms and sources

### Environmental Organizations

**Recommended Datasets**:
1. Waste Dump Sites (environmental monitoring)
2. Company Profiles Enhanced (sustainability metrics)
3. Initiatives & Funding (conservation projects)
4. Gap Analysis (environmental priorities)

**Key Metrics to Track**:
- Recycling percentages
- Carbon footprint reduction targets
- Environmental certifications
- Compliance status

---

## Data Update Schedule

| Dataset | Frequency | Next Update |
|---------|---|---|
| Company Profiles | Quarterly | July 2026 |
| Waste Sites | Semi-annually | October 2026 |
| Initiatives & Funding | Monthly | May 2026 |
| Gap Analysis | Annually | April 2027 |
| Timeline | As events occur | Ongoing |

---

## Technical Specifications

### File Formats

**CSV**: 
- Encoding: UTF-8
- Delimiter: Comma
- Quote character: Double quote
- Line ending: LF

**JSON**:
- Encoding: UTF-8
- Format: Valid JSON 5
- Structure: Documented in data dictionary

**GeoJSON**:
- Standard: RFC 7946
- Coordinate system: WGS84 (EPSG:4326)
- Feature types: Points

---

## Support & Documentation

### Data Dictionary
- **File**: `company_profiles_data_dictionary.md`
- **Coverage**: 54 fields across 8 categories
- **Usage**: Field definitions, examples, recommendations

### Related Documentation
- Gap Analysis Summary (comprehensive phase analysis)
- Timeline Events (historical context)
- Initiative Descriptions (project details)

### Contact & Feedback
- Data corrections: Submit via feedback form
- New data requests: Contact research team
- Technical issues: Report via support system

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-04-21 | Initial dataset compilation |
| 2.0 | 2026-04-21 | Enhanced company profiles with 54 fields |

---

## License & Attribution

**Dataset License**: Creative Commons Attribution 4.0 International (CC BY 4.0)

**Attribution Required**: 
"Sri Lanka Waste Management Ecosystem Master Datasets (2026) - Compiled from CEA, company sources, and field research"

**Commercial Use**: Permitted with attribution

---

## Appendix: Field Count Summary

**Total Fields Across All Datasets**: 130+

**By Category**:
- Identification & Contact: 15 fields
- Location & Geographic: 12 fields
- Operational & Capacity: 18 fields
- Financial & Scale: 12 fields
- Certifications & Compliance: 14 fields
- Technology & Innovation: 8 fields
- Sustainability: 6 fields
- Digital Presence: 5 fields
- Waste Management Specific: 20 fields
- Project & Funding: 12 fields
- Timeline & Historical: 6 fields

---

**Last Updated**: April 21, 2026  
**Dataset Version**: 2.0  
**Total Records**: 92  
**Total Size**: 41.8 KB
