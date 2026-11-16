"""Geocode unmapped directory rows from their OWN address/district fields only.
Locality = last address segment (not a road). Nominatim (OSM), 1 req/1.1 s, cached.
Accept only place-type hits (city/town/village/suburb/hamlet/neighbourhood/quarter)
and, when the row has a district, only if Nominatim's district matches it.
Everything else stays unmapped with a reason. No coordinates are invented."""
import csv, json, re, time, os, urllib.request, urllib.parse
P='/workspace/viz/_src_snapshot/phase1'; CACHE='/workspace/viz/data/_geocode_cache.json'
cache=json.load(open(CACHE)) if os.path.exists(CACHE) else {}
UA='anavaratha-atlas-geocode/0.1 (Intuitui Labs research prototype; box)'
PLACE={'city','town','village','suburb','hamlet','neighbourhood','quarter','isolated_dwelling','locality','municipality','city_district'}
ROAD=re.compile(r'\b(road|rd|mawatha|mw|street|st|lane|place|avenue|junction|highway|cross|watta|complex|building|floor|no:?)\b',re.I)
def localities(addr):
    addr=re.sub(r'\([^)]*\)','',addr)
    segs=[s.strip(' .') for s in re.split(r',',addr) if s.strip(' .')]
    out=[]
    for s in reversed(segs):
        s2=re.sub(r'\b\d{5}\b','',s).strip(' .')
        if not s2 or re.match(r'^(no\.?\s*)?\d',s2,re.I) or ROAD.search(s2) or s2.lower() in('sri lanka',): continue
        out.append(s2)
        if len(out)==2: break
    v=[]
    for o in out:
        v.append(o)
        if 'w' in o.lower(): v.append(re.sub('w','v',o,count=1,flags=re.I))
    return v
MULTI=re.compile(r'not found|not geocoded|multiple|serves |shops|outlets|itinerant|rotating|island-wide|;|/.*/.*area',re.I)
def q(text):
    if text in cache: return cache[text]
    url='https://nominatim.openstreetmap.org/search?'+urllib.parse.urlencode(dict(q=text,format='jsonv2',addressdetails=1,limit=5,countrycodes='lk'))
    req=urllib.request.Request(url,headers={'User-Agent':UA})
    try: res=json.load(urllib.request.urlopen(req,timeout=20))
    except Exception as e: res={'error':str(e)}
    cache[text]=res; time.sleep(1.1); return res
def geocode(addr,district):
    tried=[]
    for loc in localities(addr):
        for text in ([f'{loc}, {district} District, Sri Lanka'] if district else [])+[f'{loc}, Sri Lanka']:
            tried.append(text); res=q(text)
            if isinstance(res,dict): continue
            for r in res:
                if r.get('addresstype') not in PLACE: continue
                sd=(r['address'].get('state_district') or '')
                if district and district.lower() not in sd.lower(): continue
                return dict(lat=round(float(r['lat']),4),lon=round(float(r['lon']),4),
                    precision=f'approx: {r["addresstype"]} centroid "{loc}" via Nominatim (OSM){", district-checked: "+sd if district else ""}; geocoded 2026-11-16 for atlas'),tried
    return None,tried
out={}
ents=[x for x in csv.DictReader(open(P+'/DIRECTORY_WASTE_OPERATORS_LK.csv')) if x['lat'] in('','not found')]
dps=[x for x in csv.DictReader(open(P+'/DIRECTORY_WASTE_OPERATORS_LK_droppoints.csv')) if x['lat'] in('','not found')]
for x in ents:
    d=x['district'] if x['district'] and x['district'] not in('not found','island-wide') and ';' not in x['district'] else ''
    a=x['address']
    if a in('','not found') or re.search(r'not found|not geocoded',a,re.I):
        out[x['id']]=dict(status='unmapped',reason='no usable address in source' + (f' (district only: {x["district"]})' if x['district'] not in ('','not found') else '')); continue
    if MULTI.search(a):
        out[x['id']]=dict(status='unmapped',reason='multi-site, itinerant or service-area entry; no single address in source'); continue
    if False:
        out[x['id']]=dict(status='unmapped',reason='no street/locality address in source' + (f' (district: {x["district"]})' if x['district'] not in ('','not found') else '')); continue
    g,t=geocode(a,d)
    out[x['id']]=dict(status='mapped',**g) if g else dict(status='unmapped',reason=('locality not resolved in stated district' if d else 'locality not resolved')+f' (tried: {"; ".join(t[:3])})' if t else 'address has no locality segment')
for x in dps:
    a=x['address']
    if a in('','not found'):
        out[x['point_id']]=dict(status='unmapped',reason='no address in source'); continue
    g,t=geocode(a,'')
    out[x['point_id']]=dict(status='mapped',**g) if g else dict(status='unmapped',reason='locality not resolved'+(f' (tried: {"; ".join(t[:2])})' if t else ' (address has no locality segment)'))
json.dump(cache,open(CACHE,'w'))
json.dump(out,open('/workspace/viz/data/_geocode_results.json','w'),indent=1,ensure_ascii=False)
import collections; print(collections.Counter((k[:5],v['status']) for k,v in out.items()))
