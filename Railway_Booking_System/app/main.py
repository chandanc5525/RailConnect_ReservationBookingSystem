from fastapi import FastAPI

from app.database.connection import Base, engine

from app.models.train import Train
from app.models.passenger import Passenger
from app.models.booking import Booking

from app.routers import trains
from app.routers import passengers
from app.routers import bookings


app = FastAPI(
    title="Railway Booking System",
    description="Railway Ticket Booking API",
    version="1.0.0"
)


Base.metadata.create_all(
    bind=engine
)


app.include_router(
    trains.router
)

app.include_router(
    passengers.router
)

app.include_router(
    bookings.router
)


@app.get("/")
def home():

    return {
        "message": "Welcome to Railway Booking System"
    }