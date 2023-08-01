#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa
with the module SQLAlchemy"""


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
    rows = sesion.query(State).order_by(State.id).all()
    for row in rows:
        print(f"{row.id}:", row.name)
    sesion.close()
