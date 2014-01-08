#!/usr/bin/env python
import MySQLdb
conn = MySQLdb.connect(host='localhost', user='felix',passwd='hello',db='jiz')
cursor = conn.cursor()
#conn.select_db('jiz'); 
count = cursor.execute('select * from jizhang_products')
results = cursor.fetchall()
for r in results:
    print r
cursor.close();
conn.close()
