from pathlib import Path
import geopandas as gpd
import pandas as pd
import zipfile

base = Path('/home/ubuntu/anavaratha')
zip_path = base / 'lka_admin_boundaries.shp.zip'
out = base / 'lka_admin_boundaries_unzipped'
out.mkdir(exist_ok=True)
if not (out / 'lka_admin2.shp').exists():
    with zipfile.ZipFile(zip_path) as z:
        names = [n for n in z.namelist() if any(n.endswith(ext) for ext in ('.shp','.shx','.dbf','.prj','.cpg')) and ('lka_admin2.' in n or 'lka_admin1.' in n)]
        z.extractall(out, members=names)

admin2 = gpd.read_file(out / 'lka_admin2.shp')
den = pd.read_csv(base / 'CPH2024_district_denominators.csv')
admin2['district_key'] = admin2['adm2_name'].str.strip().str.casefold()
den['district_key'] = den['district'].str.strip().str.casefold()
# Source spelling variant: boundary source uses Monaragala; DCS census uses Moneragala.
name_normalization = {'monaragala': 'moneragala'}
admin2['district_key'] = admin2['district_key'].replace(name_normalization)
joined = admin2.merge(den, on='district_key', how='left', suffixes=('_boundary','_census'))
joined['census_join_status'] = joined['population_2024'].notna().map({True:'matched', False:'unmatched'})
print(f'boundary_rows={len(admin2)} census_rows={len(den)} matched={joined["population_2024"].notna().sum()} unmatched={joined["population_2024"].isna().sum()}')
print(joined[['adm2_name','adm2_pcode','area_sqkm','population_2024','households_2024','census_join_status']].sort_values('adm2_name').to_string(index=False))
joined.to_file(base / 'CPH2024_district_denominators.geojson', driver='GeoJSON')
joined.drop(columns='geometry').to_csv(base / 'CPH2024_district_denominators_join_audit.csv', index=False)
