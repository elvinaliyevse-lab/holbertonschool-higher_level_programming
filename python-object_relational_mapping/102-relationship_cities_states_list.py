#!/usr/bin/python3
""" Module to list all City objects"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State
from sys import argv

# Run only when executed
if __name__ == "__main__":
    # Creating the engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]))

    # Creating the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Printing the results
    for city in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
