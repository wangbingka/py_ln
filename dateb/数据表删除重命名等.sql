创建用户表：
CREATE TABLE IF NOT EXISTS user10(
id SMALLINT UNSIGNED KEY AUTO_INCREMENT ,
uesrname VARCHAR(20) NOT NULL UNIQUE,
password CHAR(32) NOT NULL,
email VARCHAR(50) NOT NULL DEFAULT '897266654@QQ.COM',
age TINYINT UNSIGNED DEFAULT 18,
sex ENUM('男','女','保密'),
addr VARCHAR (200) NOT NULL DEFAULT '北京',
salary FLOAT (6,2),
regTime INT UNSIGNED,
face CHAR(100) NOT NULL DEFAULT  'default.jpg'
);

修改表名：

ALTER TABLE user10 RENAME as user11; --将user10表，改名user11
ALTER TABLE user11 RENAME  user10;--将user11表，改名user10
RENAME TABLE user10 TO user11;--将user10表，改名user11

--添加card字段，默认在最后一位
ALTER TABLE user10 ADD card CHAR(18) ;
也可以在后面添加约束条件。
ALTER TABLE user10 ADD test1 CHAR(18) not null UNIQUE;


指定字段添加位置

--添加在开头
ALTER TABLE user10 ADD test2 CHAR(18) not null FIRST;
--添加在某个字段后面
ALTER TABLE user10 ADD test3 int not null DEFAULT 100 AFTER uesrname;

一个表，一次添加多个字段
ALTER TABLE user10
ADD test4 INT NOT NULL DEFAULT 100 AFTER password,
ADD test5 FLOAT(6,2) FIRST,
ADD test6 SET('A','B','C');

删除字段：
--删除一个字段
ALTER TABLE user10 DROP test6;
一次删除多个字段：
ALTER TABLE user10
DROP test1,
DROP test2,
DROP test3,
DROP test4,
DROP test5;

添加和删除字段，同时进行
ALTER TABLE user10
ADD test INT UNSIGNED NOT NULL DEFAULT 100 AFTER sex,
DROP addr;


修改字段类型和属性
ALTER TABLE tblName MODIFY 字段名称 字段类型 [挖不这个表格约束性条件] [FIRST|AAFTER 某个字段],














