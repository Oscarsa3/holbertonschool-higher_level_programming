#!/usr/bin/python3
"""this script prints the State object with the name passed as
argument from the database hbtn_0e_6_usa"""


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

    rows = sesion.query(State).filter_by(name=f"{sys.argv[4]}").first()
    if rows is None:
        print("Not found")
    else:
        print(rows.id)

    sesion.close()
