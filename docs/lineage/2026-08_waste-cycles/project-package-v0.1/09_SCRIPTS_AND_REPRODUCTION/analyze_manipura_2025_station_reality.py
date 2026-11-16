from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base=Path('/home/ubuntu/anavaratha')
df=pd.read_csv(base/'ANAVARATHA_MANIPURA_2025_WESTERN_PROVINCE_22_STATIONS.csv')
df['design_to_running_gap_pct']=100-df['running_vs_design_pct']
df['production_per_employee_t_month']=df['actual_compost_production_t_month']/df['employees']
df['production_per_area_t_m2_month']=df['actual_compost_production_t_month']/df['facility_area_m2']
df['sales_per_employee_t_month']=df['compost_sales_t_month']/df['employees']
df['production_below_10pct_running'] = df['production_vs_running_pct'] < 10
summary={
 'stations':len(df),
 'design_capacity_t_month':df.design_capacity_t_month.sum(),
 'running_capacity_t_month':df.running_capacity_t_month.sum(),
 'actual_production_t_month':df.actual_compost_production_t_month.sum(),
 'sales_t_month':df.compost_sales_t_month.sum(),
 'employees':df.employees.sum(),
 'aggregate_running_as_pct_design':df.running_capacity_t_month.sum()/df.design_capacity_t_month.sum()*100,
 'aggregate_production_as_pct_running':df.actual_compost_production_t_month.sum()/df.running_capacity_t_month.sum()*100,
 'aggregate_sales_as_pct_production':df.compost_sales_t_month.sum()/df.actual_compost_production_t_month.sum()*100,
 'mean_station_running_as_pct_design':df.running_vs_design_pct.mean(),
 'median_station_running_as_pct_design':df.running_vs_design_pct.median(),
 'below_design_count':int((df.running_capacity_t_month<df.design_capacity_t_month).sum()),
 'over_design_count':int((df.running_capacity_t_month>df.design_capacity_t_month).sum()),
 'equal_design_count':int((df.running_capacity_t_month==df.design_capacity_t_month).sum()),
 'stations_production_below_10pct_running':int(df.production_below_10pct_running.sum()),
 'mean_production_per_employee_t_month':df.production_per_employee_t_month.mean(),
}
pd.DataFrame([summary]).T.rename(columns={0:'value'}).to_csv(base/'ANAVARATHA_MANIPURA_2025_AGGREGATE_REALITY_SUMMARY.csv')
df.sort_values('production_vs_running_pct').to_csv(base/'ANAVARATHA_MANIPURA_2025_STATION_REALITY_DIAGNOSTICS.csv',index=False)
print(pd.Series(summary).to_string())
print('\nLowest production/running:')
print(df.sort_values('production_vs_running_pct')[['local_authority','code','running_vs_design_pct','production_vs_running_pct','actual_compost_production_t_month','employees']].head(10).to_string(index=False))
print('\nHighest production/running:')
print(df.sort_values('production_vs_running_pct',ascending=False)[['local_authority','code','running_vs_design_pct','production_vs_running_pct','actual_compost_production_t_month','employees']].head(10).to_string(index=False))

sns.set_theme(style='whitegrid')
fig,axes=plt.subplots(1,2,figsize=(13,5.5))
sns.scatterplot(data=df,x='running_capacity_t_month',y='actual_compost_production_t_month',hue='source_over_design_flag',palette={False:'#176b87',True:'#d95f02'},s=70,ax=axes[0])
axes[0].plot([0,300],[0,300],linestyle='--',color='grey',linewidth=1,label='production = running capacity')
axes[0].set_title('Running capacity versus actual compost production')
axes[0].set_xlabel('Reported running capacity (t/month)')
axes[0].set_ylabel('Actual compost production (t/month)')
axes[0].legend(title='Running > design')
sns.scatterplot(data=df,x='employees',y='actual_compost_production_t_month',hue='production_below_10pct_running',palette={False:'#2a9d8f',True:'#e76f51'},s=70,ax=axes[1])
axes[1].set_title('Staffing versus actual production')
axes[1].set_xlabel('Reported employees')
axes[1].set_ylabel('Actual compost production (t/month)')
axes[1].legend(title='Production <10% of running')
fig.suptitle('Sri Lanka Western Province compost stations — 2022 monthly averages',fontsize=14,y=1.02)
fig.tight_layout()
fig.savefig(base/'ANAVARATHA_MANIPURA_2025_CAPACITY_REALITY_DIAGNOSTICS.png',dpi=220,bbox_inches='tight')
