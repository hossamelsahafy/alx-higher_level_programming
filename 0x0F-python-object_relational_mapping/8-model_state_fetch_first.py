#!/usr/bin/python3
"""
script that prints the first State
object from the database hbtn_0e_6_usa
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
    F_S = session.query(State).order_by(State.id).first()
    if F_S is not None:
        print("{}: {}".format(F_S.id, F_S.name))
    else:
        print("Nothing")
    session.close()
