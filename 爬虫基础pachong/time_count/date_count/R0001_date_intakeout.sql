select '出入量表时间',department_type,b1.io_type, 
year(b1.io_datetime) as year1,month(b1.io_datetime) as month1,count(*)
from intake_output a
lateral view outer explode(a.intake_output) b as b1
group by department_type,b1.io_type, year(b1.io_datetime),month(b1.io_datetime)
order by department_type,b1.io_type,year1,month1
limit 5000;