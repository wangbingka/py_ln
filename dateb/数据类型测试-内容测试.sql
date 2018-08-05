一、--测试整型
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

二、测试浮点型:
CREATE TABLE IF NOT EXISTS test4(
num1 FLOAT(6,2),
num2 DOUBLE(6,2),
num3 DECIMAL(6,2)
);
INSERT test4 VALUES(3.1415,3.1415,3.1415);
INSERT test4 VALUES(3.1415,3.1495,3.14185);

1、插入的浮点数，超过规定的位数，会四舍五入；
2、FLOAT,存储的是数字,如果转换为字符串时，并不是严格的'3.14'，而是无限接近于'3.14'
   DOUBLE，双精度，可以等于字符串'3.14'
   而DECIMAL，定点数，对精度要求比较高，存储的是字符换，和'3.14'严格相等
   
测试：
SELECT * FROM test4 where num1 = '3.14';
结果为空

SELECT * FROM test4 where num2 = '3.14' and num3 = '3.14';
结果有值。


