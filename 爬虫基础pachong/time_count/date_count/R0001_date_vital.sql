use %s;
	select '生命体征观察时间',table_type,'住院',year(table_time) as year1,month(table_time) as month1,count(*)
	from 
	(select '体温' as table_type,b1.exam_time as table_time 
	from vital_signs_record a lateral view outer explode(temperature) b as b1
	where b1.yidu_pkid is not null
	union all
	select '呼吸' as table_type,b1.exam_time as table_time
	from vital_signs_record a lateral view outer explode(respiration) b as b1
	where b1.yidu_pkid is not null
	union all
	select 'spo2' as table_type,b1.exam_time as table_time 
	from vital_signs_record a lateral view outer explode(spo2) b as b1
	where b1.yidu_pkid is not null
	union all
	select '体重' as table_type,b1.exam_time as table_time 
	from vital_signs_record a lateral view outer explode(vital_sign_weight) b as b1
	where b1.yidu_pkid is not null
	union all
	select '身高' as table_type,b1.exam_time as table_time 
	from vital_signs_record a lateral view outer explode(vital_sign_height) b as b1
	where b1.yidu_pkid is not null
	union all
	select '心率' as table_type,b1.exam_time as table_time 
	from vital_signs_record a lateral view outer explode(heart_rate) b as b1
	where b1.yidu_pkid is not null
	union all
	select '脉搏' as table_type,b1.exam_time as table_time 
	from vital_signs_record a lateral view outer explode(pulse) b as b1
	where b1.yidu_pkid is not null
	union all
	select '血压' as table_type,b1.observation_time as table_time 
	from vital_signs_record a lateral view outer explode(blood_pressure) b as b1
	where b1.yidu_pkid is not null
	union all
	select '其它' as table_type,b1.exam_time as table_time
	from vital_signs_record a lateral view outer explode(vital_sign_others) b as b1
	where b1.yidu_pkid is not null ) c11
	group by table_type,year(table_time),month(table_time)
	order by table_type,year1,month1
	limit 5000;