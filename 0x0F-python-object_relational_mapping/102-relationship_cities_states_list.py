#!/usr/bin/python3
"""creates the State “California” with
   the City “San Francisco” from the database"""
from sys import argv
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).join(State).order_by(City.id).all()

    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()
