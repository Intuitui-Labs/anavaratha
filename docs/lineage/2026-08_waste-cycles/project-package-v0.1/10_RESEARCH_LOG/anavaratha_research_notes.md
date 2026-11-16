
## Real-data exploration: Sri Lanka 2024 Census denominators

Source: Sri Lanka Department of Census and Statistics, Census of Population and Housing 2024, Grama Niladhari Division population, household, and occupied-housing Excel tables: https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024

Retrieved real files: `CPH2024_GN_population.xlsx`, `CPH2024_GN_households.xlsx`, and `CPH2024_GN_occupied_housing.xlsx`. The population workbook contains 14,014 rows including headers and 17 columns; the household workbook contains GN-level household counts and water, cooking-fuel, lighting, and toilet variables; the occupied-housing workbook contains 14,013 rows including headers and 51 columns.

The GN-level records were aggregated to 25 districts. The sums from the retrieved provisional tables are: population 21,781,800; households 6,111,315; occupied housing units 6,030,541. The ten largest districts by population in the aggregation are Gampaha 2,436,142; Colombo 2,375,415; Kurunegala 1,768,156; Kandy 1,461,895; Kalutara 1,305,784; Ratnapura 1,145,423; Galle 1,097,372; Anuradhapura 960,080; Badulla 872,307; and Kegalle 870,476.

Province totals from the same aggregation are: Western 6,117,341; Central 2,714,045; Southern 2,606,679; North Western 2,586,972; Sabaragamuwa 2,015,899; Eastern 1,783,214; North Central 1,407,610; Uva 1,399,892; and Northern 1,150,148.

Derived persons per household across districts average approximately 3.58, with a district range from approximately 3.46 to 3.83. This is a denominator description, not a waste-generation estimate. The tables are marked provisional on the DCS portal, so any published analysis must retain that status.

Chart review: the province and top-ten-district charts render legibly with clear titles, axis labels, and value annotations. They are appropriate for a denominator overview but do not imply waste pressure, capacity, or service performance.

## Census integrity audit

The 2024 GN population and household tables each contain 14,009 post-header rows, with 14,008 non-null value rows, 25 districts, 340 DS divisions, and one blank/missing value tail row. The occupied-housing table contains 14,008 post-header rows and 14,008 non-null value rows. District-level aggregation is therefore appropriate for denominator analysis, but GN-level keys must retain the DS-division code because 16 apparent duplicate GN code/name combinations occur across different DS divisions. These are not automatically duplicate records; the same GN label/code can recur in separate DS divisions.

All 25 districts have more households than occupied housing units in the downloaded tables. This is a consistency diagnostic rather than an error judgment because the datasets measure different concepts. The derived persons-per-household range is approximately 3.46–3.83 across districts.

The official source labels the census tables provisional. The real-data workflow should preserve that status, cite the original workbook URLs, and avoid treating the population totals as final without checking for later revisions.

## Real-data exploration: World Bank What a Waste 3.0

Source: World Bank Data360, “What a Waste (3.0),” https://data360.worldbank.org/en/dataset/WB_WAW. The portal states that the dataset covers 217 economies, 262 cities, 11 indicators, and years 1994–2050. It includes waste generation, composition, collection, treatment/disposal, legal and institutional arrangements, plastics management, and related indicators. The portal provides wide-format CSV, SDMX CSV, data dictionary, metadata JSON, and PDF links.

The wide-format CSV was retrieved and resumed successfully after an initial truncation. It contains 7,858 rows and 7044661 bytes according to the portal header. A targeted extraction for Sri Lanka produced a long-format file `WB_WAW_Sri_Lanka_long.csv`. The dataset includes categorical observations for plastic policy/legislation, EPR systems, and legal/institutional arrangements, plus projected MSW generation observations for 2030, 2040, and 2050. The extracted projected values include 2030: 3,155,836.83 tonnes/year and 0.364513 kg/person/day; 2040: 3,797,570.69 tonnes/year and 0.424669 kg/person/day; 2050: 4,362,359.86 tonnes/year and 0.481686 kg/person/day.

Important audit point: the Sri Lanka extraction also contains multiple rows for the same indicator and year because the data structure includes different urbanization, population-group, waste-product, treatment, or source dimensions. These rows must be filtered and deduplicated using the full metadata columns before any trend or comparison is calculated. The projected values are model outputs in the World Bank dataset, not direct 2024 measurements, and must remain labeled as projections.

Source portal note: the portal states that data quality and definitions vary across individual data points and that sources and estimations are noted. Anavaratha must preserve source metadata and should not merge these observations directly with the DCS census denominators until reference periods and population bases are reconciled.

## What a Waste 3.0 capacity/action-side observations

The raw Sri Lanka subset contains 38 source rows across 9 indicators. It includes 28 numeric rows and 14 categorical rows after long-format expansion. The indicators are not a local-authority capacity inventory; they are national, source-specific measures with different reference years.

Management-side numeric rows include: 2021 MSW collection coverage of 47.35%; 2016 treatment/disposal shares of 52.65% uncollected, 24.81% open dump, 13.88% composting, 8.60% incineration, and 0.06% sanitary landfill; and 2012 management of uncollected MSW of 59.402% open burned, 29.353% dumped on land, 9.713% recycled or composted, 1.11% aquatic environment, and 0.425% other. The 2018 composition rows are food 62%, other 17%, paper/cardboard 7%, plastic 6%, wood 6%, and glass 2%. Non-municipal e-waste generation is listed as 175,000 tonnes/year in 2022.

Categorical action/institutional rows include observations related to legal and institutional arrangements, national plastic policy/legislation by upstream/midstream/downstream stage, and EPR systems. These are categorical status observations, not performance measures.

The management chart was visually reviewed and is legible. It explicitly labels the 2021, 2016, and 2012 reference years and notes that the panels have different denominators and must not be read as one current time series.

## Capacity and action-side evidence: Sri Lanka biodiversity/plastic issue brief

Source: GRID-Arendal, “Addressing biodiversity conservation and plastic pollution in Sri Lanka: Integrating and strengthening policies and actions,” 2024: https://gridarendal-website-live.s3.amazonaws.com/production/documents/:s_document/1626/original/SriLanka_brief_final_25.11.24.pdf?1732608731

The brief collates production, trade, consumption, waste-management, and leakage data using a material-flow approach, and integrates national, regional, and district spatial data with Key Biodiversity Areas. It reports, based on CEA communications and cited sources, more than 750 companies processing more than 450,000 metric tonnes of imported plastic precursors, additives, primary and/or intermediate forms annually. It estimates Sri Lankan plastic waste at 0.02–0.04 kg per capita per day, while cautioning that the quantities do not account for transboundary sources. These figures are source-specific and must not be mixed directly with the World Bank MSW series.

The brief’s field observations identify uneven infrastructure and technical competence, lack of maintenance and mismanagement due to funding and capacity limits, occasional but poorly maintained leachate infrastructure, lack of sewage and grey-water treatment, poor sorting that mixes biodegradable, plastic, and medical waste, low-quality compost and weak market trust, low prices for mixed plastics, limited OHS measures, weak coordination, and enforcement gaps. It emphasizes that performance varies by region and that tailored solutions are required.

The brief describes an action architecture including stronger waste-site infrastructure and wildlife barriers, regular financial audits, compost-quality standards, local-authority incentives, private-sector data sharing, stronger education and sorting, by-laws for segregation, enforcement of plastic bans, protocols for biomedical and hazardous waste, more localized systems, stronger EPR with yearly targets, centralized MSW/plastics databases, clear LA roles, biodiversity-impact data, sustainable financing through EPR/PPP/PES and park fees, and public-private maintenance of balers, conveyors, sorting machines, and compost sieves.

Implication: the action side must track not only whether projects or facilities exist, but whether they are funded, maintained, operated, enforced, monitored, and linked to measurable outcomes and ecological receptors.

## Waste law and enforcement evidence

### Open-burning regulation
Source: Gazette Extraordinary No. 2034/36, National Environmental (Prohibition of open burning of refuse and other combustible matters inclusive of plastics) Regulations No. 1 of 2017, official Environment Ministry PDF: http://env.gov.lk/web/images/downloads/legal_division/waste_management/2034_36_E.pdf

The regulation, made under the National Environmental Act No. 47 of 1980, states that no person shall burn openly or cause, allow, or permit the open burning of refuse or other combustible matters inclusive of plastics. Non-compliance is an offence punishable under Section 31 of the National Environmental Act.

FAOLEX/UNEP confirms the regulation date as 1 September 2017, says it has not been repealed, and identifies the National Environmental Act as its implementing law: https://leap.unep.org/en/countries/lk/national-legislation/national-environmental-prohibition-open-burning-refuse-and-other

### Meethotamulla Supreme Court case
Source: Asian Development Bank Law and Policy Reform database, “Judgment in the Meethotamulla Garbage Dump Case (SC/FR 311/2015 and 318/2015), Sri Lanka,” 31 March 2026: https://lpr.adb.org/resource/judgment-meethotamulla-garbage-dump-case-scfr-3112015-and-3182015-sri-lanka

The case concerns residents challenging continuous municipal dumping at Pothuvil Kumbura in Colombo, the 2017 collapse of the garbage mound, and 40 deaths. The case summary reports that the Court defined proper disposal as timely, regular, comprehensive, lawful, and ethical discarding at an appropriate location, with separation, cleaning and reuse, recycling, composting, environmentally safe energy recovery, or sanitary landfilling for non-convertible components. It reports the Court’s conclusion that unlawful dumping between 2009 and 2017 represented failure to enforce the National Environmental Act and violated Article 12(1) equal-protection rights.

Implication: the case is a strong law–capacity–reality anchor. It shows that formal legal duties can coexist with prolonged operational failure and severe burden concentration. It should be analyzed as evidence about institutional accountability and capacity, not only as a pollution event.

## National Environmental Act: institutional capacity and enforcement powers

Sources: Sri Lanka Law, “National Environmental Act,” https://www.srilankalaw.lk/n/772-national-environmental-act.html; LankaLaw text version, https://lankalaw.net/wp-content/uploads/2025/02/1980Y0V0C47A.html; official Environment Ministry Acts page, https://env.gov.lk/web/index.php/en/downloads/acts

The Act establishes the Central Environmental Authority, an Environmental Council, and District Environmental Agencies. It provides for the CEA’s powers and duties to administer the Act and regulations, conduct pollution surveys and research, set environmental standards, coordinate regulatory activities, regulate waste discharges/emissions/deposits, publish information, investigate and inspect for compliance, investigate complaints, educate the public, promote long-range environmental planning, and encourage conversion and use of residues.

Section 10(1)(i) gives the Authority power to require local authorities to comply with recommendations relating to environmental protection, including prohibition of unauthorized discharge, emission, or deposit of litter, waste, garbage, and sewage; prevention of untreated sewage or substandard industrial effluents or toxic chemicals entering soil, canals, or waterways; atmosphere and noise controls; and storage, transport, and disposal of hazardous materials. Section 12 allows the Authority, with ministerial concurrence, to give written directions to local authorities to safeguard and protect the environment, and requires the local authority to comply.

The legal text also provides for the Authority’s Fund, annual accounts and reporting, appointment of officers and servants, and delegation. These provisions are important for Anavaratha because legal authority and formal institutional design do not demonstrate that the personnel, budget, inspection frequency, evidence chain, local coordination, and follow-through needed for enforcement actually exist.

The official Environment Ministry acts page was current as of 21 August 2026 but exposed little text through extraction; the official open-burning Gazette remains the primary retrieved legal PDF for that regulation.

## National Environmental Act penalties and soil-disposal provisions

Local copy retrieved from LankaLaw: `National_Environmental_Act_1980.html`.

Section 23M states that, subject to section 23A, no person shall discharge or deposit waste into soil except according to prescribed standards or criteria. Section 23N(1) prohibits pollution or causing/permitting pollution of soil or land surface where the condition becomes or may become harmful to people, animals, wildlife, plants, life, or beneficial land use. Section 23N(2)(b) expressly includes establishing a refuse dump, garbage tip, soil/rock disposal site, sludge deposit site, waste injection well, or otherwise using land for solid or liquid waste where it is obnoxious, may pollute underground water, or may harm beneficial soil/land use. Section 23N(4) provides a fine of not less than LKR 10,000 and not exceeding LKR 100,000, plus LKR 500 for every day a continuing offence continues after conviction.

Section 31 provides a default penalty for contravening an Act provision or regulation where no punishment is expressly provided: on conviction before a Magistrate, imprisonment up to two years, a fine up to LKR 10,000, or both. The 2017 open-burning regulation invokes section 31, so the exact applicable consequence must be read together with any later amendments and the charge used in a particular case.

This creates an important analytical distinction: a legal maximum/minimum penalty is not the same as an issued notice, investigation, charge, conviction, collected fine, remedial order, or sustained compliance outcome. Anavaratha must record each enforcement stage separately.

## Recent dumping and enforcement-reality evidence

### Environmental Foundation legal case
Environmental Foundation (Guarantee) Limited’s case page for SCFR 243/2017 reports a fundamental-rights application concerning alleged illegal disposal at Muthurajawela Sanctuary and Kotikawatta Dumping Grounds, including expansion of the Kotikawatta site and alleged industrial and urban waste dumping. The page states that proceedings were terminated in August 2022 after the policy had been tabled and circulated. Source: https://www.efl.lk/legal-action-against-garbage-dumping-in-environmentally-sensitive-areas/

This is a useful case-study source but is an NGO summary, not the full court record. Claim strength should therefore be coded as reported case-summary evidence until the judgment or court documents are retrieved.

### 2026 Mongabay reporting
Mongabay’s 23 April 2026 report states, citing the CEA/WMA and named experts, that Sri Lanka generates more than 7,000 metric tonnes of solid waste daily, of which about 4,500–5,600 tonnes are collected; Western Province accounts for roughly 60% of collected waste; Colombo Municipal Council is described as generating about 500 tonnes/day in the historical context; and more than 260 open dumpsites, including around 20 large sites, continue to operate. The report also describes the Meethotamulla mound, the Aruwakkalu and Dompe systems, facility maintenance and shutdown issues, local-authority technical constraints, and weak enforcement at local levels. Source: https://news.mongabay.com/2026/04/open-dumping-failed-reforms-bury-sri-lankan-cities-in-waste-problem/

These figures are current media-reported evidence with named sources, not a retrieved official statistical table. They should be used as leads and triangulated against CEA, WMA, local-authority, project, or parliamentary records before becoming formal Anavaratha estimates.

### Commercial commentary
A 20 March 2026 CleanTech article describes illegal dumping in empty land, canals, roadsides, construction land, burning, unlicensed collectors, inspections, complaints, and record tracing. It gives no verifiable enforcement statistics or case-level fine data in the extracted article. Source: https://cleantech.lk/illegal-waste-disposal-sri-lanka-penalties/

This is low-to-moderate evidence for identifying hypotheses and language used in public compliance discussions, but not a basis for quantified claims about enforcement frequency or fine collection.

## Primary Supreme Court findings: Meethotamulla

Official judgment retrieved: Supreme Court of Sri Lanka, SC/FR Applications 311/2015 & 318/2015, https://supremecourt.lk/wp-content/uploads/judgements/sc_fr_311_2015_and_sc_fr_318_2015.pdf

The judgment states that Colombo Municipal Council was primarily responsible for unlawful disposal, health hazard, serious pollution, and the consequences including 40 deaths at Pothuvil Kumbura during 2009–2017; Kolonnawa Urban Council was secondarily responsible. It concludes that dumping by CMC and KUC was contrary to statutory obligations under the Municipal Councils Ordinance and Urban Councils Ordinance, and infringed prohibitions under sections 23B, 23H, 23K and 23N of the National Environmental Act.

The judgment finds the Urban Development Authority responsible for permitting land use and expansion beyond two acres to approximately eighteen acres; the Western Province Waste Management Authority responsible for dereliction by remaining inactive; and the CEA responsible for failing to enforce the National Environmental Act against CMC and KUC while they engaged in a prescribed activity without a licence and polluted atmosphere, water, and soil.

Reliefs included restoration and mitigation measures supervised by CEA/WMA with restoration costs jointly borne by CMC and KUC; directions to CMC and KUC to establish and operationalize proper garbage-disposal programmes within six years; and review of Aruwakkalu operations. The Court did not impose individual penal consequences, expressly stating that this was due to the jurisdiction, evidence of individual lapses, and limits of adjudication. It also made no further compensation order because Rs. 908,314,020.70 had already been paid to affected persons, but ordered CMC and KUC to jointly pay petitioners’ litigation costs.

Analytical significance: this is direct evidence that a system can possess legislation, multiple responsible agencies, and formal duties while failing to produce compliance. It also distinguishes institutional constitutional accountability, remedial directions, compensation, and litigation costs from criminal fines or individual prosecutions. Anavaratha must not summarize this case as simply “the council was fined.”

## 2026 National Environmental Amendment

Official Parliament records confirm that National Environmental (Amendment) Act No. 15 of 2026 was endorsed on 21 July 2026 after first reading on 6 May 2026 and second/third readings on 24 June 2026. Parliament’s news page says the Act strengthens the legal framework, improves regulation of waste disposal, and modernizes environmental-protection mechanisms. Sources: https://www.parliament.lk/en/business-of-parliament/act-details/G6425 ; https://www.parliament.lk/en/business-of-parliament/bill-details/G6425 ; https://www.parliament.lk/en/home/parliament-news/view/5282

The official Act download is https://www.parliament.lk/uploads/acts/gbills/english/6425.pdf. Exact revised fine amounts and waste-specific provisions must be extracted from the primary Act text before citing them. Secondary snippets claiming fines up to LKR 10 million or LKR 20 million are not treated as verified until the Act is read directly.

Analytical significance: current legal analysis must be versioned. Section 31 and other penalty figures from the pre-2026 Act cannot automatically be described as the current law after 21 July 2026. Anavaratha should maintain an effective-date field for every legal provision.

## Verified current penalties under the 2026 amendment

Primary source: National Environmental (Amendment) Act No. 15 of 2026, official Parliament PDF: https://www.parliament.lk/uploads/acts/gbills/english/6425.pdf

The amendment changes Section 23N(4) for soil pollution. A person contravening section 23N(1) is liable, after summary trial before a Magistrate, to a fine not less than LKR 100,000 and not more than LKR 1,000,000, plus LKR 5,000 per day if the offence continues after conviction. The Court may also order corrective measures, restoration, and acceptable proof that corrective measures were taken.

The amendment inserts Section 23RR as a general penalty clause. For an offence under the Act or regulations for which no penalty is expressly provided, the person is liable to a fine not less than LKR 250,000 and not exceeding LKR 15,000,000, imprisonment up to two years, or both. This replaces the older default Section 31 penalty framework for the amended law’s current operation.

The amendment also provides penalties of up to LKR 10,000,000 or imprisonment up to three years for certain prescribed-project and environmental-management-monitoring-plan violations. These are not automatically the penalty for ordinary open dumping; the exact charge and provision must be matched to the facts.

The amendment expands the legal architecture from prohibition and punishment toward monitored corrective action. In practice, Anavaratha must still distinguish legal maximum/minimum penalties from detection, inspection, evidence collection, prosecution, conviction, fine payment, restoration, and verified compliance.

## 2026 Athurugiriya CCTV enforcement lead

Daily Mirror’s Facebook video page, dated July 2026, reports CCTV footage of numerous people disposing waste near Athurugiriya despite a warning board stating that illegal garbage dumping carries a Rs. 5,000 fine: https://www.facebook.com/Dailymirroronline/videos/cctv-captures-illegal-garbage-dumping-despite-rs-5000-fine-warningdespite-a-warn/3649689118506892/

This is evidence of a visible deterrence/signage and continued alleged dumping at that location. It is not evidence that the Rs. 5,000 fine was legally imposed, collected, or associated with a completed prosecution. Record as a low-to-moderate enforcement lead pending local-authority or court confirmation.

## JICA Nuwara Eliya Municipal Council evidence

Primary source: JICA, “The data collection survey of solid waste management in Sri Lanka,” final report materials, 2016: https://openjicareport.jica.go.jp/pdf/12250205.pdf. The downloaded report is stored as `JICA_SriLanka_Waste_Survey_2016.pdf` with extracted text in `JICA_SriLanka_Waste_Survey_2016.txt`.

The Nuwara Eliya MC section reports a 2012 population record of 53,670, about 6,799 dwellings, and approximately 20,000 daily floating population that could increase tenfold during the April festive season and long vacations. It describes tourism, commerce, services, agriculture, and tea as major activities. In the 2015 survey, 97% of surveyed households were provided with garbage collection and 95% stated that they used it; 40% reported daily service and 36% reported service 2–3 times per week. Thirty-five percent separated organic and inorganic waste at source, while 72% reported recyclable collectors or others collecting reusable/recyclable material.

The final disposal site at Moonplains is about 6 km from Nuwara Eliya city center and approximately 1 km inside a forest reservation. The site was upgraded to a model semi-engineered sanitary landfill in 2003 with JICA assistance. It lies on a middle slope, is surrounded by plantation forest, and has a perennial stream at the bottom of the valley used to discharge treated effluent from landfill and toilet-waste treatment facilities. The report records an average of 26 tonnes/day received over an 11-day period, with daily values from 11.5 to 45.6 tonnes. No source-segregated collection was in place at the time; most waste was disposed at the dump except a small amount of recyclables.

The site had records of incoming waste, daily activities, visitors, personnel, vehicles, maintenance, weighbridge, collection data, supervision, environmental protection licence/clearance, nearby impacts, and court cases as survey fields. The report describes a pre-scheduled disposal plan and a site supervisor, but heavy rain made access to the active filling area difficult; waste was then unloaded from the internal road and moved/compacted by bulldozer. Human resources listed at the site included one permanent supervisor, one labour/machine/tractor operator, three permanent male labourers, and day/night security guards, with administrative roles at municipal level.

Analytical significance: the user’s recollection of a scenic lake and forest-linked dumping context cannot yet be confirmed as a current council practice, but the JICA record verifies that a formally upgraded municipal disposal site existed inside a forest reservation near Nuwara Eliya, with tourism-driven seasonal pressure, mixed waste, and weather-dependent operational constraints. It is an excellent candidate for later controlled validation, not a basis for claiming current illegal dumping without updated evidence.

## GIS source audit: Sri Lanka spatial layers

The Sri Lanka NSDI Spatial Data Services page, last updated 14 July 2026, provides WMS service categories relevant to Anavaratha, including Boundaries, Environment, Inland Waters, Transportation, Utilities/Communications, Biota, Climate/Meteorology, Economy, Society, and Imagery/Base Maps/Earth Cover. The Utilities/Communications category explicitly includes water and waste systems; Environment includes pollution, waste storage and treatment, environmental risk, and nature reserves. Source: https://nsdi.gov.lk/spatial-data-services

The Survey Department of Sri Lanka states that its digital topographic vector databases include administrative boundaries, buildings, transport, hydrology, terrain, land use, toponymy, and utilities. It lists 23 completed layers including GN, DS, district, and province boundaries; hydrography; land use; forest and wildlife reserves; transport; and utility layers. The data are supplied by tiles in GIS formats, including shapefiles or DXF, at 1:50,000 and 1:10,000 scales. The Survey Department also reports mapping GN boundaries of 339 DS divisions and creating KML files for district, DS, and GN data. Source: https://survey.gov.lk/sdweb/pages_service_geo_information.php?id=df658590a4cbb1f955f5d386b242b6be8d5cadc0&l=s

The HDX/OCHA Sri Lanka COD-AB dataset is a practical downloadable boundary layer sourced from the Survey Department. Version 03 covers Admin 1: 9, Admin 2: 25, Admin 3: 339, and Admin 4: 14,043; it was reviewed for accuracy/completeness on 30 October 2025 and modified 26 January 2026. Available formats include GDB, SHP, GeoJSON, and XLSX. HDX notes name discrepancies for 530 Admin4 features with identical English names but multiple Sinhala variants, so stable codes rather than names must be used for joins. Source: https://data.humdata.org/dataset/cod-ab-lka

GIS implication: use Survey Department/NSDI layers where access is available; use HDX COD-AB as a reproducible administrative fallback; join census data using stable administrative codes; and retain source date, scale, geometry type, and known name conflicts in the spatial metadata table.

## National GIS map review

The first national map `ANAVARATHA_GIS_POPULATION_OSM_WASTE_V0_1.png` was visually checked and is readable. It shows DCS 2024 population denominators by HDX/OCHA district polygon with labels for the ten largest districts, and 118 OSM waste-related features as blue points. The district join now matches all 25 districts after explicitly normalizing `Monaragala`/`Moneragala`.

The map is suitable as a pressure-denominator and exploratory facility-distribution figure, not as a waste-burden or compliance map. OSM points are sparse and potentially misclassified; the figure explicitly states that they are incomplete and do not represent a national inventory. No causal or correlation claim is made from the visual overlay alone.

## First district-level OSM spatial summary

The OSM extract contains 118 geocoded waste-related features, distributed across 21 of 25 districts. The highest raw mapped-feature counts are Colombo (24), Gampaha (13), Kalutara (11), Batticaloa (9), Kurunegala (9), and Badulla (8). Mapped-feature counts per million 2024 population are highest among the districts with smaller or more sparsely mapped populations, including Batticaloa (15.10), Colombo (10.10), Matale (9.49), Badulla (9.17), and Kalutara (8.42).

These are counts of OpenStreetMap tags, not facilities, usable capacity, service quality, or waste burden. Differences may reflect mapping effort, classification practice, and population denominator effects. The output is therefore a coverage/audit layer and exploratory spatial proxy only: `ANAVARATHA_OSM_FEATURES_BY_DISTRICT_V0_1.csv`.

## Population–OSM feature relationship review

The exploratory scatterplot `ANAVARATHA_GIS_POPULATION_OSM_RELATIONSHIP_V0_1.png` was visually checked and is readable. Across 25 districts, 2024 population and mapped OSM waste-related feature count show Pearson r = 0.803 and rank correlation rho = 0.687. Colombo and Gampaha are high on both population and mapped feature count; Batticaloa and Badulla have relatively high mapped-feature counts for their populations.

These correlations describe the distribution of mapped OSM features, not actual waste generation, capacity, service quality, illegal dumping, or burden. They may reflect mapping intensity, urban accessibility, facility tagging, and population denominator effects. The result is useful only as a motivation for improving the facility inventory and testing coverage bias.

## Waste-to-receiving-environment proximity analysis

Using the 118-point OSM waste-related extract and 30,208 mapped OSM receiving-environment features at the 22 August 2026 snapshot, approximate nearest-feature distances were calculated in UTM zone 44N. Of the mapped waste-related points, 53 were within 1 km of a mapped waterway, 107 within 5 km; 82 were within 1 km of a mapped waterbody or wetland, and all 118 within 5 km; 4 were within 1 km of a mapped protected area and 31 within 5 km; 42 were within 1 km of a mapped forest and 92 within 5 km.

Output: `ANAVARATHA_OSM_WASTE_RECEIVING_PROXIMITY_V0_1.csv`. These are centroid/point proximity indicators based on incomplete OSM mapping. They do not establish contamination, illegality, hydrological connection, ecological impact, or facility capacity. They identify locations for data-quality review and later targeted verification.

## Exploratory OSM waste-feature clusters

Using DBSCAN with a 5 km neighbourhood and minimum three mapped features, the 118 OSM waste-related points produced 11 exploratory clusters, containing 60 mapped features; 58 were classified as noise under this rule. The largest cluster contained 19 features around approximately 6.9042, 79.9188 and included landfill, recycling, and wastewater tags; other clusters appeared around 6.8707, 81.0505; 7.9603, 80.7585; 7.2996, 80.6293; 6.9411, 80.0125; and other locations listed in `ANAVARATHA_OSM_WASTE_CLUSTERS_V0_1.csv`.

These are clusters of OSM mapping tags, not confirmed illegal dumping clusters, facility-capacity clusters, or environmental-burden clusters. The result is useful for prioritizing data-quality checks and for testing whether mapped infrastructure is concentrated near population/activity centers, but it must not be reported as the spatial distribution of waste itself.

## GIS layer integrity audit

The current spatial layers are all EPSG:4326 with valid geometries and no duplicate IDs: 25 district polygons joined to 2024 census denominators; 118 OSM waste-related point/centroid features; and 30,208 OSM receiving-environment point/centroid features. All 25 district population denominators are present after the explicit Monaragala/Moneragala normalization. The waste-site OSM snapshot is 2026-08-22 06:08:04 UTC and the receiving-environment snapshot is 2026-08-22 06:12:08 UTC. Ninety-four of 118 waste-related OSM features lack a `name` tag, so name-based identification is weak and stable OSM IDs/coordinates must be retained.

Output: `ANAVARATHA_GIS_LAYER_INTEGRITY_AUDIT_V0_1.csv`. The completeness limitation remains central: geometry validity does not imply national completeness, legal status, operational status, or capacity.

## Official NSDI utility context

The NSDI Utilities_Communications ArcGIS REST service exposes official sanitary-sewer layers: 118 sewer interceptor manholes, 61 sewer manholes, 35 force-main lines, 89 gravity-main lines, and 119 lateral-pipeline lines. The retrieved records are all spatially located in Colombo district in the current service response. The district summary is in `ANAVARATHA_NSDI_SEWER_FEATURES_BY_DISTRICT_V0_1.csv`.

This is not a solid-waste capacity layer. It is a useful contextual proxy for public utility and wastewater-network concentration, and it demonstrates a broader data issue: a service may expose a detailed infrastructure layer for one domain and area while still lacking a national, current, comparable solid-waste facility/capacity inventory.

## Documentation consolidation: three-domain architecture

On 25 August 2026 the core Anavaratha documentation was reorganized around three distinct but connected domains: (1) Freedom from Waste, focused on unmanaged residual burdens, exposure, leakage, accumulation, unsafe work, and institutional failure; (2) Material Afterlives, the preferred label for latent utility, reuse, repair, exchange, refurbishment, salvage, and post-use circulation; and (3) Ecological Flourishing, a separate axis for ecological capability, regeneration, restoration, biodiversity, soils, forests, wetlands, waterways, and stewardship.

New canonical documents: ANAVARATHA_MASTER_RESEARCH_ARCHITECTURE_V0_1.md, ANAVARATHA_THREE_DOMAIN_ARCHITECTURE_V0_1.md, and ANAVARATHA_DOCUMENTATION_INDEX_V0_1.md. The thermodynamics framework was aligned to the three-domain terminology, including section-number corrections and explicit safeguards against treating Material Afterlives, social justice, or ecological flourishing as literal thermodynamic quantities. A portable documentation suite was assembled at ANAVARATHA_DOCUMENTATION_SUITE_V0_1.zip.
