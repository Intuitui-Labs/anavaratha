from pathlib import Path
import csv
base=Path('/home/ubuntu/anavaratha')
out=base/'ANAVARATHA_DEMO01_UNKNOWN_MIDDLE_PROCESS_REGISTER.csv'
fields=['unknown_id','possible_middle_process','why_it_could_explain_field_difference','what_current_data_show','what_is_not_shown','required_measurement','interpretation_status']
rows=[
['UM01','Running capacity is a nominal or administrative value rather than accepted input','Running capacity may describe facility capability or intended operation without proving that equivalent material entered','Only reported running-capacity field exists','Accepted input mass and definition of running capacity absent','Weighbridge or load records by day and stream','open_hypothesis'],
['UM02','Input was rejected before composting','Contamination or unsuitable material can reduce accepted feed without reducing reported running field','Study and WMA documents mention contamination','Station-level rejected input mass absent','Incoming mass and accepted/rejected mass by load','documented_possible_process'],
['UM03','Material remained in process or maturation stock','Composting requires time and space; output during period may not equal processed input','Actual production and sales are reported','Opening stock closing stock batch ages absent','Stock inventory and batch tracking','open_hypothesis'],
['UM04','Moisture or volatile matter changed mass','Decomposition and evaporation can change wet mass','Study field basis not sufficient for full conversion','Moisture content and dry-matter basis absent','Paired wet/dry mass and composition','open_hypothesis'],
['UM05','Material was diverted to another use or facility','Some accepted material may have been transferred, sold, reused, or disposed outside the station boundary','Station-level output/sales fields exist','External transfers and route records absent','Load-level destination manifest','open_hypothesis'],
['UM06','Equipment or labour downtime reduced actual processing','Reported running capacity may not represent daily uptime or effective labour','Employee counts and operating days are available in part','Machine uptime maintenance attendance and labour-hours absent','Downtime log maintenance log attendance/task log','documented_possible_process'],
['UM07','Output definition differs from running-capacity definition','Capacity may be feed capacity, process capacity, or theoretical output while actual production is saleable finished compost','Field definitions are not fully harmonized','Technical definitions and basis absent','Data dictionary and facility process specification','open_hypothesis'],
['UM08','Measurement or aggregation error','Field values may be estimated, rounded, self-reported, or aggregated from different periods','Some stations exceed design and some sales exceed production','Independent validation and matched periods absent','Raw records audit and period reconciliation','observed_data_quality_warning'],
['UM09','Rejects or residuals left the facility through an unrecorded pathway','Low output may coexist with disposal or leakage rather than transformation','Residual destinations are not available','Reject/residual mass and destination absent','Residual manifest and receiver verification','open_hypothesis'],
['UM10','Sales draw on prior stock or different period','Sales above current production can occur if inventory carries over','Four station records report sales above production','Opening/closing stock and sale period basis absent','Inventory reconciliation and sales-period definition','observed_boundary_warning'],
['UM11','Data are correct but facility process is genuinely low-output','Low output may reflect process failure or unsuitable conditions','Low production/running is widespread in reported station fields','Causal mechanism absent','Current process observation with input/output measurement','open_hypothesis'],
['UM12','Unmeasured informal recovery or worker take-home/use','Some materials may leave through informal or non-standard channels before final output accounting','Informal recovery is documented in broader system context','Station-level channel records absent','Material-channel observation and worker-inclusive accounting','open_hypothesis'],
]
with out.open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(fields); w.writerows(rows)
print('rewrote',out,'rows',len(rows),'fields',len(fields))
