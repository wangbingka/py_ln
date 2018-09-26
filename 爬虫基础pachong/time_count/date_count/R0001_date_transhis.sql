use %s;
	select '转科历史转出时间','转科历史','住院',year(b1.transfer_out_time) as year1,month(b1.transfer_out_time) as month1,count(*)
	from transfer_history a 
	lateral view outer explode(transfer_history) b as b1
	group by year(b1.transfer_out_time),month(b1.transfer_out_time)
	order by year1,month1
	limit 5000;