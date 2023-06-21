#!/usr/bin/python3

""" lists all states with a name starting with N (upper N) """

if __name__ == '__main__':

    import sys
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    conn.close()
