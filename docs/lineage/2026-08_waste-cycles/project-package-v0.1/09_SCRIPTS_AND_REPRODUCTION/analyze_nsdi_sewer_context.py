from pathlib import Path
import geopandas as gpd
import pandas as pd

base = Path('/home/ubuntu/anavaratha')
districts = gpd.read_file(base / 'CPH2024_district_denominators.geojson')
all_rows = []
for layer_id, label in [(10,'sewer_interceptor_manhole'),(11,'sewer_manhole'),(13,'sewer_force_main'),(14,'sewer_gravity_main'),(15,'sewer_lateral_pipeline')]:
    path = base / f'nsdi_sewer_{layer_id}.geojson'
    gdf = gpd.read_file(path)
    gdf['nsdi_layer_id'] = layer_id
    gdf['nsdi_layer'] = label
    all_rows.append(gdf)
    print(f'{label}_features={len(gdf)} geometry={gdf.geom_type.value_counts().to_dict()}')
all_features = gpd.GeoDataFrame(pd.concat(all_rows, ignore_index=True), crs=all_rows[0].crs)
joined = gpd.sjoin(all_features, districts[['adm2_name','adm2_pcode','population_2024','geometry']], how='left', predicate='within')
summary = joined.groupby(['adm2_name','adm2_pcode','population_2024','nsdi_layer'], dropna=False).size().rename('feature_count').reset_index()
pivot = summary.pivot_table(index=['adm2_name','adm2_pcode','population_2024'], columns='nsdi_layer', values='feature_count', fill_value=0).reset_index()
for c in ['sewer_interceptor_manhole','sewer_manhole','sewer_force_main','sewer_gravity_main','sewer_lateral_pipeline']:
    if c not in pivot: pivot[c] = 0
pivot['nsdi_sewer_feature_total'] = pivot[['sewer_interceptor_manhole','sewer_manhole','sewer_force_main','sewer_gravity_main','sewer_lateral_pipeline']].sum(axis=1)
pivot['nsdi_status'] = 'official_NS​​DI_utility_proxy__not_solid_waste_capacity'
pivot.to_csv(base / 'ANAVARATHA_NSDI_SEWER_FEATURES_BY_DISTRICT_V0_1.csv', index=False)
joined.drop(columns='geometry').to_csv(base / 'ANAVARATHA_NSDI_SEWER_FEATURES_JOIN_AUDIT.csv', index=False)
print('\ndistrict_summary:')
print(pivot.sort_values('nsdi_sewer_feature_total', ascending=False).to_string(index=False))
