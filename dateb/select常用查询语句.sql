select �ֶ�name1,�ֶ�name2,... from tblName [where ... [and ...][or ...]]
[group by having ...] [order by �ֶ�name1,... [desc|[asc]]] [limit [num1,] num2]


where:
���õ��߼��������
<,>,>=,<=,<>|!=,��ȷ�ļ��㣬����ʹ��ͨ���


and,or

between ... and ...:��...��...֮�䣬Ч��ƫ��
	����Ч�ʸ��ߣ� where id >=100 and bid <= 105 ��

in (v1,v2,v3,...)�����ڶ��ȡֵ֮�ڣ�Ч��ƫ�ͣ����Ǻ�д����
	��ͬ�ڣ�where id = v1 or id =v2 or id = v3 or ...,Ч��ƫ�ߵ㣬������ô���Ի�ʹ��


like,ģ����ѯ������ʹ��ͨ��������������ͨ�������ͬ��"="
	����������ַ���:%,ǰ�󶼿���

������֣�
	not between ... and ...
	not in (v1,v2,v3,...)
	not like ���񣬲����ڣ�����



