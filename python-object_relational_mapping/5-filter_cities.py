#!/usr/bin/python3
"""This script that takes in the name of a state as an argument
and lists all cities of that state, using the database"""


import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect("localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute(f"""SELECT cities.name
                FROM cities
                INNER JOIN states
                ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id""", (sys.argv[4],))
    rows = cur.fetchall()
    i = 0
    for row in rows:
        for col in row:
            if i == len(rows) - 1:
                print(f"{col}")
            else:
                print(f"{col}, ", end='')
        i += 1
    cur.close()
    db.close()
