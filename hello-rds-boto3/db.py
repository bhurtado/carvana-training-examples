from sqlmodel import Field, SQLModel, create_engine

DB_ENDPOINT = "mojix-training-db.c5xjijttshln.us-east-1.rds.amazonaws.com"
DB_USER = "postgres"
DB_PASSWORD = "postgres123"
DB_PORT = "5432"
DB_NAME = "carvana"

db_url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_ENDPOINT}:{DB_PORT}/{DB_NAME}"

engine = create_engine(db_url, echo=True)