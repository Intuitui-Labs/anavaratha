from pathlib import Path
import pandas as pd
base=Path('/home/ubuntu/anavaratha')
st=pd.read_csv(base/'ANAVARATHA_MANIPURA_2025_WESTERN_PROVINCE_22_STATIONS.csv')
out=pd.DataFrame({
 'local_authority':st.local_authority,
 'code':st.code,
 'study_period':st.data_period,
 'reported_design_capacity_t_month':st.design_capacity_t_month,
 'reported_running_capacity_t_month':st.running_capacity_t_month,
 'reported_actual_compost_output_t_month':st.actual_compost_production_t_month,
 'reported_compost_sales_t_month':st.compost_sales_t_month,
 'reported_field_difference_running_minus_output_t_month':st.running_capacity_t_month-st.actual_compost_production_t_month,
 'reported_field_ratio_output_to_running_pct':st.production_vs_running_pct,
 'reported_field_difference_design_minus_running_t_month':st.design_capacity_t_month-st.running_capacity_t_month,
 'reported_field_ratio_running_to_design_pct':st.running_vs_design_pct,
 'sales_minus_output_t_month':st.compost_sales_t_month-st.actual_compost_production_t_month,
 'accepted_input_t_month':'not supplied',
 'rejected_input_t_month':'not supplied',
 'in_process_or_maturation_stock_t_month':'not supplied',
 'moisture_or_dry_matter_adjustment_t_month':'not supplied',
 'other_destination_or_diversion_t_month':'not supplied',
 'rejects_residuals_t_month':'not supplied',
 'measurement_or_period_reconciliation':'not supplied',
 'what_the_numeric_difference_is':'difference between reported fields only',
 'what_it_is_not':'not measured waste; not measured loss; not entropy; not unprocessed input',
 'source':'Manipura et al. 2025 Table 1 / archived derived station table'
})
out.to_csv(base/'ANAVARATHA_DEMO01_GAP_FORENSIC_TABLE.csv',index=False)
print('rows',len(out))
print('known_reported_running_minus_output_t_month',out.reported_field_difference_running_minus_output_t_month.sum())
print('known_reported_design_minus_running_t_month',out.reported_field_difference_design_minus_running_t_month.sum())
print('sales_above_output_rows',int((out.sales_minus_output_t_month>0).sum()))
print('accepted_input_known_rows',int((out.accepted_input_t_month!='not supplied').sum()))
