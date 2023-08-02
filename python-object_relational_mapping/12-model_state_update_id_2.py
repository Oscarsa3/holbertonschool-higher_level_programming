#!/usr/bin/python3
"""This script updated or changes the name of a State
object from the database hbtn_0e_6_usa"""


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    engine = create_engine(f"""mysql+mysqldb://{sys.argv[1]}:
                           {sys.argv[2]}@localhost:3306/{sys.argv[3]}""",
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    sesion = Session()

    rows = sesion.query(State).filter_by(id=2).first()
    if rows:
        rows.name = 'New Mexico'
        sesion.commit()

    sesion.close()
