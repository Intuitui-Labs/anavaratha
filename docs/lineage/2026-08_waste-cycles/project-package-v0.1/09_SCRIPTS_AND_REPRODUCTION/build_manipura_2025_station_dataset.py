from pathlib import Path
import pandas as pd

base=Path('/home/ubuntu/anavaratha')
rows=[
('Kaduwela','KMC',275.0,225.0,1750,15.6,38,12.4,False),
('Kotikawatte','KWPS',50.0,57.5,235,2.1,6,1.1,True),
('Seethawakapura','SPUC',125.0,75.0,573,12.5,21,12.5,False),
('Seethawaka','SPS',50.0,92.5,326,5.1,12,5.1,True),
('Attanagalla','ATPS',200.0,170.0,662,13.0,8,10.0,False),
('Divulapitiya','DPS',100.0,37.5,468,6.5,9,6.2,False),
('Katana','KPS',175.0,200.0,920,18.0,7,18.0,True),
('Kelaniya','KLPS',125.0,90.0,525,1.3,17,3.0,False),
('Ja Ela','JEUC',75.0,31.3,496,5.8,9,3.8,False),
('Ja Ela','JEPS',250.0,200.0,845,18.9,6,12.7,False),
('Meerigama','MRPS',75.0,100.0,320,8.0,10,6.4,True),
('Minuwangoda','MGPS',50.0,75.0,1850,0.1,9,0.1,True),
('Negombo','NMC',250.0,187.5,1757,19.9,5,22.1,False),
('Agalawatte','AWPS',75.0,50.0,282,5.4,8,5.7,False),
('Beruwala','BPS',100.0,37.5,302,3.1,9,2.4,False),
('Bulathsinhala','BSPS',150.0,50.0,493,4.0,10,4.0,False),
('Horana','HPS',250.0,225.0,1036,10.4,16,9.2,False),
('Madurawala','MPS',50.0,50.0,238,1.7,10,1.6,False),
('Millaniya','MLPS',75.0,112.5,140,1.3,16,1.3,True),
('Mathugama','MTPS',150.0,275.0,546,2.8,16,2.8,True),
('Palindanuwara','PNPS',50.0,25.0,226,0.7,8,1.2,False),
('Walallawita','WWPS',75.0,25.0,650,0.8,4,0.8,False),
]
cols=['local_authority','code','design_capacity_t_month','running_capacity_t_month','facility_area_m2','actual_compost_production_t_month','employees','compost_sales_t_month','source_over_design_flag']
df=pd.DataFrame(rows,columns=cols)
df['operating_days_per_month']=25
df['running_vs_design_pct']=df['running_capacity_t_month']/df['design_capacity_t_month']*100
df['production_vs_running_pct']=df['actual_compost_production_t_month']/df['running_capacity_t_month']*100
df['sales_vs_production_pct']=df['compost_sales_t_month']/df['actual_compost_production_t_month']*100
df['source']='Manipura et al. 2025, Table 1; field survey and WMA (Western Province)'
df['data_period']='January–December 2022 monthly averages'
df['interpretation_caution']='Sales may include previously unsold stock; production/running capacity boundaries differ; no current-status inference'
out=base/'ANAVARATHA_MANIPURA_2025_WESTERN_PROVINCE_22_STATIONS.csv'
df.to_csv(out,index=False)
print(df.to_string(index=False))
print('\nTotals:')
print(df[['design_capacity_t_month','running_capacity_t_month','facility_area_m2','actual_compost_production_t_month','employees','compost_sales_t_month']].sum())
print('below_design',int((df.running_capacity_t_month<df.design_capacity_t_month).sum()),'over_design',int((df.running_capacity_t_month>df.design_capacity_t_month).sum()),'equal',int((df.running_capacity_t_month==df.design_capacity_t_month).sum()))
