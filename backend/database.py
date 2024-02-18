from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

db_password = os.environ.get("DB_PASSWORD")

# PostgreSQL database URL
POSTGRES_DB = f"postgresql://clutch_vacations:{db_password}@localhost:5432/clutch_vacations"

# Create a SQLAlchemy engine
engine = create_engine(POSTGRES_DB)

# Create a session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SQLAlchemy Base
Base = declarative_base()
