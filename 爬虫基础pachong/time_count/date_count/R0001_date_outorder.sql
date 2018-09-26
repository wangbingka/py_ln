use %s;
	select '门急诊药品开立时间',d1,'门急诊',year(b1) as year1,month(b1) as month1,
	count(*) 
	from outpatient_medicinal_order a  
	lateral view outer explode(a.prescription.order_group_info.prescribed_time) b as b1  
	lateral view outer explode(a.prescription.order_group_info.drug_info) c as c1  
	lateral view outer explode(c1.class_name) d as d1 
	group by d1,year(b1),month(b1)
	order by d1,year1,month1
	limit 2000;