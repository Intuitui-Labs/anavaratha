from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

base=Path('/home/ubuntu/anavaratha')
rows=[
(2022,896,237,325,0,92,232,324,334),
(2023,962,199,399,0,103,297,400,364),
(2024,1021,171,596,160,110,340,610,254),
(2025,1084,136,611,160,117,340,610,337),
(2026,1146,108,677,240,130,340,710,361),
(2027,1207,72,692,240,131,340,710,443),
(2028,1266,566,700,320,131,340,790,0),
(2029,1335,591,744,320,131,340,790,0),
(2030,1402,616,786,400,131,340,870,0),
(2031,1479,638,841,400,136,340,870,0),
(2032,1525,650,875,400,136,364,900,0),
(2033,1594,668,926,400,136,414,950,0),
(2034,1662,741,921,400,136,414,950,0),
(2035,1717,757,960,400,136,464,1000,0),
(2036,1782,772,1006,400,136,464,1000,4),
(2037,1856,793,1063,400,136,524,1060,0),
(2038,1926,806,1120,400,136,584,1120,0),
(2039,1997,822,1175,400,136,644,1180,0),
(2040,2063,832,1231,400,136,694,1230,0),
(2041,2143,850,1293,400,136,764,1300,0),
(2042,2226,868,1332,400,136,794,1330,26),
]
cols=['year','biodegradable_collected_t_day','treated_LA_compost_t_day','treated_waste_parks_t_day','treated_TRF_t_day','cluster_compost_capacity_t_day','waste_park_compost_capacity_t_day','total_compost_capacity_t_day','direct_final_disposal_t_day']
df=pd.DataFrame(rows,columns=cols)
df['treated_total_t_day']=df[['treated_LA_compost_t_day','treated_waste_parks_t_day','treated_TRF_t_day']].sum(axis=1)
df['compost_capacity_coverage_pct']=df.total_compost_capacity_t_day/df.biodegradable_collected_t_day*100
df['direct_disposal_pct']=df.direct_final_disposal_t_day/df.biodegradable_collected_t_day*100
df['treated_share_pct']=df.treated_total_t_day/df.biodegradable_collected_t_day*100
df['record_type']=df.year.map(lambda y:'base/near-term plan year' if y<=2022 else ('near-term planned year' if y<=2027 else 'long-term planned year'))
df['source']='WMA Western Province Solid Waste Management Master Plan, Table 4-21'
df['source_period']='2022-2042 plan series'
df['caution']='Plan series mixes base-year/estimated quantities with planned future targets; not realized capacity'
df.to_csv(base/'ANAVARATHA_WMA_WESTERN_CAPACITY_SERIES.csv',index=False)
print(df.to_string(index=False))
print('\nSelected metrics:')
print(df.loc[df.year.isin([2022,2024,2026,2028,2030,2042]),['year','biodegradable_collected_t_day','treated_total_t_day','total_compost_capacity_t_day','compost_capacity_coverage_pct','direct_final_disposal_t_day','direct_disposal_pct','record_type']].to_string(index=False))

fig,ax=plt.subplots(figsize=(12,6))
ax.plot(df.year,df.biodegradable_collected_t_day,label='Collected biodegradable waste',lw=2.5,color='#264653')
ax.plot(df.year,df.total_compost_capacity_t_day,label='Total planned compost capacity',lw=2.5,color='#2a9d8f')
ax.plot(df.year,df.treated_total_t_day,label='Treatment shown in table',lw=2,color='#e9c46a')
ax.plot(df.year,df.direct_final_disposal_t_day,label='Direct final disposal',lw=2,color='#e76f51')
ax.axvline(2022,color='grey',ls='--',lw=1)
ax.text(2022.15,df.biodegradable_collected_t_day.max()*0.95,'2022 table baseline',fontsize=9,color='grey')
ax.set_title('Western Province master-plan biodegradable-waste series')
ax.set_xlabel('Year in plan')
ax.set_ylabel('Tons per day')
ax.legend(frameon=True)
ax.grid(alpha=.25)
fig.tight_layout()
fig.savefig(base/'ANAVARATHA_WMA_WESTERN_CAPACITY_SERIES.png',dpi=220)
