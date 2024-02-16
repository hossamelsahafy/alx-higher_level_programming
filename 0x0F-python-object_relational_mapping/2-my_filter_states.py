#!/usr/bin/python3
"""
script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where namematches the argument
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    cur = db.cursor()
    state_name_searched = sys.argv[4]
    Q = ("SELECT * FROM states WHERE name LIKE BINARY '{}' \
        ORDER BY id ASC".format(sys.argv[4]))
    cur.execute(Q)
    rows = cur.fetchall()
    for r in rows:
        print(r)
    db.close()
