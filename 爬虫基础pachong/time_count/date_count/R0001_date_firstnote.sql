use %s;
	select '首次病程记录时间','首程','住院',
	year(b1) as year1,month(b1) as month1,count(*)  
	from first_medical_note a lateral view outer explode(a.recorders.date_of_note) b as b1 
	group by year(b1),month(b1)
	order by year1,month1
	limit 5000;