#!/usr/bin/python3
"""Module to list all States and corresponding Cities"""
from relationship_city import City
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

# Run only when executed
if __name__ == "__main__":
    # Creating the engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    # Creating the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Printing
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
