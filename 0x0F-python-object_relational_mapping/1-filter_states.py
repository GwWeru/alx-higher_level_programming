#!/usr/bin/python3
"""
Script to list all states with a name starting with 'N'
should take 3 arguments username, passwd and db name
"""


if __name__ == '__main__':
    import sys
    import MySQLdb
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states where name LIKE ''N%'\
                ORDER BY id ASC")
    lst = cur.fetchall()
    for r in lst:
        if row[1][0] == 'N':
            print(r)
    cur.close()
    db.close()
