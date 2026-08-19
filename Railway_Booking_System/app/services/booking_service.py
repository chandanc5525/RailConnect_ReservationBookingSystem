from sqlalchemy.orm import Session

from app.models.train import Train
from app.models.booking import Booking
from app.utils.pnr_generator import generate_pnr


def create_booking(
    db: Session,
    passenger_id: int,
    train_id: int,
    journey_date: str
):

    train = db.query(Train).filter(
        Train.id == train_id
    ).first()

    if not train:
        return None, "Train not found"

    if train.available_seats <= 0:
        return None, "No seats available"

    seat_number = (
        train.total_seats -
        train.available_seats +
        1
    )

    booking = Booking(
        pnr=generate_pnr(),
        passenger_id=passenger_id,
        train_id=train_id,
        journey_date=journey_date,
        seat_number=seat_number,
        fare=train.fare,
        booking_status="CONFIRMED"
    )

    train.available_seats -= 1

    db.add(booking)

    db.commit()

    db.refresh(booking)

    return booking, "Booking successful"