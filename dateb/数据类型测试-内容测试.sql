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

三、测试字符串字符类型
1、CHAR(M),定长字符换，占用空间固定位M，最多入M长度以内的字符，占用空间大大，速度快
2、VARCHAR(M)，变长字符串，占用空间是M+1位，最多输入M长度的字符，占用空间小小，速度慢
3、注意事项，当使用拼接函数CONCAT时，CHAR类数据开始的空格会被保留，末尾的空格会自动去掉，
  而VARCHAR，开始和末尾的空格都会保留。
4、mysql5.6之后，可以插入中文，不需要SET NAMES GBK,之前需要，中文在utf8下默认占3个字符。
 但是对于CHAR和VARCHAR来说，一个中文只是占用1个字符长度，CHAR(5),可以输入5个中文
5、当存储大量文本时，可以用TINYTEXT、TEXT、MEDIUMTEXT，
  是一种特殊的字符串，只能保存字符，并且不能有默认值
6、检索效率，CHAR>>VARCHAR>>TEXT,尽量不用TEXT类型
CREATE TABLE IF NOT EXISTS test5(
str1 CHAR(5),
str2 VARCHAR(5)
);

INSERT  test5 VALUES('1234','12345');

INSERT test5 VALUES('  A  ','  1  ');
SELECT  CONCAT(str1,'_',str2) from test5;
结果：
 CONCAT(str1,'_',str2) |
+-----------------------+
| 1234_12345            |
|   A_  1

INSERT  test5 VALUES('啊','哈');
INSERT  test5 VALUES('啊啊啊啊啊','哈哈哈哈哈');
测试查询字符串度
select CHAR_LENGTH(str1),CHAR_LENGTH(str2) from test5;
结果：
CHAR_LENGTH(str1) | CHAR_LENGTH(str2) |
+-------------------+-------------------+
|                 4 |                 5 |
|                 3 |                 5 |
|                 1 |                 1 |
|                 5 |                 5 |

CREATE TABLE IF NOT EXISTS TEST6(
str1 TEXT
);
INSERT test6 VALUES('打法撒旦法规撒沙发沙发按时发动机后撒上发的撒开了按时发货洒进来的说法都是驾驶的方式大');


四、测试枚举/集合类型
1、ENUM('VALUE1','VALUE2',...),只能单选一个，可以插入值，
  也可以插入值的序列数，第一个就是1，没有0，可以插入NULL,不能插入空格
  占用1或者2字节，取决于枚举值的个数，最多65535个，
2、SET('VALUE1','VALUE2',..)，可以多选，占用1、2、4、8个字节由集合数量决定，最多64个成员。
  多选后，显示出来的值能占用集合中的顺序展示
  SET的可选项，分别占用1、2、4、8个，字节，最多64个成员，所以输入1表示第一个，输入3表示前两个，输入7表示前三个，以此类推
CREATE TABLE IF NOT EXISTS test7(
sex ENUM('男','女','保密')
);
INSERT test7 VALUES ('男');
INSERT test7 values (2);
INSERT test7 values ('保密');
INSERT test7 values (NULL);

CREATE TABLE IF NOT EXISTS test8(
fav SET('A','B','C','D')
);

INSERT test8 VALUES ('A,D');
INSERT test8 VALUES ('D,B,A');
INSERT test8 VALUES ('1');
INSERT test8 VALUES ('3');
INSERT test8 VALUES ('7');
INSERT test8 VALUES ('15');

五、测试时间类型
0、最常用的是通过整型保存时间戳，方便计算
1、TIME，用三个字节保存时间，-838:59:59-838:59:59，不常用
2、DATE，1000-01-01~9999-12-31，占用4个字节
3、DATATIME
4、TIMESTAMP
5、YEAR,，占用1个字节，保存年份，1901-2155年之间
  00-69之间，会自动转换2000-2069,70-99，会转换成1970-1999，
  字符串'0'会转换成2000，数字0,会转换成0000.

CREATE TABLE IF NOT EXISTS  test9(
birth YEAR
);
insert test9 values ('1989');
insert test9 values (2055);
insert test9 values (12);
insert test9 values (79);
insert test9 values (0);
insert test9 values ('0');

CREATE TABLE IF NOT EXISTS test10(
test TIME
);
日时分秒
INSERT test10 values ('1 12:12:12');
时分秒
INSERT test10 values ('12:12:12');
分秒
INSERT test10 values ('12:12');
分秒
INSERT test10 values ('1212');
秒
INSERT test10 values ('12');
0，结果是0时0分0秒
INSERT test10 values ('0');
结果：
 test     |
+----------+
| 36:12:12 |
| 12:12:12 |
| 12:12:00 |
| 00:12:12 |
| 00:00:12 |
| 00:00:00 |


CREATE TABLE IF NOT EXISTS test11(
test DATE
);
INSERT test11 values ('2012-06-07');
INSERT test11 values ('12/06/07');
INSERT test11 values ('12@6@07');
INSERT test11 values ('12@6/07');
这四个保存结果是一致的

