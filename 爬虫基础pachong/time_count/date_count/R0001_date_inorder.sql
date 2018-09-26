select '住院药品医嘱开立时间',b1,'住院',year(order_group_info.prescribed_time) as year1,month(order_group_info.prescribed_time) as month1,
count(*)  
from inpatient_medicinal_order a  
lateral view outer explode(a.order_group_info.drug_info.class_name) b as b1 
group by b1,year(order_group_info.prescribed_time),month(order_group_info.prescribed_time)
order by b1,year1,month1