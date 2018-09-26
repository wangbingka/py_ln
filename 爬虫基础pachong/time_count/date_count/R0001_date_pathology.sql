select '病理记录表','病理',visit_type,year(time1) as year1,month(time1) as month1,count(*) from 
(select 
visit_type, 
(case 
when pathology_note.exam_date is not null and pathology_note.exam_date <>'' then pathology_note.exam_date  
when participant_reporter.participant_date is not null and participant_reporter.participant_date <>''  
then participant_reporter.participant_date 
else participant_report_reviewer.participant_date end) as time1 
from pathology_record a ) c 
group by visit_type,year(time1),month(time1)
order by visit_type,year1,month1
limit 2000;