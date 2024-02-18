#!/usr/bin/python3
"""
script that prints the State object with the
name passed as argument from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name_to_search = sys.argv[4]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            user_name, password, db_name.strip()
        ), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = (session.query(State).filter(State.name == state_name_to_search)
             .first())
    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close()
