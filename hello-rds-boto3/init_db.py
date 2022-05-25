from sqlmodel import SQLModel
import models       # sqlmodel needs this import
from db import engine

SQLModel.metadata.create_all(engine)
