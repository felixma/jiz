#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
conn = MySQLdb.connect(host='localhost', user='felix',passwd='hello',db='jiz')
cursor = conn.cursor()
#conn.select_db('jiz'); 
count = cursor.execute('select * from jizhang_products')
results = cursor.fetchall()
for r in results:
    print r
    #print r[0].decode('utf8')
cursor.close();
conn.close()
