select '入院记录入院时间','入院记录','住院',
year(inpatient_info.admission_time) as year1,month(inpatient_info.admission_time) as month1,
count(*)  
from admission_record a  
group by year(inpatient_info.admission_time),month(inpatient_info.admission_time)
order by year1,month1
limit 2000;