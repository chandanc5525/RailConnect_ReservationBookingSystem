from pydantic import BaseModel


class BookingCreate(BaseModel):

    passenger_id: int

    train_id: int

    journey_date: str


class BookingResponse(BaseModel):

    id: int

    pnr: str

    passenger_id: int

    train_id: int

    journey_date: str

    seat_number: int

    fare: float

    booking_status: str

    class Config:
        from_attributes = True