use %s;
	select '费用明细表收费时间', b1.charge_type_name, visit_type, 
	year(b1.billing_time) as year1,month(b1.billing_time) as month1,count(*)
	from medical_costs_details_record a 
	lateral view outer explode(bill_items_details) b as b1
	where b1.charge_type_name in ('西药','中成药','中草药','手术','卫生材料','挂号','检查','化验','诊察','治疗','体检')
	group by b1.charge_type_name, visit_type, year(b1.billing_time) ,month(b1.billing_time)
	order by b1.charge_type_name, visit_type,year1,month1
	limit 5000;