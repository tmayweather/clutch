from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel
from database import SessionLocal
from models import Destinations

app = FastAPI()

__version__ = "0.1.0"

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow requests from your React app
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Destinations(BaseModel):
    date: str
    city: str
    cost: str




@app.get("/home")
async def root():
    return {"message": "Welcome to Clutch Vacations"}

@app.get("/destinations", response_model=List[Destinations])
async def get_destinations():
    # Example data, replace with actual weather forecast data
    destinations = [
        {"date": "2024-02-15", "city": ",italy", "cost": "$300.00" },
        {"date": "2024-02-16", "city": "spain", "cost": "$300.00" },
        {"date": "2024-02-17", "city": "france", "cost": "$300.00"},
    ]
    return destinations


# @app.get("/destinations")
# async def get_destinations(db: Session = Depends(get_db)):
#     # Query the database to get destinations
#     destinations = db.query(User).all()

#     # Convert SQLAlchemy objects to dictionaries
#     destinations_dict = [{"date": destination.date, "city": destination.city, "cost": destination.cost} for destination in destinations]

#     return destinations_dict