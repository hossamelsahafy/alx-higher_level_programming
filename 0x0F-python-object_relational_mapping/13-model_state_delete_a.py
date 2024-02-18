#!/usr/bin/python3
"""
script that deletes all State objects with a
name containing the letter a from the database
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
    states = (session.query(State)
              .filter(State.name.contains('a'))
              .order_by(State.id)
              .all())
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
