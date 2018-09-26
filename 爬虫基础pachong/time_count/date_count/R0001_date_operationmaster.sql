select '手术麻醉主记录手术开始时间', '手麻','住院',
year(key_event_timing.oper_start_time) as year1,month(key_event_timing.oper_start_time) as month1,
count(*) 
from operation_master_record a 
group by year(key_event_timing.oper_start_time),month(key_event_timing.oper_start_time)
order by year1,month1
limit 1000;