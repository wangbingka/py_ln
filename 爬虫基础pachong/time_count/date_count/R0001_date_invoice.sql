use %s;
	select '发票结算时间', b3.charge_group_type, visit_type, 
	year(b1.settle_datetime) as year1,month(b1.settle_datetime) as month1,count(*)
	from medical_invoice_record a 
	lateral view outer explode(invoice_info) b as b1
	lateral view outer explode(b1.charges_groups_info) b2 as b3
	where b3.charge_group_type like '%药%' or b3.charge_group_type like '%材%' or b3.charge_group_type like '%验%'
	or b3.charge_group_type like '%查%' or b3.charge_group_type like '%术%'
	group by b3.charge_group_type, visit_type, year(b1.settle_datetime) ,month(b1.settle_datetime)
	order by b3.charge_group_type, visit_type,year1,month1
	limit 5000;