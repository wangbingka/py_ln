 select '检查日期分布',visit_type,exam_type,year(table_time) as year_time ,month(table_time) as month_time,count(*) from 
 (select visit_type,b1.exam_type,
 (case when participant_report_reviewer.participant_date is not null or participant_report_reviewer.participant_date <> '' then participant_report_reviewer.participant_date
 when participant_reporter.participant_date is not null or participant_reporter.participant_date <> '' then participant_reporter.participant_date
 else b1.exam_date end ) as table_time 
 from examination_record a lateral view outer  explode(exam_note) b as b1
where b1.exam_type in ('X线','CT','MR','超声','肺功能','内镜','核医学','神经电生理','心电','骨密度','病理')) c11
group by visit_type,exam_type,year(table_time) ,month(table_time)
order by visit_type,exam_type,year_time ,month_time
limit 20000;