#!/usr/bin/python3

"""displays all values in the states table where name matches the argument"""

if __name__ == '__main__':

    import sys
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    state_name = state_name.split("'")[0]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC"
    query = query.format(state_name)
    cur.execute(query)
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    conn.close()
