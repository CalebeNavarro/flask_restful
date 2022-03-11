from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

import os

load_dotenv()
Base = declarative_base()

engine = create_engine(os.getenv("DATABASE_URI"), echo=True, future=True)
engine.connect()

session = sessionmaker(
    engine,
    expire_on_commit=False,
    future=True,
)


def init_db():
  import app.models.users_model
  import app.models.honor_model
  Base.metadata.create_all(bind=engine)
