#!/usr/bin/python3
"""lists all State objects that contain the letter a from the database"""
from sys import argv
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).order_by(
        State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
