#!/usr/bin/python3
"""
script that changes the name of a
State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            user_name, password, db_name.strip()
        ), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).get(2)
    if state is not None:
        state.name = "New Mexico"
        session.commit()
    session.close()
