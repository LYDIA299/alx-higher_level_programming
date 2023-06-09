#!/usr/bin/python3

"""takes name of a state as an argument and lists all cities of that state"""

if __name__ == '__main__':

    import sys
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4].split("'")[0]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    query = "SELECT c.name FROM cities c INNER JOIN states s \
ON c.state_id = s.id WHERE s.name = '{}' ORDER BY c.id ASC".format(state_name)
    cur.execute(query)
    results = cur.fetchall()
    i = 1
    for row in results:
        if i < len(results):
            print(row[0], end=', ')
        else:
            print(row[0])
        i = i + 1
    cur.close()
    conn.close()
