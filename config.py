import sqlalchemy
from dotenv import load_dotenv
import os


load_dotenv('.env')

DATABASE_URI = os.environ.get('DATABASE_URL').replace("s://", "sql://", 1)
engine: sqlalchemy.engine = \
    sqlalchemy.create_engine(DATABASE_URI, echo=True, pool_pre_ping=True)
