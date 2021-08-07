#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy.orm import session

from sqlalchemy.orm.session import Session
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)

    session = Session()

    for result in session.query(State).filter(
            State.name.like("%a%")).order_by(State.id):
        print("{}: {}".format(result.id, result.name))

    session.close()
