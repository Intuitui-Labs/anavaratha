"""Build normalized JSON for the Anavaratha atlas.
Every node/event/flow carries `src` = file path (+ section) it traces to.
Inputs are read from the frozen snapshot /workspace/viz/_src_snapshot (copied 2026-11-16 ~11:07 +0530)
plus read-only raw legacy files under /workspace/anavaratha-legacy/raw.
"""
import csv, json, re, collections, hashlib, os
S='/workspace/viz/_src_snapshot'; P=S+'/phase1'; RAW='/workspace/anavaratha-legacy/raw'
OUT='/workspace/viz/data'
CH='anavaratha-legacy/CHRONOLOGY.md'; OV='anavaratha-legacy/OVERLAP_MAP.md'
CHARTER='anavaratha-legacy/raw/IntuituiLabs_Anavaratha/ANAVARATHA_CHARTER_V0_1.md'
WC_MAP='anavaratha-legacy/raw/waste_cycles_anavaratha/zip_entries/Anavaratha Enforcement Institution and Capacity Map v0.1.md'
LLA='anavaratha-legacy/raw/waste_cycles_anavaratha/zip_entries/ANAVARATHA_DOCUMENTATION_SUITE_V0_1__unzipped/anavaratha_documentation_suite/domain_frameworks/ANAVARATHA_LEARNING_LEVERAGE_ACTION_ARCHITECTURE_V0_1.md'
PH='neevsk-research/anavaratha/phase1/'
nodes=[]; edges=[]
def N(id,label,kind,src,**kw): nodes.append(dict(id=id,label=label,kind=kind,src=src,**kw))
def E(s,t,rel,src,**kw): edges.append(dict(source=s,target=t,rel=rel,src=src,**kw))

# ---- domains, frames, glossary (concept layer)
N('anavaratha','Anavaratha','root',CHARTER+' §1')
for i,(d,q) in enumerate([('Freedom from Waste','reduce involuntary exposure to residual burdens without transferring them'),
  ('Material Afterlives','when does "no longer needed by me" become "available for another"'),
  ('Ecological Flourishing','conditions that let ecological systems regenerate')],1):
    N(f'dom{i}',f'Domain {"I"*i if i<3 else "III"} · {d}','domain',CHARTER+' §5',question=q); E('anavaratha',f'dom{i}','has_domain',CHARTER+' §5')
for f,l,s in [('frameA','Frame A · use → residual → regeneration','FRAME_INVERSION.md §Frame A'),
              ('frameB','Frame B · residuals that refuse regeneration','FRAME_INVERSION.md §Frame B'),
              ('frameC','Frame C · syntropy first (lock)','FRAME_C_SYNTROPY.md §Lock')]:
    N(f,l,'frame',PH+s); E('anavaratha',f,'has_frame',PH+s)
E('frameC','frameA','order_of_work',PH+'FRAME_C_SYNTROPY.md "C → A → B"'); E('frameA','frameB','order_of_work',PH+'FRAME_C_SYNTROPY.md "C → A → B"')
for t in ['Capability','Use','Residuality','Regeneration','Pressure','Unit of analysis','Evidence','Stage exit (Sensemaking)']:
    N('g_'+re.sub(r'\W+','_',t.lower()),t,'glossary',PH+'GLOSSARY_v0.md'); E('frameA','g_'+re.sub(r'\W+','_',t.lower()),'defines',PH+'GLOSSARY_v0.md')
for t in ['Material','Flow','Stock','Boundary','Capacity','Dissipation','Afterlife','Receiver','Evidence status']:
    N('sg_'+re.sub(r'\W+','_',t.lower()),t,'shared_grammar',CHARTER+' §3 Shared grammar'); E('anavaratha','sg_'+re.sub(r'\W+','_',t.lower()),'shared_grammar',CHARTER+' §3')

# ---- lineage: legacy concept -> current status (OVERLAP_MAP §2 codes)
lineage=[ # (id,legacy concept,legacy source,current object,code)
 ('premise','Project premise / identity','Charter final; projects.ts 2026-08-29','PROBLEM_FRAME.md','DUP'),
 ('name','Name meaning','What Does Anavaratha Mean zip; charter draft vs final','BRIEF Q1 gate','DUP+CON'),
 ('three_domains','Three domains','Charter; Core Package','(none in phase1)','IGN'),
 ('two_dirs','Two directions → Freedom to Flourish','Project Package','(superseded)','IGN'),
 ('urr','Use → residual → regeneration','public premise','Frame A','DUP'),
 ('displacement','Displacement test / accountable transition','Feb evaluation; charter §6','Frame B','EXT'),
 ('negentropy','Negentropy as cautious metaphor','Charter §4; Core §12; Feb L1','Frame C syntropy-first','CON'),
 ('exergy','Exergy / accounting identity / holarchy','Feb L1','(none)','IGN'),
 ('reservoirs','Pressure reservoirs / visibility gradient','Feb L1','QUESTIONS Q1, Q6','DUP'),
 ('leverage','Leverage points (Meadows; A–F)','Feb; Core Package','(premature under Sensemaking)','CON'),
 ('intervention','Intervention typology + methodology','Feb 2026-02-24 docs','KILL_LOG items 1,4','CON'),
 ('evaluation','Evaluation framework','Feb','(none)','IGN'),
 ('maturity','Maturity model Mapped→Actionable','Charter §3','STAGE_EXIT_CRITERIA.md','DUP+CON'),
 ('sequence','Foundational sequence desk→…→action','Charter §3','EVIDENCE_CATALOG.md posture','DUP'),
 ('evidence_vocab','Evidence status vocabulary','Charter §3','listed vs verified','DUP'),
 ('capacity_chain','Capacity chain / no public evidence system','Core Package','LEDGER §3–4','DUP'),
 ('compost','WP compost 157 of 2,775 t/month','Core Package (Manipura 2025)','LEDGER (b) counts compost as gain','CON'),
 ('facility_reg','Facility registers [WC]','waste_cycles zip','DIRECTORY geojson 707 features','DUP'),
 ('operator_dir','15-company operator list','Comprehensive Dataset zip (Oct)','DIRECTORY 487 operators','DUP'),
 ('platform','"Waste ecosystem platform" dashboard','ideas.md, *.tsx (Oct)','KILL_LOG item 1','CON'),
 ('cases','Meethotamulla / Kerawalapitiya / Karadiyana','Core Package + [WC]','LEDGER L10, L20–22','DUP'),
 ('data_request','Data request pack (unsent drafts)','[WC]','call sheets (operator-level)','DUP'),
 ('afterlives_ev','Material Afterlives evidence','Project Package 05_circulation','household-route research','EXT'),
 ('ecology_atlas','Cultivation atlas / Osu Uyana','Project Package','(none; QS1 Dry Zone only)','IGN'),
 ('institutions','Institutions as coordination / responsibility chain','Core §3C/§3F; [WC] map','DIRECTORY + LEDGER (unaware)','DUP'),
 ('tooling','Tooling (DuckDB/Parquet, data/raw→processed)','Feb agent_context','(none)','IGN'),
 ('peace_valley','Peace Valley boundary','—','BOUNDARY_MEMO (lock)','NEW'),
]
for lid,l,lsrc,cur,code in lineage:
    N('lg_'+lid,l,'legacy_concept',OV+' §2 / §1',legacy_source=lsrc)
    N('cu_'+lid,cur,'current_object',OV+' §2',)
    E('lg_'+lid,'cu_'+lid,code,OV+' §2 row "'+l+'"')

# ---- institutions: 11 actor classes from [WC] map, chain links from Core §3F
chain=['duty','capacity','detection','enforcement','remedy','persistence']
for c in chain: N('ch_'+c,c,'chain_link',LLA+' §F')
for a,b in zip(chain,chain[1:]): E('ch_'+a,'ch_'+b,'next',LLA+' §F')
inst=[] ; txt=open(RAW+'/waste_cycles_anavaratha/zip_entries/Anavaratha Enforcement Institution and Capacity Map v0.1.md').read()
for line in txt.splitlines():
    m=re.match(r'\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|$',line)
    if m and not m.group(1).startswith(('Institution','---')):
        inst.append(dict(name=m.group(1),role=m.group(2),capacity=m.group(3),evidence=m.group(4)))
assert len(inst)==11, len(inst)
# map actor -> chain link ONLY by keyword present in the role text (quoted in edge)
kw={'duty':r'\b(collection|duties|policy|administer|regulations|local waste)','capacity':r'\b(operational|technical|programs|recovery|sorting|transport)\b',
    'detection':r'\b(inspect|investigat|monitoring|complaints|detect)','enforcement':r'\b(licen[cs]e|directions|enforcement|criminal|orders|summary trials|approvals|permissions)',
    'remedy':r'\b(remedy|restoration|corrective|fines|litigation)','persistence':r'\b(monitoring of compliance|steering and monitoring)'}
for i,x in enumerate(inst,1):
    iid=f'inst{i:02d}'; N(iid,x['name'],'institution',WC_MAP+' §Institutional map',role=x['role'],capacity_needed=x['capacity'],evidence_to_seek=x['evidence'])
    for c,r in kw.items():
        m=re.search(r,x['role'],re.I)
        if m: E(iid,'ch_'+c,'role_keyword',WC_MAP+' §Institutional map',keyword=m.group(0))
comp=['Rule clarity','Boundary clarity','Detection','Attribution','Evidence integrity','Authority action','Adjudication','Sanction or remedy','Implementation','Verification','Persistence']
for i,c in enumerate(comp,1): N(f'cp{i:02d}',f'{i}. {c}','compliance_step',WC_MAP+' §Compliance-production chain')
for i in range(1,11): E(f'cp{i:02d}',f'cp{i+1:02d}','next',WC_MAP+' §Compliance-production chain')

# ---- projects (41 ledger rows) + funders by string match
L=list(csv.DictReader(open(P+'/ledger_waste_projects_lk.csv')))
def yrs(s):
    ys=[int(y) for y in re.findall(r'\b(19[89]\d|20[0-3]\d)\b',s)]
    return (min(ys),max(ys)) if ys else (None,None)
funders={'World Bank':r'World Bank|\bWB\b|IDA','JICA':r'JICA','ADB':r'\bADB\b','KOICA / Korea':r'KOICA|Korea','UNDP':r'UNDP','UNEP / IGES':r'UNEP|IGES','EU':r'\bEU\b|European','USAID':r'USAID','CEA':r'\bCEA\b','WMA (Western Province)':r'\bWMA\b','CMC':r'\bCMC\b','UDA':r'\bUDA\b','Min. Environment / Urban Dev':r'Ministry|MoE|MUD','Local authorities':r'\bUC\b|\bMC\b|\bPS\b|local author|\bLAs?\b'}
for f in funders: N('org_'+re.sub(r'\W+','_',f.lower()),f,'org',PH+'ledger_waste_projects_lk.csv funder_implementer (string match)')
projects=[]
for r in L:
    s,e=yrs(r['years']); flag=None
    if r['id']=='L41': s,e,flag=None,None,'IATI dates are placeholders (ledger says not found)'
    if r['id']=='L04': flag='conflicting establishment dates (ledger)'
    ongoing=bool(re.search(r'present|onward|-\s*$|launched|not in full operation|again',r['years']))
    approx=False
    if r['id']=='L38': s,e,approx,flag=2000,2019,True,'ledger gives decades only ("2000s-2010s"); bar spans 2000–2019 and is approximate'
    pid='prj_'+r['id']; N(pid,r['id']+' '+r['name'],'project',PH+f'ledger_waste_projects_lk.csv row {r["id"]}',type=r['type'],years_text=r['years'],start=s,end=e,pattern=r['pattern'],flag=flag)
    projects.append(dict(id=r['id'],name=r['name'],type=r['type'],years_text=r['years'],start=s,end=e,ongoing=ongoing,pattern=r['pattern'].split(' ')[0],pattern_note=r['pattern'],funder_implementer=r['funder_implementer'],evaluation=r['independent_evaluation_audit'],src=PH+f'ledger_waste_projects_lk.csv row {r["id"]}',flag=flag,approx=approx,undated=s is None))
    for f,rx in funders.items():
        if re.search(rx,r['funder_implementer']): E(pid,'org_'+re.sub(r'\W+','_',f.lower()),'funder_or_implementer',PH+f'ledger_waste_projects_lk.csv row {r["id"]} funder_implementer')

# ---- docs layer (key artifacts, dated, from CHRONOLOGY §A)
docs=[('d_concept','Concept Doc (Claude Project)','2026-02-20','zips/claudeexport_neevsk_projects-000__unzipped/projects/019c7a5f-75d3-71d4-947e-a186b780585a.json','L1'),
 ('d_feb24','Feb framework docs (8) + data-domain map','2026-02-24','IntuituiLabs_Anavaratha/files__unzipped/*','L1'),
 ('d_core','Core Package V0_1','2026-08-22','IntuituiLabs_Anavaratha/ANAVARATHA_CORE_PACKAGE_V0_1__unzipped/','L2'),
 ('d_wc','Waste-cycles [WC] institution/enforcement layer','2026-08-25','waste_cycles_anavaratha/zip_entries/','L2'),
 ('d_proj','Project Package','2026-08-25','IntuituiLabs_Anavaratha/ANAVARATHA_PROJECT_PACKAGE__unzipped/','L2'),
 ('d_charter','Charter V0.1 final','2026-08-29','IntuituiLabs_Anavaratha/ANAVARATHA_CHARTER_V0_1.md','L2'),
 ('d_web','intuitui-web projects.ts + SystemLifecycle','2026-08-29','github/*/src_lib_projects.ts.snippet.txt','L3'),
 ('d_repo','Public repo Phase 1 pack','2026-09-22','github/Intuitui-Labs_anavaratha__gitlog.txt','C'),
 ('d_name','"What Does Anavaratha Mean" export','2026-10-04','IntuituiLabs_Anavaratha/What Does _Anavaratha_ Mean_.zip','L3'),
 ('d_dataset','Comprehensive Dataset (platform brainstorm)','2026-10-04','IntuituiLabs_Anavaratha/Comprehensive Dataset on Waste Management in Sri Lanka.zip','L3'),
 ('d_initdoc','docs/initiatives/anavaratha.md','2026-10-16','intuitui-web/anavaratha.md','L3'),
 ('d_dir','Directory + ledger + desk notes (unpushed)','2026-11-09','current_snapshot_2026-11-16/','C'),
 ('d_tax','Taxonomy + call sheets + sweep','2026-11-16','neevsk-research/anavaratha/phase1/','C')]
for i,l,d,p,layer in docs: N(i,l,'doc','anavaratha-legacy/raw/'+p if not p.startswith('neevsk') else p,date=d,layer=layer)
for a,b in zip(docs,docs[1:]): E(a[0],b[0],'precedes',CH+' §A')
doc_concept=[('d_concept','lg_negentropy'),('d_concept','lg_reservoirs'),('d_concept','lg_exergy'),('d_feb24','lg_intervention'),('d_feb24','lg_leverage'),('d_feb24','lg_evaluation'),('d_feb24','lg_displacement'),('d_feb24','lg_tooling'),
 ('d_core','lg_capacity_chain'),('d_core','lg_compost'),('d_core','lg_institutions'),('d_wc','lg_institutions'),('d_wc','lg_data_request'),('d_wc','lg_facility_reg'),('d_wc','lg_cases'),
 ('d_proj','lg_two_dirs'),('d_proj','lg_afterlives_ev'),('d_proj','lg_ecology_atlas'),('d_charter','lg_three_domains'),('d_charter','lg_maturity'),('d_charter','lg_sequence'),('d_charter','lg_evidence_vocab'),('d_charter','lg_premise'),
 ('d_name','lg_name'),('d_dataset','lg_platform'),('d_dataset','lg_operator_dir'),('d_charter','lg_urr')]
for d,c in doc_concept: E(d,c,'introduces',CH+' §A/§B; '+OV+' §2')
for d,c in [('d_repo','frameA'),('d_repo','frameB'),('d_repo','frameC'),('d_repo','cu_peace_valley'),('d_dir','cu_operator_dir'),('d_dir','cu_cases')]: E(d,c,'introduces',CH+' §A')
for i in (1,2,3): E('d_charter',f'dom{i}','introduces',CHARTER+' §5')
E('dom1','lg_institutions','scope',OV+' §2 (three domains row)'); E('dom2','lg_afterlives_ev','scope',CHARTER+' §5 Domain II'); E('dom3','lg_ecology_atlas','scope',CHARTER+' §5 Domain III')
E('frameC','lg_negentropy','bridge',OV+' §4 (Frame C row: map C to Domain III & care amplifiers)')

ids={n['id'] for n in nodes}; bad=[e for e in edges if e['source'] not in ids or e['target'] not in ids]; assert not bad,bad[:3]
json.dump(dict(meta=dict(generated='2026-11-16 (Asia/Colombo)',note='Every node/edge has src. institution→chain edges are keyword matches in role text, not judgements.',counts=collections.Counter(n['kind'] for n in nodes)),nodes=nodes,edges=edges),open(OUT+'/graph.json','w'),indent=1,ensure_ascii=False)

# ---- timeline.json: concept events (CHRONOLOGY §A/§B) + ledger
ev=[('2026-02-20','first','Claude Project "Anavaratha" + Concept Doc','name, negentropy/care, "does not prescribe", institutions in operational layer','H'),
 ('2026-02-20','first','Chat: mapping data with geo/temporal dimensions','data-domain map idea','H'),
 ('2026-02-24','mutation','Feb framework docs + data-domain map v1/v2','"zones of care" → intervention design; Meadows leverage; displacement test; exergy identity; 29 data-provider institutions','M'),
 ('2026-02-25','dormant','~6-month gap','no Anavaratha artifacts until 2026-08-22','M'),
 ('2026-08-22','revival','Chat "Anavaratha project" (returning after ~6 months)','revival; Manus desk research','H'),
 ('2026-08-22','mutation','Core Package frameworks','waste/material-cycle focus; negentropy "not a score"; coordination leverage + accountability chain; WP compost 157/2,775','H'),
 ('2026-08-22','first','[WC] Waste desk sequence + Waste Sense-Making Model','first waste track; "sense-making" named as a model; site/pilot selection (later dropped). Dated ≤08-22, order inferred from version numbers','L'),
 ('2026-08-22','accretion','[WC] Demonstrator 01 + capacity datasets','usable vs nominal capacity; bottleneck matrix carries an intervention column (conflicts with the Sensemaking lock)','H'),
 ('2026-08-25','accretion','Project Package + [WC] institution/enforcement layer','cultivation, Osu Uyana, circulation; 11-actor responsibility map; data-request drafts','H/M'),
 ('2026-08-25','rename','Three-Domain Architecture','"Freedom to Flourish" → Material Afterlives + Ecological Flourishing','H'),
 ('2026-08-27','first','Charter v0.1 draft','Sanskrit caution on name; two movements + interval','H'),
 ('2026-08-29','mutation','Charter v0.1 final','adds inspirations + thermodynamics; name → "draws from Sinhala"; drops two-movements frame','H/M'),
 ('2026-08-29','drop','Charter §7: no site claims','[WC] site/pilot selection and candidate ranking not carried forward','M'),
 ('2026-08-29','first','intuitui-web projects.ts','first public appearance of charter premise','H'),
 ('2026-09-03','first','SystemLifecycle.astro','"Sensemaking" stage label first appears','H'),
 ('2026-09-22','revival','Public repo Phase 1 pack','Frames A/B/C, syntropy-primary, kill log, Peace Valley boundary; revives Feb-20 "does not prescribe" unknowingly','H'),
 ('2026-09-22','drop','KILL_LOG','product/app, market opportunity, national regen programmes killed','H'),
 ('2026-10-04','accretion','Name research + platform brainstorm exports','anavarata = ceaseless; dashboard idea (later killed)','M'),
 ('2026-10-16','rename','intuitui-web initiative doc','public wording → three domains','H'),
 ('2026-11-09','accretion','Directory, ledger, desk notes','re-does operator/institution inventory','H/L'),
 ('2026-11-16','accretion','Taxonomy, call sheets v1, sweep','487 operators, 352 drop points, 20+ types with no household route','M'),
 ('2026-11-16','revival','Lineage consolidation','legacy layers re-attached (this atlas)','H')]
timeline=dict(meta=dict(src=CH+' §A, §B; '+PH+'ledger_waste_projects_lk.csv',pattern_key={'a':'repeated/recycled promise or claims not matched by outcomes','b':'real but local or temporary gain','c':'no evaluation or no outcome data'}),
  concept_events=[dict(date=d,type=t,title=ti,effect=ef,confidence=c,src=CH+' §A') for d,t,ti,ef,c in ev],
  projects=projects)
json.dump(timeline,open(OUT+'/timeline.json','w'),indent=1,ensure_ascii=False)

# ---- flows.json
tax=[]; cur=None
for line in open(P+'/WASTE_TAXONOMY_LK.md'):
    if line.startswith('## '): cur=re.sub(r'^##\s*\d+\.\s*','',line.strip()).replace(' (PRIORITY)','')
    m=re.match(r'\|\s*`([A-Z]+\.[\w]+)`\s*\|([^|]*)\|([^|]*)\|([^|]*)\|',line)
    if m and not cur.startswith('2026'): tax.append(dict(group=cur,type_id=m.group(1),label=m.group(2).strip(),hh_route=m.group(3).strip(' *'),ops=int(m.group(4).strip()) if m.group(4).strip().isdigit() else None))
links=collections.Counter((t['group'],t['hh_route']) for t in tax)
sankey=dict(src=PH+'WASTE_TAXONOMY_LK.md type tables (HH route column)',unit='waste types',
  nodes=sorted({t['group'] for t in tax})+sorted({t['hh_route'] for t in tax}),
  links=[dict(source=a,target=b,value=v) for (a,b),v in links.items()],types=tax)
H=PH+'DESK_HOUSEHOLD_WASTE_STREAMS_LK.md'
route=dict(src=H,item='Household aerosol / hazardous item',steps=[
 dict(id='bylaw',label='By-law: separate "hazardous waste" (c)',status='rule exists',src=H+' §1 [S1]'),
 dict(id='council',label='Hand to council collector / council bins',status='on paper',src=H+' §1 [S1]'),
 dict(id='cmc',broken=True,label='CMC 3 streams: recyclable / non-recyclable / food',status='no hazardous stream found',src=H+' §1 [S2][S3]'),
 dict(id='sw',broken=True,label='CEA Scheduled Waste licence',status='industrial generators only',src=H+' §3 [S15]'),
 dict(id='msw',broken=True,label='CEA MSW guideline',status='hazardous out of scope; screen it out',src=H+' §3 [S16]'),
 dict(id='mixed',label='Mixed into non-degradables',status='what happens (Negombo: ~200 kg/day)',src=H+' §3 [S6]'),
 dict(id='dump',label='Open dump (~63% of disposal, UNDP 2026)',status='dominant destination',src=H+' §2 [S7]'),
 dict(id='wte',label='Kerawalapitiya WtE / landfill (Colombo)',status='possible',src=H+' §2 [S13]')],
 breaks=[dict(between=['cmc','sw'],why='council route has no hazardous channel; national system excludes households',src=H+' §4.1'),
         dict(between=['cmc','msw'],why='MSW guideline sends hazardous "somewhere else" that does not exist',src=H+' §4.1')],
 frame='Frame B refusal case candidate',frame_src=H+' §6')
json.dump(dict(household_route_sankey=sankey,hazardous_route=route,
  responsibility_chain=dict(links=chain,src=LLA+' §F',compliance_steps=comp,compliance_src=WC_MAP+' §Compliance-production chain')),open(OUT+'/flows.json','w'),indent=1,ensure_ascii=False)

# ---- contact-free operators geojson
g=json.load(open(P+'/DIRECTORY_WASTE_OPERATORS_LK.geojson'))
DROP={'contact_public','address','price'}
phone=re.compile(r'(?<![\w/=.-])(\+?94[\s-]?|0)?\d{2,3}[\s-]?\d{3}[\s-]?\d{3,4}(?![\w/])'); email=re.compile(r'[\w.+-]+@[\w-]+\.[\w.]+')
def scrub(k,v):
    if not isinstance(v,str) or k in('source_urls','source'): 
        return email.sub('[email removed]',v) if isinstance(v,str) else v
    v=email.sub('[email removed]',v)
    return phone.sub('[phone removed]',v) if k not in ('id','point_id','cea_licence_status') else v
feats=[]
for f in g['features']:
    p={k:scrub(k,v) for k,v in f['properties'].items() if k not in DROP}
    c=f['geometry']['coordinates']; feats.append(dict(type='Feature',geometry=dict(type='Point',coordinates=[round(c[0],4),round(c[1],4)]),properties=p))
# ---- rows the source geojson leaves out: geocoded from their own address/district (scripts/geocode_unmapped.py) or listed as not mapped
GEO=json.load(open(OUT+'/_geocode_results.json'))
have={f['properties'].get('id') or f['properties'].get('point_id') for f in g['features']}
ECOLS=['id','name','type','waste_streams','accepts_detail','activity','household_access','district','coord_precision','cea_licence_status','active_evidence','source_urls','url_check','dataset_origin','verified_on_ground','waste_types']
unmapped=[]
for path,idk,layer,cols in [(P+'/DIRECTORY_WASTE_OPERATORS_LK.csv','id','entity',ECOLS),(P+'/DIRECTORY_WASTE_OPERATORS_LK_droppoints.csv','point_id','drop_point',['point_id','point_name','operator','kind','streams','accepts','coord_precision','source'])]:
    for r in csv.DictReader(open(path)):
        if r[idk] in have: continue
        gr=GEO.get(r[idk])
        try: gr=dict(status='mapped',lat=round(float(r['lat']),4),lon=round(float(r['lon']),4),precision=r['coord_precision']+' (coordinates from the source CSV; row absent from source geojson)',from_csv=True)
        except (ValueError,KeyError): pass
        if gr and gr['status']=='mapped':
            p={k:scrub(k,r[k]) for k in cols if k in r}; p['layer']=layer; p['coord_precision']=gr['precision']; p['geocoded_by_atlas']=not gr.get('from_csv')
            feats.append(dict(type='Feature',geometry=dict(type='Point',coordinates=[gr['lon'],gr['lat']]),properties=p))
        else:
            unmapped.append(dict(id=r[idk],layer=layer,name=scrub('name',r.get('name') or r.get('point_name')),district=r.get('district',''),
              reason=(gr or {}).get('reason','no coordinates in source and no geocode attempt'),src_precision=r.get('coord_precision','')))
cnt=collections.Counter((f['properties']['layer'],bool(f['properties'].get('geocoded_by_atlas'))) for f in feats)
pub=dict(type='FeatureCollection',meta=dict(src=PH+'DIRECTORY_WASTE_OPERATORS_LK.geojson + .csv + _droppoints.csv (snapshot 2026-11-16)',removed_fields=sorted(DROP),scrubbed='phone/email patterns in remaining text',status='listed, not verified on ground',
  geocoded_by_atlas='approximate locality centroids from the row\'s own address (Nominatim/OSM, district-checked); flagged geocoded_by_atlas=true',
  counts=dict(entities_total=sum(1 for _ in open(P+'/DIRECTORY_WASTE_OPERATORS_LK.csv'))-1,drop_points_total=sum(1 for _ in csv.DictReader(open(P+'/DIRECTORY_WASTE_OPERATORS_LK_droppoints.csv'))),
    entities_mapped=cnt[('entity',False)]+cnt[('entity',True)],entities_geocoded_by_atlas=cnt[('entity',True)],
    drop_points_mapped=cnt[('drop_point',False)]+cnt[('drop_point',True)],drop_points_geocoded_by_atlas=cnt[('drop_point',True)],
    entities_not_mapped=sum(1 for u in unmapped if u['layer']=='entity'),drop_points_not_mapped=sum(1 for u in unmapped if u['layer']=='drop_point'))),features=feats)
json.dump(dict(meta=dict(src=pub['meta']['src'],note='rows with no usable coordinates; reason per row. No coordinates invented.'),rows=unmapped),open(OUT+'/operators_unmapped.json','w'),indent=1,ensure_ascii=False)
print('geo counts',pub['meta']['counts'])
s=json.dumps(pub,ensure_ascii=False)
assert not email.search(re.sub(r'https?://\S+','',s)), 'email left'
json.dump(pub,open(OUT+'/operators_public.geojson','w'),ensure_ascii=False)
print('nodes',len(nodes),'edges',len(edges),'projects',len(projects),'tax types',len(tax),'features',len(feats))

# ---- matrix.json from COMPARISON_MATRIX.csv (concept presence per source layer)
M=list(csv.DictReader(open(S+'/COMPARISON_MATRIX.csv')))
cols=[c for c in M[0].keys() if c not in('category','row','regex')]
cells=[]
for r in M:
    for c in cols:
        v=r[c]; m=re.search(r'\((\d+)\)|\[(\d+)\]',v)
        n=int(m.group(1) or m.group(2)) if m else 0
        cells.append(dict(row=r['row'],category=r['category'],source=c,hits=n,raw=v))
json.dump(dict(src='anavaratha-legacy/COMPARISON_MATRIX.csv',note='regex hit counts per source layer; presence ≠ endorsement',sources=cols,rows=[r['row'] for r in M],cells=cells),open(OUT+'/matrix.json','w'),ensure_ascii=False)
print('matrix rows',len(M),'cols',len(cols))
