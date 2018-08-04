--测试整型
CREATE TABLE test1(
num1 TINYINT,
num2 SMALLINT,
num3 MEDIUMINT,
num4 INT,
num5 BIGINT
);

--向表中插入数据记录：
INSERT tbl_name VALUE|VALUES(值1,值2,...)
INSERT test1 VALUES(-128,-32768,-8388608,-2147483648,-9223372036854775808)

如果插入超过数据类型范围的数字，会报错，无法插入：
INSERT test1 VALUES(130,-32768,-8388608,-2147483648,-9223372036854775808)

没有符号的数据类型，即没有负数的
CREATE TABLE test2(
num1 TINYINT UNSIGNED,
num2 TINYINT
);
INSERT test2 VALUES(128,-128);
插入负数会报错
INSERT test2 VALUES(-128,-128);

--零填充ZEROFILL,数字必须从0开始，并且在值前面用'0'补齐长度位数
CREATE TABLE test3(
num1 TINYINT ZEROFILL,
num2 SMALLINT ZEROFILL,
num3 MEDIUMINT ZEROFILL,
num4 INT ZEROFILL,
num5 BIGINT
);
例如:
INSERT test3 VALUES(1,1,1,1,1)
结果:
num1 | num2  | num3     | num4       | num5 |
+------+-------+----------+------------+------+
|  001 | 00001 | 00000001 | 0000000001 |    1 |