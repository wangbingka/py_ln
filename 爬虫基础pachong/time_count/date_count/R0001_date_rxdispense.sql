select '门急诊发药记录发药时间年份统计', b1.class_name,visit_type,
year(b1.dispense_datetime) as year1,month(b1.dispense_datetime) as month1,
count(*)  
from outpatient_and_emergency_medication_dispense a 
lateral view outer explode(a.dispense) b as b1
group by  b1.class_name,visit_type,year(b1.dispense_datetime),month(b1.dispense_datetime)
order by b1.class_name,visit_type,year1,month1
limit 2000