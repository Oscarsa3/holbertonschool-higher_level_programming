#!/usr/bin/python3
"""this script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument"""


import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect("localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute(f"""SELECT id, name
                FROM states
                WHERE name = '{sys.argv[4]}'
                ORDER BY id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
