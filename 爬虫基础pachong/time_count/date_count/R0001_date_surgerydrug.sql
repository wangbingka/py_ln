use %s;
	select '手术用药开始时间',b1.medication_type,'住院', 
	year(c11.administer_time) as year1,month(c11.administer_time) as month1,count(*)
	from operation_med_fluid_blood_oxygen_record a
	lateral view outer explode(a.med_infor) b as b1
	lateral view outer explode(b1.administer_information) c as c11
	group by b1.medication_type, year(c11.administer_time) ,month(c11.administer_time)
	order by b1.medication_type,year1,month1
	limit 5000;