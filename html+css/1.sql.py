select count(*) from 
(select distinct inpatient_visit_id, hybrid_name from tbl_mar_dispense_withdraw_rec a where biz_type='退药'
left join 
(select distinct inpatient_visit_id, hybrid_name from tbl_mar_dispense_withdraw_rec b where biz_type='摆药' ) b1
on a.inpatient_visit_id = b1.inpatient_visit_id and a.hybrid_name = b1.hybrid_name
where b1.hybrid_name is null ) c