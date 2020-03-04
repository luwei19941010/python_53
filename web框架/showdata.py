#-*-coding:utf-8-*-
# Author:Lu Wei
import pymysql

def showdata():
    conn=pymysql.connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         password='Lw@123123',
                         database='day53',
                         charset='utf8')
    cur=conn.cursor(pymysql.cursors.DictCursor)
    sql='select * from userinfo;'
    cur.execute(sql)
    data=cur.fetchall()
    # print(data)
    conn.commit()
    cur.close()
    conn.close()
    return data