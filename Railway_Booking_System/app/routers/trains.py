from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.train import Train
from app.schemas.train import TrainCreate, TrainResponse


router = APIRouter(
    prefix="/trains",
    tags=["Trains"]
)


@router.post("/", response_model=TrainResponse)
def create_train(
    train: TrainCreate,
    db: Session = Depends(get_db)
):

    new_train = Train(
        train_number=train.train_number,
        train_name=train.train_name,
        source=train.source,
        destination=train.destination,
        departure_time=train.departure_time,
        arrival_time=train.arrival_time,
        total_seats=train.total_seats,
        available_seats=train.total_seats,
        fare=train.fare
    )

    db.add(new_train)

    db.commit()

    db.refresh(new_train)

    return new_train


@router.get("/")
def get_trains(
    db: Session = Depends(get_db)
):

    trains = db.query(Train).all()

    return trains