select '死亡记录死亡时间', '死亡记录','住院',
year(death_note.death_time) as year1,month(death_note.death_time) as month1,
count(*)  
from death_record a 
group by year(death_note.death_time),month(death_note.death_time)
order by year1,month1
limit 1000;