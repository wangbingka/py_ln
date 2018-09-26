SELECT '就诊信息表',affair_info.visit_type as visit_type,affair_info.register_status as outstatus,
affair_info.adt_status as instatus,substring(affair_info.admission_date,1,4) AS inyear,
substring(affair_info.visit_date,1,4) AS outyear,count(*) AS yearcount 
FROM 



medical_visit_summary 
GROUP BY  affair_info.visit_type ,affair_info.register_status,affair_info.adt_status, 
substring(affair_info.admission_date,1,4),substring(affair_info.visit_date,1,4) 
ORDER BY visit_type,outstatus,instatus,inyear,outyear desc;


select '就诊日期年份分布',affair_info.visit_type,
year( affair_info.visit_date) as year1,year(affair_info.admission_date) as year2,count(*) from 

select affair_info.visit_type,case


medical_visit_summary a 
group by affair_info.visit_type,year( affair_info.visit_date),year(affair_info.admission_date) 
order by affair_info.visit_type,year1,year2 