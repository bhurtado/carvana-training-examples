from sqlmodel import Session
from models import Subject
from db import engine

subjects = [
    Subject(name="math", level="3"),
    Subject(name="chem", level="2"),
    Subject(name="phys", level="3"),
    Subject(name="comp", level="5"),
]

session = Session(engine)
for subject in subjects:
    session.add(subject)

session.commit()
