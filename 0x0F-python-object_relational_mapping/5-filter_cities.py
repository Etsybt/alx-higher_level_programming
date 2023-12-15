#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    query = """
         SELECT cities.id, cities.name
         FROM cities
         JOIN states ON cities.state_id = states.id
         WHERE states.name = %s
         ORDER BY cities.id ASC
    """
    cursor.execute(query, [argv[4]])

    cities = cursor.fetchall()
    c = []
    for city in cities:
        c.append(city[1])
    print(", ".join(c))
    cursor.close()
    db.close()
