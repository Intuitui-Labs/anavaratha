#!/usr/bin/env python3
"""Build the site map data from the merged public export (Anavaratha merge v2, 2026-11-17).
Input: the public-safe export (repo: data/merged/ ; box: /workspace/anavaratha-merge/public/).
Output: public/data/operators_public.geojson, public/data/operators_unmapped.json, src/data/geo_meta.json.
Address, contact and price are not put on the map. Retired alias ids are folded into their canonical row (listed in `aliases`)."""
import csv,json,os,re,sys
HERE=os.path.dirname(os.path.abspath(__file__)); SITE=os.path.abspath(HERE+'/../..')
SRC=sys.argv[1] if len(sys.argv)>1 else os.path.abspath(SITE+'/../data/merged')
rd=lambda p:list(csv.DictReader(open(p,encoding='utf-8')))
PH=re.compile(r'(?<![\w./])(?:\+94[ -]?|0)\d{2}[ -]?\d{3}[ -]?\d{4}(?![\w.])|(?<![\w./=#-])(?:\+?94)?[1-9]\d{8}(?![\w./])'); EM=re.compile(r'[\w.+-]+@[\w-]+\.[\w.]+')
def clean(v): return EM.sub('[email removed]',PH.sub('[phone removed]',v or ''))
def num(x):
    try: float(x); return True
    except: return False
old={}
op=SITE+'/public/data/operators_unmapped.json'
if os.path.exists(op):
    for r in json.load(open(op))['rows']: old[r['id']]=r
E=['id','name','type','waste_streams','waste_types','accepts_detail','activity','household_access','coord_precision','coord_status','cea_licence_status','active_evidence','source_urls','dataset_origin','verified_on_ground','record_status','aliases','evidence_status','domain_primary','domain_secondary','domain_confidence','merged_id']
DPK=['point_id','point_name','operator','kind','streams','accepts','coord_precision','coord_status','source','evidence_status','domain_primary','domain_secondary','domain_confidence','merged_id']
feats=[];um=[];c=dict(entities_total=0,entities_proposed=0,drop_points_total=0,entities_mapped=0,entities_geocoded_by_atlas=0,drop_points_mapped=0,drop_points_geocoded_by_atlas=0,entities_not_mapped=0,drop_points_not_mapped=0,retired_aliases_folded=0)
for r in rd(SRC+'/directory_public.csv'):
    c['entities_total']+=1; prop=r['record_status'].startswith('proposed'); c['entities_proposed']+=prop
    c['retired_aliases_folded']+=len([a for a in r['aliases'].split(';') if a])
    p={k:clean(r.get(k,'')) for k in E}; p['district']=r['district_resolved']; p['layer']='entity'; p['geocoded_by_atlas']=r['coord_status'].startswith('approximate')
    if num(r['lat']) and num(r['lon']):
        c['entities_mapped']+=1; c['entities_geocoded_by_atlas']+=p['geocoded_by_atlas']
        feats.append(dict(type='Feature',geometry=dict(type='Point',coordinates=[round(float(r['lon']),4),round(float(r['lat']),4)]),properties=p))
    else:
        c['entities_not_mapped']+=1; o=old.get(r['id'],{})
        reason=o.get('reason') or ('proposed row from the Oct 2026 company list (unverified); no usable address' if prop else 'no usable coordinates in source')
        um.append(dict(id=r['id'],layer='entity',name=p['name'],district=p['district'],reason=reason,src_precision=o.get('src_precision',r['coord_precision'])))
for r in rd(SRC+'/droppoints_public.csv'):
    c['drop_points_total']+=1
    p={k:clean(r.get(k,'')) for k in DPK}; p['layer']='drop_point'; p['geocoded_by_atlas']=r['coord_status'].startswith('approximate')
    if num(r['lat']) and num(r['lon']):
        c['drop_points_mapped']+=1; c['drop_points_geocoded_by_atlas']+=p['geocoded_by_atlas']
        feats.append(dict(type='Feature',geometry=dict(type='Point',coordinates=[round(float(r['lon']),4),round(float(r['lat']),4)]),properties=p))
    else:
        c['drop_points_not_mapped']+=1; o=old.get(r['point_id'],{})
        um.append(dict(id=r['point_id'],layer='drop_point',name=p['point_name'],district='',reason=o.get('reason','no usable coordinates in source'),src_precision=o.get('src_precision',r['coord_precision'])))
meta=dict(src='data/merged/ (Anavaratha merge v2, 2026-11-17) ← phase1 DIRECTORY_WASTE_OPERATORS_LK (+_droppoints)',removed_fields=['address','contact_public','price'],scrubbed='phone/email patterns in remaining text',status='listed, not verified on ground',
  geocoded_by_atlas="approximate locality centroids from the row's own address (Nominatim/OSM, district-checked), written back into the directory; flagged geocoded_by_atlas=true / coord_status=approximate",
  merge='8 duplicate ids folded into canonical rows (see aliases); 6 proposed rows from the Oct 2026 list are unverified; evidence_status and domain tags follow the charter',counts=c)
json.dump(dict(type='FeatureCollection',meta=meta,features=feats),open(SITE+'/public/data/operators_public.geojson','w'),ensure_ascii=False)
json.dump(dict(meta=dict(src=meta['src'],note='rows with no usable coordinates; reason per row. No coordinates invented.'),rows=um),open(op,'w'),indent=1,ensure_ascii=False)
json.dump(c|dict(features=len(feats)),open(SITE+'/src/data/geo_meta.json','w'),indent=1)
print(json.dumps(c|dict(features=len(feats))))
