from pathlib import Path
import geopandas as gpd
import pandas as pd
import json

base = Path('/home/ubuntu/anavaratha')
rows = []
for name, path in [
    ('district_population_join', base/'CPH2024_district_denominators.geojson'),
    ('osm_waste_sites', base/'OSM_Sri_Lanka_waste_sites.geojson'),
    ('osm_receiving_environments', base/'OSM_Sri_Lanka_receiving_environments.geojson'),
]:
    gdf = gpd.read_file(path)
    geom_valid = gdf.geometry.notna() & ~gdf.geometry.is_empty
    id_col = 'osm_id' if 'osm_id' in gdf.columns else ('adm2_pcode' if 'adm2_pcode' in gdf.columns else None)
    duplicate_ids = int(gdf[id_col].duplicated().sum()) if id_col else None
    rows.append({
        'layer': name, 'path': str(path.name), 'features': len(gdf),
        'crs': str(gdf.crs), 'valid_geometry': int(geom_valid.sum()),
        'missing_geometry': int((~geom_valid).sum()), 'duplicate_id_count': duplicate_ids,
        'minx': gdf.total_bounds[0], 'miny': gdf.total_bounds[1], 'maxx': gdf.total_bounds[2], 'maxy': gdf.total_bounds[3],
        'date_or_snapshot_field': 'osm_timestamp' if 'osm_timestamp' in gdf.columns else ('valid_on' if 'valid_on' in gdf.columns else None)
    })

audit = pd.DataFrame(rows)
audit.to_csv(base/'ANAVARATHA_GIS_LAYER_INTEGRITY_AUDIT_V0_1.csv', index=False)
print(audit.to_string(index=False))
# Layer-specific checks
admin = gpd.read_file(base/'CPH2024_district_denominators.geojson')
print(f'admin2_population_missing={int(admin.population_2024.isna().sum())} admin2_codes_unique={admin.adm2_pcode.nunique()}')
waste = gpd.read_file(base/'OSM_Sri_Lanka_waste_sites.geojson')
print(f'waste_osm_id_unique={waste.osm_id.nunique()} categories_missing_name={int(waste.name.isna().sum())}')
env = gpd.read_file(base/'OSM_Sri_Lanka_receiving_environments.geojson')
print('environment_categories:')
print(env.category.value_counts(dropna=False).to_string())
print('waste_snapshot_values:')
print(waste.osm_timestamp.dropna().unique())
print('environment_snapshot_values:')
print(env.osm_timestamp.dropna().unique())
