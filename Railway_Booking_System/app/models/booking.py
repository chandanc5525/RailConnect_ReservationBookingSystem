from sqlalchemy import Column, Integer, String, Float
from app.database.connection import Base


class Booking(Base):

    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)

    pnr = Column(String, unique=True, nullable=False)

    passenger_id = Column(Integer, nullable=False)

    train_id = Column(Integer, nullable=False)

    journey_date = Column(String, nullable=False)

    seat_number = Column(Integer, nullable=False)

    fare = Column(Float, nullable=False)

    booking_status = Column(
        String,
        default="CONFIRMED"
    )