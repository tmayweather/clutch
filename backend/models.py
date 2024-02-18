from sqlalchemy import Column, Integer, String
from database import Base

# Define the SQLAlchemy model
class Destinations(Base):
    __tablename__ = "destinations"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, unique=True, index=True)
    cost = Column(String, unique=True, index=True)
    date = Column(String, unique=True, index=True)
