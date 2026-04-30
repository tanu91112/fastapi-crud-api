from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

url_database = "sqlite:///D:/OneDrive/Desktop/crud-api-fastapi-main/src/database.db"

engine = create_engine(
    url_database,
    connect_args={"check_same_thread": False}
)

session = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()