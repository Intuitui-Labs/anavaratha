from pathlib import Path
import pandas as pd

base=Path('/home/ubuntu/anavaratha')
path=base/'ANAVARATHA_IWMI_HISTORICAL_CAPACITY_FACILITY_REGISTER_V0_1.csv'
df=pd.read_csv(path)
df['design_capacity_mt_day_high']=pd.NA
df['utilization_comparability']='not calculated'
df['utilization_low_pct']=pd.NA
df['utilization_high_pct']=pd.NA
# Design ranges or compatible facility boundaries taken from the source text.
design_high={'FAC-02':30.0}
for rid,v in design_high.items(): df.loc[df.record_id==rid,'design_capacity_mt_day_high']=v
compatible=['FAC-02','FAC-03','FAC-04','FAC-06','FAC-07','FAC-08','FAC-10']
for rid in compatible:
    row=df[df.record_id==rid].iloc[0]
    design_low=row['design_capacity_mt_day']; design_high_v=float(row['design_capacity_mt_day_high']) if pd.notna(row['design_capacity_mt_day_high']) else float(design_low)
    proc_low=row['processed_mt_day_low']; proc_high=row['processed_mt_day_high']
    if pd.notna(proc_low) and pd.notna(proc_high) and design_low>0 and design_high_v>0:
        # Range is conservative: min throughput / max design to max throughput / min design.
        df.loc[df.record_id==rid,'utilization_low_pct']=round(float(proc_low)/design_high_v*100,1)
        df.loc[df.record_id==rid,'utilization_high_pct']=round(float(proc_high)/design_low*100,1)
        df.loc[df.record_id==rid,'utilization_comparability']='same facility boundary and MT/day design/processed units in source record'
for rid in ['FAC-01','FAC-05','FAC-09','FAC-11','FAC-12','FAC-13']:
    if rid in set(df.record_id):
        df.loc[df.record_id==rid,'utilization_comparability']='not calculated: unit, input/output boundary, or design-capacity limitation'
out=base/'ANAVARATHA_IWMI_CAPACITY_UTILIZATION_AUDIT_V0_1.csv'
df.to_csv(out,index=False)
print(df[df.record_type=='facility capacity record'][['record_id','city','design_capacity_mt_day','design_capacity_mt_day_high','processed_mt_day_low','processed_mt_day_high','utilization_low_pct','utilization_high_pct','utilization_comparability']].to_string(index=False))
