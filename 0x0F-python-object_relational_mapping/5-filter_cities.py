#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])
    cur = db.cursor()
    state_name = sys.argv[4]
    Q = "SELECT cities.name FROM cities\
        JOIN states ON cities.state_id = states.id\
        WHERE states.name = %s ORDER BY cities.id ASC"
    cur.execute(Q, (state_name,))
    rows = cur.fetchall()
    print(", ".join(r[0] for r in rows))
    db.close()
