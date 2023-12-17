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

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California")
    session.add(california)
    session.commit()

    san_francisco = City(name="San Francisco", state=california)
    session.add(san_francisco)
    session.commit()

    session.close()
