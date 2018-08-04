注释写法：
1、#注释内容
2、 --注释内容

Mysql8三种常用存储引擎:
InnoDB ,mysql8默认存储引擎
是较新的事务安全型存储引擎，用于事务处理应用程序，支持BDB的几乎所有特性，并具有众多新特性，包括ACID事务支持。
特性：
•事务处理机制
•支持外链
•崩溃后能立即恢复
•支持外键功能，级联删除
•支持并发能力
•在硬盘上的存储方式：InnoBDB frm

MyISAM,mysql5默认的存储引擎:
优点：
•1.比InnoDB表更小，所占资源更少
•2.可以在不同平台间二进制移植表的类型在创建表时指定。
缺点：不支持事务

Memory存储的表就是内存表。实际的数据存储在内存中，磁盘中只有表结构定义文件。
注：内存的占用空间由max_heap_table_size参数控制，默认16M。
当心！当Mysql服务关闭时，数据会丢失。
断电后，数据也会丢失





查看表的存储引擎和编码类型：
show create table tableName;
更改表的存储引擎：
alter table tableName engine =innodb;




--创建一个数据库maizi
CREATE DATABASE IF NOT EXISTS maizi DEFAULT CHARACTER SET 'UTF8';

USE maizi;

CREATE TABLE IF NOT EXISTS `user` (
id SMALLINT,
username VARCHAR(20),
age TINYINT,
sex ENUM('男','女','未知'),
email VARCHAR(50),
address VARCHAR(200),
birth YEAR,
salary FLOAT(8,2),
tel INT,
married TINYINT(1) COMMENT '0代表未结婚，非0代表已婚'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ;

一、创建表
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
--注意：
  --1、需要输入中文的时候，需要临时转换字符串的编码方式为GBK
	  用法： SET NAMES GBK
  --2、字段注释 通过COMMENT 	给字段注释。
	  用法：字段 类型 COMMENT '注释内容'
  --3、对列名或者库名，括起来防止与关键字冲突时，需要使用反引号`，不是单引号'
  --4、最后一个字段后面，不能加逗号,

CREATE TABLE IF NOT EXISTS `courses` (
cid TINYINT COMMENT '课程编号',
courseName VARCHAR(50) COMMENT '课程名称',
courseDesc VARCHAR(200) COMMENT '课程 描述'
)ENGINE=MYISAM DEFAULT CHARSET=utf8;




二、表内中操作；
  查看库中的表：
    SHOW TABLES;
  查看表中的所有字段和字段:
    DESC user;
    DESCRIBE user;
    show columns from tableName;

  查看表中所有字段的注释、类型等：
    show full fields from tableName;
  修改表的注释:
    alter table tableName comment '修改后的表的注释';
  修改某表中某字段的注释:
    alter table tableName modify column columnName int comment '修改后的字段注释';

三、练习
--创建新闻分类表cms_cate
--字段：编号、分类名称、分类描述
  CREATE TABLE IF NOT EXISTS cms_cate (
  id TINYINT,
  cateName ENUM('社会','科技','体育','文艺','财经','健康','汽车','其他'),
  cateDesc VARCHAR(100)
  );

--创建新闻表cms_news
--字段：编号、新闻标题、新闻内容、新闻发布时间、点击量、是否置顶、新闻所属分类、发布人
  CREATE TABLE IF NOT EXISTS cms_news (
  id TINYINT,
  newsTitle VARCHAR(20),
  newsComment VARCHAR(1000),
  newsTime Timestamp,
  clickNumber INT,
  zhiding_yn TINYINT(0) COMMENT '1表示置顶，其他表示不置顶',
  news_cate ENUM('社会','科技','体育','文艺','财经','健康','汽车','其他'),
  newsAuthor VARCHAR(20)
  );

更改newsTime的类型:
alter table cms_news modify column newsTime int comment '记录时间戳';
修改字段名称zhding_yn，改为isTop,此时一定要指定数据类型:
alter table cms_news CHANGE zhding_yn isTop TINYINT(0) COMMENT '1表示置顶，其他表示不置顶';
增加一个字段：
//增加一个字段，默认为空
alter table user add COLUMN new1 VARCHAR(20) DEFAULT NULL;
//增加一个字段，默认不能为空
alter table user add COLUMN new2 VARCHAR(20) NOT NULL;
增量多个字段：
alter table 表名 add (字段1 类型(长度),字段2 类型(长度),字段3 类型(长度));
alter table em_day_data add (f_day_house11 int(11),f_day_house12 int(11),f_day_house13 int(11));
删除一个字段：
alter table user DROP COLUMN new2;











