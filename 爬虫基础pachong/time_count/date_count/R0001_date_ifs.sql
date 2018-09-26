use %s;
	select '病案首页表入院时间',record_status,'住院',
	year(admission_discharge_t_info.admission_time) as year1,month(admission_discharge_t_info.admission_time) as month1,
	count(*) 
	from first_page_of_hospital_medical_record a 
	group by record_status,year(admission_discharge_t_info.admission_time),month(admission_discharge_t_info.admission_time)
	order by record_status,year1,month1
	limit 5000;
