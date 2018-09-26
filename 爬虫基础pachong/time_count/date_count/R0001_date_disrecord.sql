use %s;
	select '出院记录出院时间', '出院记录','住院',
	year(discharge_note.discharge_time) as year1,month(discharge_note.discharge_time) as month1,
	count(*) 
	from discharge_record a  
	group by year(discharge_note.discharge_time), month(discharge_note.discharge_time)
	order by year1,month1
	limit 2000;