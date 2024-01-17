#!/usr/bin/python3
"""
Module to define the State class and create a corresponding table in a MySQL database.
"""

import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    """
    State class to represent the states table in the database.

    Attributes:
        id (int): Auto-incremented unique identifier for each state.
        name (str): Name of the state, with a maximum length of 128 characters.

    Args:
        Base (declarative_base()): Base class for declarative class definitions.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create the 'states' table in the database
    Base.metadata.create_all(engine)

    print("Table 'states' created successfully.")
