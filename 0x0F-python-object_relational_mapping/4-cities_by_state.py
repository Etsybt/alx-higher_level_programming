#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    query = """
         SELECT cities.id, cities.name, states.name
         FROM cities
         JOIN states ON cities.state_id = states.id
         ORDER BY cities.id ASC
    """
    cursor.execute(query)

    n = cursor.fetchall()
    for x in n:
        print(x)
    cursor.close()
    db.close()
