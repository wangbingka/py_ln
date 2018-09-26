select '检验记录',test_type,visit_type,year(time) as year1,month(time) as month1,count(*) from 
(select 
visit_type, 
test_report.test_type as test_type, 
(case  
when lab_test_note.test_time is not null and lab_test_note.test_time <>'' then lab_test_note.test_time  
when participant_reporter.participant_date is not null and participant_reporter.participant_date <>''  
then participant_reporter.participant_date 
else participant_reviewer.participant_date end) as time 
from laboratory_test_record a) b 
group by test_type,visit_type,year(time),month(time)
order by test_type,visit_type,year1,month1
limit 5000;