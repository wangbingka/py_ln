select '非药品类型医嘱类型开立时间',order_type,visit_type,year(order_time) as year1,month(order_time) as month1,
count(*) 
from non_drug_order a 
group by order_type,visit_type,year(order_time),month(order_time)
order by order_type,visit_type,year1,month1
limit 2000;