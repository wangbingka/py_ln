select '非药品类型医嘱类型开立时间',order_type,visit_type,year(order_time) as year1,month(order_time) as month1,
count(*) 
from non_drug_order a 
group by order_type,visit_type,year(order_time),month(order_time)
order by order_type,visit_type,year1,month1
limit 2000;



select '生命体征表测量日期',table_type,'住院',year(measure_datetime) as year1,month(measure_datetime) as month1,count(*) from  
(select 
case when cdt_vital_sign_index = 'VS000001' then '体温'  
when cdt_vital_sign_index = 'VS000002' then '脉搏'  
when cdt_vital_sign_index = 'VS000003' then '心率'  
when cdt_vital_sign_index = 'VS000004' then '呼吸'  
when cdt_vital_sign_index = 'VS000005' then '收缩压'  
when cdt_vital_sign_index = 'VS000006' then '舒张压'  
when cdt_vital_sign_index = 'VS000007' then '血氧饱和度'  
when cdt_vital_sign_index = 'VS000008' then '身高'  
when cdt_vital_sign_index = 'VS000009' then '体重'  
when cdt_vital_sign_index = 'VS000010' then '血压'  
when cdt_vital_sign_index = 'VS000011' then '呼吸末二氧化碳'  
else cdt_vital_sign_index end as table_type, 
measure_datetime 
from vital_signs_record a ) b  
where type in ('体温','脉搏' ,'呼吸' ,'收缩压' ,'舒张压' ,'血氧饱和度' ,'身高' ,'体重' ,'血压','呼吸末二氧化碳','心率',null ) 
group by table_type,year(measure_datetime) ,month(measure_datetime)
order by table_type,year1,month1
limit 3000;


select '体温' as table_type,