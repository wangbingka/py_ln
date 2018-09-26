use %s;
	select '就诊日期年份分布',visit_type,table_status,year(table_time) as year1,month(table_time) as month1,count(*) from 
	(select affair_info.visit_type,
	(case when affair_info.visit_date is not null or affair_info.visit_date <> '' then affair_info.visit_date
		 when affair_info.admission_date is not null or affair_info.admission_date <> '' then affair_info.admission_date
		 else affair_info.register_time end ) as table_time,
	(case when affair_info.register_status is not null or affair_info.register_status <> '' then affair_info.register_status
		 when affair_info.adt_status is not null or affair_info.adt_status <> '' then affair_info.adt_status
		 else affair_info.checkup_status end ) as table_status
	from medical_visit_summary a ) b1
	group by visit_type,table_status,year(table_time),month(table_time)
	order by visit_type,table_status,year1,month1
	limit 5000;