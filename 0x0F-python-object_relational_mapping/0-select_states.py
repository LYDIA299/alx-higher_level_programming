#!/usr/bin/python3

import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="hbtn_0e_0_usa", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
results = cur.fetchall()
for row in results:
    print(row)
cur.close()
conn.close()
