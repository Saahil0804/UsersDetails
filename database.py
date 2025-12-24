import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
load_dotenv() 

#connection to database

db_url = (
    f"postgresql+psycopg2://{os.getenv('USER_NAME')}:"
    f"{os.getenv('PASSWORD')}@"
    f"{os.getenv('HOSTNAME')}:"
    f"{os.getenv('PORT')}/"
    f"{os.getenv('DATABASE')}"
)

engine = create_engine(db_url)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()
