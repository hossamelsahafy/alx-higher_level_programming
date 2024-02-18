#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to
the database hbtn_0e_6_usa
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
    NS = State(name="Louisiana")
    session.add(NS)
    session.commit()
    print(NS.id)
    session.close()
