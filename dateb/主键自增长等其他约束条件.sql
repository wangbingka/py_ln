一、主键，PRIMARY KEY，无意义字符，自动非空，并且是唯一的
    单字段主键，多字段组成符合主键，每个表只能有1个主键
    索引时会必须用到主键
    可以省略:PRIMARY，只写:KEY

CREATE TABLE IF NOT EXISTS USER3(
ID INT KEY,
USERNAME VARCHAR(20)
);

#单字段主键
CREATE TABLE IF NOT EXISTS USER1(
ID INT PRIMARY KEY,
USERNAME VARCHAR(20)
);

INSERT user1 VALUES (1,'king');
INSERT user1 VALUES (13,'tom');
报错
INSERT uesr1 VALUES (1,'emy');

#多字段组成符合主键
CREATE TABLE IF NOT EXISTS USER2(
id INT,
username VARCHAR(20),
card CHAR(20),
primary key(id,card)
);

INSERT user2 VALUES (1,'king','111');
INSERT user2 VALUES (13,'tom','222');
INSERT user2 VALUES (1,'tom','222');

二、自增长，AUTO_INCREMENT，默认从1开始，每次自动加1
  每个表只有1个自增长字段，最好配合主键使用，自增长一定的一定是主键，主键可以不是自增长
  可以自己设置更大的值，然后下一个值会从当前最大的值，继续自增长+1
  NULL,DEFAULT,都会继续自增长


CREATE TABLE IF NOT EXISTS user4(
id SMALLINT KEY AUTO_INCREMENT,
username VARCHAR(20)
);

INSERT user4 VALUES('1','king');
INSERT user4(username) VALUES('tom');
INSERT user4 VALUES(111,'carry');
INSERT user4(username) VALUES('jim');
INSERT user4 VALUES(888,'jack');
INSERT user4(username) VALUES('amy');
INSERT user4 VALUES(null ,'jack');
INSERT user4 VALUES(DEFAULT ,'jack');

设置初始自增长值：
CREATE TABLE IF NOT EXISTS user6(
id SMALLINT KEY AUTO_INCREMENT,
username VARCHAR(20)
)AUTO_INCREMENT=100;
INSERT user4(username) VALUES('tom');

修改当前的自增长值：
ALTER TABLE user6 AUTO_INCREMENT=500;
INSERT user6(username) VALUES('tom1');


三、外键，FOREIGN KEY，多表查询时再讲

四、非空，NOT NULL，在插入值，不能为空，
  不能为NULL，但可以是空字符串''，其他不设置非空的字段默认为NULL

CREATE TABLE IF NOT EXISTS user7(
id SMALLINT UNSIGNED KEY AUTO_INCREMENT,
username VARCHAR(20) NOT NULL,
password CHAR(32) NOT NULL,
age TINYINT UNSIGNED
);

INSERT user7(username,password) VALUES('KING','KING');
INSERT user7(username,password,age) VALUES('KING','KING',12);
INSERT user7(username,password,age) VALUES('TOM','',13);


报错1
INSERT user7(username,age) VALUES('KING',12);
报错2
INSERT user7(username,password,age) VALUES('KING',NULL,12);

六、默认值，DEFAULT,一般和非空 NOT NULL 一起使用

CREATE TABLE IF NOT EXISTS user8(
id SMALLINT UNSIGNED KEY AUTO_INCREMENT,
username VARCHAR(20) NOT NULL,
password CHAR(32) NOT NULL,
age TINYINT UNSIGNED DEFAULT 18,
addr VARCHAR(50) NOT NULL DEFAULT '北京',
sex ENUM('男','女','保密') NOT NULL DEFAULT '保密'
);

INSERT user8(username,password) values ('KING','KING');
INSERT user8 VALUES(null ,'TOM','TOM',DEFAULT,DEFAULT,DEFAULT );
INSERT user8 VALUES (29,'QUEEN','QUEEN',29,'上海','男');



五、唯一，UNIQUE KEY，在创建字段时，Key省略，只写:UNIQUE,
  一个表可以有多个唯一键，除了特例：NULL，不算重复

CREATE TABLE IF NOT EXISTS user9(
id SMALLINT UNSIGNED KEY AUTO_INCREMENT,
username VARCHAR(20) NOT NULL UNIQUE,
card char(18) UNIQUE
);

INSERT user9(username) VALUES('A1');

报错：
INSERT user9(username) VALUES('A1');

INSERT user9(username,card) VALUES('B1',null);
INSERT user9(username,card) VALUES('C1',null);

创建完整的表
CREATE TABLE [IF NOT EXISTS ] tbl_name{
字段名称 字段类型 [NOT NULL] [DEFAULT 默认值] [[PRIMARY] KEY| UNIQUE [KEY]] [AUTO_INCRMENT],
字段名称1,
...
} [ENGINE = Innodb|MYISAM|MEMORY] [CHARSET=uft8|GBK] [AUTO_INCREMENT=初始自增长值];


