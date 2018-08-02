注释写法：
1、#注释内容
2、 --注释内容

--创建一个数据库maizi
CREATE DATABASE IF NOT EXISTS maizi DEFAULT CHARACTER SET 'UTF8';

USE maizi;

CREATE TABLE IF NOT EXISTS 'user'(
id SMALLINT,
username VARCHAR(20),
age TINYINT,
sex ENUM('男','女','未知'),
email VARCHAR(50),
address VARCHAR(200),
birth YEAR,
salary FLOAT(8,2),
tel INT,
married TINYINT(1) COMMEN '0代表未结婚，非0代表已婚',
) ENGING=INNODB CHARSET=UTF8;
--创建学员表(user)
--编号id
--用户名 username
--性别 sex
--邮箱 email
--地址 address
--生日 birth
--薪水 salary
--电话 tel
--是否结婚 married
--注意：当需要输入中文的时候，需要临时转换字符串的编码方式为GBK
	用法： SET NAMES GBK
--字段注释 通过COMMENT 	给字段注释。
	用法：字段 类型 COMMENT '注释内容'