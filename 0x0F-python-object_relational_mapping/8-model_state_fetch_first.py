#!/usr/bin/python3
"""prints the first State object from the database"""
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
    first_st = session.query(State).order_by(State.id).first()

    if first_st:
        print("{}: {}".format(first_st.id, first_st.name))
    else:
        print("Nothing")

    session.close()
