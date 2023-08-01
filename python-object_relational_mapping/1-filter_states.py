#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""


import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect("localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT id, name
                FROM states
                WHERE name
                LIKE BINARY 'N%'
                ORDER BY id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
