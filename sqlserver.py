#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymssql
conn = pymssql.connect(host='192.168.1.231', user='infoadmin', password='3r5Ja4uqZB7rd6fARBF2', database='Attendance', charset='utf8')
cur = conn.cursor()
if not cur:
    raise (NameError,'数据库连接失败')
sql = 'select cardno from [USERINFO] where BADGENUMBER = 4543'
cur.execute(sql)
resList = cur.fetchall()  #fetchall()是接收全部的返回结果行

sql = 'select userid from [USERINFO] where name = \'邹欣\''
cur.execute(sql)
rs = cur.fetchall()
conn.close()
print(resList)
print(rs[0])



