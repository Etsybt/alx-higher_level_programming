#!/usr/bin/python3
"""prints the State object with the name passed as argument from the database"""
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
    state_name = sys.argv[4]

    state = session.query(State).filter(State.name == state_name).first()
    
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
