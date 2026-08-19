from sqlalchemy import Column, Integer, String
from app.database.connection import Base


class Passenger(Base):

    __tablename__ = "passengers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    age = Column(Integer, nullable=False)

    gender = Column(String, nullable=False)

    mobile = Column(String, nullable=False)