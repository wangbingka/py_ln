use %s;
	select '上级查房记录时间间年份分布', '上级查房','住院',
	year(b1) as year1,month(b1) as month1,
	count(*)  
	from senior_doctor_ward_round_record a lateral view outer explode(a.recorders.note_date) b as b1 
	group by year(b1), month(b1)
	order by year1,month1
	limit 5000;