select '病情记录护理记录时间', '病情记录','住院',
year(b1) as year1,month(b1) as month1,
count(*)  
from nursing_note a lateral view outer explode(a.nursing_note.record_datetime) b as b1 
group by year(b1),month(b1)
order by year1,month1
limit 2000