#!/usr/bin/python3
"""
script that takes in arguments and
displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
safe from MySQL injections
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    state_name_search = sys.argv[4]
    Q = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(Q, (state_name_search,))
    rows = cur.fetchall()
    for r in rows:
        print(r)
    db.close()
