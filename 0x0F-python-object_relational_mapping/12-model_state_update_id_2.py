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
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)

    session = Session()

    obj = session.query(State).filter(State.id == 2).first()

    obj.name = "New Mexico"
    session.add(obj)
    session.commit()
    session.close()
