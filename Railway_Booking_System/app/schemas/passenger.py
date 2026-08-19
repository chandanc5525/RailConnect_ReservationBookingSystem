from pydantic import BaseModel


class PassengerCreate(BaseModel):

    name: str

    age: int

    gender: str

    mobile: str


class PassengerResponse(PassengerCreate):

    id: int

    class Config:
        from_attributes = True