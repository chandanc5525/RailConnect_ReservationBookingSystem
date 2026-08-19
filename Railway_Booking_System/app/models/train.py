from sqlalchemy import Column, Integer, String, Float
from app.database.connection import Base


class Train(Base):

    __tablename__ = "trains"

    id = Column(Integer, primary_key=True, index=True)

    train_number = Column(String, unique=True, nullable=False)

    train_name = Column(String, nullable=False)

    source = Column(String, nullable=False)

    destination = Column(String, nullable=False)

    departure_time = Column(String, nullable=False)

    arrival_time = Column(String, nullable=False)

    total_seats = Column(Integer, nullable=False)

    available_seats = Column(Integer, nullable=False)

    fare = Column(Float, nullable=False)