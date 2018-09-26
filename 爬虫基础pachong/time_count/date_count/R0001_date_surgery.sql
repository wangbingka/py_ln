select '手术记录手术开始时间', '手术','住院',
year(surgery.surgery_start_date) as year1,month(surgery.surgery_start_date) as month1,
count(*) 
from general_surgery_record a 
group by year(surgery.surgery_start_date) ,month(surgery.surgery_start_date)
order by year1,month1
limit 1000