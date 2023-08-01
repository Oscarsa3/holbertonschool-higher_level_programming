#!/usr/bin/python3
"""This script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!"""


import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect("localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT id, name
                FROM states
                WHERE BINARY name = %s
                ORDER BY id""", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
