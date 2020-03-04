#-*-coding:utf-8-*-
# Author:Lu Wei
import pymysql

conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='Lw@123123',database='day53',charset='utf8')
cur=conn.cursor(pymysql.cursors.DictCursor)
# sql='create table userinfo(id int primary key auto_increment,' \
#     'name char(10),' \
#     'age int not null)'
sql='insert into userinfo(name,age) values("luwei",18);'
cur.execute(sql)
conn.commit()
cur.close()
conn.close()