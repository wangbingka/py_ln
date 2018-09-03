select 字段name1,字段name2,... from tblName [where ... [and ...][or ...]]
[group by having ...] [order by 字段name1,... [desc|[asc]]] [limit [num1,] num2]


where:
常用的逻辑运算符：
<,>,>=,<=,<>|!=,精确的计算，不能使用通配符


and,or

between ... and ...:在...和...之间，效率偏低
	程序效率更高： where id >=100 and bid <= 105 ，

in (v1,v2,v3,...)，等于多个取值之内，效率偏低，但是好写好用
	等同于：where id = v1 or id =v2 or id = v3 or ...,效率偏高点，但不怎么人性化使用


like,模糊查询，可以使用通配符，如果不适用通配符，等同于"="
	任意个数的字符数:%,前后都可用

反向表现：
	not between ... and ...
	not in (v1,v2,v3,...)
	not like 不像，不等于，不是



