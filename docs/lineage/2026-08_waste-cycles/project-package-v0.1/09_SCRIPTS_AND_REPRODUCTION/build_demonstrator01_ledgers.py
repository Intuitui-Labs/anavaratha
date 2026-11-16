from pathlib import Path
import pandas as pd
import numpy as np

base=Path('/home/ubuntu/anavaratha')
st=pd.read_csv(base/'ANAVARATHA_MANIPURA_2025_WESTERN_PROVINCE_22_STATIONS.csv')

material=pd.DataFrame({
    'local_authority':st['local_authority'],
    'code':st['code'],
    'data_period':st['data_period'],
    'design_capacity_t_month':st['design_capacity_t_month'],
    'running_capacity_t_month':st['running_capacity_t_month'],
    'actual_compost_production_t_month':st['actual_compost_production_t_month'],
    'compost_sales_t_month':st['compost_sales_t_month'],
    'reported_capacity_output_difference_t_month':st['running_capacity_t_month']-st['actual_compost_production_t_month'],
    'reported_design_running_difference_t_month':st['design_capacity_t_month']-st['running_capacity_t_month'],
    'production_as_pct_running':st['production_vs_running_pct'],
    'running_as_pct_design':st['running_vs_design_pct'],
    'sales_as_pct_production':st['sales_vs_production_pct'],
    'rejects_t_month':'unknown',
    'residuals_t_month':'unknown',
    'opening_stock_t_month':'unknown',
    'closing_stock_t_month':'unknown',
    'measurement_error_t_month':'unknown',
    'mass_balance_status':'not_calculable_from_available_fields',
    'source':'Manipura et al. 2025 supplementary/station table'
})

diss=pd.DataFrame({
    'local_authority':st['local_authority'],
    'code':st['code'],
    'reported_capacity_output_difference_t_month':st['running_capacity_t_month']-st['actual_compost_production_t_month'],
    'reported_output_as_pct_running':st['production_vs_running_pct'],
    'reported_design_output_difference_t_month':st['design_capacity_t_month']-st['actual_compost_production_t_month'],
    'sales_minus_production_t_month':st['compost_sales_t_month']-st['actual_compost_production_t_month'],
    'possible_stock_or_boundary_warning':np.where(st['compost_sales_t_month']>st['actual_compost_production_t_month'],'yes','no'),
    'physical_entropy_production_calculated':'no',
    'operational_diagnostic':'reported_capacity_output_difference; middle_process_unknown',
    'interpretation':'descriptive proxy; not thermodynamic entropy'
})

cap=pd.DataFrame({
    'local_authority':st['local_authority'],
    'code':st['code'],
    'employees':st['employees'],
    'operating_days_per_month':st['operating_days_per_month'],
    'running_as_pct_design':st['running_vs_design_pct'],
    'production_as_pct_running':st['production_vs_running_pct'],
    'production_per_employee_t_month':st['actual_compost_production_t_month']/st['employees'],
    'source_over_design_flag':st['source_over_design_flag'],
    'capacity_capability_interpretation':'requires current validation; source reports output and staffing but not attendance, downtime, maintenance, quality, or residual route'
})

unc=pd.DataFrame([
 {'field':'incoming accepted mass','availability':'not available in 22-station table','why_it_matters':'needed for accepted-input denominator'},
 {'field':'rejects and residuals','availability':'not available','why_it_matters':'prevents claiming material closure'},
 {'field':'opening/closing stock','availability':'not available','why_it_matters':'sales above current production may reflect stock'},
 {'field':'equipment downtime and maintenance','availability':'not complete in station CSV','why_it_matters':'tests usable capacity'},
 {'field':'staff attendance and hours','availability':'employee count only','why_it_matters':'tests effective labour capacity'},
 {'field':'compost quality and contamination','availability':'not complete in station CSV','why_it_matters':'tests product usefulness and quality dissipation'},
 {'field':'residual destination','availability':'not available','why_it_matters':'tests burden transfer'},
 {'field':'current 2026 status','availability':'not established','why_it_matters':'2022 evidence cannot prove current operation'},
])

material.to_csv(base/'ANAVARATHA_DEMO01_MATERIAL_LEDGER.csv',index=False)
diss.to_csv(base/'ANAVARATHA_DEMO01_DISSIPATION_LEDGER.csv',index=False)
cap.to_csv(base/'ANAVARATHA_DEMO01_CAPABILITY_LEDGER.csv',index=False)
unc.to_csv(base/'ANAVARATHA_DEMO01_UNCERTAINTY_LEDGER.csv',index=False)
print('material_rows',len(material))
print('dissipation_rows',len(diss))
print('capability_rows',len(cap))
print('uncertainty_rows',len(unc))
print('aggregate_reported_capacity_output_difference_t_month',float(material.reported_capacity_output_difference_t_month.sum()))
print('aggregate_reported_design_running_difference_t_month',float(material.reported_design_running_difference_t_month.sum()))
print('sales_above_production_count',int((st.compost_sales_t_month>st.actual_compost_production_t_month).sum()))
