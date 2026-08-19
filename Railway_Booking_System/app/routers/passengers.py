from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.passenger import Passenger
from app.schemas.passenger import PassengerCreate


router = APIRouter(
    prefix="/passengers",
    tags=["Passengers"]
)


@router.post("/")
def create_passenger(
    passenger: PassengerCreate,
    db: Session = Depends(get_db)
):

    new_passenger = Passenger(
        name=passenger.name,
        age=passenger.age,
        gender=passenger.gender,
        mobile=passenger.mobile
    )

    db.add(new_passenger)

    db.commit()

    db.refresh(new_passenger)

    return new_passenger


@router.get("/")
def get_passengers(
    db: Session = Depends(get_db)
):

    passengers = db.query(Passenger).all()

    return passengers