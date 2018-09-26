use %s;
	select '诊断记录表',b1.diagnosis_type_name, visit_type,year(b1.diagnosis_date) as year1 ,month(b1.diagnosis_date) as month1,count(*) 
	from diagnostic_record a
	lateral view outer explode(a.diagnosis_details) b as b1 
	where b1.diagnosis_type_name in ('门诊诊断','入院诊断','死亡诊断','出院诊断')
	group by b1.diagnosis_type_name, visit_type,year(b1.diagnosis_date) ,month(b1.diagnosis_date)
	order by b1.diagnosis_type_name, visit_type,year1,month1
	limit 2000