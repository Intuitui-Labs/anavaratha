from pathlib import Path
import pandas as pd
import numpy as np

base=Path('/home/ubuntu/anavaratha')
st=pd.read_csv(base/'ANAVARATHA_MANIPURA_2025_WESTERN_PROVINCE_22_STATIONS.csv')
agg=pd.read_csv(base/'ANAVARATHA_MANIPURA_2025_AGGREGATE_REALITY_SUMMARY.csv')
agg_metric_col=agg.columns[0]
agg=agg.set_index(agg_metric_col)
plan=pd.read_csv(base/'ANAVARATHA_WMA_WESTERN_CAPACITY_SERIES.csv')

# station distributions
metrics={
 'running_vs_design_pct':st['running_vs_design_pct'],
 'production_vs_running_pct':st['production_vs_running_pct'],
 'sales_vs_production_pct':st['sales_vs_production_pct'],
 'production_t_month':st['actual_compost_production_t_month'],
 'employees':st['employees']
}
summary=[]
for name,s in metrics.items():
    summary.append({'metric':name,'n':int(s.notna().sum()),'mean':float(s.mean()),'median':float(s.median()),'p10':float(s.quantile(.1)), 'p90':float(s.quantile(.9)), 'min':float(s.min()), 'max':float(s.max())})
dist=pd.DataFrame(summary)

# plan base/near-term records only; no inferred actual-vs-plan comparison
p2022=plan[plan.year==2022].iloc[0]
p2024=plan[plan.year==2024].iloc[0]
p2026=plan[plan.year==2026].iloc[0]
plan_comparison=pd.DataFrame([
 {'comparison':'2022 WMA plan total compost capacity / collected biodegradable waste','value_pct':float(p2022.compost_capacity_coverage_pct),'interpretation':'Plan baseline ratio; not realized utilization'},
 {'comparison':'2022 WMA plan direct final disposal / collected biodegradable waste','value_pct':float(p2022.direct_disposal_pct),'interpretation':'Plan baseline ratio; not independently measured current disposal'},
 {'comparison':'2024 WMA plan total compost capacity / collected biodegradable waste','value_pct':float(p2024.compost_capacity_coverage_pct),'interpretation':'Near-term plan ratio; not delivered capacity'},
 {'comparison':'2026 WMA plan total compost capacity / collected biodegradable waste','value_pct':float(p2026.compost_capacity_coverage_pct),'interpretation':'Near-term plan ratio; not delivered capacity'},
 {'comparison':'22-station actual production / running capacity (2022 monthly dataset)','value_pct':float(agg.loc['aggregate_production_as_pct_running','value']),'interpretation':'Observed/reported subset ratio; not whole-province ratio'},
 {'comparison':'22-station running capacity / design capacity (2022 monthly dataset)','value_pct':float(agg.loc['aggregate_running_as_pct_design','value']),'interpretation':'Observed/reported subset ratio; not whole-province ratio'},
])

# explicit compatibility matrix
compat=pd.DataFrame([
 {'dataset_a':'22 compost stations','dataset_b':'WMA Table 4-21 2022','compatible_for_direct_addition':False,'reason':'Different facility boundary: 22 surveyed stations versus province-wide plan categories; monthly station values versus t/day plan series; compost station scope versus all LA/waste-park/TRF flows.'},
 {'dataset_a':'22 compost stations','dataset_b':'WMA 28 composting facilities','compatible_for_direct_addition':False,'reason':'22-study station sample is not proven identical to all 28 facilities; facility identities and stream boundaries are not fully reconciled.'},
 {'dataset_a':'WMA 2020 baseline','dataset_b':'WMA 2022 plan baseline','compatible_for_direct_addition':False,'reason':'Different base years and plan revisions; same document but not a demonstrated time-series measurement system.'},
 {'dataset_a':'WMA plan targets','dataset_b':'current operational reality','compatible_for_direct_addition':False,'reason':'Future targets/design assumptions require delivery, uptime, throughput, maintenance, and audit evidence.'},
])

st.to_csv(base/'ANAVARATHA_WESTERN_STATION_ANALYTICS_FULL.csv',index=False)
dist.to_csv(base/'ANAVARATHA_WESTERN_STATION_DISTRIBUTION_SUMMARY.csv',index=False)
plan_comparison.to_csv(base/'ANAVARATHA_WESTERN_PLAN_VS_OPERATIONAL_COMPARISON.csv',index=False)
compat.to_csv(base/'ANAVARATHA_WESTERN_DATA_COMPATIBILITY_MATRIX.csv',index=False)

print('station_count',len(st))
print('stations_production_below_10pct_running',int((st.production_vs_running_pct<10).sum()))
print('stations_over_design_running_capacity',int((st.running_capacity_t_month>st.design_capacity_t_month).sum()))
print('stations_sales_over_production',int((st.compost_sales_t_month>st.actual_compost_production_t_month).sum()))
print('aggregate_station_metrics')
print(agg.to_string())
print('distribution')
print(dist.to_string(index=False))
print('plan_comparison')
print(plan_comparison.to_string(index=False))
print('compatibility_matrix')
print(compat.to_string(index=False))
