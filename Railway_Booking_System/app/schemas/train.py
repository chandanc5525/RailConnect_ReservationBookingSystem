from pydantic import BaseModel


class TrainCreate(BaseModel):

    train_number: str

    train_name: str

    source: str

    destination: str

    departure_time: str

    arrival_time: str

    total_seats: int

    fare: float


class TrainResponse(TrainCreate):

    id: int

    available_seats: int

    class Config:
        from_attributes = True