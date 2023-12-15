#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT DISTINCT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    name = cursor.fetchall()
    for x in name:
        print(x)
    cursor.close()
    db.close()
