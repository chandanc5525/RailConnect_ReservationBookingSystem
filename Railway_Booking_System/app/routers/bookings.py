from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.booking import BookingCreate
from app.services.booking_service import create_booking


router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


@router.post("/")
def book_ticket(
    booking: BookingCreate,
    db: Session = Depends(get_db)
):

    result, message = create_booking(
        db=db,
        passenger_id=booking.passenger_id,
        train_id=booking.train_id,
        journey_date=booking.journey_date
    )

    if result is None:

        raise HTTPException(
            status_code=400,
            detail=message
        )

    return {
        "message": message,
        "pnr": result.pnr,
        "seat_number": result.seat_number,
        "fare": result.fare,
        "status": result.booking_status
    }