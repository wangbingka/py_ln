select '住院发药记录退药时间年份统计', b1.class_name,'住院',
year(b1.return_datetime) as year1,month(b1.return_datetime) as month1,
count(*) 
from inpatient_medication_dispense a 
lateral view outer explode(a.return) b as b1
group by  b1.class_name,year(b1.return_datetime),month(b1.return_datetime)
order by b1.class_name,year1,month1