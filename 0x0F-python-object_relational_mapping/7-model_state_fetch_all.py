#!/usr/bin/python3
"""A script that lists all State objects from the database
hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
        # Connect to the database
            engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                                               .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                                                                          pool_pre_ping=True)
                Base.metadata.create_all(engine)

                    Session = sessionmaker(engine)
                        session = Session()
                            try:
                                        states = session.query(State).order_by(State.id)
                                                for state in states:
                                                                print(state.id, state.name, sep=": ")
                                                                    finally:
                                                                                session.close()
